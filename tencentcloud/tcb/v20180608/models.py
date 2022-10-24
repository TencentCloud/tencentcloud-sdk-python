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


class ActivityInfoItem(AbstractModel):
    """活动信息

    """

    def __init__(self):
        r"""
        :param ActivityId: 活动id
        :type ActivityId: int
        :param CreateTime: 记录插入时间
        :type CreateTime: str
        :param UpdateTime: 记录最后一次变更时间
        :type UpdateTime: str
        :param StartTime: 活动开始时间
        :type StartTime: str
        :param ExpireTime: 活动结束时间
        :type ExpireTime: str
        :param Tag: 自定义备注信息
        :type Tag: str
        """
        self.ActivityId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.StartTime = None
        self.ExpireTime = None
        self.Tag = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.StartTime = params.get("StartTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivityRecordItem(AbstractModel):
    """活动详情

    """

    def __init__(self):
        r"""
        :param Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param ActivityId: 活动id
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityId: int
        :param Status: 自定义状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param SubStatus: 自定义子状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubStatus: str
        :param SubStatusInt: 整型子状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubStatusInt: int
        :param IsDeleted: 是否软删除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDeleted: bool
        """
        self.Uin = None
        self.ActivityId = None
        self.Status = None
        self.SubStatus = None
        self.SubStatusInt = None
        self.IsDeleted = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.ActivityId = params.get("ActivityId")
        self.Status = params.get("Status")
        self.SubStatus = params.get("SubStatus")
        self.SubStatusInt = params.get("SubStatusInt")
        self.IsDeleted = params.get("IsDeleted")
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaasPackageInfo(AbstractModel):
    """新套餐套餐详情

    """

    def __init__(self):
        r"""
        :param PackageName: DAU产品套餐ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param PackageTitle: DAU套餐中文名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageTitle: str
        :param GroupName: 套餐分组
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param GroupTitle: 套餐分组中文名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupTitle: str
        :param BillTags: json格式化计费标签，例如：
{"pid":2, "cids":{"create": 2, "renew": 2, "modify": 2}, "productCode":"p_tcb_mp", "subProductCode":"sp_tcb_mp_cloudbase_dau"}
注意：此字段可能返回 null，表示取不到有效值。
        :type BillTags: str
        :param ResourceLimit: json格式化用户资源限制，例如：
{"Qps":1000,"InvokeNum":{"TimeUnit":"m", "Unit":"万次", "MaxSize": 100},"Capacity":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}, "Cdn":{"Flux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}, "BackFlux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}},"Scf":{"Concurrency":1000,"OutFlux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100},"MemoryUse":{"TimeUnit":"m", "Unit":"WGBS", "MaxSize": 100000}}}
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceLimit: str
        :param AdvanceLimit: json格式化高级限制，例如：
{"CMSEnable":false,"ProvisionedConcurrencyMem":512000, "PictureProcessing":false, "SecurityAudit":false, "RealTimePush":false, "TemplateMessageBatchPush":false, "Payment":false}
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceLimit: str
        :param PackageDescription: 套餐描述
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageDescription: str
        :param IsExternal: 是否对外展示
注意：此字段可能返回 null，表示取不到有效值。
        :type IsExternal: bool
        """
        self.PackageName = None
        self.PackageTitle = None
        self.GroupName = None
        self.GroupTitle = None
        self.BillTags = None
        self.ResourceLimit = None
        self.AdvanceLimit = None
        self.PackageDescription = None
        self.IsExternal = None


    def _deserialize(self, params):
        self.PackageName = params.get("PackageName")
        self.PackageTitle = params.get("PackageTitle")
        self.GroupName = params.get("GroupName")
        self.GroupTitle = params.get("GroupTitle")
        self.BillTags = params.get("BillTags")
        self.ResourceLimit = params.get("ResourceLimit")
        self.AdvanceLimit = params.get("AdvanceLimit")
        self.PackageDescription = params.get("PackageDescription")
        self.IsExternal = params.get("IsExternal")
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
        r"""
        :param ServiceName: 服务名称
        :type ServiceName: str
        :param Status: 服务状态
        :type Status: str
        """
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
        r"""
        :param SubEnvId: 子环境id
        :type SubEnvId: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param BuildPercent: ci部署进度（%）
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildPercent: int
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
        self.BuildPercent = None


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
        self.BuildPercent = params.get("BuildPercent")
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
        r"""
        :param EnableEmptyDirVolume: 启用emptydir数据卷
        :type EnableEmptyDirVolume: bool
        :param Medium: "","Memory","HugePages"
        :type Medium: str
        :param SizeLimit: emptydir数据卷大小
        :type SizeLimit: str
        """
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
        r"""
        :param IsZero: 是否缩容到0
        :type IsZero: bool
        :param Weight: 按百分比灰度的权重
        :type Weight: int
        :param GrayKey: 按请求/header参数的灰度Key
        :type GrayKey: str
        :param GrayValue: 按请求/header参数的灰度Value
        :type GrayValue: str
        :param IsDefault: 是否为默认版本(按请求/header参数)
        :type IsDefault: bool
        :param AccessType: 访问权限，对应二进制分多段，vpc内网｜公网｜oa
        :type AccessType: int
        :param URLs: 访问的URL（域名＋路径）列表
        :type URLs: list of str
        :param EnvId: 环境ID
        :type EnvId: str
        :param ServerName: 服务名称
        :type ServerName: str
        :param VersionName: 版本名称
        :type VersionName: str
        :param GrayType: 灰度类型：FLOW(权重), URL_PARAMS/HEAD_PARAMS
        :type GrayType: str
        :param LbAddr: CLB的IP:Port
        :type LbAddr: str
        :param ConfigType: 0:http访问服务配置信息, 1: 服务域名
        :type ConfigType: int
        """
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
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunKVPriority(AbstractModel):
    """KV参数的优先级

    """

    def __init__(self):
        r"""
        :param Key: 参数的Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 参数的Value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Priority: 优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        """
        self.Key = None
        self.Value = None
        self.Priority = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Priority = params.get("Priority")
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunServerVersionItem(AbstractModel):
    """版本的列表

    """

    def __init__(self):
        r"""
        :param VersionName: 版本名称
        :type VersionName: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param FlowRatio: 流量占比
        :type FlowRatio: int
        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param UpdatedTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        :param BuildId: 构建ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildId: int
        :param UploadType: 构建方式
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadType: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param UrlParam: url中的参数路径
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlParam: :class:`tencentcloud.tcb.v20180608.models.ObjectKV`
        :param Priority: 优先级（数值越小，优先级越高）
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param IsDefaultPriority: 是否是默认兜底版本
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefaultPriority: bool
        :param FlowParams: KV Params
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowParams: list of CloudBaseRunKVPriority
        :param MinReplicas: 最小副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinReplicas: int
        :param MaxReplicas: 最大副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReplicas: int
        :param RunId: 操作记录id
注意：此字段可能返回 null，表示取不到有效值。
        :type RunId: str
        :param Percent: 进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param CurrentReplicas: 当前副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentReplicas: int
        :param Architecture: Monolithic，Microservice
注意：此字段可能返回 null，表示取不到有效值。
        :type Architecture: str
        """
        self.VersionName = None
        self.Status = None
        self.FlowRatio = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.BuildId = None
        self.UploadType = None
        self.Remark = None
        self.UrlParam = None
        self.Priority = None
        self.IsDefaultPriority = None
        self.FlowParams = None
        self.MinReplicas = None
        self.MaxReplicas = None
        self.RunId = None
        self.Percent = None
        self.CurrentReplicas = None
        self.Architecture = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.Status = params.get("Status")
        self.FlowRatio = params.get("FlowRatio")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.BuildId = params.get("BuildId")
        self.UploadType = params.get("UploadType")
        self.Remark = params.get("Remark")
        if params.get("UrlParam") is not None:
            self.UrlParam = ObjectKV()
            self.UrlParam._deserialize(params.get("UrlParam"))
        self.Priority = params.get("Priority")
        self.IsDefaultPriority = params.get("IsDefaultPriority")
        if params.get("FlowParams") is not None:
            self.FlowParams = []
            for item in params.get("FlowParams"):
                obj = CloudBaseRunKVPriority()
                obj._deserialize(item)
                self.FlowParams.append(obj)
        self.MinReplicas = params.get("MinReplicas")
        self.MaxReplicas = params.get("MaxReplicas")
        self.RunId = params.get("RunId")
        self.Percent = params.get("Percent")
        self.CurrentReplicas = params.get("CurrentReplicas")
        self.Architecture = params.get("Architecture")
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
        r"""
        :param Name: Volume 名称
        :type Name: str
        :param MountPath: 挂载路径
        :type MountPath: str
        :param ReadOnly: 是否只读
        :type ReadOnly: bool
        :param SubPath: 子路径
        :type SubPath: str
        :param MountPropagation: 传播挂载方式
        :type MountPropagation: str
        """
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
        r"""
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
        r"""
        :param VersionName: 版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param FlowRatio: 流量占比
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowRatio: int
        :param UrlParam: 流量参数键值对（URL参数/HEADERS参数）
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlParam: :class:`tencentcloud.tcb.v20180608.models.ObjectKV`
        :param Priority: 优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param IsDefaultPriority: 是否是默认兜底版本
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefaultPriority: bool
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param Capabilities: 安全特性
注意：此字段可能返回 null，表示取不到有效值。
        :type Capabilities: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCapabilities`
        """
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
        r"""
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
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param NFS: NFS的挂载方式
注意：此字段可能返回 null，表示取不到有效值。
        :type NFS: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunNfsVolumeSource`
        :param SecretName: secret名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretName: str
        :param EnableEmptyDirVolume: 是否开启临时目录逐步废弃，请使用 EmptyDir
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableEmptyDirVolume: bool
        :param EmptyDir: emptydir数据卷详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EmptyDir: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunEmptyDirVolumeSource`
        """
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
        r"""
        :param ClsRegion: cls所属地域
        :type ClsRegion: str
        :param ClsLogsetId: cls日志集ID
        :type ClsLogsetId: str
        :param ClsTopicId: cls日志主题ID
        :type ClsTopicId: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
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
        r"""
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
        :param ProjectId: coding项目ID，type为coding时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param ProjectName: coding项目
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        """
        self.Type = None
        self.Url = None
        self.Name = None
        self.WorkDir = None
        self.CodingPackageName = None
        self.CodingPackageVersion = None
        self.RawCode = None
        self.Branch = None
        self.ProjectId = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Url = params.get("Url")
        self.Name = params.get("Name")
        self.WorkDir = params.get("WorkDir")
        self.CodingPackageName = params.get("CodingPackageName")
        self.CodingPackageVersion = params.get("CodingPackageVersion")
        self.RawCode = params.get("RawCode")
        self.Branch = params.get("Branch")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
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
        r"""
        :param Service: Service名，需要转发访问的接口名
        :type Service: str
        :param JSONData: 需要转发的云API参数，要转成JSON格式
        :type JSONData: str
        :param ApiRole: 指定角色
        :type ApiRole: str
        """
        self.Service = None
        self.JSONData = None
        self.ApiRole = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.JSONData = params.get("JSONData")
        self.ApiRole = params.get("ApiRole")
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
        r"""
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
        r"""
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
        :param EnvAlias: 环境别名。要以a-z开头，不能包含a-zA-z0-9-以外的字符
        :type EnvAlias: str
        :param RcJson: rc.json的内容
        :type RcJson: str
        :param AddonConfig: 插件配置内容
        :type AddonConfig: str
        :param Tags: 标签
        :type Tags: list of str
        :param NetworkConfig: 网络配置
        :type NetworkConfig: str
        :param FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param UploadType: 枚举（package/repository/image/jar/war)
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
        :param IsCreateJnsGw: 是否创建JnsGw 0未传默认创建 1创建 2不创建
        :type IsCreateJnsGw: int
        :param ServiceVolumeMounts: 数据卷挂载参数
        :type ServiceVolumeMounts: list of CloudBaseRunServiceVolumeMount
        :param HasDockerfile: 是否有Dockerfile：0-default has, 1-has, 2-has not
        :type HasDockerfile: int
        :param BaseImage: 基础镜像
        :type BaseImage: str
        :param EntryPoint: 容器启动入口命令
        :type EntryPoint: str
        :param RepoLanguage: 仓库语言
        :type RepoLanguage: str
        :param UploadFilename: 用户实际上传文件名（仅UploadType为jar/war时必填）
        :type UploadFilename: str
        :param PolicyDetail: 自动扩缩容策略组
        :type PolicyDetail: list of HpaPolicy
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
        self.IsCreateJnsGw = None
        self.ServiceVolumeMounts = None
        self.HasDockerfile = None
        self.BaseImage = None
        self.EntryPoint = None
        self.RepoLanguage = None
        self.UploadFilename = None
        self.PolicyDetail = None


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
        self.HasDockerfile = params.get("HasDockerfile")
        self.BaseImage = params.get("BaseImage")
        self.EntryPoint = params.get("EntryPoint")
        self.RepoLanguage = params.get("RepoLanguage")
        self.UploadFilename = params.get("UploadFilename")
        if params.get("PolicyDetail") is not None:
            self.PolicyDetail = []
            for item in params.get("PolicyDetail"):
                obj = HpaPolicy()
                obj._deserialize(item)
                self.PolicyDetail.append(obj)
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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


class CreateStandaloneGatewayRequest(AbstractModel):
    """CreateStandaloneGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param GatewayAlias: 网关名
        :type GatewayAlias: str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetIds: 子网ID
        :type SubnetIds: list of str
        :param GatewayDesc: 网关描述
        :type GatewayDesc: str
        :param PackageVersion: 网关套餐版本
        :type PackageVersion: str
        """
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
        r"""
        :param GatewayName: 网关名称
        :type GatewayName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GatewayName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GatewayName = params.get("GatewayName")
        self.RequestId = params.get("RequestId")


class CreateStaticStoreRequest(AbstractModel):
    """CreateStaticStore请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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


class CreateWxCloudBaseRunEnvRequest(AbstractModel):
    """CreateWxCloudBaseRunEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param WxAppId: wx应用Id
        :type WxAppId: str
        :param Alias: 环境别名，要以a-z开头，不能包含 a-z,0-9,- 以外的字符
        :type Alias: str
        :param FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。
        :type FreeQuota: str
        :param Flag: 订单标记。建议使用方统一转大小写之后再判断。
QuickStart：快速启动来源
Activity：活动来源
        :type Flag: str
        :param VpcId: 私有网络Id
        :type VpcId: str
        :param SubNetIds: 子网列表
        :type SubNetIds: list of str
        :param IsOpenCloudInvoke: 是否打开云调用
        :type IsOpenCloudInvoke: bool
        """
        self.WxAppId = None
        self.Alias = None
        self.FreeQuota = None
        self.Flag = None
        self.VpcId = None
        self.SubNetIds = None
        self.IsOpenCloudInvoke = None


    def _deserialize(self, params):
        self.WxAppId = params.get("WxAppId")
        self.Alias = params.get("Alias")
        self.FreeQuota = params.get("FreeQuota")
        self.Flag = params.get("Flag")
        self.VpcId = params.get("VpcId")
        self.SubNetIds = params.get("SubNetIds")
        self.IsOpenCloudInvoke = params.get("IsOpenCloudInvoke")
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
        r"""
        :param EnvId: 环境Id
        :type EnvId: str
        :param TranId: 后付费订单号
        :type TranId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param AccountPassword: 账户密码
        :type AccountPassword: str
        :param EnvId: 环境ID
        :type EnvId: str
        :param WxAppId: 微信appid
        :type WxAppId: str
        :param DbVersion: mysql内核版本，支持5.7,8.0
        :type DbVersion: str
        :param LowerCaseTableName: 0: 非大小写敏感
1: 大小写敏感
默认 0
        :type LowerCaseTableName: str
        """
        self.AccountPassword = None
        self.EnvId = None
        self.WxAppId = None
        self.DbVersion = None
        self.LowerCaseTableName = None


    def _deserialize(self, params):
        self.AccountPassword = params.get("AccountPassword")
        self.EnvId = params.get("EnvId")
        self.WxAppId = params.get("WxAppId")
        self.DbVersion = params.get("DbVersion")
        self.LowerCaseTableName = params.get("LowerCaseTableName")
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DatabasesInfo(AbstractModel):
    """数据库资源信息

    """

    def __init__(self):
        r"""
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
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.InstanceId = None
        self.Status = None
        self.Region = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")
        self.Region = params.get("Region")
        self.UpdateTime = params.get("UpdateTime")
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
        r"""
        :param EnvId: 环境id
        :type EnvId: str
        :param ProjectName: 项目名
        :type ProjectName: str
        :param KeepResource: 是否保留资源
        :type KeepResource: bool
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCloudBaseRunServerVersionRequest(AbstractModel):
    """DeleteCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param ServerName: 服务名称
        :type ServerName: str
        :param VersionName: 版本名称
        :type VersionName: str
        :param IsDeleteServer: 是否删除服务，只有最后一个版本的时候，才生效。
        :type IsDeleteServer: bool
        :param IsDeleteImage: 只有删除服务的时候，才会起作用
        :type IsDeleteImage: bool
        :param OperatorRemark: 操作备注
        :type OperatorRemark: str
        """
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
        r"""
        :param Result: 返回结果，succ为成功
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


class DeleteEndUserRequest(AbstractModel):
    """DeleteEndUser请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeActivityInfoRequest(AbstractModel):
    """DescribeActivityInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ActivityIdList: 活动id列表
        :type ActivityIdList: list of int
        """
        self.ActivityIdList = None


    def _deserialize(self, params):
        self.ActivityIdList = params.get("ActivityIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActivityInfoResponse(AbstractModel):
    """DescribeActivityInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ActivityInfoList: 活动详情
        :type ActivityInfoList: list of ActivityInfoItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ActivityInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ActivityInfoList") is not None:
            self.ActivityInfoList = []
            for item in params.get("ActivityInfoList"):
                obj = ActivityInfoItem()
                obj._deserialize(item)
                self.ActivityInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeActivityRecordRequest(AbstractModel):
    """DescribeActivityRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelToken: 渠道加密token
        :type ChannelToken: str
        :param Channel: 渠道来源，每个来源对应不同secretKey
        :type Channel: str
        :param ActivityIdList: 活动id列表
        :type ActivityIdList: list of int
        :param Status: 过滤状态码，已废弃
        :type Status: int
        :param Statuses: 状态码过滤数组，空数组时不过滤
        :type Statuses: list of int
        :param IsDeletedList: 根据是否软删除进行过滤，[0]未删除, [1] 删除，不传不过滤
        :type IsDeletedList: list of int
        """
        self.ChannelToken = None
        self.Channel = None
        self.ActivityIdList = None
        self.Status = None
        self.Statuses = None
        self.IsDeletedList = None


    def _deserialize(self, params):
        self.ChannelToken = params.get("ChannelToken")
        self.Channel = params.get("Channel")
        self.ActivityIdList = params.get("ActivityIdList")
        self.Status = params.get("Status")
        self.Statuses = params.get("Statuses")
        self.IsDeletedList = params.get("IsDeletedList")
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
        r"""
        :param ActivityRecords: 活动记录详情
        :type ActivityRecords: list of ActivityRecordItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        """
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
        r"""
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


class DescribeBaasPackageListRequest(AbstractModel):
    """DescribeBaasPackageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PackageName: tcb产品套餐ID，不填拉取全量package信息。
        :type PackageName: str
        :param EnvId: 环境ID
        :type EnvId: str
        :param Source: 套餐归属方，填写后只返回对应的套餐 包含miniapp与qcloud两种 默认为miniapp
        :type Source: str
        :param EnvChannel: 套餐归属环境渠道
        :type EnvChannel: str
        :param TargetAction: 拉取套餐用途：
1）new 新购
2）modify变配
3）renew续费
        :type TargetAction: str
        :param GroupName: 预留字段，同一商品会对应多个类型套餐，对指标有不同侧重。
计算型calculation
流量型flux
容量型capactiy
        :type GroupName: str
        :param PackageTypeList: 类型分组过滤。默认为["default"]
        :type PackageTypeList: list of str
        :param PaymentChannel: 付费渠道，与回包billTags中的计费参数相关，不填返回默认值。
        :type PaymentChannel: str
        """
        self.PackageName = None
        self.EnvId = None
        self.Source = None
        self.EnvChannel = None
        self.TargetAction = None
        self.GroupName = None
        self.PackageTypeList = None
        self.PaymentChannel = None


    def _deserialize(self, params):
        self.PackageName = params.get("PackageName")
        self.EnvId = params.get("EnvId")
        self.Source = params.get("Source")
        self.EnvChannel = params.get("EnvChannel")
        self.TargetAction = params.get("TargetAction")
        self.GroupName = params.get("GroupName")
        self.PackageTypeList = params.get("PackageTypeList")
        self.PaymentChannel = params.get("PaymentChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaasPackageListResponse(AbstractModel):
    """DescribeBaasPackageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param PackageList: 套餐列表
        :type PackageList: list of BaasPackageInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PackageList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PackageList") is not None:
            self.PackageList = []
            for item in params.get("PackageList"):
                obj = BaasPackageInfo()
                obj._deserialize(item)
                self.PackageList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseBuildServiceRequest(AbstractModel):
    """DescribeCloudBaseBuildService请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境id
        :type EnvId: str
        :param ServiceName: 服务名
        :type ServiceName: str
        :param CIBusiness: build类型,枚举值有: cloudbaserun, framework-ci
        :type CIBusiness: str
        :param ServiceVersion: 服务版本
        :type ServiceVersion: str
        :param Suffix: 文件后缀
        :type Suffix: str
        """
        self.EnvId = None
        self.ServiceName = None
        self.CIBusiness = None
        self.ServiceVersion = None
        self.Suffix = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServiceName = params.get("ServiceName")
        self.CIBusiness = params.get("CIBusiness")
        self.ServiceVersion = params.get("ServiceVersion")
        self.Suffix = params.get("Suffix")
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
        r"""
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
        r"""
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
        :param CiId: ci的id
        :type CiId: str
        """
        self.Offset = None
        self.PageSize = None
        self.EnvId = None
        self.ProjectName = None
        self.ProjectType = None
        self.Tags = None
        self.CiId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.PageSize = params.get("PageSize")
        self.EnvId = params.get("EnvId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectType = params.get("ProjectType")
        self.Tags = params.get("Tags")
        self.CiId = params.get("CiId")
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
        r"""
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
        r"""
        :param EnvId: 环境id
        :type EnvId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param PageSize: 页大小
        :type PageSize: int
        :param PageNum: 第几页,从0开始
        :type PageNum: int
        :param StartTime: 起始时间 2021-03-27 12:00:00
        :type StartTime: str
        :param EndTime: 终止时间 2021-03-27 12:00:00
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
        r"""
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


class DescribeCloudBaseRunAllVpcsRequest(AbstractModel):
    """DescribeCloudBaseRunAllVpcs请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunAllVpcsResponse(AbstractModel):
    """DescribeCloudBaseRunAllVpcs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Vpcs: 所有vpcid
注意：此字段可能返回 null，表示取不到有效值。
        :type Vpcs: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Vpcs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Vpcs = params.get("Vpcs")
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunConfForGateWayRequest(AbstractModel):
    """DescribeCloudBaseRunConfForGateWay请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvID: 环境ID
        :type EnvID: str
        :param VpcID: vpc信息
        :type VpcID: str
        """
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
        r"""
        :param LastUpTime: 最近更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpTime: str
        :param Data: 配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CloudBaseRunForGatewayConf
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeCloudBaseRunOneClickTaskExternalRequest(AbstractModel):
    """DescribeCloudBaseRunOneClickTaskExternal请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExternalId: 外部任务Id 最长64字节
        :type ExternalId: str
        """
        self.ExternalId = None


    def _deserialize(self, params):
        self.ExternalId = params.get("ExternalId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunOneClickTaskExternalResponse(AbstractModel):
    """DescribeCloudBaseRunOneClickTaskExternal返回参数结构体

    """

    def __init__(self):
        r"""
        :param ExternalId: 外部任务Id
        :type ExternalId: str
        :param EnvId: 弃用
        :type EnvId: str
        :param UserUin: 用户uin
        :type UserUin: str
        :param ServerName: 服务名
        :type ServerName: str
        :param VersionName: 版本名
        :type VersionName: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Stage: 当前阶段
微信云托管环境创建阶段：envStage
存储资源创建阶段：storageStage
服务创建阶段：serverStage
        :type Stage: str
        :param Status: 状态
running
stopped
failed
finished
        :type Status: str
        :param FailReason: 失败原因
        :type FailReason: str
        :param UserEnvId: 用户envId
        :type UserEnvId: str
        :param StartTime: 创建时间
        :type StartTime: str
        :param Steps: 步骤信息
        :type Steps: list of OneClickTaskStepInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ExternalId = None
        self.EnvId = None
        self.UserUin = None
        self.ServerName = None
        self.VersionName = None
        self.CreateTime = None
        self.Stage = None
        self.Status = None
        self.FailReason = None
        self.UserEnvId = None
        self.StartTime = None
        self.Steps = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExternalId = params.get("ExternalId")
        self.EnvId = params.get("EnvId")
        self.UserUin = params.get("UserUin")
        self.ServerName = params.get("ServerName")
        self.VersionName = params.get("VersionName")
        self.CreateTime = params.get("CreateTime")
        self.Stage = params.get("Stage")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        self.UserEnvId = params.get("UserEnvId")
        self.StartTime = params.get("StartTime")
        if params.get("Steps") is not None:
            self.Steps = []
            for item in params.get("Steps"):
                obj = OneClickTaskStepInfo()
                obj._deserialize(item)
                self.Steps.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunOperationTypesRequest(AbstractModel):
    """DescribeCloudBaseRunOperationTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param ServerName: 服务名称，精确匹配
        :type ServerName: str
        """
        self.EnvId = None
        self.ServerName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunOperationTypesResponse(AbstractModel):
    """DescribeCloudBaseRunOperationTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param Action: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: list of str
        :param ServerName: 服务名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Action = None
        self.ServerName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.ServerName = params.get("ServerName")
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunPodListRequest(AbstractModel):
    """DescribeCloudBaseRunPodList请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境id
        :type EnvId: str
        :param ServerName: 服务名
        :type ServerName: str
        :param VersionName: 版本名
        :type VersionName: str
        :param Limit: 分页限制
        :type Limit: int
        :param Offset: 分页偏移量
        :type Offset: int
        :param Status: 容器状态
        :type Status: str
        :param PodName: 容器名
        :type PodName: str
        """
        self.EnvId = None
        self.ServerName = None
        self.VersionName = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.PodName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.VersionName = params.get("VersionName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunPodListResponse(AbstractModel):
    """DescribeCloudBaseRunPodList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunResourceForExtendRequest(AbstractModel):
    """DescribeCloudBaseRunResourceForExtend请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        """
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
        r"""
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
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        """
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
        r"""
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


class DescribeCloudBaseRunServerDomainNameRequest(AbstractModel):
    """DescribeCloudBaseRunServerDomainName请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServerName: 服务名
        :type ServerName: str
        :param UserEnvId: 环境Id
        :type UserEnvId: str
        :param UserUin: 用户Uin
        :type UserUin: str
        :param ExternalId: 外部Id
        :type ExternalId: str
        """
        self.ServerName = None
        self.UserEnvId = None
        self.UserUin = None
        self.ExternalId = None


    def _deserialize(self, params):
        self.ServerName = params.get("ServerName")
        self.UserEnvId = params.get("UserEnvId")
        self.UserUin = params.get("UserUin")
        self.ExternalId = params.get("ExternalId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunServerDomainNameResponse(AbstractModel):
    """DescribeCloudBaseRunServerDomainName返回参数结构体

    """

    def __init__(self):
        r"""
        :param PublicDomain: 公网服务域名
        :type PublicDomain: str
        :param InternalDomain: 内部服务域名
        :type InternalDomain: str
        :param DomainName: 弃用
        :type DomainName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PublicDomain = None
        self.InternalDomain = None
        self.DomainName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PublicDomain = params.get("PublicDomain")
        self.InternalDomain = params.get("InternalDomain")
        self.DomainName = params.get("DomainName")
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunServerRequest(AbstractModel):
    """DescribeCloudBaseRunServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param ServerName: 服务名称
        :type ServerName: str
        :param Offset: 分页偏移
        :type Offset: int
        :param Limit: 分页数量
        :type Limit: int
        :param VersionName: 版本名字（精确匹配）
        :type VersionName: str
        """
        self.EnvId = None
        self.ServerName = None
        self.Offset = None
        self.Limit = None
        self.VersionName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunServerResponse(AbstractModel):
    """DescribeCloudBaseRunServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param VersionItems: 版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionItems: list of CloudBaseRunServerVersionItem
        :param ServerName: 服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param IsPublic: 是否对于外网开放
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublic: bool
        :param ImageRepo: 镜像仓库
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageRepo: str
        :param TrafficType: 流量配置的类型（FLOW,URL_PARAMS)
注意：此字段可能返回 null，表示取不到有效值。
        :type TrafficType: str
        :param SourceType: 服务创建类型，默认为空，一键部署为oneclick
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VersionItems = None
        self.ServerName = None
        self.IsPublic = None
        self.ImageRepo = None
        self.TrafficType = None
        self.SourceType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VersionItems") is not None:
            self.VersionItems = []
            for item in params.get("VersionItems"):
                obj = CloudBaseRunServerVersionItem()
                obj._deserialize(item)
                self.VersionItems.append(obj)
        self.ServerName = params.get("ServerName")
        self.IsPublic = params.get("IsPublic")
        self.ImageRepo = params.get("ImageRepo")
        self.TrafficType = params.get("TrafficType")
        self.SourceType = params.get("SourceType")
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunServerVersionRequest(AbstractModel):
    """DescribeCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        :param RepoType: Repo的类型(gitlab/github/coding)
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
        :param HasDockerfile: 是否有Dockerfile：0-default has, 1-has, 2-has not
注意：此字段可能返回 null，表示取不到有效值。
        :type HasDockerfile: int
        :param BaseImage: 基础镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseImage: str
        :param EntryPoint: 容器启动入口命令
注意：此字段可能返回 null，表示取不到有效值。
        :type EntryPoint: str
        :param RepoLanguage: 仓库语言
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoLanguage: str
        :param PolicyDetail: 自动扩缩容策略组
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDetail: list of HpaPolicy
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
        self.HasDockerfile = None
        self.BaseImage = None
        self.EntryPoint = None
        self.RepoLanguage = None
        self.PolicyDetail = None
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
        self.HasDockerfile = params.get("HasDockerfile")
        self.BaseImage = params.get("BaseImage")
        self.EntryPoint = params.get("EntryPoint")
        self.RepoLanguage = params.get("RepoLanguage")
        if params.get("PolicyDetail") is not None:
            self.PolicyDetail = []
            for item in params.get("PolicyDetail"):
                obj = HpaPolicy()
                obj._deserialize(item)
                self.PolicyDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunVersionRequest(AbstractModel):
    """DescribeCloudBaseRunVersion请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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


class DescribeCloudBaseRunVersionRsByConditionRequest(AbstractModel):
    """DescribeCloudBaseRunVersionRsByCondition请求参数结构体

    """


class DescribeCloudBaseRunVersionRsByConditionResponse(AbstractModel):
    """DescribeCloudBaseRunVersionRsByCondition返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCloudBaseRunVersionSnapshotRequest(AbstractModel):
    """DescribeCloudBaseRunVersionSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServerName: 服务名
        :type ServerName: str
        :param VersionName: 版本名
        :type VersionName: str
        :param EnvId: 环境id
        :type EnvId: str
        :param SnapshotName: 版本历史名
        :type SnapshotName: str
        :param Offset: 偏移量。默认0
        :type Offset: int
        :param Limit: 限制大小。默认10，最大20
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
        r"""
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


class DescribeCurveDataRequest(AbstractModel):
    """DescribeCurveData请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param MetricName: <li> 指标名: </li>
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
<li> TkeInvokeNum: 调用量 </li>
        :type MetricName: str
        :param StartTime: 开始时间，如2018-08-24 10:50:00, 开始时间需要早于结束时间至少五分钟(原因是因为目前统计粒度最小是5分钟).
        :type StartTime: str
        :param EndTime: 结束时间，如2018-08-24 10:50:00, 结束时间需要晚于开始时间至少五分钟(原因是因为目前统计粒度最小是5分钟)..
        :type EndTime: str
        :param ResourceID: 资源ID, 目前仅对云函数、容器托管相关的指标有意义。云函数(FunctionInvocation, FunctionGBs, FunctionFlux, FunctionError, FunctionDuration)、容器托管（服务名称）, 如果想查询某个云函数的指标则在ResourceId中传入函数名; 如果只想查询整个namespace的指标, 则留空或不传.如果想查询数据库某个集合相关信息，传入集合名称
        :type ResourceID: str
        """
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
        r"""
        :param StartTime: 开始时间, 会根据数据的统计周期进行取整.
        :type StartTime: str
        :param EndTime: 结束时间, 会根据数据的统计周期进行取整.
        :type EndTime: str
        :param MetricName: 指标名.
        :type MetricName: str
        :param Period: 统计周期(单位秒), 当时间区间为1天内, 统计周期为5分钟; 当时间区间选择为1天以上, 15天以下, 统计周期为1小时; 当时间区间选择为15天以上, 180天以下, 统计周期为1天.
        :type Period: int
        :param Values: 有效的监控数据, 每个有效监控数据的上报时间可以从时间数组中的对应位置上获取到.
        :type Values: list of int
        :param Time: 时间数据, 标识监控数据Values中的点是哪个时间段上报的.
        :type Time: list of int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
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
        r"""
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
        r"""
        :param CodeUri: 代码uri，格式如：extension://abcdefhhxxx.zip，对应 DescribeExtensionUploadInfo 接口的返回值
        :type CodeUri: str
        """
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
        r"""
        :param FilePath: 文件路径，该字段已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        :param CustomKey: 加密key，用于计算下载加密文件的header。参考SSE-C https://cloud.tencent.com/document/product/436/7728#sse-c
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
        r"""
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
        r"""
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
        r"""
        :param EnvId: 环境id
        :type EnvId: str
        """
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
        r"""
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
        r"""
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
        r"""
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


class DescribeEnvDealRegionRequest(AbstractModel):
    """DescribeEnvDealRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param DealType: 订单类型：
ENV_PREPAY_MINIAPP= 预付费环境(微信小程序)
ENV_PREPAY_CLOUD= 预付费环境(腾讯云)
ENV_POSTPAY = 后付费环境
HOSTING_PREPAY = 预付费静态托管
PACKAGE=套餐包
        :type DealType: str
        :param DealAction: 下单类型：
CREATE = 新购
RENEW = 续费
MODIFY = 套餐调整(升级/降级)
REFUND = 退费
        :type DealAction: str
        :param DealRegion: 下单地域：
ap-guangzhou = 广州地域
ap-shanghai = 上海地域
ap-beijing = 北京地域
        :type DealRegion: str
        """
        self.EnvId = None
        self.DealType = None
        self.DealAction = None
        self.DealRegion = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.DealType = params.get("DealType")
        self.DealAction = params.get("DealAction")
        self.DealRegion = params.get("DealRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvDealRegionResponse(AbstractModel):
    """DescribeEnvDealRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param Region: 下单region
        :type Region: str
        :param Zone: 下单zone
        :type Zone: str
        :param RegionId: 下单regionId
        :type RegionId: int
        :param ZoneId: 下单zoneId
        :type ZoneId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Region = None
        self.Zone = None
        self.RegionId = None
        self.ZoneId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.RequestId = params.get("RequestId")


class DescribeEnvFreeQuotaRequest(AbstractModel):
    """DescribeEnvFreeQuota请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        :param MaxFreeTrialNum: 微信网关体验版可购买月份数
        :type MaxFreeTrialNum: int
        :param CurrentFreeTrialNum: 微信网关体验版已购买月份数
        :type CurrentFreeTrialNum: int
        :param ChangePayTotal: 转支付限额总数
        :type ChangePayTotal: int
        :param CurrentChangePayTotal: 当前已用转支付次数
        :type CurrentChangePayTotal: int
        :param ChangePayMonthly: 转支付每月限额
        :type ChangePayMonthly: int
        :param CurrentChangePayMonthly: 本月已用转支付额度
        :type CurrentChangePayMonthly: int
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
        r"""
        :param ResourceTypes: 资源方列表
        :type ResourceTypes: list of str
        :param EnvId: 环境id
        :type EnvId: str
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        """
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
        r"""
        :param PostPaidEnvDeductInfoList: 指标抵扣详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PostPaidEnvDeductInfoList: list of PostPaidEnvDeductInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param EnvId: 已购买增值包的环境ID
        :type EnvId: str
        """
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
        r"""
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


class DescribeHostingDomainTaskRequest(AbstractModel):
    """DescribeHostingDomainTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        """
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
        r"""
        :param Status: todo/doing/done/error
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribePostpayFreeQuotasRequest(AbstractModel):
    """DescribePostpayFreeQuotas请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        """
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
        r"""
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


class DescribeSpecialCostItemsRequest(AbstractModel):
    """DescribeSpecialCostItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境id
        :type EnvId: str
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        """
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
        r"""
        :param SpecialCostItems: 1分钱抵扣详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialCostItems: list of SpecialCostItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param PackageVersion: 套餐版本，包含starter、basic、advanced、enterprise
        :type PackageVersion: str
        """
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
        r"""
        :param Total: 总数
        :type Total: int
        :param StandaloneGatewayPackageList: 套餐详情
        :type StandaloneGatewayPackageList: list of StandaloneGatewayPackageInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param GatewayName: 网关名称
        :type GatewayName: str
        :param GatewayAlias: 网关别名
        :type GatewayAlias: str
        """
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
        r"""
        :param StandaloneGatewayList: 独立网关信息列表
        :type StandaloneGatewayList: list of StandaloneGatewayInfo
        :param Total: 总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeUserActivityInfoRequest(AbstractModel):
    """DescribeUserActivityInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ActivityId: 活动id
        :type ActivityId: int
        :param ChannelToken: 渠道加密token
        :type ChannelToken: str
        :param Channel: 渠道来源，每个来源对应不同secretKey
        :type Channel: str
        :param GroupId: 团id, 1元钱裂变中活动团id不为空时根据团id来查询记录，为空时查询uin最新记录
        :type GroupId: str
        """
        self.ActivityId = None
        self.ChannelToken = None
        self.Channel = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.ChannelToken = params.get("ChannelToken")
        self.Channel = params.get("Channel")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserActivityInfoResponse(AbstractModel):
    """DescribeUserActivityInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Tag: 自定义标记，1元钱裂变需求中即代指`团id`
        :type Tag: str
        :param Notes: 自定义备注，1元钱裂变需求中返回`团列表`，uin列表通过","拼接
        :type Notes: str
        :param ActivityTimeLeft: 活动剩余时间，单位为s.1元钱裂变需求中即为 time(活动过期时间)-Now()), 过期后为0，即返回必为自然数
        :type ActivityTimeLeft: int
        :param GroupTimeLeft: 拼团剩余时间，单位为s.1元钱裂变需求中即为time(成团时间)+24H-Now()，过期后为0，即返回必为自然数
        :type GroupTimeLeft: int
        :param NickNameList: 昵称列表,通过","拼接， 1元钱裂变活动中与Notes中uin一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type NickNameList: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Tag = None
        self.Notes = None
        self.ActivityTimeLeft = None
        self.GroupTimeLeft = None
        self.NickNameList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Notes = params.get("Notes")
        self.ActivityTimeLeft = params.get("ActivityTimeLeft")
        self.GroupTimeLeft = params.get("GroupTimeLeft")
        self.NickNameList = params.get("NickNameList")
        self.RequestId = params.get("RequestId")


class DescribeWxCloudBaseRunEnvsRequest(AbstractModel):
    """DescribeWxCloudBaseRunEnvs请求参数结构体

    """

    def __init__(self):
        r"""
        :param WxAppId: wx应用Id
        :type WxAppId: str
        :param AllRegions: 是否查询全地域
        :type AllRegions: bool
        """
        self.WxAppId = None
        self.AllRegions = None


    def _deserialize(self, params):
        self.WxAppId = params.get("WxAppId")
        self.AllRegions = params.get("AllRegions")
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
        r"""
        :param EnvList: env列表
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


class DescribeWxCloudBaseRunSubNetsRequest(AbstractModel):
    """DescribeWxCloudBaseRunSubNets请求参数结构体

    """

    def __init__(self):
        r"""
        :param VpcId: VPC id
        :type VpcId: str
        :param Limit: 查询个数限制，不填或小于等于0，等于不限制
        :type Limit: int
        """
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
        r"""
        :param SubNetIds: 子网Id列表
        :type SubNetIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubNetIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubNetIds = params.get("SubNetIds")
        self.RequestId = params.get("RequestId")


class DestroyEnvRequest(AbstractModel):
    """DestroyEnv请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DestroyStandaloneGatewayRequest(AbstractModel):
    """DestroyStandaloneGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param GatewayName: 网名名称
        :type GatewayName: str
        :param IsForce: 是否强制释放
        :type IsForce: bool
        """
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
        r"""
        :param Status: 删除独立网关状态
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DestroyStaticStoreRequest(AbstractModel):
    """DestroyStaticStore请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param EnableOverrun: 是否开启 `超过套餐额度部分转按量付费`
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableOverrun: bool
        :param ExtPackageType: 环境套餐类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtPackageType: str
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
        self.EnableOverrun = None
        self.ExtPackageType = None


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
        self.EnableOverrun = params.get("EnableOverrun")
        self.ExtPackageType = params.get("ExtPackageType")
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
        r"""
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
        :param Tags: 环境标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param CustomLogServices: 自定义日志服务
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLogServices: list of ClsInfo
        :param EnvType: 环境类型：baas, run, hoting, weda
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvType: str
        :param IsDauPackage: 是否是dau新套餐
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDauPackage: bool
        :param PackageType: 套餐类型:空\baas\tcbr
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
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
        self.Tags = None
        self.CustomLogServices = None
        self.EnvType = None
        self.IsDauPackage = None
        self.PackageType = None


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
        self.EnvType = params.get("EnvType")
        self.IsDauPackage = params.get("IsDauPackage")
        self.PackageType = params.get("PackageType")
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
        r"""
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
        :param OpenAccessTypes: OA PUBLIC MINIAPP VPC
        :type OpenAccessTypes: list of str
        :param IsCreatePath: 是否创建Path 0未传默认创建 1创建 2不创建
        :type IsCreatePath: int
        :param ServerPath: 指定创建路径（如不存在，则创建。存在，则忽略）
        :type ServerPath: str
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreezeCloudBaseRunServersRequest(AbstractModel):
    """FreezeCloudBaseRunServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param ServerNameList: 服务名列表
        :type ServerNameList: list of str
        """
        self.EnvId = None
        self.ServerNameList = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerNameList = params.get("ServerNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreezeCloudBaseRunServersResponse(AbstractModel):
    """FreezeCloudBaseRunServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 批量状态状态
成功：succ
失败：fail
部分：partial（部分成功、部分失败）
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param FailServerList: 冻结失败服务列表
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailServerList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.FailServerList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.FailServerList = params.get("FailServerList")
        self.RequestId = params.get("RequestId")


class FunctionInfo(AbstractModel):
    """函数的信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HpaPolicy(AbstractModel):
    """扩缩容策略

    """

    def __init__(self):
        r"""
        :param PolicyType: 策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param PolicyThreshold: 策略阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyThreshold: int
        """
        self.PolicyType = None
        self.PolicyThreshold = None


    def _deserialize(self, params):
        self.PolicyType = params.get("PolicyType")
        self.PolicyThreshold = params.get("PolicyThreshold")
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogObject(AbstractModel):
    """CLS日志单条信息

    """

    def __init__(self):
        r"""
        :param TopicId: 日志属于的 topic ID
        :type TopicId: str
        :param TopicName: 日志主题的名字
        :type TopicName: str
        :param Timestamp: 日志时间
        :type Timestamp: str
        :param Content: 日志内容
        :type Content: str
        :param FileName: 采集路径
        :type FileName: str
        :param Source: 日志来源设备
        :type Source: str
        """
        self.TopicId = None
        self.TopicName = None
        self.Timestamp = None
        self.Content = None
        self.FileName = None
        self.Source = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Timestamp = params.get("Timestamp")
        self.Content = params.get("Content")
        self.FileName = params.get("FileName")
        self.Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogResObject(AbstractModel):
    """CLS日志结果

    """

    def __init__(self):
        r"""
        :param Context: 获取更多检索结果的游标
        :type Context: str
        :param ListOver: 搜索结果是否已经全部返回
        :type ListOver: bool
        :param Results: 日志内容信息
        :type Results: list of LogObject
        """
        self.Context = None
        self.ListOver = None
        self.Results = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.ListOver = params.get("ListOver")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = LogObject()
                obj._deserialize(item)
                self.Results.append(obj)
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
        r"""
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
        :param Period: topic保存时长 默认7天
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        """
        self.LogsetName = None
        self.LogsetId = None
        self.TopicName = None
        self.TopicId = None
        self.Region = None
        self.Period = None


    def _deserialize(self, params):
        self.LogsetName = params.get("LogsetName")
        self.LogsetId = params.get("LogsetId")
        self.TopicName = params.get("TopicName")
        self.TopicId = params.get("TopicId")
        self.Region = params.get("Region")
        self.Period = params.get("Period")
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
        r"""
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
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param ServerName: 服务名称
        :type ServerName: str
        :param VersionFlowItems: 流量占比
        :type VersionFlowItems: list of CloudBaseRunVersionFlowItem
        :param TrafficType: 流量类型（URL_PARAMS / FLOW / HEADERS)
        :type TrafficType: str
        :param OperatorRemark: 操作备注
        :type OperatorRemark: str
        """
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
        r"""
        :param Result: 返回结果，succ代表成功
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


class ModifyCloudBaseRunServerVersionRequest(AbstractModel):
    """ModifyCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param ServerName: 服务名称
        :type ServerName: str
        :param VersionName: 版本名称
        :type VersionName: str
        :param EnvParams: 环境变量
        :type EnvParams: str
        :param MinNum: 最小副本数
        :type MinNum: str
        :param MaxNum: 最大副本数
        :type MaxNum: str
        :param ContainerPort: 端口
        :type ContainerPort: str
        :param Remark: 备注
        :type Remark: str
        :param CustomLogs: 日志采集路径
        :type CustomLogs: str
        :param IsResetRemark: 是否重设备注
        :type IsResetRemark: bool
        :param BasicModify: 修改基础信息
        :type BasicModify: bool
        :param OperatorRemark: 操作备注
        :type OperatorRemark: str
        """
        self.EnvId = None
        self.ServerName = None
        self.VersionName = None
        self.EnvParams = None
        self.MinNum = None
        self.MaxNum = None
        self.ContainerPort = None
        self.Remark = None
        self.CustomLogs = None
        self.IsResetRemark = None
        self.BasicModify = None
        self.OperatorRemark = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.VersionName = params.get("VersionName")
        self.EnvParams = params.get("EnvParams")
        self.MinNum = params.get("MinNum")
        self.MaxNum = params.get("MaxNum")
        self.ContainerPort = params.get("ContainerPort")
        self.Remark = params.get("Remark")
        self.CustomLogs = params.get("CustomLogs")
        self.IsResetRemark = params.get("IsResetRemark")
        self.BasicModify = params.get("BasicModify")
        self.OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudBaseRunServerVersionResponse(AbstractModel):
    """ModifyCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果（succ为成功）
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


class ModifyClsTopicRequest(AbstractModel):
    """ModifyClsTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param Period: 日志生命周期，单位天，可取值范围1~3600，取值为3640时代表永久保存
        :type Period: int
        """
        self.EnvId = None
        self.Period = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClsTopicResponse(AbstractModel):
    """ModifyClsTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDatabaseACLRequest(AbstractModel):
    """ModifyDatabaseACL请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param UUId: C端用户端的唯一ID
        :type UUId: str
        :param Status: 帐号的状态
<li>ENABLE</li>
<li>DISABLE</li>
        :type Status: str
        """
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
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ObjectKV(AbstractModel):
    """Key-Value类型，模拟的 object 类型

    """

    def __init__(self):
        r"""
        :param Key: object 的 key
        :type Key: str
        :param Value: object key 对应的 value
        :type Value: str
        """
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
        


class OneClickTaskStepInfo(AbstractModel):
    """一键部署步骤信息

    """

    def __init__(self):
        r"""
        :param Status: 未启动："todo"
运行中："running"
失败："failed"
成功结束："finished"
        :type Status: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param CostTime: 耗时：秒
        :type CostTime: int
        :param FailReason: 失败原因
        :type FailReason: str
        :param Name: 步骤名
        :type Name: str
        """
        self.Status = None
        self.StartTime = None
        self.EndTime = None
        self.CostTime = None
        self.FailReason = None
        self.Name = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CostTime = params.get("CostTime")
        self.FailReason = params.get("FailReason")
        self.Name = params.get("Name")
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
        r"""
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
        :param Flag: 安装标记。建议使用方统一转大小写之后再判断。
<li>QuickStart：快速启动来源</li>
<li>Activity：活动来源</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Flag: str
        :param ReqBody: 下单时的参数
        :type ReqBody: str
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
        self.Flag = None
        self.ReqBody = None


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
        self.Flag = params.get("Flag")
        self.ReqBody = params.get("ReqBody")
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
        r"""
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
        r"""
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
        r"""
        :param ResourceType: 资源方
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param MetricName: 指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param ResQuota: 按量计费详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ResQuota: float
        :param PkgQuota: 资源包抵扣详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgQuota: float
        :param FreeQuota: 免费额度抵扣详情
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuota: float
        :param EnvId: 环境id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        """
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
        r"""
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
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceActivityRecordRequest(AbstractModel):
    """ReplaceActivityRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param ActivityId: 活动id
        :type ActivityId: int
        :param Status: 状态码
        :type Status: int
        :param SubStatus: 自定义子状态
        :type SubStatus: str
        :param ChannelToken: 鉴权token
        :type ChannelToken: str
        :param Channel: 渠道名，不同渠道对应不同secretKey
        :type Channel: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RollUpdateCloudBaseRunServerVersionRequest(AbstractModel):
    """RollUpdateCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param VersionName: 要替换的版本名称，可以为latest
        :type VersionName: str
        :param UploadType: 枚举（package/repository/image)
        :type UploadType: str
        :param RepositoryType: repository的类型(coding/gitlab/github)
        :type RepositoryType: str
        :param FlowRatio: 流量占比
        :type FlowRatio: int
        :param DockerfilePath: dockerfile地址
        :type DockerfilePath: str
        :param BuildDir: 构建目录
        :type BuildDir: str
        :param Cpu: Cpu的大小，单位：核
        :type Cpu: str
        :param Mem: Mem的大小，单位：G
        :type Mem: str
        :param MinNum: 最小副本数，最小值：0
        :type MinNum: str
        :param MaxNum: 最大副本数
        :type MaxNum: str
        :param PolicyType: 策略类型
        :type PolicyType: str
        :param PolicyThreshold: 策略阈值
        :type PolicyThreshold: str
        :param EnvParams: 环境变量
        :type EnvParams: str
        :param ContainerPort: 容器端口
        :type ContainerPort: int
        :param ServerName: 服务名称
        :type ServerName: str
        :param Repository: repository地址
        :type Repository: str
        :param Branch: 分支
        :type Branch: str
        :param VersionRemark: 版本备注
        :type VersionRemark: str
        :param PackageName: 代码包名字
        :type PackageName: str
        :param PackageVersion: 代码包版本
        :type PackageVersion: str
        :param ImageInfo: Image的详情
        :type ImageInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageInfo`
        :param CodeDetail: Github等拉取代码的详情
        :type CodeDetail: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoDetail`
        :param IsRebuild: 是否回放流量
        :type IsRebuild: bool
        :param InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）
        :type InitialDelaySeconds: int
        :param MountVolumeInfo: cfs挂载信息
        :type MountVolumeInfo: list of CloudBaseRunVolumeMount
        :param Rollback: 是否回滚
        :type Rollback: bool
        :param SnapshotName: 版本历史名
        :type SnapshotName: str
        :param CustomLogs: 自定义采集路径
        :type CustomLogs: str
        :param EnableUnion: 是否启用统一域名
        :type EnableUnion: bool
        :param OperatorRemark: 操作备注
        :type OperatorRemark: str
        :param ServerPath: 服务路径（只会第一次生效）
        :type ServerPath: str
        :param IsUpdateCls: 是否更新Cls
        :type IsUpdateCls: bool
        :param PolicyDetail: 自动扩缩容策略组
        :type PolicyDetail: list of HpaPolicy
        """
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
        self.PolicyDetail = None


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
        if params.get("PolicyDetail") is not None:
            self.PolicyDetail = []
            for item in params.get("PolicyDetail"):
                obj = HpaPolicy()
                obj._deserialize(item)
                self.PolicyDetail.append(obj)
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
        r"""
        :param Result: succ为成功
        :type Result: str
        :param VersionName: 滚动更新的VersionName
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


class SearchClsLogRequest(AbstractModel):
    """SearchClsLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境唯一ID
        :type EnvId: str
        :param StartTime: 查询起始时间条件
        :type StartTime: str
        :param EndTime: 查询结束时间条件
        :type EndTime: str
        :param QueryString: 查询语句，详情参考 https://cloud.tencent.com/document/product/614/47044
        :type QueryString: str
        :param Limit: 单次要返回的日志条数，单次返回的最大条数为100
        :type Limit: int
        :param Context: 加载更多使用，透传上次返回的 context 值，获取后续的日志内容，通过游标最多可获取10000条，请尽可能缩小时间范围
        :type Context: str
        :param Sort: 按时间排序 asc（升序）或者 desc（降序），默认为 desc
        :type Sort: str
        :param UseLucene: 是否使用Lucene语法，默认为false
        :type UseLucene: bool
        """
        self.EnvId = None
        self.StartTime = None
        self.EndTime = None
        self.QueryString = None
        self.Limit = None
        self.Context = None
        self.Sort = None
        self.UseLucene = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.QueryString = params.get("QueryString")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Sort = params.get("Sort")
        self.UseLucene = params.get("UseLucene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClsLogResponse(AbstractModel):
    """SearchClsLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogResults: 日志内容结果
        :type LogResults: :class:`tencentcloud.tcb.v20180608.models.LogResObject`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogResults = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogResults") is not None:
            self.LogResults = LogResObject()
            self.LogResults._deserialize(params.get("LogResults"))
        self.RequestId = params.get("RequestId")


class SmsFreeQuota(AbstractModel):
    """短信免费量

    """

    def __init__(self):
        r"""
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
        r"""
        :param ReportDate: 上报日期
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportDate: str
        :param Uin: 腾讯云uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param EnvId: 资源id:环境id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param Status: 上报任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
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
        r"""
        :param GatewayName: 独立网关名称
        :type GatewayName: str
        :param CPU: CPU核心数
        :type CPU: float
        :param Mem: 内存大小，单位MB
        :type Mem: int
        :param PackageVersion: 套餐包版本名称
        :type PackageVersion: str
        :param GatewayAlias: 网关别名
        :type GatewayAlias: str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetIds: 子网ID列表
        :type SubnetIds: list of str
        :param GatewayDesc: 网关描述
        :type GatewayDesc: str
        :param GateWayStatus: 网关状态
        :type GateWayStatus: str
        :param ServiceInfo: 服务信息
        :type ServiceInfo: :class:`tencentcloud.tcb.v20180608.models.BackendServiceInfo`
        :param PublicClbIp: 公网CLBIP
        :type PublicClbIp: str
        :param InternalClbIp: 内网CLBIP
        :type InternalClbIp: str
        """
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
        self.PublicClbIp = None
        self.InternalClbIp = None


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
        self.PublicClbIp = params.get("PublicClbIp")
        self.InternalClbIp = params.get("InternalClbIp")
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
        r"""
        :param CPU: CPU核心数
        :type CPU: float
        :param Mem: 内存大小，单位MB
        :type Mem: int
        :param PackageVersion: 套餐包版本名称
        :type PackageVersion: str
        """
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
        r"""
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
        r"""
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
        r"""
        :param Key: 标签键
        :type Key: str
        :param Value: 标签值
        :type Value: str
        """
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
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param GatewayName: 网关名称
        :type GatewayName: str
        :param ServiceNameList: 服务名称列表
        :type ServiceNameList: list of str
        """
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
        r"""
        :param Status: 关闭独立网关状态
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class TurnOnStandaloneGatewayRequest(AbstractModel):
    """TurnOnStandaloneGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param GatewayName: 网关名称
        :type GatewayName: str
        :param ServiceNameList: 服务名称列表
        :type ServiceNameList: list of str
        """
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
        r"""
        :param Status: 小租户网关开启状态
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class UnfreezeCloudBaseRunServersRequest(AbstractModel):
    """UnfreezeCloudBaseRunServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境ID
        :type EnvId: str
        :param ServerNameList: 服务名称列表
        :type ServerNameList: list of str
        """
        self.EnvId = None
        self.ServerNameList = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerNameList = params.get("ServerNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnfreezeCloudBaseRunServersResponse(AbstractModel):
    """UnfreezeCloudBaseRunServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 批量执行结果
成功：succ
失败：fail
部分：partial（部分成功、部分失败）
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param FailServerList: 解冻失败列表
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailServerList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.FailServerList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.FailServerList = params.get("FailServerList")
        self.RequestId = params.get("RequestId")