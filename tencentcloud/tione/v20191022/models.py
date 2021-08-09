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
        """
        :param TrainingImageName: 镜像名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type TrainingImageName: str\n        :param TrainingInputMode: 输入模式File|Pipe
注意：此字段可能返回 null，表示取不到有效值。\n        :type TrainingInputMode: str\n        :param AlgorithmName: 算法名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type AlgorithmName: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillingLabel(AbstractModel):
    """计费标签

    """

    def __init__(self):
        """
        :param Label: 计费项标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type Label: str\n        :param VolumeSize: 存储大小\n        :type VolumeSize: int\n        :param Status: 计费状态
None: 不计费
StorageOnly: 仅存储计费
Computing: 计算和存储都计费\n        :type Status: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsConfig(AbstractModel):
    """接入CLS服务的配置

    """

    def __init__(self):
        """
        :param Type: 接入类型，可选项为free、customer\n        :type Type: str\n        :param LogSetId: 自定义CLS的日志集ID，只有当Type为customer时生效\n        :type LogSetId: str\n        :param TopicId: 自定义CLS的日志主题ID，只有当Type为customer时生效\n        :type TopicId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeRepoSummary(AbstractModel):
    """存储库列表

    """

    def __init__(self):
        """
        :param CreationTime: 创建时间\n        :type CreationTime: str\n        :param LastModifiedTime: 更新时间\n        :type LastModifiedTime: str\n        :param CodeRepositoryName: 存储库名称\n        :type CodeRepositoryName: str\n        :param GitConfig: Git配置\n        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`\n        :param NoSecret: 是否有Git凭证\n        :type NoSecret: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosDataSource(AbstractModel):
    """cos路径

    """

    def __init__(self):
        """
        :param Bucket: cos桶
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bucket: str\n        :param KeyPrefix: cos文件key
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeyPrefix: str\n        :param DataDistributionType: 分布式数据下载方式
注意：此字段可能返回 null，表示取不到有效值。\n        :type DataDistributionType: str\n        :param DataType: 数据类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type DataType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeRepositoryRequest(AbstractModel):
    """CreateCodeRepository请求参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称\n        :type CodeRepositoryName: str\n        :param GitConfig: Git相关配置\n        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`\n        :param GitSecret: Git凭证\n        :type GitSecret: :class:`tencentcloud.tione.v20191022.models.GitSecret`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeRepositoryResponse(AbstractModel):
    """CreateCodeRepository返回参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称\n        :type CodeRepositoryName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CodeRepositoryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        self.RequestId = params.get("RequestId")


class CreateNotebookInstanceRequest(AbstractModel):
    """CreateNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称，不能超过63个字符
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”\n        :type NotebookInstanceName: str\n        :param InstanceType: Notebook算力类型
参考https://cloud.tencent.com/document/product/851/41239\n        :type InstanceType: str\n        :param VolumeSizeInGB: 数据卷大小(GB)
用户持久化Notebook实例的数据\n        :type VolumeSizeInGB: int\n        :param DirectInternetAccess: 外网访问权限，可取值Enabled/Disabled
开启后，Notebook实例可以具有访问外网80，443端口的权限\n        :type DirectInternetAccess: str\n        :param RootAccess: Root用户权限，可取值Enabled/Disabled
开启后，Notebook实例可以切换至root用户执行命令\n        :type RootAccess: str\n        :param SubnetId: 子网ID
如果需要Notebook实例访问VPC内的资源，则需要选择对应的子网\n        :type SubnetId: str\n        :param LifecycleScriptsName: 生命周期脚本名称
必须是已存在的生命周期脚本，具体参考https://cloud.tencent.com/document/product/851/43140\n        :type LifecycleScriptsName: str\n        :param DefaultCodeRepository: 默认存储库名称
可以是已创建的存储库名称或者已https://开头的公共git库
参考https://cloud.tencent.com/document/product/851/43139\n        :type DefaultCodeRepository: str\n        :param AdditionalCodeRepositories: 其他存储库列表
每个元素可以是已创建的存储库名称或者已https://开头的公共git库
参考https://cloud.tencent.com/document/product/851/43139\n        :type AdditionalCodeRepositories: list of str\n        :param ClsAccess: 已弃用，请使用ClsConfig配置。
是否开启CLS日志服务，可取值Enabled/Disabled，默认为Disabled
开启后，Notebook运行的日志会收集到CLS中，CLS会产生费用，请根据需要选择\n        :type ClsAccess: str\n        :param StoppingCondition: 自动停止配置
选择定时停止Notebook实例\n        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`\n        :param AutoStopping: 自动停止，可取值Enabled/Disabled
取值为Disabled的时候StoppingCondition将被忽略
取值为Enabled的时候读取StoppingCondition作为自动停止的配置\n        :type AutoStopping: str\n        :param ClsConfig: 接入日志的配置，默认接入免费日志\n        :type ClsConfig: :class:`tencentcloud.tione.v20191022.models.ClsConfig`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookInstanceResponse(AbstractModel):
    """CreateNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名字\n        :type NotebookInstanceName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NotebookInstanceName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.RequestId = params.get("RequestId")


class CreateNotebookLifecycleScriptRequest(AbstractModel):
    """CreateNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: Notebook生命周期脚本名称\n        :type NotebookLifecycleScriptsName: str\n        :param CreateScript: 创建脚本，base64编码
base64后的脚本长度不能超过16384个字符\n        :type CreateScript: str\n        :param StartScript: 启动脚本，base64编码
base64后的脚本长度不能超过16384个字符\n        :type StartScript: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookLifecycleScriptResponse(AbstractModel):
    """CreateNotebookLifecycleScript返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命周期脚本名称\n        :type NotebookLifecycleScriptsName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NotebookLifecycleScriptsName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.RequestId = params.get("RequestId")


class CreatePresignedNotebookInstanceUrlRequest(AbstractModel):
    """CreatePresignedNotebookInstanceUrl请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”\n        :type NotebookInstanceName: str\n        :param SessionExpirationDurationInSeconds: session有效时间，秒，取值范围[1800, 43200]\n        :type SessionExpirationDurationInSeconds: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePresignedNotebookInstanceUrlResponse(AbstractModel):
    """CreatePresignedNotebookInstanceUrl返回参数结构体

    """

    def __init__(self):
        """
        :param AuthorizedUrl: 授权url\n        :type AuthorizedUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AuthorizedUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuthorizedUrl = params.get("AuthorizedUrl")
        self.RequestId = params.get("RequestId")


class CreateTrainingJobRequest(AbstractModel):
    """CreateTrainingJob请求参数结构体

    """

    def __init__(self):
        """
        :param AlgorithmSpecification: 算法镜像配置\n        :type AlgorithmSpecification: :class:`tencentcloud.tione.v20191022.models.AlgorithmSpecification`\n        :param OutputDataConfig: 输出数据配置\n        :type OutputDataConfig: :class:`tencentcloud.tione.v20191022.models.OutputDataConfig`\n        :param ResourceConfig: 资源实例配置\n        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`\n        :param TrainingJobName: 训练任务名称\n        :type TrainingJobName: str\n        :param InputDataConfig: 输入数据配置\n        :type InputDataConfig: list of InputDataConfig\n        :param StoppingCondition: 中止条件\n        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`\n        :param VpcConfig: 私有网络配置\n        :type VpcConfig: :class:`tencentcloud.tione.v20191022.models.VpcConfig`\n        :param HyperParameters: 算法超级参数\n        :type HyperParameters: str\n        :param EnvConfig: 环境变量配置\n        :type EnvConfig: list of EnvConfig\n        :param RoleName: 角色名称\n        :type RoleName: str\n        :param RetryWhenResourceInsufficient: 在资源不足（ResourceInsufficient）时后台不定时尝试重新创建训练任务。可取值Enabled/Disabled
默认值为Disabled即不重新尝试。设为Enabled时重新尝试有一定的时间期限，定义在 StoppingCondition 中 MaxWaitTimeInSecond中 ，默认值为1天，超过该期限创建失败。\n        :type RetryWhenResourceInsufficient: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrainingJobResponse(AbstractModel):
    """CreateTrainingJob返回参数结构体

    """

    def __init__(self):
        """
        :param TrainingJobName: 训练任务名称\n        :type TrainingJobName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TrainingJobName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TrainingJobName = params.get("TrainingJobName")
        self.RequestId = params.get("RequestId")


class DataSource(AbstractModel):
    """数据源

    """

    def __init__(self):
        """
        :param CosDataSource: cos数据源
注意：此字段可能返回 null，表示取不到有效值。\n        :type CosDataSource: :class:`tencentcloud.tione.v20191022.models.CosDataSource`\n        :param FileSystemDataSource: 文件系统输入源
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileSystemDataSource: :class:`tencentcloud.tione.v20191022.models.FileSystemDataSource`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeRepositoryRequest(AbstractModel):
    """DeleteCodeRepository请求参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称\n        :type CodeRepositoryName: str\n        """
        self.CodeRepositoryName = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeRepositoryResponse(AbstractModel):
    """DeleteCodeRepository返回参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称\n        :type CodeRepositoryName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CodeRepositoryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        self.RequestId = params.get("RequestId")


class DeleteNotebookInstanceRequest(AbstractModel):
    """DeleteNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称\n        :type NotebookInstanceName: str\n        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNotebookInstanceResponse(AbstractModel):
    """DeleteNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNotebookLifecycleScriptRequest(AbstractModel):
    """DeleteNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命周期脚本名称\n        :type NotebookLifecycleScriptsName: str\n        :param Forcible: 是否忽略已关联的 notebook 实例强行删除生命周期脚本，默认 false\n        :type Forcible: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNotebookLifecycleScriptResponse(AbstractModel):
    """DeleteNotebookLifecycleScript返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCodeRepositoriesRequest(AbstractModel):
    """DescribeCodeRepositories请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回数量，默认为20\n        :type Limit: int\n        :param Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。\n        :type Filters: list of Filter\n        :param SortOrder: 排序规则。默认取Descending
Descending 按更新时间降序
Ascending 按更新时间升序\n        :type SortOrder: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodeRepositoriesResponse(AbstractModel):
    """DescribeCodeRepositories返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 存储库总数目\n        :type TotalCount: int\n        :param CodeRepoSet: 存储库列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type CodeRepoSet: list of CodeRepoSummary\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeCodeRepositoryRequest(AbstractModel):
    """DescribeCodeRepository请求参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称\n        :type CodeRepositoryName: str\n        """
        self.CodeRepositoryName = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodeRepositoryResponse(AbstractModel):
    """DescribeCodeRepository返回参数结构体

    """

    def __init__(self):
        """
        :param CreationTime: 创建时间\n        :type CreationTime: str\n        :param LastModifiedTime: 更新时间\n        :type LastModifiedTime: str\n        :param CodeRepositoryName: 存储库名称\n        :type CodeRepositoryName: str\n        :param GitConfig: Git存储配置\n        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`\n        :param NoSecret: 是否有Git凭证\n        :type NoSecret: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeNotebookInstanceRequest(AbstractModel):
    """DescribeNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”\n        :type NotebookInstanceName: str\n        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookInstanceResponse(AbstractModel):
    """DescribeNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称\n        :type NotebookInstanceName: str\n        :param InstanceType: Notebook算力资源类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param RoleArn: 角色的资源描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type RoleArn: str\n        :param DirectInternetAccess: 外网访问权限
注意：此字段可能返回 null，表示取不到有效值。\n        :type DirectInternetAccess: str\n        :param RootAccess: Root用户权限
注意：此字段可能返回 null，表示取不到有效值。\n        :type RootAccess: str\n        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetId: str\n        :param VolumeSizeInGB: 数据卷大小(GB)
注意：此字段可能返回 null，表示取不到有效值。\n        :type VolumeSizeInGB: int\n        :param FailureReason: 创建失败原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailureReason: str\n        :param CreationTime: Notebook实例创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreationTime: str\n        :param LastModifiedTime: Notebook实例最近修改时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastModifiedTime: str\n        :param LogUrl: Notebook实例日志链接
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogUrl: str\n        :param NotebookInstanceStatus: Notebook实例状态

Pending: 创建中
Inservice: 运行中
Stopping: 停止中
Stopped: 已停止
Failed: 失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type NotebookInstanceStatus: str\n        :param InstanceId: Notebook实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param LifecycleScriptsName: notebook生命周期脚本名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type LifecycleScriptsName: str\n        :param DefaultCodeRepository: 默认存储库名称
可以是已创建的存储库名称或者已https://开头的公共git库
注意：此字段可能返回 null，表示取不到有效值。\n        :type DefaultCodeRepository: str\n        :param AdditionalCodeRepositories: 其他存储库列表
每个元素可以是已创建的存储库名称或者已https://开头的公共git库
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdditionalCodeRepositories: list of str\n        :param ClsAccess: 是否开启CLS日志服务
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClsAccess: str\n        :param Prepay: 是否预付费实例
注意：此字段可能返回 null，表示取不到有效值。\n        :type Prepay: bool\n        :param Deadline: 实例运行截止时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type Deadline: str\n        :param StoppingCondition: 自动停止配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`\n        :param ClsConfig: Cls配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClsConfig: :class:`tencentcloud.tione.v20191022.models.ClsConfig`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeNotebookInstancesRequest(AbstractModel):
    """DescribeNotebookInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param SortOrder: 排序规则。默认取Descending
Descending 按更新时间降序
Ascending 按更新时间升序\n        :type SortOrder: str\n        :param Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。
lifecycle-name - String - 是否必填：否 -（过滤条件）按照生命周期脚本名称过滤。
default-code-repo-name - String - 是否必填：否 -（过滤条件）按照默认存储库名称过滤。
additional-code-repo-name - String - 是否必填：否 -（过滤条件）按照其他存储库名称过滤。
billing-status - String - 是否必填：否 - （过滤条件）按照计费状态过滤，可取以下值
   StorageOnly：仅存储计费的实例
   Computing：计算和存储都计费的实例\n        :type Filters: list of Filter\n        :param SortBy: 【废弃字段】排序字段\n        :type SortBy: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookInstancesResponse(AbstractModel):
    """DescribeNotebookInstances返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceSet: Notebook实例列表\n        :type NotebookInstanceSet: list of NotebookInstanceSummary\n        :param TotalCount: Notebook实例总数目\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeNotebookLifecycleScriptRequest(AbstractModel):
    """DescribeNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命周期脚本名称\n        :type NotebookLifecycleScriptsName: str\n        """
        self.NotebookLifecycleScriptsName = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookLifecycleScriptResponse(AbstractModel):
    """DescribeNotebookLifecycleScript返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命周期脚本名称\n        :type NotebookLifecycleScriptsName: str\n        :param CreateScript: 创建脚本
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateScript: str\n        :param StartScript: 启动脚本
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartScript: str\n        :param CreationTime: 创建时间\n        :type CreationTime: str\n        :param LastModifiedTime: 最后修改时间\n        :type LastModifiedTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeNotebookLifecycleScriptsRequest(AbstractModel):
    """DescribeNotebookLifecycleScripts请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回数量，默认为20\n        :type Limit: int\n        :param Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。\n        :type Filters: list of Filter\n        :param SortOrder: 排序规则。默认取Descending
Descending 按更新时间降序
Ascending 按更新时间升序\n        :type SortOrder: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookLifecycleScriptsResponse(AbstractModel):
    """DescribeNotebookLifecycleScripts返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsSet: Notebook生命周期脚本列表\n        :type NotebookLifecycleScriptsSet: list of NotebookLifecycleScriptsSummary\n        :param TotalCount: Notebook生命周期脚本总数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeNotebookSummaryRequest(AbstractModel):
    """DescribeNotebookSummary请求参数结构体

    """


class DescribeNotebookSummaryResponse(AbstractModel):
    """DescribeNotebookSummary返回参数结构体

    """

    def __init__(self):
        """
        :param AllInstanceCnt: 实例总数\n        :type AllInstanceCnt: int\n        :param BillingInstanceCnt: 计费实例总数\n        :type BillingInstanceCnt: int\n        :param StorageOnlyBillingInstanceCnt: 仅存储计费的实例总数\n        :type StorageOnlyBillingInstanceCnt: int\n        :param ComputingBillingInstanceCnt: 计算和存储都计费的实例总数\n        :type ComputingBillingInstanceCnt: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeTrainingJobRequest(AbstractModel):
    """DescribeTrainingJob请求参数结构体

    """

    def __init__(self):
        """
        :param TrainingJobName: 训练任务名称\n        :type TrainingJobName: str\n        """
        self.TrainingJobName = None


    def _deserialize(self, params):
        self.TrainingJobName = params.get("TrainingJobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingJobResponse(AbstractModel):
    """DescribeTrainingJob返回参数结构体

    """

    def __init__(self):
        """
        :param AlgorithmSpecification: 算法镜像配置\n        :type AlgorithmSpecification: :class:`tencentcloud.tione.v20191022.models.AlgorithmSpecification`\n        :param TrainingJobName: 任务名称\n        :type TrainingJobName: str\n        :param HyperParameters: 算法超级参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type HyperParameters: str\n        :param InputDataConfig: 输入数据配置\n        :type InputDataConfig: list of InputDataConfig\n        :param OutputDataConfig: 输出数据配置\n        :type OutputDataConfig: :class:`tencentcloud.tione.v20191022.models.OutputDataConfig`\n        :param StoppingCondition: 中止条件
注意：此字段可能返回 null，表示取不到有效值。\n        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`\n        :param ResourceConfig: 计算实例配置\n        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`\n        :param VpcConfig: 私有网络配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcConfig: :class:`tencentcloud.tione.v20191022.models.VpcConfig`\n        :param FailureReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailureReason: str\n        :param LastModifiedTime: 最近修改时间\n        :type LastModifiedTime: str\n        :param TrainingStartTime: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type TrainingStartTime: str\n        :param TrainingEndTime: 任务完成时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type TrainingEndTime: str\n        :param ModelArtifacts: 模型输出配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModelArtifacts: :class:`tencentcloud.tione.v20191022.models.ModelArtifacts`\n        :param SecondaryStatus: 详细状态，取值范围
Starting：启动中
Downloading: 准备训练数据
Training: 正在训练
Uploading: 上传训练结果
Completed：已完成
Failed: 失败
MaxRuntimeExceeded: 任务超过最大运行时间
Stopping: 停止中
Stopped：已停止\n        :type SecondaryStatus: str\n        :param SecondaryStatusTransitions: 详细状态事件记录
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecondaryStatusTransitions: list of SecondaryStatusTransition\n        :param RoleName: 角色名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type RoleName: str\n        :param TrainingJobStatus: 训练任务状态，取值范围
InProgress：运行中
Completed: 已完成
Failed: 失败
Stopping: 停止中
Stopped：已停止\n        :type TrainingJobStatus: str\n        :param LogUrl: 训练任务日志链接
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogUrl: str\n        :param InstanceId: 训练任务实例ID\n        :type InstanceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeTrainingJobsRequest(AbstractModel):
    """DescribeTrainingJobs请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param CreationTimeAfter: 创建时间晚于\n        :type CreationTimeAfter: str\n        :param CreationTimeBefore: 创建时间早于\n        :type CreationTimeBefore: str\n        :param NameContains: 根据名称过滤\n        :type NameContains: str\n        :param StatusEquals: 根据状态过滤\n        :type StatusEquals: str\n        :param Filters: 过滤条件。
instance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。
search-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。\n        :type Filters: list of Filter\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingJobsResponse(AbstractModel):
    """DescribeTrainingJobs返回参数结构体

    """

    def __init__(self):
        """
        :param TrainingJobSet: 训练任务列表\n        :type TrainingJobSet: list of TrainingJobSummary\n        :param TotalCount: 训练任务总数目\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class EnvConfig(AbstractModel):
    """环境变量

    """

    def __init__(self):
        """
        :param Name: 名称\n        :type Name: str\n        :param Value: 值\n        :type Value: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSystemDataSource(AbstractModel):
    """文件系统输入数据源

    """

    def __init__(self):
        """
        :param DirectoryPath: 文件系统目录
注意：此字段可能返回 null，表示取不到有效值。\n        :type DirectoryPath: str\n        :param FileSystemType: 文件系统类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileSystemType: str\n        :param FileSystemAccessMode: 文件系统访问模式
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileSystemAccessMode: str\n        :param FileSystemId: 文件系统ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileSystemId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        """
        :param Name: 过滤字段名称\n        :type Name: str\n        :param Values: 过滤字段取值\n        :type Values: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GitConfig(AbstractModel):
    """存储库Git相关配置

    """

    def __init__(self):
        """
        :param RepositoryUrl: git地址\n        :type RepositoryUrl: str\n        :param Branch: 代码分支
注意：此字段可能返回 null，表示取不到有效值。\n        :type Branch: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GitSecret(AbstractModel):
    """Git凭证

    """

    def __init__(self):
        """
        :param NoSecret: 无秘钥，默认选项\n        :type NoSecret: bool\n        :param Secret: Git用户名密码base64编码后的字符串
编码前的内容应为Json字符串，如
{"UserName": "用户名", "Password":"密码"}\n        :type Secret: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputDataConfig(AbstractModel):
    """输入数据配置

    """

    def __init__(self):
        """
        :param ChannelName: 通道名
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChannelName: str\n        :param DataSource: 数据源配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type DataSource: :class:`tencentcloud.tione.v20191022.models.DataSource`\n        :param InputMode: 输入类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type InputMode: str\n        :param ContentType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContentType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelArtifacts(AbstractModel):
    """模型输出

    """

    def __init__(self):
        """
        :param CosModelArtifacts: cos输出路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type CosModelArtifacts: str\n        """
        self.CosModelArtifacts = None


    def _deserialize(self, params):
        self.CosModelArtifacts = params.get("CosModelArtifacts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookInstanceSummary(AbstractModel):
    """notebook实例概览

    """

    def __init__(self):
        """
        :param CreationTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreationTime: str\n        :param LastModifiedTime: 最近修改时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastModifiedTime: str\n        :param NotebookInstanceName: notebook实例名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type NotebookInstanceName: str\n        :param NotebookInstanceStatus: notebook实例状态，取值范围：
Pending: 创建中
Inservice: 运行中
Stopping: 停止中
Stopped: 已停止
Failed: 失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type NotebookInstanceStatus: str\n        :param InstanceType: 算力类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param StartupTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartupTime: str\n        :param Deadline: 运行截止时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type Deadline: str\n        :param StoppingCondition: 自动停止配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`\n        :param Prepay: 是否是预付费实例
注意：此字段可能返回 null，表示取不到有效值。\n        :type Prepay: bool\n        :param BillingLabel: 计费标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type BillingLabel: :class:`tencentcloud.tione.v20191022.models.BillingLabel`\n        :param RuntimeInSeconds: 运行时长，秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuntimeInSeconds: int\n        :param RemainTimeInSeconds: 剩余时长，秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type RemainTimeInSeconds: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookLifecycleScriptsSummary(AbstractModel):
    """notebook生命周期脚本实例概览

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: notebook生命周期脚本名称\n        :type NotebookLifecycleScriptsName: str\n        :param CreationTime: 创建时间\n        :type CreationTime: str\n        :param LastModifiedTime: 修改时间\n        :type LastModifiedTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputDataConfig(AbstractModel):
    """输出数据配置

    """

    def __init__(self):
        """
        :param CosOutputBucket: cos输出桶
注意：此字段可能返回 null，表示取不到有效值。\n        :type CosOutputBucket: str\n        :param CosOutputKeyPrefix: cos输出key前缀
注意：此字段可能返回 null，表示取不到有效值。\n        :type CosOutputKeyPrefix: str\n        :param FileSystemDataSource: 文件系统输出，如果指定了文件系统，那么Cos输出会被忽略
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileSystemDataSource: :class:`tencentcloud.tione.v20191022.models.FileSystemDataSource`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceConfig(AbstractModel):
    """计算资源配置

    """

    def __init__(self):
        """
        :param InstanceCount: 计算实例数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceCount: int\n        :param InstanceType: 计算实例类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param VolumeSizeInGB: 挂载CBS大小（GB）
注意：此字段可能返回 null，表示取不到有效值。\n        :type VolumeSizeInGB: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecondaryStatusTransition(AbstractModel):
    """二级状态流水

    """

    def __init__(self):
        """
        :param StartTime: 状态开始时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTime: str\n        :param EndTime: 状态结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTime: str\n        :param Status: 状态名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param StatusMessage: 状态详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusMessage: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartNotebookInstanceRequest(AbstractModel):
    """StartNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称\n        :type NotebookInstanceName: str\n        :param AutoStopping: 自动停止，可取值Enabled/Disabled
取值为Disabled的时候StoppingCondition将被忽略
取值为Enabled的时候读取StoppingCondition作为自动停止的配置\n        :type AutoStopping: str\n        :param StoppingCondition: 自动停止配置，只在AutoStopping为Enabled的时候生效\n        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartNotebookInstanceResponse(AbstractModel):
    """StartNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopNotebookInstanceRequest(AbstractModel):
    """StopNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称\n        :type NotebookInstanceName: str\n        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopNotebookInstanceResponse(AbstractModel):
    """StopNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopTrainingJobRequest(AbstractModel):
    """StopTrainingJob请求参数结构体

    """

    def __init__(self):
        """
        :param TrainingJobName: 训练任务名称\n        :type TrainingJobName: str\n        """
        self.TrainingJobName = None


    def _deserialize(self, params):
        self.TrainingJobName = params.get("TrainingJobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopTrainingJobResponse(AbstractModel):
    """StopTrainingJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StoppingCondition(AbstractModel):
    """终止条件

    """

    def __init__(self):
        """
        :param MaxRuntimeInSeconds: 最长运行运行时间（秒）
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxRuntimeInSeconds: int\n        :param MaxWaitTimeInSeconds: 最长等待运行时间（秒）
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxWaitTimeInSeconds: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingJobSummary(AbstractModel):
    """训练任务概要

    """

    def __init__(self):
        """
        :param CreationTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreationTime: str\n        :param LastModifiedTime: 最近修改时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastModifiedTime: str\n        :param TrainingJobName: 训练任务名
注意：此字段可能返回 null，表示取不到有效值。\n        :type TrainingJobName: str\n        :param TrainingJobStatus: 训练任务状态，取值范围
InProgress：运行中
Completed: 已完成
Failed: 失败
Stopping: 停止中
Stopped：已停止
注意：此字段可能返回 null，表示取不到有效值。\n        :type TrainingJobStatus: str\n        :param TrainingEndTime: 完成时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type TrainingEndTime: str\n        :param InstanceId: 算了实例Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param ResourceConfig: 资源配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCodeRepositoryRequest(AbstractModel):
    """UpdateCodeRepository请求参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 查询存储库名称\n        :type CodeRepositoryName: str\n        :param GitSecret: Git凭证\n        :type GitSecret: :class:`tencentcloud.tione.v20191022.models.GitSecret`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCodeRepositoryResponse(AbstractModel):
    """UpdateCodeRepository返回参数结构体

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 存储库名称\n        :type CodeRepositoryName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CodeRepositoryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        self.RequestId = params.get("RequestId")


class UpdateNotebookInstanceRequest(AbstractModel):
    """UpdateNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
规则：“^\[a-zA-Z0-9\](-\*\[a-zA-Z0-9\])\*$”\n        :type NotebookInstanceName: str\n        :param RoleArn: 角色的资源描述\n        :type RoleArn: str\n        :param RootAccess: Root访问权限\n        :type RootAccess: str\n        :param VolumeSizeInGB: 数据卷大小(GB)\n        :type VolumeSizeInGB: int\n        :param InstanceType: 算力资源类型\n        :type InstanceType: str\n        :param LifecycleScriptsName: notebook生命周期脚本名称\n        :type LifecycleScriptsName: str\n        :param DisassociateLifecycleScript: 是否解绑生命周期脚本，默认 false。
该值为true时，LifecycleScriptsName将被忽略\n        :type DisassociateLifecycleScript: bool\n        :param DefaultCodeRepository: 默认存储库名称
可以是已创建的存储库名称或者已https://开头的公共git库\n        :type DefaultCodeRepository: str\n        :param AdditionalCodeRepositories: 其他存储库列表
每个元素可以是已创建的存储库名称或者已https://开头的公共git库\n        :type AdditionalCodeRepositories: list of str\n        :param DisassociateDefaultCodeRepository: 是否取消关联默认存储库，默认false
该值为true时，DefaultCodeRepository将被忽略\n        :type DisassociateDefaultCodeRepository: bool\n        :param DisassociateAdditionalCodeRepositories: 是否取消关联其他存储库，默认false
该值为true时，AdditionalCodeRepositories将被忽略\n        :type DisassociateAdditionalCodeRepositories: bool\n        :param ClsAccess: 已弃用，请使用ClsConfig配置。是否开启CLS日志服务，可取值Enabled/Disabled\n        :type ClsAccess: str\n        :param AutoStopping: 自动停止，可取值Enabled/Disabled
取值为Disabled的时候StoppingCondition将被忽略
取值为Enabled的时候读取StoppingCondition作为自动停止的配置\n        :type AutoStopping: str\n        :param StoppingCondition: 自动停止配置，只在AutoStopping为Enabled的时候生效\n        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`\n        :param ClsConfig: 接入日志的配置，默认使用免费日志服务。\n        :type ClsConfig: :class:`tencentcloud.tione.v20191022.models.ClsConfig`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateNotebookInstanceResponse(AbstractModel):
    """UpdateNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateNotebookLifecycleScriptRequest(AbstractModel):
    """UpdateNotebookLifecycleScript请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: notebook生命周期脚本名称\n        :type NotebookLifecycleScriptsName: str\n        :param CreateScript: 创建脚本，base64编码
base64后的脚本长度不能超过16384个字符\n        :type CreateScript: str\n        :param StartScript: 启动脚本，base64编码
base64后的脚本长度不能超过16384个字符\n        :type StartScript: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateNotebookLifecycleScriptResponse(AbstractModel):
    """UpdateNotebookLifecycleScript返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VpcConfig(AbstractModel):
    """VPC配置

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全组id
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityGroupIds: list of str\n        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        