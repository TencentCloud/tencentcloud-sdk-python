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


class CosToken(AbstractModel):
    """Cos token

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID
        :type RequestId: str
        :param Bucket: 存储桶桶名
        :type Bucket: str
        :param Region: 存储桶所在区域
        :type Region: str
        :param TmpSecretId: 临时密钥的SecretId
        :type TmpSecretId: str
        :param TmpSecretKey: 临时密钥的SecretKey
        :type TmpSecretKey: str
        :param SessionToken: 临时密钥的 sessionToken
        :type SessionToken: str
        :param StartTime: 临时密钥获取的开始时间
        :type StartTime: str
        :param ExpiredTime: 临时密钥的 expiredTime
        :type ExpiredTime: str
        :param FullPath: 包完整路径
        :type FullPath: str
        """
        self.RequestId = None
        self.Bucket = None
        self.Region = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.SessionToken = None
        self.StartTime = None
        self.ExpiredTime = None
        self.FullPath = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.SessionToken = params.get("SessionToken")
        self.StartTime = params.get("StartTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.FullPath = params.get("FullPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosTokenRequest(AbstractModel):
    """CreateCosToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务ID
        :type ServiceId: str
        :param VersionId: 服务版本ID
        :type VersionId: str
        :param PkgName: 包名
        :type PkgName: str
        :param OptType: optType 1上传  2查询
        :type OptType: int
        :param SourceChannel: 来源 channel
        :type SourceChannel: int
        """
        self.ServiceId = None
        self.VersionId = None
        self.PkgName = None
        self.OptType = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.VersionId = params.get("VersionId")
        self.PkgName = params.get("PkgName")
        self.OptType = params.get("OptType")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosTokenResponse(AbstractModel):
    """CreateCosToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 成功时为CosToken对象，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tem.v20201221.models.CosToken`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CosToken()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateCosTokenV2Request(AbstractModel):
    """CreateCosTokenV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务ID
        :type ServiceId: str
        :param PkgName: 包名
        :type PkgName: str
        :param OptType: optType 1上传  2查询
        :type OptType: int
        :param SourceChannel: 来源 channel
        :type SourceChannel: int
        :param TimeVersion: 充当deployVersion入参
        :type TimeVersion: str
        """
        self.ServiceId = None
        self.PkgName = None
        self.OptType = None
        self.SourceChannel = None
        self.TimeVersion = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.PkgName = params.get("PkgName")
        self.OptType = params.get("OptType")
        self.SourceChannel = params.get("SourceChannel")
        self.TimeVersion = params.get("TimeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosTokenV2Response(AbstractModel):
    """CreateCosTokenV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 成功时为CosToken对象，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tem.v20201221.models.CosToken`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CosToken()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param Vpc: 私有网络名称
        :type Vpc: str
        :param SubnetIds: 子网列表
        :type SubnetIds: list of str
        :param Description: 命名空间描述
        :type Description: str
        :param K8sVersion: K8s version
        :type K8sVersion: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param EnableTswTraceService: 是否开启tsw服务
        :type EnableTswTraceService: bool
        """
        self.NamespaceName = None
        self.Vpc = None
        self.SubnetIds = None
        self.Description = None
        self.K8sVersion = None
        self.SourceChannel = None
        self.EnableTswTraceService = None


    def _deserialize(self, params):
        self.NamespaceName = params.get("NamespaceName")
        self.Vpc = params.get("Vpc")
        self.SubnetIds = params.get("SubnetIds")
        self.Description = params.get("Description")
        self.K8sVersion = params.get("K8sVersion")
        self.SourceChannel = params.get("SourceChannel")
        self.EnableTswTraceService = params.get("EnableTswTraceService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 成功时为命名空间ID，失败为null
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


class CreateResourceRequest(AbstractModel):
    """CreateResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param NamespaceId: 命名空间 Id
        :type NamespaceId: str
        :param ResourceType: 资源类型，目前支持文件系统：CFS；日志服务：CLS；注册中心：TSE_SRE
        :type ResourceType: str
        :param ResourceId: 资源 Id
        :type ResourceId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.ResourceType = None
        self.ResourceId = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceResponse(AbstractModel):
    """CreateResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 成功与否
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateServiceV2Request(AbstractModel):
    """CreateServiceV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceName: 服务名
        :type ServiceName: str
        :param Description: 描述
        :type Description: str
        :param UseDefaultImageService: 是否使用默认镜像服务 1-是，0-否
        :type UseDefaultImageService: int
        :param RepoType: 如果是绑定仓库，绑定的仓库类型，0-个人版，1-企业版
        :type RepoType: int
        :param InstanceId: 企业版镜像服务的实例id
        :type InstanceId: str
        :param RepoServer: 绑定镜像服务器地址
        :type RepoServer: str
        :param RepoName: 绑定镜像仓库名
        :type RepoName: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param SubnetList: 服务所在子网
        :type SubnetList: list of str
        :param CodingLanguage: 编程语言 
- JAVA
- OTHER
        :type CodingLanguage: str
        :param DeployMode: 部署方式 
- IMAGE
- JAR
- WAR
        :type DeployMode: str
        """
        self.ServiceName = None
        self.Description = None
        self.UseDefaultImageService = None
        self.RepoType = None
        self.InstanceId = None
        self.RepoServer = None
        self.RepoName = None
        self.SourceChannel = None
        self.SubnetList = None
        self.CodingLanguage = None
        self.DeployMode = None


    def _deserialize(self, params):
        self.ServiceName = params.get("ServiceName")
        self.Description = params.get("Description")
        self.UseDefaultImageService = params.get("UseDefaultImageService")
        self.RepoType = params.get("RepoType")
        self.InstanceId = params.get("InstanceId")
        self.RepoServer = params.get("RepoServer")
        self.RepoName = params.get("RepoName")
        self.SourceChannel = params.get("SourceChannel")
        self.SubnetList = params.get("SubnetList")
        self.CodingLanguage = params.get("CodingLanguage")
        self.DeployMode = params.get("DeployMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceV2Response(AbstractModel):
    """CreateServiceV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 服务code
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteIngressRequest(AbstractModel):
    """DeleteIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param NamespaceId: tem NamespaceId
        :type NamespaceId: str
        :param EksNamespace: eks namespace 名
        :type EksNamespace: str
        :param Name: ingress 规则名
        :type Name: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.EksNamespace = None
        self.Name = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.EksNamespace = params.get("EksNamespace")
        self.Name = params.get("Name")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIngressResponse(AbstractModel):
    """DeleteIngress返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否删除成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeployServiceV2Request(AbstractModel):
    """DeployServiceV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务ID
        :type ServiceId: str
        :param ContainerPort: 容器端口
        :type ContainerPort: int
        :param InitPodNum: 初始化 pod 数
        :type InitPodNum: int
        :param CpuSpec: cpu规格
        :type CpuSpec: float
        :param MemorySpec: 内存规格
        :type MemorySpec: float
        :param NamespaceId: 环境ID
        :type NamespaceId: str
        :param ImgRepo: 镜像仓库
        :type ImgRepo: str
        :param VersionDesc: 版本描述信息
        :type VersionDesc: str
        :param JvmOpts: 启动参数
        :type JvmOpts: str
        :param EsInfo: 弹性伸缩配置，不传默认不启用弹性伸缩配置
        :type EsInfo: :class:`tencentcloud.tem.v20201221.models.EsInfo`
        :param EnvConf: 环境变量配置
        :type EnvConf: list of Pair
        :param LogConfs: 日志配置
        :type LogConfs: list of str
        :param StorageConfs: 数据卷配置
        :type StorageConfs: list of StorageConf
        :param StorageMountConfs: 数据卷挂载配置
        :type StorageMountConfs: list of StorageMountConf
        :param DeployMode: 部署类型。
- JAR：通过 jar 包部署
- WAR：通过 war 包部署
- IMAGE：通过镜像部署
        :type DeployMode: str
        :param DeployVersion: 部署类型为 IMAGE 时，该参数表示镜像 tag。
部署类型为 JAR/WAR 时，该参数表示包版本号。
        :type DeployVersion: str
        :param PkgName: 包名。使用 JAR 包或者 WAR 包部署的时候必填。
        :type PkgName: str
        :param JdkVersion: JDK 版本。
- KONA：使用 kona jdk。
- OPEN：使用 open jdk。
        :type JdkVersion: str
        :param SecurityGroupIds: 安全组ID s
        :type SecurityGroupIds: list of str
        :param LogOutputConf: 日志输出配置
        :type LogOutputConf: :class:`tencentcloud.tem.v20201221.models.LogOutputConf`
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param Description: 版本描述
        :type Description: str
        :param ImageCommand: 镜像命令
        :type ImageCommand: str
        :param ImageArgs: 镜像命令参数
        :type ImageArgs: list of str
        :param PortMappings: 服务端口映射
        :type PortMappings: list of PortMapping
        :param UseRegistryDefaultConfig: 是否添加默认注册中心配置
        :type UseRegistryDefaultConfig: bool
        :param SettingConfs: 挂载配置信息
        :type SettingConfs: list of MountedSettingConf
        :param EksService: eks 访问设置
        :type EksService: :class:`tencentcloud.tem.v20201221.models.EksService`
        :param VersionId: 要回滚到的历史版本id
        :type VersionId: str
        :param PostStart: 启动后执行的脚本
        :type PostStart: str
        :param PreStop: 停止前执行的脚本
        :type PreStop: str
        :param DeployStrategyConf: 分批发布策略配置
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20201221.models.DeployStrategyConf`
        :param Liveness: 存活探针配置
        :type Liveness: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        :param Readiness: 就绪探针配置
        :type Readiness: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        """
        self.ServiceId = None
        self.ContainerPort = None
        self.InitPodNum = None
        self.CpuSpec = None
        self.MemorySpec = None
        self.NamespaceId = None
        self.ImgRepo = None
        self.VersionDesc = None
        self.JvmOpts = None
        self.EsInfo = None
        self.EnvConf = None
        self.LogConfs = None
        self.StorageConfs = None
        self.StorageMountConfs = None
        self.DeployMode = None
        self.DeployVersion = None
        self.PkgName = None
        self.JdkVersion = None
        self.SecurityGroupIds = None
        self.LogOutputConf = None
        self.SourceChannel = None
        self.Description = None
        self.ImageCommand = None
        self.ImageArgs = None
        self.PortMappings = None
        self.UseRegistryDefaultConfig = None
        self.SettingConfs = None
        self.EksService = None
        self.VersionId = None
        self.PostStart = None
        self.PreStop = None
        self.DeployStrategyConf = None
        self.Liveness = None
        self.Readiness = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ContainerPort = params.get("ContainerPort")
        self.InitPodNum = params.get("InitPodNum")
        self.CpuSpec = params.get("CpuSpec")
        self.MemorySpec = params.get("MemorySpec")
        self.NamespaceId = params.get("NamespaceId")
        self.ImgRepo = params.get("ImgRepo")
        self.VersionDesc = params.get("VersionDesc")
        self.JvmOpts = params.get("JvmOpts")
        if params.get("EsInfo") is not None:
            self.EsInfo = EsInfo()
            self.EsInfo._deserialize(params.get("EsInfo"))
        if params.get("EnvConf") is not None:
            self.EnvConf = []
            for item in params.get("EnvConf"):
                obj = Pair()
                obj._deserialize(item)
                self.EnvConf.append(obj)
        self.LogConfs = params.get("LogConfs")
        if params.get("StorageConfs") is not None:
            self.StorageConfs = []
            for item in params.get("StorageConfs"):
                obj = StorageConf()
                obj._deserialize(item)
                self.StorageConfs.append(obj)
        if params.get("StorageMountConfs") is not None:
            self.StorageMountConfs = []
            for item in params.get("StorageMountConfs"):
                obj = StorageMountConf()
                obj._deserialize(item)
                self.StorageMountConfs.append(obj)
        self.DeployMode = params.get("DeployMode")
        self.DeployVersion = params.get("DeployVersion")
        self.PkgName = params.get("PkgName")
        self.JdkVersion = params.get("JdkVersion")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LogOutputConf") is not None:
            self.LogOutputConf = LogOutputConf()
            self.LogOutputConf._deserialize(params.get("LogOutputConf"))
        self.SourceChannel = params.get("SourceChannel")
        self.Description = params.get("Description")
        self.ImageCommand = params.get("ImageCommand")
        self.ImageArgs = params.get("ImageArgs")
        if params.get("PortMappings") is not None:
            self.PortMappings = []
            for item in params.get("PortMappings"):
                obj = PortMapping()
                obj._deserialize(item)
                self.PortMappings.append(obj)
        self.UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("SettingConfs") is not None:
            self.SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self.SettingConfs.append(obj)
        if params.get("EksService") is not None:
            self.EksService = EksService()
            self.EksService._deserialize(params.get("EksService"))
        self.VersionId = params.get("VersionId")
        self.PostStart = params.get("PostStart")
        self.PreStop = params.get("PreStop")
        if params.get("DeployStrategyConf") is not None:
            self.DeployStrategyConf = DeployStrategyConf()
            self.DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("Liveness") is not None:
            self.Liveness = HealthCheckConfig()
            self.Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self.Readiness = HealthCheckConfig()
            self.Readiness._deserialize(params.get("Readiness"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployServiceV2Response(AbstractModel):
    """DeployServiceV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 版本ID（前端可忽略）
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeployStrategyConf(AbstractModel):
    """分批发布策略配置

    """

    def __init__(self):
        r"""
        :param TotalBatchCount: 总分批数
        :type TotalBatchCount: int
        :param BetaBatchNum: beta分批实例数
        :type BetaBatchNum: int
        :param DeployStrategyType: 分批策略：0-全自动，1-全手动，beta分批一定是手动的，这里的策略指定的是剩余批次
        :type DeployStrategyType: int
        :param BatchInterval: 每批暂停间隔
        :type BatchInterval: int
        """
        self.TotalBatchCount = None
        self.BetaBatchNum = None
        self.DeployStrategyType = None
        self.BatchInterval = None


    def _deserialize(self, params):
        self.TotalBatchCount = params.get("TotalBatchCount")
        self.BetaBatchNum = params.get("BetaBatchNum")
        self.DeployStrategyType = params.get("DeployStrategyType")
        self.BatchInterval = params.get("BatchInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressRequest(AbstractModel):
    """DescribeIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param NamespaceId: tem namespaceId
        :type NamespaceId: str
        :param EksNamespace: eks namespace 名
        :type EksNamespace: str
        :param Name: ingress 规则名
        :type Name: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.EksNamespace = None
        self.Name = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.EksNamespace = params.get("EksNamespace")
        self.Name = params.get("Name")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressResponse(AbstractModel):
    """DescribeIngress返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: Ingress 规则配置
        :type Result: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = IngressInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeIngressesRequest(AbstractModel):
    """DescribeIngresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param NamespaceId: namespace id
        :type NamespaceId: str
        :param EksNamespace: namespace
        :type EksNamespace: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param Names: ingress 规则名列表
        :type Names: list of str
        """
        self.NamespaceId = None
        self.EksNamespace = None
        self.SourceChannel = None
        self.Names = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.EksNamespace = params.get("EksNamespace")
        self.SourceChannel = params.get("SourceChannel")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressesResponse(AbstractModel):
    """DescribeIngresses返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: ingress 数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of IngressInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = IngressInfo()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页limit
        :type Limit: int
        :param Offset: 分页下标
        :type Offset: int
        :param SourceChannel: 来源source
        :type SourceChannel: int
        """
        self.Limit = None
        self.Offset = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20201221.models.NamespacePage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = NamespacePage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeRelatedIngressesRequest(AbstractModel):
    """DescribeRelatedIngresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param NamespaceId: 环境 id
        :type NamespaceId: str
        :param EksNamespace: EKS namespace
        :type EksNamespace: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param ServiceId: 服务 ID
        :type ServiceId: str
        """
        self.NamespaceId = None
        self.EksNamespace = None
        self.SourceChannel = None
        self.ServiceId = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.EksNamespace = params.get("EksNamespace")
        self.SourceChannel = params.get("SourceChannel")
        self.ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelatedIngressesResponse(AbstractModel):
    """DescribeRelatedIngresses返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: ingress 数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of IngressInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = IngressInfo()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRunPodPage(AbstractModel):
    """版本pod列表

    """

    def __init__(self):
        r"""
        :param Offset: 分页下标
        :type Offset: int
        :param Limit: 单页条数
        :type Limit: int
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 请求id
        :type RequestId: str
        :param PodList: 条目
        :type PodList: list of RunVersionPod
        """
        self.Offset = None
        self.Limit = None
        self.TotalCount = None
        self.RequestId = None
        self.PodList = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        if params.get("PodList") is not None:
            self.PodList = []
            for item in params.get("PodList"):
                obj = RunVersionPod()
                obj._deserialize(item)
                self.PodList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceRunPodListV2Request(AbstractModel):
    """DescribeServiceRunPodListV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param NamespaceId: 环境id
        :type NamespaceId: str
        :param ServiceId: 服务名id
        :type ServiceId: str
        :param Limit: 单页条数，默认值20
        :type Limit: int
        :param Offset: 分页下标，默认值0
        :type Offset: int
        :param Status: 实例状态 
- Running 
- Pending 
- Error
        :type Status: str
        :param PodName: 实例名字
        :type PodName: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.ServiceId = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.PodName = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.PodName = params.get("PodName")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceRunPodListV2Response(AbstractModel):
    """DescribeServiceRunPodListV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20201221.models.DescribeRunPodPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DescribeRunPodPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class EksService(AbstractModel):
    """eks service info

    """

    def __init__(self):
        r"""
        :param Name: service name
        :type Name: str
        :param Ports: 可用端口
        :type Ports: list of int
        :param Yaml: yaml 内容
        :type Yaml: str
        :param ServiceName: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param VersionName: 版本名
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param ClusterIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIp: list of str
        :param ExternalIp: 外网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalIp: str
        :param Type: 访问类型，可选值：
- EXTERNAL（公网访问）
- VPC（vpc内访问）
- CLUSTER（集群内访问）
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param SubnetId: 子网ID，只在类型为vpc访问时才有值
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param LoadBalanceId: 负载均衡ID，只在外网访问和vpc内访问才有值，默认自动创建
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalanceId: str
        :param PortMappings: 端口映射
注意：此字段可能返回 null，表示取不到有效值。
        :type PortMappings: list of PortMapping
        """
        self.Name = None
        self.Ports = None
        self.Yaml = None
        self.ServiceName = None
        self.VersionName = None
        self.ClusterIp = None
        self.ExternalIp = None
        self.Type = None
        self.SubnetId = None
        self.LoadBalanceId = None
        self.PortMappings = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Ports = params.get("Ports")
        self.Yaml = params.get("Yaml")
        self.ServiceName = params.get("ServiceName")
        self.VersionName = params.get("VersionName")
        self.ClusterIp = params.get("ClusterIp")
        self.ExternalIp = params.get("ExternalIp")
        self.Type = params.get("Type")
        self.SubnetId = params.get("SubnetId")
        self.LoadBalanceId = params.get("LoadBalanceId")
        if params.get("PortMappings") is not None:
            self.PortMappings = []
            for item in params.get("PortMappings"):
                obj = PortMapping()
                obj._deserialize(item)
                self.PortMappings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsInfo(AbstractModel):
    """弹性伸缩配置

    """

    def __init__(self):
        r"""
        :param MinAliveInstances: 最小实例数
        :type MinAliveInstances: int
        :param MaxAliveInstances: 最大实例数
        :type MaxAliveInstances: int
        :param EsStrategy: 弹性策略,1:cpu，2:内存
        :type EsStrategy: int
        :param Threshold: 弹性扩缩容条件值
        :type Threshold: int
        :param VersionId: 版本Id
        :type VersionId: str
        """
        self.MinAliveInstances = None
        self.MaxAliveInstances = None
        self.EsStrategy = None
        self.Threshold = None
        self.VersionId = None


    def _deserialize(self, params):
        self.MinAliveInstances = params.get("MinAliveInstances")
        self.MaxAliveInstances = params.get("MaxAliveInstances")
        self.EsStrategy = params.get("EsStrategy")
        self.Threshold = params.get("Threshold")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateDownloadUrlRequest(AbstractModel):
    """GenerateDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务ID
        :type ServiceId: str
        :param PkgName: 包名
        :type PkgName: str
        :param DeployVersion: 需要下载的包版本
        :type DeployVersion: str
        :param SourceChannel: 来源 channel
        :type SourceChannel: int
        """
        self.ServiceId = None
        self.PkgName = None
        self.DeployVersion = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.PkgName = params.get("PkgName")
        self.DeployVersion = params.get("DeployVersion")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateDownloadUrlResponse(AbstractModel):
    """GenerateDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 包下载临时链接
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


class HealthCheckConfig(AbstractModel):
    """健康检查配置

    """

    def __init__(self):
        r"""
        :param Type: 支持的健康检查类型，如 HttpGet，TcpSocket，Exec
        :type Type: str
        :param Protocol: 仅当健康检查类型为 HttpGet 时有效，表示协议类型，如 HTTP，HTTPS
        :type Protocol: str
        :param Path: 仅当健康检查类型为 HttpGet 时有效，表示请求路径
        :type Path: str
        :param Exec: 仅当健康检查类型为 Exec 时有效，表示执行的脚本内容
        :type Exec: str
        :param Port: 仅当健康检查类型为 HttpGet\TcpSocket 时有效，表示请求路径
        :type Port: int
        :param InitialDelaySeconds: 检查延迟开始时间，单位为秒，默认为 0
        :type InitialDelaySeconds: int
        :param TimeoutSeconds: 超时时间，单位为秒，默认为 1
        :type TimeoutSeconds: int
        :param PeriodSeconds: 间隔时间，单位为秒，默认为 10
        :type PeriodSeconds: int
        """
        self.Type = None
        self.Protocol = None
        self.Path = None
        self.Exec = None
        self.Port = None
        self.InitialDelaySeconds = None
        self.TimeoutSeconds = None
        self.PeriodSeconds = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Protocol = params.get("Protocol")
        self.Path = params.get("Path")
        self.Exec = params.get("Exec")
        self.Port = params.get("Port")
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        self.TimeoutSeconds = params.get("TimeoutSeconds")
        self.PeriodSeconds = params.get("PeriodSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressInfo(AbstractModel):
    """Ingress 配置

    """

    def __init__(self):
        r"""
        :param NamespaceId: tem namespaceId
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param EksNamespace: eks namespace
        :type EksNamespace: str
        :param AddressIPVersion: ip version
        :type AddressIPVersion: str
        :param Name: ingress name
        :type Name: str
        :param Rules: rules 配置
        :type Rules: list of IngressRule
        :param ClbId: clb ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClbId: str
        :param Tls: tls 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tls: list of IngressTls
        :param ClusterId: eks clusterId
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Vip: clb ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Mixed: 是否混合 https，默认 false，可选值 true 代表有 https 协议监听
        :type Mixed: bool
        """
        self.NamespaceId = None
        self.EksNamespace = None
        self.AddressIPVersion = None
        self.Name = None
        self.Rules = None
        self.ClbId = None
        self.Tls = None
        self.ClusterId = None
        self.Vip = None
        self.CreateTime = None
        self.Mixed = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.EksNamespace = params.get("EksNamespace")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.Name = params.get("Name")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = IngressRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.ClbId = params.get("ClbId")
        if params.get("Tls") is not None:
            self.Tls = []
            for item in params.get("Tls"):
                obj = IngressTls()
                obj._deserialize(item)
                self.Tls.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.Vip = params.get("Vip")
        self.CreateTime = params.get("CreateTime")
        self.Mixed = params.get("Mixed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRule(AbstractModel):
    """ingress rule 配置

    """

    def __init__(self):
        r"""
        :param Http: ingress rule value
        :type Http: :class:`tencentcloud.tem.v20201221.models.IngressRuleValue`
        :param Host: host 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param Protocol: 协议，选项为 http， https，默认为 http
        :type Protocol: str
        """
        self.Http = None
        self.Host = None
        self.Protocol = None


    def _deserialize(self, params):
        if params.get("Http") is not None:
            self.Http = IngressRuleValue()
            self.Http._deserialize(params.get("Http"))
        self.Host = params.get("Host")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRuleBackend(AbstractModel):
    """Ingress 规则 backend 配置

    """

    def __init__(self):
        r"""
        :param ServiceName: eks service 名
        :type ServiceName: str
        :param ServicePort: eks service 端口
        :type ServicePort: int
        """
        self.ServiceName = None
        self.ServicePort = None


    def _deserialize(self, params):
        self.ServiceName = params.get("ServiceName")
        self.ServicePort = params.get("ServicePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRulePath(AbstractModel):
    """Ingress Rule Path 配置

    """

    def __init__(self):
        r"""
        :param Path: path 信息
        :type Path: str
        :param Backend: backend 配置
        :type Backend: :class:`tencentcloud.tem.v20201221.models.IngressRuleBackend`
        """
        self.Path = None
        self.Backend = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        if params.get("Backend") is not None:
            self.Backend = IngressRuleBackend()
            self.Backend._deserialize(params.get("Backend"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRuleValue(AbstractModel):
    """Ingress Rule Value 配置

    """

    def __init__(self):
        r"""
        :param Paths: rule 整体配置
        :type Paths: list of IngressRulePath
        """
        self.Paths = None


    def _deserialize(self, params):
        if params.get("Paths") is not None:
            self.Paths = []
            for item in params.get("Paths"):
                obj = IngressRulePath()
                obj._deserialize(item)
                self.Paths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressTls(AbstractModel):
    """ingress tls 配置

    """

    def __init__(self):
        r"""
        :param Hosts: host 数组, 空数组表示全部域名的默认证书
        :type Hosts: list of str
        :param SecretName: secret name，如使用证书，则填空字符串
        :type SecretName: str
        :param CertificateId: SSL Certificate Id
        :type CertificateId: str
        """
        self.Hosts = None
        self.SecretName = None
        self.CertificateId = None


    def _deserialize(self, params):
        self.Hosts = params.get("Hosts")
        self.SecretName = params.get("SecretName")
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogOutputConf(AbstractModel):
    """日志输出配置

    """

    def __init__(self):
        r"""
        :param OutputType: 日志消费端类型
        :type OutputType: str
        :param ClsLogsetName: cls日志集
        :type ClsLogsetName: str
        :param ClsLogTopicId: cls日志主题
        :type ClsLogTopicId: str
        :param ClsLogsetId: cls日志集id
        :type ClsLogsetId: str
        :param ClsLogTopicName: cls日志名称
        :type ClsLogTopicName: str
        """
        self.OutputType = None
        self.ClsLogsetName = None
        self.ClsLogTopicId = None
        self.ClsLogsetId = None
        self.ClsLogTopicName = None


    def _deserialize(self, params):
        self.OutputType = params.get("OutputType")
        self.ClsLogsetName = params.get("ClsLogsetName")
        self.ClsLogTopicId = params.get("ClsLogTopicId")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsLogTopicName = params.get("ClsLogTopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIngressRequest(AbstractModel):
    """ModifyIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ingress: Ingress 规则配置
        :type Ingress: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.Ingress = None
        self.SourceChannel = None


    def _deserialize(self, params):
        if params.get("Ingress") is not None:
            self.Ingress = IngressInfo()
            self.Ingress._deserialize(params.get("Ingress"))
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIngressResponse(AbstractModel):
    """ModifyIngress返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 创建成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param NamespaceId: 环境id
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param Description: 命名空间描述
        :type Description: str
        :param Vpc: 私有网络名称
        :type Vpc: str
        :param SubnetIds: 子网网络
        :type SubnetIds: list of str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.NamespaceName = None
        self.Description = None
        self.Vpc = None
        self.SubnetIds = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.Description = params.get("Description")
        self.Vpc = params.get("Vpc")
        self.SubnetIds = params.get("SubnetIds")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNamespaceResponse(AbstractModel):
    """ModifyNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 成功时为命名空间ID，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyServiceInfoRequest(AbstractModel):
    """ModifyServiceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务ID
        :type ServiceId: str
        :param Description: 描述
        :type Description: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.ServiceId = None
        self.Description = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Description = params.get("Description")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceInfoResponse(AbstractModel):
    """ModifyServiceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 成功与否
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class MountedSettingConf(AbstractModel):
    """挂载配置信息

    """

    def __init__(self):
        r"""
        :param ConfigDataName: 配置名称
        :type ConfigDataName: str
        :param MountedPath: 挂载路径
        :type MountedPath: str
        :param Data: 配置内容
        :type Data: list of Pair
        """
        self.ConfigDataName = None
        self.MountedPath = None
        self.Data = None


    def _deserialize(self, params):
        self.ConfigDataName = params.get("ConfigDataName")
        self.MountedPath = params.get("MountedPath")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespacePage(AbstractModel):
    """命名空间分页

    """

    def __init__(self):
        r"""
        :param Records: 分页内容
        :type Records: list of TemNamespaceInfo
        :param Total: 总数
        :type Total: int
        :param Size: 条目数
        :type Size: int
        :param Pages: 页数
        :type Pages: int
        """
        self.Records = None
        self.Total = None
        self.Size = None
        self.Pages = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = TemNamespaceInfo()
                obj._deserialize(item)
                self.Records.append(obj)
        self.Total = params.get("Total")
        self.Size = params.get("Size")
        self.Pages = params.get("Pages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pair(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param Key: 建
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
        


class PortMapping(AbstractModel):
    """服务端口映射

    """

    def __init__(self):
        r"""
        :param Port: 端口
        :type Port: int
        :param TargetPort: 映射端口
        :type TargetPort: int
        :param Protocol: 协议栈 TCP/UDP
        :type Protocol: str
        """
        self.Port = None
        self.TargetPort = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.TargetPort = params.get("TargetPort")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartServiceRunPodRequest(AbstractModel):
    """RestartServiceRunPod请求参数结构体

    """

    def __init__(self):
        r"""
        :param NamespaceId: 环境id
        :type NamespaceId: str
        :param ServiceId: 服务名id
        :type ServiceId: str
        :param PodName: 名字
        :type PodName: str
        :param Limit: 单页条数
        :type Limit: int
        :param Offset: 分页下标
        :type Offset: int
        :param Status: pod状态
        :type Status: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.ServiceId = None
        self.PodName = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.ServiceId = params.get("ServiceId")
        self.PodName = params.get("PodName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartServiceRunPodResponse(AbstractModel):
    """RestartServiceRunPod返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RunVersionPod(AbstractModel):
    """版本pod

    """

    def __init__(self):
        r"""
        :param Webshell: shell地址
        :type Webshell: str
        :param PodId: pod的id
        :type PodId: str
        :param Status: 状态
        :type Status: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param PodIp: 实例的ip
        :type PodIp: str
        :param Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param DeployVersion: 部署版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployVersion: str
        :param RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        """
        self.Webshell = None
        self.PodId = None
        self.Status = None
        self.CreateTime = None
        self.PodIp = None
        self.Zone = None
        self.DeployVersion = None
        self.RestartCount = None


    def _deserialize(self, params):
        self.Webshell = params.get("Webshell")
        self.PodId = params.get("PodId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.PodIp = params.get("PodIp")
        self.Zone = params.get("Zone")
        self.DeployVersion = params.get("DeployVersion")
        self.RestartCount = params.get("RestartCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageConf(AbstractModel):
    """存储卷配置

    """

    def __init__(self):
        r"""
        :param StorageVolName: 存储卷名称
        :type StorageVolName: str
        :param StorageVolPath: 存储卷路径
        :type StorageVolPath: str
        :param StorageVolIp: 存储卷IP
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageVolIp: str
        """
        self.StorageVolName = None
        self.StorageVolPath = None
        self.StorageVolIp = None


    def _deserialize(self, params):
        self.StorageVolName = params.get("StorageVolName")
        self.StorageVolPath = params.get("StorageVolPath")
        self.StorageVolIp = params.get("StorageVolIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageMountConf(AbstractModel):
    """数据卷挂载信息

    """

    def __init__(self):
        r"""
        :param VolumeName: 数据卷名
        :type VolumeName: str
        :param MountPath: 数据卷绑定路径
        :type MountPath: str
        """
        self.VolumeName = None
        self.MountPath = None


    def _deserialize(self, params):
        self.VolumeName = params.get("VolumeName")
        self.MountPath = params.get("MountPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemNamespaceInfo(AbstractModel):
    """命名空间对象

    """

    def __init__(self):
        r"""
        :param NamespaceId: 命名空间id
        :type NamespaceId: str
        :param Channel: 渠道
        :type Channel: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param Region: 区域名称
        :type Region: str
        :param Description: 命名空间描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Status: 状态,1:已销毁;0:正常
        :type Status: int
        :param Vpc: vpc网络
        :type Vpc: str
        :param CreateDate: 创建时间
        :type CreateDate: str
        :param ModifyDate: 修改时间
        :type ModifyDate: str
        :param Modifier: 修改人
        :type Modifier: str
        :param Creator: 创建人
        :type Creator: str
        :param ServiceNum: 服务数
        :type ServiceNum: int
        :param RunInstancesNum: 运行实例数
        :type RunInstancesNum: int
        :param SubnetId: 子网络
        :type SubnetId: str
        :param TcbEnvStatus: tcb环境状态
        :type TcbEnvStatus: str
        :param ClusterStatus: eks cluster status
        :type ClusterStatus: str
        :param EnableTswTraceService: 是否开启tsw
        :type EnableTswTraceService: bool
        """
        self.NamespaceId = None
        self.Channel = None
        self.NamespaceName = None
        self.Region = None
        self.Description = None
        self.Status = None
        self.Vpc = None
        self.CreateDate = None
        self.ModifyDate = None
        self.Modifier = None
        self.Creator = None
        self.ServiceNum = None
        self.RunInstancesNum = None
        self.SubnetId = None
        self.TcbEnvStatus = None
        self.ClusterStatus = None
        self.EnableTswTraceService = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.Channel = params.get("Channel")
        self.NamespaceName = params.get("NamespaceName")
        self.Region = params.get("Region")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        self.Vpc = params.get("Vpc")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.Modifier = params.get("Modifier")
        self.Creator = params.get("Creator")
        self.ServiceNum = params.get("ServiceNum")
        self.RunInstancesNum = params.get("RunInstancesNum")
        self.SubnetId = params.get("SubnetId")
        self.TcbEnvStatus = params.get("TcbEnvStatus")
        self.ClusterStatus = params.get("ClusterStatus")
        self.EnableTswTraceService = params.get("EnableTswTraceService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        