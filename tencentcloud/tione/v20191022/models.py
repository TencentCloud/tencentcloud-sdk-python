# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
        """
        :param TrainingImageName: 镜像名字
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingImageName: str
        :param TrainingInputMode: 输入模式File|Pipe
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingInputMode: str
        :param AlgorithmName: 算法名字
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgorithmName: str
        """
        self.TrainingImageName = None
        self.TrainingInputMode = None
        self.AlgorithmName = None


    def _deserialize(self, params):
        self.TrainingImageName = params.get("TrainingImageName")
        self.TrainingInputMode = params.get("TrainingInputMode")
        self.AlgorithmName = params.get("AlgorithmName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BillingLabel(AbstractModel):
    """计费标签

    """

    def __init__(self):
        """
        :param Label: 计费项标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param VolumeSize: 存储大小
        :type VolumeSize: int
        :param Status: 计费状态
None: 不计费
StorageOnly: 仅存储计费
Computing: 计算和存储都计费
        :type Status: str
        """
        self.Label = None
        self.VolumeSize = None
        self.Status = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.VolumeSize = params.get("VolumeSize")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClsConfig(AbstractModel):
    """接入CLS服务的配置

    """

    def __init__(self):
        """
        :param Type: 接入类型，可选项为free、customer
        :type Type: str
        :param LogSetId: 自定义CLS的日志集ID，只有当Type为customer时生效
        :type LogSetId: str
        :param TopicId: 自定义CLS的日志主题ID，只有当Type为customer时生效
        :type TopicId: str
        """
        self.Type = None
        self.LogSetId = None
        self.TopicId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.LogSetId = params.get("LogSetId")
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CodeRepoSummary(AbstractModel):
    """存储库列表

    """

    def __init__(self):
        """
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param LastModifiedTime: 更新时间
        :type LastModifiedTime: str
        :param CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param GitConfig: Git配置
        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`
        :param NoSecret: 是否有Git凭证
        :type NoSecret: bool
        """
        self.CreationTime = None
        self.LastModifiedTime = None
        self.CodeRepositoryName = None
        self.GitConfig = None
        self.NoSecret = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitConfig") is not None:
            self.GitConfig = GitConfig()
            self.GitConfig._deserialize(params.get("GitConfig"))
        self.NoSecret = params.get("NoSecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CosDataSource(AbstractModel):
    """cos路径

    """

    def __init__(self):
        """
        :param Bucket: cos桶
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param KeyPrefix: cos文件key
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyPrefix: str
        :param DataDistributionType: 分布式数据下载方式
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDistributionType: str
        :param DataType: 数据类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DataType: str
        """
        self.Bucket = None
        self.KeyPrefix = None
        self.DataDistributionType = None
        self.DataType = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.KeyPrefix = params.get("KeyPrefix")
        self.DataDistributionType = params.get("DataDistributionType")
        self.DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateCodeRepositoryRequest(AbstractModel):
    """CreateCodeRepository请求参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param GitConfig: Git相关配置
        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`
        :param GitSecret: Git凭证
        :type GitSecret: :class:`tencentcloud.tione.v20191022.models.GitSecret`
        """
        self.CodeRepositoryName = None
        self.GitConfig = None
        self.GitSecret = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitConfig") is not None:
            self.GitConfig = GitConfig()
            self.GitConfig._deserialize(params.get("GitConfig"))
        if params.get("GitSecret") is not None:
            self.GitSecret = GitSecret()
            self.GitSecret._deserialize(params.get("GitSecret"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateCodeRepositoryResponse(AbstractModel):
    """CreateCodeRepository返回参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CodeRepositoryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateNotebookInstanceRequest(AbstractModel):
    """CreateNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称，不能超过63个字符
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”
        :type NotebookInstanceName: str
        :param InstanceType: Notebook算力类型
参考https://cloud.tencent.com/document/product/851/41239
        :type InstanceType: str
        :param VolumeSizeInGB: 数据卷大小(GB)
用户持久化Notebook实例的数据
        :type VolumeSizeInGB: int
        :param DirectInternetAccess: 外网访问权限，可取值Enabled/Disabled
开启后，Notebook实例可以具有访问外网80，443端口的权限
        :type DirectInternetAccess: str
        :param RootAccess: Root用户权限，可取值Enabled/Disabled
开启后，Notebook实例可以切换至root用户执行命令
        :type RootAccess: str
        :param SubnetId: 子网ID
如果需要Notebook实例访问VPC内的资源，则需要选择对应的子网
        :type SubnetId: str
        :param LifecycleScriptsName: 生命周期脚本名称
必须是已存在的生命周期脚本，具体参考https://cloud.tencent.com/document/product/851/43140
        :type LifecycleScriptsName: str
        :param DefaultCodeRepository: 默认存储库名称
可以是已创建的存储库名称或者已https://开头的公共git库
参考https://cloud.tencent.com/document/product/851/43139
        :type DefaultCodeRepository: str
        :param AdditionalCodeRepositories: 其他存储库列表
每个元素可以是已创建的存储库名称或者已https://开头的公共git库
参考https://cloud.tencent.com/document/product/851/43139
        :type AdditionalCodeRepositories: list of str
        :param ClsAccess: 已弃用，请使用ClsConfig配置。
是否开启CLS日志服务，可取值Enabled/Disabled，默认为Disabled
开启后，Notebook运行的日志会收集到CLS中，CLS会产生费用，请根据需要选择
        :type ClsAccess: str
        :param StoppingCondition: 自动停止配置
选择定时停止Notebook实例
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param AutoStopping: 自动停止，可取值Enabled/Disabled
取值为Disabled的时候StoppingCondition将被忽略
取值为Enabled的时候读取StoppingCondition作为自动停止的配置
        :type AutoStopping: str
        :param ClsConfig: 接入日志的配置，默认接入免费日志
        :type ClsConfig: :class:`tencentcloud.tione.v20191022.models.ClsConfig`
        """
        self.NotebookInstanceName = None
        self.InstanceType = None
        self.VolumeSizeInGB = None
        self.DirectInternetAccess = None
        self.RootAccess = None
        self.SubnetId = None
        self.LifecycleScriptsName = None
        self.DefaultCodeRepository = None
        self.AdditionalCodeRepositories = None
        self.ClsAccess = None
        self.StoppingCondition = None
        self.AutoStopping = None
        self.ClsConfig = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.InstanceType = params.get("InstanceType")
        self.VolumeSizeInGB = params.get("VolumeSizeInGB")
        self.DirectInternetAccess = params.get("DirectInternetAccess")
        self.RootAccess = params.get("RootAccess")
        self.SubnetId = params.get("SubnetId")
        self.LifecycleScriptsName = params.get("LifecycleScriptsName")
        self.DefaultCodeRepository = params.get("DefaultCodeRepository")
        self.AdditionalCodeRepositories = params.get("AdditionalCodeRepositories")
        self.ClsAccess = params.get("ClsAccess")
        if params.get("StoppingCondition") is not None:
            self.StoppingCondition = StoppingCondition()
            self.StoppingCondition._deserialize(params.get("StoppingCondition"))
        self.AutoStopping = params.get("AutoStopping")
        if params.get("ClsConfig") is not None:
            self.ClsConfig = ClsConfig()
            self.ClsConfig._deserialize(params.get("ClsConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateNotebookInstanceResponse(AbstractModel):
    """CreateNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名字
        :type NotebookInstanceName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookInstanceName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateNotebookLifecycleScriptRequest(AbstractModel):
    """CreateNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: Notebook生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param CreateScript: 创建脚本，base64编码
base64后的脚本长度不能超过16384个字符
        :type CreateScript: str
        :param StartScript: 启动脚本，base64编码
base64后的脚本长度不能超过16384个字符
        :type StartScript: str
        """
        self.NotebookLifecycleScriptsName = None
        self.CreateScript = None
        self.StartScript = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.CreateScript = params.get("CreateScript")
        self.StartScript = params.get("StartScript")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateNotebookLifecycleScriptResponse(AbstractModel):
    """CreateNotebookLifecycleScript返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookLifecycleScriptsName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePresignedNotebookInstanceUrlRequest(AbstractModel):
    """CreatePresignedNotebookInstanceUrl请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”
        :type NotebookInstanceName: str
        :param SessionExpirationDurationInSeconds: session有效时间，秒，取值范围[1800, 43200]
        :type SessionExpirationDurationInSeconds: int
        """
        self.NotebookInstanceName = None
        self.SessionExpirationDurationInSeconds = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.SessionExpirationDurationInSeconds = params.get("SessionExpirationDurationInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePresignedNotebookInstanceUrlResponse(AbstractModel):
    """CreatePresignedNotebookInstanceUrl返回参数结构体

    """

    def __init__(self):
        """
        :param AuthorizedUrl: 授权url
        :type AuthorizedUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AuthorizedUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuthorizedUrl = params.get("AuthorizedUrl")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateTrainingJobRequest(AbstractModel):
    """CreateTrainingJob请求参数结构体

    """

    def __init__(self):
        """
        :param AlgorithmSpecification: 算法镜像配置
        :type AlgorithmSpecification: :class:`tencentcloud.tione.v20191022.models.AlgorithmSpecification`
        :param OutputDataConfig: 输出数据配置
        :type OutputDataConfig: :class:`tencentcloud.tione.v20191022.models.OutputDataConfig`
        :param ResourceConfig: 资源实例配置
        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`
        :param TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        :param InputDataConfig: 输入数据配置
        :type InputDataConfig: list of InputDataConfig
        :param StoppingCondition: 中止条件
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param VpcConfig: 私有网络配置
        :type VpcConfig: :class:`tencentcloud.tione.v20191022.models.VpcConfig`
        :param HyperParameters: 算法超级参数
        :type HyperParameters: str
        :param EnvConfig: 环境变量配置
        :type EnvConfig: list of EnvConfig
        :param RoleName: 角色名称
        :type RoleName: str
        :param RetryWhenResourceInsufficient: 在资源不足（ResourceInsufficient）时后台不定时尝试重新创建训练任务。可取值Enabled/Disabled
默认值为Disabled即不重新尝试。设为Enabled时重新尝试有一定的时间期限，定义在 StoppingCondition 中 MaxWaitTimeInSecond中 ，默认值为1天，超过该期限创建失败。
        :type RetryWhenResourceInsufficient: str
        """
        self.AlgorithmSpecification = None
        self.OutputDataConfig = None
        self.ResourceConfig = None
        self.TrainingJobName = None
        self.InputDataConfig = None
        self.StoppingCondition = None
        self.VpcConfig = None
        self.HyperParameters = None
        self.EnvConfig = None
        self.RoleName = None
        self.RetryWhenResourceInsufficient = None


    def _deserialize(self, params):
        if params.get("AlgorithmSpecification") is not None:
            self.AlgorithmSpecification = AlgorithmSpecification()
            self.AlgorithmSpecification._deserialize(params.get("AlgorithmSpecification"))
        if params.get("OutputDataConfig") is not None:
            self.OutputDataConfig = OutputDataConfig()
            self.OutputDataConfig._deserialize(params.get("OutputDataConfig"))
        if params.get("ResourceConfig") is not None:
            self.ResourceConfig = ResourceConfig()
            self.ResourceConfig._deserialize(params.get("ResourceConfig"))
        self.TrainingJobName = params.get("TrainingJobName")
        if params.get("InputDataConfig") is not None:
            self.InputDataConfig = []
            for item in params.get("InputDataConfig"):
                obj = InputDataConfig()
                obj._deserialize(item)
                self.InputDataConfig.append(obj)
        if params.get("StoppingCondition") is not None:
            self.StoppingCondition = StoppingCondition()
            self.StoppingCondition._deserialize(params.get("StoppingCondition"))
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.HyperParameters = params.get("HyperParameters")
        if params.get("EnvConfig") is not None:
            self.EnvConfig = []
            for item in params.get("EnvConfig"):
                obj = EnvConfig()
                obj._deserialize(item)
                self.EnvConfig.append(obj)
        self.RoleName = params.get("RoleName")
        self.RetryWhenResourceInsufficient = params.get("RetryWhenResourceInsufficient")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateTrainingJobResponse(AbstractModel):
    """CreateTrainingJob返回参数结构体

    """

    def __init__(self):
        """
        :param TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TrainingJobName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TrainingJobName = params.get("TrainingJobName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DataSource(AbstractModel):
    """数据源

    """

    def __init__(self):
        """
        :param CosDataSource: cos数据源
注意：此字段可能返回 null，表示取不到有效值。
        :type CosDataSource: :class:`tencentcloud.tione.v20191022.models.CosDataSource`
        :param FileSystemDataSource: 文件系统输入源
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemDataSource: :class:`tencentcloud.tione.v20191022.models.FileSystemDataSource`
        """
        self.CosDataSource = None
        self.FileSystemDataSource = None


    def _deserialize(self, params):
        if params.get("CosDataSource") is not None:
            self.CosDataSource = CosDataSource()
            self.CosDataSource._deserialize(params.get("CosDataSource"))
        if params.get("FileSystemDataSource") is not None:
            self.FileSystemDataSource = FileSystemDataSource()
            self.FileSystemDataSource._deserialize(params.get("FileSystemDataSource"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteCodeRepositoryRequest(AbstractModel):
    """DeleteCodeRepository请求参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        """
        self.CodeRepositoryName = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteCodeRepositoryResponse(AbstractModel):
    """DeleteCodeRepository返回参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CodeRepositoryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteNotebookInstanceRequest(AbstractModel):
    """DeleteNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteNotebookInstanceResponse(AbstractModel):
    """DeleteNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteNotebookLifecycleScriptRequest(AbstractModel):
    """DeleteNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param Forcible: 是否忽略已关联的 notebook 实例强行删除生命周期脚本，默认 false
        :type Forcible: bool
        """
        self.NotebookLifecycleScriptsName = None
        self.Forcible = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.Forcible = params.get("Forcible")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteNotebookLifecycleScriptResponse(AbstractModel):
    """DeleteNotebookLifecycleScript返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCodeRepositoriesRequest(AbstractModel):
    """DescribeCodeRepositories请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20
        :type Limit: int
        :param Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。
        :type Filters: list of Filter
        :param SortOrder: 排序规则。默认取Descending
Descending 按更新时间降序
Ascending 按更新时间升序
        :type SortOrder: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.SortOrder = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCodeRepositoriesResponse(AbstractModel):
    """DescribeCodeRepositories返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 存储库总数目
        :type TotalCount: int
        :param CodeRepoSet: 存储库列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeRepoSet: list of CodeRepoSummary
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CodeRepoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CodeRepoSet") is not None:
            self.CodeRepoSet = []
            for item in params.get("CodeRepoSet"):
                obj = CodeRepoSummary()
                obj._deserialize(item)
                self.CodeRepoSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCodeRepositoryRequest(AbstractModel):
    """DescribeCodeRepository请求参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        """
        self.CodeRepositoryName = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCodeRepositoryResponse(AbstractModel):
    """DescribeCodeRepository返回参数结构体

    """

    def __init__(self):
        """
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param LastModifiedTime: 更新时间
        :type LastModifiedTime: str
        :param CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param GitConfig: Git存储配置
        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`
        :param NoSecret: 是否有Git凭证
        :type NoSecret: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CreationTime = None
        self.LastModifiedTime = None
        self.CodeRepositoryName = None
        self.GitConfig = None
        self.NoSecret = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitConfig") is not None:
            self.GitConfig = GitConfig()
            self.GitConfig._deserialize(params.get("GitConfig"))
        self.NoSecret = params.get("NoSecret")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeNotebookInstanceRequest(AbstractModel):
    """DescribeNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”
        :type NotebookInstanceName: str
        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeNotebookInstanceResponse(AbstractModel):
    """DescribeNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        :param InstanceType: Notebook算力资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param RoleArn: 角色的资源描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleArn: str
        :param DirectInternetAccess: 外网访问权限
注意：此字段可能返回 null，表示取不到有效值。
        :type DirectInternetAccess: str
        :param RootAccess: Root用户权限
注意：此字段可能返回 null，表示取不到有效值。
        :type RootAccess: str
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param VolumeSizeInGB: 数据卷大小(GB)
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeSizeInGB: int
        :param FailureReason: 创建失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param CreationTime: Notebook实例创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param LastModifiedTime: Notebook实例最近修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedTime: str
        :param LogUrl: Notebook实例日志链接
注意：此字段可能返回 null，表示取不到有效值。
        :type LogUrl: str
        :param NotebookInstanceStatus: Notebook实例状态

Pending: 创建中
Inservice: 运行中
Stopping: 停止中
Stopped: 已停止
Failed: 失败
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookInstanceStatus: str
        :param InstanceId: Notebook实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param LifecycleScriptsName: notebook生命周期脚本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LifecycleScriptsName: str
        :param DefaultCodeRepository: 默认存储库名称
可以是已创建的存储库名称或者已https://开头的公共git库
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultCodeRepository: str
        :param AdditionalCodeRepositories: 其他存储库列表
每个元素可以是已创建的存储库名称或者已https://开头的公共git库
注意：此字段可能返回 null，表示取不到有效值。
        :type AdditionalCodeRepositories: list of str
        :param ClsAccess: 是否开启CLS日志服务
注意：此字段可能返回 null，表示取不到有效值。
        :type ClsAccess: str
        :param Prepay: 是否预付费实例
注意：此字段可能返回 null，表示取不到有效值。
        :type Prepay: bool
        :param Deadline: 实例运行截止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Deadline: str
        :param StoppingCondition: 自动停止配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param ClsConfig: Cls配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ClsConfig: :class:`tencentcloud.tione.v20191022.models.ClsConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookInstanceName = None
        self.InstanceType = None
        self.RoleArn = None
        self.DirectInternetAccess = None
        self.RootAccess = None
        self.SubnetId = None
        self.VolumeSizeInGB = None
        self.FailureReason = None
        self.CreationTime = None
        self.LastModifiedTime = None
        self.LogUrl = None
        self.NotebookInstanceStatus = None
        self.InstanceId = None
        self.LifecycleScriptsName = None
        self.DefaultCodeRepository = None
        self.AdditionalCodeRepositories = None
        self.ClsAccess = None
        self.Prepay = None
        self.Deadline = None
        self.StoppingCondition = None
        self.ClsConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.InstanceType = params.get("InstanceType")
        self.RoleArn = params.get("RoleArn")
        self.DirectInternetAccess = params.get("DirectInternetAccess")
        self.RootAccess = params.get("RootAccess")
        self.SubnetId = params.get("SubnetId")
        self.VolumeSizeInGB = params.get("VolumeSizeInGB")
        self.FailureReason = params.get("FailureReason")
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.LogUrl = params.get("LogUrl")
        self.NotebookInstanceStatus = params.get("NotebookInstanceStatus")
        self.InstanceId = params.get("InstanceId")
        self.LifecycleScriptsName = params.get("LifecycleScriptsName")
        self.DefaultCodeRepository = params.get("DefaultCodeRepository")
        self.AdditionalCodeRepositories = params.get("AdditionalCodeRepositories")
        self.ClsAccess = params.get("ClsAccess")
        self.Prepay = params.get("Prepay")
        self.Deadline = params.get("Deadline")
        if params.get("StoppingCondition") is not None:
            self.StoppingCondition = StoppingCondition()
            self.StoppingCondition._deserialize(params.get("StoppingCondition"))
        if params.get("ClsConfig") is not None:
            self.ClsConfig = ClsConfig()
            self.ClsConfig._deserialize(params.get("ClsConfig"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeNotebookInstancesRequest(AbstractModel):
    """DescribeNotebookInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        :param SortOrder: 排序规则。默认取Descending
Descending 按更新时间降序
Ascending 按更新时间升序
        :type SortOrder: str
        :param Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。
lifecycle-name - String - 是否必填：否 -（过滤条件）按照生命周期脚本名称过滤。
default-code-repo-name - String - 是否必填：否 -（过滤条件）按照默认存储库名称过滤。
additional-code-repo-name - String - 是否必填：否 -（过滤条件）按照其他存储库名称过滤。
billing-status - String - 是否必填：否 - （过滤条件）按照计费状态过滤，可取以下值
   StorageOnly：仅存储计费的实例
   Computing：计算和存储都计费的实例
        :type Filters: list of Filter
        :param SortBy: 【废弃字段】排序字段
        :type SortBy: str
        """
        self.Offset = None
        self.Limit = None
        self.SortOrder = None
        self.Filters = None
        self.SortBy = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SortOrder = params.get("SortOrder")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SortBy = params.get("SortBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeNotebookInstancesResponse(AbstractModel):
    """DescribeNotebookInstances返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceSet: Notebook实例列表
        :type NotebookInstanceSet: list of NotebookInstanceSummary
        :param TotalCount: Notebook实例总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookInstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NotebookInstanceSet") is not None:
            self.NotebookInstanceSet = []
            for item in params.get("NotebookInstanceSet"):
                obj = NotebookInstanceSummary()
                obj._deserialize(item)
                self.NotebookInstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeNotebookLifecycleScriptRequest(AbstractModel):
    """DescribeNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        """
        self.NotebookLifecycleScriptsName = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeNotebookLifecycleScriptResponse(AbstractModel):
    """DescribeNotebookLifecycleScript返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param CreateScript: 创建脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateScript: str
        :param StartScript: 启动脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type StartScript: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param LastModifiedTime: 最后修改时间
        :type LastModifiedTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookLifecycleScriptsName = None
        self.CreateScript = None
        self.StartScript = None
        self.CreationTime = None
        self.LastModifiedTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.CreateScript = params.get("CreateScript")
        self.StartScript = params.get("StartScript")
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeNotebookLifecycleScriptsRequest(AbstractModel):
    """DescribeNotebookLifecycleScripts请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20
        :type Limit: int
        :param Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。
        :type Filters: list of Filter
        :param SortOrder: 排序规则。默认取Descending
Descending 按更新时间降序
Ascending 按更新时间升序
        :type SortOrder: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.SortOrder = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeNotebookLifecycleScriptsResponse(AbstractModel):
    """DescribeNotebookLifecycleScripts返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsSet: Notebook生命周期脚本列表
        :type NotebookLifecycleScriptsSet: list of NotebookLifecycleScriptsSummary
        :param TotalCount: Notebook生命周期脚本总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookLifecycleScriptsSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NotebookLifecycleScriptsSet") is not None:
            self.NotebookLifecycleScriptsSet = []
            for item in params.get("NotebookLifecycleScriptsSet"):
                obj = NotebookLifecycleScriptsSummary()
                obj._deserialize(item)
                self.NotebookLifecycleScriptsSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeNotebookSummaryRequest(AbstractModel):
    """DescribeNotebookSummary请求参数结构体

    """


class DescribeNotebookSummaryResponse(AbstractModel):
    """DescribeNotebookSummary返回参数结构体

    """

    def __init__(self):
        """
        :param AllInstanceCnt: 实例总数
        :type AllInstanceCnt: int
        :param BillingInstanceCnt: 计费实例总数
        :type BillingInstanceCnt: int
        :param StorageOnlyBillingInstanceCnt: 仅存储计费的实例总数
        :type StorageOnlyBillingInstanceCnt: int
        :param ComputingBillingInstanceCnt: 计算和存储都计费的实例总数
        :type ComputingBillingInstanceCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AllInstanceCnt = None
        self.BillingInstanceCnt = None
        self.StorageOnlyBillingInstanceCnt = None
        self.ComputingBillingInstanceCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllInstanceCnt = params.get("AllInstanceCnt")
        self.BillingInstanceCnt = params.get("BillingInstanceCnt")
        self.StorageOnlyBillingInstanceCnt = params.get("StorageOnlyBillingInstanceCnt")
        self.ComputingBillingInstanceCnt = params.get("ComputingBillingInstanceCnt")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTrainingJobRequest(AbstractModel):
    """DescribeTrainingJob请求参数结构体

    """

    def __init__(self):
        """
        :param TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        """
        self.TrainingJobName = None


    def _deserialize(self, params):
        self.TrainingJobName = params.get("TrainingJobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTrainingJobResponse(AbstractModel):
    """DescribeTrainingJob返回参数结构体

    """

    def __init__(self):
        """
        :param AlgorithmSpecification: 算法镜像配置
        :type AlgorithmSpecification: :class:`tencentcloud.tione.v20191022.models.AlgorithmSpecification`
        :param TrainingJobName: 任务名称
        :type TrainingJobName: str
        :param HyperParameters: 算法超级参数
注意：此字段可能返回 null，表示取不到有效值。
        :type HyperParameters: str
        :param InputDataConfig: 输入数据配置
        :type InputDataConfig: list of InputDataConfig
        :param OutputDataConfig: 输出数据配置
        :type OutputDataConfig: :class:`tencentcloud.tione.v20191022.models.OutputDataConfig`
        :param StoppingCondition: 中止条件
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param ResourceConfig: 计算实例配置
        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`
        :param VpcConfig: 私有网络配置
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcConfig: :class:`tencentcloud.tione.v20191022.models.VpcConfig`
        :param FailureReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param LastModifiedTime: 最近修改时间
        :type LastModifiedTime: str
        :param TrainingStartTime: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingStartTime: str
        :param TrainingEndTime: 任务完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingEndTime: str
        :param ModelArtifacts: 模型输出配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelArtifacts: :class:`tencentcloud.tione.v20191022.models.ModelArtifacts`
        :param SecondaryStatus: 详细状态，取值范围
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
        :param SecondaryStatusTransitions: 详细状态事件记录
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondaryStatusTransitions: list of SecondaryStatusTransition
        :param RoleName: 角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        :param TrainingJobStatus: 训练任务状态，取值范围
InProgress：运行中
Completed: 已完成
Failed: 失败
Stopping: 停止中
Stopped：已停止
        :type TrainingJobStatus: str
        :param LogUrl: 训练任务日志链接
注意：此字段可能返回 null，表示取不到有效值。
        :type LogUrl: str
        :param InstanceId: 训练任务实例ID
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlgorithmSpecification = None
        self.TrainingJobName = None
        self.HyperParameters = None
        self.InputDataConfig = None
        self.OutputDataConfig = None
        self.StoppingCondition = None
        self.ResourceConfig = None
        self.VpcConfig = None
        self.FailureReason = None
        self.LastModifiedTime = None
        self.TrainingStartTime = None
        self.TrainingEndTime = None
        self.ModelArtifacts = None
        self.SecondaryStatus = None
        self.SecondaryStatusTransitions = None
        self.RoleName = None
        self.TrainingJobStatus = None
        self.LogUrl = None
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlgorithmSpecification") is not None:
            self.AlgorithmSpecification = AlgorithmSpecification()
            self.AlgorithmSpecification._deserialize(params.get("AlgorithmSpecification"))
        self.TrainingJobName = params.get("TrainingJobName")
        self.HyperParameters = params.get("HyperParameters")
        if params.get("InputDataConfig") is not None:
            self.InputDataConfig = []
            for item in params.get("InputDataConfig"):
                obj = InputDataConfig()
                obj._deserialize(item)
                self.InputDataConfig.append(obj)
        if params.get("OutputDataConfig") is not None:
            self.OutputDataConfig = OutputDataConfig()
            self.OutputDataConfig._deserialize(params.get("OutputDataConfig"))
        if params.get("StoppingCondition") is not None:
            self.StoppingCondition = StoppingCondition()
            self.StoppingCondition._deserialize(params.get("StoppingCondition"))
        if params.get("ResourceConfig") is not None:
            self.ResourceConfig = ResourceConfig()
            self.ResourceConfig._deserialize(params.get("ResourceConfig"))
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.FailureReason = params.get("FailureReason")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.TrainingStartTime = params.get("TrainingStartTime")
        self.TrainingEndTime = params.get("TrainingEndTime")
        if params.get("ModelArtifacts") is not None:
            self.ModelArtifacts = ModelArtifacts()
            self.ModelArtifacts._deserialize(params.get("ModelArtifacts"))
        self.SecondaryStatus = params.get("SecondaryStatus")
        if params.get("SecondaryStatusTransitions") is not None:
            self.SecondaryStatusTransitions = []
            for item in params.get("SecondaryStatusTransitions"):
                obj = SecondaryStatusTransition()
                obj._deserialize(item)
                self.SecondaryStatusTransitions.append(obj)
        self.RoleName = params.get("RoleName")
        self.TrainingJobStatus = params.get("TrainingJobStatus")
        self.LogUrl = params.get("LogUrl")
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTrainingJobsRequest(AbstractModel):
    """DescribeTrainingJobs请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        :param CreationTimeAfter: 创建时间晚于
        :type CreationTimeAfter: str
        :param CreationTimeBefore: 创建时间早于
        :type CreationTimeBefore: str
        :param NameContains: 根据名称过滤
        :type NameContains: str
        :param StatusEquals: 根据状态过滤
        :type StatusEquals: str
        :param Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.CreationTimeAfter = None
        self.CreationTimeBefore = None
        self.NameContains = None
        self.StatusEquals = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreationTimeAfter = params.get("CreationTimeAfter")
        self.CreationTimeBefore = params.get("CreationTimeBefore")
        self.NameContains = params.get("NameContains")
        self.StatusEquals = params.get("StatusEquals")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTrainingJobsResponse(AbstractModel):
    """DescribeTrainingJobs返回参数结构体

    """

    def __init__(self):
        """
        :param TrainingJobSet: 训练任务列表
        :type TrainingJobSet: list of TrainingJobSummary
        :param TotalCount: 训练任务总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TrainingJobSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TrainingJobSet") is not None:
            self.TrainingJobSet = []
            for item in params.get("TrainingJobSet"):
                obj = TrainingJobSummary()
                obj._deserialize(item)
                self.TrainingJobSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnvConfig(AbstractModel):
    """环境变量

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Value: 值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FileSystemDataSource(AbstractModel):
    """文件系统输入数据源

    """

    def __init__(self):
        """
        :param DirectoryPath: 文件系统目录
注意：此字段可能返回 null，表示取不到有效值。
        :type DirectoryPath: str
        :param FileSystemType: 文件系统类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemType: str
        :param FileSystemAccessMode: 文件系统访问模式
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemAccessMode: str
        :param FileSystemId: 文件系统ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemId: str
        """
        self.DirectoryPath = None
        self.FileSystemType = None
        self.FileSystemAccessMode = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.DirectoryPath = params.get("DirectoryPath")
        self.FileSystemType = params.get("FileSystemType")
        self.FileSystemAccessMode = params.get("FileSystemAccessMode")
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        """
        :param Name: 过滤字段名称
        :type Name: str
        :param Values: 过滤字段取值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GitConfig(AbstractModel):
    """存储库Git相关配置

    """

    def __init__(self):
        """
        :param RepositoryUrl: git地址
        :type RepositoryUrl: str
        :param Branch: 代码分支
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        """
        self.RepositoryUrl = None
        self.Branch = None


    def _deserialize(self, params):
        self.RepositoryUrl = params.get("RepositoryUrl")
        self.Branch = params.get("Branch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GitSecret(AbstractModel):
    """Git凭证

    """

    def __init__(self):
        """
        :param NoSecret: 无秘钥，默认选项
        :type NoSecret: bool
        :param Secret: Git用户名密码base64编码后的字符串
编码前的内容应为Json字符串，如
{"UserName": "用户名", "Password":"密码"}
        :type Secret: str
        """
        self.NoSecret = None
        self.Secret = None


    def _deserialize(self, params):
        self.NoSecret = params.get("NoSecret")
        self.Secret = params.get("Secret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InputDataConfig(AbstractModel):
    """输入数据配置

    """

    def __init__(self):
        """
        :param ChannelName: 通道名
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelName: str
        :param DataSource: 数据源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: :class:`tencentcloud.tione.v20191022.models.DataSource`
        :param InputMode: 输入类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InputMode: str
        :param ContentType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentType: str
        """
        self.ChannelName = None
        self.DataSource = None
        self.InputMode = None
        self.ContentType = None


    def _deserialize(self, params):
        self.ChannelName = params.get("ChannelName")
        if params.get("DataSource") is not None:
            self.DataSource = DataSource()
            self.DataSource._deserialize(params.get("DataSource"))
        self.InputMode = params.get("InputMode")
        self.ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModelArtifacts(AbstractModel):
    """模型输出

    """

    def __init__(self):
        """
        :param CosModelArtifacts: cos输出路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CosModelArtifacts: str
        """
        self.CosModelArtifacts = None


    def _deserialize(self, params):
        self.CosModelArtifacts = params.get("CosModelArtifacts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class NotebookInstanceSummary(AbstractModel):
    """notebook实例概览

    """

    def __init__(self):
        """
        :param CreationTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param LastModifiedTime: 最近修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedTime: str
        :param NotebookInstanceName: notebook实例名字
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookInstanceName: str
        :param NotebookInstanceStatus: notebook实例状态，取值范围：
Pending: 创建中
Inservice: 运行中
Stopping: 停止中
Stopped: 已停止
Failed: 失败
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookInstanceStatus: str
        :param InstanceType: 算力类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param StartupTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartupTime: str
        :param Deadline: 运行截止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Deadline: str
        :param StoppingCondition: 自动停止配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param Prepay: 是否是预付费实例
注意：此字段可能返回 null，表示取不到有效值。
        :type Prepay: bool
        :param BillingLabel: 计费标识
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingLabel: :class:`tencentcloud.tione.v20191022.models.BillingLabel`
        :param RuntimeInSeconds: 运行时长，秒
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param RemainTimeInSeconds: 剩余时长，秒
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainTimeInSeconds: int
        """
        self.CreationTime = None
        self.LastModifiedTime = None
        self.NotebookInstanceName = None
        self.NotebookInstanceStatus = None
        self.InstanceType = None
        self.InstanceId = None
        self.StartupTime = None
        self.Deadline = None
        self.StoppingCondition = None
        self.Prepay = None
        self.BillingLabel = None
        self.RuntimeInSeconds = None
        self.RemainTimeInSeconds = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.NotebookInstanceStatus = params.get("NotebookInstanceStatus")
        self.InstanceType = params.get("InstanceType")
        self.InstanceId = params.get("InstanceId")
        self.StartupTime = params.get("StartupTime")
        self.Deadline = params.get("Deadline")
        if params.get("StoppingCondition") is not None:
            self.StoppingCondition = StoppingCondition()
            self.StoppingCondition._deserialize(params.get("StoppingCondition"))
        self.Prepay = params.get("Prepay")
        if params.get("BillingLabel") is not None:
            self.BillingLabel = BillingLabel()
            self.BillingLabel._deserialize(params.get("BillingLabel"))
        self.RuntimeInSeconds = params.get("RuntimeInSeconds")
        self.RemainTimeInSeconds = params.get("RemainTimeInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class NotebookLifecycleScriptsSummary(AbstractModel):
    """notebook生命周期脚本实例概览

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: notebook生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param LastModifiedTime: 修改时间
        :type LastModifiedTime: str
        """
        self.NotebookLifecycleScriptsName = None
        self.CreationTime = None
        self.LastModifiedTime = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OutputDataConfig(AbstractModel):
    """输出数据配置

    """

    def __init__(self):
        """
        :param CosOutputBucket: cos输出桶
注意：此字段可能返回 null，表示取不到有效值。
        :type CosOutputBucket: str
        :param CosOutputKeyPrefix: cos输出key前缀
注意：此字段可能返回 null，表示取不到有效值。
        :type CosOutputKeyPrefix: str
        :param FileSystemDataSource: 文件系统输出，如果指定了文件系统，那么Cos输出会被忽略
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemDataSource: :class:`tencentcloud.tione.v20191022.models.FileSystemDataSource`
        """
        self.CosOutputBucket = None
        self.CosOutputKeyPrefix = None
        self.FileSystemDataSource = None


    def _deserialize(self, params):
        self.CosOutputBucket = params.get("CosOutputBucket")
        self.CosOutputKeyPrefix = params.get("CosOutputKeyPrefix")
        if params.get("FileSystemDataSource") is not None:
            self.FileSystemDataSource = FileSystemDataSource()
            self.FileSystemDataSource._deserialize(params.get("FileSystemDataSource"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResourceConfig(AbstractModel):
    """计算资源配置

    """

    def __init__(self):
        """
        :param InstanceCount: 计算实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param InstanceType: 计算实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param VolumeSizeInGB: 挂载CBS大小（GB）
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeSizeInGB: int
        """
        self.InstanceCount = None
        self.InstanceType = None
        self.VolumeSizeInGB = None


    def _deserialize(self, params):
        self.InstanceCount = params.get("InstanceCount")
        self.InstanceType = params.get("InstanceType")
        self.VolumeSizeInGB = params.get("VolumeSizeInGB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SecondaryStatusTransition(AbstractModel):
    """二级状态流水

    """

    def __init__(self):
        """
        :param StartTime: 状态开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 状态结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Status: 状态名
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param StatusMessage: 状态详情
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMessage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.StatusMessage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.StatusMessage = params.get("StatusMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartNotebookInstanceRequest(AbstractModel):
    """StartNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        :param AutoStopping: 自动停止，可取值Enabled/Disabled
取值为Disabled的时候StoppingCondition将被忽略
取值为Enabled的时候读取StoppingCondition作为自动停止的配置
        :type AutoStopping: str
        :param StoppingCondition: 自动停止配置，只在AutoStopping为Enabled的时候生效
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        """
        self.NotebookInstanceName = None
        self.AutoStopping = None
        self.StoppingCondition = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.AutoStopping = params.get("AutoStopping")
        if params.get("StoppingCondition") is not None:
            self.StoppingCondition = StoppingCondition()
            self.StoppingCondition._deserialize(params.get("StoppingCondition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartNotebookInstanceResponse(AbstractModel):
    """StartNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopNotebookInstanceRequest(AbstractModel):
    """StopNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopNotebookInstanceResponse(AbstractModel):
    """StopNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopTrainingJobRequest(AbstractModel):
    """StopTrainingJob请求参数结构体

    """

    def __init__(self):
        """
        :param TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        """
        self.TrainingJobName = None


    def _deserialize(self, params):
        self.TrainingJobName = params.get("TrainingJobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopTrainingJobResponse(AbstractModel):
    """StopTrainingJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StoppingCondition(AbstractModel):
    """终止条件

    """

    def __init__(self):
        """
        :param MaxRuntimeInSeconds: 最长运行运行时间（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRuntimeInSeconds: int
        :param MaxWaitTimeInSeconds: 最长等待运行时间（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxWaitTimeInSeconds: int
        """
        self.MaxRuntimeInSeconds = None
        self.MaxWaitTimeInSeconds = None


    def _deserialize(self, params):
        self.MaxRuntimeInSeconds = params.get("MaxRuntimeInSeconds")
        self.MaxWaitTimeInSeconds = params.get("MaxWaitTimeInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TrainingJobSummary(AbstractModel):
    """训练任务概要

    """

    def __init__(self):
        """
        :param CreationTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param LastModifiedTime: 最近修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedTime: str
        :param TrainingJobName: 训练任务名
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingJobName: str
        :param TrainingJobStatus: 训练任务状态，取值范围
InProgress：运行中
Completed: 已完成
Failed: 失败
Stopping: 停止中
Stopped：已停止
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingJobStatus: str
        :param TrainingEndTime: 完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingEndTime: str
        :param InstanceId: 算了实例Id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param ResourceConfig: 资源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`
        """
        self.CreationTime = None
        self.LastModifiedTime = None
        self.TrainingJobName = None
        self.TrainingJobStatus = None
        self.TrainingEndTime = None
        self.InstanceId = None
        self.ResourceConfig = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.TrainingJobName = params.get("TrainingJobName")
        self.TrainingJobStatus = params.get("TrainingJobStatus")
        self.TrainingEndTime = params.get("TrainingEndTime")
        self.InstanceId = params.get("InstanceId")
        if params.get("ResourceConfig") is not None:
            self.ResourceConfig = ResourceConfig()
            self.ResourceConfig._deserialize(params.get("ResourceConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateCodeRepositoryRequest(AbstractModel):
    """UpdateCodeRepository请求参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 查询存储库名称
        :type CodeRepositoryName: str
        :param GitSecret: Git凭证
        :type GitSecret: :class:`tencentcloud.tione.v20191022.models.GitSecret`
        """
        self.CodeRepositoryName = None
        self.GitSecret = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitSecret") is not None:
            self.GitSecret = GitSecret()
            self.GitSecret._deserialize(params.get("GitSecret"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateCodeRepositoryResponse(AbstractModel):
    """UpdateCodeRepository返回参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称
        :type CodeRepositoryName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CodeRepositoryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateNotebookInstanceRequest(AbstractModel):
    """UpdateNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”
        :type NotebookInstanceName: str
        :param RoleArn: 角色的资源描述
        :type RoleArn: str
        :param RootAccess: Root访问权限
        :type RootAccess: str
        :param VolumeSizeInGB: 数据卷大小(GB)
        :type VolumeSizeInGB: int
        :param InstanceType: 算力资源类型
        :type InstanceType: str
        :param LifecycleScriptsName: notebook生命周期脚本名称
        :type LifecycleScriptsName: str
        :param DisassociateLifecycleScript: 是否解绑生命周期脚本，默认 false。
该值为true时，LifecycleScriptsName将被忽略
        :type DisassociateLifecycleScript: bool
        :param DefaultCodeRepository: 默认存储库名称
可以是已创建的存储库名称或者已https://开头的公共git库
        :type DefaultCodeRepository: str
        :param AdditionalCodeRepositories: 其他存储库列表
每个元素可以是已创建的存储库名称或者已https://开头的公共git库
        :type AdditionalCodeRepositories: list of str
        :param DisassociateDefaultCodeRepository: 是否取消关联默认存储库，默认false
该值为true时，DefaultCodeRepository将被忽略
        :type DisassociateDefaultCodeRepository: bool
        :param DisassociateAdditionalCodeRepositories: 是否取消关联其他存储库，默认false
该值为true时，AdditionalCodeRepositories将被忽略
        :type DisassociateAdditionalCodeRepositories: bool
        :param ClsAccess: 已弃用，请使用ClsConfig配置。是否开启CLS日志服务，可取值Enabled/Disabled
        :type ClsAccess: str
        :param AutoStopping: 自动停止，可取值Enabled/Disabled
取值为Disabled的时候StoppingCondition将被忽略
取值为Enabled的时候读取StoppingCondition作为自动停止的配置
        :type AutoStopping: str
        :param StoppingCondition: 自动停止配置，只在AutoStopping为Enabled的时候生效
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param ClsConfig: 接入日志的配置，默认使用免费日志服务。
        :type ClsConfig: :class:`tencentcloud.tione.v20191022.models.ClsConfig`
        """
        self.NotebookInstanceName = None
        self.RoleArn = None
        self.RootAccess = None
        self.VolumeSizeInGB = None
        self.InstanceType = None
        self.LifecycleScriptsName = None
        self.DisassociateLifecycleScript = None
        self.DefaultCodeRepository = None
        self.AdditionalCodeRepositories = None
        self.DisassociateDefaultCodeRepository = None
        self.DisassociateAdditionalCodeRepositories = None
        self.ClsAccess = None
        self.AutoStopping = None
        self.StoppingCondition = None
        self.ClsConfig = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.RoleArn = params.get("RoleArn")
        self.RootAccess = params.get("RootAccess")
        self.VolumeSizeInGB = params.get("VolumeSizeInGB")
        self.InstanceType = params.get("InstanceType")
        self.LifecycleScriptsName = params.get("LifecycleScriptsName")
        self.DisassociateLifecycleScript = params.get("DisassociateLifecycleScript")
        self.DefaultCodeRepository = params.get("DefaultCodeRepository")
        self.AdditionalCodeRepositories = params.get("AdditionalCodeRepositories")
        self.DisassociateDefaultCodeRepository = params.get("DisassociateDefaultCodeRepository")
        self.DisassociateAdditionalCodeRepositories = params.get("DisassociateAdditionalCodeRepositories")
        self.ClsAccess = params.get("ClsAccess")
        self.AutoStopping = params.get("AutoStopping")
        if params.get("StoppingCondition") is not None:
            self.StoppingCondition = StoppingCondition()
            self.StoppingCondition._deserialize(params.get("StoppingCondition"))
        if params.get("ClsConfig") is not None:
            self.ClsConfig = ClsConfig()
            self.ClsConfig._deserialize(params.get("ClsConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateNotebookInstanceResponse(AbstractModel):
    """UpdateNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateNotebookLifecycleScriptRequest(AbstractModel):
    """UpdateNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: notebook生命周期脚本名称
        :type NotebookLifecycleScriptsName: str
        :param CreateScript: 创建脚本，base64编码
base64后的脚本长度不能超过16384个字符
        :type CreateScript: str
        :param StartScript: 启动脚本，base64编码
base64后的脚本长度不能超过16384个字符
        :type StartScript: str
        """
        self.NotebookLifecycleScriptsName = None
        self.CreateScript = None
        self.StartScript = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.CreateScript = params.get("CreateScript")
        self.StartScript = params.get("StartScript")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateNotebookLifecycleScriptResponse(AbstractModel):
    """UpdateNotebookLifecycleScript返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VpcConfig(AbstractModel):
    """VPC配置

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全组id
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        """
        self.SecurityGroupIds = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        