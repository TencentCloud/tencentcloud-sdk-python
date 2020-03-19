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


class CreateNotebookInstanceRequest(AbstractModel):
    """CreateNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        :param InstanceType: Notebook算力类型
        :type InstanceType: str
        :param RoleArn: 角色的资源描述
        :type RoleArn: str
        :param DirectInternetAccess: 外网访问权限，可取值Enabled/Disabled
        :type DirectInternetAccess: str
        :param RootAccess: Root用户权限，可取值Enabled/Disabled
        :type RootAccess: str
        :param SecurityGroupIds: 安全组ID
        :type SecurityGroupIds: list of str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param VolumeSizeInGB: 数据卷大小(GB)
        :type VolumeSizeInGB: int
        :param Tags: Notebook标签
        :type Tags: list of Tag
        """
        self.NotebookInstanceName = None
        self.InstanceType = None
        self.RoleArn = None
        self.DirectInternetAccess = None
        self.RootAccess = None
        self.SecurityGroupIds = None
        self.SubnetId = None
        self.VolumeSizeInGB = None
        self.Tags = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.InstanceType = params.get("InstanceType")
        self.RoleArn = params.get("RoleArn")
        self.DirectInternetAccess = params.get("DirectInternetAccess")
        self.RootAccess = params.get("RootAccess")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.SubnetId = params.get("SubnetId")
        self.VolumeSizeInGB = params.get("VolumeSizeInGB")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateNotebookInstanceResponse(AbstractModel):
    """CreateNotebookInstance返回参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名字
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookInstanceName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookInstanceName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.RequestId = params.get("RequestId")


class CreatePresignedNotebookInstanceUrlRequest(AbstractModel):
    """CreatePresignedNotebookInstanceUrl请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        :param SessionExpirationDurationInSeconds: session有效时间，秒
        :type SessionExpirationDurationInSeconds: int
        """
        self.NotebookInstanceName = None
        self.SessionExpirationDurationInSeconds = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.SessionExpirationDurationInSeconds = params.get("SessionExpirationDurationInSeconds")


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


class CreateTrainingJobRequest(AbstractModel):
    """CreateTrainingJob请求参数结构体

    """

    def __init__(self):
        """
        :param TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        :param AlgorithmSpecification: 算法镜像配置
        :type AlgorithmSpecification: :class:`tencentcloud.tione.v20191022.models.AlgorithmSpecification`
        :param InputDataConfig: 输入数据配置
        :type InputDataConfig: list of InputDataConfig
        :param OutputDataConfig: 输出数据配置
        :type OutputDataConfig: :class:`tencentcloud.tione.v20191022.models.OutputDataConfig`
        :param ResourceConfig: 资源实例配置
        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`
        :param StoppingCondition: 中止条件
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param VpcConfig: 私有网络配置
        :type VpcConfig: :class:`tencentcloud.tione.v20191022.models.VpcConfig`
        :param HyperParameters: 算法超级参数
        :type HyperParameters: str
        :param RoleName: 角色名称
        :type RoleName: str
        :param EnvConfig: 环境变量配置
        :type EnvConfig: list of EnvConfig
        """
        self.TrainingJobName = None
        self.AlgorithmSpecification = None
        self.InputDataConfig = None
        self.OutputDataConfig = None
        self.ResourceConfig = None
        self.StoppingCondition = None
        self.VpcConfig = None
        self.HyperParameters = None
        self.RoleName = None
        self.EnvConfig = None


    def _deserialize(self, params):
        self.TrainingJobName = params.get("TrainingJobName")
        if params.get("AlgorithmSpecification") is not None:
            self.AlgorithmSpecification = AlgorithmSpecification()
            self.AlgorithmSpecification._deserialize(params.get("AlgorithmSpecification"))
        if params.get("InputDataConfig") is not None:
            self.InputDataConfig = []
            for item in params.get("InputDataConfig"):
                obj = InputDataConfig()
                obj._deserialize(item)
                self.InputDataConfig.append(obj)
        if params.get("OutputDataConfig") is not None:
            self.OutputDataConfig = OutputDataConfig()
            self.OutputDataConfig._deserialize(params.get("OutputDataConfig"))
        if params.get("ResourceConfig") is not None:
            self.ResourceConfig = ResourceConfig()
            self.ResourceConfig._deserialize(params.get("ResourceConfig"))
        if params.get("StoppingCondition") is not None:
            self.StoppingCondition = StoppingCondition()
            self.StoppingCondition._deserialize(params.get("StoppingCondition"))
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.HyperParameters = params.get("HyperParameters")
        self.RoleName = params.get("RoleName")
        if params.get("EnvConfig") is not None:
            self.EnvConfig = []
            for item in params.get("EnvConfig"):
                obj = EnvConfig()
                obj._deserialize(item)
                self.EnvConfig.append(obj)


class CreateTrainingJobResponse(AbstractModel):
    """CreateTrainingJob返回参数结构体

    """

    def __init__(self):
        """
        :param TrainingJobName: 训练任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingJobName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeNotebookInstanceRequest(AbstractModel):
    """DescribeNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")


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
        :param SecurityGroupIds: 安全组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param VolumeSizeInGB: 数据卷大小(GB)
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeSizeInGB: int
        :param Url: Notebook实例链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param FailureReason: 创建失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param CreationTime: Notebook实例创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param LastModifiedTime: Notebook实例最近修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedTime: str
        :param NetworkInterfaceId: Notebook实例网卡ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkInterfaceId: str
        :param LogUrl: Notebook实例日志链接
注意：此字段可能返回 null，表示取不到有效值。
        :type LogUrl: str
        :param NotebookInstanceStatus: Notebook实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookInstanceStatus: str
        :param InstanceId: Notebook实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookInstanceName = None
        self.InstanceType = None
        self.RoleArn = None
        self.DirectInternetAccess = None
        self.RootAccess = None
        self.SecurityGroupIds = None
        self.SubnetId = None
        self.VolumeSizeInGB = None
        self.Url = None
        self.FailureReason = None
        self.CreationTime = None
        self.LastModifiedTime = None
        self.NetworkInterfaceId = None
        self.LogUrl = None
        self.NotebookInstanceStatus = None
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.InstanceType = params.get("InstanceType")
        self.RoleArn = params.get("RoleArn")
        self.DirectInternetAccess = params.get("DirectInternetAccess")
        self.RootAccess = params.get("RootAccess")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.SubnetId = params.get("SubnetId")
        self.VolumeSizeInGB = params.get("VolumeSizeInGB")
        self.Url = params.get("Url")
        self.FailureReason = params.get("FailureReason")
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.LogUrl = params.get("LogUrl")
        self.NotebookInstanceStatus = params.get("NotebookInstanceStatus")
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DescribeNotebookInstancesRequest(AbstractModel):
    """DescribeNotebookInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        :param SortBy: 排序字段
        :type SortBy: str
        :param SortOrder: 排序方式
        :type SortOrder: str
        :param CreationTimeAfter: 创建时间晚于
        :type CreationTimeAfter: str
        :param CreationTimeBefore: 创建时间早于
        :type CreationTimeBefore: str
        :param LastModifiedTimeAfter: 最近修改时间晚于
        :type LastModifiedTimeAfter: str
        :param LastModifiedTimeBefore: 最近修改时间早于
        :type LastModifiedTimeBefore: str
        :param NameContains: 根据名称过滤
        :type NameContains: str
        :param StatusEquals: 根据状态过滤
        :type StatusEquals: str
        :param MaxResults: 最大返回个数
        :type MaxResults: int
        """
        self.Offset = None
        self.Limit = None
        self.SortBy = None
        self.SortOrder = None
        self.CreationTimeAfter = None
        self.CreationTimeBefore = None
        self.LastModifiedTimeAfter = None
        self.LastModifiedTimeBefore = None
        self.NameContains = None
        self.StatusEquals = None
        self.MaxResults = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.SortOrder = params.get("SortOrder")
        self.CreationTimeAfter = params.get("CreationTimeAfter")
        self.CreationTimeBefore = params.get("CreationTimeBefore")
        self.LastModifiedTimeAfter = params.get("LastModifiedTimeAfter")
        self.LastModifiedTimeBefore = params.get("LastModifiedTimeBefore")
        self.NameContains = params.get("NameContains")
        self.StatusEquals = params.get("StatusEquals")
        self.MaxResults = params.get("MaxResults")


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


class DescribeTrainingJobResponse(AbstractModel):
    """DescribeTrainingJob返回参数结构体

    """

    def __init__(self):
        """
        :param AlgorithmSpecification: 算法镜像配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgorithmSpecification: :class:`tencentcloud.tione.v20191022.models.AlgorithmSpecification`
        :param TrainingJobName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingJobName: str
        :param HyperParameters: 算法超级参数
注意：此字段可能返回 null，表示取不到有效值。
        :type HyperParameters: str
        :param InputDataConfig: 输入数据配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InputDataConfig: list of InputDataConfig
        :param OutputDataConfig: 输出数据配置
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputDataConfig: :class:`tencentcloud.tione.v20191022.models.OutputDataConfig`
        :param StoppingCondition: 中止条件
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param ResourceConfig: 计算实例配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`
        :param VpcConfig: 私有网络配置
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcConfig: :class:`tencentcloud.tione.v20191022.models.VpcConfig`
        :param FailureReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param LastModifiedTime: 最近修改时间
注意：此字段可能返回 null，表示取不到有效值。
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
        :param SecondaryStatus: 详细状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondaryStatus: str
        :param SecondaryStatusTransitions: 详细状态事件记录
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondaryStatusTransitions: list of SecondaryStatusTransition
        :param RoleName: 角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        :param TrainingJobStatus: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingJobStatus: str
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
        self.RequestId = params.get("RequestId")


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
        :param NotebookInstanceStatus: notebook实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookInstanceStatus: str
        :param InstanceType: 算力类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param InstanceId: 算力Id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        """
        self.CreationTime = None
        self.LastModifiedTime = None
        self.NotebookInstanceName = None
        self.NotebookInstanceStatus = None
        self.InstanceType = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.NotebookInstanceStatus = params.get("NotebookInstanceStatus")
        self.InstanceType = params.get("InstanceType")
        self.InstanceId = params.get("InstanceId")


class OutputDataConfig(AbstractModel):
    """输出数据配置

    """

    def __init__(self):
        """
        :param CosOutputBucket: cos桶
注意：此字段可能返回 null，表示取不到有效值。
        :type CosOutputBucket: str
        :param CosOutputKeyPrefix: cos文件key
注意：此字段可能返回 null，表示取不到有效值。
        :type CosOutputKeyPrefix: str
        """
        self.CosOutputBucket = None
        self.CosOutputKeyPrefix = None


    def _deserialize(self, params):
        self.CosOutputBucket = params.get("CosOutputBucket")
        self.CosOutputKeyPrefix = params.get("CosOutputKeyPrefix")


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


class StartNotebookInstanceRequest(AbstractModel):
    """StartNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")


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


class StoppingCondition(AbstractModel):
    """终止条件

    """

    def __init__(self):
        """
        :param MaxRuntimeInSeconds: 最长运行运行时间（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRuntimeInSeconds: int
        """
        self.MaxRuntimeInSeconds = None


    def _deserialize(self, params):
        self.MaxRuntimeInSeconds = params.get("MaxRuntimeInSeconds")


class Tag(AbstractModel):
    """notebook标签

    """

    def __init__(self):
        """
        :param Key: key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class UpdateNotebookInstanceRequest(AbstractModel):
    """UpdateNotebookInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook实例名称
        :type NotebookInstanceName: str
        :param RoleArn: 角色的资源描述
        :type RoleArn: str
        :param RootAccess: Root访问权限
        :type RootAccess: str
        :param VolumeSizeInGB: 数据卷大小(GB)
        :type VolumeSizeInGB: int
        :param InstanceType: 算力资源类型
        :type InstanceType: str
        """
        self.NotebookInstanceName = None
        self.RoleArn = None
        self.RootAccess = None
        self.VolumeSizeInGB = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.RoleArn = params.get("RoleArn")
        self.RootAccess = params.get("RootAccess")
        self.VolumeSizeInGB = params.get("VolumeSizeInGB")
        self.InstanceType = params.get("InstanceType")


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