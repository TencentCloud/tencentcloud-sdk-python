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


class AlgorithmSpecification(AbstractModel):
    """算法配置

    """

    def __init__(self):
        r"""
        :param _TrainingImageName: 镜像名字
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingImageName: str
        :param _TrainingInputMode: 输入模式File|Pipe
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingInputMode: str
        :param _AlgorithmName: 算法名字
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgorithmName: str
        """
        self._TrainingImageName = None
        self._TrainingInputMode = None
        self._AlgorithmName = None

    @property
    def TrainingImageName(self):
        return self._TrainingImageName

    @TrainingImageName.setter
    def TrainingImageName(self, TrainingImageName):
        self._TrainingImageName = TrainingImageName

    @property
    def TrainingInputMode(self):
        return self._TrainingInputMode

    @TrainingInputMode.setter
    def TrainingInputMode(self, TrainingInputMode):
        self._TrainingInputMode = TrainingInputMode

    @property
    def AlgorithmName(self):
        return self._AlgorithmName

    @AlgorithmName.setter
    def AlgorithmName(self, AlgorithmName):
        self._AlgorithmName = AlgorithmName


    def _deserialize(self, params):
        self._TrainingImageName = params.get("TrainingImageName")
        self._TrainingInputMode = params.get("TrainingInputMode")
        self._AlgorithmName = params.get("AlgorithmName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillingLabel(AbstractModel):
    """计费标签

    """

    def __init__(self):
        r"""
        :param _Label: 计费项标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _VolumeSize: 存储大小
        :type VolumeSize: int
        :param _Status: 计费状态
None: 不计费
StorageOnly: 仅存储计费
Computing: 计算和存储都计费
        :type Status: str
        """
        self._Label = None
        self._VolumeSize = None
        self._Status = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def VolumeSize(self):
        return self._VolumeSize

    @VolumeSize.setter
    def VolumeSize(self, VolumeSize):
        self._VolumeSize = VolumeSize

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._VolumeSize = params.get("VolumeSize")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsConfig(AbstractModel):
    """接入CLS服务的配置

    """

    def __init__(self):
        r"""
        :param _Type: 接入类型，可选项为free、customer
        :type Type: str
        :param _LogSetId: 自定义CLS的日志集ID，只有当Type为customer时生效
        :type LogSetId: str
        :param _TopicId: 自定义CLS的日志主题ID，只有当Type为customer时生效
        :type TopicId: str
        """
        self._Type = None
        self._LogSetId = None
        self._TopicId = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LogSetId(self):
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._LogSetId = params.get("LogSetId")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeRepoSummary(AbstractModel):
    """存储库列表

    """

    def __init__(self):
        r"""
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _LastModifiedTime: 更新时间
        :type LastModifiedTime: str
        :param _CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param _GitConfig: Git配置
        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`
        :param _NoSecret: 是否有Git凭证
        :type NoSecret: bool
        """
        self._CreationTime = None
        self._LastModifiedTime = None
        self._CodeRepositoryName = None
        self._GitConfig = None
        self._NoSecret = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastModifiedTime(self):
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime

    @property
    def CodeRepositoryName(self):
        return self._CodeRepositoryName

    @CodeRepositoryName.setter
    def CodeRepositoryName(self, CodeRepositoryName):
        self._CodeRepositoryName = CodeRepositoryName

    @property
    def GitConfig(self):
        return self._GitConfig

    @GitConfig.setter
    def GitConfig(self, GitConfig):
        self._GitConfig = GitConfig

    @property
    def NoSecret(self):
        return self._NoSecret

    @NoSecret.setter
    def NoSecret(self, NoSecret):
        self._NoSecret = NoSecret


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._LastModifiedTime = params.get("LastModifiedTime")
        self._CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitConfig") is not None:
            self._GitConfig = GitConfig()
            self._GitConfig._deserialize(params.get("GitConfig"))
        self._NoSecret = params.get("NoSecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosDataSource(AbstractModel):
    """cos路径

    """

    def __init__(self):
        r"""
        :param _Bucket: cos桶
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param _KeyPrefix: cos文件key
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyPrefix: str
        :param _DataDistributionType: 分布式数据下载方式
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDistributionType: str
        :param _DataType: 数据类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DataType: str
        """
        self._Bucket = None
        self._KeyPrefix = None
        self._DataDistributionType = None
        self._DataType = None

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def KeyPrefix(self):
        return self._KeyPrefix

    @KeyPrefix.setter
    def KeyPrefix(self, KeyPrefix):
        self._KeyPrefix = KeyPrefix

    @property
    def DataDistributionType(self):
        return self._DataDistributionType

    @DataDistributionType.setter
    def DataDistributionType(self, DataDistributionType):
        self._DataDistributionType = DataDistributionType

    @property
    def DataType(self):
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._KeyPrefix = params.get("KeyPrefix")
        self._DataDistributionType = params.get("DataDistributionType")
        self._DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeRepositoryRequest(AbstractModel):
    """CreateCodeRepository请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param _GitConfig: Git相关配置
        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`
        :param _GitSecret: Git凭证
        :type GitSecret: :class:`tencentcloud.tione.v20191022.models.GitSecret`
        """
        self._CodeRepositoryName = None
        self._GitConfig = None
        self._GitSecret = None

    @property
    def CodeRepositoryName(self):
        return self._CodeRepositoryName

    @CodeRepositoryName.setter
    def CodeRepositoryName(self, CodeRepositoryName):
        self._CodeRepositoryName = CodeRepositoryName

    @property
    def GitConfig(self):
        return self._GitConfig

    @GitConfig.setter
    def GitConfig(self, GitConfig):
        self._GitConfig = GitConfig

    @property
    def GitSecret(self):
        return self._GitSecret

    @GitSecret.setter
    def GitSecret(self, GitSecret):
        self._GitSecret = GitSecret


    def _deserialize(self, params):
        self._CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitConfig") is not None:
            self._GitConfig = GitConfig()
            self._GitConfig._deserialize(params.get("GitConfig"))
        if params.get("GitSecret") is not None:
            self._GitSecret = GitSecret()
            self._GitSecret._deserialize(params.get("GitSecret"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeRepositoryResponse(AbstractModel):
    """CreateCodeRepository返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CodeRepositoryName = None
        self._RequestId = None

    @property
    def CodeRepositoryName(self):
        return self._CodeRepositoryName

    @CodeRepositoryName.setter
    def CodeRepositoryName(self, CodeRepositoryName):
        self._CodeRepositoryName = CodeRepositoryName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CodeRepositoryName = params.get("CodeRepositoryName")
        self._RequestId = params.get("RequestId")


class CreateNotebookInstanceRequest(AbstractModel):
    """CreateNotebookInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookInstanceName: Notebook实例名称，不能超过63个字符
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”
        :type NotebookInstanceName: str
        :param _InstanceType: Notebook算力类型
参考https://cloud.tencent.com/document/product/851/41239
        :type InstanceType: str
        :param _VolumeSizeInGB: 数据卷大小(GB)
用户持久化Notebook实例的数据
        :type VolumeSizeInGB: int
        :param _DirectInternetAccess: 外网访问权限，可取值Enabled/Disabled
开启后，Notebook实例可以具有访问外网80，443端口的权限
        :type DirectInternetAccess: str
        :param _RootAccess: Root用户权限，可取值Enabled/Disabled
开启后，Notebook实例可以切换至root用户执行命令
        :type RootAccess: str
        :param _SubnetId: 子网ID
如果需要Notebook实例访问VPC内的资源，则需要选择对应的子网
        :type SubnetId: str
        :param _LifecycleScriptsName: 生命周期脚本名称
必须是已存在的生命周期脚本，具体参考https://cloud.tencent.com/document/product/851/43140
        :type LifecycleScriptsName: str
        :param _DefaultCodeRepository: 默认存储库名称
可以是已创建的存储库名称或者已https://开头的公共git库
参考https://cloud.tencent.com/document/product/851/43139
        :type DefaultCodeRepository: str
        :param _AdditionalCodeRepositories: 其他存储库列表
每个元素可以是已创建的存储库名称或者已https://开头的公共git库
参考https://cloud.tencent.com/document/product/851/43139
        :type AdditionalCodeRepositories: list of str
        :param _ClsAccess: 已弃用，请使用ClsConfig配置。
是否开启CLS日志服务，可取值Enabled/Disabled，默认为Disabled
开启后，Notebook运行的日志会收集到CLS中，CLS会产生费用，请根据需要选择
        :type ClsAccess: str
        :param _StoppingCondition: 自动停止配置
选择定时停止Notebook实例
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param _AutoStopping: 自动停止，可取值Enabled/Disabled
取值为Disabled的时候StoppingCondition将被忽略
取值为Enabled的时候读取StoppingCondition作为自动停止的配置
        :type AutoStopping: str
        :param _ClsConfig: 接入日志的配置，默认接入免费日志
        :type ClsConfig: :class:`tencentcloud.tione.v20191022.models.ClsConfig`
        """
        self._NotebookInstanceName = None
        self._InstanceType = None
        self._VolumeSizeInGB = None
        self._DirectInternetAccess = None
        self._RootAccess = None
        self._SubnetId = None
        self._LifecycleScriptsName = None
        self._DefaultCodeRepository = None
        self._AdditionalCodeRepositories = None
        self._ClsAccess = None
        self._StoppingCondition = None
        self._AutoStopping = None
        self._ClsConfig = None

    @property
    def NotebookInstanceName(self):
        return self._NotebookInstanceName

    @NotebookInstanceName.setter
    def NotebookInstanceName(self, NotebookInstanceName):
        self._NotebookInstanceName = NotebookInstanceName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def VolumeSizeInGB(self):
        return self._VolumeSizeInGB

    @VolumeSizeInGB.setter
    def VolumeSizeInGB(self, VolumeSizeInGB):
        self._VolumeSizeInGB = VolumeSizeInGB

    @property
    def DirectInternetAccess(self):
        return self._DirectInternetAccess

    @DirectInternetAccess.setter
    def DirectInternetAccess(self, DirectInternetAccess):
        self._DirectInternetAccess = DirectInternetAccess

    @property
    def RootAccess(self):
        return self._RootAccess

    @RootAccess.setter
    def RootAccess(self, RootAccess):
        self._RootAccess = RootAccess

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def LifecycleScriptsName(self):
        return self._LifecycleScriptsName

    @LifecycleScriptsName.setter
    def LifecycleScriptsName(self, LifecycleScriptsName):
        self._LifecycleScriptsName = LifecycleScriptsName

    @property
    def DefaultCodeRepository(self):
        return self._DefaultCodeRepository

    @DefaultCodeRepository.setter
    def DefaultCodeRepository(self, DefaultCodeRepository):
        self._DefaultCodeRepository = DefaultCodeRepository

    @property
    def AdditionalCodeRepositories(self):
        return self._AdditionalCodeRepositories

    @AdditionalCodeRepositories.setter
    def AdditionalCodeRepositories(self, AdditionalCodeRepositories):
        self._AdditionalCodeRepositories = AdditionalCodeRepositories

    @property
    def ClsAccess(self):
        return self._ClsAccess

    @ClsAccess.setter
    def ClsAccess(self, ClsAccess):
        self._ClsAccess = ClsAccess

    @property
    def StoppingCondition(self):
        return self._StoppingCondition

    @StoppingCondition.setter
    def StoppingCondition(self, StoppingCondition):
        self._StoppingCondition = StoppingCondition

    @property
    def AutoStopping(self):
        return self._AutoStopping

    @AutoStopping.setter
    def AutoStopping(self, AutoStopping):
        self._AutoStopping = AutoStopping

    @property
    def ClsConfig(self):
        return self._ClsConfig

    @ClsConfig.setter
    def ClsConfig(self, ClsConfig):
        self._ClsConfig = ClsConfig


    def _deserialize(self, params):
        self._NotebookInstanceName = params.get("NotebookInstanceName")
        self._InstanceType = params.get("InstanceType")
        self._VolumeSizeInGB = params.get("VolumeSizeInGB")
        self._DirectInternetAccess = params.get("DirectInternetAccess")
        self._RootAccess = params.get("RootAccess")
        self._SubnetId = params.get("SubnetId")
        self._LifecycleScriptsName = params.get("LifecycleScriptsName")
        self._DefaultCodeRepository = params.get("DefaultCodeRepository")
        self._AdditionalCodeRepositories = params.get("AdditionalCodeRepositories")
        self._ClsAccess = params.get("ClsAccess")
        if params.get("StoppingCondition") is not None:
            self._StoppingCondition = StoppingCondition()
            self._StoppingCondition._deserialize(params.get("StoppingCondition"))
        self._AutoStopping = params.get("AutoStopping")
        if params.get("ClsConfig") is not None:
            self._ClsConfig = ClsConfig()
            self._ClsConfig._deserialize(params.get("ClsConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookInstanceResponse(AbstractModel):
    """CreateNotebookInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookInstanceName: Notebook实例名字
        :type NotebookInstanceName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookInstanceName = None
        self._RequestId = None

    @property
    def NotebookInstanceName(self):
        return self._NotebookInstanceName

    @NotebookInstanceName.setter
    def NotebookInstanceName(self, NotebookInstanceName):
        self._NotebookInstanceName = NotebookInstanceName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NotebookInstanceName = params.get("NotebookInstanceName")
        self._RequestId = params.get("RequestId")


class CreateNotebookLifecycleScriptRequest(AbstractModel):
    """CreateNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookLifecycleScriptsName: Notebook生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param _CreateScript: 创建脚本，base64编码
base64后的脚本长度不能超过16384个字符
        :type CreateScript: str
        :param _StartScript: 启动脚本，base64编码
base64后的脚本长度不能超过16384个字符
        :type StartScript: str
        """
        self._NotebookLifecycleScriptsName = None
        self._CreateScript = None
        self._StartScript = None

    @property
    def NotebookLifecycleScriptsName(self):
        return self._NotebookLifecycleScriptsName

    @NotebookLifecycleScriptsName.setter
    def NotebookLifecycleScriptsName(self, NotebookLifecycleScriptsName):
        self._NotebookLifecycleScriptsName = NotebookLifecycleScriptsName

    @property
    def CreateScript(self):
        return self._CreateScript

    @CreateScript.setter
    def CreateScript(self, CreateScript):
        self._CreateScript = CreateScript

    @property
    def StartScript(self):
        return self._StartScript

    @StartScript.setter
    def StartScript(self, StartScript):
        self._StartScript = StartScript


    def _deserialize(self, params):
        self._NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self._CreateScript = params.get("CreateScript")
        self._StartScript = params.get("StartScript")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookLifecycleScriptResponse(AbstractModel):
    """CreateNotebookLifecycleScript返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookLifecycleScriptsName: 生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookLifecycleScriptsName = None
        self._RequestId = None

    @property
    def NotebookLifecycleScriptsName(self):
        return self._NotebookLifecycleScriptsName

    @NotebookLifecycleScriptsName.setter
    def NotebookLifecycleScriptsName(self, NotebookLifecycleScriptsName):
        self._NotebookLifecycleScriptsName = NotebookLifecycleScriptsName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self._RequestId = params.get("RequestId")


class CreatePresignedNotebookInstanceUrlRequest(AbstractModel):
    """CreatePresignedNotebookInstanceUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookInstanceName: Notebook实例名称
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”
        :type NotebookInstanceName: str
        :param _SessionExpirationDurationInSeconds: session有效时间，秒，取值范围[1800, 43200]
        :type SessionExpirationDurationInSeconds: int
        """
        self._NotebookInstanceName = None
        self._SessionExpirationDurationInSeconds = None

    @property
    def NotebookInstanceName(self):
        return self._NotebookInstanceName

    @NotebookInstanceName.setter
    def NotebookInstanceName(self, NotebookInstanceName):
        self._NotebookInstanceName = NotebookInstanceName

    @property
    def SessionExpirationDurationInSeconds(self):
        return self._SessionExpirationDurationInSeconds

    @SessionExpirationDurationInSeconds.setter
    def SessionExpirationDurationInSeconds(self, SessionExpirationDurationInSeconds):
        self._SessionExpirationDurationInSeconds = SessionExpirationDurationInSeconds


    def _deserialize(self, params):
        self._NotebookInstanceName = params.get("NotebookInstanceName")
        self._SessionExpirationDurationInSeconds = params.get("SessionExpirationDurationInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePresignedNotebookInstanceUrlResponse(AbstractModel):
    """CreatePresignedNotebookInstanceUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthorizedUrl: 授权url
        :type AuthorizedUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuthorizedUrl = None
        self._RequestId = None

    @property
    def AuthorizedUrl(self):
        return self._AuthorizedUrl

    @AuthorizedUrl.setter
    def AuthorizedUrl(self, AuthorizedUrl):
        self._AuthorizedUrl = AuthorizedUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AuthorizedUrl = params.get("AuthorizedUrl")
        self._RequestId = params.get("RequestId")


class CreateTrainingJobRequest(AbstractModel):
    """CreateTrainingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlgorithmSpecification: 算法镜像配置
        :type AlgorithmSpecification: :class:`tencentcloud.tione.v20191022.models.AlgorithmSpecification`
        :param _OutputDataConfig: 输出数据配置
        :type OutputDataConfig: :class:`tencentcloud.tione.v20191022.models.OutputDataConfig`
        :param _ResourceConfig: 资源实例配置
        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`
        :param _TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        :param _InputDataConfig: 输入数据配置
        :type InputDataConfig: list of InputDataConfig
        :param _StoppingCondition: 中止条件
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param _VpcConfig: 私有网络配置
        :type VpcConfig: :class:`tencentcloud.tione.v20191022.models.VpcConfig`
        :param _HyperParameters: 算法超级参数
        :type HyperParameters: str
        :param _EnvConfig: 环境变量配置
        :type EnvConfig: list of EnvConfig
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _RetryWhenResourceInsufficient: 在资源不足（ResourceInsufficient）时后台不定时尝试重新创建训练任务。可取值Enabled/Disabled
默认值为Disabled即不重新尝试。设为Enabled时重新尝试有一定的时间期限，定义在 StoppingCondition 中 MaxWaitTimeInSecond中 ，默认值为1天，超过该期限创建失败。
        :type RetryWhenResourceInsufficient: str
        """
        self._AlgorithmSpecification = None
        self._OutputDataConfig = None
        self._ResourceConfig = None
        self._TrainingJobName = None
        self._InputDataConfig = None
        self._StoppingCondition = None
        self._VpcConfig = None
        self._HyperParameters = None
        self._EnvConfig = None
        self._RoleName = None
        self._RetryWhenResourceInsufficient = None

    @property
    def AlgorithmSpecification(self):
        return self._AlgorithmSpecification

    @AlgorithmSpecification.setter
    def AlgorithmSpecification(self, AlgorithmSpecification):
        self._AlgorithmSpecification = AlgorithmSpecification

    @property
    def OutputDataConfig(self):
        return self._OutputDataConfig

    @OutputDataConfig.setter
    def OutputDataConfig(self, OutputDataConfig):
        self._OutputDataConfig = OutputDataConfig

    @property
    def ResourceConfig(self):
        return self._ResourceConfig

    @ResourceConfig.setter
    def ResourceConfig(self, ResourceConfig):
        self._ResourceConfig = ResourceConfig

    @property
    def TrainingJobName(self):
        return self._TrainingJobName

    @TrainingJobName.setter
    def TrainingJobName(self, TrainingJobName):
        self._TrainingJobName = TrainingJobName

    @property
    def InputDataConfig(self):
        return self._InputDataConfig

    @InputDataConfig.setter
    def InputDataConfig(self, InputDataConfig):
        self._InputDataConfig = InputDataConfig

    @property
    def StoppingCondition(self):
        return self._StoppingCondition

    @StoppingCondition.setter
    def StoppingCondition(self, StoppingCondition):
        self._StoppingCondition = StoppingCondition

    @property
    def VpcConfig(self):
        return self._VpcConfig

    @VpcConfig.setter
    def VpcConfig(self, VpcConfig):
        self._VpcConfig = VpcConfig

    @property
    def HyperParameters(self):
        return self._HyperParameters

    @HyperParameters.setter
    def HyperParameters(self, HyperParameters):
        self._HyperParameters = HyperParameters

    @property
    def EnvConfig(self):
        return self._EnvConfig

    @EnvConfig.setter
    def EnvConfig(self, EnvConfig):
        self._EnvConfig = EnvConfig

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RetryWhenResourceInsufficient(self):
        return self._RetryWhenResourceInsufficient

    @RetryWhenResourceInsufficient.setter
    def RetryWhenResourceInsufficient(self, RetryWhenResourceInsufficient):
        self._RetryWhenResourceInsufficient = RetryWhenResourceInsufficient


    def _deserialize(self, params):
        if params.get("AlgorithmSpecification") is not None:
            self._AlgorithmSpecification = AlgorithmSpecification()
            self._AlgorithmSpecification._deserialize(params.get("AlgorithmSpecification"))
        if params.get("OutputDataConfig") is not None:
            self._OutputDataConfig = OutputDataConfig()
            self._OutputDataConfig._deserialize(params.get("OutputDataConfig"))
        if params.get("ResourceConfig") is not None:
            self._ResourceConfig = ResourceConfig()
            self._ResourceConfig._deserialize(params.get("ResourceConfig"))
        self._TrainingJobName = params.get("TrainingJobName")
        if params.get("InputDataConfig") is not None:
            self._InputDataConfig = []
            for item in params.get("InputDataConfig"):
                obj = InputDataConfig()
                obj._deserialize(item)
                self._InputDataConfig.append(obj)
        if params.get("StoppingCondition") is not None:
            self._StoppingCondition = StoppingCondition()
            self._StoppingCondition._deserialize(params.get("StoppingCondition"))
        if params.get("VpcConfig") is not None:
            self._VpcConfig = VpcConfig()
            self._VpcConfig._deserialize(params.get("VpcConfig"))
        self._HyperParameters = params.get("HyperParameters")
        if params.get("EnvConfig") is not None:
            self._EnvConfig = []
            for item in params.get("EnvConfig"):
                obj = EnvConfig()
                obj._deserialize(item)
                self._EnvConfig.append(obj)
        self._RoleName = params.get("RoleName")
        self._RetryWhenResourceInsufficient = params.get("RetryWhenResourceInsufficient")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrainingJobResponse(AbstractModel):
    """CreateTrainingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TrainingJobName = None
        self._RequestId = None

    @property
    def TrainingJobName(self):
        return self._TrainingJobName

    @TrainingJobName.setter
    def TrainingJobName(self, TrainingJobName):
        self._TrainingJobName = TrainingJobName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TrainingJobName = params.get("TrainingJobName")
        self._RequestId = params.get("RequestId")


class DataSource(AbstractModel):
    """数据源

    """

    def __init__(self):
        r"""
        :param _CosDataSource: cos数据源
注意：此字段可能返回 null，表示取不到有效值。
        :type CosDataSource: :class:`tencentcloud.tione.v20191022.models.CosDataSource`
        :param _FileSystemDataSource: 文件系统输入源
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemDataSource: :class:`tencentcloud.tione.v20191022.models.FileSystemDataSource`
        """
        self._CosDataSource = None
        self._FileSystemDataSource = None

    @property
    def CosDataSource(self):
        return self._CosDataSource

    @CosDataSource.setter
    def CosDataSource(self, CosDataSource):
        self._CosDataSource = CosDataSource

    @property
    def FileSystemDataSource(self):
        return self._FileSystemDataSource

    @FileSystemDataSource.setter
    def FileSystemDataSource(self, FileSystemDataSource):
        self._FileSystemDataSource = FileSystemDataSource


    def _deserialize(self, params):
        if params.get("CosDataSource") is not None:
            self._CosDataSource = CosDataSource()
            self._CosDataSource._deserialize(params.get("CosDataSource"))
        if params.get("FileSystemDataSource") is not None:
            self._FileSystemDataSource = FileSystemDataSource()
            self._FileSystemDataSource._deserialize(params.get("FileSystemDataSource"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeRepositoryRequest(AbstractModel):
    """DeleteCodeRepository请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        """
        self._CodeRepositoryName = None

    @property
    def CodeRepositoryName(self):
        return self._CodeRepositoryName

    @CodeRepositoryName.setter
    def CodeRepositoryName(self, CodeRepositoryName):
        self._CodeRepositoryName = CodeRepositoryName


    def _deserialize(self, params):
        self._CodeRepositoryName = params.get("CodeRepositoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeRepositoryResponse(AbstractModel):
    """DeleteCodeRepository返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CodeRepositoryName = None
        self._RequestId = None

    @property
    def CodeRepositoryName(self):
        return self._CodeRepositoryName

    @CodeRepositoryName.setter
    def CodeRepositoryName(self, CodeRepositoryName):
        self._CodeRepositoryName = CodeRepositoryName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CodeRepositoryName = params.get("CodeRepositoryName")
        self._RequestId = params.get("RequestId")


class DeleteNotebookInstanceRequest(AbstractModel):
    """DeleteNotebookInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        """
        self._NotebookInstanceName = None

    @property
    def NotebookInstanceName(self):
        return self._NotebookInstanceName

    @NotebookInstanceName.setter
    def NotebookInstanceName(self, NotebookInstanceName):
        self._NotebookInstanceName = NotebookInstanceName


    def _deserialize(self, params):
        self._NotebookInstanceName = params.get("NotebookInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNotebookInstanceResponse(AbstractModel):
    """DeleteNotebookInstance返回参数结构体

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


class DeleteNotebookLifecycleScriptRequest(AbstractModel):
    """DeleteNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookLifecycleScriptsName: 生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param _Forcible: 是否忽略已关联的 notebook 实例强行删除生命周期脚本，默认 false
        :type Forcible: bool
        """
        self._NotebookLifecycleScriptsName = None
        self._Forcible = None

    @property
    def NotebookLifecycleScriptsName(self):
        return self._NotebookLifecycleScriptsName

    @NotebookLifecycleScriptsName.setter
    def NotebookLifecycleScriptsName(self, NotebookLifecycleScriptsName):
        self._NotebookLifecycleScriptsName = NotebookLifecycleScriptsName

    @property
    def Forcible(self):
        return self._Forcible

    @Forcible.setter
    def Forcible(self, Forcible):
        self._Forcible = Forcible


    def _deserialize(self, params):
        self._NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self._Forcible = params.get("Forcible")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNotebookLifecycleScriptResponse(AbstractModel):
    """DeleteNotebookLifecycleScript返回参数结构体

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


class DescribeCodeRepositoriesRequest(AbstractModel):
    """DescribeCodeRepositories请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20
        :type Limit: int
        :param _Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。
        :type Filters: list of Filter
        :param _SortOrder: 排序规则。默认取Descending
Descending 按更新时间降序
Ascending 按更新时间升序
        :type SortOrder: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._SortOrder = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortOrder(self):
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodeRepositoriesResponse(AbstractModel):
    """DescribeCodeRepositories返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 存储库总数目
        :type TotalCount: int
        :param _CodeRepoSet: 存储库列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeRepoSet: list of CodeRepoSummary
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CodeRepoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CodeRepoSet(self):
        return self._CodeRepoSet

    @CodeRepoSet.setter
    def CodeRepoSet(self, CodeRepoSet):
        self._CodeRepoSet = CodeRepoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CodeRepoSet") is not None:
            self._CodeRepoSet = []
            for item in params.get("CodeRepoSet"):
                obj = CodeRepoSummary()
                obj._deserialize(item)
                self._CodeRepoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCodeRepositoryRequest(AbstractModel):
    """DescribeCodeRepository请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        """
        self._CodeRepositoryName = None

    @property
    def CodeRepositoryName(self):
        return self._CodeRepositoryName

    @CodeRepositoryName.setter
    def CodeRepositoryName(self, CodeRepositoryName):
        self._CodeRepositoryName = CodeRepositoryName


    def _deserialize(self, params):
        self._CodeRepositoryName = params.get("CodeRepositoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodeRepositoryResponse(AbstractModel):
    """DescribeCodeRepository返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _LastModifiedTime: 更新时间
        :type LastModifiedTime: str
        :param _CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param _GitConfig: Git存储配置
        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`
        :param _NoSecret: 是否有Git凭证
        :type NoSecret: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CreationTime = None
        self._LastModifiedTime = None
        self._CodeRepositoryName = None
        self._GitConfig = None
        self._NoSecret = None
        self._RequestId = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastModifiedTime(self):
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime

    @property
    def CodeRepositoryName(self):
        return self._CodeRepositoryName

    @CodeRepositoryName.setter
    def CodeRepositoryName(self, CodeRepositoryName):
        self._CodeRepositoryName = CodeRepositoryName

    @property
    def GitConfig(self):
        return self._GitConfig

    @GitConfig.setter
    def GitConfig(self, GitConfig):
        self._GitConfig = GitConfig

    @property
    def NoSecret(self):
        return self._NoSecret

    @NoSecret.setter
    def NoSecret(self, NoSecret):
        self._NoSecret = NoSecret

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._LastModifiedTime = params.get("LastModifiedTime")
        self._CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitConfig") is not None:
            self._GitConfig = GitConfig()
            self._GitConfig._deserialize(params.get("GitConfig"))
        self._NoSecret = params.get("NoSecret")
        self._RequestId = params.get("RequestId")


class DescribeNotebookInstanceRequest(AbstractModel):
    """DescribeNotebookInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookInstanceName: Notebook实例名称
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”
        :type NotebookInstanceName: str
        """
        self._NotebookInstanceName = None

    @property
    def NotebookInstanceName(self):
        return self._NotebookInstanceName

    @NotebookInstanceName.setter
    def NotebookInstanceName(self, NotebookInstanceName):
        self._NotebookInstanceName = NotebookInstanceName


    def _deserialize(self, params):
        self._NotebookInstanceName = params.get("NotebookInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookInstanceResponse(AbstractModel):
    """DescribeNotebookInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        :param _InstanceType: Notebook算力资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _RoleArn: 角色的资源描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleArn: str
        :param _DirectInternetAccess: 外网访问权限
注意：此字段可能返回 null，表示取不到有效值。
        :type DirectInternetAccess: str
        :param _RootAccess: Root用户权限
注意：此字段可能返回 null，表示取不到有效值。
        :type RootAccess: str
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _VolumeSizeInGB: 数据卷大小(GB)
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeSizeInGB: int
        :param _FailureReason: 创建失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param _CreationTime: Notebook实例创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param _LastModifiedTime: Notebook实例最近修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedTime: str
        :param _LogUrl: Notebook实例日志链接
注意：此字段可能返回 null，表示取不到有效值。
        :type LogUrl: str
        :param _NotebookInstanceStatus: Notebook实例状态

Pending: 创建中
Inservice: 运行中
Stopping: 停止中
Stopped: 已停止
Failed: 失败
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookInstanceStatus: str
        :param _InstanceId: Notebook实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _LifecycleScriptsName: notebook生命周期脚本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LifecycleScriptsName: str
        :param _DefaultCodeRepository: 默认存储库名称
可以是已创建的存储库名称或者已https://开头的公共git库
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultCodeRepository: str
        :param _AdditionalCodeRepositories: 其他存储库列表
每个元素可以是已创建的存储库名称或者已https://开头的公共git库
注意：此字段可能返回 null，表示取不到有效值。
        :type AdditionalCodeRepositories: list of str
        :param _ClsAccess: 是否开启CLS日志服务
注意：此字段可能返回 null，表示取不到有效值。
        :type ClsAccess: str
        :param _Prepay: 是否预付费实例
注意：此字段可能返回 null，表示取不到有效值。
        :type Prepay: bool
        :param _Deadline: 实例运行截止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Deadline: str
        :param _StoppingCondition: 自动停止配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param _ClsConfig: Cls配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ClsConfig: :class:`tencentcloud.tione.v20191022.models.ClsConfig`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookInstanceName = None
        self._InstanceType = None
        self._RoleArn = None
        self._DirectInternetAccess = None
        self._RootAccess = None
        self._SubnetId = None
        self._VolumeSizeInGB = None
        self._FailureReason = None
        self._CreationTime = None
        self._LastModifiedTime = None
        self._LogUrl = None
        self._NotebookInstanceStatus = None
        self._InstanceId = None
        self._LifecycleScriptsName = None
        self._DefaultCodeRepository = None
        self._AdditionalCodeRepositories = None
        self._ClsAccess = None
        self._Prepay = None
        self._Deadline = None
        self._StoppingCondition = None
        self._ClsConfig = None
        self._RequestId = None

    @property
    def NotebookInstanceName(self):
        return self._NotebookInstanceName

    @NotebookInstanceName.setter
    def NotebookInstanceName(self, NotebookInstanceName):
        self._NotebookInstanceName = NotebookInstanceName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def RoleArn(self):
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def DirectInternetAccess(self):
        return self._DirectInternetAccess

    @DirectInternetAccess.setter
    def DirectInternetAccess(self, DirectInternetAccess):
        self._DirectInternetAccess = DirectInternetAccess

    @property
    def RootAccess(self):
        return self._RootAccess

    @RootAccess.setter
    def RootAccess(self, RootAccess):
        self._RootAccess = RootAccess

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VolumeSizeInGB(self):
        return self._VolumeSizeInGB

    @VolumeSizeInGB.setter
    def VolumeSizeInGB(self, VolumeSizeInGB):
        self._VolumeSizeInGB = VolumeSizeInGB

    @property
    def FailureReason(self):
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastModifiedTime(self):
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime

    @property
    def LogUrl(self):
        return self._LogUrl

    @LogUrl.setter
    def LogUrl(self, LogUrl):
        self._LogUrl = LogUrl

    @property
    def NotebookInstanceStatus(self):
        return self._NotebookInstanceStatus

    @NotebookInstanceStatus.setter
    def NotebookInstanceStatus(self, NotebookInstanceStatus):
        self._NotebookInstanceStatus = NotebookInstanceStatus

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LifecycleScriptsName(self):
        return self._LifecycleScriptsName

    @LifecycleScriptsName.setter
    def LifecycleScriptsName(self, LifecycleScriptsName):
        self._LifecycleScriptsName = LifecycleScriptsName

    @property
    def DefaultCodeRepository(self):
        return self._DefaultCodeRepository

    @DefaultCodeRepository.setter
    def DefaultCodeRepository(self, DefaultCodeRepository):
        self._DefaultCodeRepository = DefaultCodeRepository

    @property
    def AdditionalCodeRepositories(self):
        return self._AdditionalCodeRepositories

    @AdditionalCodeRepositories.setter
    def AdditionalCodeRepositories(self, AdditionalCodeRepositories):
        self._AdditionalCodeRepositories = AdditionalCodeRepositories

    @property
    def ClsAccess(self):
        return self._ClsAccess

    @ClsAccess.setter
    def ClsAccess(self, ClsAccess):
        self._ClsAccess = ClsAccess

    @property
    def Prepay(self):
        return self._Prepay

    @Prepay.setter
    def Prepay(self, Prepay):
        self._Prepay = Prepay

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def StoppingCondition(self):
        return self._StoppingCondition

    @StoppingCondition.setter
    def StoppingCondition(self, StoppingCondition):
        self._StoppingCondition = StoppingCondition

    @property
    def ClsConfig(self):
        return self._ClsConfig

    @ClsConfig.setter
    def ClsConfig(self, ClsConfig):
        self._ClsConfig = ClsConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NotebookInstanceName = params.get("NotebookInstanceName")
        self._InstanceType = params.get("InstanceType")
        self._RoleArn = params.get("RoleArn")
        self._DirectInternetAccess = params.get("DirectInternetAccess")
        self._RootAccess = params.get("RootAccess")
        self._SubnetId = params.get("SubnetId")
        self._VolumeSizeInGB = params.get("VolumeSizeInGB")
        self._FailureReason = params.get("FailureReason")
        self._CreationTime = params.get("CreationTime")
        self._LastModifiedTime = params.get("LastModifiedTime")
        self._LogUrl = params.get("LogUrl")
        self._NotebookInstanceStatus = params.get("NotebookInstanceStatus")
        self._InstanceId = params.get("InstanceId")
        self._LifecycleScriptsName = params.get("LifecycleScriptsName")
        self._DefaultCodeRepository = params.get("DefaultCodeRepository")
        self._AdditionalCodeRepositories = params.get("AdditionalCodeRepositories")
        self._ClsAccess = params.get("ClsAccess")
        self._Prepay = params.get("Prepay")
        self._Deadline = params.get("Deadline")
        if params.get("StoppingCondition") is not None:
            self._StoppingCondition = StoppingCondition()
            self._StoppingCondition._deserialize(params.get("StoppingCondition"))
        if params.get("ClsConfig") is not None:
            self._ClsConfig = ClsConfig()
            self._ClsConfig._deserialize(params.get("ClsConfig"))
        self._RequestId = params.get("RequestId")


class DescribeNotebookInstancesRequest(AbstractModel):
    """DescribeNotebookInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _SortOrder: 排序规则。默认取Descending
Descending 按更新时间降序
Ascending 按更新时间升序
        :type SortOrder: str
        :param _Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。
lifecycle-name - String - 是否必填：否 -（过滤条件）按照生命周期脚本名称过滤。
default-code-repo-name - String - 是否必填：否 -（过滤条件）按照默认存储库名称过滤。
additional-code-repo-name - String - 是否必填：否 -（过滤条件）按照其他存储库名称过滤。
billing-status - String - 是否必填：否 - （过滤条件）按照计费状态过滤，可取以下值
   StorageOnly：仅存储计费的实例
   Computing：计算和存储都计费的实例
        :type Filters: list of Filter
        :param _SortBy: 【废弃字段】排序字段
        :type SortBy: str
        """
        self._Offset = None
        self._Limit = None
        self._SortOrder = None
        self._Filters = None
        self._SortBy = None

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
    def SortOrder(self):
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SortOrder = params.get("SortOrder")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortBy = params.get("SortBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookInstancesResponse(AbstractModel):
    """DescribeNotebookInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookInstanceSet: Notebook实例列表
        :type NotebookInstanceSet: list of NotebookInstanceSummary
        :param _TotalCount: Notebook实例总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookInstanceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NotebookInstanceSet(self):
        return self._NotebookInstanceSet

    @NotebookInstanceSet.setter
    def NotebookInstanceSet(self, NotebookInstanceSet):
        self._NotebookInstanceSet = NotebookInstanceSet

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
        if params.get("NotebookInstanceSet") is not None:
            self._NotebookInstanceSet = []
            for item in params.get("NotebookInstanceSet"):
                obj = NotebookInstanceSummary()
                obj._deserialize(item)
                self._NotebookInstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNotebookLifecycleScriptRequest(AbstractModel):
    """DescribeNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookLifecycleScriptsName: 生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        """
        self._NotebookLifecycleScriptsName = None

    @property
    def NotebookLifecycleScriptsName(self):
        return self._NotebookLifecycleScriptsName

    @NotebookLifecycleScriptsName.setter
    def NotebookLifecycleScriptsName(self, NotebookLifecycleScriptsName):
        self._NotebookLifecycleScriptsName = NotebookLifecycleScriptsName


    def _deserialize(self, params):
        self._NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookLifecycleScriptResponse(AbstractModel):
    """DescribeNotebookLifecycleScript返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookLifecycleScriptsName: 生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param _CreateScript: 创建脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateScript: str
        :param _StartScript: 启动脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type StartScript: str
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _LastModifiedTime: 最后修改时间
        :type LastModifiedTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookLifecycleScriptsName = None
        self._CreateScript = None
        self._StartScript = None
        self._CreationTime = None
        self._LastModifiedTime = None
        self._RequestId = None

    @property
    def NotebookLifecycleScriptsName(self):
        return self._NotebookLifecycleScriptsName

    @NotebookLifecycleScriptsName.setter
    def NotebookLifecycleScriptsName(self, NotebookLifecycleScriptsName):
        self._NotebookLifecycleScriptsName = NotebookLifecycleScriptsName

    @property
    def CreateScript(self):
        return self._CreateScript

    @CreateScript.setter
    def CreateScript(self, CreateScript):
        self._CreateScript = CreateScript

    @property
    def StartScript(self):
        return self._StartScript

    @StartScript.setter
    def StartScript(self, StartScript):
        self._StartScript = StartScript

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastModifiedTime(self):
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self._CreateScript = params.get("CreateScript")
        self._StartScript = params.get("StartScript")
        self._CreationTime = params.get("CreationTime")
        self._LastModifiedTime = params.get("LastModifiedTime")
        self._RequestId = params.get("RequestId")


class DescribeNotebookLifecycleScriptsRequest(AbstractModel):
    """DescribeNotebookLifecycleScripts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20
        :type Limit: int
        :param _Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。
        :type Filters: list of Filter
        :param _SortOrder: 排序规则。默认取Descending
Descending 按更新时间降序
Ascending 按更新时间升序
        :type SortOrder: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._SortOrder = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortOrder(self):
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookLifecycleScriptsResponse(AbstractModel):
    """DescribeNotebookLifecycleScripts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookLifecycleScriptsSet: Notebook生命周期脚本列表
        :type NotebookLifecycleScriptsSet: list of NotebookLifecycleScriptsSummary
        :param _TotalCount: Notebook生命周期脚本总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookLifecycleScriptsSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NotebookLifecycleScriptsSet(self):
        return self._NotebookLifecycleScriptsSet

    @NotebookLifecycleScriptsSet.setter
    def NotebookLifecycleScriptsSet(self, NotebookLifecycleScriptsSet):
        self._NotebookLifecycleScriptsSet = NotebookLifecycleScriptsSet

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
        if params.get("NotebookLifecycleScriptsSet") is not None:
            self._NotebookLifecycleScriptsSet = []
            for item in params.get("NotebookLifecycleScriptsSet"):
                obj = NotebookLifecycleScriptsSummary()
                obj._deserialize(item)
                self._NotebookLifecycleScriptsSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNotebookSummaryRequest(AbstractModel):
    """DescribeNotebookSummary请求参数结构体

    """


class DescribeNotebookSummaryResponse(AbstractModel):
    """DescribeNotebookSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AllInstanceCnt: 实例总数
        :type AllInstanceCnt: int
        :param _BillingInstanceCnt: 计费实例总数
        :type BillingInstanceCnt: int
        :param _StorageOnlyBillingInstanceCnt: 仅存储计费的实例总数
        :type StorageOnlyBillingInstanceCnt: int
        :param _ComputingBillingInstanceCnt: 计算和存储都计费的实例总数
        :type ComputingBillingInstanceCnt: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AllInstanceCnt = None
        self._BillingInstanceCnt = None
        self._StorageOnlyBillingInstanceCnt = None
        self._ComputingBillingInstanceCnt = None
        self._RequestId = None

    @property
    def AllInstanceCnt(self):
        return self._AllInstanceCnt

    @AllInstanceCnt.setter
    def AllInstanceCnt(self, AllInstanceCnt):
        self._AllInstanceCnt = AllInstanceCnt

    @property
    def BillingInstanceCnt(self):
        return self._BillingInstanceCnt

    @BillingInstanceCnt.setter
    def BillingInstanceCnt(self, BillingInstanceCnt):
        self._BillingInstanceCnt = BillingInstanceCnt

    @property
    def StorageOnlyBillingInstanceCnt(self):
        return self._StorageOnlyBillingInstanceCnt

    @StorageOnlyBillingInstanceCnt.setter
    def StorageOnlyBillingInstanceCnt(self, StorageOnlyBillingInstanceCnt):
        self._StorageOnlyBillingInstanceCnt = StorageOnlyBillingInstanceCnt

    @property
    def ComputingBillingInstanceCnt(self):
        return self._ComputingBillingInstanceCnt

    @ComputingBillingInstanceCnt.setter
    def ComputingBillingInstanceCnt(self, ComputingBillingInstanceCnt):
        self._ComputingBillingInstanceCnt = ComputingBillingInstanceCnt

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AllInstanceCnt = params.get("AllInstanceCnt")
        self._BillingInstanceCnt = params.get("BillingInstanceCnt")
        self._StorageOnlyBillingInstanceCnt = params.get("StorageOnlyBillingInstanceCnt")
        self._ComputingBillingInstanceCnt = params.get("ComputingBillingInstanceCnt")
        self._RequestId = params.get("RequestId")


class DescribeTrainingJobRequest(AbstractModel):
    """DescribeTrainingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        """
        self._TrainingJobName = None

    @property
    def TrainingJobName(self):
        return self._TrainingJobName

    @TrainingJobName.setter
    def TrainingJobName(self, TrainingJobName):
        self._TrainingJobName = TrainingJobName


    def _deserialize(self, params):
        self._TrainingJobName = params.get("TrainingJobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingJobResponse(AbstractModel):
    """DescribeTrainingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlgorithmSpecification: 算法镜像配置
        :type AlgorithmSpecification: :class:`tencentcloud.tione.v20191022.models.AlgorithmSpecification`
        :param _TrainingJobName: 任务名称
        :type TrainingJobName: str
        :param _HyperParameters: 算法超级参数
注意：此字段可能返回 null，表示取不到有效值。
        :type HyperParameters: str
        :param _InputDataConfig: 输入数据配置
        :type InputDataConfig: list of InputDataConfig
        :param _OutputDataConfig: 输出数据配置
        :type OutputDataConfig: :class:`tencentcloud.tione.v20191022.models.OutputDataConfig`
        :param _StoppingCondition: 中止条件
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param _ResourceConfig: 计算实例配置
        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`
        :param _VpcConfig: 私有网络配置
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcConfig: :class:`tencentcloud.tione.v20191022.models.VpcConfig`
        :param _FailureReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param _LastModifiedTime: 最近修改时间
        :type LastModifiedTime: str
        :param _TrainingStartTime: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingStartTime: str
        :param _TrainingEndTime: 任务完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingEndTime: str
        :param _ModelArtifacts: 模型输出配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelArtifacts: :class:`tencentcloud.tione.v20191022.models.ModelArtifacts`
        :param _SecondaryStatus: 详细状态，取值范围
Starting：启动中
Downloading: 准备训练数据
Training: 正在训练
Uploading: 上传训练结果
Completed：已完成
Failed: 失败
MaxRuntimeExceeded: 任务超过最大运行时间
Stopping: 停止中
Stopped：已停止
        :type SecondaryStatus: str
        :param _SecondaryStatusTransitions: 详细状态事件记录
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondaryStatusTransitions: list of SecondaryStatusTransition
        :param _RoleName: 角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        :param _TrainingJobStatus: 训练任务状态，取值范围
InProgress：运行中
Completed: 已完成
Failed: 失败
Stopping: 停止中
Stopped：已停止
        :type TrainingJobStatus: str
        :param _LogUrl: 训练任务日志链接
注意：此字段可能返回 null，表示取不到有效值。
        :type LogUrl: str
        :param _InstanceId: 训练任务实例ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlgorithmSpecification = None
        self._TrainingJobName = None
        self._HyperParameters = None
        self._InputDataConfig = None
        self._OutputDataConfig = None
        self._StoppingCondition = None
        self._ResourceConfig = None
        self._VpcConfig = None
        self._FailureReason = None
        self._LastModifiedTime = None
        self._TrainingStartTime = None
        self._TrainingEndTime = None
        self._ModelArtifacts = None
        self._SecondaryStatus = None
        self._SecondaryStatusTransitions = None
        self._RoleName = None
        self._TrainingJobStatus = None
        self._LogUrl = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def AlgorithmSpecification(self):
        return self._AlgorithmSpecification

    @AlgorithmSpecification.setter
    def AlgorithmSpecification(self, AlgorithmSpecification):
        self._AlgorithmSpecification = AlgorithmSpecification

    @property
    def TrainingJobName(self):
        return self._TrainingJobName

    @TrainingJobName.setter
    def TrainingJobName(self, TrainingJobName):
        self._TrainingJobName = TrainingJobName

    @property
    def HyperParameters(self):
        return self._HyperParameters

    @HyperParameters.setter
    def HyperParameters(self, HyperParameters):
        self._HyperParameters = HyperParameters

    @property
    def InputDataConfig(self):
        return self._InputDataConfig

    @InputDataConfig.setter
    def InputDataConfig(self, InputDataConfig):
        self._InputDataConfig = InputDataConfig

    @property
    def OutputDataConfig(self):
        return self._OutputDataConfig

    @OutputDataConfig.setter
    def OutputDataConfig(self, OutputDataConfig):
        self._OutputDataConfig = OutputDataConfig

    @property
    def StoppingCondition(self):
        return self._StoppingCondition

    @StoppingCondition.setter
    def StoppingCondition(self, StoppingCondition):
        self._StoppingCondition = StoppingCondition

    @property
    def ResourceConfig(self):
        return self._ResourceConfig

    @ResourceConfig.setter
    def ResourceConfig(self, ResourceConfig):
        self._ResourceConfig = ResourceConfig

    @property
    def VpcConfig(self):
        return self._VpcConfig

    @VpcConfig.setter
    def VpcConfig(self, VpcConfig):
        self._VpcConfig = VpcConfig

    @property
    def FailureReason(self):
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def LastModifiedTime(self):
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime

    @property
    def TrainingStartTime(self):
        return self._TrainingStartTime

    @TrainingStartTime.setter
    def TrainingStartTime(self, TrainingStartTime):
        self._TrainingStartTime = TrainingStartTime

    @property
    def TrainingEndTime(self):
        return self._TrainingEndTime

    @TrainingEndTime.setter
    def TrainingEndTime(self, TrainingEndTime):
        self._TrainingEndTime = TrainingEndTime

    @property
    def ModelArtifacts(self):
        return self._ModelArtifacts

    @ModelArtifacts.setter
    def ModelArtifacts(self, ModelArtifacts):
        self._ModelArtifacts = ModelArtifacts

    @property
    def SecondaryStatus(self):
        return self._SecondaryStatus

    @SecondaryStatus.setter
    def SecondaryStatus(self, SecondaryStatus):
        self._SecondaryStatus = SecondaryStatus

    @property
    def SecondaryStatusTransitions(self):
        return self._SecondaryStatusTransitions

    @SecondaryStatusTransitions.setter
    def SecondaryStatusTransitions(self, SecondaryStatusTransitions):
        self._SecondaryStatusTransitions = SecondaryStatusTransitions

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def TrainingJobStatus(self):
        return self._TrainingJobStatus

    @TrainingJobStatus.setter
    def TrainingJobStatus(self, TrainingJobStatus):
        self._TrainingJobStatus = TrainingJobStatus

    @property
    def LogUrl(self):
        return self._LogUrl

    @LogUrl.setter
    def LogUrl(self, LogUrl):
        self._LogUrl = LogUrl

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AlgorithmSpecification") is not None:
            self._AlgorithmSpecification = AlgorithmSpecification()
            self._AlgorithmSpecification._deserialize(params.get("AlgorithmSpecification"))
        self._TrainingJobName = params.get("TrainingJobName")
        self._HyperParameters = params.get("HyperParameters")
        if params.get("InputDataConfig") is not None:
            self._InputDataConfig = []
            for item in params.get("InputDataConfig"):
                obj = InputDataConfig()
                obj._deserialize(item)
                self._InputDataConfig.append(obj)
        if params.get("OutputDataConfig") is not None:
            self._OutputDataConfig = OutputDataConfig()
            self._OutputDataConfig._deserialize(params.get("OutputDataConfig"))
        if params.get("StoppingCondition") is not None:
            self._StoppingCondition = StoppingCondition()
            self._StoppingCondition._deserialize(params.get("StoppingCondition"))
        if params.get("ResourceConfig") is not None:
            self._ResourceConfig = ResourceConfig()
            self._ResourceConfig._deserialize(params.get("ResourceConfig"))
        if params.get("VpcConfig") is not None:
            self._VpcConfig = VpcConfig()
            self._VpcConfig._deserialize(params.get("VpcConfig"))
        self._FailureReason = params.get("FailureReason")
        self._LastModifiedTime = params.get("LastModifiedTime")
        self._TrainingStartTime = params.get("TrainingStartTime")
        self._TrainingEndTime = params.get("TrainingEndTime")
        if params.get("ModelArtifacts") is not None:
            self._ModelArtifacts = ModelArtifacts()
            self._ModelArtifacts._deserialize(params.get("ModelArtifacts"))
        self._SecondaryStatus = params.get("SecondaryStatus")
        if params.get("SecondaryStatusTransitions") is not None:
            self._SecondaryStatusTransitions = []
            for item in params.get("SecondaryStatusTransitions"):
                obj = SecondaryStatusTransition()
                obj._deserialize(item)
                self._SecondaryStatusTransitions.append(obj)
        self._RoleName = params.get("RoleName")
        self._TrainingJobStatus = params.get("TrainingJobStatus")
        self._LogUrl = params.get("LogUrl")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DescribeTrainingJobsRequest(AbstractModel):
    """DescribeTrainingJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _CreationTimeAfter: 创建时间晚于
        :type CreationTimeAfter: str
        :param _CreationTimeBefore: 创建时间早于
        :type CreationTimeBefore: str
        :param _NameContains: 根据名称过滤
        :type NameContains: str
        :param _StatusEquals: 根据状态过滤
        :type StatusEquals: str
        :param _Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._CreationTimeAfter = None
        self._CreationTimeBefore = None
        self._NameContains = None
        self._StatusEquals = None
        self._Filters = None

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
    def CreationTimeAfter(self):
        return self._CreationTimeAfter

    @CreationTimeAfter.setter
    def CreationTimeAfter(self, CreationTimeAfter):
        self._CreationTimeAfter = CreationTimeAfter

    @property
    def CreationTimeBefore(self):
        return self._CreationTimeBefore

    @CreationTimeBefore.setter
    def CreationTimeBefore(self, CreationTimeBefore):
        self._CreationTimeBefore = CreationTimeBefore

    @property
    def NameContains(self):
        return self._NameContains

    @NameContains.setter
    def NameContains(self, NameContains):
        self._NameContains = NameContains

    @property
    def StatusEquals(self):
        return self._StatusEquals

    @StatusEquals.setter
    def StatusEquals(self, StatusEquals):
        self._StatusEquals = StatusEquals

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CreationTimeAfter = params.get("CreationTimeAfter")
        self._CreationTimeBefore = params.get("CreationTimeBefore")
        self._NameContains = params.get("NameContains")
        self._StatusEquals = params.get("StatusEquals")
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
        


class DescribeTrainingJobsResponse(AbstractModel):
    """DescribeTrainingJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingJobSet: 训练任务列表
        :type TrainingJobSet: list of TrainingJobSummary
        :param _TotalCount: 训练任务总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TrainingJobSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TrainingJobSet(self):
        return self._TrainingJobSet

    @TrainingJobSet.setter
    def TrainingJobSet(self, TrainingJobSet):
        self._TrainingJobSet = TrainingJobSet

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
        if params.get("TrainingJobSet") is not None:
            self._TrainingJobSet = []
            for item in params.get("TrainingJobSet"):
                obj = TrainingJobSummary()
                obj._deserialize(item)
                self._TrainingJobSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class EnvConfig(AbstractModel):
    """环境变量

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Value: 值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSystemDataSource(AbstractModel):
    """文件系统输入数据源

    """

    def __init__(self):
        r"""
        :param _DirectoryPath: 文件系统目录
注意：此字段可能返回 null，表示取不到有效值。
        :type DirectoryPath: str
        :param _FileSystemType: 文件系统类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemType: str
        :param _FileSystemAccessMode: 文件系统访问模式
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemAccessMode: str
        :param _FileSystemId: 文件系统ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemId: str
        """
        self._DirectoryPath = None
        self._FileSystemType = None
        self._FileSystemAccessMode = None
        self._FileSystemId = None

    @property
    def DirectoryPath(self):
        return self._DirectoryPath

    @DirectoryPath.setter
    def DirectoryPath(self, DirectoryPath):
        self._DirectoryPath = DirectoryPath

    @property
    def FileSystemType(self):
        return self._FileSystemType

    @FileSystemType.setter
    def FileSystemType(self, FileSystemType):
        self._FileSystemType = FileSystemType

    @property
    def FileSystemAccessMode(self):
        return self._FileSystemAccessMode

    @FileSystemAccessMode.setter
    def FileSystemAccessMode(self, FileSystemAccessMode):
        self._FileSystemAccessMode = FileSystemAccessMode

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._DirectoryPath = params.get("DirectoryPath")
        self._FileSystemType = params.get("FileSystemType")
        self._FileSystemAccessMode = params.get("FileSystemAccessMode")
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段名称
        :type Name: str
        :param _Values: 过滤字段取值
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
        


class GitConfig(AbstractModel):
    """存储库Git相关配置

    """

    def __init__(self):
        r"""
        :param _RepositoryUrl: git地址
        :type RepositoryUrl: str
        :param _Branch: 代码分支
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        """
        self._RepositoryUrl = None
        self._Branch = None

    @property
    def RepositoryUrl(self):
        return self._RepositoryUrl

    @RepositoryUrl.setter
    def RepositoryUrl(self, RepositoryUrl):
        self._RepositoryUrl = RepositoryUrl

    @property
    def Branch(self):
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch


    def _deserialize(self, params):
        self._RepositoryUrl = params.get("RepositoryUrl")
        self._Branch = params.get("Branch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GitSecret(AbstractModel):
    """Git凭证

    """

    def __init__(self):
        r"""
        :param _NoSecret: 无秘钥，默认选项
        :type NoSecret: bool
        :param _Secret: Git用户名密码base64编码后的字符串
编码前的内容应为Json字符串，如
{"UserName": "用户名", "Password":"密码"}
        :type Secret: str
        """
        self._NoSecret = None
        self._Secret = None

    @property
    def NoSecret(self):
        return self._NoSecret

    @NoSecret.setter
    def NoSecret(self, NoSecret):
        self._NoSecret = NoSecret

    @property
    def Secret(self):
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret


    def _deserialize(self, params):
        self._NoSecret = params.get("NoSecret")
        self._Secret = params.get("Secret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputDataConfig(AbstractModel):
    """输入数据配置

    """

    def __init__(self):
        r"""
        :param _ChannelName: 通道名
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelName: str
        :param _DataSource: 数据源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: :class:`tencentcloud.tione.v20191022.models.DataSource`
        :param _InputMode: 输入类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InputMode: str
        :param _ContentType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentType: str
        """
        self._ChannelName = None
        self._DataSource = None
        self._InputMode = None
        self._ContentType = None

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def InputMode(self):
        return self._InputMode

    @InputMode.setter
    def InputMode(self, InputMode):
        self._InputMode = InputMode

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType


    def _deserialize(self, params):
        self._ChannelName = params.get("ChannelName")
        if params.get("DataSource") is not None:
            self._DataSource = DataSource()
            self._DataSource._deserialize(params.get("DataSource"))
        self._InputMode = params.get("InputMode")
        self._ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelArtifacts(AbstractModel):
    """模型输出

    """

    def __init__(self):
        r"""
        :param _CosModelArtifacts: cos输出路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CosModelArtifacts: str
        """
        self._CosModelArtifacts = None

    @property
    def CosModelArtifacts(self):
        return self._CosModelArtifacts

    @CosModelArtifacts.setter
    def CosModelArtifacts(self, CosModelArtifacts):
        self._CosModelArtifacts = CosModelArtifacts


    def _deserialize(self, params):
        self._CosModelArtifacts = params.get("CosModelArtifacts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookInstanceSummary(AbstractModel):
    """notebook实例概览

    """

    def __init__(self):
        r"""
        :param _CreationTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param _LastModifiedTime: 最近修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedTime: str
        :param _NotebookInstanceName: notebook实例名字
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookInstanceName: str
        :param _NotebookInstanceStatus: notebook实例状态，取值范围：
Pending: 创建中
Inservice: 运行中
Stopping: 停止中
Stopped: 已停止
Failed: 失败
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookInstanceStatus: str
        :param _InstanceType: 算力类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _StartupTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartupTime: str
        :param _Deadline: 运行截止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Deadline: str
        :param _StoppingCondition: 自动停止配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param _Prepay: 是否是预付费实例
注意：此字段可能返回 null，表示取不到有效值。
        :type Prepay: bool
        :param _BillingLabel: 计费标识
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingLabel: :class:`tencentcloud.tione.v20191022.models.BillingLabel`
        :param _RuntimeInSeconds: 运行时长，秒
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param _RemainTimeInSeconds: 剩余时长，秒
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainTimeInSeconds: int
        """
        self._CreationTime = None
        self._LastModifiedTime = None
        self._NotebookInstanceName = None
        self._NotebookInstanceStatus = None
        self._InstanceType = None
        self._InstanceId = None
        self._StartupTime = None
        self._Deadline = None
        self._StoppingCondition = None
        self._Prepay = None
        self._BillingLabel = None
        self._RuntimeInSeconds = None
        self._RemainTimeInSeconds = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastModifiedTime(self):
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime

    @property
    def NotebookInstanceName(self):
        return self._NotebookInstanceName

    @NotebookInstanceName.setter
    def NotebookInstanceName(self, NotebookInstanceName):
        self._NotebookInstanceName = NotebookInstanceName

    @property
    def NotebookInstanceStatus(self):
        return self._NotebookInstanceStatus

    @NotebookInstanceStatus.setter
    def NotebookInstanceStatus(self, NotebookInstanceStatus):
        self._NotebookInstanceStatus = NotebookInstanceStatus

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartupTime(self):
        return self._StartupTime

    @StartupTime.setter
    def StartupTime(self, StartupTime):
        self._StartupTime = StartupTime

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def StoppingCondition(self):
        return self._StoppingCondition

    @StoppingCondition.setter
    def StoppingCondition(self, StoppingCondition):
        self._StoppingCondition = StoppingCondition

    @property
    def Prepay(self):
        return self._Prepay

    @Prepay.setter
    def Prepay(self, Prepay):
        self._Prepay = Prepay

    @property
    def BillingLabel(self):
        return self._BillingLabel

    @BillingLabel.setter
    def BillingLabel(self, BillingLabel):
        self._BillingLabel = BillingLabel

    @property
    def RuntimeInSeconds(self):
        return self._RuntimeInSeconds

    @RuntimeInSeconds.setter
    def RuntimeInSeconds(self, RuntimeInSeconds):
        self._RuntimeInSeconds = RuntimeInSeconds

    @property
    def RemainTimeInSeconds(self):
        return self._RemainTimeInSeconds

    @RemainTimeInSeconds.setter
    def RemainTimeInSeconds(self, RemainTimeInSeconds):
        self._RemainTimeInSeconds = RemainTimeInSeconds


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._LastModifiedTime = params.get("LastModifiedTime")
        self._NotebookInstanceName = params.get("NotebookInstanceName")
        self._NotebookInstanceStatus = params.get("NotebookInstanceStatus")
        self._InstanceType = params.get("InstanceType")
        self._InstanceId = params.get("InstanceId")
        self._StartupTime = params.get("StartupTime")
        self._Deadline = params.get("Deadline")
        if params.get("StoppingCondition") is not None:
            self._StoppingCondition = StoppingCondition()
            self._StoppingCondition._deserialize(params.get("StoppingCondition"))
        self._Prepay = params.get("Prepay")
        if params.get("BillingLabel") is not None:
            self._BillingLabel = BillingLabel()
            self._BillingLabel._deserialize(params.get("BillingLabel"))
        self._RuntimeInSeconds = params.get("RuntimeInSeconds")
        self._RemainTimeInSeconds = params.get("RemainTimeInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookLifecycleScriptsSummary(AbstractModel):
    """notebook生命周期脚本实例概览

    """

    def __init__(self):
        r"""
        :param _NotebookLifecycleScriptsName: notebook生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _LastModifiedTime: 修改时间
        :type LastModifiedTime: str
        """
        self._NotebookLifecycleScriptsName = None
        self._CreationTime = None
        self._LastModifiedTime = None

    @property
    def NotebookLifecycleScriptsName(self):
        return self._NotebookLifecycleScriptsName

    @NotebookLifecycleScriptsName.setter
    def NotebookLifecycleScriptsName(self, NotebookLifecycleScriptsName):
        self._NotebookLifecycleScriptsName = NotebookLifecycleScriptsName

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastModifiedTime(self):
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime


    def _deserialize(self, params):
        self._NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self._CreationTime = params.get("CreationTime")
        self._LastModifiedTime = params.get("LastModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputDataConfig(AbstractModel):
    """输出数据配置

    """

    def __init__(self):
        r"""
        :param _CosOutputBucket: cos输出桶
注意：此字段可能返回 null，表示取不到有效值。
        :type CosOutputBucket: str
        :param _CosOutputKeyPrefix: cos输出key前缀
注意：此字段可能返回 null，表示取不到有效值。
        :type CosOutputKeyPrefix: str
        :param _FileSystemDataSource: 文件系统输出，如果指定了文件系统，那么Cos输出会被忽略
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemDataSource: :class:`tencentcloud.tione.v20191022.models.FileSystemDataSource`
        """
        self._CosOutputBucket = None
        self._CosOutputKeyPrefix = None
        self._FileSystemDataSource = None

    @property
    def CosOutputBucket(self):
        return self._CosOutputBucket

    @CosOutputBucket.setter
    def CosOutputBucket(self, CosOutputBucket):
        self._CosOutputBucket = CosOutputBucket

    @property
    def CosOutputKeyPrefix(self):
        return self._CosOutputKeyPrefix

    @CosOutputKeyPrefix.setter
    def CosOutputKeyPrefix(self, CosOutputKeyPrefix):
        self._CosOutputKeyPrefix = CosOutputKeyPrefix

    @property
    def FileSystemDataSource(self):
        return self._FileSystemDataSource

    @FileSystemDataSource.setter
    def FileSystemDataSource(self, FileSystemDataSource):
        self._FileSystemDataSource = FileSystemDataSource


    def _deserialize(self, params):
        self._CosOutputBucket = params.get("CosOutputBucket")
        self._CosOutputKeyPrefix = params.get("CosOutputKeyPrefix")
        if params.get("FileSystemDataSource") is not None:
            self._FileSystemDataSource = FileSystemDataSource()
            self._FileSystemDataSource._deserialize(params.get("FileSystemDataSource"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceConfig(AbstractModel):
    """计算资源配置

    """

    def __init__(self):
        r"""
        :param _InstanceCount: 计算实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param _InstanceType: 计算实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _VolumeSizeInGB: 挂载CBS大小（GB）
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeSizeInGB: int
        """
        self._InstanceCount = None
        self._InstanceType = None
        self._VolumeSizeInGB = None

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def VolumeSizeInGB(self):
        return self._VolumeSizeInGB

    @VolumeSizeInGB.setter
    def VolumeSizeInGB(self, VolumeSizeInGB):
        self._VolumeSizeInGB = VolumeSizeInGB


    def _deserialize(self, params):
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceType = params.get("InstanceType")
        self._VolumeSizeInGB = params.get("VolumeSizeInGB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecondaryStatusTransition(AbstractModel):
    """二级状态流水

    """

    def __init__(self):
        r"""
        :param _StartTime: 状态开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 状态结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Status: 状态名
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _StatusMessage: 状态详情
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMessage: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._StatusMessage = None

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
    def StatusMessage(self):
        return self._StatusMessage

    @StatusMessage.setter
    def StatusMessage(self, StatusMessage):
        self._StatusMessage = StatusMessage


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._StatusMessage = params.get("StatusMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartNotebookInstanceRequest(AbstractModel):
    """StartNotebookInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        :param _AutoStopping: 自动停止，可取值Enabled/Disabled
取值为Disabled的时候StoppingCondition将被忽略
取值为Enabled的时候读取StoppingCondition作为自动停止的配置
        :type AutoStopping: str
        :param _StoppingCondition: 自动停止配置，只在AutoStopping为Enabled的时候生效
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        """
        self._NotebookInstanceName = None
        self._AutoStopping = None
        self._StoppingCondition = None

    @property
    def NotebookInstanceName(self):
        return self._NotebookInstanceName

    @NotebookInstanceName.setter
    def NotebookInstanceName(self, NotebookInstanceName):
        self._NotebookInstanceName = NotebookInstanceName

    @property
    def AutoStopping(self):
        return self._AutoStopping

    @AutoStopping.setter
    def AutoStopping(self, AutoStopping):
        self._AutoStopping = AutoStopping

    @property
    def StoppingCondition(self):
        return self._StoppingCondition

    @StoppingCondition.setter
    def StoppingCondition(self, StoppingCondition):
        self._StoppingCondition = StoppingCondition


    def _deserialize(self, params):
        self._NotebookInstanceName = params.get("NotebookInstanceName")
        self._AutoStopping = params.get("AutoStopping")
        if params.get("StoppingCondition") is not None:
            self._StoppingCondition = StoppingCondition()
            self._StoppingCondition._deserialize(params.get("StoppingCondition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartNotebookInstanceResponse(AbstractModel):
    """StartNotebookInstance返回参数结构体

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


class StopNotebookInstanceRequest(AbstractModel):
    """StopNotebookInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        """
        self._NotebookInstanceName = None

    @property
    def NotebookInstanceName(self):
        return self._NotebookInstanceName

    @NotebookInstanceName.setter
    def NotebookInstanceName(self, NotebookInstanceName):
        self._NotebookInstanceName = NotebookInstanceName


    def _deserialize(self, params):
        self._NotebookInstanceName = params.get("NotebookInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopNotebookInstanceResponse(AbstractModel):
    """StopNotebookInstance返回参数结构体

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


class StopTrainingJobRequest(AbstractModel):
    """StopTrainingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        """
        self._TrainingJobName = None

    @property
    def TrainingJobName(self):
        return self._TrainingJobName

    @TrainingJobName.setter
    def TrainingJobName(self, TrainingJobName):
        self._TrainingJobName = TrainingJobName


    def _deserialize(self, params):
        self._TrainingJobName = params.get("TrainingJobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopTrainingJobResponse(AbstractModel):
    """StopTrainingJob返回参数结构体

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


class StoppingCondition(AbstractModel):
    """终止条件

    """

    def __init__(self):
        r"""
        :param _MaxRuntimeInSeconds: 最长运行运行时间（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRuntimeInSeconds: int
        :param _MaxWaitTimeInSeconds: 最长等待运行时间（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxWaitTimeInSeconds: int
        """
        self._MaxRuntimeInSeconds = None
        self._MaxWaitTimeInSeconds = None

    @property
    def MaxRuntimeInSeconds(self):
        return self._MaxRuntimeInSeconds

    @MaxRuntimeInSeconds.setter
    def MaxRuntimeInSeconds(self, MaxRuntimeInSeconds):
        self._MaxRuntimeInSeconds = MaxRuntimeInSeconds

    @property
    def MaxWaitTimeInSeconds(self):
        return self._MaxWaitTimeInSeconds

    @MaxWaitTimeInSeconds.setter
    def MaxWaitTimeInSeconds(self, MaxWaitTimeInSeconds):
        self._MaxWaitTimeInSeconds = MaxWaitTimeInSeconds


    def _deserialize(self, params):
        self._MaxRuntimeInSeconds = params.get("MaxRuntimeInSeconds")
        self._MaxWaitTimeInSeconds = params.get("MaxWaitTimeInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingJobSummary(AbstractModel):
    """训练任务概要

    """

    def __init__(self):
        r"""
        :param _CreationTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param _LastModifiedTime: 最近修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedTime: str
        :param _TrainingJobName: 训练任务名
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingJobName: str
        :param _TrainingJobStatus: 训练任务状态，取值范围
InProgress：运行中
Completed: 已完成
Failed: 失败
Stopping: 停止中
Stopped：已停止
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingJobStatus: str
        :param _TrainingEndTime: 完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingEndTime: str
        :param _InstanceId: 算了实例Id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _ResourceConfig: 资源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`
        """
        self._CreationTime = None
        self._LastModifiedTime = None
        self._TrainingJobName = None
        self._TrainingJobStatus = None
        self._TrainingEndTime = None
        self._InstanceId = None
        self._ResourceConfig = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastModifiedTime(self):
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime

    @property
    def TrainingJobName(self):
        return self._TrainingJobName

    @TrainingJobName.setter
    def TrainingJobName(self, TrainingJobName):
        self._TrainingJobName = TrainingJobName

    @property
    def TrainingJobStatus(self):
        return self._TrainingJobStatus

    @TrainingJobStatus.setter
    def TrainingJobStatus(self, TrainingJobStatus):
        self._TrainingJobStatus = TrainingJobStatus

    @property
    def TrainingEndTime(self):
        return self._TrainingEndTime

    @TrainingEndTime.setter
    def TrainingEndTime(self, TrainingEndTime):
        self._TrainingEndTime = TrainingEndTime

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceConfig(self):
        return self._ResourceConfig

    @ResourceConfig.setter
    def ResourceConfig(self, ResourceConfig):
        self._ResourceConfig = ResourceConfig


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._LastModifiedTime = params.get("LastModifiedTime")
        self._TrainingJobName = params.get("TrainingJobName")
        self._TrainingJobStatus = params.get("TrainingJobStatus")
        self._TrainingEndTime = params.get("TrainingEndTime")
        self._InstanceId = params.get("InstanceId")
        if params.get("ResourceConfig") is not None:
            self._ResourceConfig = ResourceConfig()
            self._ResourceConfig._deserialize(params.get("ResourceConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCodeRepositoryRequest(AbstractModel):
    """UpdateCodeRepository请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeRepositoryName: 查询存储库名称
        :type CodeRepositoryName: str
        :param _GitSecret: Git凭证
        :type GitSecret: :class:`tencentcloud.tione.v20191022.models.GitSecret`
        """
        self._CodeRepositoryName = None
        self._GitSecret = None

    @property
    def CodeRepositoryName(self):
        return self._CodeRepositoryName

    @CodeRepositoryName.setter
    def CodeRepositoryName(self, CodeRepositoryName):
        self._CodeRepositoryName = CodeRepositoryName

    @property
    def GitSecret(self):
        return self._GitSecret

    @GitSecret.setter
    def GitSecret(self, GitSecret):
        self._GitSecret = GitSecret


    def _deserialize(self, params):
        self._CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitSecret") is not None:
            self._GitSecret = GitSecret()
            self._GitSecret._deserialize(params.get("GitSecret"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCodeRepositoryResponse(AbstractModel):
    """UpdateCodeRepository返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CodeRepositoryName = None
        self._RequestId = None

    @property
    def CodeRepositoryName(self):
        return self._CodeRepositoryName

    @CodeRepositoryName.setter
    def CodeRepositoryName(self, CodeRepositoryName):
        self._CodeRepositoryName = CodeRepositoryName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CodeRepositoryName = params.get("CodeRepositoryName")
        self._RequestId = params.get("RequestId")


class UpdateNotebookInstanceRequest(AbstractModel):
    """UpdateNotebookInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookInstanceName: Notebook实例名称
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”
        :type NotebookInstanceName: str
        :param _RoleArn: 角色的资源描述
        :type RoleArn: str
        :param _RootAccess: Root访问权限
        :type RootAccess: str
        :param _VolumeSizeInGB: 数据卷大小(GB)
        :type VolumeSizeInGB: int
        :param _InstanceType: 算力资源类型
        :type InstanceType: str
        :param _LifecycleScriptsName: notebook生命周期脚本名称
        :type LifecycleScriptsName: str
        :param _DisassociateLifecycleScript: 是否解绑生命周期脚本，默认 false。
该值为true时，LifecycleScriptsName将被忽略
        :type DisassociateLifecycleScript: bool
        :param _DefaultCodeRepository: 默认存储库名称
可以是已创建的存储库名称或者已https://开头的公共git库
        :type DefaultCodeRepository: str
        :param _AdditionalCodeRepositories: 其他存储库列表
每个元素可以是已创建的存储库名称或者已https://开头的公共git库
        :type AdditionalCodeRepositories: list of str
        :param _DisassociateDefaultCodeRepository: 是否取消关联默认存储库，默认false
该值为true时，DefaultCodeRepository将被忽略
        :type DisassociateDefaultCodeRepository: bool
        :param _DisassociateAdditionalCodeRepositories: 是否取消关联其他存储库，默认false
该值为true时，AdditionalCodeRepositories将被忽略
        :type DisassociateAdditionalCodeRepositories: bool
        :param _ClsAccess: 已弃用，请使用ClsConfig配置。是否开启CLS日志服务，可取值Enabled/Disabled
        :type ClsAccess: str
        :param _AutoStopping: 自动停止，可取值Enabled/Disabled
取值为Disabled的时候StoppingCondition将被忽略
取值为Enabled的时候读取StoppingCondition作为自动停止的配置
        :type AutoStopping: str
        :param _StoppingCondition: 自动停止配置，只在AutoStopping为Enabled的时候生效
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param _ClsConfig: 接入日志的配置，默认使用免费日志服务。
        :type ClsConfig: :class:`tencentcloud.tione.v20191022.models.ClsConfig`
        """
        self._NotebookInstanceName = None
        self._RoleArn = None
        self._RootAccess = None
        self._VolumeSizeInGB = None
        self._InstanceType = None
        self._LifecycleScriptsName = None
        self._DisassociateLifecycleScript = None
        self._DefaultCodeRepository = None
        self._AdditionalCodeRepositories = None
        self._DisassociateDefaultCodeRepository = None
        self._DisassociateAdditionalCodeRepositories = None
        self._ClsAccess = None
        self._AutoStopping = None
        self._StoppingCondition = None
        self._ClsConfig = None

    @property
    def NotebookInstanceName(self):
        return self._NotebookInstanceName

    @NotebookInstanceName.setter
    def NotebookInstanceName(self, NotebookInstanceName):
        self._NotebookInstanceName = NotebookInstanceName

    @property
    def RoleArn(self):
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def RootAccess(self):
        return self._RootAccess

    @RootAccess.setter
    def RootAccess(self, RootAccess):
        self._RootAccess = RootAccess

    @property
    def VolumeSizeInGB(self):
        return self._VolumeSizeInGB

    @VolumeSizeInGB.setter
    def VolumeSizeInGB(self, VolumeSizeInGB):
        self._VolumeSizeInGB = VolumeSizeInGB

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def LifecycleScriptsName(self):
        return self._LifecycleScriptsName

    @LifecycleScriptsName.setter
    def LifecycleScriptsName(self, LifecycleScriptsName):
        self._LifecycleScriptsName = LifecycleScriptsName

    @property
    def DisassociateLifecycleScript(self):
        return self._DisassociateLifecycleScript

    @DisassociateLifecycleScript.setter
    def DisassociateLifecycleScript(self, DisassociateLifecycleScript):
        self._DisassociateLifecycleScript = DisassociateLifecycleScript

    @property
    def DefaultCodeRepository(self):
        return self._DefaultCodeRepository

    @DefaultCodeRepository.setter
    def DefaultCodeRepository(self, DefaultCodeRepository):
        self._DefaultCodeRepository = DefaultCodeRepository

    @property
    def AdditionalCodeRepositories(self):
        return self._AdditionalCodeRepositories

    @AdditionalCodeRepositories.setter
    def AdditionalCodeRepositories(self, AdditionalCodeRepositories):
        self._AdditionalCodeRepositories = AdditionalCodeRepositories

    @property
    def DisassociateDefaultCodeRepository(self):
        return self._DisassociateDefaultCodeRepository

    @DisassociateDefaultCodeRepository.setter
    def DisassociateDefaultCodeRepository(self, DisassociateDefaultCodeRepository):
        self._DisassociateDefaultCodeRepository = DisassociateDefaultCodeRepository

    @property
    def DisassociateAdditionalCodeRepositories(self):
        return self._DisassociateAdditionalCodeRepositories

    @DisassociateAdditionalCodeRepositories.setter
    def DisassociateAdditionalCodeRepositories(self, DisassociateAdditionalCodeRepositories):
        self._DisassociateAdditionalCodeRepositories = DisassociateAdditionalCodeRepositories

    @property
    def ClsAccess(self):
        return self._ClsAccess

    @ClsAccess.setter
    def ClsAccess(self, ClsAccess):
        self._ClsAccess = ClsAccess

    @property
    def AutoStopping(self):
        return self._AutoStopping

    @AutoStopping.setter
    def AutoStopping(self, AutoStopping):
        self._AutoStopping = AutoStopping

    @property
    def StoppingCondition(self):
        return self._StoppingCondition

    @StoppingCondition.setter
    def StoppingCondition(self, StoppingCondition):
        self._StoppingCondition = StoppingCondition

    @property
    def ClsConfig(self):
        return self._ClsConfig

    @ClsConfig.setter
    def ClsConfig(self, ClsConfig):
        self._ClsConfig = ClsConfig


    def _deserialize(self, params):
        self._NotebookInstanceName = params.get("NotebookInstanceName")
        self._RoleArn = params.get("RoleArn")
        self._RootAccess = params.get("RootAccess")
        self._VolumeSizeInGB = params.get("VolumeSizeInGB")
        self._InstanceType = params.get("InstanceType")
        self._LifecycleScriptsName = params.get("LifecycleScriptsName")
        self._DisassociateLifecycleScript = params.get("DisassociateLifecycleScript")
        self._DefaultCodeRepository = params.get("DefaultCodeRepository")
        self._AdditionalCodeRepositories = params.get("AdditionalCodeRepositories")
        self._DisassociateDefaultCodeRepository = params.get("DisassociateDefaultCodeRepository")
        self._DisassociateAdditionalCodeRepositories = params.get("DisassociateAdditionalCodeRepositories")
        self._ClsAccess = params.get("ClsAccess")
        self._AutoStopping = params.get("AutoStopping")
        if params.get("StoppingCondition") is not None:
            self._StoppingCondition = StoppingCondition()
            self._StoppingCondition._deserialize(params.get("StoppingCondition"))
        if params.get("ClsConfig") is not None:
            self._ClsConfig = ClsConfig()
            self._ClsConfig._deserialize(params.get("ClsConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateNotebookInstanceResponse(AbstractModel):
    """UpdateNotebookInstance返回参数结构体

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


class UpdateNotebookLifecycleScriptRequest(AbstractModel):
    """UpdateNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookLifecycleScriptsName: notebook生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param _CreateScript: 创建脚本，base64编码
base64后的脚本长度不能超过16384个字符
        :type CreateScript: str
        :param _StartScript: 启动脚本，base64编码
base64后的脚本长度不能超过16384个字符
        :type StartScript: str
        """
        self._NotebookLifecycleScriptsName = None
        self._CreateScript = None
        self._StartScript = None

    @property
    def NotebookLifecycleScriptsName(self):
        return self._NotebookLifecycleScriptsName

    @NotebookLifecycleScriptsName.setter
    def NotebookLifecycleScriptsName(self, NotebookLifecycleScriptsName):
        self._NotebookLifecycleScriptsName = NotebookLifecycleScriptsName

    @property
    def CreateScript(self):
        return self._CreateScript

    @CreateScript.setter
    def CreateScript(self, CreateScript):
        self._CreateScript = CreateScript

    @property
    def StartScript(self):
        return self._StartScript

    @StartScript.setter
    def StartScript(self, StartScript):
        self._StartScript = StartScript


    def _deserialize(self, params):
        self._NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self._CreateScript = params.get("CreateScript")
        self._StartScript = params.get("StartScript")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateNotebookLifecycleScriptResponse(AbstractModel):
    """UpdateNotebookLifecycleScript返回参数结构体

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


class VpcConfig(AbstractModel):
    """VPC配置

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: 安全组id
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        :param _SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        """
        self._SecurityGroupIds = None
        self._SubnetId = None

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        