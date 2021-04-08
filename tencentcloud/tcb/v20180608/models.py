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


class AuthDomain(AbstractModel):
    """合法域名

    """

    def __init__(self):
        """
        :param Id: 域名ID
        :type Id: str
        :param Domain: 域名
        :type Domain: str
        :param Type: 域名类型。包含以下取值：
<li>SYSTEM</li>
<li>USER</li>
        :type Type: str
        :param Status: 状态。包含以下取值：
<li>ENABLE</li>
<li>DISABLE</li>
        :type Status: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self.Id = None
        self.Domain = None
        self.Type = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class CheckTcbServiceRequest(AbstractModel):
    """CheckTcbService请求参数结构体

    """


class CheckTcbServiceResponse(AbstractModel):
    """CheckTcbService返回参数结构体

    """

    def __init__(self):
        """
        :param Initialized: true表示已开通
        :type Initialized: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Initialized = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Initialized = params.get("Initialized")
        self.RequestId = params.get("RequestId")


class CloudBaseCapabilities(AbstractModel):
    """cloudrun安全特性能力


    """

    def __init__(self):
        """
        :param Add: 启用安全能力项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Add: list of str
        :param Drop: 禁用安全能力向列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Drop: list of str
        """
        self.Add = None
        self.Drop = None


    def _deserialize(self, params):
        self.Add = params.get("Add")
        self.Drop = params.get("Drop")


class CloudBaseCodeRepoDetail(AbstractModel):
    """代码仓库里 Repo的信息描述

    """

    def __init__(self):
        """
        :param Name: repo的名字
        :type Name: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoName`
        :param Url: repo的url
        :type Url: str
        """
        self.Name = None
        self.Url = None


    def _deserialize(self, params):
        if params.get("Name") is not None:
            self.Name = CloudBaseCodeRepoName()
            self.Name._deserialize(params.get("Name"))
        self.Url = params.get("Url")


class CloudBaseCodeRepoName(AbstractModel):
    """代码仓库 repo的名字

    """

    def __init__(self):
        """
        :param Name: repo的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param FullName: repo的完整全名
注意：此字段可能返回 null，表示取不到有效值。
        :type FullName: str
        """
        self.Name = None
        self.FullName = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.FullName = params.get("FullName")


class CloudBaseEsInfo(AbstractModel):
    """es信息

    """

    def __init__(self):
        """
        :param Id: es的id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param SecretName: secret名字
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretName: str
        :param Ip: ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: str
        :param Account: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Account: str
        :param Password: 密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        """
        self.Id = None
        self.SecretName = None
        self.Ip = None
        self.Port = None
        self.Index = None
        self.Account = None
        self.Password = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.SecretName = params.get("SecretName")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Index = params.get("Index")
        self.Account = params.get("Account")
        self.Password = params.get("Password")


class CloudBaseProjectVersion(AbstractModel):
    """云开发项目版本

    """

    def __init__(self):
        """
        :param Name: 项目名
        :type Name: str
        :param Sam: SAM json
注意：此字段可能返回 null，表示取不到有效值。
        :type Sam: str
        :param Source: 来源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: :class:`tencentcloud.tcb.v20180608.models.CodeSource`
        :param CreateTime: 创建时间, unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param UpdateTime: 更新时间 ,unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param Status: 项目状态, 枚举值: 
        "creatingEnv"-创建环境中
	"createEnvFail"-创建环境失败
	"building"-构建中
	"buildFail"-构建失败
	"deploying"-部署中
	 "deployFail"-部署失败
	 "success"-部署成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Parameters: 环境变量
注意：此字段可能返回 null，表示取不到有效值。
        :type Parameters: list of KVPair
        :param Type: 项目类型, 枚举值:
"framework-oneclick" 控制台一键部署
"framework-local-oneclick" cli本地一键部署
"qci-extension-cicd" 内网coding ci cd
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param CIId: ci的id
注意：此字段可能返回 null，表示取不到有效值。
        :type CIId: str
        :param CDId: cd的id
注意：此字段可能返回 null，表示取不到有效值。
        :type CDId: str
        :param EnvId: 环境id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param VersionNum: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionNum: int
        :param FailReason: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param RcJson: rc.json内容
注意：此字段可能返回 null，表示取不到有效值。
        :type RcJson: str
        :param AddonConfig: 插件配置内容
注意：此字段可能返回 null，表示取不到有效值。
        :type AddonConfig: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param NetworkConfig: 网络配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkConfig: str
        :param ExtensionId: 扩展id
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtensionId: str
        :param FailType: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FailType: str
        :param RepoUrl: 私有仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoUrl: str
        :param AutoDeployOnCodeChange: 是否私有仓库代码变更触发自动部署
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoDeployOnCodeChange: bool
        """
        self.Name = None
        self.Sam = None
        self.Source = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Status = None
        self.Parameters = None
        self.Type = None
        self.CIId = None
        self.CDId = None
        self.EnvId = None
        self.VersionNum = None
        self.FailReason = None
        self.RcJson = None
        self.AddonConfig = None
        self.Tags = None
        self.NetworkConfig = None
        self.ExtensionId = None
        self.FailType = None
        self.RepoUrl = None
        self.AutoDeployOnCodeChange = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Sam = params.get("Sam")
        if params.get("Source") is not None:
            self.Source = CodeSource()
            self.Source._deserialize(params.get("Source"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = KVPair()
                obj._deserialize(item)
                self.Parameters.append(obj)
        self.Type = params.get("Type")
        self.CIId = params.get("CIId")
        self.CDId = params.get("CDId")
        self.EnvId = params.get("EnvId")
        self.VersionNum = params.get("VersionNum")
        self.FailReason = params.get("FailReason")
        self.RcJson = params.get("RcJson")
        self.AddonConfig = params.get("AddonConfig")
        self.Tags = params.get("Tags")
        self.NetworkConfig = params.get("NetworkConfig")
        self.ExtensionId = params.get("ExtensionId")
        self.FailType = params.get("FailType")
        self.RepoUrl = params.get("RepoUrl")
        self.AutoDeployOnCodeChange = params.get("AutoDeployOnCodeChange")


class CloudBaseRunImageInfo(AbstractModel):
    """CloudBaseRun 镜像信息

    """

    def __init__(self):
        """
        :param RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param IsPublic: 是否公有
        :type IsPublic: bool
        :param TagName: 镜像tag名称
        :type TagName: str
        :param ServerAddr: 镜像server
        :type ServerAddr: str
        :param ImageUrl: 镜像拉取地址
        :type ImageUrl: str
        """
        self.RepositoryName = None
        self.IsPublic = None
        self.TagName = None
        self.ServerAddr = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.RepositoryName = params.get("RepositoryName")
        self.IsPublic = params.get("IsPublic")
        self.TagName = params.get("TagName")
        self.ServerAddr = params.get("ServerAddr")
        self.ImageUrl = params.get("ImageUrl")


class CloudBaseRunImageSecretInfo(AbstractModel):
    """ImageSecretInfo的信息

    """

    def __init__(self):
        """
        :param RegistryServer: 镜像地址
        :type RegistryServer: str
        :param UserName: 用户名
        :type UserName: str
        :param Password: 仓库密码
        :type Password: str
        :param Email: 邮箱
        :type Email: str
        """
        self.RegistryServer = None
        self.UserName = None
        self.Password = None
        self.Email = None


    def _deserialize(self, params):
        self.RegistryServer = params.get("RegistryServer")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.Email = params.get("Email")


class CloudBaseRunNfsVolumeSource(AbstractModel):
    """nfs挂载资源

    """

    def __init__(self):
        """
        :param Server: NFS挂载Server
        :type Server: str
        :param Path: Server路径
        :type Path: str
        :param ReadOnly: 是否只读
        :type ReadOnly: bool
        :param SecretName: secret名称
        :type SecretName: str
        :param EnableEmptyDirVolume: 临时目录
        :type EnableEmptyDirVolume: bool
        """
        self.Server = None
        self.Path = None
        self.ReadOnly = None
        self.SecretName = None
        self.EnableEmptyDirVolume = None


    def _deserialize(self, params):
        self.Server = params.get("Server")
        self.Path = params.get("Path")
        self.ReadOnly = params.get("ReadOnly")
        self.SecretName = params.get("SecretName")
        self.EnableEmptyDirVolume = params.get("EnableEmptyDirVolume")


class CloudBaseRunSideSpec(AbstractModel):
    """CloudBaseRun 的 Side 描述定义

    """

    def __init__(self):
        """
        :param ContainerImage: 容器镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerImage: str
        :param ContainerPort: 容器端口
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerPort: int
        :param ContainerName: 容器的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerName: str
        :param EnvVar: kv的json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvVar: str
        :param InitialDelaySeconds: InitialDelaySeconds 延迟多长时间启动健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param Cpu: CPU大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param Mem: 内存大小（单位：M）
注意：此字段可能返回 null，表示取不到有效值。
        :type Mem: int
        :param Security: 安全特性
注意：此字段可能返回 null，表示取不到有效值。
        :type Security: :class:`tencentcloud.tcb.v20180608.models.CloudBaseSecurityContext`
        :param VolumeMountInfos: 挂载信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeMountInfos: list of CloudBaseRunVolumeMount
        """
        self.ContainerImage = None
        self.ContainerPort = None
        self.ContainerName = None
        self.EnvVar = None
        self.InitialDelaySeconds = None
        self.Cpu = None
        self.Mem = None
        self.Security = None
        self.VolumeMountInfos = None


    def _deserialize(self, params):
        self.ContainerImage = params.get("ContainerImage")
        self.ContainerPort = params.get("ContainerPort")
        self.ContainerName = params.get("ContainerName")
        self.EnvVar = params.get("EnvVar")
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        if params.get("Security") is not None:
            self.Security = CloudBaseSecurityContext()
            self.Security._deserialize(params.get("Security"))
        if params.get("VolumeMountInfos") is not None:
            self.VolumeMountInfos = []
            for item in params.get("VolumeMountInfos"):
                obj = CloudBaseRunVolumeMount()
                obj._deserialize(item)
                self.VolumeMountInfos.append(obj)


class CloudBaseRunVolumeMount(AbstractModel):
    """cfs挂载点

    """

    def __init__(self):
        """
        :param Name: 资源名
        :type Name: str
        :param MountPath: 挂载路径
        :type MountPath: str
        :param ReadOnly: 是否只读
        :type ReadOnly: bool
        :param NfsVolumes: Nfs挂载信息
        :type NfsVolumes: list of CloudBaseRunNfsVolumeSource
        """
        self.Name = None
        self.MountPath = None
        self.ReadOnly = None
        self.NfsVolumes = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.MountPath = params.get("MountPath")
        self.ReadOnly = params.get("ReadOnly")
        if params.get("NfsVolumes") is not None:
            self.NfsVolumes = []
            for item in params.get("NfsVolumes"):
                obj = CloudBaseRunNfsVolumeSource()
                obj._deserialize(item)
                self.NfsVolumes.append(obj)


class CloudBaseRunVpcInfo(AbstractModel):
    """vpc信息

    """

    def __init__(self):
        """
        :param VpcId: vpc的id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetIds: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param CreateType: 创建类型(0=继承; 1=新建; 2=指定)
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateType: int
        """
        self.VpcId = None
        self.SubnetIds = None
        self.CreateType = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.CreateType = params.get("CreateType")


class CloudBaseRunVpcSubnet(AbstractModel):
    """子网信息

    """

    def __init__(self):
        """
        :param Id: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param Cidr: 子网的ipv4
注意：此字段可能返回 null，表示取不到有效值。
        :type Cidr: str
        :param Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Target: subnet类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Target: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.Id = None
        self.Cidr = None
        self.Zone = None
        self.Type = None
        self.Target = None
        self.Region = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Cidr = params.get("Cidr")
        self.Zone = params.get("Zone")
        self.Type = params.get("Type")
        self.Target = params.get("Target")
        self.Region = params.get("Region")
        self.Name = params.get("Name")


class CloudBaseSecurityContext(AbstractModel):
    """cloudrun安全特性


    """

    def __init__(self):
        """
        :param Capabilities: 安全特性
注意：此字段可能返回 null，表示取不到有效值。
        :type Capabilities: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCapabilities`
        """
        self.Capabilities = None


    def _deserialize(self, params):
        if params.get("Capabilities") is not None:
            self.Capabilities = CloudBaseCapabilities()
            self.Capabilities._deserialize(params.get("Capabilities"))


class CloudRunServiceSimpleVersionSnapshot(AbstractModel):
    """CloudRunServiceSimpleVersionSnapshot 信息

    """

    def __init__(self):
        """
        :param VersionName: 版本名
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param Remark: 版本备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param Cpu: cpu规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: float
        :param Mem: 内存规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Mem: float
        :param MinNum: 最小副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinNum: int
        :param MaxNum: 最大副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxNum: int
        :param ImageUrl: 镜像url
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param PolicyType: 扩容策略
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param PolicyThreshold: 策略阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyThreshold: int
        :param EnvParams: 环境参数
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvParams: str
        :param ContainerPort: 容器端口
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerPort: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param UploadType: 更新类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadType: str
        :param DockerfilePath: dockerfile路径
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerfilePath: str
        :param BuildDir: 构建路径
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildDir: str
        :param RepoType: repo类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoType: str
        :param Repo: 仓库
注意：此字段可能返回 null，表示取不到有效值。
        :type Repo: str
        :param Branch: 分支
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        :param EnvId: 环境id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param ServerName: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param PackageName: package名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param PackageVersion: package版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param CustomLogs: 自定义log路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLogs: str
        :param InitialDelaySeconds: 延时健康检查时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param SnapshotName: snapshot名
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotName: str
        :param ImageInfo: 镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageInfo`
        :param CodeDetail: 代码仓库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeDetail: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoDetail`
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.VersionName = None
        self.Remark = None
        self.Cpu = None
        self.Mem = None
        self.MinNum = None
        self.MaxNum = None
        self.ImageUrl = None
        self.PolicyType = None
        self.PolicyThreshold = None
        self.EnvParams = None
        self.ContainerPort = None
        self.CreateTime = None
        self.UpdateTime = None
        self.UploadType = None
        self.DockerfilePath = None
        self.BuildDir = None
        self.RepoType = None
        self.Repo = None
        self.Branch = None
        self.EnvId = None
        self.ServerName = None
        self.PackageName = None
        self.PackageVersion = None
        self.CustomLogs = None
        self.InitialDelaySeconds = None
        self.SnapshotName = None
        self.ImageInfo = None
        self.CodeDetail = None
        self.Status = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.Remark = params.get("Remark")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.MinNum = params.get("MinNum")
        self.MaxNum = params.get("MaxNum")
        self.ImageUrl = params.get("ImageUrl")
        self.PolicyType = params.get("PolicyType")
        self.PolicyThreshold = params.get("PolicyThreshold")
        self.EnvParams = params.get("EnvParams")
        self.ContainerPort = params.get("ContainerPort")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.UploadType = params.get("UploadType")
        self.DockerfilePath = params.get("DockerfilePath")
        self.BuildDir = params.get("BuildDir")
        self.RepoType = params.get("RepoType")
        self.Repo = params.get("Repo")
        self.Branch = params.get("Branch")
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.PackageName = params.get("PackageName")
        self.PackageVersion = params.get("PackageVersion")
        self.CustomLogs = params.get("CustomLogs")
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        self.SnapshotName = params.get("SnapshotName")
        if params.get("ImageInfo") is not None:
            self.ImageInfo = CloudBaseRunImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("CodeDetail") is not None:
            self.CodeDetail = CloudBaseCodeRepoDetail()
            self.CodeDetail._deserialize(params.get("CodeDetail"))
        self.Status = params.get("Status")


class CloudRunServiceVolume(AbstractModel):
    """服务的volume

    """

    def __init__(self):
        """
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param NFS: NFS的挂载方式
注意：此字段可能返回 null，表示取不到有效值。
        :type NFS: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunNfsVolumeSource`
        :param SecretName: secret名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretName: str
        :param EnableEmptyDirVolume: 是否开启临时目录
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableEmptyDirVolume: bool
        """
        self.Name = None
        self.NFS = None
        self.SecretName = None
        self.EnableEmptyDirVolume = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("NFS") is not None:
            self.NFS = CloudBaseRunNfsVolumeSource()
            self.NFS._deserialize(params.get("NFS"))
        self.SecretName = params.get("SecretName")
        self.EnableEmptyDirVolume = params.get("EnableEmptyDirVolume")


class CodeSource(AbstractModel):
    """云开发项目来源

    """

    def __init__(self):
        """
        :param Type: 类型, 可能的枚举: "coding","package","package_url","github","gitlab","gitee","rawcode"
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Url: 下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param WorkDir: 工作目录
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkDir: str
        :param CodingPackageName: code包名, type为coding的时候需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type CodingPackageName: str
        :param CodingPackageVersion: coding版本名, type为coding的时候需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type CodingPackageVersion: str
        :param RawCode: 源码
注意：此字段可能返回 null，表示取不到有效值。
        :type RawCode: str
        :param Branch: 代码分支
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        """
        self.Type = None
        self.Url = None
        self.Name = None
        self.WorkDir = None
        self.CodingPackageName = None
        self.CodingPackageVersion = None
        self.RawCode = None
        self.Branch = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Url = params.get("Url")
        self.Name = params.get("Name")
        self.WorkDir = params.get("WorkDir")
        self.CodingPackageName = params.get("CodingPackageName")
        self.CodingPackageVersion = params.get("CodingPackageVersion")
        self.RawCode = params.get("RawCode")
        self.Branch = params.get("Branch")


class CommonServiceAPIRequest(AbstractModel):
    """CommonServiceAPI请求参数结构体

    """

    def __init__(self):
        """
        :param Service: Service名，需要转发访问的接口名
        :type Service: str
        :param JSONData: 需要转发的云API参数，要转成JSON格式
        :type JSONData: str
        """
        self.Service = None
        self.JSONData = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.JSONData = params.get("JSONData")


class CommonServiceAPIResponse(AbstractModel):
    """CommonServiceAPI返回参数结构体

    """

    def __init__(self):
        """
        :param JSONResp: json格式response
        :type JSONResp: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JSONResp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JSONResp = params.get("JSONResp")
        self.RequestId = params.get("RequestId")


class CreateAndDeployCloudBaseProjectRequest(AbstractModel):
    """CreateAndDeployCloudBaseProject请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 项目名
        :type Name: str
        :param Source: 来源
        :type Source: :class:`tencentcloud.tcb.v20180608.models.CodeSource`
        :param EnvId: 环境id
        :type EnvId: str
        :param Type: 项目类型, 枚举值为: framework-oneclick,qci-extension-cicd
        :type Type: str
        :param Parameters: 环境变量
        :type Parameters: list of KVPair
        :param EnvAlias: 环境别名
        :type EnvAlias: str
        :param RcJson: rc.json的内容
        :type RcJson: str
        :param AddonConfig: 插件配置内容
        :type AddonConfig: str
        :param Tags: 标签
        :type Tags: list of str
        :param NetworkConfig: 网络配置
        :type NetworkConfig: str
        :param FreeQuota: 免费额度的"basic", 不使用的用""
        :type FreeQuota: str
        :param AutoDeployOnCodeChange: 是否代码变更触发自动部署
        :type AutoDeployOnCodeChange: bool
        :param RepoUrl: 私有仓库地址
        :type RepoUrl: str
        """
        self.Name = None
        self.Source = None
        self.EnvId = None
        self.Type = None
        self.Parameters = None
        self.EnvAlias = None
        self.RcJson = None
        self.AddonConfig = None
        self.Tags = None
        self.NetworkConfig = None
        self.FreeQuota = None
        self.AutoDeployOnCodeChange = None
        self.RepoUrl = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Source") is not None:
            self.Source = CodeSource()
            self.Source._deserialize(params.get("Source"))
        self.EnvId = params.get("EnvId")
        self.Type = params.get("Type")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = KVPair()
                obj._deserialize(item)
                self.Parameters.append(obj)
        self.EnvAlias = params.get("EnvAlias")
        self.RcJson = params.get("RcJson")
        self.AddonConfig = params.get("AddonConfig")
        self.Tags = params.get("Tags")
        self.NetworkConfig = params.get("NetworkConfig")
        self.FreeQuota = params.get("FreeQuota")
        self.AutoDeployOnCodeChange = params.get("AutoDeployOnCodeChange")
        self.RepoUrl = params.get("RepoUrl")


class CreateAndDeployCloudBaseProjectResponse(AbstractModel):
    """CreateAndDeployCloudBaseProject返回参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境Id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.RequestId = params.get("RequestId")


class CreateAuthDomainRequest(AbstractModel):
    """CreateAuthDomain请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param Domains: 安全域名
        :type Domains: list of str
        """
        self.EnvId = None
        self.Domains = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Domains = params.get("Domains")


class CreateAuthDomainResponse(AbstractModel):
    """CreateAuthDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCloudBaseRunResourceRequest(AbstractModel):
    """CreateCloudBaseRunResource请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param VpcId: vpc的ID
        :type VpcId: str
        :param SubnetIds: 子网ID列表，当VpcId不为空，SubnetIds也不能为空
        :type SubnetIds: list of str
        """
        self.EnvId = None
        self.VpcId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")


class CreateCloudBaseRunResourceResponse(AbstractModel):
    """CreateCloudBaseRunResource返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回集群创建是否成功 succ为成功。并且中间无err
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateCloudBaseRunServerVersionRequest(AbstractModel):
    """CreateCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param UploadType: 枚举（package/repository/image)
        :type UploadType: str
        :param FlowRatio: 流量占比
        :type FlowRatio: int
        :param Cpu: Cpu的大小，单位：核
        :type Cpu: float
        :param Mem: Mem的大小，单位：G
        :type Mem: float
        :param MinNum: 最小副本数，最小值：0
        :type MinNum: int
        :param MaxNum: 副本最大数，最大值：50
        :type MaxNum: int
        :param PolicyType: 策略类型(枚举值：比如cpu)
        :type PolicyType: str
        :param PolicyThreshold: 策略阈值
        :type PolicyThreshold: int
        :param ContainerPort: 服务端口
        :type ContainerPort: int
        :param ServerName: 服务名称
        :type ServerName: str
        :param RepositoryType: repository的类型(coding/gitlab/github/coding)
        :type RepositoryType: str
        :param DockerfilePath: Dockerfile地址
        :type DockerfilePath: str
        :param BuildDir: 构建目录
        :type BuildDir: str
        :param EnvParams: 环境变量
        :type EnvParams: str
        :param Repository: repository地址
        :type Repository: str
        :param Branch: 分支
        :type Branch: str
        :param VersionRemark: 版本备注
        :type VersionRemark: str
        :param PackageName: 代码包名字
        :type PackageName: str
        :param PackageVersion: 代码包的版本
        :type PackageVersion: str
        :param ImageInfo: Image的详情
        :type ImageInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageInfo`
        :param CodeDetail: Github等拉取代码的详情
        :type CodeDetail: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoDetail`
        :param ImageSecretInfo: 私有镜像秘钥信息
        :type ImageSecretInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageSecretInfo`
        :param ImagePullSecret: 私有镜像 认证名称
        :type ImagePullSecret: str
        :param CustomLogs: 用户自定义采集日志路径
        :type CustomLogs: str
        :param InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）
        :type InitialDelaySeconds: int
        :param MountVolumeInfo: cfs挂载信息
        :type MountVolumeInfo: list of CloudBaseRunVolumeMount
        :param AccessType: 4 代表只能微信链路访问
        :type AccessType: int
        :param EsInfo: es信息
        :type EsInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseEsInfo`
        :param EnableUnion: 是否使用统一域名
        :type EnableUnion: bool
        :param OperatorRemark: 操作备注
        :type OperatorRemark: str
        :param ServerPath: 服务路径
        :type ServerPath: str
        :param ImageReuseKey: 镜像复用的key
        :type ImageReuseKey: str
        :param SidecarSpecs: 容器的描述文件
        :type SidecarSpecs: list of CloudBaseRunSideSpec
        :param Security: 安全特性
        :type Security: :class:`tencentcloud.tcb.v20180608.models.CloudBaseSecurityContext`
        :param ServiceVolumes: 服务磁盘挂载
        :type ServiceVolumes: list of CloudRunServiceVolume
        """
        self.EnvId = None
        self.UploadType = None
        self.FlowRatio = None
        self.Cpu = None
        self.Mem = None
        self.MinNum = None
        self.MaxNum = None
        self.PolicyType = None
        self.PolicyThreshold = None
        self.ContainerPort = None
        self.ServerName = None
        self.RepositoryType = None
        self.DockerfilePath = None
        self.BuildDir = None
        self.EnvParams = None
        self.Repository = None
        self.Branch = None
        self.VersionRemark = None
        self.PackageName = None
        self.PackageVersion = None
        self.ImageInfo = None
        self.CodeDetail = None
        self.ImageSecretInfo = None
        self.ImagePullSecret = None
        self.CustomLogs = None
        self.InitialDelaySeconds = None
        self.MountVolumeInfo = None
        self.AccessType = None
        self.EsInfo = None
        self.EnableUnion = None
        self.OperatorRemark = None
        self.ServerPath = None
        self.ImageReuseKey = None
        self.SidecarSpecs = None
        self.Security = None
        self.ServiceVolumes = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.UploadType = params.get("UploadType")
        self.FlowRatio = params.get("FlowRatio")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.MinNum = params.get("MinNum")
        self.MaxNum = params.get("MaxNum")
        self.PolicyType = params.get("PolicyType")
        self.PolicyThreshold = params.get("PolicyThreshold")
        self.ContainerPort = params.get("ContainerPort")
        self.ServerName = params.get("ServerName")
        self.RepositoryType = params.get("RepositoryType")
        self.DockerfilePath = params.get("DockerfilePath")
        self.BuildDir = params.get("BuildDir")
        self.EnvParams = params.get("EnvParams")
        self.Repository = params.get("Repository")
        self.Branch = params.get("Branch")
        self.VersionRemark = params.get("VersionRemark")
        self.PackageName = params.get("PackageName")
        self.PackageVersion = params.get("PackageVersion")
        if params.get("ImageInfo") is not None:
            self.ImageInfo = CloudBaseRunImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("CodeDetail") is not None:
            self.CodeDetail = CloudBaseCodeRepoDetail()
            self.CodeDetail._deserialize(params.get("CodeDetail"))
        if params.get("ImageSecretInfo") is not None:
            self.ImageSecretInfo = CloudBaseRunImageSecretInfo()
            self.ImageSecretInfo._deserialize(params.get("ImageSecretInfo"))
        self.ImagePullSecret = params.get("ImagePullSecret")
        self.CustomLogs = params.get("CustomLogs")
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        if params.get("MountVolumeInfo") is not None:
            self.MountVolumeInfo = []
            for item in params.get("MountVolumeInfo"):
                obj = CloudBaseRunVolumeMount()
                obj._deserialize(item)
                self.MountVolumeInfo.append(obj)
        self.AccessType = params.get("AccessType")
        if params.get("EsInfo") is not None:
            self.EsInfo = CloudBaseEsInfo()
            self.EsInfo._deserialize(params.get("EsInfo"))
        self.EnableUnion = params.get("EnableUnion")
        self.OperatorRemark = params.get("OperatorRemark")
        self.ServerPath = params.get("ServerPath")
        self.ImageReuseKey = params.get("ImageReuseKey")
        if params.get("SidecarSpecs") is not None:
            self.SidecarSpecs = []
            for item in params.get("SidecarSpecs"):
                obj = CloudBaseRunSideSpec()
                obj._deserialize(item)
                self.SidecarSpecs.append(obj)
        if params.get("Security") is not None:
            self.Security = CloudBaseSecurityContext()
            self.Security._deserialize(params.get("Security"))
        if params.get("ServiceVolumes") is not None:
            self.ServiceVolumes = []
            for item in params.get("ServiceVolumes"):
                obj = CloudRunServiceVolume()
                obj._deserialize(item)
                self.ServiceVolumes.append(obj)


class CreateCloudBaseRunServerVersionResponse(AbstractModel):
    """CreateCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 状态(creating/succ)
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param VersionName: 版本名称（只有Result为succ的时候，才会返回VersionName)
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param RunId: 操作记录id
注意：此字段可能返回 null，表示取不到有效值。
        :type RunId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.VersionName = None
        self.RunId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.VersionName = params.get("VersionName")
        self.RunId = params.get("RunId")
        self.RequestId = params.get("RequestId")


class CreateHostingDomainRequest(AbstractModel):
    """CreateHostingDomain请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param Domain: 域名
        :type Domain: str
        :param CertId: 证书ID
        :type CertId: str
        """
        self.EnvId = None
        self.Domain = None
        self.CertId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Domain = params.get("Domain")
        self.CertId = params.get("CertId")


class CreateHostingDomainResponse(AbstractModel):
    """CreateHostingDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePostpayPackageRequest(AbstractModel):
    """CreatePostpayPackage请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID，需要系统自动创建环境时，此字段不传
        :type EnvId: str
        :param WxAppId: 微信 AppId，微信必传
        :type WxAppId: str
        :param Source: 付费来源
<li>miniapp</li>
<li>qcloud</li>
        :type Source: str
        :param FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。
        :type FreeQuota: str
        :param EnvSource: 环境创建来源，取值：
<li>miniapp</li>
<li>qcloud</li>
用法同CreateEnv接口的Source参数
和 Channel 参数同时传，或者同时不传；EnvId 为空时必传。
        :type EnvSource: str
        :param Alias: 环境别名，要以a-z开头，不能包含  a-z,0-9,-  以外的字符
        :type Alias: str
        :param Channel: 如果envsource为miniapp, channel可以为ide或api;
如果envsource为qcloud, channel可以为qc_console,cocos, qq, cloudgame,dcloud,serverless_framework
和 EnvSource 参数同时传，或者同时不传；EnvId 为空时必传。
        :type Channel: str
        :param ExtensionId: 扩展ID
        :type ExtensionId: str
        :param Flag: 订单标记。建议使用方统一转大小写之后再判断。
<li>QuickStart：快速启动来源</li>
<li>Activity：活动来源</li>
        :type Flag: str
        """
        self.EnvId = None
        self.WxAppId = None
        self.Source = None
        self.FreeQuota = None
        self.EnvSource = None
        self.Alias = None
        self.Channel = None
        self.ExtensionId = None
        self.Flag = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.WxAppId = params.get("WxAppId")
        self.Source = params.get("Source")
        self.FreeQuota = params.get("FreeQuota")
        self.EnvSource = params.get("EnvSource")
        self.Alias = params.get("Alias")
        self.Channel = params.get("Channel")
        self.ExtensionId = params.get("ExtensionId")
        self.Flag = params.get("Flag")


class CreatePostpayPackageResponse(AbstractModel):
    """CreatePostpayPackage返回参数结构体

    """

    def __init__(self):
        """
        :param TranId: 后付费订单号
        :type TranId: str
        :param EnvId: 环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TranId = None
        self.EnvId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.EnvId = params.get("EnvId")
        self.RequestId = params.get("RequestId")


class CreateStaticStoreRequest(AbstractModel):
    """CreateStaticStore请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param EnableUnion: 是否启用统一域名
        :type EnableUnion: bool
        """
        self.EnvId = None
        self.EnableUnion = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnableUnion = params.get("EnableUnion")


class CreateStaticStoreResponse(AbstractModel):
    """CreateStaticStore返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建静态资源结果(succ/fail)
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DatabasesInfo(AbstractModel):
    """数据库资源信息

    """

    def __init__(self):
        """
        :param InstanceId: 数据库唯一标识
        :type InstanceId: str
        :param Status: 状态。包含以下取值：
<li>INITIALIZING：资源初始化中</li>
<li>RUNNING：运行中，可正常使用的状态</li>
<li>UNUSABLE：禁用，不可用</li>
<li>OVERDUE：资源过期</li>
        :type Status: str
        :param Region: 所属地域。
当前支持ap-shanghai
        :type Region: str
        """
        self.InstanceId = None
        self.Status = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")
        self.Region = params.get("Region")


class DeleteCloudBaseProjectLatestVersionRequest(AbstractModel):
    """DeleteCloudBaseProjectLatestVersion请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id
        :type EnvId: str
        :param ProjectName: 项目名
        :type ProjectName: str
        """
        self.EnvId = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ProjectName = params.get("ProjectName")


class DeleteCloudBaseProjectLatestVersionResponse(AbstractModel):
    """DeleteCloudBaseProjectLatestVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEndUserRequest(AbstractModel):
    """DeleteEndUser请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param UserList: 用户列表，每一项都是uuid
        :type UserList: list of str
        """
        self.EnvId = None
        self.UserList = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.UserList = params.get("UserList")


class DeleteEndUserResponse(AbstractModel):
    """DeleteEndUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWxGatewayRouteRequest(AbstractModel):
    """DeleteWxGatewayRoute请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id
        :type EnvId: str
        :param GatewayRouteName: 服务名称
        :type GatewayRouteName: str
        """
        self.EnvId = None
        self.GatewayRouteName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.GatewayRouteName = params.get("GatewayRouteName")


class DeleteWxGatewayRouteResponse(AbstractModel):
    """DeleteWxGatewayRoute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAuthDomainsRequest(AbstractModel):
    """DescribeAuthDomains请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeAuthDomainsResponse(AbstractModel):
    """DescribeAuthDomains返回参数结构体

    """

    def __init__(self):
        """
        :param Domains: 安全域名列表列表
        :type Domains: list of AuthDomain
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = AuthDomain()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseBuildServiceRequest(AbstractModel):
    """DescribeCloudBaseBuildService请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id
        :type EnvId: str
        :param ServiceName: 服务名
        :type ServiceName: str
        :param CIBusiness: build类型,枚举值有: cloudbaserun, framework-ci
        :type CIBusiness: str
        :param ServiceVersion: 服务版本
        :type ServiceVersion: str
        """
        self.EnvId = None
        self.ServiceName = None
        self.CIBusiness = None
        self.ServiceVersion = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServiceName = params.get("ServiceName")
        self.CIBusiness = params.get("CIBusiness")
        self.ServiceVersion = params.get("ServiceVersion")


class DescribeCloudBaseBuildServiceResponse(AbstractModel):
    """DescribeCloudBaseBuildService返回参数结构体

    """

    def __init__(self):
        """
        :param UploadUrl: 上传url
        :type UploadUrl: str
        :param UploadHeaders: 上传heder
        :type UploadHeaders: list of KVPair
        :param PackageName: 包名
        :type PackageName: str
        :param PackageVersion: 包版本
        :type PackageVersion: str
        :param DownloadUrl: 下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param DownloadHeaders: 下载Httpheader
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadHeaders: list of KVPair
        :param OutDate: 下载链接是否过期
注意：此字段可能返回 null，表示取不到有效值。
        :type OutDate: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UploadUrl = None
        self.UploadHeaders = None
        self.PackageName = None
        self.PackageVersion = None
        self.DownloadUrl = None
        self.DownloadHeaders = None
        self.OutDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UploadUrl = params.get("UploadUrl")
        if params.get("UploadHeaders") is not None:
            self.UploadHeaders = []
            for item in params.get("UploadHeaders"):
                obj = KVPair()
                obj._deserialize(item)
                self.UploadHeaders.append(obj)
        self.PackageName = params.get("PackageName")
        self.PackageVersion = params.get("PackageVersion")
        self.DownloadUrl = params.get("DownloadUrl")
        if params.get("DownloadHeaders") is not None:
            self.DownloadHeaders = []
            for item in params.get("DownloadHeaders"):
                obj = KVPair()
                obj._deserialize(item)
                self.DownloadHeaders.append(obj)
        self.OutDate = params.get("OutDate")
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseProjectLatestVersionListRequest(AbstractModel):
    """DescribeCloudBaseProjectLatestVersionList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param PageSize: 个数
        :type PageSize: int
        :param EnvId: 环境id, 非必填
        :type EnvId: str
        :param ProjectName: 项目名称, 非必填
        :type ProjectName: str
        :param ProjectType: 项目类型: framework-oneclick,qci-extension-cicd
        :type ProjectType: str
        :param Tags: 标签
        :type Tags: list of str
        """
        self.Offset = None
        self.PageSize = None
        self.EnvId = None
        self.ProjectName = None
        self.ProjectType = None
        self.Tags = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.PageSize = params.get("PageSize")
        self.EnvId = params.get("EnvId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectType = params.get("ProjectType")
        self.Tags = params.get("Tags")


class DescribeCloudBaseProjectLatestVersionListResponse(AbstractModel):
    """DescribeCloudBaseProjectLatestVersionList返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectList: 项目列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectList: list of CloudBaseProjectVersion
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProjectList") is not None:
            self.ProjectList = []
            for item in params.get("ProjectList"):
                obj = CloudBaseProjectVersion()
                obj._deserialize(item)
                self.ProjectList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseProjectVersionListRequest(AbstractModel):
    """DescribeCloudBaseProjectVersionList请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id
        :type EnvId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param PageSize: 页大小
        :type PageSize: int
        :param PageNum: 第几页,从0开始
        :type PageNum: int
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 终止时间
        :type EndTime: str
        """
        self.EnvId = None
        self.ProjectName = None
        self.PageSize = None
        self.PageNum = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ProjectName = params.get("ProjectName")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeCloudBaseProjectVersionListResponse(AbstractModel):
    """DescribeCloudBaseProjectVersionList返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectVersions: 版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectVersions: list of CloudBaseProjectVersion
        :param TotalCount: 总个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectVersions = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProjectVersions") is not None:
            self.ProjectVersions = []
            for item in params.get("ProjectVersions"):
                obj = CloudBaseProjectVersion()
                obj._deserialize(item)
                self.ProjectVersions.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunResourceForExtendRequest(AbstractModel):
    """DescribeCloudBaseRunResourceForExtend请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeCloudBaseRunResourceForExtendResponse(AbstractModel):
    """DescribeCloudBaseRunResourceForExtend返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterStatus: 集群状态(creating/succ)
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStatus: str
        :param VirtualClusterId: 虚拟集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualClusterId: str
        :param VpcId: vpc id信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param Region: 地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param SubnetIds: 子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of CloudBaseRunVpcSubnet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterStatus = None
        self.VirtualClusterId = None
        self.VpcId = None
        self.Region = None
        self.SubnetIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterStatus = params.get("ClusterStatus")
        self.VirtualClusterId = params.get("VirtualClusterId")
        self.VpcId = params.get("VpcId")
        self.Region = params.get("Region")
        if params.get("SubnetIds") is not None:
            self.SubnetIds = []
            for item in params.get("SubnetIds"):
                obj = CloudBaseRunVpcSubnet()
                obj._deserialize(item)
                self.SubnetIds.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunResourceRequest(AbstractModel):
    """DescribeCloudBaseRunResource请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeCloudBaseRunResourceResponse(AbstractModel):
    """DescribeCloudBaseRunResource返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterStatus: 集群状态(creating/succ)
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStatus: str
        :param VirtualClusterId: 虚拟集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualClusterId: str
        :param VpcId: vpc id信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param Region: 地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param SubnetIds: 子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of CloudBaseRunVpcSubnet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterStatus = None
        self.VirtualClusterId = None
        self.VpcId = None
        self.Region = None
        self.SubnetIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterStatus = params.get("ClusterStatus")
        self.VirtualClusterId = params.get("VirtualClusterId")
        self.VpcId = params.get("VpcId")
        self.Region = params.get("Region")
        if params.get("SubnetIds") is not None:
            self.SubnetIds = []
            for item in params.get("SubnetIds"):
                obj = CloudBaseRunVpcSubnet()
                obj._deserialize(item)
                self.SubnetIds.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunServerVersionRequest(AbstractModel):
    """DescribeCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param ServerName: 服务名称
        :type ServerName: str
        :param VersionName: 版本名称
        :type VersionName: str
        """
        self.EnvId = None
        self.ServerName = None
        self.VersionName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.VersionName = params.get("VersionName")


class DescribeCloudBaseRunServerVersionResponse(AbstractModel):
    """DescribeCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        """
        :param VersionName: 版本名称
        :type VersionName: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param DockerfilePath: Dockefile的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerfilePath: str
        :param BuildDir: DockerBuild的目录
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildDir: str
        :param Cpu: 请使用CPUSize
        :type Cpu: int
        :param Mem: 请使用MemSize
        :type Mem: int
        :param MinNum: 副本最小值
        :type MinNum: int
        :param MaxNum: 副本最大值
        :type MaxNum: int
        :param PolicyType: 策略类型
        :type PolicyType: str
        :param PolicyThreshold: 策略阈值
        :type PolicyThreshold: float
        :param EnvParams: 环境变量
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvParams: str
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param UpdatedTime: 更新时间
        :type UpdatedTime: str
        :param VersionIP: 版本的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionIP: str
        :param VersionPort: 版本的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionPort: int
        :param Status: 版本状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param PackageName: 代码包的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param PackageVersion: 代码版本的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param UploadType: 枚举（package/repository/image)
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadType: str
        :param RepoType: Repo的类型(coding/gitlab/github/coding)
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoType: str
        :param Repo: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Repo: str
        :param Branch: 分支
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        :param ServerName: 服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param IsPublic: 是否对于外网开放
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublic: bool
        :param VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetIds: 子网实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param CustomLogs: 日志采集路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLogs: str
        :param ContainerPort: 监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerPort: int
        :param InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param ImageUrl: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param CpuSize: CPU 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuSize: float
        :param MemSize: MEM 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VersionName = None
        self.Remark = None
        self.DockerfilePath = None
        self.BuildDir = None
        self.Cpu = None
        self.Mem = None
        self.MinNum = None
        self.MaxNum = None
        self.PolicyType = None
        self.PolicyThreshold = None
        self.EnvParams = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.VersionIP = None
        self.VersionPort = None
        self.Status = None
        self.PackageName = None
        self.PackageVersion = None
        self.UploadType = None
        self.RepoType = None
        self.Repo = None
        self.Branch = None
        self.ServerName = None
        self.IsPublic = None
        self.VpcId = None
        self.SubnetIds = None
        self.CustomLogs = None
        self.ContainerPort = None
        self.InitialDelaySeconds = None
        self.ImageUrl = None
        self.CpuSize = None
        self.MemSize = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.Remark = params.get("Remark")
        self.DockerfilePath = params.get("DockerfilePath")
        self.BuildDir = params.get("BuildDir")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.MinNum = params.get("MinNum")
        self.MaxNum = params.get("MaxNum")
        self.PolicyType = params.get("PolicyType")
        self.PolicyThreshold = params.get("PolicyThreshold")
        self.EnvParams = params.get("EnvParams")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.VersionIP = params.get("VersionIP")
        self.VersionPort = params.get("VersionPort")
        self.Status = params.get("Status")
        self.PackageName = params.get("PackageName")
        self.PackageVersion = params.get("PackageVersion")
        self.UploadType = params.get("UploadType")
        self.RepoType = params.get("RepoType")
        self.Repo = params.get("Repo")
        self.Branch = params.get("Branch")
        self.ServerName = params.get("ServerName")
        self.IsPublic = params.get("IsPublic")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.CustomLogs = params.get("CustomLogs")
        self.ContainerPort = params.get("ContainerPort")
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        self.ImageUrl = params.get("ImageUrl")
        self.CpuSize = params.get("CpuSize")
        self.MemSize = params.get("MemSize")
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunVersionRequest(AbstractModel):
    """DescribeCloudBaseRunVersion请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param ServerName: 服务名称
        :type ServerName: str
        :param VersionName: 版本名称
        :type VersionName: str
        """
        self.EnvId = None
        self.ServerName = None
        self.VersionName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.VersionName = params.get("VersionName")


class DescribeCloudBaseRunVersionResponse(AbstractModel):
    """DescribeCloudBaseRunVersion返回参数结构体

    """

    def __init__(self):
        """
        :param VersionName: 版本名称
        :type VersionName: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param DockerfilePath: Dockefile的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerfilePath: str
        :param BuildDir: DockerBuild的目录
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildDir: str
        :param MinNum: 副本最小值
        :type MinNum: int
        :param MaxNum: 副本最大值
        :type MaxNum: int
        :param PolicyType: 策略类型
        :type PolicyType: str
        :param PolicyThreshold: 策略阈值
        :type PolicyThreshold: float
        :param EnvParams: 环境变量
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvParams: str
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param UpdatedTime: 更新时间
        :type UpdatedTime: str
        :param VersionIP: 版本的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionIP: str
        :param VersionPort: 版本的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionPort: int
        :param Status: 版本状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param PackageName: 代码包的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param PackageVersion: 代码版本的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param UploadType: 枚举（package/repository/image)
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadType: str
        :param RepoType: Repo的类型(coding/gitlab/github/coding)
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoType: str
        :param Repo: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Repo: str
        :param Branch: 分支
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        :param ServerName: 服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param IsPublic: 是否对于外网开放
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublic: bool
        :param VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetIds: 子网实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param CustomLogs: 日志采集路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLogs: str
        :param ContainerPort: 监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerPort: int
        :param InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param ImageUrl: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param CpuSize: CPU 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuSize: float
        :param MemSize: MEM 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VersionName = None
        self.Remark = None
        self.DockerfilePath = None
        self.BuildDir = None
        self.MinNum = None
        self.MaxNum = None
        self.PolicyType = None
        self.PolicyThreshold = None
        self.EnvParams = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.VersionIP = None
        self.VersionPort = None
        self.Status = None
        self.PackageName = None
        self.PackageVersion = None
        self.UploadType = None
        self.RepoType = None
        self.Repo = None
        self.Branch = None
        self.ServerName = None
        self.IsPublic = None
        self.VpcId = None
        self.SubnetIds = None
        self.CustomLogs = None
        self.ContainerPort = None
        self.InitialDelaySeconds = None
        self.ImageUrl = None
        self.CpuSize = None
        self.MemSize = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.Remark = params.get("Remark")
        self.DockerfilePath = params.get("DockerfilePath")
        self.BuildDir = params.get("BuildDir")
        self.MinNum = params.get("MinNum")
        self.MaxNum = params.get("MaxNum")
        self.PolicyType = params.get("PolicyType")
        self.PolicyThreshold = params.get("PolicyThreshold")
        self.EnvParams = params.get("EnvParams")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.VersionIP = params.get("VersionIP")
        self.VersionPort = params.get("VersionPort")
        self.Status = params.get("Status")
        self.PackageName = params.get("PackageName")
        self.PackageVersion = params.get("PackageVersion")
        self.UploadType = params.get("UploadType")
        self.RepoType = params.get("RepoType")
        self.Repo = params.get("Repo")
        self.Branch = params.get("Branch")
        self.ServerName = params.get("ServerName")
        self.IsPublic = params.get("IsPublic")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.CustomLogs = params.get("CustomLogs")
        self.ContainerPort = params.get("ContainerPort")
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        self.ImageUrl = params.get("ImageUrl")
        self.CpuSize = params.get("CpuSize")
        self.MemSize = params.get("MemSize")
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunVersionSnapshotRequest(AbstractModel):
    """DescribeCloudBaseRunVersionSnapshot请求参数结构体

    """

    def __init__(self):
        """
        :param ServerName: 服务名
        :type ServerName: str
        :param VersionName: 版本名
        :type VersionName: str
        :param EnvId: 环境id
        :type EnvId: str
        :param SnapshotName: 版本历史名
        :type SnapshotName: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制大小
        :type Limit: int
        """
        self.ServerName = None
        self.VersionName = None
        self.EnvId = None
        self.SnapshotName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ServerName = params.get("ServerName")
        self.VersionName = params.get("VersionName")
        self.EnvId = params.get("EnvId")
        self.SnapshotName = params.get("SnapshotName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeCloudBaseRunVersionSnapshotResponse(AbstractModel):
    """DescribeCloudBaseRunVersionSnapshot返回参数结构体

    """

    def __init__(self):
        """
        :param Snapshots: 版本历史
注意：此字段可能返回 null，表示取不到有效值。
        :type Snapshots: list of CloudRunServiceSimpleVersionSnapshot
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Snapshots = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Snapshots") is not None:
            self.Snapshots = []
            for item in params.get("Snapshots"):
                obj = CloudRunServiceSimpleVersionSnapshot()
                obj._deserialize(item)
                self.Snapshots.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabaseACLRequest(AbstractModel):
    """DescribeDatabaseACL请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param CollectionName: 集合名称
        :type CollectionName: str
        """
        self.EnvId = None
        self.CollectionName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CollectionName = params.get("CollectionName")


class DescribeDatabaseACLResponse(AbstractModel):
    """DescribeDatabaseACL返回参数结构体

    """

    def __init__(self):
        """
        :param AclTag: 权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
        :type AclTag: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AclTag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AclTag = params.get("AclTag")
        self.RequestId = params.get("RequestId")


class DescribeDownloadFileRequest(AbstractModel):
    """DescribeDownloadFile请求参数结构体

    """

    def __init__(self):
        """
        :param CodeUri: 代码uri
        :type CodeUri: str
        """
        self.CodeUri = None


    def _deserialize(self, params):
        self.CodeUri = params.get("CodeUri")


class DescribeDownloadFileResponse(AbstractModel):
    """DescribeDownloadFile返回参数结构体

    """

    def __init__(self):
        """
        :param FilePath: 文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        :param CustomKey: 加密key
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomKey: str
        :param DownloadUrl: 下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FilePath = None
        self.CustomKey = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FilePath = params.get("FilePath")
        self.CustomKey = params.get("CustomKey")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeEndUserLoginStatisticRequest(AbstractModel):
    """DescribeEndUserLoginStatistic请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id
        :type EnvId: str
        :param Source: 终端用户来源
<li> qcloud </li>
<li>miniapp</li>
        :type Source: str
        """
        self.EnvId = None
        self.Source = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Source = params.get("Source")


class DescribeEndUserLoginStatisticResponse(AbstractModel):
    """DescribeEndUserLoginStatistic返回参数结构体

    """

    def __init__(self):
        """
        :param LoginStatistics: 环境终端用户新增与登录统计
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginStatistics: list of LoginStatistic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoginStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginStatistics") is not None:
            self.LoginStatistics = []
            for item in params.get("LoginStatistics"):
                obj = LoginStatistic()
                obj._deserialize(item)
                self.LoginStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEndUserStatisticRequest(AbstractModel):
    """DescribeEndUserStatistic请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeEndUserStatisticResponse(AbstractModel):
    """DescribeEndUserStatistic返回参数结构体

    """

    def __init__(self):
        """
        :param PlatformStatistics: 终端用户各平台统计
注意：此字段可能返回 null，表示取不到有效值。
        :type PlatformStatistics: list of PlatformStatistic
        :param TotalCount: 终端用户总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlatformStatistics = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlatformStatistics") is not None:
            self.PlatformStatistics = []
            for item in params.get("PlatformStatistics"):
                obj = PlatformStatistic()
                obj._deserialize(item)
                self.PlatformStatistics.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEndUsersRequest(AbstractModel):
    """DescribeEndUsers请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 开发者的环境ID
        :type EnvId: str
        :param Offset: 可选参数，偏移量，默认 0
        :type Offset: int
        :param Limit: 可选参数，拉取数量，默认 20
        :type Limit: int
        :param UUIds: 按照 uuid 列表过滤，最大个数为100
        :type UUIds: list of str
        """
        self.EnvId = None
        self.Offset = None
        self.Limit = None
        self.UUIds = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.UUIds = params.get("UUIds")


class DescribeEndUsersResponse(AbstractModel):
    """DescribeEndUsers返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 用户总数
        :type Total: int
        :param Users: 用户列表
        :type Users: list of EndUserInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = EndUserInfo()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvFreeQuotaRequest(AbstractModel):
    """DescribeEnvFreeQuota请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param ResourceTypes: 资源类型：可选值：CDN, COS, FLEXDB, HOSTING, SCF
不传则返回全部资源指标
        :type ResourceTypes: list of str
        """
        self.EnvId = None
        self.ResourceTypes = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ResourceTypes = params.get("ResourceTypes")


class DescribeEnvFreeQuotaResponse(AbstractModel):
    """DescribeEnvFreeQuota返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaItems: 免费抵扣配额详情
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaItems: list of PostpayEnvQuota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QuotaItems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaItems") is not None:
            self.QuotaItems = []
            for item in params.get("QuotaItems"):
                obj = PostpayEnvQuota()
                obj._deserialize(item)
                self.QuotaItems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvLimitRequest(AbstractModel):
    """DescribeEnvLimit请求参数结构体

    """


class DescribeEnvLimitResponse(AbstractModel):
    """DescribeEnvLimit返回参数结构体

    """

    def __init__(self):
        """
        :param MaxEnvNum: 环境总数上限
        :type MaxEnvNum: int
        :param CurrentEnvNum: 目前环境总数
        :type CurrentEnvNum: int
        :param MaxFreeEnvNum: 免费环境数量上限
        :type MaxFreeEnvNum: int
        :param CurrentFreeEnvNum: 目前免费环境数量
        :type CurrentFreeEnvNum: int
        :param MaxDeleteTotal: 总计允许销毁环境次数上限
        :type MaxDeleteTotal: int
        :param CurrentDeleteTotal: 目前已销毁环境次数
        :type CurrentDeleteTotal: int
        :param MaxDeleteMonthly: 每月允许销毁环境次数上限
        :type MaxDeleteMonthly: int
        :param CurrentDeleteMonthly: 本月已销毁环境次数
        :type CurrentDeleteMonthly: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaxEnvNum = None
        self.CurrentEnvNum = None
        self.MaxFreeEnvNum = None
        self.CurrentFreeEnvNum = None
        self.MaxDeleteTotal = None
        self.CurrentDeleteTotal = None
        self.MaxDeleteMonthly = None
        self.CurrentDeleteMonthly = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaxEnvNum = params.get("MaxEnvNum")
        self.CurrentEnvNum = params.get("CurrentEnvNum")
        self.MaxFreeEnvNum = params.get("MaxFreeEnvNum")
        self.CurrentFreeEnvNum = params.get("CurrentFreeEnvNum")
        self.MaxDeleteTotal = params.get("MaxDeleteTotal")
        self.CurrentDeleteTotal = params.get("CurrentDeleteTotal")
        self.MaxDeleteMonthly = params.get("MaxDeleteMonthly")
        self.CurrentDeleteMonthly = params.get("CurrentDeleteMonthly")
        self.RequestId = params.get("RequestId")


class DescribeEnvsRequest(AbstractModel):
    """DescribeEnvs请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID，如果传了这个参数则只返回该环境的相关信息
        :type EnvId: str
        :param IsVisible: 指定Channels字段为可见渠道列表或不可见渠道列表
如只想获取渠道A的环境 就填写IsVisible= true,Channels = ["A"], 过滤渠道A拉取其他渠道环境时填写IsVisible= false,Channels = ["A"]
        :type IsVisible: bool
        :param Channels: 渠道列表，代表可见或不可见渠道由IsVisible参数指定
        :type Channels: list of str
        """
        self.EnvId = None
        self.IsVisible = None
        self.Channels = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.IsVisible = params.get("IsVisible")
        self.Channels = params.get("Channels")


class DescribeEnvsResponse(AbstractModel):
    """DescribeEnvs返回参数结构体

    """

    def __init__(self):
        """
        :param EnvList: 环境信息列表
        :type EnvList: list of EnvInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnvList") is not None:
            self.EnvList = []
            for item in params.get("EnvList"):
                obj = EnvInfo()
                obj._deserialize(item)
                self.EnvList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeExtensionUploadInfoRequest(AbstractModel):
    """DescribeExtensionUploadInfo请求参数结构体

    """

    def __init__(self):
        """
        :param ExtensionFiles: 待上传的文件
        :type ExtensionFiles: list of ExtensionFile
        """
        self.ExtensionFiles = None


    def _deserialize(self, params):
        if params.get("ExtensionFiles") is not None:
            self.ExtensionFiles = []
            for item in params.get("ExtensionFiles"):
                obj = ExtensionFile()
                obj._deserialize(item)
                self.ExtensionFiles.append(obj)


class DescribeExtensionUploadInfoResponse(AbstractModel):
    """DescribeExtensionUploadInfo返回参数结构体

    """

    def __init__(self):
        """
        :param FilesData: 待上传文件的信息数组
        :type FilesData: list of ExtensionFileInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FilesData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FilesData") is not None:
            self.FilesData = []
            for item in params.get("FilesData"):
                obj = ExtensionFileInfo()
                obj._deserialize(item)
                self.FilesData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeExtraPkgBillingInfoRequest(AbstractModel):
    """DescribeExtraPkgBillingInfo请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 已购买增值包的环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeExtraPkgBillingInfoResponse(AbstractModel):
    """DescribeExtraPkgBillingInfo返回参数结构体

    """

    def __init__(self):
        """
        :param EnvInfoList: 增值包计费信息列表
        :type EnvInfoList: list of EnvBillingInfoItem
        :param Total: 增值包数目
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvInfoList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnvInfoList") is not None:
            self.EnvInfoList = []
            for item in params.get("EnvInfoList"):
                obj = EnvBillingInfoItem()
                obj._deserialize(item)
                self.EnvInfoList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribePostpayFreeQuotasRequest(AbstractModel):
    """DescribePostpayFreeQuotas请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribePostpayFreeQuotasResponse(AbstractModel):
    """DescribePostpayFreeQuotas返回参数结构体

    """

    def __init__(self):
        """
        :param FreequotaInfoList: 免费量资源信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FreequotaInfoList: list of FreequotaInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FreequotaInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FreequotaInfoList") is not None:
            self.FreequotaInfoList = []
            for item in params.get("FreequotaInfoList"):
                obj = FreequotaInfo()
                obj._deserialize(item)
                self.FreequotaInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePostpayPackageFreeQuotasRequest(AbstractModel):
    """DescribePostpayPackageFreeQuotas请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param FreeQuotaType: 免费额度类型标识
        :type FreeQuotaType: str
        """
        self.EnvId = None
        self.FreeQuotaType = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.FreeQuotaType = params.get("FreeQuotaType")


class DescribePostpayPackageFreeQuotasResponse(AbstractModel):
    """DescribePostpayPackageFreeQuotas返回参数结构体

    """

    def __init__(self):
        """
        :param PackageFreeQuotaInfos: 免费量资源信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageFreeQuotaInfos: list of PackageFreeQuotaInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PackageFreeQuotaInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PackageFreeQuotaInfos") is not None:
            self.PackageFreeQuotaInfos = []
            for item in params.get("PackageFreeQuotaInfos"):
                obj = PackageFreeQuotaInfo()
                obj._deserialize(item)
                self.PackageFreeQuotaInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeQuotaDataRequest(AbstractModel):
    """DescribeQuotaData请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param MetricName: <li> 指标名: </li>
<li> StorageSizepkg: 当月存储空间容量, 单位MB </li>
<li> StorageReadpkg: 当月存储读请求次数 </li>
<li> StorageWritepkg: 当月存储写请求次数 </li>
<li> StorageCdnOriginFluxpkg: 当月CDN回源流量, 单位字节 </li>
<li> StorageCdnOriginFluxpkgDay: 当日CDN回源流量, 单位字节 </li>
<li> StorageReadpkgDay: 当日存储读请求次数 </li>
<li> StorageWritepkgDay: 当日写请求次数 </li>
<li> CDNFluxpkg: 当月CDN流量, 单位为字节 </li>
<li> CDNFluxpkgDay: 当日CDN流量, 单位为字节 </li>
<li> FunctionInvocationpkg: 当月云函数调用次数 </li>
<li> FunctionGBspkg: 当月云函数资源使用量, 单位Mb*Ms </li>
<li> FunctionFluxpkg: 当月云函数流量, 单位千字节(KB) </li>
<li> FunctionInvocationpkgDay: 当日云函数调用次数 </li>
<li> FunctionGBspkgDay: 当日云函数资源使用量, 单位Mb*Ms </li>
<li> FunctionFluxpkgDay: 当日云函数流量, 单位千字节(KB) </li>
<li> DbSizepkg: 当月数据库容量大小, 单位MB </li>
<li> DbReadpkg: 当日数据库读请求数 </li>
<li> DbWritepkg: 当日数据库写请求数 </li>
<li> StaticFsFluxPkgDay: 当日静态托管流量 </li>
<li> StaticFsFluxPkg: 当月静态托管流量</li>
<li> StaticFsSizePkg: 当月静态托管容量 </li>
<li> TkeCpuUsedPkg: 当月容器托管CPU使用量，单位核*秒 </li>
<li> TkeCpuUsedPkgDay: 当天容器托管CPU使用量，单位核*秒 </li>
<li> TkeMemUsedPkg: 当月容器托管内存使用量，单位MB*秒 </li>
<li> TkeMemUsedPkgDay: 当天容器托管内存使用量，单位MB*秒 </li>
<li> CodingBuildTimePkgDay: 当天容器托管构建时间使用量，单位毫秒 </li>
<li> TkeHttpServiceNatPkgDay: 当天容器托管流量使用量，单位B </li>
        :type MetricName: str
        :param ResourceID: 资源ID, 目前仅对云函数、容器托管相关的指标有意义。云函数(FunctionInvocationpkg, FunctionGBspkg, FunctionFluxpkg)、容器托管（服务名称）。如果想查询某个云函数的指标则在ResourceId中传入函数名; 如果只想查询整个namespace的指标, 则留空或不传。
        :type ResourceID: str
        """
        self.EnvId = None
        self.MetricName = None
        self.ResourceID = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.MetricName = params.get("MetricName")
        self.ResourceID = params.get("ResourceID")


class DescribeQuotaDataResponse(AbstractModel):
    """DescribeQuotaData返回参数结构体

    """

    def __init__(self):
        """
        :param MetricName: 指标名
        :type MetricName: str
        :param Value: 指标的值
        :type Value: int
        :param SubValue: 指标的附加值信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubValue: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricName = None
        self.Value = None
        self.SubValue = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Value = params.get("Value")
        self.SubValue = params.get("SubValue")
        self.RequestId = params.get("RequestId")


class DescribeSmsQuotasRequest(AbstractModel):
    """DescribeSmsQuotas请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeSmsQuotasResponse(AbstractModel):
    """DescribeSmsQuotas返回参数结构体

    """

    def __init__(self):
        """
        :param SmsFreeQuotaList: 短信免费量信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsFreeQuotaList: list of SmsFreeQuota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SmsFreeQuotaList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SmsFreeQuotaList") is not None:
            self.SmsFreeQuotaList = []
            for item in params.get("SmsFreeQuotaList"):
                obj = SmsFreeQuota()
                obj._deserialize(item)
                self.SmsFreeQuotaList.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyEnvRequest(AbstractModel):
    """DestroyEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境Id
        :type EnvId: str
        :param IsForce: 针对预付费 删除隔离中的环境时要传true 正常环境直接跳过隔离期删除
        :type IsForce: bool
        :param BypassCheck: 是否绕过资源检查，资源包等额外资源，默认为false，如果为true，则不检查资源是否有数据，直接删除。
        :type BypassCheck: bool
        """
        self.EnvId = None
        self.IsForce = None
        self.BypassCheck = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.IsForce = params.get("IsForce")
        self.BypassCheck = params.get("BypassCheck")


class DestroyEnvResponse(AbstractModel):
    """DestroyEnv返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DestroyStaticStoreRequest(AbstractModel):
    """DestroyStaticStore请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param CdnDomain: cdn域名
        :type CdnDomain: str
        """
        self.EnvId = None
        self.CdnDomain = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CdnDomain = params.get("CdnDomain")


class DestroyStaticStoreResponse(AbstractModel):
    """DestroyStaticStore返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 条件任务结果(succ/fail)
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class EndUserInfo(AbstractModel):
    """终端用户信息

    """

    def __init__(self):
        """
        :param UUId: 用户唯一ID
        :type UUId: str
        :param WXOpenId: 微信ID
        :type WXOpenId: str
        :param QQOpenId: qq ID
        :type QQOpenId: str
        :param Phone: 手机号
        :type Phone: str
        :param Email: 邮箱
        :type Email: str
        :param NickName: 昵称
        :type NickName: str
        :param Gender: 性别
        :type Gender: str
        :param AvatarUrl: 头像地址
        :type AvatarUrl: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param IsAnonymous: 是否为匿名用户
        :type IsAnonymous: bool
        :param IsDisabled: 是否禁用账户
        :type IsDisabled: bool
        :param HasPassword: 是否设置过密码
        :type HasPassword: bool
        :param UserName: 用户名
        :type UserName: str
        """
        self.UUId = None
        self.WXOpenId = None
        self.QQOpenId = None
        self.Phone = None
        self.Email = None
        self.NickName = None
        self.Gender = None
        self.AvatarUrl = None
        self.UpdateTime = None
        self.CreateTime = None
        self.IsAnonymous = None
        self.IsDisabled = None
        self.HasPassword = None
        self.UserName = None


    def _deserialize(self, params):
        self.UUId = params.get("UUId")
        self.WXOpenId = params.get("WXOpenId")
        self.QQOpenId = params.get("QQOpenId")
        self.Phone = params.get("Phone")
        self.Email = params.get("Email")
        self.NickName = params.get("NickName")
        self.Gender = params.get("Gender")
        self.AvatarUrl = params.get("AvatarUrl")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.IsAnonymous = params.get("IsAnonymous")
        self.IsDisabled = params.get("IsDisabled")
        self.HasPassword = params.get("HasPassword")
        self.UserName = params.get("UserName")


class EnvBillingInfoItem(AbstractModel):
    """环境计费信息

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param PackageId: tcb产品套餐ID，参考DescribePackages接口的返回值。
        :type PackageId: str
        :param IsAutoRenew: 自动续费标记
        :type IsAutoRenew: bool
        :param Status: 状态。包含以下取值：
<li> 空字符串：初始化中</li>
<li> NORMAL：正常</li>
<li> ISOLATE：隔离</li>
        :type Status: str
        :param PayMode: 支付方式。包含以下取值：
<li> PREPAYMENT：预付费</li>
<li> POSTPAID：后付费</li>
        :type PayMode: str
        :param IsolatedTime: 隔离时间，最近一次隔离的时间
        :type IsolatedTime: str
        :param ExpireTime: 过期时间，套餐即将到期的时间
        :type ExpireTime: str
        :param CreateTime: 创建时间，第一次接入计费方案的时间。
        :type CreateTime: str
        :param UpdateTime: 更新时间，计费信息最近一次更新的时间。
        :type UpdateTime: str
        :param IsAlwaysFree: true表示从未升级过付费版。
        :type IsAlwaysFree: bool
        :param PaymentChannel: 付费渠道。
<li> miniapp：小程序</li>
<li> qcloud：腾讯云</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentChannel: str
        :param OrderInfo: 最新的订单信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderInfo: :class:`tencentcloud.tcb.v20180608.models.OrderInfo`
        :param FreeQuota: 免费配额信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuota: str
        """
        self.EnvId = None
        self.PackageId = None
        self.IsAutoRenew = None
        self.Status = None
        self.PayMode = None
        self.IsolatedTime = None
        self.ExpireTime = None
        self.CreateTime = None
        self.UpdateTime = None
        self.IsAlwaysFree = None
        self.PaymentChannel = None
        self.OrderInfo = None
        self.FreeQuota = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.PackageId = params.get("PackageId")
        self.IsAutoRenew = params.get("IsAutoRenew")
        self.Status = params.get("Status")
        self.PayMode = params.get("PayMode")
        self.IsolatedTime = params.get("IsolatedTime")
        self.ExpireTime = params.get("ExpireTime")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.IsAlwaysFree = params.get("IsAlwaysFree")
        self.PaymentChannel = params.get("PaymentChannel")
        if params.get("OrderInfo") is not None:
            self.OrderInfo = OrderInfo()
            self.OrderInfo._deserialize(params.get("OrderInfo"))
        self.FreeQuota = params.get("FreeQuota")


class EnvInfo(AbstractModel):
    """环境信息

    """

    def __init__(self):
        """
        :param EnvId: 账户下该环境唯一标识
        :type EnvId: str
        :param Source: 环境来源。包含以下取值：
<li>miniapp：微信小程序</li>
<li>qcloud ：腾讯云</li>
        :type Source: str
        :param Alias: 环境别名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符
        :type Alias: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 最后修改时间
        :type UpdateTime: str
        :param Status: 环境状态。包含以下取值：
<li>NORMAL：正常可用</li>
<li>UNAVAILABLE：服务不可用，可能是尚未初始化或者初始化过程中</li>
        :type Status: str
        :param Databases: 数据库列表
        :type Databases: list of DatabasesInfo
        :param Storages: 存储列表
        :type Storages: list of StorageInfo
        :param Functions: 函数列表
        :type Functions: list of FunctionInfo
        :param PackageId: tcb产品套餐ID，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param PackageName: 套餐中文名称，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param LogServices: 云日志服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogServices: list of LogServiceInfo
        :param StaticStorages: 静态资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StaticStorages: list of StaticStorageInfo
        :param IsAutoDegrade: 是否到期自动降为免费版
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAutoDegrade: bool
        :param EnvChannel: 环境渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvChannel: str
        :param PayMode: 支付方式。包含以下取值：
<li> prepayment：预付费</li>
<li> postpaid：后付费</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param IsDefault: 是否为默认环境
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: bool
        :param Region: 环境所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self.EnvId = None
        self.Source = None
        self.Alias = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Status = None
        self.Databases = None
        self.Storages = None
        self.Functions = None
        self.PackageId = None
        self.PackageName = None
        self.LogServices = None
        self.StaticStorages = None
        self.IsAutoDegrade = None
        self.EnvChannel = None
        self.PayMode = None
        self.IsDefault = None
        self.Region = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Source = params.get("Source")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = DatabasesInfo()
                obj._deserialize(item)
                self.Databases.append(obj)
        if params.get("Storages") is not None:
            self.Storages = []
            for item in params.get("Storages"):
                obj = StorageInfo()
                obj._deserialize(item)
                self.Storages.append(obj)
        if params.get("Functions") is not None:
            self.Functions = []
            for item in params.get("Functions"):
                obj = FunctionInfo()
                obj._deserialize(item)
                self.Functions.append(obj)
        self.PackageId = params.get("PackageId")
        self.PackageName = params.get("PackageName")
        if params.get("LogServices") is not None:
            self.LogServices = []
            for item in params.get("LogServices"):
                obj = LogServiceInfo()
                obj._deserialize(item)
                self.LogServices.append(obj)
        if params.get("StaticStorages") is not None:
            self.StaticStorages = []
            for item in params.get("StaticStorages"):
                obj = StaticStorageInfo()
                obj._deserialize(item)
                self.StaticStorages.append(obj)
        self.IsAutoDegrade = params.get("IsAutoDegrade")
        self.EnvChannel = params.get("EnvChannel")
        self.PayMode = params.get("PayMode")
        self.IsDefault = params.get("IsDefault")
        self.Region = params.get("Region")


class EstablishCloudBaseRunServerRequest(AbstractModel):
    """EstablishCloudBaseRunServer请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id
        :type EnvId: str
        :param ServiceName: 服务名称
        :type ServiceName: str
        :param IsPublic: 是否开通外网访问
        :type IsPublic: bool
        :param ImageRepo: 镜像仓库
        :type ImageRepo: str
        :param Remark: 服务描述
        :type Remark: str
        :param EsInfo: es信息
        :type EsInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseEsInfo`
        :param LogType: 日志类型; es/cls
        :type LogType: str
        :param OperatorRemark: 操作备注
        :type OperatorRemark: str
        :param Source: 来源方（默认值：qcloud，微信侧来源miniapp)
        :type Source: str
        :param VpcInfo: vpc信息
        :type VpcInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunVpcInfo`
        :param PublicAccess: 0/1=允许公网访问;2=关闭公网访问
        :type PublicAccess: int
        """
        self.EnvId = None
        self.ServiceName = None
        self.IsPublic = None
        self.ImageRepo = None
        self.Remark = None
        self.EsInfo = None
        self.LogType = None
        self.OperatorRemark = None
        self.Source = None
        self.VpcInfo = None
        self.PublicAccess = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServiceName = params.get("ServiceName")
        self.IsPublic = params.get("IsPublic")
        self.ImageRepo = params.get("ImageRepo")
        self.Remark = params.get("Remark")
        if params.get("EsInfo") is not None:
            self.EsInfo = CloudBaseEsInfo()
            self.EsInfo._deserialize(params.get("EsInfo"))
        self.LogType = params.get("LogType")
        self.OperatorRemark = params.get("OperatorRemark")
        self.Source = params.get("Source")
        if params.get("VpcInfo") is not None:
            self.VpcInfo = CloudBaseRunVpcInfo()
            self.VpcInfo._deserialize(params.get("VpcInfo"))
        self.PublicAccess = params.get("PublicAccess")


class EstablishCloudBaseRunServerResponse(AbstractModel):
    """EstablishCloudBaseRunServer返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EstablishWxGatewayRouteRequest(AbstractModel):
    """EstablishWxGatewayRoute请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayId: 网关id
        :type GatewayId: str
        :param GatewayRouteName: 服务名称
        :type GatewayRouteName: str
        :param GatewayRouteAddr: 服务地址
        :type GatewayRouteAddr: str
        :param GatewayRouteProtocol: 协议类型 http/https
        :type GatewayRouteProtocol: str
        :param GatewayRouteDesc: 服务描述
        :type GatewayRouteDesc: str
        """
        self.GatewayId = None
        self.GatewayRouteName = None
        self.GatewayRouteAddr = None
        self.GatewayRouteProtocol = None
        self.GatewayRouteDesc = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.GatewayRouteName = params.get("GatewayRouteName")
        self.GatewayRouteAddr = params.get("GatewayRouteAddr")
        self.GatewayRouteProtocol = params.get("GatewayRouteProtocol")
        self.GatewayRouteDesc = params.get("GatewayRouteDesc")


class EstablishWxGatewayRouteResponse(AbstractModel):
    """EstablishWxGatewayRoute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExtensionFile(AbstractModel):
    """扩展文件

    """

    def __init__(self):
        """
        :param FileType: 文件类型。枚举值
<li>FUNCTION：函数代码</li>
<li>STATIC：静态托管代码</li>
<li>SMS：短信文件</li>
        :type FileType: str
        :param FileName: 文件名，长度不超过24
        :type FileName: str
        """
        self.FileType = None
        self.FileName = None


    def _deserialize(self, params):
        self.FileType = params.get("FileType")
        self.FileName = params.get("FileName")


class ExtensionFileInfo(AbstractModel):
    """扩展文件信息

    """

    def __init__(self):
        """
        :param CodeUri: 模板里使用的地址
        :type CodeUri: str
        :param UploadUrl: 上传文件的临时地址，含签名
        :type UploadUrl: str
        :param CustomKey: 自定义密钥。如果为空，则表示不需要加密
        :type CustomKey: str
        :param MaxSize: 文件大小限制，单位M，客户端上传前需要主动检查文件大小，超过限制的文件会被删除。
        :type MaxSize: int
        """
        self.CodeUri = None
        self.UploadUrl = None
        self.CustomKey = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.CodeUri = params.get("CodeUri")
        self.UploadUrl = params.get("UploadUrl")
        self.CustomKey = params.get("CustomKey")
        self.MaxSize = params.get("MaxSize")


class FreequotaInfo(AbstractModel):
    """后付费资源免费量信息

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型
<li>COS</li>
<li>CDN</li>
<li>FLEXDB</li>
<li>SCF</li>
        :type ResourceType: str
        :param ResourceMetric: 资源指标名称
        :type ResourceMetric: str
        :param FreeQuota: 资源指标免费量
        :type FreeQuota: int
        :param MetricUnit: 指标单位
        :type MetricUnit: str
        :param DeductType: 免费量抵扣周期
<li>sum-month:以月为单位抵扣</li>
<li>sum-day:以天为单位抵扣</li>
<li>totalize:总容量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductType: str
        :param FreeQuotaType: 免费量类型
<li>basic:通用量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuotaType: str
        """
        self.ResourceType = None
        self.ResourceMetric = None
        self.FreeQuota = None
        self.MetricUnit = None
        self.DeductType = None
        self.FreeQuotaType = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceMetric = params.get("ResourceMetric")
        self.FreeQuota = params.get("FreeQuota")
        self.MetricUnit = params.get("MetricUnit")
        self.DeductType = params.get("DeductType")
        self.FreeQuotaType = params.get("FreeQuotaType")


class FunctionInfo(AbstractModel):
    """函数的信息

    """

    def __init__(self):
        """
        :param Namespace: 命名空间
        :type Namespace: str
        :param Region: 所属地域。
当前支持ap-shanghai
        :type Region: str
        """
        self.Namespace = None
        self.Region = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Region = params.get("Region")


class KVPair(AbstractModel):
    """键值对

    """

    def __init__(self):
        """
        :param Key: 键
        :type Key: str
        :param Value: 值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class LogServiceInfo(AbstractModel):
    """云日志服务相关信息

    """

    def __init__(self):
        """
        :param LogsetName: log名
        :type LogsetName: str
        :param LogsetId: log-id
        :type LogsetId: str
        :param TopicName: topic名
        :type TopicName: str
        :param TopicId: topic-id
        :type TopicId: str
        :param Region: cls日志所属地域
        :type Region: str
        """
        self.LogsetName = None
        self.LogsetId = None
        self.TopicName = None
        self.TopicId = None
        self.Region = None


    def _deserialize(self, params):
        self.LogsetName = params.get("LogsetName")
        self.LogsetId = params.get("LogsetId")
        self.TopicName = params.get("TopicName")
        self.TopicId = params.get("TopicId")
        self.Region = params.get("Region")


class LoginStatistic(AbstractModel):
    """终端用户登录新增统计

    """

    def __init__(self):
        """
        :param StatisticalType: 统计类型 新增NEWUSER 和登录 LOGIN
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticalType: str
        :param StatisticalCycle: 统计周期：日DAY，周WEEK，月MONTH
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticalCycle: str
        :param Count: 统计总量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.StatisticalType = None
        self.StatisticalCycle = None
        self.Count = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.StatisticalType = params.get("StatisticalType")
        self.StatisticalCycle = params.get("StatisticalCycle")
        self.Count = params.get("Count")
        self.UpdateTime = params.get("UpdateTime")


class ModifyDatabaseACLRequest(AbstractModel):
    """ModifyDatabaseACL请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param CollectionName: 集合名称
        :type CollectionName: str
        :param AclTag: 权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
        :type AclTag: str
        """
        self.EnvId = None
        self.CollectionName = None
        self.AclTag = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CollectionName = params.get("CollectionName")
        self.AclTag = params.get("AclTag")


class ModifyDatabaseACLResponse(AbstractModel):
    """ModifyDatabaseACL返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEndUserRequest(AbstractModel):
    """ModifyEndUser请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param UUId: C端用户端的唯一ID
        :type UUId: str
        :param Status: 帐号的状态
        :type Status: str
        """
        self.EnvId = None
        self.UUId = None
        self.Status = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.UUId = params.get("UUId")
        self.Status = params.get("Status")


class ModifyEndUserResponse(AbstractModel):
    """ModifyEndUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEnvRequest(AbstractModel):
    """ModifyEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param Alias: 环境备注名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符
        :type Alias: str
        """
        self.EnvId = None
        self.Alias = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Alias = params.get("Alias")


class ModifyEnvResponse(AbstractModel):
    """ModifyEnv返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OrderInfo(AbstractModel):
    """订单信息

    """

    def __init__(self):
        """
        :param TranId: 订单号
        :type TranId: str
        :param PackageId: 订单要切换的套餐ID
        :type PackageId: str
        :param TranType: 订单类型
<li>1 购买</li>
<li>2 续费</li>
<li>3 变配</li>
        :type TranType: str
        :param TranStatus: 订单状态。
<li>1未支付</li>
<li>2 支付中</li>
<li>3 发货中</li>
<li>4 发货成功</li>
<li>5 发货失败</li>
<li>6 已退款</li>
<li>7 已取消</li>
<li>100 已删除</li>
        :type TranStatus: str
        :param UpdateTime: 订单更新时间
        :type UpdateTime: str
        :param CreateTime: 订单创建时间
        :type CreateTime: str
        :param PayMode: 付费模式.
<li>prepayment 预付费</li>
<li>postpaid 后付费</li>
        :type PayMode: str
        :param ExtensionId: 订单绑定的扩展ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtensionId: str
        :param ResourceReady: 资源初始化结果(仅当ExtensionId不为空时有效): successful(初始化成功), failed(初始化失败), doing(初始化进行中), init(准备初始化)
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceReady: str
        """
        self.TranId = None
        self.PackageId = None
        self.TranType = None
        self.TranStatus = None
        self.UpdateTime = None
        self.CreateTime = None
        self.PayMode = None
        self.ExtensionId = None
        self.ResourceReady = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.PackageId = params.get("PackageId")
        self.TranType = params.get("TranType")
        self.TranStatus = params.get("TranStatus")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.PayMode = params.get("PayMode")
        self.ExtensionId = params.get("ExtensionId")
        self.ResourceReady = params.get("ResourceReady")


class PackageFreeQuotaInfo(AbstractModel):
    """后付费免费额度

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型
<li>COS</li>
<li>CDN</li>
<li>FLEXDB</li>
<li>SCF</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param ResourceMetric: 资源指标名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceMetric: str
        :param FreeQuota: 资源指标免费量
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuota: int
        :param MetricUnit: 指标单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricUnit: str
        :param DeductType: 免费量抵扣周期
<li>sum-month:以月为单位抵扣</li>
<li>sum-day:以天为单位抵扣</li>
<li>totalize:总容量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductType: str
        :param FreeQuotaType: 免费量类型
<li>basic:通用量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuotaType: str
        """
        self.ResourceType = None
        self.ResourceMetric = None
        self.FreeQuota = None
        self.MetricUnit = None
        self.DeductType = None
        self.FreeQuotaType = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceMetric = params.get("ResourceMetric")
        self.FreeQuota = params.get("FreeQuota")
        self.MetricUnit = params.get("MetricUnit")
        self.DeductType = params.get("DeductType")
        self.FreeQuotaType = params.get("FreeQuotaType")


class PlatformStatistic(AbstractModel):
    """终端用户平台统计信息

    """

    def __init__(self):
        """
        :param Platform: 终端用户从属平台
注意：此字段可能返回 null，表示取不到有效值。
        :type Platform: str
        :param Count: 平台终端用户数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Platform = None
        self.Count = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Count = params.get("Count")
        self.UpdateTime = params.get("UpdateTime")


class PostpayEnvQuota(AbstractModel):
    """按量付费免费配额信息

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型
        :type ResourceType: str
        :param MetricName: 指标名
        :type MetricName: str
        :param Value: 配额值
        :type Value: int
        :param StartTime: 配额生效时间
为空表示没有时间限制
        :type StartTime: str
        :param EndTime: 配额失效时间
为空表示没有时间限制
        :type EndTime: str
        """
        self.ResourceType = None
        self.MetricName = None
        self.Value = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.MetricName = params.get("MetricName")
        self.Value = params.get("Value")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ReinstateEnvRequest(AbstractModel):
    """ReinstateEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class ReinstateEnvResponse(AbstractModel):
    """ReinstateEnv返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SmsFreeQuota(AbstractModel):
    """短信免费量

    """

    def __init__(self):
        """
        :param FreeQuota: 免费量总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuota: int
        :param TotalUsedQuota: 共计已使用总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUsedQuota: int
        :param CycleStart: 免费周期起点，0000-00-00 00:00:00 形式
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleStart: str
        :param CycleEnd: 免费周期终点，0000-00-00 00:00:00 形式
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleEnd: str
        :param TodayUsedQuota: 今天已使用总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TodayUsedQuota: int
        """
        self.FreeQuota = None
        self.TotalUsedQuota = None
        self.CycleStart = None
        self.CycleEnd = None
        self.TodayUsedQuota = None


    def _deserialize(self, params):
        self.FreeQuota = params.get("FreeQuota")
        self.TotalUsedQuota = params.get("TotalUsedQuota")
        self.CycleStart = params.get("CycleStart")
        self.CycleEnd = params.get("CycleEnd")
        self.TodayUsedQuota = params.get("TodayUsedQuota")


class StaticStorageInfo(AbstractModel):
    """静态CDN资源信息

    """

    def __init__(self):
        """
        :param StaticDomain: 静态CDN域名
注意：此字段可能返回 null，表示取不到有效值。
        :type StaticDomain: str
        :param DefaultDirName: 静态CDN默认文件夹，当前为根目录
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultDirName: str
        :param Status: 资源状态(process/online/offline/init)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Region: cos所属区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Bucket: bucket信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        """
        self.StaticDomain = None
        self.DefaultDirName = None
        self.Status = None
        self.Region = None
        self.Bucket = None


    def _deserialize(self, params):
        self.StaticDomain = params.get("StaticDomain")
        self.DefaultDirName = params.get("DefaultDirName")
        self.Status = params.get("Status")
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")


class StorageInfo(AbstractModel):
    """StorageInfo 资源信息

    """

    def __init__(self):
        """
        :param Region: 资源所属地域。
当前支持ap-shanghai
        :type Region: str
        :param Bucket: 桶名，存储资源的唯一标识
        :type Bucket: str
        :param CdnDomain: cdn 域名
        :type CdnDomain: str
        :param AppId: 资源所属用户的腾讯云appId
        :type AppId: str
        """
        self.Region = None
        self.Bucket = None
        self.CdnDomain = None
        self.AppId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.CdnDomain = params.get("CdnDomain")
        self.AppId = params.get("AppId")