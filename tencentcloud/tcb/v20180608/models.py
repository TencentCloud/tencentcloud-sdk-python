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


class ActivityRecordItem(AbstractModel):
    """活动详情

    """

    def __init__(self):
        """
        :param Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。\n        :type Uin: str\n        :param ActivityId: 活动id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityId: int\n        :param Status: 自定义状态码
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param SubStatus: 自定义子状态码
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubStatus: str\n        """
        self.Uin = None
        self.ActivityId = None
        self.Status = None
        self.SubStatus = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.ActivityId = params.get("ActivityId")
        self.Status = params.get("Status")
        self.SubStatus = params.get("SubStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthDomain(AbstractModel):
    """合法域名

    """

    def __init__(self):
        """
        :param Id: 域名ID\n        :type Id: str\n        :param Domain: 域名\n        :type Domain: str\n        :param Type: 域名类型。包含以下取值：
<li>SYSTEM</li>
<li>USER</li>\n        :type Type: str\n        :param Status: 状态。包含以下取值：
<li>ENABLE</li>
<li>DISABLE</li>\n        :type Status: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackendServiceInfo(AbstractModel):
    """网关服务信息

    """

    def __init__(self):
        """
        :param ServiceName: 服务名称\n        :type ServiceName: str\n        :param Status: 服务状态\n        :type Status: str\n        """
        self.ServiceName = None
        self.Status = None


    def _deserialize(self, params):
        self.ServiceName = params.get("ServiceName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvGatewayRequest(AbstractModel):
    """BindEnvGateway请求参数结构体

    """

    def __init__(self):
        """
        :param SubEnvId: 子环境id\n        :type SubEnvId: str\n        """
        self.SubEnvId = None


    def _deserialize(self, params):
        self.SubEnvId = params.get("SubEnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvGatewayResponse(AbstractModel):
    """BindEnvGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CheckTcbServiceRequest(AbstractModel):
    """CheckTcbService请求参数结构体

    """


class CheckTcbServiceResponse(AbstractModel):
    """CheckTcbService返回参数结构体

    """

    def __init__(self):
        """
        :param Initialized: true表示已开通\n        :type Initialized: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type Add: list of str\n        :param Drop: 禁用安全能力向列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Drop: list of str\n        """
        self.Add = None
        self.Drop = None


    def _deserialize(self, params):
        self.Add = params.get("Add")
        self.Drop = params.get("Drop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseCodeRepoDetail(AbstractModel):
    """代码仓库里 Repo的信息描述

    """

    def __init__(self):
        """
        :param Name: repo的名字\n        :type Name: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoName`\n        :param Url: repo的url\n        :type Url: str\n        """
        self.Name = None
        self.Url = None


    def _deserialize(self, params):
        if params.get("Name") is not None:
            self.Name = CloudBaseCodeRepoName()
            self.Name._deserialize(params.get("Name"))
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseCodeRepoName(AbstractModel):
    """代码仓库 repo的名字

    """

    def __init__(self):
        """
        :param Name: repo的名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param FullName: repo的完整全名
注意：此字段可能返回 null，表示取不到有效值。\n        :type FullName: str\n        """
        self.Name = None
        self.FullName = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.FullName = params.get("FullName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseEsInfo(AbstractModel):
    """es信息

    """

    def __init__(self):
        """
        :param Id: es的id
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: int\n        :param SecretName: secret名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretName: str\n        :param Ip: ip地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ip: str\n        :param Port: 端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: int\n        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: str\n        :param Account: 用户名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Account: str\n        :param Password: 密码
注意：此字段可能返回 null，表示取不到有效值。\n        :type Password: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseProjectVersion(AbstractModel):
    """云开发项目版本

    """

    def __init__(self):
        """
        :param Name: 项目名\n        :type Name: str\n        :param Sam: SAM json
注意：此字段可能返回 null，表示取不到有效值。\n        :type Sam: str\n        :param Source: 来源类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Source: :class:`tencentcloud.tcb.v20180608.models.CodeSource`\n        :param CreateTime: 创建时间, unix时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param UpdateTime: 更新时间 ,unix时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: int\n        :param Status: 项目状态, 枚举值: 
        "creatingEnv"-创建环境中
	"createEnvFail"-创建环境失败
	"building"-构建中
	"buildFail"-构建失败
	"deploying"-部署中
	 "deployFail"-部署失败
	 "success"-部署成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Parameters: 环境变量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Parameters: list of KVPair\n        :param Type: 项目类型, 枚举值:
"framework-oneclick" 控制台一键部署
"framework-local-oneclick" cli本地一键部署
"qci-extension-cicd" 内网coding ci cd
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param CIId: ci的id
注意：此字段可能返回 null，表示取不到有效值。\n        :type CIId: str\n        :param CDId: cd的id
注意：此字段可能返回 null，表示取不到有效值。\n        :type CDId: str\n        :param EnvId: 环境id
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvId: str\n        :param VersionNum: 版本号
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionNum: int\n        :param FailReason: 错误原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailReason: str\n        :param RcJson: rc.json内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type RcJson: str\n        :param AddonConfig: 插件配置内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type AddonConfig: str\n        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of str\n        :param NetworkConfig: 网络配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetworkConfig: str\n        :param ExtensionId: 扩展id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExtensionId: str\n        :param FailType: 错误类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailType: str\n        :param RepoUrl: 私有仓库地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepoUrl: str\n        :param AutoDeployOnCodeChange: 是否私有仓库代码变更触发自动部署
注意：此字段可能返回 null，表示取不到有效值。\n        :type AutoDeployOnCodeChange: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunEmptyDirVolumeSource(AbstractModel):
    """emptydir 数据卷详细信息

    """

    def __init__(self):
        """
        :param EnableEmptyDirVolume: 启用emptydir数据卷\n        :type EnableEmptyDirVolume: bool\n        :param Medium: "","Memory","HugePages"\n        :type Medium: str\n        :param SizeLimit: emptydir数据卷大小\n        :type SizeLimit: str\n        """
        self.EnableEmptyDirVolume = None
        self.Medium = None
        self.SizeLimit = None


    def _deserialize(self, params):
        self.EnableEmptyDirVolume = params.get("EnableEmptyDirVolume")
        self.Medium = params.get("Medium")
        self.SizeLimit = params.get("SizeLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunForGatewayConf(AbstractModel):
    """独立网关云托管服务配置信息

    """

    def __init__(self):
        """
        :param IsZero: 是否缩容到0\n        :type IsZero: bool\n        :param Weight: 按百分比灰度的权重\n        :type Weight: int\n        :param GrayKey: 按请求/header参数的灰度Key\n        :type GrayKey: str\n        :param GrayValue: 按请求/header参数的灰度Value\n        :type GrayValue: str\n        :param IsDefault: 是否为默认版本(按请求/header参数)\n        :type IsDefault: bool\n        :param AccessType: 访问权限，对应二进制分多段，vpc内网｜公网｜oa\n        :type AccessType: int\n        :param URLs: 访问的URL（域名＋路径）列表\n        :type URLs: list of str\n        :param EnvId: 环境ID\n        :type EnvId: str\n        :param ServerName: 服务名称\n        :type ServerName: str\n        :param VersionName: 版本名称\n        :type VersionName: str\n        :param GrayType: 灰度类型：FLOW(权重), URL_PARAMS/HEAD_PARAMS\n        :type GrayType: str\n        :param LbAddr: CLB的IP:Port\n        :type LbAddr: str\n        :param ConfigType: 0:http访问服务配置信息, 1: 服务域名\n        :type ConfigType: int\n        """
        self.IsZero = None
        self.Weight = None
        self.GrayKey = None
        self.GrayValue = None
        self.IsDefault = None
        self.AccessType = None
        self.URLs = None
        self.EnvId = None
        self.ServerName = None
        self.VersionName = None
        self.GrayType = None
        self.LbAddr = None
        self.ConfigType = None


    def _deserialize(self, params):
        self.IsZero = params.get("IsZero")
        self.Weight = params.get("Weight")
        self.GrayKey = params.get("GrayKey")
        self.GrayValue = params.get("GrayValue")
        self.IsDefault = params.get("IsDefault")
        self.AccessType = params.get("AccessType")
        self.URLs = params.get("URLs")
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.VersionName = params.get("VersionName")
        self.GrayType = params.get("GrayType")
        self.LbAddr = params.get("LbAddr")
        self.ConfigType = params.get("ConfigType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunImageInfo(AbstractModel):
    """CloudBaseRun 镜像信息

    """

    def __init__(self):
        """
        :param RepositoryName: 镜像仓库名称\n        :type RepositoryName: str\n        :param IsPublic: 是否公有\n        :type IsPublic: bool\n        :param TagName: 镜像tag名称\n        :type TagName: str\n        :param ServerAddr: 镜像server\n        :type ServerAddr: str\n        :param ImageUrl: 镜像拉取地址\n        :type ImageUrl: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunImageSecretInfo(AbstractModel):
    """ImageSecretInfo的信息

    """

    def __init__(self):
        """
        :param RegistryServer: 镜像地址\n        :type RegistryServer: str\n        :param UserName: 用户名\n        :type UserName: str\n        :param Password: 仓库密码\n        :type Password: str\n        :param Email: 邮箱\n        :type Email: str\n        """
        self.RegistryServer = None
        self.UserName = None
        self.Password = None
        self.Email = None


    def _deserialize(self, params):
        self.RegistryServer = params.get("RegistryServer")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunNfsVolumeSource(AbstractModel):
    """nfs挂载资源

    """

    def __init__(self):
        """
        :param Server: NFS挂载Server\n        :type Server: str\n        :param Path: Server路径\n        :type Path: str\n        :param ReadOnly: 是否只读\n        :type ReadOnly: bool\n        :param SecretName: secret名称\n        :type SecretName: str\n        :param EnableEmptyDirVolume: 临时目录\n        :type EnableEmptyDirVolume: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunServiceVolumeMount(AbstractModel):
    """对标 EKS VolumeMount

    """

    def __init__(self):
        """
        :param Name: Volume 名称\n        :type Name: str\n        :param MountPath: 挂载路径\n        :type MountPath: str\n        :param ReadOnly: 是否只读\n        :type ReadOnly: bool\n        :param SubPath: 子路径\n        :type SubPath: str\n        :param MountPropagation: 传播挂载方式\n        :type MountPropagation: str\n        """
        self.Name = None
        self.MountPath = None
        self.ReadOnly = None
        self.SubPath = None
        self.MountPropagation = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.MountPath = params.get("MountPath")
        self.ReadOnly = params.get("ReadOnly")
        self.SubPath = params.get("SubPath")
        self.MountPropagation = params.get("MountPropagation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunSideSpec(AbstractModel):
    """CloudBaseRun 的 Side 描述定义

    """

    def __init__(self):
        """
        :param ContainerImage: 容器镜像
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContainerImage: str\n        :param ContainerPort: 容器端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContainerPort: int\n        :param ContainerName: 容器的名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContainerName: str\n        :param EnvVar: kv的json字符串
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvVar: str\n        :param InitialDelaySeconds: InitialDelaySeconds 延迟多长时间启动健康检查
注意：此字段可能返回 null，表示取不到有效值。\n        :type InitialDelaySeconds: int\n        :param Cpu: CPU大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cpu: int\n        :param Mem: 内存大小（单位：M）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Mem: int\n        :param Security: 安全特性
注意：此字段可能返回 null，表示取不到有效值。\n        :type Security: :class:`tencentcloud.tcb.v20180608.models.CloudBaseSecurityContext`\n        :param VolumeMountInfos: 挂载信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type VolumeMountInfos: list of CloudBaseRunVolumeMount\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunVersionFlowItem(AbstractModel):
    """版本流量占比

    """

    def __init__(self):
        """
        :param VersionName: 版本名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionName: str\n        :param FlowRatio: 流量占比
注意：此字段可能返回 null，表示取不到有效值。\n        :type FlowRatio: int\n        :param UrlParam: 流量参数键值对（URL参数/HEADERS参数）
注意：此字段可能返回 null，表示取不到有效值。\n        :type UrlParam: :class:`tencentcloud.tcb.v20180608.models.ObjectKV`\n        :param Priority: 优先级
注意：此字段可能返回 null，表示取不到有效值。\n        :type Priority: int\n        :param IsDefaultPriority: 是否是默认兜底版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDefaultPriority: bool\n        """
        self.VersionName = None
        self.FlowRatio = None
        self.UrlParam = None
        self.Priority = None
        self.IsDefaultPriority = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.FlowRatio = params.get("FlowRatio")
        if params.get("UrlParam") is not None:
            self.UrlParam = ObjectKV()
            self.UrlParam._deserialize(params.get("UrlParam"))
        self.Priority = params.get("Priority")
        self.IsDefaultPriority = params.get("IsDefaultPriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunVolumeMount(AbstractModel):
    """cfs挂载点

    """

    def __init__(self):
        """
        :param Name: 资源名\n        :type Name: str\n        :param MountPath: 挂载路径\n        :type MountPath: str\n        :param ReadOnly: 是否只读\n        :type ReadOnly: bool\n        :param NfsVolumes: Nfs挂载信息\n        :type NfsVolumes: list of CloudBaseRunNfsVolumeSource\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunVpcInfo(AbstractModel):
    """vpc信息

    """

    def __init__(self):
        """
        :param VpcId: vpc的id
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param SubnetIds: 子网id
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetIds: list of str\n        :param CreateType: 创建类型(0=继承; 1=新建; 2=指定)
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateType: int\n        """
        self.VpcId = None
        self.SubnetIds = None
        self.CreateType = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.CreateType = params.get("CreateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunVpcSubnet(AbstractModel):
    """子网信息

    """

    def __init__(self):
        """
        :param Id: 子网id
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: str\n        :param Cidr: 子网的ipv4
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cidr: str\n        :param Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。\n        :type Zone: str\n        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param Target: subnet类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Target: str\n        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param Name: 名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseSecurityContext(AbstractModel):
    """cloudrun安全特性


    """

    def __init__(self):
        """
        :param Capabilities: 安全特性
注意：此字段可能返回 null，表示取不到有效值。\n        :type Capabilities: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCapabilities`\n        """
        self.Capabilities = None


    def _deserialize(self, params):
        if params.get("Capabilities") is not None:
            self.Capabilities = CloudBaseCapabilities()
            self.Capabilities._deserialize(params.get("Capabilities"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudRunServiceSimpleVersionSnapshot(AbstractModel):
    """CloudRunServiceSimpleVersionSnapshot 信息

    """

    def __init__(self):
        """
        :param VersionName: 版本名
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionName: str\n        :param Remark: 版本备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param Cpu: cpu规格
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cpu: float\n        :param Mem: 内存规格
注意：此字段可能返回 null，表示取不到有效值。\n        :type Mem: float\n        :param MinNum: 最小副本数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MinNum: int\n        :param MaxNum: 最大副本数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxNum: int\n        :param ImageUrl: 镜像url
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageUrl: str\n        :param PolicyType: 扩容策略
注意：此字段可能返回 null，表示取不到有效值。\n        :type PolicyType: str\n        :param PolicyThreshold: 策略阈值
注意：此字段可能返回 null，表示取不到有效值。\n        :type PolicyThreshold: int\n        :param EnvParams: 环境参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvParams: str\n        :param ContainerPort: 容器端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContainerPort: int\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param UploadType: 更新类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type UploadType: str\n        :param DockerfilePath: dockerfile路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type DockerfilePath: str\n        :param BuildDir: 构建路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type BuildDir: str\n        :param RepoType: repo类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepoType: str\n        :param Repo: 仓库
注意：此字段可能返回 null，表示取不到有效值。\n        :type Repo: str\n        :param Branch: 分支
注意：此字段可能返回 null，表示取不到有效值。\n        :type Branch: str\n        :param EnvId: 环境id
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvId: str\n        :param ServerName: 服务名
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServerName: str\n        :param PackageName: package名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageName: str\n        :param PackageVersion: package版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageVersion: str\n        :param CustomLogs: 自定义log路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type CustomLogs: str\n        :param InitialDelaySeconds: 延时健康检查时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type InitialDelaySeconds: int\n        :param SnapshotName: snapshot名
注意：此字段可能返回 null，表示取不到有效值。\n        :type SnapshotName: str\n        :param ImageInfo: 镜像信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageInfo`\n        :param CodeDetail: 代码仓库信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type CodeDetail: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoDetail`\n        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudRunServiceVolume(AbstractModel):
    """服务的volume

    """

    def __init__(self):
        """
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param NFS: NFS的挂载方式
注意：此字段可能返回 null，表示取不到有效值。\n        :type NFS: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunNfsVolumeSource`\n        :param SecretName: secret名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretName: str\n        :param EnableEmptyDirVolume: 是否开启临时目录逐步废弃，请使用 EmptyDir
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnableEmptyDirVolume: bool\n        :param EmptyDir: emptydir数据卷详细信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type EmptyDir: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunEmptyDirVolumeSource`\n        """
        self.Name = None
        self.NFS = None
        self.SecretName = None
        self.EnableEmptyDirVolume = None
        self.EmptyDir = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("NFS") is not None:
            self.NFS = CloudBaseRunNfsVolumeSource()
            self.NFS._deserialize(params.get("NFS"))
        self.SecretName = params.get("SecretName")
        self.EnableEmptyDirVolume = params.get("EnableEmptyDirVolume")
        if params.get("EmptyDir") is not None:
            self.EmptyDir = CloudBaseRunEmptyDirVolumeSource()
            self.EmptyDir._deserialize(params.get("EmptyDir"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsInfo(AbstractModel):
    """cls日志信息

    """

    def __init__(self):
        """
        :param ClsRegion: cls所属地域\n        :type ClsRegion: str\n        :param ClsLogsetId: cls日志集ID\n        :type ClsLogsetId: str\n        :param ClsTopicId: cls日志主题ID\n        :type ClsTopicId: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        """
        self.ClsRegion = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ClsRegion = params.get("ClsRegion")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeSource(AbstractModel):
    """云开发项目来源

    """

    def __init__(self):
        """
        :param Type: 类型, 可能的枚举: "coding","package","package_url","github","gitlab","gitee","rawcode"
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param Url: 下载链接
注意：此字段可能返回 null，表示取不到有效值。\n        :type Url: str\n        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param WorkDir: 工作目录
注意：此字段可能返回 null，表示取不到有效值。\n        :type WorkDir: str\n        :param CodingPackageName: code包名, type为coding的时候需要填写
注意：此字段可能返回 null，表示取不到有效值。\n        :type CodingPackageName: str\n        :param CodingPackageVersion: coding版本名, type为coding的时候需要填写
注意：此字段可能返回 null，表示取不到有效值。\n        :type CodingPackageVersion: str\n        :param RawCode: 源码
注意：此字段可能返回 null，表示取不到有效值。\n        :type RawCode: str\n        :param Branch: 代码分支
注意：此字段可能返回 null，表示取不到有效值。\n        :type Branch: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonServiceAPIRequest(AbstractModel):
    """CommonServiceAPI请求参数结构体

    """

    def __init__(self):
        """
        :param Service: Service名，需要转发访问的接口名\n        :type Service: str\n        :param JSONData: 需要转发的云API参数，要转成JSON格式\n        :type JSONData: str\n        """
        self.Service = None
        self.JSONData = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.JSONData = params.get("JSONData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonServiceAPIResponse(AbstractModel):
    """CommonServiceAPI返回参数结构体

    """

    def __init__(self):
        """
        :param JSONResp: json格式response\n        :type JSONResp: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Name: 项目名\n        :type Name: str\n        :param Source: 来源\n        :type Source: :class:`tencentcloud.tcb.v20180608.models.CodeSource`\n        :param EnvId: 环境id\n        :type EnvId: str\n        :param Type: 项目类型, 枚举值为: framework-oneclick,qci-extension-cicd\n        :type Type: str\n        :param Parameters: 环境变量\n        :type Parameters: list of KVPair\n        :param EnvAlias: 环境别名。要以a-z开头，不能包含a-zA-z0-9-以外的字符\n        :type EnvAlias: str\n        :param RcJson: rc.json的内容\n        :type RcJson: str\n        :param AddonConfig: 插件配置内容\n        :type AddonConfig: str\n        :param Tags: 标签\n        :type Tags: list of str\n        :param NetworkConfig: 网络配置\n        :type NetworkConfig: str\n        :param FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。\n        :type FreeQuota: str\n        :param AutoDeployOnCodeChange: 是否代码变更触发自动部署\n        :type AutoDeployOnCodeChange: bool\n        :param RepoUrl: 私有仓库地址\n        :type RepoUrl: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndDeployCloudBaseProjectResponse(AbstractModel):
    """CreateAndDeployCloudBaseProject返回参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param Domains: 安全域名\n        :type Domains: list of str\n        """
        self.EnvId = None
        self.Domains = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuthDomainResponse(AbstractModel):
    """CreateAuthDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCloudBaseRunResourceRequest(AbstractModel):
    """CreateCloudBaseRunResource请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param VpcId: vpc的ID\n        :type VpcId: str\n        :param SubnetIds: 子网ID列表，当VpcId不为空，SubnetIds也不能为空\n        :type SubnetIds: list of str\n        """
        self.EnvId = None
        self.VpcId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudBaseRunResourceResponse(AbstractModel):
    """CreateCloudBaseRunResource返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回集群创建是否成功 succ为成功。并且中间无err
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param UploadType: 枚举（package/repository/image)\n        :type UploadType: str\n        :param FlowRatio: 流量占比\n        :type FlowRatio: int\n        :param Cpu: Cpu的大小，单位：核\n        :type Cpu: float\n        :param Mem: Mem的大小，单位：G\n        :type Mem: float\n        :param MinNum: 最小副本数，最小值：0\n        :type MinNum: int\n        :param MaxNum: 副本最大数，最大值：50\n        :type MaxNum: int\n        :param PolicyType: 策略类型(枚举值：比如cpu)\n        :type PolicyType: str\n        :param PolicyThreshold: 策略阈值\n        :type PolicyThreshold: int\n        :param ContainerPort: 服务端口\n        :type ContainerPort: int\n        :param ServerName: 服务名称\n        :type ServerName: str\n        :param RepositoryType: repository的类型(coding/gitlab/github/coding)\n        :type RepositoryType: str\n        :param DockerfilePath: Dockerfile地址\n        :type DockerfilePath: str\n        :param BuildDir: 构建目录\n        :type BuildDir: str\n        :param EnvParams: 环境变量\n        :type EnvParams: str\n        :param Repository: repository地址\n        :type Repository: str\n        :param Branch: 分支\n        :type Branch: str\n        :param VersionRemark: 版本备注\n        :type VersionRemark: str\n        :param PackageName: 代码包名字\n        :type PackageName: str\n        :param PackageVersion: 代码包的版本\n        :type PackageVersion: str\n        :param ImageInfo: Image的详情\n        :type ImageInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageInfo`\n        :param CodeDetail: Github等拉取代码的详情\n        :type CodeDetail: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoDetail`\n        :param ImageSecretInfo: 私有镜像秘钥信息\n        :type ImageSecretInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageSecretInfo`\n        :param ImagePullSecret: 私有镜像 认证名称\n        :type ImagePullSecret: str\n        :param CustomLogs: 用户自定义采集日志路径\n        :type CustomLogs: str\n        :param InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）\n        :type InitialDelaySeconds: int\n        :param MountVolumeInfo: cfs挂载信息\n        :type MountVolumeInfo: list of CloudBaseRunVolumeMount\n        :param AccessType: 4 代表只能微信链路访问\n        :type AccessType: int\n        :param EsInfo: es信息\n        :type EsInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseEsInfo`\n        :param EnableUnion: 是否使用统一域名\n        :type EnableUnion: bool\n        :param OperatorRemark: 操作备注\n        :type OperatorRemark: str\n        :param ServerPath: 服务路径\n        :type ServerPath: str\n        :param ImageReuseKey: 镜像复用的key\n        :type ImageReuseKey: str\n        :param SidecarSpecs: 容器的描述文件\n        :type SidecarSpecs: list of CloudBaseRunSideSpec\n        :param Security: 安全特性\n        :type Security: :class:`tencentcloud.tcb.v20180608.models.CloudBaseSecurityContext`\n        :param ServiceVolumes: 服务磁盘挂载\n        :type ServiceVolumes: list of CloudRunServiceVolume\n        :param IsCreateJnsGw: 是否创建JnsGw 0未传默认创建 1创建 2不创建\n        :type IsCreateJnsGw: int\n        :param ServiceVolumeMounts: 数据卷挂载参数\n        :type ServiceVolumeMounts: list of CloudBaseRunServiceVolumeMount\n        """
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
        self.IsCreateJnsGw = None
        self.ServiceVolumeMounts = None


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
        self.IsCreateJnsGw = params.get("IsCreateJnsGw")
        if params.get("ServiceVolumeMounts") is not None:
            self.ServiceVolumeMounts = []
            for item in params.get("ServiceVolumeMounts"):
                obj = CloudBaseRunServiceVolumeMount()
                obj._deserialize(item)
                self.ServiceVolumeMounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudBaseRunServerVersionResponse(AbstractModel):
    """CreateCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 状态(creating/succ)
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param VersionName: 版本名称（只有Result为succ的时候，才会返回VersionName)
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionName: str\n        :param RunId: 操作记录id
注意：此字段可能返回 null，表示取不到有效值。\n        :type RunId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param Domain: 域名\n        :type Domain: str\n        :param CertId: 证书ID\n        :type CertId: str\n        """
        self.EnvId = None
        self.Domain = None
        self.CertId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Domain = params.get("Domain")
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHostingDomainResponse(AbstractModel):
    """CreateHostingDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePostpayPackageRequest(AbstractModel):
    """CreatePostpayPackage请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID，需要系统自动创建环境时，此字段不传\n        :type EnvId: str\n        :param WxAppId: 微信 AppId，微信必传\n        :type WxAppId: str\n        :param Source: 付费来源
<li>miniapp</li>
<li>qcloud</li>\n        :type Source: str\n        :param FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。\n        :type FreeQuota: str\n        :param EnvSource: 环境创建来源，取值：
<li>miniapp</li>
<li>qcloud</li>
用法同CreateEnv接口的Source参数
和 Channel 参数同时传，或者同时不传；EnvId 为空时必传。\n        :type EnvSource: str\n        :param Alias: 环境别名，要以a-z开头，不能包含  a-z,0-9,-  以外的字符\n        :type Alias: str\n        :param Channel: 如果envsource为miniapp, channel可以为ide或api;
如果envsource为qcloud, channel可以为qc_console,cocos, qq, cloudgame,dcloud,serverless_framework
和 EnvSource 参数同时传，或者同时不传；EnvId 为空时必传。\n        :type Channel: str\n        :param ExtensionId: 扩展ID\n        :type ExtensionId: str\n        :param Flag: 订单标记。建议使用方统一转大小写之后再判断。
<li>QuickStart：快速启动来源</li>
<li>Activity：活动来源</li>\n        :type Flag: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePostpayPackageResponse(AbstractModel):
    """CreatePostpayPackage返回参数结构体

    """

    def __init__(self):
        """
        :param TranId: 后付费订单号\n        :type TranId: str\n        :param EnvId: 环境ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TranId = None
        self.EnvId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.EnvId = params.get("EnvId")
        self.RequestId = params.get("RequestId")


class CreateStandaloneGatewayRequest(AbstractModel):
    """CreateStandaloneGateway请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param GatewayAlias: 网关名\n        :type GatewayAlias: str\n        :param VpcId: 私有网络ID\n        :type VpcId: str\n        :param SubnetIds: 子网ID\n        :type SubnetIds: list of str\n        :param GatewayDesc: 网关描述\n        :type GatewayDesc: str\n        :param PackageVersion: 网关套餐版本\n        :type PackageVersion: str\n        """
        self.EnvId = None
        self.GatewayAlias = None
        self.VpcId = None
        self.SubnetIds = None
        self.GatewayDesc = None
        self.PackageVersion = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.GatewayAlias = params.get("GatewayAlias")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.GatewayDesc = params.get("GatewayDesc")
        self.PackageVersion = params.get("PackageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStandaloneGatewayResponse(AbstractModel):
    """CreateStandaloneGateway返回参数结构体

    """

    def __init__(self):
        """
        :param GatewayName: 网关名称\n        :type GatewayName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GatewayName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GatewayName = params.get("GatewayName")
        self.RequestId = params.get("RequestId")


class CreateStaticStoreRequest(AbstractModel):
    """CreateStaticStore请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param EnableUnion: 是否启用统一域名\n        :type EnableUnion: bool\n        """
        self.EnvId = None
        self.EnableUnion = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnableUnion = params.get("EnableUnion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStaticStoreResponse(AbstractModel):
    """CreateStaticStore返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建静态资源结果(succ/fail)
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateWxCloudBaseRunEnvRequest(AbstractModel):
    """CreateWxCloudBaseRunEnv请求参数结构体

    """

    def __init__(self):
        """
        :param WxAppId: wx应用Id\n        :type WxAppId: str\n        :param Alias: 环境别名，要以a-z开头，不能包含 a-z,0-9,- 以外的字符\n        :type Alias: str\n        :param FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。\n        :type FreeQuota: str\n        :param Flag: 订单标记。建议使用方统一转大小写之后再判断。
QuickStart：快速启动来源
Activity：活动来源\n        :type Flag: str\n        :param VpcId: 私有网络Id\n        :type VpcId: str\n        :param SubNetIds: 子网列表\n        :type SubNetIds: list of str\n        """
        self.WxAppId = None
        self.Alias = None
        self.FreeQuota = None
        self.Flag = None
        self.VpcId = None
        self.SubNetIds = None


    def _deserialize(self, params):
        self.WxAppId = params.get("WxAppId")
        self.Alias = params.get("Alias")
        self.FreeQuota = params.get("FreeQuota")
        self.Flag = params.get("Flag")
        self.VpcId = params.get("VpcId")
        self.SubNetIds = params.get("SubNetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWxCloudBaseRunEnvResponse(AbstractModel):
    """CreateWxCloudBaseRunEnv返回参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境Id\n        :type EnvId: str\n        :param TranId: 后付费订单号\n        :type TranId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EnvId = None
        self.TranId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.TranId = params.get("TranId")
        self.RequestId = params.get("RequestId")


class CreateWxCloudBaseRunServerDBClusterRequest(AbstractModel):
    """CreateWxCloudBaseRunServerDBCluster请求参数结构体

    """

    def __init__(self):
        """
        :param AccountPassword: 账户密码\n        :type AccountPassword: str\n        :param EnvId: 环境ID\n        :type EnvId: str\n        :param WxAppId: 微信appid\n        :type WxAppId: str\n        """
        self.AccountPassword = None
        self.EnvId = None
        self.WxAppId = None


    def _deserialize(self, params):
        self.AccountPassword = params.get("AccountPassword")
        self.EnvId = params.get("EnvId")
        self.WxAppId = params.get("WxAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWxCloudBaseRunServerDBClusterResponse(AbstractModel):
    """CreateWxCloudBaseRunServerDBCluster返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DatabasesInfo(AbstractModel):
    """数据库资源信息

    """

    def __init__(self):
        """
        :param InstanceId: 数据库唯一标识\n        :type InstanceId: str\n        :param Status: 状态。包含以下取值：
<li>INITIALIZING：资源初始化中</li>
<li>RUNNING：运行中，可正常使用的状态</li>
<li>UNUSABLE：禁用，不可用</li>
<li>OVERDUE：资源过期</li>\n        :type Status: str\n        :param Region: 所属地域。
当前支持ap-shanghai\n        :type Region: str\n        """
        self.InstanceId = None
        self.Status = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudBaseProjectLatestVersionRequest(AbstractModel):
    """DeleteCloudBaseProjectLatestVersion请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id\n        :type EnvId: str\n        :param ProjectName: 项目名\n        :type ProjectName: str\n        :param KeepResource: 是否保留资源\n        :type KeepResource: bool\n        """
        self.EnvId = None
        self.ProjectName = None
        self.KeepResource = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ProjectName = params.get("ProjectName")
        self.KeepResource = params.get("KeepResource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudBaseProjectLatestVersionResponse(AbstractModel):
    """DeleteCloudBaseProjectLatestVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCloudBaseRunServerVersionRequest(AbstractModel):
    """DeleteCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param ServerName: 服务名称\n        :type ServerName: str\n        :param VersionName: 版本名称\n        :type VersionName: str\n        :param IsDeleteServer: 是否删除服务，只有最后一个版本的时候，才生效。\n        :type IsDeleteServer: bool\n        :param IsDeleteImage: 只有删除服务的时候，才会起作用\n        :type IsDeleteImage: bool\n        :param OperatorRemark: 操作备注\n        :type OperatorRemark: str\n        """
        self.EnvId = None
        self.ServerName = None
        self.VersionName = None
        self.IsDeleteServer = None
        self.IsDeleteImage = None
        self.OperatorRemark = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.VersionName = params.get("VersionName")
        self.IsDeleteServer = params.get("IsDeleteServer")
        self.IsDeleteImage = params.get("IsDeleteImage")
        self.OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudBaseRunServerVersionResponse(AbstractModel):
    """DeleteCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，succ为成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteEndUserRequest(AbstractModel):
    """DeleteEndUser请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param UserList: 用户列表，每一项都是uuid\n        :type UserList: list of str\n        """
        self.EnvId = None
        self.UserList = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.UserList = params.get("UserList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEndUserResponse(AbstractModel):
    """DeleteEndUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWxGatewayRouteRequest(AbstractModel):
    """DeleteWxGatewayRoute请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id\n        :type EnvId: str\n        :param GatewayRouteName: 服务名称\n        :type GatewayRouteName: str\n        """
        self.EnvId = None
        self.GatewayRouteName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.GatewayRouteName = params.get("GatewayRouteName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWxGatewayRouteResponse(AbstractModel):
    """DeleteWxGatewayRoute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeActivityRecordRequest(AbstractModel):
    """DescribeActivityRecord请求参数结构体

    """

    def __init__(self):
        """
        :param ChannelToken: 渠道加密token\n        :type ChannelToken: str\n        :param Channel: 渠道来源，每个来源对应不同secretKey\n        :type Channel: str\n        :param ActivityIdList: 活动id列表\n        :type ActivityIdList: list of int\n        :param Status: 过滤状态码，已废弃\n        :type Status: int\n        :param Statuses: 状态码过滤数组，空数组时不过滤\n        :type Statuses: list of int\n        """
        self.ChannelToken = None
        self.Channel = None
        self.ActivityIdList = None
        self.Status = None
        self.Statuses = None


    def _deserialize(self, params):
        self.ChannelToken = params.get("ChannelToken")
        self.Channel = params.get("Channel")
        self.ActivityIdList = params.get("ActivityIdList")
        self.Status = params.get("Status")
        self.Statuses = params.get("Statuses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActivityRecordResponse(AbstractModel):
    """DescribeActivityRecord返回参数结构体

    """

    def __init__(self):
        """
        :param ActivityRecords: 活动记录详情\n        :type ActivityRecords: list of ActivityRecordItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ActivityRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ActivityRecords") is not None:
            self.ActivityRecords = []
            for item in params.get("ActivityRecords"):
                obj = ActivityRecordItem()
                obj._deserialize(item)
                self.ActivityRecords.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAuthDomainsRequest(AbstractModel):
    """DescribeAuthDomains请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuthDomainsResponse(AbstractModel):
    """DescribeAuthDomains返回参数结构体

    """

    def __init__(self):
        """
        :param Domains: 安全域名列表列表\n        :type Domains: list of AuthDomain\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境id\n        :type EnvId: str\n        :param ServiceName: 服务名\n        :type ServiceName: str\n        :param CIBusiness: build类型,枚举值有: cloudbaserun, framework-ci\n        :type CIBusiness: str\n        :param ServiceVersion: 服务版本\n        :type ServiceVersion: str\n        """
        self.EnvId = None
        self.ServiceName = None
        self.CIBusiness = None
        self.ServiceVersion = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServiceName = params.get("ServiceName")
        self.CIBusiness = params.get("CIBusiness")
        self.ServiceVersion = params.get("ServiceVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseBuildServiceResponse(AbstractModel):
    """DescribeCloudBaseBuildService返回参数结构体

    """

    def __init__(self):
        """
        :param UploadUrl: 上传url\n        :type UploadUrl: str\n        :param UploadHeaders: 上传heder\n        :type UploadHeaders: list of KVPair\n        :param PackageName: 包名\n        :type PackageName: str\n        :param PackageVersion: 包版本\n        :type PackageVersion: str\n        :param DownloadUrl: 下载链接
注意：此字段可能返回 null，表示取不到有效值。\n        :type DownloadUrl: str\n        :param DownloadHeaders: 下载Httpheader
注意：此字段可能返回 null，表示取不到有效值。\n        :type DownloadHeaders: list of KVPair\n        :param OutDate: 下载链接是否过期
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutDate: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 偏移量\n        :type Offset: int\n        :param PageSize: 个数\n        :type PageSize: int\n        :param EnvId: 环境id, 非必填\n        :type EnvId: str\n        :param ProjectName: 项目名称, 非必填\n        :type ProjectName: str\n        :param ProjectType: 项目类型: framework-oneclick,qci-extension-cicd\n        :type ProjectType: str\n        :param Tags: 标签\n        :type Tags: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseProjectLatestVersionListResponse(AbstractModel):
    """DescribeCloudBaseProjectLatestVersionList返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectList: 项目列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectList: list of CloudBaseProjectVersion\n        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境id\n        :type EnvId: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param PageSize: 页大小\n        :type PageSize: int\n        :param PageNum: 第几页,从0开始\n        :type PageNum: int\n        :param StartTime: 起始时间 2021-03-27 12:00:00\n        :type StartTime: str\n        :param EndTime: 终止时间 2021-03-27 12:00:00\n        :type EndTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseProjectVersionListResponse(AbstractModel):
    """DescribeCloudBaseProjectVersionList返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectVersions: 版本列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectVersions: list of CloudBaseProjectVersion\n        :param TotalCount: 总个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeCloudBaseRunConfForGateWayRequest(AbstractModel):
    """DescribeCloudBaseRunConfForGateWay请求参数结构体

    """

    def __init__(self):
        """
        :param EnvID: 环境ID\n        :type EnvID: str\n        :param VpcID: vpc信息\n        :type VpcID: str\n        """
        self.EnvID = None
        self.VpcID = None


    def _deserialize(self, params):
        self.EnvID = params.get("EnvID")
        self.VpcID = params.get("VpcID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunConfForGateWayResponse(AbstractModel):
    """DescribeCloudBaseRunConfForGateWay返回参数结构体

    """

    def __init__(self):
        """
        :param LastUpTime: 最近更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastUpTime: str\n        :param Data: 配置信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: list of CloudBaseRunForGatewayConf\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LastUpTime = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LastUpTime = params.get("LastUpTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CloudBaseRunForGatewayConf()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunResourceForExtendRequest(AbstractModel):
    """DescribeCloudBaseRunResourceForExtend请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunResourceForExtendResponse(AbstractModel):
    """DescribeCloudBaseRunResourceForExtend返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterStatus: 集群状态(creating/succ)
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterStatus: str\n        :param VirtualClusterId: 虚拟集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type VirtualClusterId: str\n        :param VpcId: vpc id信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param Region: 地域信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param SubnetIds: 子网信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetIds: list of CloudBaseRunVpcSubnet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境ID\n        :type EnvId: str\n        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunResourceResponse(AbstractModel):
    """DescribeCloudBaseRunResource返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterStatus: 集群状态(creating/succ)
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterStatus: str\n        :param VirtualClusterId: 虚拟集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type VirtualClusterId: str\n        :param VpcId: vpc id信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param Region: 地域信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param SubnetIds: 子网信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetIds: list of CloudBaseRunVpcSubnet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param ServerName: 服务名称\n        :type ServerName: str\n        :param VersionName: 版本名称\n        :type VersionName: str\n        """
        self.EnvId = None
        self.ServerName = None
        self.VersionName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunServerVersionResponse(AbstractModel):
    """DescribeCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        """
        :param VersionName: 版本名称\n        :type VersionName: str\n        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param DockerfilePath: Dockefile的路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type DockerfilePath: str\n        :param BuildDir: DockerBuild的目录
注意：此字段可能返回 null，表示取不到有效值。\n        :type BuildDir: str\n        :param Cpu: 请使用CPUSize\n        :type Cpu: int\n        :param Mem: 请使用MemSize\n        :type Mem: int\n        :param MinNum: 副本最小值\n        :type MinNum: int\n        :param MaxNum: 副本最大值\n        :type MaxNum: int\n        :param PolicyType: 策略类型\n        :type PolicyType: str\n        :param PolicyThreshold: 策略阈值\n        :type PolicyThreshold: float\n        :param EnvParams: 环境变量
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvParams: str\n        :param CreatedTime: 创建时间\n        :type CreatedTime: str\n        :param UpdatedTime: 更新时间\n        :type UpdatedTime: str\n        :param VersionIP: 版本的IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionIP: str\n        :param VersionPort: 版本的端口号
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionPort: int\n        :param Status: 版本状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param PackageName: 代码包的名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageName: str\n        :param PackageVersion: 代码版本的名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageVersion: str\n        :param UploadType: 枚举（package/repository/image)
注意：此字段可能返回 null，表示取不到有效值。\n        :type UploadType: str\n        :param RepoType: Repo的类型(gitlab/github/coding)
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepoType: str\n        :param Repo: 地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type Repo: str\n        :param Branch: 分支
注意：此字段可能返回 null，表示取不到有效值。\n        :type Branch: str\n        :param ServerName: 服务名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServerName: str\n        :param IsPublic: 是否对于外网开放
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsPublic: bool\n        :param VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param SubnetIds: 子网实例id
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetIds: list of str\n        :param CustomLogs: 日志采集路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type CustomLogs: str\n        :param ContainerPort: 监听端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContainerPort: int\n        :param InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）
注意：此字段可能返回 null，表示取不到有效值。\n        :type InitialDelaySeconds: int\n        :param ImageUrl: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageUrl: str\n        :param CpuSize: CPU 大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type CpuSize: float\n        :param MemSize: MEM 大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemSize: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param ServerName: 服务名称\n        :type ServerName: str\n        :param VersionName: 版本名称\n        :type VersionName: str\n        """
        self.EnvId = None
        self.ServerName = None
        self.VersionName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunVersionResponse(AbstractModel):
    """DescribeCloudBaseRunVersion返回参数结构体

    """

    def __init__(self):
        """
        :param VersionName: 版本名称\n        :type VersionName: str\n        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param DockerfilePath: Dockefile的路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type DockerfilePath: str\n        :param BuildDir: DockerBuild的目录
注意：此字段可能返回 null，表示取不到有效值。\n        :type BuildDir: str\n        :param MinNum: 副本最小值\n        :type MinNum: int\n        :param MaxNum: 副本最大值\n        :type MaxNum: int\n        :param PolicyType: 策略类型\n        :type PolicyType: str\n        :param PolicyThreshold: 策略阈值\n        :type PolicyThreshold: float\n        :param EnvParams: 环境变量
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvParams: str\n        :param CreatedTime: 创建时间\n        :type CreatedTime: str\n        :param UpdatedTime: 更新时间\n        :type UpdatedTime: str\n        :param VersionIP: 版本的IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionIP: str\n        :param VersionPort: 版本的端口号
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionPort: int\n        :param Status: 版本状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param PackageName: 代码包的名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageName: str\n        :param PackageVersion: 代码版本的名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageVersion: str\n        :param UploadType: 枚举（package/repository/image)
注意：此字段可能返回 null，表示取不到有效值。\n        :type UploadType: str\n        :param RepoType: Repo的类型(coding/gitlab/github/coding)
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepoType: str\n        :param Repo: 地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type Repo: str\n        :param Branch: 分支
注意：此字段可能返回 null，表示取不到有效值。\n        :type Branch: str\n        :param ServerName: 服务名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServerName: str\n        :param IsPublic: 是否对于外网开放
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsPublic: bool\n        :param VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param SubnetIds: 子网实例id
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetIds: list of str\n        :param CustomLogs: 日志采集路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type CustomLogs: str\n        :param ContainerPort: 监听端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContainerPort: int\n        :param InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）
注意：此字段可能返回 null，表示取不到有效值。\n        :type InitialDelaySeconds: int\n        :param ImageUrl: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageUrl: str\n        :param CpuSize: CPU 大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type CpuSize: float\n        :param MemSize: MEM 大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemSize: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ServerName: 服务名\n        :type ServerName: str\n        :param VersionName: 版本名\n        :type VersionName: str\n        :param EnvId: 环境id\n        :type EnvId: str\n        :param SnapshotName: 版本历史名\n        :type SnapshotName: str\n        :param Offset: 偏移量。默认0\n        :type Offset: int\n        :param Limit: 限制大小。默认10，最大20\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunVersionSnapshotResponse(AbstractModel):
    """DescribeCloudBaseRunVersionSnapshot返回参数结构体

    """

    def __init__(self):
        """
        :param Snapshots: 版本历史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Snapshots: list of CloudRunServiceSimpleVersionSnapshot\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeCurveDataRequest(AbstractModel):
    """DescribeCurveData请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param MetricName: <li> 指标名: </li>
<li> StorageRead: 存储读请求次数 </li>
<li> StorageWrite: 存储写请求次数 </li>
<li> StorageCdnOriginFlux: CDN回源流量, 单位字节 </li>
<li> CDNFlux: CDN回源流量, 单位字节 </li>
<li> FunctionInvocation: 云函数调用次数 </li>
<li> FunctionGBs: 云函数资源使用量, 单位Mb*Ms </li>
<li> FunctionFlux: 云函数流量, 单位千字节(KB) </li>
<li> FunctionError: 云函数调用错误次数 </li>
<li> FunctionDuration: 云函数运行时间, 单位毫秒 </li>
<li> DbRead: 数据库读请求数 </li>
<li> DbWrite: 数据库写请求数 </li>
<li> DbCostTime10ms: 数据库耗时在10ms~50ms请求数 </li>
<li> DbCostTime50ms: 数据库耗时在50ms~100ms请求数 </li>
<li> DbCostTime100ms: 数据库耗时在100ms以上请求数 </li>
<li> TkeCpuRatio: 容器CPU占用率 </li>
<li> TkeMemRatio: 容器内存占用率 </li>
<li> TkeCpuUsed: 容器CPU使用量 </li>
<li> TkeMemUsed: 容器内存使用量 </li>
<li> TkeInvokeNum: 调用量 </li>\n        :type MetricName: str\n        :param StartTime: 开始时间，如2018-08-24 10:50:00, 开始时间需要早于结束时间至少五分钟(原因是因为目前统计粒度最小是5分钟).\n        :type StartTime: str\n        :param EndTime: 结束时间，如2018-08-24 10:50:00, 结束时间需要晚于开始时间至少五分钟(原因是因为目前统计粒度最小是5分钟)..\n        :type EndTime: str\n        :param ResourceID: 资源ID, 目前仅对云函数、容器托管相关的指标有意义。云函数(FunctionInvocation, FunctionGBs, FunctionFlux, FunctionError, FunctionDuration)、容器托管（服务名称）, 如果想查询某个云函数的指标则在ResourceId中传入函数名; 如果只想查询整个namespace的指标, 则留空或不传.如果想查询数据库某个集合相关信息，传入集合名称\n        :type ResourceID: str\n        """
        self.EnvId = None
        self.MetricName = None
        self.StartTime = None
        self.EndTime = None
        self.ResourceID = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.MetricName = params.get("MetricName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ResourceID = params.get("ResourceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCurveDataResponse(AbstractModel):
    """DescribeCurveData返回参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间, 会根据数据的统计周期进行取整.\n        :type StartTime: str\n        :param EndTime: 结束时间, 会根据数据的统计周期进行取整.\n        :type EndTime: str\n        :param MetricName: 指标名.\n        :type MetricName: str\n        :param Period: 统计周期(单位秒), 当时间区间为1天内, 统计周期为5分钟; 当时间区间选择为1天以上, 15天以下, 统计周期为1小时; 当时间区间选择为15天以上, 180天以下, 统计周期为1天.\n        :type Period: int\n        :param Values: 有效的监控数据, 每个有效监控数据的上报时间可以从时间数组中的对应位置上获取到.\n        :type Values: list of int\n        :param Time: 时间数据, 标识监控数据Values中的点是哪个时间段上报的.\n        :type Time: list of int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Period = None
        self.Values = None
        self.Time = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.Values = params.get("Values")
        self.Time = params.get("Time")
        self.RequestId = params.get("RequestId")


class DescribeDatabaseACLRequest(AbstractModel):
    """DescribeDatabaseACL请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param CollectionName: 集合名称\n        :type CollectionName: str\n        """
        self.EnvId = None
        self.CollectionName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CollectionName = params.get("CollectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseACLResponse(AbstractModel):
    """DescribeDatabaseACL返回参数结构体

    """

    def __init__(self):
        """
        :param AclTag: 权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>\n        :type AclTag: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param CodeUri: 代码uri，格式如：extension://abcdefhhxxx.zip，对应 DescribeExtensionUploadInfo 接口的返回值\n        :type CodeUri: str\n        """
        self.CodeUri = None


    def _deserialize(self, params):
        self.CodeUri = params.get("CodeUri")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDownloadFileResponse(AbstractModel):
    """DescribeDownloadFile返回参数结构体

    """

    def __init__(self):
        """
        :param FilePath: 文件路径，该字段已废弃
注意：此字段可能返回 null，表示取不到有效值。\n        :type FilePath: str\n        :param CustomKey: 加密key，用于计算下载加密文件的header。参考SSE-C https://cloud.tencent.com/document/product/436/7728#sse-c
注意：此字段可能返回 null，表示取不到有效值。\n        :type CustomKey: str\n        :param DownloadUrl: 下载链接
注意：此字段可能返回 null，表示取不到有效值。\n        :type DownloadUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境id\n        :type EnvId: str\n        :param Source: 终端用户来源
<li> qcloud </li>
<li>miniapp</li>\n        :type Source: str\n        """
        self.EnvId = None
        self.Source = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEndUserLoginStatisticResponse(AbstractModel):
    """DescribeEndUserLoginStatistic返回参数结构体

    """

    def __init__(self):
        """
        :param LoginStatistics: 环境终端用户新增与登录统计
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoginStatistics: list of LoginStatistic\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境id\n        :type EnvId: str\n        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEndUserStatisticResponse(AbstractModel):
    """DescribeEndUserStatistic返回参数结构体

    """

    def __init__(self):
        """
        :param PlatformStatistics: 终端用户各平台统计
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlatformStatistics: list of PlatformStatistic\n        :param TotalCount: 终端用户总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 开发者的环境ID\n        :type EnvId: str\n        :param Offset: 可选参数，偏移量，默认 0\n        :type Offset: int\n        :param Limit: 可选参数，拉取数量，默认 20\n        :type Limit: int\n        :param UUIds: 按照 uuid 列表过滤，最大个数为100\n        :type UUIds: list of str\n        """
        self.EnvId = None
        self.Offset = None
        self.Limit = None
        self.UUIds = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.UUIds = params.get("UUIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEndUsersResponse(AbstractModel):
    """DescribeEndUsers返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 用户总数\n        :type Total: int\n        :param Users: 用户列表\n        :type Users: list of EndUserInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param ResourceTypes: 资源类型：可选值：CDN, COS, FLEXDB, HOSTING, SCF
不传则返回全部资源指标\n        :type ResourceTypes: list of str\n        """
        self.EnvId = None
        self.ResourceTypes = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ResourceTypes = params.get("ResourceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvFreeQuotaResponse(AbstractModel):
    """DescribeEnvFreeQuota返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaItems: 免费抵扣配额详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type QuotaItems: list of PostpayEnvQuota\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param MaxEnvNum: 环境总数上限\n        :type MaxEnvNum: int\n        :param CurrentEnvNum: 目前环境总数\n        :type CurrentEnvNum: int\n        :param MaxFreeEnvNum: 免费环境数量上限\n        :type MaxFreeEnvNum: int\n        :param CurrentFreeEnvNum: 目前免费环境数量\n        :type CurrentFreeEnvNum: int\n        :param MaxDeleteTotal: 总计允许销毁环境次数上限\n        :type MaxDeleteTotal: int\n        :param CurrentDeleteTotal: 目前已销毁环境次数\n        :type CurrentDeleteTotal: int\n        :param MaxDeleteMonthly: 每月允许销毁环境次数上限\n        :type MaxDeleteMonthly: int\n        :param CurrentDeleteMonthly: 本月已销毁环境次数\n        :type CurrentDeleteMonthly: int\n        :param MaxFreeTrialNum: 微信网关体验版可购买月份数\n        :type MaxFreeTrialNum: int\n        :param CurrentFreeTrialNum: 微信网关体验版已购买月份数\n        :type CurrentFreeTrialNum: int\n        :param ChangePayTotal: 转支付限额总数\n        :type ChangePayTotal: int\n        :param CurrentChangePayTotal: 当前已用转支付次数\n        :type CurrentChangePayTotal: int\n        :param ChangePayMonthly: 转支付每月限额\n        :type ChangePayMonthly: int\n        :param CurrentChangePayMonthly: 本月已用转支付额度\n        :type CurrentChangePayMonthly: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MaxEnvNum = None
        self.CurrentEnvNum = None
        self.MaxFreeEnvNum = None
        self.CurrentFreeEnvNum = None
        self.MaxDeleteTotal = None
        self.CurrentDeleteTotal = None
        self.MaxDeleteMonthly = None
        self.CurrentDeleteMonthly = None
        self.MaxFreeTrialNum = None
        self.CurrentFreeTrialNum = None
        self.ChangePayTotal = None
        self.CurrentChangePayTotal = None
        self.ChangePayMonthly = None
        self.CurrentChangePayMonthly = None
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
        self.MaxFreeTrialNum = params.get("MaxFreeTrialNum")
        self.CurrentFreeTrialNum = params.get("CurrentFreeTrialNum")
        self.ChangePayTotal = params.get("ChangePayTotal")
        self.CurrentChangePayTotal = params.get("CurrentChangePayTotal")
        self.ChangePayMonthly = params.get("ChangePayMonthly")
        self.CurrentChangePayMonthly = params.get("CurrentChangePayMonthly")
        self.RequestId = params.get("RequestId")


class DescribeEnvPostpaidDeductRequest(AbstractModel):
    """DescribeEnvPostpaidDeduct请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceTypes: 资源方列表\n        :type ResourceTypes: list of str\n        :param EnvId: 环境id\n        :type EnvId: str\n        :param StartTime: 查询开始时间\n        :type StartTime: str\n        :param EndTime: 查询结束时间\n        :type EndTime: str\n        """
        self.ResourceTypes = None
        self.EnvId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ResourceTypes = params.get("ResourceTypes")
        self.EnvId = params.get("EnvId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvPostpaidDeductResponse(AbstractModel):
    """DescribeEnvPostpaidDeduct返回参数结构体

    """

    def __init__(self):
        """
        :param PostPaidEnvDeductInfoList: 指标抵扣详情列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type PostPaidEnvDeductInfoList: list of PostPaidEnvDeductInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PostPaidEnvDeductInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PostPaidEnvDeductInfoList") is not None:
            self.PostPaidEnvDeductInfoList = []
            for item in params.get("PostPaidEnvDeductInfoList"):
                obj = PostPaidEnvDeductInfo()
                obj._deserialize(item)
                self.PostPaidEnvDeductInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvsRequest(AbstractModel):
    """DescribeEnvs请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID，如果传了这个参数则只返回该环境的相关信息\n        :type EnvId: str\n        :param IsVisible: 指定Channels字段为可见渠道列表或不可见渠道列表
如只想获取渠道A的环境 就填写IsVisible= true,Channels = ["A"], 过滤渠道A拉取其他渠道环境时填写IsVisible= false,Channels = ["A"]\n        :type IsVisible: bool\n        :param Channels: 渠道列表，代表可见或不可见渠道由IsVisible参数指定\n        :type Channels: list of str\n        """
        self.EnvId = None
        self.IsVisible = None
        self.Channels = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.IsVisible = params.get("IsVisible")
        self.Channels = params.get("Channels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvsResponse(AbstractModel):
    """DescribeEnvs返回参数结构体

    """

    def __init__(self):
        """
        :param EnvList: 环境信息列表\n        :type EnvList: list of EnvInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ExtensionFiles: 待上传的文件\n        :type ExtensionFiles: list of ExtensionFile\n        """
        self.ExtensionFiles = None


    def _deserialize(self, params):
        if params.get("ExtensionFiles") is not None:
            self.ExtensionFiles = []
            for item in params.get("ExtensionFiles"):
                obj = ExtensionFile()
                obj._deserialize(item)
                self.ExtensionFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtensionUploadInfoResponse(AbstractModel):
    """DescribeExtensionUploadInfo返回参数结构体

    """

    def __init__(self):
        """
        :param FilesData: 待上传文件的信息数组\n        :type FilesData: list of ExtensionFileInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 已购买增值包的环境ID\n        :type EnvId: str\n        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtraPkgBillingInfoResponse(AbstractModel):
    """DescribeExtraPkgBillingInfo返回参数结构体

    """

    def __init__(self):
        """
        :param EnvInfoList: 增值包计费信息列表\n        :type EnvInfoList: list of EnvBillingInfoItem\n        :param Total: 增值包数目\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeHostingDomainTaskRequest(AbstractModel):
    """DescribeHostingDomainTask请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostingDomainTaskResponse(AbstractModel):
    """DescribeHostingDomainTask返回参数结构体

    """

    def __init__(self):
        """
        :param Status: todo/doing/done/error\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribePostpayFreeQuotasRequest(AbstractModel):
    """DescribePostpayFreeQuotas请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePostpayFreeQuotasResponse(AbstractModel):
    """DescribePostpayFreeQuotas返回参数结构体

    """

    def __init__(self):
        """
        :param FreequotaInfoList: 免费量资源信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type FreequotaInfoList: list of FreequotaInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param FreeQuotaType: 免费额度类型标识\n        :type FreeQuotaType: str\n        """
        self.EnvId = None
        self.FreeQuotaType = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.FreeQuotaType = params.get("FreeQuotaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePostpayPackageFreeQuotasResponse(AbstractModel):
    """DescribePostpayPackageFreeQuotas返回参数结构体

    """

    def __init__(self):
        """
        :param PackageFreeQuotaInfos: 免费量资源信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageFreeQuotaInfos: list of PackageFreeQuotaInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param MetricName: <li> 指标名: </li>
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
<li> TkeHttpServiceNatPkgDay: 当天容器托管流量使用量，单位B </li>\n        :type MetricName: str\n        :param ResourceID: 资源ID, 目前仅对云函数、容器托管相关的指标有意义。云函数(FunctionInvocationpkg, FunctionGBspkg, FunctionFluxpkg)、容器托管（服务名称）。如果想查询某个云函数的指标则在ResourceId中传入函数名; 如果只想查询整个namespace的指标, 则留空或不传。\n        :type ResourceID: str\n        """
        self.EnvId = None
        self.MetricName = None
        self.ResourceID = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.MetricName = params.get("MetricName")
        self.ResourceID = params.get("ResourceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQuotaDataResponse(AbstractModel):
    """DescribeQuotaData返回参数结构体

    """

    def __init__(self):
        """
        :param MetricName: 指标名\n        :type MetricName: str\n        :param Value: 指标的值\n        :type Value: int\n        :param SubValue: 指标的附加值信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubValue: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvId: 环境ID\n        :type EnvId: str\n        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsQuotasResponse(AbstractModel):
    """DescribeSmsQuotas返回参数结构体

    """

    def __init__(self):
        """
        :param SmsFreeQuotaList: 短信免费量信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SmsFreeQuotaList: list of SmsFreeQuota\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeSpecialCostItemsRequest(AbstractModel):
    """DescribeSpecialCostItems请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id\n        :type EnvId: str\n        :param StartTime: 查询开始时间\n        :type StartTime: str\n        :param EndTime: 查询结束时间\n        :type EndTime: str\n        """
        self.EnvId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecialCostItemsResponse(AbstractModel):
    """DescribeSpecialCostItems返回参数结构体

    """

    def __init__(self):
        """
        :param SpecialCostItems: 1分钱抵扣详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type SpecialCostItems: list of SpecialCostItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SpecialCostItems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecialCostItems") is not None:
            self.SpecialCostItems = []
            for item in params.get("SpecialCostItems"):
                obj = SpecialCostItem()
                obj._deserialize(item)
                self.SpecialCostItems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStandaloneGatewayPackageRequest(AbstractModel):
    """DescribeStandaloneGatewayPackage请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param PackageVersion: 套餐版本，包含starter、basic、advanced、enterprise\n        :type PackageVersion: str\n        """
        self.EnvId = None
        self.PackageVersion = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.PackageVersion = params.get("PackageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStandaloneGatewayPackageResponse(AbstractModel):
    """DescribeStandaloneGatewayPackage返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 总数\n        :type Total: int\n        :param StandaloneGatewayPackageList: 套餐详情\n        :type StandaloneGatewayPackageList: list of StandaloneGatewayPackageInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.StandaloneGatewayPackageList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("StandaloneGatewayPackageList") is not None:
            self.StandaloneGatewayPackageList = []
            for item in params.get("StandaloneGatewayPackageList"):
                obj = StandaloneGatewayPackageInfo()
                obj._deserialize(item)
                self.StandaloneGatewayPackageList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStandaloneGatewayRequest(AbstractModel):
    """DescribeStandaloneGateway请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param GatewayName: 网关名称\n        :type GatewayName: str\n        :param GatewayAlias: 网关别名\n        :type GatewayAlias: str\n        """
        self.EnvId = None
        self.GatewayName = None
        self.GatewayAlias = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.GatewayName = params.get("GatewayName")
        self.GatewayAlias = params.get("GatewayAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStandaloneGatewayResponse(AbstractModel):
    """DescribeStandaloneGateway返回参数结构体

    """

    def __init__(self):
        """
        :param StandaloneGatewayList: 独立网关信息列表\n        :type StandaloneGatewayList: list of StandaloneGatewayInfo\n        :param Total: 总数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.StandaloneGatewayList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StandaloneGatewayList") is not None:
            self.StandaloneGatewayList = []
            for item in params.get("StandaloneGatewayList"):
                obj = StandaloneGatewayInfo()
                obj._deserialize(item)
                self.StandaloneGatewayList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeWxCloudBaseRunEnvsRequest(AbstractModel):
    """DescribeWxCloudBaseRunEnvs请求参数结构体

    """

    def __init__(self):
        """
        :param WxAppId: wx应用Id\n        :type WxAppId: str\n        """
        self.WxAppId = None


    def _deserialize(self, params):
        self.WxAppId = params.get("WxAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWxCloudBaseRunEnvsResponse(AbstractModel):
    """DescribeWxCloudBaseRunEnvs返回参数结构体

    """

    def __init__(self):
        """
        :param EnvList: env列表\n        :type EnvList: list of EnvInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeWxCloudBaseRunSubNetsRequest(AbstractModel):
    """DescribeWxCloudBaseRunSubNets请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC id\n        :type VpcId: str\n        :param Limit: 查询个数限制，不填或小于等于0，等于不限制\n        :type Limit: int\n        """
        self.VpcId = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWxCloudBaseRunSubNetsResponse(AbstractModel):
    """DescribeWxCloudBaseRunSubNets返回参数结构体

    """

    def __init__(self):
        """
        :param SubNetIds: 子网Id列表\n        :type SubNetIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SubNetIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubNetIds = params.get("SubNetIds")
        self.RequestId = params.get("RequestId")


class DestroyEnvRequest(AbstractModel):
    """DestroyEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境Id\n        :type EnvId: str\n        :param IsForce: 针对预付费 删除隔离中的环境时要传true 正常环境直接跳过隔离期删除\n        :type IsForce: bool\n        :param BypassCheck: 是否绕过资源检查，资源包等额外资源，默认为false，如果为true，则不检查资源是否有数据，直接删除。\n        :type BypassCheck: bool\n        """
        self.EnvId = None
        self.IsForce = None
        self.BypassCheck = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.IsForce = params.get("IsForce")
        self.BypassCheck = params.get("BypassCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyEnvResponse(AbstractModel):
    """DestroyEnv返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DestroyStandaloneGatewayRequest(AbstractModel):
    """DestroyStandaloneGateway请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param GatewayName: 网名名称\n        :type GatewayName: str\n        :param IsForce: 是否强制释放\n        :type IsForce: bool\n        """
        self.EnvId = None
        self.GatewayName = None
        self.IsForce = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.GatewayName = params.get("GatewayName")
        self.IsForce = params.get("IsForce")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyStandaloneGatewayResponse(AbstractModel):
    """DestroyStandaloneGateway返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 删除独立网关状态\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DestroyStaticStoreRequest(AbstractModel):
    """DestroyStaticStore请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param CdnDomain: cdn域名\n        :type CdnDomain: str\n        """
        self.EnvId = None
        self.CdnDomain = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CdnDomain = params.get("CdnDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyStaticStoreResponse(AbstractModel):
    """DestroyStaticStore返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 条件任务结果(succ/fail)\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param UUId: 用户唯一ID\n        :type UUId: str\n        :param WXOpenId: 微信ID\n        :type WXOpenId: str\n        :param QQOpenId: qq ID\n        :type QQOpenId: str\n        :param Phone: 手机号\n        :type Phone: str\n        :param Email: 邮箱\n        :type Email: str\n        :param NickName: 昵称\n        :type NickName: str\n        :param Gender: 性别\n        :type Gender: str\n        :param AvatarUrl: 头像地址\n        :type AvatarUrl: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param IsAnonymous: 是否为匿名用户\n        :type IsAnonymous: bool\n        :param IsDisabled: 是否禁用账户\n        :type IsDisabled: bool\n        :param HasPassword: 是否设置过密码\n        :type HasPassword: bool\n        :param UserName: 用户名\n        :type UserName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvBillingInfoItem(AbstractModel):
    """环境计费信息

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param PackageId: tcb产品套餐ID，参考DescribePackages接口的返回值。\n        :type PackageId: str\n        :param IsAutoRenew: 自动续费标记\n        :type IsAutoRenew: bool\n        :param Status: 状态。包含以下取值：
<li> 空字符串：初始化中</li>
<li> NORMAL：正常</li>
<li> ISOLATE：隔离</li>\n        :type Status: str\n        :param PayMode: 支付方式。包含以下取值：
<li> PREPAYMENT：预付费</li>
<li> POSTPAID：后付费</li>\n        :type PayMode: str\n        :param IsolatedTime: 隔离时间，最近一次隔离的时间\n        :type IsolatedTime: str\n        :param ExpireTime: 过期时间，套餐即将到期的时间\n        :type ExpireTime: str\n        :param CreateTime: 创建时间，第一次接入计费方案的时间。\n        :type CreateTime: str\n        :param UpdateTime: 更新时间，计费信息最近一次更新的时间。\n        :type UpdateTime: str\n        :param IsAlwaysFree: true表示从未升级过付费版。\n        :type IsAlwaysFree: bool\n        :param PaymentChannel: 付费渠道。
<li> miniapp：小程序</li>
<li> qcloud：腾讯云</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type PaymentChannel: str\n        :param OrderInfo: 最新的订单信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrderInfo: :class:`tencentcloud.tcb.v20180608.models.OrderInfo`\n        :param FreeQuota: 免费配额信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FreeQuota: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvInfo(AbstractModel):
    """环境信息

    """

    def __init__(self):
        """
        :param EnvId: 账户下该环境唯一标识\n        :type EnvId: str\n        :param Source: 环境来源。包含以下取值：
<li>miniapp：微信小程序</li>
<li>qcloud ：腾讯云</li>\n        :type Source: str\n        :param Alias: 环境别名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符\n        :type Alias: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 最后修改时间\n        :type UpdateTime: str\n        :param Status: 环境状态。包含以下取值：
<li>NORMAL：正常可用</li>
<li>UNAVAILABLE：服务不可用，可能是尚未初始化或者初始化过程中</li>\n        :type Status: str\n        :param Databases: 数据库列表\n        :type Databases: list of DatabasesInfo\n        :param Storages: 存储列表\n        :type Storages: list of StorageInfo\n        :param Functions: 函数列表\n        :type Functions: list of FunctionInfo\n        :param PackageId: tcb产品套餐ID，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageId: str\n        :param PackageName: 套餐中文名称，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageName: str\n        :param LogServices: 云日志服务列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogServices: list of LogServiceInfo\n        :param StaticStorages: 静态资源信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type StaticStorages: list of StaticStorageInfo\n        :param IsAutoDegrade: 是否到期自动降为免费版
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsAutoDegrade: bool\n        :param EnvChannel: 环境渠道
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvChannel: str\n        :param PayMode: 支付方式。包含以下取值：
<li> prepayment：预付费</li>
<li> postpaid：后付费</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayMode: str\n        :param IsDefault: 是否为默认环境
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDefault: bool\n        :param Region: 环境所属地域
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param Tags: 环境标签列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param CustomLogServices: 自定义日志服务
注意：此字段可能返回 null，表示取不到有效值。\n        :type CustomLogServices: list of ClsInfo\n        """
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
        self.Tags = None
        self.CustomLogServices = None


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
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("CustomLogServices") is not None:
            self.CustomLogServices = []
            for item in params.get("CustomLogServices"):
                obj = ClsInfo()
                obj._deserialize(item)
                self.CustomLogServices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EstablishCloudBaseRunServerRequest(AbstractModel):
    """EstablishCloudBaseRunServer请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id\n        :type EnvId: str\n        :param ServiceName: 服务名称\n        :type ServiceName: str\n        :param IsPublic: 是否开通外网访问\n        :type IsPublic: bool\n        :param ImageRepo: 镜像仓库\n        :type ImageRepo: str\n        :param Remark: 服务描述\n        :type Remark: str\n        :param EsInfo: es信息\n        :type EsInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseEsInfo`\n        :param LogType: 日志类型; es/cls\n        :type LogType: str\n        :param OperatorRemark: 操作备注\n        :type OperatorRemark: str\n        :param Source: 来源方（默认值：qcloud，微信侧来源miniapp)\n        :type Source: str\n        :param VpcInfo: vpc信息\n        :type VpcInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunVpcInfo`\n        :param PublicAccess: 0/1=允许公网访问;2=关闭公网访问\n        :type PublicAccess: int\n        :param OpenAccessTypes: OA PUBLIC MINIAPP VPC\n        :type OpenAccessTypes: list of str\n        :param IsCreatePath: 是否创建Path 0未传默认创建 1创建 2不创建\n        :type IsCreatePath: int\n        :param ServerPath: 指定创建路径（如不存在，则创建。存在，则忽略）\n        :type ServerPath: str\n        """
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
        self.OpenAccessTypes = None
        self.IsCreatePath = None
        self.ServerPath = None


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
        self.OpenAccessTypes = params.get("OpenAccessTypes")
        self.IsCreatePath = params.get("IsCreatePath")
        self.ServerPath = params.get("ServerPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EstablishCloudBaseRunServerResponse(AbstractModel):
    """EstablishCloudBaseRunServer返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EstablishWxGatewayRouteRequest(AbstractModel):
    """EstablishWxGatewayRoute请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayId: 网关id\n        :type GatewayId: str\n        :param GatewayRouteName: 服务名称\n        :type GatewayRouteName: str\n        :param GatewayRouteAddr: 服务地址\n        :type GatewayRouteAddr: str\n        :param GatewayRouteProtocol: 协议类型 http/https\n        :type GatewayRouteProtocol: str\n        :param GatewayRouteDesc: 服务描述\n        :type GatewayRouteDesc: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EstablishWxGatewayRouteResponse(AbstractModel):
    """EstablishWxGatewayRoute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
<li>SMS：短信文件</li>\n        :type FileType: str\n        :param FileName: 文件名，长度不超过24\n        :type FileName: str\n        """
        self.FileType = None
        self.FileName = None


    def _deserialize(self, params):
        self.FileType = params.get("FileType")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensionFileInfo(AbstractModel):
    """扩展文件信息

    """

    def __init__(self):
        """
        :param CodeUri: 模板里使用的地址\n        :type CodeUri: str\n        :param UploadUrl: 上传文件的临时地址，含签名\n        :type UploadUrl: str\n        :param CustomKey: 自定义密钥。如果为空，则表示不需要加密\n        :type CustomKey: str\n        :param MaxSize: 文件大小限制，单位M，客户端上传前需要主动检查文件大小，超过限制的文件会被删除。\n        :type MaxSize: int\n        """
        self.CodeUri = None
        self.UploadUrl = None
        self.CustomKey = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.CodeUri = params.get("CodeUri")
        self.UploadUrl = params.get("UploadUrl")
        self.CustomKey = params.get("CustomKey")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreequotaInfo(AbstractModel):
    """后付费资源免费量信息

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型
<li>COS</li>
<li>CDN</li>
<li>FLEXDB</li>
<li>SCF</li>\n        :type ResourceType: str\n        :param ResourceMetric: 资源指标名称\n        :type ResourceMetric: str\n        :param FreeQuota: 资源指标免费量\n        :type FreeQuota: int\n        :param MetricUnit: 指标单位\n        :type MetricUnit: str\n        :param DeductType: 免费量抵扣周期
<li>sum-month:以月为单位抵扣</li>
<li>sum-day:以天为单位抵扣</li>
<li>totalize:总容量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeductType: str\n        :param FreeQuotaType: 免费量类型
<li>basic:通用量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type FreeQuotaType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionInfo(AbstractModel):
    """函数的信息

    """

    def __init__(self):
        """
        :param Namespace: 命名空间\n        :type Namespace: str\n        :param Region: 所属地域。
当前支持ap-shanghai\n        :type Region: str\n        """
        self.Namespace = None
        self.Region = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVPair(AbstractModel):
    """键值对

    """

    def __init__(self):
        """
        :param Key: 键\n        :type Key: str\n        :param Value: 值\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogServiceInfo(AbstractModel):
    """云日志服务相关信息

    """

    def __init__(self):
        """
        :param LogsetName: log名\n        :type LogsetName: str\n        :param LogsetId: log-id\n        :type LogsetId: str\n        :param TopicName: topic名\n        :type TopicName: str\n        :param TopicId: topic-id\n        :type TopicId: str\n        :param Region: cls日志所属地域\n        :type Region: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginStatistic(AbstractModel):
    """终端用户登录新增统计

    """

    def __init__(self):
        """
        :param StatisticalType: 统计类型 新增NEWUSER 和登录 LOGIN
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatisticalType: str\n        :param StatisticalCycle: 统计周期：日DAY，周WEEK，月MONTH
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatisticalCycle: str\n        :param Count: 统计总量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Count: int\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        """
        self.StatisticalType = None
        self.StatisticalCycle = None
        self.Count = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.StatisticalType = params.get("StatisticalType")
        self.StatisticalCycle = params.get("StatisticalCycle")
        self.Count = params.get("Count")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudBaseRunServerFlowConfRequest(AbstractModel):
    """ModifyCloudBaseRunServerFlowConf请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param ServerName: 服务名称\n        :type ServerName: str\n        :param VersionFlowItems: 流量占比\n        :type VersionFlowItems: list of CloudBaseRunVersionFlowItem\n        :param TrafficType: 流量类型（URL_PARAMS / FLOW / HEADERS)\n        :type TrafficType: str\n        :param OperatorRemark: 操作备注\n        :type OperatorRemark: str\n        """
        self.EnvId = None
        self.ServerName = None
        self.VersionFlowItems = None
        self.TrafficType = None
        self.OperatorRemark = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        if params.get("VersionFlowItems") is not None:
            self.VersionFlowItems = []
            for item in params.get("VersionFlowItems"):
                obj = CloudBaseRunVersionFlowItem()
                obj._deserialize(item)
                self.VersionFlowItems.append(obj)
        self.TrafficType = params.get("TrafficType")
        self.OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudBaseRunServerFlowConfResponse(AbstractModel):
    """ModifyCloudBaseRunServerFlowConf返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，succ代表成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyDatabaseACLRequest(AbstractModel):
    """ModifyDatabaseACL请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param CollectionName: 集合名称\n        :type CollectionName: str\n        :param AclTag: 权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>\n        :type AclTag: str\n        """
        self.EnvId = None
        self.CollectionName = None
        self.AclTag = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CollectionName = params.get("CollectionName")
        self.AclTag = params.get("AclTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseACLResponse(AbstractModel):
    """ModifyDatabaseACL返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEndUserRequest(AbstractModel):
    """ModifyEndUser请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param UUId: C端用户端的唯一ID\n        :type UUId: str\n        :param Status: 帐号的状态
<li>ENABLE</li>
<li>DISABLE</li>\n        :type Status: str\n        """
        self.EnvId = None
        self.UUId = None
        self.Status = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.UUId = params.get("UUId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEndUserResponse(AbstractModel):
    """ModifyEndUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEnvRequest(AbstractModel):
    """ModifyEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param Alias: 环境备注名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符\n        :type Alias: str\n        """
        self.EnvId = None
        self.Alias = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvResponse(AbstractModel):
    """ModifyEnv返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ObjectKV(AbstractModel):
    """Key-Value类型，模拟的 object 类型

    """

    def __init__(self):
        """
        :param Key: object 的 key\n        :type Key: str\n        :param Value: object key 对应的 value\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderInfo(AbstractModel):
    """订单信息

    """

    def __init__(self):
        """
        :param TranId: 订单号\n        :type TranId: str\n        :param PackageId: 订单要切换的套餐ID\n        :type PackageId: str\n        :param TranType: 订单类型
<li>1 购买</li>
<li>2 续费</li>
<li>3 变配</li>\n        :type TranType: str\n        :param TranStatus: 订单状态。
<li>1未支付</li>
<li>2 支付中</li>
<li>3 发货中</li>
<li>4 发货成功</li>
<li>5 发货失败</li>
<li>6 已退款</li>
<li>7 已取消</li>
<li>100 已删除</li>\n        :type TranStatus: str\n        :param UpdateTime: 订单更新时间\n        :type UpdateTime: str\n        :param CreateTime: 订单创建时间\n        :type CreateTime: str\n        :param PayMode: 付费模式.
<li>prepayment 预付费</li>
<li>postpaid 后付费</li>\n        :type PayMode: str\n        :param ExtensionId: 订单绑定的扩展ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExtensionId: str\n        :param ResourceReady: 资源初始化结果(仅当ExtensionId不为空时有效): successful(初始化成功), failed(初始化失败), doing(初始化进行中), init(准备初始化)
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceReady: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceType: str\n        :param ResourceMetric: 资源指标名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceMetric: str\n        :param FreeQuota: 资源指标免费量
注意：此字段可能返回 null，表示取不到有效值。\n        :type FreeQuota: int\n        :param MetricUnit: 指标单位
注意：此字段可能返回 null，表示取不到有效值。\n        :type MetricUnit: str\n        :param DeductType: 免费量抵扣周期
<li>sum-month:以月为单位抵扣</li>
<li>sum-day:以天为单位抵扣</li>
<li>totalize:总容量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeductType: str\n        :param FreeQuotaType: 免费量类型
<li>basic:通用量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type FreeQuotaType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlatformStatistic(AbstractModel):
    """终端用户平台统计信息

    """

    def __init__(self):
        """
        :param Platform: 终端用户从属平台
注意：此字段可能返回 null，表示取不到有效值。\n        :type Platform: str\n        :param Count: 平台终端用户数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Count: int\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        """
        self.Platform = None
        self.Count = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Count = params.get("Count")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostPaidEnvDeductInfo(AbstractModel):
    """后付费计费详情

    """

    def __init__(self):
        """
        :param ResourceType: 资源方
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceType: str\n        :param MetricName: 指标名
注意：此字段可能返回 null，表示取不到有效值。\n        :type MetricName: str\n        :param ResQuota: 按量计费详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResQuota: float\n        :param PkgQuota: 资源包抵扣详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgQuota: float\n        :param FreeQuota: 免费额度抵扣详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type FreeQuota: float\n        :param EnvId: 环境id
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvId: str\n        """
        self.ResourceType = None
        self.MetricName = None
        self.ResQuota = None
        self.PkgQuota = None
        self.FreeQuota = None
        self.EnvId = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.MetricName = params.get("MetricName")
        self.ResQuota = params.get("ResQuota")
        self.PkgQuota = params.get("PkgQuota")
        self.FreeQuota = params.get("FreeQuota")
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostpayEnvQuota(AbstractModel):
    """按量付费免费配额信息

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型\n        :type ResourceType: str\n        :param MetricName: 指标名\n        :type MetricName: str\n        :param Value: 配额值\n        :type Value: int\n        :param StartTime: 配额生效时间
为空表示没有时间限制\n        :type StartTime: str\n        :param EndTime: 配额失效时间
为空表示没有时间限制\n        :type EndTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReinstateEnvRequest(AbstractModel):
    """ReinstateEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReinstateEnvResponse(AbstractModel):
    """ReinstateEnv返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceActivityRecordRequest(AbstractModel):
    """ReplaceActivityRecord请求参数结构体

    """

    def __init__(self):
        """
        :param ActivityId: 活动id\n        :type ActivityId: int\n        :param Status: 状态码\n        :type Status: int\n        :param SubStatus: 自定义子状态\n        :type SubStatus: str\n        :param ChannelToken: 鉴权token\n        :type ChannelToken: str\n        :param Channel: 渠道名，不同渠道对应不同secretKey\n        :type Channel: str\n        """
        self.ActivityId = None
        self.Status = None
        self.SubStatus = None
        self.ChannelToken = None
        self.Channel = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.Status = params.get("Status")
        self.SubStatus = params.get("SubStatus")
        self.ChannelToken = params.get("ChannelToken")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceActivityRecordResponse(AbstractModel):
    """ReplaceActivityRecord返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RollUpdateCloudBaseRunServerVersionRequest(AbstractModel):
    """RollUpdateCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param VersionName: 要替换的版本名称，可以为latest\n        :type VersionName: str\n        :param UploadType: 枚举（package/repository/image)\n        :type UploadType: str\n        :param RepositoryType: repository的类型(coding/gitlab/github)\n        :type RepositoryType: str\n        :param FlowRatio: 流量占比\n        :type FlowRatio: int\n        :param DockerfilePath: dockerfile地址\n        :type DockerfilePath: str\n        :param BuildDir: 构建目录\n        :type BuildDir: str\n        :param Cpu: Cpu的大小，单位：核\n        :type Cpu: str\n        :param Mem: Mem的大小，单位：G\n        :type Mem: str\n        :param MinNum: 最小副本数，最小值：0\n        :type MinNum: str\n        :param MaxNum: 最大副本数\n        :type MaxNum: str\n        :param PolicyType: 策略类型\n        :type PolicyType: str\n        :param PolicyThreshold: 策略阈值\n        :type PolicyThreshold: str\n        :param EnvParams: 环境变量\n        :type EnvParams: str\n        :param ContainerPort: 容器端口\n        :type ContainerPort: int\n        :param ServerName: 服务名称\n        :type ServerName: str\n        :param Repository: repository地址\n        :type Repository: str\n        :param Branch: 分支\n        :type Branch: str\n        :param VersionRemark: 版本备注\n        :type VersionRemark: str\n        :param PackageName: 代码包名字\n        :type PackageName: str\n        :param PackageVersion: 代码包版本\n        :type PackageVersion: str\n        :param ImageInfo: Image的详情\n        :type ImageInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageInfo`\n        :param CodeDetail: Github等拉取代码的详情\n        :type CodeDetail: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoDetail`\n        :param IsRebuild: 是否回放流量\n        :type IsRebuild: bool\n        :param InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）\n        :type InitialDelaySeconds: int\n        :param MountVolumeInfo: cfs挂载信息\n        :type MountVolumeInfo: list of CloudBaseRunVolumeMount\n        :param Rollback: 是否回滚\n        :type Rollback: bool\n        :param SnapshotName: 版本历史名\n        :type SnapshotName: str\n        :param CustomLogs: 自定义采集路径\n        :type CustomLogs: str\n        :param EnableUnion: 是否启用统一域名\n        :type EnableUnion: bool\n        :param OperatorRemark: 操作备注\n        :type OperatorRemark: str\n        :param ServerPath: 服务路径（只会第一次生效）\n        :type ServerPath: str\n        :param IsUpdateCls: 是否更新Cls\n        :type IsUpdateCls: bool\n        """
        self.EnvId = None
        self.VersionName = None
        self.UploadType = None
        self.RepositoryType = None
        self.FlowRatio = None
        self.DockerfilePath = None
        self.BuildDir = None
        self.Cpu = None
        self.Mem = None
        self.MinNum = None
        self.MaxNum = None
        self.PolicyType = None
        self.PolicyThreshold = None
        self.EnvParams = None
        self.ContainerPort = None
        self.ServerName = None
        self.Repository = None
        self.Branch = None
        self.VersionRemark = None
        self.PackageName = None
        self.PackageVersion = None
        self.ImageInfo = None
        self.CodeDetail = None
        self.IsRebuild = None
        self.InitialDelaySeconds = None
        self.MountVolumeInfo = None
        self.Rollback = None
        self.SnapshotName = None
        self.CustomLogs = None
        self.EnableUnion = None
        self.OperatorRemark = None
        self.ServerPath = None
        self.IsUpdateCls = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.VersionName = params.get("VersionName")
        self.UploadType = params.get("UploadType")
        self.RepositoryType = params.get("RepositoryType")
        self.FlowRatio = params.get("FlowRatio")
        self.DockerfilePath = params.get("DockerfilePath")
        self.BuildDir = params.get("BuildDir")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.MinNum = params.get("MinNum")
        self.MaxNum = params.get("MaxNum")
        self.PolicyType = params.get("PolicyType")
        self.PolicyThreshold = params.get("PolicyThreshold")
        self.EnvParams = params.get("EnvParams")
        self.ContainerPort = params.get("ContainerPort")
        self.ServerName = params.get("ServerName")
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
        self.IsRebuild = params.get("IsRebuild")
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        if params.get("MountVolumeInfo") is not None:
            self.MountVolumeInfo = []
            for item in params.get("MountVolumeInfo"):
                obj = CloudBaseRunVolumeMount()
                obj._deserialize(item)
                self.MountVolumeInfo.append(obj)
        self.Rollback = params.get("Rollback")
        self.SnapshotName = params.get("SnapshotName")
        self.CustomLogs = params.get("CustomLogs")
        self.EnableUnion = params.get("EnableUnion")
        self.OperatorRemark = params.get("OperatorRemark")
        self.ServerPath = params.get("ServerPath")
        self.IsUpdateCls = params.get("IsUpdateCls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollUpdateCloudBaseRunServerVersionResponse(AbstractModel):
    """RollUpdateCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        """
        :param Result: succ为成功\n        :type Result: str\n        :param VersionName: 滚动更新的VersionName
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionName: str\n        :param RunId: 操作记录id
注意：此字段可能返回 null，表示取不到有效值。\n        :type RunId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.VersionName = None
        self.RunId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.VersionName = params.get("VersionName")
        self.RunId = params.get("RunId")
        self.RequestId = params.get("RequestId")


class SmsFreeQuota(AbstractModel):
    """短信免费量

    """

    def __init__(self):
        """
        :param FreeQuota: 免费量总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type FreeQuota: int\n        :param TotalUsedQuota: 共计已使用总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalUsedQuota: int\n        :param CycleStart: 免费周期起点，0000-00-00 00:00:00 形式
注意：此字段可能返回 null，表示取不到有效值。\n        :type CycleStart: str\n        :param CycleEnd: 免费周期终点，0000-00-00 00:00:00 形式
注意：此字段可能返回 null，表示取不到有效值。\n        :type CycleEnd: str\n        :param TodayUsedQuota: 今天已使用总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TodayUsedQuota: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecialCostItem(AbstractModel):
    """1分钱计费详情

    """

    def __init__(self):
        """
        :param ReportDate: 上报日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReportDate: str\n        :param Uin: 腾讯云uin
注意：此字段可能返回 null，表示取不到有效值。\n        :type Uin: str\n        :param EnvId: 资源id:环境id
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvId: str\n        :param Status: 上报任务状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        """
        self.ReportDate = None
        self.Uin = None
        self.EnvId = None
        self.Status = None


    def _deserialize(self, params):
        self.ReportDate = params.get("ReportDate")
        self.Uin = params.get("Uin")
        self.EnvId = params.get("EnvId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandaloneGatewayInfo(AbstractModel):
    """独立网关信息

    """

    def __init__(self):
        """
        :param GatewayName: 独立网关名称\n        :type GatewayName: str\n        :param CPU: CPU核心数\n        :type CPU: float\n        :param Mem: 内存大小，单位MB\n        :type Mem: int\n        :param PackageVersion: 套餐包版本名称\n        :type PackageVersion: str\n        :param GatewayAlias: 网关别名\n        :type GatewayAlias: str\n        :param VpcId: 私有网络ID\n        :type VpcId: str\n        :param SubnetIds: 子网ID列表\n        :type SubnetIds: list of str\n        :param GatewayDesc: 网关描述\n        :type GatewayDesc: str\n        :param GateWayStatus: 网关状态\n        :type GateWayStatus: str\n        :param ServiceInfo: 服务信息\n        :type ServiceInfo: :class:`tencentcloud.tcb.v20180608.models.BackendServiceInfo`\n        """
        self.GatewayName = None
        self.CPU = None
        self.Mem = None
        self.PackageVersion = None
        self.GatewayAlias = None
        self.VpcId = None
        self.SubnetIds = None
        self.GatewayDesc = None
        self.GateWayStatus = None
        self.ServiceInfo = None


    def _deserialize(self, params):
        self.GatewayName = params.get("GatewayName")
        self.CPU = params.get("CPU")
        self.Mem = params.get("Mem")
        self.PackageVersion = params.get("PackageVersion")
        self.GatewayAlias = params.get("GatewayAlias")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.GatewayDesc = params.get("GatewayDesc")
        self.GateWayStatus = params.get("GateWayStatus")
        if params.get("ServiceInfo") is not None:
            self.ServiceInfo = BackendServiceInfo()
            self.ServiceInfo._deserialize(params.get("ServiceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandaloneGatewayPackageInfo(AbstractModel):
    """小租户网关套餐配置

    """

    def __init__(self):
        """
        :param CPU: CPU核心数\n        :type CPU: float\n        :param Mem: 内存大小，单位MB\n        :type Mem: int\n        :param PackageVersion: 套餐包版本名称\n        :type PackageVersion: str\n        """
        self.CPU = None
        self.Mem = None
        self.PackageVersion = None


    def _deserialize(self, params):
        self.CPU = params.get("CPU")
        self.Mem = params.get("Mem")
        self.PackageVersion = params.get("PackageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaticStorageInfo(AbstractModel):
    """静态CDN资源信息

    """

    def __init__(self):
        """
        :param StaticDomain: 静态CDN域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type StaticDomain: str\n        :param DefaultDirName: 静态CDN默认文件夹，当前为根目录
注意：此字段可能返回 null，表示取不到有效值。\n        :type DefaultDirName: str\n        :param Status: 资源状态(process/online/offline/init)
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Region: cos所属区域
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param Bucket: bucket信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bucket: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageInfo(AbstractModel):
    """StorageInfo 资源信息

    """

    def __init__(self):
        """
        :param Region: 资源所属地域。
当前支持ap-shanghai\n        :type Region: str\n        :param Bucket: 桶名，存储资源的唯一标识\n        :type Bucket: str\n        :param CdnDomain: cdn 域名\n        :type CdnDomain: str\n        :param AppId: 资源所属用户的腾讯云appId\n        :type AppId: str\n        """
        self.Region = None
        self.Bucket = None
        self.CdnDomain = None
        self.AppId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.CdnDomain = params.get("CdnDomain")
        self.AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        """
        :param Key: 标签键\n        :type Key: str\n        :param Value: 标签值\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TurnOffStandaloneGatewayRequest(AbstractModel):
    """TurnOffStandaloneGateway请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param GatewayName: 网关名称\n        :type GatewayName: str\n        :param ServiceNameList: 服务名称列表\n        :type ServiceNameList: list of str\n        """
        self.EnvId = None
        self.GatewayName = None
        self.ServiceNameList = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.GatewayName = params.get("GatewayName")
        self.ServiceNameList = params.get("ServiceNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TurnOffStandaloneGatewayResponse(AbstractModel):
    """TurnOffStandaloneGateway返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 关闭独立网关状态\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class TurnOnStandaloneGatewayRequest(AbstractModel):
    """TurnOnStandaloneGateway请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID\n        :type EnvId: str\n        :param GatewayName: 网关名称\n        :type GatewayName: str\n        :param ServiceNameList: 服务名称列表\n        :type ServiceNameList: list of str\n        """
        self.EnvId = None
        self.GatewayName = None
        self.ServiceNameList = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.GatewayName = params.get("GatewayName")
        self.ServiceNameList = params.get("ServiceNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TurnOnStandaloneGatewayResponse(AbstractModel):
    """TurnOnStandaloneGateway返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 小租户网关开启状态\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")