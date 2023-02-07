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


class Autoscaler(AbstractModel):
    """弹性伸缩策略组合

    """

    def __init__(self):
        r"""
        :param MinReplicas: 弹性伸缩最小实例数
        :type MinReplicas: int
        :param MaxReplicas: 弹性伸缩最大实例数
        :type MaxReplicas: int
        :param HorizontalAutoscaler: 指标弹性伸缩策略
注意：此字段可能返回 null，表示取不到有效值。
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param CronHorizontalAutoscaler: 定时弹性伸缩策略
注意：此字段可能返回 null，表示取不到有效值。
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param AutoscalerId: 弹性伸缩ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalerId: str
        :param AutoscalerName: 弹性伸缩名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalerName: str
        :param Description: 弹性伸缩描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateDate: 创建日期
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param ModifyDate: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyDate: str
        :param EnableDate: 启用时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableDate: str
        :param Enabled: 是否启用
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self.MinReplicas = None
        self.MaxReplicas = None
        self.HorizontalAutoscaler = None
        self.CronHorizontalAutoscaler = None
        self.AutoscalerId = None
        self.AutoscalerName = None
        self.Description = None
        self.CreateDate = None
        self.ModifyDate = None
        self.EnableDate = None
        self.Enabled = None


    def _deserialize(self, params):
        self.MinReplicas = params.get("MinReplicas")
        self.MaxReplicas = params.get("MaxReplicas")
        if params.get("HorizontalAutoscaler") is not None:
            self.HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self.HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self.CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self.CronHorizontalAutoscaler.append(obj)
        self.AutoscalerId = params.get("AutoscalerId")
        self.AutoscalerName = params.get("AutoscalerName")
        self.Description = params.get("Description")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.EnableDate = params.get("EnableDate")
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigData(AbstractModel):
    """配置

    """

    def __init__(self):
        r"""
        :param Name: 配置名称
        :type Name: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param RelatedApplications: 关联的服务列表
        :type RelatedApplications: list of TemService
        :param Data: 配置条目
        :type Data: list of Pair
        """
        self.Name = None
        self.CreateTime = None
        self.RelatedApplications = None
        self.Data = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        if params.get("RelatedApplications") is not None:
            self.RelatedApplications = []
            for item in params.get("RelatedApplications"):
                obj = TemService()
                obj._deserialize(item)
                self.RelatedApplications.append(obj)
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
        


class CreateApplicationAutoscalerRequest(AbstractModel):
    """CreateApplicationAutoscaler请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param Autoscaler: 弹性伸缩策略
        :type Autoscaler: :class:`tencentcloud.tem.v20210701.models.Autoscaler`
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.Autoscaler = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        if params.get("Autoscaler") is not None:
            self.Autoscaler = Autoscaler()
            self.Autoscaler._deserialize(params.get("Autoscaler"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationAutoscalerResponse(AbstractModel):
    """CreateApplicationAutoscaler返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 弹性伸缩策略组合ID
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


class CreateApplicationRequest(AbstractModel):
    """CreateApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationName: 应用名
        :type ApplicationName: str
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
        :param SubnetList: 应用所在子网
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
        :param EnableTracing: 是否开启 Java 应用的 APM 自动上报功能，1 表示启用；0 表示关闭
        :type EnableTracing: int
        :param UseDefaultImageServiceParameters: 使用默认镜像服务额外参数
        :type UseDefaultImageServiceParameters: :class:`tencentcloud.tem.v20210701.models.UseDefaultRepoParameters`
        :param Tags: 标签
        :type Tags: list of Tag
        """
        self.ApplicationName = None
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
        self.EnableTracing = None
        self.UseDefaultImageServiceParameters = None
        self.Tags = None


    def _deserialize(self, params):
        self.ApplicationName = params.get("ApplicationName")
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
        self.EnableTracing = params.get("EnableTracing")
        if params.get("UseDefaultImageServiceParameters") is not None:
            self.UseDefaultImageServiceParameters = UseDefaultRepoParameters()
            self.UseDefaultImageServiceParameters._deserialize(params.get("UseDefaultImageServiceParameters"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationResponse(AbstractModel):
    """CreateApplication返回参数结构体

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


class CreateApplicationServiceRequest(AbstractModel):
    """CreateApplicationService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param Service: 访问方式详情
        :type Service: :class:`tencentcloud.tem.v20210701.models.ServicePortMapping`
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.Service = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        if params.get("Service") is not None:
            self.Service = ServicePortMapping()
            self.Service._deserialize(params.get("Service"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationServiceResponse(AbstractModel):
    """CreateApplicationService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否成功
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


class CreateConfigDataRequest(AbstractModel):
    """CreateConfigData请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param Name: 配置名
        :type Name: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param Data: 配置信息
        :type Data: list of Pair
        """
        self.EnvironmentId = None
        self.Name = None
        self.SourceChannel = None
        self.Data = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.SourceChannel = params.get("SourceChannel")
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
        


class CreateConfigDataResponse(AbstractModel):
    """CreateConfigData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 创建是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateCosTokenRequest(AbstractModel):
    """CreateCosToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param PkgName: 包名
        :type PkgName: str
        :param OptType: optType 1上传  2查询
        :type OptType: int
        :param SourceChannel: 来源 channel
        :type SourceChannel: int
        :param TimeVersion: 充当deployVersion入参
        :type TimeVersion: str
        """
        self.ApplicationId = None
        self.PkgName = None
        self.OptType = None
        self.SourceChannel = None
        self.TimeVersion = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
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
        


class CreateCosTokenResponse(AbstractModel):
    """CreateCosToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 成功时为CosToken对象，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tem.v20210701.models.CosToken`
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


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentName: 环境名称
        :type EnvironmentName: str
        :param Description: 环境描述
        :type Description: str
        :param Vpc: 私有网络名称
        :type Vpc: str
        :param SubnetIds: 子网列表
        :type SubnetIds: list of str
        :param K8sVersion: K8s version
        :type K8sVersion: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param EnableTswTraceService: 是否开启tsw服务
        :type EnableTswTraceService: bool
        :param Tags: 标签
        :type Tags: list of Tag
        :param EnvType: 环境类型：test、pre、prod
        :type EnvType: str
        :param CreateRegion: 创建环境的region
        :type CreateRegion: str
        :param SetupVpc: 是否创建私有网络
        :type SetupVpc: bool
        :param SetupPrometheus: 是否创建 Prometheus 实例
        :type SetupPrometheus: bool
        :param PrometheusId: prometheus 实例 id
        :type PrometheusId: str
        :param ApmId: apm id
        :type ApmId: str
        """
        self.EnvironmentName = None
        self.Description = None
        self.Vpc = None
        self.SubnetIds = None
        self.K8sVersion = None
        self.SourceChannel = None
        self.EnableTswTraceService = None
        self.Tags = None
        self.EnvType = None
        self.CreateRegion = None
        self.SetupVpc = None
        self.SetupPrometheus = None
        self.PrometheusId = None
        self.ApmId = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Description = params.get("Description")
        self.Vpc = params.get("Vpc")
        self.SubnetIds = params.get("SubnetIds")
        self.K8sVersion = params.get("K8sVersion")
        self.SourceChannel = params.get("SourceChannel")
        self.EnableTswTraceService = params.get("EnableTswTraceService")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.EnvType = params.get("EnvType")
        self.CreateRegion = params.get("CreateRegion")
        self.SetupVpc = params.get("SetupVpc")
        self.SetupPrometheus = params.get("SetupPrometheus")
        self.PrometheusId = params.get("PrometheusId")
        self.ApmId = params.get("ApmId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 成功时为环境ID，失败为null
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


class CreateLogConfigRequest(AbstractModel):
    """CreateLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param Name: 配置名
        :type Name: str
        :param InputType: 收集类型，container_stdout 为标准输出；container_file 为文件；
        :type InputType: str
        :param ApplicationId: 应用 ID
        :type ApplicationId: str
        :param LogsetId: 日志集 ID
        :type LogsetId: str
        :param TopicId: 日志主题 ID
        :type TopicId: str
        :param LogType: 日志提取模式，minimalist_log 为单行全文；multiline_log 为多行全文；json_log 为 json格式；fullregex_log 为单行正则；multiline_fullregex_log 为多行正则
        :type LogType: str
        :param BeginningRegex: 首行正则表达式，当LogType=multiline_log 时生效
        :type BeginningRegex: str
        :param LogPath: 收集文件目录，当 InputType=container_file 时生效
        :type LogPath: str
        :param FilePattern: 收集文件名模式，当 InputType=container_file 时生效
        :type FilePattern: str
        :param ExtractRule: 导出规则
        :type ExtractRule: :class:`tencentcloud.tem.v20210701.models.LogConfigExtractRule`
        """
        self.EnvironmentId = None
        self.Name = None
        self.InputType = None
        self.ApplicationId = None
        self.LogsetId = None
        self.TopicId = None
        self.LogType = None
        self.BeginningRegex = None
        self.LogPath = None
        self.FilePattern = None
        self.ExtractRule = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.InputType = params.get("InputType")
        self.ApplicationId = params.get("ApplicationId")
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.LogType = params.get("LogType")
        self.BeginningRegex = params.get("BeginningRegex")
        self.LogPath = params.get("LogPath")
        self.FilePattern = params.get("FilePattern")
        if params.get("ExtractRule") is not None:
            self.ExtractRule = LogConfigExtractRule()
            self.ExtractRule._deserialize(params.get("ExtractRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogConfigResponse(AbstractModel):
    """CreateLogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 创建是否成功
        :type Result: bool
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
        :param EnvironmentId: 环境 Id
        :type EnvironmentId: str
        :param ResourceType: 资源类型，目前支持文件系统：CFS；日志服务：CLS；注册中心：TSE_SRE
        :type ResourceType: str
        :param ResourceId: 资源 Id
        :type ResourceId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param ResourceFrom: 资源来源，目前支持：existing，已有资源；creating，自动创建
        :type ResourceFrom: str
        :param ResourceConfig: 设置 resource 的额外配置
        :type ResourceConfig: str
        """
        self.EnvironmentId = None
        self.ResourceType = None
        self.ResourceId = None
        self.SourceChannel = None
        self.ResourceFrom = None
        self.ResourceConfig = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.SourceChannel = params.get("SourceChannel")
        self.ResourceFrom = params.get("ResourceFrom")
        self.ResourceConfig = params.get("ResourceConfig")
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


class CronHorizontalAutoscaler(AbstractModel):
    """定时伸缩策略

    """

    def __init__(self):
        r"""
        :param Name: 定时伸缩策略名称
        :type Name: str
        :param Period: 策略周期
* * *，三个范围，第一个是天，第二个是月，第三个是周，中间用空格隔开
例子：
* * * （每天）
* * 0-3 （每周日到周三）
1,11,21 * *（每个月1号，11号，21号）
        :type Period: str
        :param Schedules: 定时伸缩策略明细
        :type Schedules: list of CronHorizontalAutoscalerSchedule
        :param Enabled: 是否启用
        :type Enabled: bool
        :param Priority: 策略优先级，值越大优先级越高，0为最小值
        :type Priority: int
        """
        self.Name = None
        self.Period = None
        self.Schedules = None
        self.Enabled = None
        self.Priority = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Period = params.get("Period")
        if params.get("Schedules") is not None:
            self.Schedules = []
            for item in params.get("Schedules"):
                obj = CronHorizontalAutoscalerSchedule()
                obj._deserialize(item)
                self.Schedules.append(obj)
        self.Enabled = params.get("Enabled")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CronHorizontalAutoscalerSchedule(AbstractModel):
    """定时伸缩策略明细

    """

    def __init__(self):
        r"""
        :param StartAt: 触发事件，小时分钟，用:分割
例如
00:00（零点零分触发）
        :type StartAt: str
        :param TargetReplicas: 目标实例数（不大于50）
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetReplicas: int
        """
        self.StartAt = None
        self.TargetReplicas = None


    def _deserialize(self, params):
        self.StartAt = params.get("StartAt")
        self.TargetReplicas = params.get("TargetReplicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationAutoscalerRequest(AbstractModel):
    """DeleteApplicationAutoscaler请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param AutoscalerId: 弹性伸缩策略ID
        :type AutoscalerId: str
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.AutoscalerId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationAutoscalerResponse(AbstractModel):
    """DeleteApplicationAutoscaler返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否成功
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


class DeleteApplicationRequest(AbstractModel):
    """DeleteApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务Id
        :type ApplicationId: str
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param DeleteApplicationIfNoRunningVersion: 当服务没有任何运行版本时，是否删除此服务
        :type DeleteApplicationIfNoRunningVersion: bool
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.DeleteApplicationIfNoRunningVersion = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.DeleteApplicationIfNoRunningVersion = params.get("DeleteApplicationIfNoRunningVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationResponse(AbstractModel):
    """DeleteApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApplicationServiceRequest(AbstractModel):
    """DeleteApplicationService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param ServiceName: 访问方式服务名
        :type ServiceName: str
        """
        self.ApplicationId = None
        self.SourceChannel = None
        self.EnvironmentId = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SourceChannel = params.get("SourceChannel")
        self.EnvironmentId = params.get("EnvironmentId")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationServiceResponse(AbstractModel):
    """DeleteApplicationService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否成功
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


class DeleteIngressRequest(AbstractModel):
    """DeleteIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param ClusterNamespace: 环境 namespace
        :type ClusterNamespace: str
        :param IngressName: ingress 规则名
        :type IngressName: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.ClusterNamespace = None
        self.IngressName = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterNamespace = params.get("ClusterNamespace")
        self.IngressName = params.get("IngressName")
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


class DeployApplicationRequest(AbstractModel):
    """DeployApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param InitPodNum: 初始化 pod 数
        :type InitPodNum: int
        :param CpuSpec: cpu规格
        :type CpuSpec: float
        :param MemorySpec: 内存规格
        :type MemorySpec: float
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param ImgRepo: 镜像仓库
        :type ImgRepo: str
        :param VersionDesc: 版本描述信息
        :type VersionDesc: str
        :param JvmOpts: 启动参数
        :type JvmOpts: str
        :param EsInfo: 弹性伸缩配置（已废弃，请使用HorizontalAutoscaler设置弹性策略）
        :type EsInfo: :class:`tencentcloud.tem.v20210701.models.EsInfo`
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
- KONA:8：使用 kona jdk 8。
- OPEN:8：使用 open jdk 8。
- KONA:11：使用 kona jdk 11。
- OPEN:11：使用 open jdk 11。
        :type JdkVersion: str
        :param SecurityGroupIds: 安全组ID s
        :type SecurityGroupIds: list of str
        :param LogOutputConf: 日志输出配置
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param Description: 版本描述
        :type Description: str
        :param ImageCommand: 镜像命令
        :type ImageCommand: str
        :param ImageArgs: 镜像命令参数
        :type ImageArgs: list of str
        :param UseRegistryDefaultConfig: 是否添加默认注册中心配置
        :type UseRegistryDefaultConfig: bool
        :param SettingConfs: 挂载配置信息
        :type SettingConfs: list of MountedSettingConf
        :param Service: 应用访问设置
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param VersionId: 要回滚到的历史版本id
        :type VersionId: str
        :param PostStart: 启动后执行的脚本
        :type PostStart: str
        :param PreStop: 停止前执行的脚本
        :type PreStop: str
        :param Liveness: 存活探针配置
        :type Liveness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param Readiness: 就绪探针配置
        :type Readiness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param DeployStrategyConf: 分批发布策略配置
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`
        :param HorizontalAutoscaler: 弹性策略（已弃用，请使用弹性伸缩策略组合相关接口）
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param CronHorizontalAutoscaler: 定时弹性策略（已弃用，请使用弹性伸缩策略组合相关接口）
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param LogEnable: 是否启用log，1为启用，0为不启用
        :type LogEnable: int
        :param ConfEdited: （除开镜像配置）配置是否修改
        :type ConfEdited: bool
        :param SpeedUp: 是否开启应用加速
        :type SpeedUp: bool
        :param StartupProbe: 启动探针配置
        :type StartupProbe: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param OsFlavour: 操作系统版本；
当选择openjdk时，可选参数：
- ALPINE
- CENTOS
当选择konajdk时，可选参数：
- ALPINE
- TENCENTOS
        :type OsFlavour: str
        :param EnablePrometheusConf: metrics业务指标监控配置
        :type EnablePrometheusConf: :class:`tencentcloud.tem.v20210701.models.EnablePrometheusConf`
        :param EnableTracing: 1：开始自动apm采集（skywalking）；
0：关闭apm采集；
        :type EnableTracing: int
        :param EnableMetrics: 1：开始自动metrics采集（open-telemetry）；
0：关闭metrics采集；
        :type EnableMetrics: int
        :param TcrInstanceId: 镜像部署时，选择的tcr实例id
        :type TcrInstanceId: str
        :param RepoServer: 镜像部署时，选择的镜像服务器地址
        :type RepoServer: str
        :param RepoType: 镜像部署时，仓库类型：0：个人仓库；1：企业版；2：公共仓库；3：tem托管仓库；4：demo仓库
        :type RepoType: int
        """
        self.ApplicationId = None
        self.InitPodNum = None
        self.CpuSpec = None
        self.MemorySpec = None
        self.EnvironmentId = None
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
        self.UseRegistryDefaultConfig = None
        self.SettingConfs = None
        self.Service = None
        self.VersionId = None
        self.PostStart = None
        self.PreStop = None
        self.Liveness = None
        self.Readiness = None
        self.DeployStrategyConf = None
        self.HorizontalAutoscaler = None
        self.CronHorizontalAutoscaler = None
        self.LogEnable = None
        self.ConfEdited = None
        self.SpeedUp = None
        self.StartupProbe = None
        self.OsFlavour = None
        self.EnablePrometheusConf = None
        self.EnableTracing = None
        self.EnableMetrics = None
        self.TcrInstanceId = None
        self.RepoServer = None
        self.RepoType = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.InitPodNum = params.get("InitPodNum")
        self.CpuSpec = params.get("CpuSpec")
        self.MemorySpec = params.get("MemorySpec")
        self.EnvironmentId = params.get("EnvironmentId")
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
        self.UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("SettingConfs") is not None:
            self.SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self.SettingConfs.append(obj)
        if params.get("Service") is not None:
            self.Service = EksService()
            self.Service._deserialize(params.get("Service"))
        self.VersionId = params.get("VersionId")
        self.PostStart = params.get("PostStart")
        self.PreStop = params.get("PreStop")
        if params.get("Liveness") is not None:
            self.Liveness = HealthCheckConfig()
            self.Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self.Readiness = HealthCheckConfig()
            self.Readiness._deserialize(params.get("Readiness"))
        if params.get("DeployStrategyConf") is not None:
            self.DeployStrategyConf = DeployStrategyConf()
            self.DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("HorizontalAutoscaler") is not None:
            self.HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self.HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self.CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self.CronHorizontalAutoscaler.append(obj)
        self.LogEnable = params.get("LogEnable")
        self.ConfEdited = params.get("ConfEdited")
        self.SpeedUp = params.get("SpeedUp")
        if params.get("StartupProbe") is not None:
            self.StartupProbe = HealthCheckConfig()
            self.StartupProbe._deserialize(params.get("StartupProbe"))
        self.OsFlavour = params.get("OsFlavour")
        if params.get("EnablePrometheusConf") is not None:
            self.EnablePrometheusConf = EnablePrometheusConf()
            self.EnablePrometheusConf._deserialize(params.get("EnablePrometheusConf"))
        self.EnableTracing = params.get("EnableTracing")
        self.EnableMetrics = params.get("EnableMetrics")
        self.TcrInstanceId = params.get("TcrInstanceId")
        self.RepoServer = params.get("RepoServer")
        self.RepoType = params.get("RepoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployApplicationResponse(AbstractModel):
    """DeployApplication返回参数结构体

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


class DeployServiceBatchDetail(AbstractModel):
    """分批发布单批次详情

    """

    def __init__(self):
        r"""
        :param OldPodList: 旧实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OldPodList: :class:`tencentcloud.tem.v20210701.models.DeployServicePodDetail`
        :param NewPodList: 新实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NewPodList: :class:`tencentcloud.tem.v20210701.models.DeployServicePodDetail`
        :param BatchStatus: 当前批次状态："WaitForTimeExceed", "WaitForResume", "Deploying", "Finish", "NotStart"
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchStatus: str
        :param PodNum: 该批次预计旧实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PodNum: int
        :param BatchIndex: 批次id
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchIndex: int
        :param OldPods: 旧实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OldPods: list of DeployServicePodDetail
        :param NewPods: 新实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NewPods: list of DeployServicePodDetail
        :param NextBatchStartTime: =0：手动确认批次；>0：下一批次开始时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type NextBatchStartTime: int
        """
        self.OldPodList = None
        self.NewPodList = None
        self.BatchStatus = None
        self.PodNum = None
        self.BatchIndex = None
        self.OldPods = None
        self.NewPods = None
        self.NextBatchStartTime = None


    def _deserialize(self, params):
        if params.get("OldPodList") is not None:
            self.OldPodList = DeployServicePodDetail()
            self.OldPodList._deserialize(params.get("OldPodList"))
        if params.get("NewPodList") is not None:
            self.NewPodList = DeployServicePodDetail()
            self.NewPodList._deserialize(params.get("NewPodList"))
        self.BatchStatus = params.get("BatchStatus")
        self.PodNum = params.get("PodNum")
        self.BatchIndex = params.get("BatchIndex")
        if params.get("OldPods") is not None:
            self.OldPods = []
            for item in params.get("OldPods"):
                obj = DeployServicePodDetail()
                obj._deserialize(item)
                self.OldPods.append(obj)
        if params.get("NewPods") is not None:
            self.NewPods = []
            for item in params.get("NewPods"):
                obj = DeployServicePodDetail()
                obj._deserialize(item)
                self.NewPods.append(obj)
        self.NextBatchStartTime = params.get("NextBatchStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployServicePodDetail(AbstractModel):
    """分批发布单批次详情

    """

    def __init__(self):
        r"""
        :param PodId: pod Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PodId: str
        :param PodStatus: pod状态
注意：此字段可能返回 null，表示取不到有效值。
        :type PodStatus: list of str
        :param PodVersion: pod版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PodVersion: str
        :param CreateTime: pod创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Zone: pod所在可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param Webshell: webshell地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Webshell: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.PodId = None
        self.PodStatus = None
        self.PodVersion = None
        self.CreateTime = None
        self.Zone = None
        self.Webshell = None
        self.Status = None


    def _deserialize(self, params):
        self.PodId = params.get("PodId")
        self.PodStatus = params.get("PodStatus")
        self.PodVersion = params.get("PodVersion")
        self.CreateTime = params.get("CreateTime")
        self.Zone = params.get("Zone")
        self.Webshell = params.get("Webshell")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployStrategyConf(AbstractModel):
    """分批发布策略配置

    """

    def __init__(self):
        r"""
        :param TotalBatchCount: 总分批数
        :type TotalBatchCount: int
        :param BetaBatchNum: beta分批实例数
        :type BetaBatchNum: int
        :param DeployStrategyType: 分批策略：0-全自动，1-全手动，2-beta分批，beta批一定是手动的，3-首次发布
        :type DeployStrategyType: int
        :param BatchInterval: 每批暂停间隔
        :type BatchInterval: int
        :param MinAvailable: 最小可用实例数
        :type MinAvailable: int
        :param Force: 是否强制发布
        :type Force: bool
        """
        self.TotalBatchCount = None
        self.BetaBatchNum = None
        self.DeployStrategyType = None
        self.BatchInterval = None
        self.MinAvailable = None
        self.Force = None


    def _deserialize(self, params):
        self.TotalBatchCount = params.get("TotalBatchCount")
        self.BetaBatchNum = params.get("BetaBatchNum")
        self.DeployStrategyType = params.get("DeployStrategyType")
        self.BatchInterval = params.get("BatchInterval")
        self.MinAvailable = params.get("MinAvailable")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationAutoscalerListRequest(AbstractModel):
    """DescribeApplicationAutoscalerList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationAutoscalerListResponse(AbstractModel):
    """DescribeApplicationAutoscalerList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 弹性伸缩策略组合
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of Autoscaler
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = Autoscaler()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeApplicationInfoRequest(AbstractModel):
    """DescribeApplicationInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务版本ID
        :type ApplicationId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        """
        self.ApplicationId = None
        self.SourceChannel = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SourceChannel = params.get("SourceChannel")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationInfoResponse(AbstractModel):
    """DescribeApplicationInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20210701.models.TemServiceVersionInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TemServiceVersionInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationPodsRequest(AbstractModel):
    """DescribeApplicationPods请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境id
        :type EnvironmentId: str
        :param ApplicationId: 应用id
        :type ApplicationId: str
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
        self.EnvironmentId = None
        self.ApplicationId = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.PodName = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ApplicationId = params.get("ApplicationId")
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
        


class DescribeApplicationPodsResponse(AbstractModel):
    """DescribeApplicationPods返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
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


class DescribeApplicationServiceListRequest(AbstractModel):
    """DescribeApplicationServiceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: namespace id
        :type EnvironmentId: str
        :param ApplicationId: 服务ID
        :type ApplicationId: str
        :param SourceChannel: xx
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.ApplicationId = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ApplicationId = params.get("ApplicationId")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationServiceListResponse(AbstractModel):
    """DescribeApplicationServiceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 应用 EKS Service 列表
        :type Result: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = EksService()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationsRequest(AbstractModel):
    """DescribeApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 命名空间ID
        :type EnvironmentId: str
        :param Limit: 分页Limit
        :type Limit: int
        :param Offset: 分页offset
        :type Offset: int
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param Keyword: 搜索关键字
        :type Keyword: str
        :param Filters: 查询过滤器
        :type Filters: list of QueryFilter
        :param SortInfo: 排序字段
        :type SortInfo: :class:`tencentcloud.tem.v20210701.models.SortType`
        """
        self.EnvironmentId = None
        self.Limit = None
        self.Offset = None
        self.SourceChannel = None
        self.ApplicationId = None
        self.Keyword = None
        self.Filters = None
        self.SortInfo = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SourceChannel = params.get("SourceChannel")
        self.ApplicationId = params.get("ApplicationId")
        self.Keyword = params.get("Keyword")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("SortInfo") is not None:
            self.SortInfo = SortType()
            self.SortInfo._deserialize(params.get("SortInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsResponse(AbstractModel):
    """DescribeApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20210701.models.ServicePage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServicePage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationsStatusRequest(AbstractModel):
    """DescribeApplicationsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        """
        self.SourceChannel = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.SourceChannel = params.get("SourceChannel")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsStatusResponse(AbstractModel):
    """DescribeApplicationsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: list of ServiceVersionBrief
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = ServiceVersionBrief()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeConfigDataListPage(AbstractModel):
    """配置信息的分页列表

    """

    def __init__(self):
        r"""
        :param Records: 记录
        :type Records: list of ConfigData
        :param ContinueToken: 分页游标，用以查询下一页
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinueToken: str
        :param RemainingCount: 剩余数目
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainingCount: int
        """
        self.Records = None
        self.ContinueToken = None
        self.RemainingCount = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = ConfigData()
                obj._deserialize(item)
                self.Records.append(obj)
        self.ContinueToken = params.get("ContinueToken")
        self.RemainingCount = params.get("RemainingCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataListRequest(AbstractModel):
    """DescribeConfigDataList请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param ContinueToken: 查询游标
        :type ContinueToken: str
        :param Limit: 分页 limit
        :type Limit: int
        """
        self.EnvironmentId = None
        self.SourceChannel = None
        self.ContinueToken = None
        self.Limit = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.ContinueToken = params.get("ContinueToken")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataListResponse(AbstractModel):
    """DescribeConfigDataList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 配置列表
        :type Result: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataListPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DescribeConfigDataListPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigDataRequest(AbstractModel):
    """DescribeConfigData请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param Name: 配置名
        :type Name: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.Name = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataResponse(AbstractModel):
    """DescribeConfigData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 配置
        :type Result: :class:`tencentcloud.tem.v20210701.models.ConfigData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ConfigData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeDeployApplicationDetailRequest(AbstractModel):
    """DescribeDeployApplicationDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境id
        :type EnvironmentId: str
        :param VersionId: 版本部署id
        :type VersionId: str
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployApplicationDetailResponse(AbstractModel):
    """DescribeDeployApplicationDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 分批发布结果详情
        :type Result: :class:`tencentcloud.tem.v20210701.models.TemDeployApplicationDetailInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TemDeployApplicationDetailInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentRequest(AbstractModel):
    """DescribeEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 命名空间id
        :type EnvironmentId: str
        :param SourceChannel: 来源Channel
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentResponse(AbstractModel):
    """DescribeEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 环境信息
        :type Result: :class:`tencentcloud.tem.v20210701.models.NamespaceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = NamespaceInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentStatusRequest(AbstractModel):
    """DescribeEnvironmentStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentIds: 命名空间id
        :type EnvironmentIds: list of str
        :param SourceChannel: 来源Channel
        :type SourceChannel: int
        """
        self.EnvironmentIds = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentIds = params.get("EnvironmentIds")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentStatusResponse(AbstractModel):
    """DescribeEnvironmentStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回状态列表
        :type Result: list of NamespaceStatusInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = NamespaceStatusInfo()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页limit
        :type Limit: int
        :param Offset: 分页下标
        :type Offset: int
        :param SourceChannel: 来源source
        :type SourceChannel: int
        :param Filters: 查询过滤器
        :type Filters: list of QueryFilter
        :param SortInfo: 排序字段
        :type SortInfo: :class:`tencentcloud.tem.v20210701.models.SortType`
        :param EnvironmentId: 环境id
        :type EnvironmentId: str
        """
        self.Limit = None
        self.Offset = None
        self.SourceChannel = None
        self.Filters = None
        self.SortInfo = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SourceChannel = params.get("SourceChannel")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("SortInfo") is not None:
            self.SortInfo = SortType()
            self.SortInfo._deserialize(params.get("SortInfo"))
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20210701.models.NamespacePage`
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


class DescribeIngressRequest(AbstractModel):
    """DescribeIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param ClusterNamespace: 环境namespace
        :type ClusterNamespace: str
        :param IngressName: ingress 规则名
        :type IngressName: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.ClusterNamespace = None
        self.IngressName = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterNamespace = params.get("ClusterNamespace")
        self.IngressName = params.get("IngressName")
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
        :type Result: :class:`tencentcloud.tem.v20210701.models.IngressInfo`
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
        :param EnvironmentId: 环境 id
        :type EnvironmentId: str
        :param ClusterNamespace: 环境 namespace
        :type ClusterNamespace: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param IngressNames: ingress 规则名列表
        :type IngressNames: list of str
        """
        self.EnvironmentId = None
        self.ClusterNamespace = None
        self.SourceChannel = None
        self.IngressNames = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterNamespace = params.get("ClusterNamespace")
        self.SourceChannel = params.get("SourceChannel")
        self.IngressNames = params.get("IngressNames")
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


class DescribeLogConfigRequest(AbstractModel):
    """DescribeLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param Name: 配置名
        :type Name: str
        :param ApplicationId: 应用 ID
        :type ApplicationId: str
        """
        self.EnvironmentId = None
        self.Name = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogConfigResponse(AbstractModel):
    """DescribeLogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 配置
        :type Result: :class:`tencentcloud.tem.v20210701.models.LogConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = LogConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePagedLogConfigListRequest(AbstractModel):
    """DescribePagedLogConfigList请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param ApplicationId: 应用 ID
        :type ApplicationId: str
        :param ApplicationName: 应用名
        :type ApplicationName: str
        :param Name: 规则名
        :type Name: str
        :param Limit: 分页大小，默认 20
        :type Limit: int
        :param ContinueToken: 翻页游标
        :type ContinueToken: str
        """
        self.EnvironmentId = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.Name = None
        self.Limit = None
        self.ContinueToken = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.Name = params.get("Name")
        self.Limit = params.get("Limit")
        self.ContinueToken = params.get("ContinueToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePagedLogConfigListResponse(AbstractModel):
    """DescribePagedLogConfigList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 日志收集配置列表
        :type Result: :class:`tencentcloud.tem.v20210701.models.LogConfigListPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = LogConfigListPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeRelatedIngressesRequest(AbstractModel):
    """DescribeRelatedIngresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境 id
        :type EnvironmentId: str
        :param ClusterNamespace: 环境 namespace
        :type ClusterNamespace: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param ApplicationId: 应用 ID
        :type ApplicationId: str
        """
        self.EnvironmentId = None
        self.ClusterNamespace = None
        self.SourceChannel = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterNamespace = params.get("ClusterNamespace")
        self.SourceChannel = params.get("SourceChannel")
        self.ApplicationId = params.get("ApplicationId")
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
        


class DestroyConfigDataRequest(AbstractModel):
    """DestroyConfigData请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param Name: 配置名
        :type Name: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.Name = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyConfigDataResponse(AbstractModel):
    """DestroyConfigData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DestroyEnvironmentRequest(AbstractModel):
    """DestroyEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 命名空间ID
        :type EnvironmentId: str
        :param SourceChannel: Namespace
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyEnvironmentResponse(AbstractModel):
    """DestroyEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DestroyLogConfigRequest(AbstractModel):
    """DestroyLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param Name: 配置名
        :type Name: str
        :param ApplicationId: 应用 ID
        :type ApplicationId: str
        """
        self.EnvironmentId = None
        self.Name = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyLogConfigResponse(AbstractModel):
    """DestroyLogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DisableApplicationAutoscalerRequest(AbstractModel):
    """DisableApplicationAutoscaler请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param AutoscalerId: 弹性伸缩策略ID
        :type AutoscalerId: str
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.AutoscalerId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableApplicationAutoscalerResponse(AbstractModel):
    """DisableApplicationAutoscaler返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否成功
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
        :param ApplicationName: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
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
        :param ServicePortMappingList: 每种类型访问配置详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ServicePortMappingList: list of ServicePortMapping
        :param FlushAll: 刷新复写所有类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FlushAll: bool
        :param EnableRegistryNextDeploy: 1: 下次部署自动注入注册中心信息；0：不注入
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableRegistryNextDeploy: int
        :param ApplicationId: 返回应用id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param AllIpDone: 所有服务IP是否已经ready
注意：此字段可能返回 null，表示取不到有效值。
        :type AllIpDone: bool
        """
        self.Name = None
        self.Ports = None
        self.Yaml = None
        self.ApplicationName = None
        self.VersionName = None
        self.ClusterIp = None
        self.ExternalIp = None
        self.Type = None
        self.SubnetId = None
        self.LoadBalanceId = None
        self.PortMappings = None
        self.ServicePortMappingList = None
        self.FlushAll = None
        self.EnableRegistryNextDeploy = None
        self.ApplicationId = None
        self.AllIpDone = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Ports = params.get("Ports")
        self.Yaml = params.get("Yaml")
        self.ApplicationName = params.get("ApplicationName")
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
        if params.get("ServicePortMappingList") is not None:
            self.ServicePortMappingList = []
            for item in params.get("ServicePortMappingList"):
                obj = ServicePortMapping()
                obj._deserialize(item)
                self.ServicePortMappingList.append(obj)
        self.FlushAll = params.get("FlushAll")
        self.EnableRegistryNextDeploy = params.get("EnableRegistryNextDeploy")
        self.ApplicationId = params.get("ApplicationId")
        self.AllIpDone = params.get("AllIpDone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApplicationAutoscalerRequest(AbstractModel):
    """EnableApplicationAutoscaler请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param AutoscalerId: 弹性伸缩策略ID
        :type AutoscalerId: str
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.AutoscalerId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApplicationAutoscalerResponse(AbstractModel):
    """EnableApplicationAutoscaler返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否成功
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


class EnablePrometheusConf(AbstractModel):
    """开启prometheus监控配置

    """

    def __init__(self):
        r"""
        :param Port: 应用开放的监听端口
        :type Port: int
        :param Path: 业务指标暴露的url path
        :type Path: str
        """
        self.Port = None
        self.Path = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Path = params.get("Path")
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
        


class GenerateApplicationPackageDownloadUrlRequest(AbstractModel):
    """GenerateApplicationPackageDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param PkgName: 包名
        :type PkgName: str
        :param DeployVersion: 需要下载的包版本
        :type DeployVersion: str
        :param SourceChannel: 来源 channel
        :type SourceChannel: int
        """
        self.ApplicationId = None
        self.PkgName = None
        self.DeployVersion = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgName = params.get("PkgName")
        self.DeployVersion = params.get("DeployVersion")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateApplicationPackageDownloadUrlResponse(AbstractModel):
    """GenerateApplicationPackageDownloadUrl返回参数结构体

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
        


class HorizontalAutoscaler(AbstractModel):
    """弹性伸缩策略

    """

    def __init__(self):
        r"""
        :param MinReplicas: 最小实例数（可以不传）
        :type MinReplicas: int
        :param MaxReplicas: 最大实例数（可以不传）
        :type MaxReplicas: int
        :param Metrics: 指标度量
CPU（CPU使用率，%）
MEMORY（内存使用率，%）
CPU_CORE_USED（CPU使用量，core）
MEMORY_SIZE_USED(内存使用量，MiB)
NETWORK_BANDWIDTH_RECEIVE(网络入带宽，MBps)
NETWORK_BANDWIDTH_TRANSMIT(网络出带宽，MBps)
NETWORK_TRAFFIC_RECEIVE(网络入流量，MiB/s)
NETWORK_TRAFFIC_TRANSMIT(网络出流量，MiB/s)
NETWORK_PACKETS_RECEIVE(网络入包量，Count/s)
NETWORK_PACKETS_TRANSMIT(网络出包量，Count/s)
FS_IOPS_WRITE(磁盘写次数，Count/s)
FS_IOPS_READ(磁盘读次数，Count/s)
FS_SIZE_WRITE(磁盘写大小，MiB/s)
FS_SIZE_READ(磁盘读大小，MiB/s)
        :type Metrics: str
        :param Threshold: 阈值（整数）
        :type Threshold: int
        :param Enabled: 是否启用
        :type Enabled: bool
        :param DoubleThreshold: 阈值（小数，优先使用）
注意：此字段可能返回 null，表示取不到有效值。
        :type DoubleThreshold: float
        """
        self.MinReplicas = None
        self.MaxReplicas = None
        self.Metrics = None
        self.Threshold = None
        self.Enabled = None
        self.DoubleThreshold = None


    def _deserialize(self, params):
        self.MinReplicas = params.get("MinReplicas")
        self.MaxReplicas = params.get("MaxReplicas")
        self.Metrics = params.get("Metrics")
        self.Threshold = params.get("Threshold")
        self.Enabled = params.get("Enabled")
        self.DoubleThreshold = params.get("DoubleThreshold")
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
        :param EnvironmentId: 环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentId: str
        :param ClusterNamespace: 环境namespace
        :type ClusterNamespace: str
        :param AddressIPVersion: ip version
        :type AddressIPVersion: str
        :param IngressName: ingress name
        :type IngressName: str
        :param Rules: rules 配置
        :type Rules: list of IngressRule
        :param ClbId: clb ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClbId: str
        :param Tls: tls 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tls: list of IngressTls
        :param ClusterId: 环境集群ID
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
        :param RewriteType: 重定向模式，可选值：
- AUTO（自动重定向http到https）
- NONE（不使用重定向）
注意：此字段可能返回 null，表示取不到有效值。
        :type RewriteType: str
        """
        self.EnvironmentId = None
        self.ClusterNamespace = None
        self.AddressIPVersion = None
        self.IngressName = None
        self.Rules = None
        self.ClbId = None
        self.Tls = None
        self.ClusterId = None
        self.Vip = None
        self.CreateTime = None
        self.Mixed = None
        self.RewriteType = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterNamespace = params.get("ClusterNamespace")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.IngressName = params.get("IngressName")
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
        self.RewriteType = params.get("RewriteType")
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
        :type Http: :class:`tencentcloud.tem.v20210701.models.IngressRuleValue`
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
        :type Backend: :class:`tencentcloud.tem.v20210701.models.IngressRuleBackend`
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
        


class LogConfig(AbstractModel):
    """日志收集配置

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param InputType: 收集类型，container_stdout 为标准输出；container_file 为文件；
        :type InputType: str
        :param LogsetId: 日志集 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetId: str
        :param TopicId: 日志主题 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param LogType: 日志提取模式，minimalist_log 为单行全文；multiline_log 为多行全文；  fullregex_log 为单行正则； multiline_fullregex_log 为多行正则； json_log 为 json；
        :type LogType: str
        :param BeginningRegex: 首行正则表达式，当 LogType 为多行全文、多行正则时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginningRegex: str
        :param LogPath: 收集文件目录，当 InputType=container_file 时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type LogPath: str
        :param FilePattern: 收集文件名模式，当 InputType=container_file 时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePattern: str
        :param CreateDate: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param ModifyDate: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyDate: str
        :param ApplicationId: 应用 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 应用名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param ExtractRule: 导出规则
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtractRule: :class:`tencentcloud.tem.v20210701.models.LogConfigExtractRule`
        """
        self.Name = None
        self.InputType = None
        self.LogsetId = None
        self.TopicId = None
        self.LogType = None
        self.BeginningRegex = None
        self.LogPath = None
        self.FilePattern = None
        self.CreateDate = None
        self.ModifyDate = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.ExtractRule = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.InputType = params.get("InputType")
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.LogType = params.get("LogType")
        self.BeginningRegex = params.get("BeginningRegex")
        self.LogPath = params.get("LogPath")
        self.FilePattern = params.get("FilePattern")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        if params.get("ExtractRule") is not None:
            self.ExtractRule = LogConfigExtractRule()
            self.ExtractRule._deserialize(params.get("ExtractRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfigExtractRule(AbstractModel):
    """日志采集的导出规则配置

    """

    def __init__(self):
        r"""
        :param BeginningRegex: 首行正则表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginningRegex: str
        :param Keys: 提取结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of str
        :param FilterKeys: 过滤键
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterKeys: list of str
        :param FilterRegex: 过滤值
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterRegex: list of str
        :param LogRegex: 日志正则表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type LogRegex: str
        :param TimeKey: 时间字段
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeKey: str
        :param TimeFormat: 时间格式
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeFormat: str
        :param UnMatchUpload: 是否上传解析失败日志
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchUpload: str
        :param UnMatchedKey: 解析失败日志的键名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchedKey: str
        """
        self.BeginningRegex = None
        self.Keys = None
        self.FilterKeys = None
        self.FilterRegex = None
        self.LogRegex = None
        self.TimeKey = None
        self.TimeFormat = None
        self.UnMatchUpload = None
        self.UnMatchedKey = None


    def _deserialize(self, params):
        self.BeginningRegex = params.get("BeginningRegex")
        self.Keys = params.get("Keys")
        self.FilterKeys = params.get("FilterKeys")
        self.FilterRegex = params.get("FilterRegex")
        self.LogRegex = params.get("LogRegex")
        self.TimeKey = params.get("TimeKey")
        self.TimeFormat = params.get("TimeFormat")
        self.UnMatchUpload = params.get("UnMatchUpload")
        self.UnMatchedKey = params.get("UnMatchedKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfigListPage(AbstractModel):
    """LogConfig 列表结果

    """

    def __init__(self):
        r"""
        :param Records: 记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Records: list of LogConfig
        :param ContinueToken: 翻页游标
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinueToken: str
        """
        self.Records = None
        self.ContinueToken = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = LogConfig()
                obj._deserialize(item)
                self.Records.append(obj)
        self.ContinueToken = params.get("ContinueToken")
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
        


class ModifyApplicationAutoscalerRequest(AbstractModel):
    """ModifyApplicationAutoscaler请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param AutoscalerId: 弹性伸缩策略ID
        :type AutoscalerId: str
        :param Autoscaler: 弹性伸缩策略
        :type Autoscaler: :class:`tencentcloud.tem.v20210701.models.Autoscaler`
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.AutoscalerId = None
        self.Autoscaler = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.AutoscalerId = params.get("AutoscalerId")
        if params.get("Autoscaler") is not None:
            self.Autoscaler = Autoscaler()
            self.Autoscaler._deserialize(params.get("Autoscaler"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationAutoscalerResponse(AbstractModel):
    """ModifyApplicationAutoscaler返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否成功
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


class ModifyApplicationInfoRequest(AbstractModel):
    """ModifyApplicationInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param Description: 描述
        :type Description: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param EnableTracing: 是否开启调用链,（此参数已弃用）
        :type EnableTracing: int
        """
        self.ApplicationId = None
        self.Description = None
        self.SourceChannel = None
        self.EnableTracing = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.Description = params.get("Description")
        self.SourceChannel = params.get("SourceChannel")
        self.EnableTracing = params.get("EnableTracing")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationInfoResponse(AbstractModel):
    """ModifyApplicationInfo返回参数结构体

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


class ModifyApplicationReplicasRequest(AbstractModel):
    """ModifyApplicationReplicas请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param Replicas: 实例数量
        :type Replicas: int
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.Replicas = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.Replicas = params.get("Replicas")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationReplicasResponse(AbstractModel):
    """ModifyApplicationReplicas返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否成功
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


class ModifyApplicationServiceRequest(AbstractModel):
    """ModifyApplicationService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param Service: 全量访问方式设置
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param Data: 单条访问方式设置
        :type Data: :class:`tencentcloud.tem.v20210701.models.ServicePortMapping`
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.Service = None
        self.Data = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        if params.get("Service") is not None:
            self.Service = EksService()
            self.Service._deserialize(params.get("Service"))
        if params.get("Data") is not None:
            self.Data = ServicePortMapping()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationServiceResponse(AbstractModel):
    """ModifyApplicationService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否成功
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


class ModifyConfigDataRequest(AbstractModel):
    """ModifyConfigData请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param Name: 配置名
        :type Name: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param Data: 配置信息
        :type Data: list of Pair
        """
        self.EnvironmentId = None
        self.Name = None
        self.SourceChannel = None
        self.Data = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.SourceChannel = params.get("SourceChannel")
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
        


class ModifyConfigDataResponse(AbstractModel):
    """ModifyConfigData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 编辑是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyEnvironmentRequest(AbstractModel):
    """ModifyEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境id
        :type EnvironmentId: str
        :param EnvironmentName: 环境名称
        :type EnvironmentName: str
        :param Description: 环境描述
        :type Description: str
        :param Vpc: 私有网络名称
        :type Vpc: str
        :param SubnetIds: 子网网络
        :type SubnetIds: list of str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param EnvType: 环境类型：test、pre、prod
        :type EnvType: str
        """
        self.EnvironmentId = None
        self.EnvironmentName = None
        self.Description = None
        self.Vpc = None
        self.SubnetIds = None
        self.SourceChannel = None
        self.EnvType = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Description = params.get("Description")
        self.Vpc = params.get("Vpc")
        self.SubnetIds = params.get("SubnetIds")
        self.SourceChannel = params.get("SourceChannel")
        self.EnvType = params.get("EnvType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentResponse(AbstractModel):
    """ModifyEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 成功时为环境ID，失败为null
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


class ModifyIngressRequest(AbstractModel):
    """ModifyIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ingress: Ingress 规则配置
        :type Ingress: :class:`tencentcloud.tem.v20210701.models.IngressInfo`
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


class ModifyLogConfigRequest(AbstractModel):
    """ModifyLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param Name: 配置名
        :type Name: str
        :param Data: 日志收集配置信息
        :type Data: :class:`tencentcloud.tem.v20210701.models.LogConfig`
        :param ApplicationId: 应用 ID
        :type ApplicationId: str
        """
        self.EnvironmentId = None
        self.Name = None
        self.Data = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        if params.get("Data") is not None:
            self.Data = LogConfig()
            self.Data._deserialize(params.get("Data"))
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLogConfigResponse(AbstractModel):
    """ModifyLogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 编辑是否成功
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
        :param SecretDataName: 加密配置名称
        :type SecretDataName: str
        """
        self.ConfigDataName = None
        self.MountedPath = None
        self.Data = None
        self.SecretDataName = None


    def _deserialize(self, params):
        self.ConfigDataName = params.get("ConfigDataName")
        self.MountedPath = params.get("MountedPath")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self.Data.append(obj)
        self.SecretDataName = params.get("SecretDataName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceInfo(AbstractModel):
    """Namespace 基础信息

    """

    def __init__(self):
        r"""
        :param EnvironmentId: ID 信息
        :type EnvironmentId: str
        :param NamespaceName: 名字（已弃用）
        :type NamespaceName: str
        :param Region: 地域
        :type Region: str
        :param VpcId: vpc id
        :type VpcId: str
        :param SubnetIds: subnet id 数组
        :type SubnetIds: list of str
        :param Description: 描述
        :type Description: str
        :param CreatedDate: 创建时间
        :type CreatedDate: str
        :param EnvironmentName: 环境名称
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        :param ApmInstanceId: APM 资源 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApmInstanceId: str
        :param Locked: 环境是否上锁，1为上锁，0则未上锁
注意：此字段可能返回 null，表示取不到有效值。
        :type Locked: int
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param EnvType: 环境类型：test、pre、prod
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvType: str
        """
        self.EnvironmentId = None
        self.NamespaceName = None
        self.Region = None
        self.VpcId = None
        self.SubnetIds = None
        self.Description = None
        self.CreatedDate = None
        self.EnvironmentName = None
        self.ApmInstanceId = None
        self.Locked = None
        self.Tags = None
        self.EnvType = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.NamespaceName = params.get("NamespaceName")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.Description = params.get("Description")
        self.CreatedDate = params.get("CreatedDate")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApmInstanceId = params.get("ApmInstanceId")
        self.Locked = params.get("Locked")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.EnvType = params.get("EnvType")
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
        :param Current: 当前条目
注意：此字段可能返回 null，表示取不到有效值。
        :type Current: int
        """
        self.Records = None
        self.Total = None
        self.Size = None
        self.Pages = None
        self.Current = None


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
        self.Current = params.get("Current")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceStatusInfo(AbstractModel):
    """命名空间状态

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 命名空间id
        :type EnvironmentId: str
        :param EnvironmentName: 命名空间名称
        :type EnvironmentName: str
        :param ClusterId: TCB envId | EKS clusterId
        :type ClusterId: str
        :param ClusterStatus: 环境状态
        :type ClusterStatus: str
        :param EnvironmentStartingStatus: 环境启动状态（不在启动中为null）
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentStartingStatus: :class:`tencentcloud.tem.v20210701.models.TemEnvironmentStartingStatus`
        :param EnvironmentStoppingStatus: 环境停止状态（不在停止中为null）
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentStoppingStatus: :class:`tencentcloud.tem.v20210701.models.TemEnvironmentStoppingStatus`
        """
        self.EnvironmentId = None
        self.EnvironmentName = None
        self.ClusterId = None
        self.ClusterStatus = None
        self.EnvironmentStartingStatus = None
        self.EnvironmentStoppingStatus = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterStatus = params.get("ClusterStatus")
        if params.get("EnvironmentStartingStatus") is not None:
            self.EnvironmentStartingStatus = TemEnvironmentStartingStatus()
            self.EnvironmentStartingStatus._deserialize(params.get("EnvironmentStartingStatus"))
        if params.get("EnvironmentStoppingStatus") is not None:
            self.EnvironmentStoppingStatus = TemEnvironmentStoppingStatus()
            self.EnvironmentStoppingStatus._deserialize(params.get("EnvironmentStoppingStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """node信息

    """

    def __init__(self):
        r"""
        :param Name: node名字
        :type Name: str
        :param Zone: node可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param SubnetId: node子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param AvailableIpCount: 可用IP数
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableIpCount: str
        :param Cidr: cidr块
注意：此字段可能返回 null，表示取不到有效值。
        :type Cidr: str
        """
        self.Name = None
        self.Zone = None
        self.SubnetId = None
        self.AvailableIpCount = None
        self.Cidr = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Zone = params.get("Zone")
        self.SubnetId = params.get("SubnetId")
        self.AvailableIpCount = params.get("AvailableIpCount")
        self.Cidr = params.get("Cidr")
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
        :param Key: 键
        :type Key: str
        :param Value: 值
        :type Value: str
        :param Type: 类型，default 为自定义，reserved 为系统变量，referenced 为引用配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Config: 配置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: str
        :param Secret: 加密配置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Secret: str
        """
        self.Key = None
        self.Value = None
        self.Type = None
        self.Config = None
        self.Secret = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Type = params.get("Type")
        self.Config = params.get("Config")
        self.Secret = params.get("Secret")
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
        :param ServiceName: k8s service名称
        :type ServiceName: str
        """
        self.Port = None
        self.TargetPort = None
        self.Protocol = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.TargetPort = params.get("TargetPort")
        self.Protocol = params.get("Protocol")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilter(AbstractModel):
    """查询过滤器

    """

    def __init__(self):
        r"""
        :param Name: 查询字段名称
        :type Name: str
        :param Value: 查询字段值
        :type Value: list of str
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartApplicationPodRequest(AbstractModel):
    """RestartApplicationPod请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境id
        :type EnvironmentId: str
        :param ApplicationId: 应用id
        :type ApplicationId: str
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
        self.EnvironmentId = None
        self.ApplicationId = None
        self.PodName = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ApplicationId = params.get("ApplicationId")
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
        


class RestartApplicationPodResponse(AbstractModel):
    """RestartApplicationPod返回参数结构体

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


class RestartApplicationRequest(AbstractModel):
    """RestartApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        """
        self.ApplicationId = None
        self.SourceChannel = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SourceChannel = params.get("SourceChannel")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartApplicationResponse(AbstractModel):
    """RestartApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ResumeDeployApplicationRequest(AbstractModel):
    """ResumeDeployApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 需要开始下一批次的服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境id
        :type EnvironmentId: str
        """
        self.ApplicationId = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeDeployApplicationResponse(AbstractModel):
    """ResumeDeployApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RevertDeployApplicationRequest(AbstractModel):
    """RevertDeployApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 需要回滚的服务id
        :type ApplicationId: str
        :param EnvironmentId: 需要回滚的服务所在环境id
        :type EnvironmentId: str
        """
        self.ApplicationId = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevertDeployApplicationResponse(AbstractModel):
    """RevertDeployApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RollingUpdateApplicationByVersionRequest(AbstractModel):
    """RollingUpdateApplicationByVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param DeployVersion: 更新版本，IMAGE 部署为 tag 值；JAR/WAR 部署 为 Version
        :type DeployVersion: str
        :param PackageName: JAR/WAR 包名，仅 JAR/WAR 部署时必填
        :type PackageName: str
        :param From: 请求来源平台，含 IntelliJ，Coding
        :type From: str
        :param DeployStrategyType: 部署策略，AUTO 为全自动；BETA 为小批量验证后自动；MANUAL 为全手动；
        :type DeployStrategyType: str
        :param TotalBatchCount: 发布批次数
        :type TotalBatchCount: int
        :param BatchInterval: 批次间隔时间
        :type BatchInterval: int
        :param BetaBatchNum: 小批量验证批次的实例数
        :type BetaBatchNum: int
        :param MinAvailable: 发布过程中保障的最小可用实例数
        :type MinAvailable: int
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.DeployVersion = None
        self.PackageName = None
        self.From = None
        self.DeployStrategyType = None
        self.TotalBatchCount = None
        self.BatchInterval = None
        self.BetaBatchNum = None
        self.MinAvailable = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.DeployVersion = params.get("DeployVersion")
        self.PackageName = params.get("PackageName")
        self.From = params.get("From")
        self.DeployStrategyType = params.get("DeployStrategyType")
        self.TotalBatchCount = params.get("TotalBatchCount")
        self.BatchInterval = params.get("BatchInterval")
        self.BetaBatchNum = params.get("BetaBatchNum")
        self.MinAvailable = params.get("MinAvailable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollingUpdateApplicationByVersionResponse(AbstractModel):
    """RollingUpdateApplicationByVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 版本ID
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RunVersionPod(AbstractModel):
    """应用实例

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
        :param Ready: pod是否就绪
注意：此字段可能返回 null，表示取不到有效值。
        :type Ready: bool
        :param ContainerState: 容器状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerState: str
        :param NodeInfo: 实例所在节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInfo: :class:`tencentcloud.tem.v20210701.models.NodeInfo`
        :param StartTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param Unhealthy: 是否健康
注意：此字段可能返回 null，表示取不到有效值。
        :type Unhealthy: bool
        :param UnhealthyWarningMsg: 不健康时的提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UnhealthyWarningMsg: str
        :param VersionId: 版本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: str
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        """
        self.Webshell = None
        self.PodId = None
        self.Status = None
        self.CreateTime = None
        self.PodIp = None
        self.Zone = None
        self.DeployVersion = None
        self.RestartCount = None
        self.Ready = None
        self.ContainerState = None
        self.NodeInfo = None
        self.StartTime = None
        self.Unhealthy = None
        self.UnhealthyWarningMsg = None
        self.VersionId = None
        self.ApplicationName = None


    def _deserialize(self, params):
        self.Webshell = params.get("Webshell")
        self.PodId = params.get("PodId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.PodIp = params.get("PodIp")
        self.Zone = params.get("Zone")
        self.DeployVersion = params.get("DeployVersion")
        self.RestartCount = params.get("RestartCount")
        self.Ready = params.get("Ready")
        self.ContainerState = params.get("ContainerState")
        if params.get("NodeInfo") is not None:
            self.NodeInfo = NodeInfo()
            self.NodeInfo._deserialize(params.get("NodeInfo"))
        self.StartTime = params.get("StartTime")
        self.Unhealthy = params.get("Unhealthy")
        self.UnhealthyWarningMsg = params.get("UnhealthyWarningMsg")
        self.VersionId = params.get("VersionId")
        self.ApplicationName = params.get("ApplicationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePage(AbstractModel):
    """服务分页

    """

    def __init__(self):
        r"""
        :param Records: 条目
        :type Records: list of TemService
        :param Total: 总数
        :type Total: int
        :param Size: 条目
        :type Size: int
        :param Pages: 页数
        :type Pages: int
        :param Current: 当前条数
注意：此字段可能返回 null，表示取不到有效值。
        :type Current: int
        """
        self.Records = None
        self.Total = None
        self.Size = None
        self.Pages = None
        self.Current = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = TemService()
                obj._deserialize(item)
                self.Records.append(obj)
        self.Total = params.get("Total")
        self.Size = params.get("Size")
        self.Pages = params.get("Pages")
        self.Current = params.get("Current")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePortMapping(AbstractModel):
    """端口映射详细信息结构体

    """

    def __init__(self):
        r"""
        :param Type: 服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param ServiceName: 服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param ClusterIp: 集群内访问vip
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIp: str
        :param ExternalIp: 集群外方位vip
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalIp: str
        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param LoadBalanceId: LoadBalance Id
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalanceId: str
        :param Yaml: yaml 内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param Ports: 暴露端口列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Ports: list of int
        :param PortMappingItemList: 端口映射数组
注意：此字段可能返回 null，表示取不到有效值。
        :type PortMappingItemList: list of ServicePortMappingItem
        """
        self.Type = None
        self.ServiceName = None
        self.ClusterIp = None
        self.ExternalIp = None
        self.SubnetId = None
        self.VpcId = None
        self.LoadBalanceId = None
        self.Yaml = None
        self.Ports = None
        self.PortMappingItemList = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.ServiceName = params.get("ServiceName")
        self.ClusterIp = params.get("ClusterIp")
        self.ExternalIp = params.get("ExternalIp")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.LoadBalanceId = params.get("LoadBalanceId")
        self.Yaml = params.get("Yaml")
        self.Ports = params.get("Ports")
        if params.get("PortMappingItemList") is not None:
            self.PortMappingItemList = []
            for item in params.get("PortMappingItemList"):
                obj = ServicePortMappingItem()
                obj._deserialize(item)
                self.PortMappingItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePortMappingItem(AbstractModel):
    """服务端口映射条目

    """

    def __init__(self):
        r"""
        :param Port: 应用访问端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param TargetPort: 应用监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetPort: int
        :param Protocol: 协议类型
注意：此字段可能返回 null，表示取不到有效值。
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
        


class ServiceVersionBrief(AbstractModel):
    """服务版本信息列表

    """

    def __init__(self):
        r"""
        :param VersionName: 版本名称
        :type VersionName: str
        :param Status: 状态
        :type Status: str
        :param EnableEs: 是否启动弹性 -- 已废弃
        :type EnableEs: int
        :param CurrentInstances: 当前实例
        :type CurrentInstances: int
        :param VersionId: version的id
        :type VersionId: str
        :param LogOutputConf: 日志输出配置 -- 已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param ExpectedInstances: 期望实例
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectedInstances: int
        :param DeployMode: 部署方式
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMode: str
        :param BuildTaskId: 建构任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildTaskId: str
        :param EnvironmentId: 环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentId: str
        :param EnvironmentName: 环境name
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        :param ApplicationId: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 服务name
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param UnderDeploying: 是否正在发布中
注意：此字段可能返回 null，表示取不到有效值。
        :type UnderDeploying: bool
        :param BatchDeployStatus: 分批次部署状态
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchDeployStatus: str
        :param Zones: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: list of str
        :param NodeInfos: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInfos: list of NodeInfo
        :param PodList: 实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param WorkloadInfo: 工作负载信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadInfo: :class:`tencentcloud.tem.v20210701.models.WorkloadInfo`
        :param CreateDate: 创建日期
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        """
        self.VersionName = None
        self.Status = None
        self.EnableEs = None
        self.CurrentInstances = None
        self.VersionId = None
        self.LogOutputConf = None
        self.ExpectedInstances = None
        self.DeployMode = None
        self.BuildTaskId = None
        self.EnvironmentId = None
        self.EnvironmentName = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.UnderDeploying = None
        self.BatchDeployStatus = None
        self.Zones = None
        self.NodeInfos = None
        self.PodList = None
        self.WorkloadInfo = None
        self.CreateDate = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.Status = params.get("Status")
        self.EnableEs = params.get("EnableEs")
        self.CurrentInstances = params.get("CurrentInstances")
        self.VersionId = params.get("VersionId")
        if params.get("LogOutputConf") is not None:
            self.LogOutputConf = LogOutputConf()
            self.LogOutputConf._deserialize(params.get("LogOutputConf"))
        self.ExpectedInstances = params.get("ExpectedInstances")
        self.DeployMode = params.get("DeployMode")
        self.BuildTaskId = params.get("BuildTaskId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.UnderDeploying = params.get("UnderDeploying")
        self.BatchDeployStatus = params.get("BatchDeployStatus")
        self.Zones = params.get("Zones")
        if params.get("NodeInfos") is not None:
            self.NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfos.append(obj)
        if params.get("PodList") is not None:
            self.PodList = DescribeRunPodPage()
            self.PodList._deserialize(params.get("PodList"))
        if params.get("WorkloadInfo") is not None:
            self.WorkloadInfo = WorkloadInfo()
            self.WorkloadInfo._deserialize(params.get("WorkloadInfo"))
        self.CreateDate = params.get("CreateDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortType(AbstractModel):
    """查询过滤器

    """

    def __init__(self):
        r"""
        :param Key: 排序字段名称
        :type Key: str
        :param Type: 0：升序，1：倒序
        :type Type: int
        """
        self.Key = None
        self.Type = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopApplicationRequest(AbstractModel):
    """StopApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        :param EnvironmentId: 环境ID
        :type EnvironmentId: str
        """
        self.ApplicationId = None
        self.SourceChannel = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SourceChannel = params.get("SourceChannel")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopApplicationResponse(AbstractModel):
    """StopApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


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
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemDeployApplicationDetailInfo(AbstractModel):
    """分批发布详情

    """

    def __init__(self):
        r"""
        :param DeployStrategyConf: 分批发布策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Status: 当前状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param BetaBatchDetail: beta分批详情
注意：此字段可能返回 null，表示取不到有效值。
        :type BetaBatchDetail: :class:`tencentcloud.tem.v20210701.models.DeployServiceBatchDetail`
        :param OtherBatchDetail: 其他分批详情
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherBatchDetail: list of DeployServiceBatchDetail
        :param OldVersionPodList: 老版本pod列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OldVersionPodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param CurrentBatchIndex: 当前批次id
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentBatchIndex: int
        :param ErrorMessage: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param CurrentBatchStatus: 当前批次状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentBatchStatus: str
        :param NewDeployVersion: 新版本version
注意：此字段可能返回 null，表示取不到有效值。
        :type NewDeployVersion: str
        :param OldDeployVersion: 旧版本version
注意：此字段可能返回 null，表示取不到有效值。
        :type OldDeployVersion: str
        :param NewVersionPackageInfo: 包名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NewVersionPackageInfo: str
        :param NextBatchStartTime: 下一批次开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type NextBatchStartTime: int
        """
        self.DeployStrategyConf = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.BetaBatchDetail = None
        self.OtherBatchDetail = None
        self.OldVersionPodList = None
        self.CurrentBatchIndex = None
        self.ErrorMessage = None
        self.CurrentBatchStatus = None
        self.NewDeployVersion = None
        self.OldDeployVersion = None
        self.NewVersionPackageInfo = None
        self.NextBatchStartTime = None


    def _deserialize(self, params):
        if params.get("DeployStrategyConf") is not None:
            self.DeployStrategyConf = DeployStrategyConf()
            self.DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        if params.get("BetaBatchDetail") is not None:
            self.BetaBatchDetail = DeployServiceBatchDetail()
            self.BetaBatchDetail._deserialize(params.get("BetaBatchDetail"))
        if params.get("OtherBatchDetail") is not None:
            self.OtherBatchDetail = []
            for item in params.get("OtherBatchDetail"):
                obj = DeployServiceBatchDetail()
                obj._deserialize(item)
                self.OtherBatchDetail.append(obj)
        if params.get("OldVersionPodList") is not None:
            self.OldVersionPodList = DescribeRunPodPage()
            self.OldVersionPodList._deserialize(params.get("OldVersionPodList"))
        self.CurrentBatchIndex = params.get("CurrentBatchIndex")
        self.ErrorMessage = params.get("ErrorMessage")
        self.CurrentBatchStatus = params.get("CurrentBatchStatus")
        self.NewDeployVersion = params.get("NewDeployVersion")
        self.OldDeployVersion = params.get("OldDeployVersion")
        self.NewVersionPackageInfo = params.get("NewVersionPackageInfo")
        self.NextBatchStartTime = params.get("NextBatchStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemEnvironmentStartingStatus(AbstractModel):
    """环境启动进程（只统计由环境启动操作触发的应用数量）

    """

    def __init__(self):
        r"""
        :param ApplicationNumNeedToStart: 需要启动的应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationNumNeedToStart: int
        :param StartedApplicationNum: 已经启动的应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StartedApplicationNum: int
        """
        self.ApplicationNumNeedToStart = None
        self.StartedApplicationNum = None


    def _deserialize(self, params):
        self.ApplicationNumNeedToStart = params.get("ApplicationNumNeedToStart")
        self.StartedApplicationNum = params.get("StartedApplicationNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemEnvironmentStoppingStatus(AbstractModel):
    """环境停止进程（只统计由环境停止操作触发的应用数量）

    """

    def __init__(self):
        r"""
        :param ApplicationNumNeedToStop: 需要停止的应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationNumNeedToStop: int
        :param StoppedApplicationNum: 已经停止的应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppedApplicationNum: int
        """
        self.ApplicationNumNeedToStop = None
        self.StoppedApplicationNum = None


    def _deserialize(self, params):
        self.ApplicationNumNeedToStop = params.get("ApplicationNumNeedToStop")
        self.StoppedApplicationNum = params.get("StoppedApplicationNum")
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
        :param EnvironmentId: 环境id
        :type EnvironmentId: str
        :param Channel: 渠道
        :type Channel: str
        :param EnvironmentName: 环境名称
        :type EnvironmentName: str
        :param Region: 区域名称
        :type Region: str
        :param Description: 环境描述
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
        :param ApplicationNum: 应用数
        :type ApplicationNum: int
        :param RunInstancesNum: 运行实例数
        :type RunInstancesNum: int
        :param SubnetId: 子网络
        :type SubnetId: str
        :param ClusterStatus: 环境集群 status
        :type ClusterStatus: str
        :param EnableTswTraceService: 是否开启tsw
        :type EnableTswTraceService: bool
        :param Locked: 环境锁，1为上锁，0则为上锁
        :type Locked: int
        :param AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param Uin: 用户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param SubAccountUin: 用户SubAccountUin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param HasAuthority: 资源是否有权限
注意：此字段可能返回 null，表示取不到有效值。
        :type HasAuthority: bool
        :param EnvType: 环境类型: test、pre、prod
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvType: str
        :param RegionId: 地域码
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        """
        self.EnvironmentId = None
        self.Channel = None
        self.EnvironmentName = None
        self.Region = None
        self.Description = None
        self.Status = None
        self.Vpc = None
        self.CreateDate = None
        self.ModifyDate = None
        self.Modifier = None
        self.Creator = None
        self.ApplicationNum = None
        self.RunInstancesNum = None
        self.SubnetId = None
        self.ClusterStatus = None
        self.EnableTswTraceService = None
        self.Locked = None
        self.AppId = None
        self.Uin = None
        self.SubAccountUin = None
        self.ClusterId = None
        self.Tags = None
        self.HasAuthority = None
        self.EnvType = None
        self.RegionId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Channel = params.get("Channel")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Region = params.get("Region")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        self.Vpc = params.get("Vpc")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.Modifier = params.get("Modifier")
        self.Creator = params.get("Creator")
        self.ApplicationNum = params.get("ApplicationNum")
        self.RunInstancesNum = params.get("RunInstancesNum")
        self.SubnetId = params.get("SubnetId")
        self.ClusterStatus = params.get("ClusterStatus")
        self.EnableTswTraceService = params.get("EnableTswTraceService")
        self.Locked = params.get("Locked")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.SubAccountUin = params.get("SubAccountUin")
        self.ClusterId = params.get("ClusterId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.HasAuthority = params.get("HasAuthority")
        self.EnvType = params.get("EnvType")
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemService(AbstractModel):
    """服务

    """

    def __init__(self):
        r"""
        :param ApplicationId: 主键
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param EnvironmentId: 命名空间id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentId: str
        :param CreateDate: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param ModifyDate: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyDate: str
        :param Modifier: 修改人
注意：此字段可能返回 null，表示取不到有效值。
        :type Modifier: str
        :param Creator: 创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param RepoType: tcr个人版or企业版
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoType: int
        :param InstanceId: 企业版实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param RepoName: 镜像仓库名
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoName: str
        :param CodingLanguage: 编程语言
注意：此字段可能返回 null，表示取不到有效值。
        :type CodingLanguage: str
        :param DeployMode: 部署方式
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMode: str
        :param EnvironmentName: 环境名称
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        :param ActiveVersions: 服务当前运行环境的实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveVersions: list of ServiceVersionBrief
        :param EnableTracing: 是否启用链路追踪
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableTracing: int
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param HasAuthority: 是否有资源权限
注意：此字段可能返回 null，表示取不到有效值。
        :type HasAuthority: bool
        """
        self.ApplicationId = None
        self.ApplicationName = None
        self.Description = None
        self.EnvironmentId = None
        self.CreateDate = None
        self.ModifyDate = None
        self.Modifier = None
        self.Creator = None
        self.RepoType = None
        self.InstanceId = None
        self.RepoName = None
        self.CodingLanguage = None
        self.DeployMode = None
        self.EnvironmentName = None
        self.ActiveVersions = None
        self.EnableTracing = None
        self.Tags = None
        self.HasAuthority = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.Description = params.get("Description")
        self.EnvironmentId = params.get("EnvironmentId")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.Modifier = params.get("Modifier")
        self.Creator = params.get("Creator")
        self.RepoType = params.get("RepoType")
        self.InstanceId = params.get("InstanceId")
        self.RepoName = params.get("RepoName")
        self.CodingLanguage = params.get("CodingLanguage")
        self.DeployMode = params.get("DeployMode")
        self.EnvironmentName = params.get("EnvironmentName")
        if params.get("ActiveVersions") is not None:
            self.ActiveVersions = []
            for item in params.get("ActiveVersions"):
                obj = ServiceVersionBrief()
                obj._deserialize(item)
                self.ActiveVersions.append(obj)
        self.EnableTracing = params.get("EnableTracing")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.HasAuthority = params.get("HasAuthority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemServiceVersionInfo(AbstractModel):
    """版本信息

    """

    def __init__(self):
        r"""
        :param VersionId: 主键
        :type VersionId: str
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param DeployMode: 部署方式
        :type DeployMode: str
        :param JdkVersion: jdk版本
        :type JdkVersion: str
        :param Description: 描述
        :type Description: str
        :param DeployVersion: 部署版本
        :type DeployVersion: str
        :param PublishMode: 发布方式
        :type PublishMode: str
        :param JvmOpts: 启动参数
        :type JvmOpts: str
        :param InitPodNum: 初始实例
        :type InitPodNum: int
        :param CpuSpec: cpu规格
        :type CpuSpec: float
        :param MemorySpec: 内存规格
        :type MemorySpec: float
        :param ImgRepo: 镜像路径
        :type ImgRepo: str
        :param ImgName: 镜像名称
        :type ImgName: str
        :param ImgVersion: 镜像版本
        :type ImgVersion: str
        :param EsInfo: 弹性配置
注意：此字段可能返回 null，表示取不到有效值。
        :type EsInfo: :class:`tencentcloud.tem.v20210701.models.EsInfo`
        :param EnvConf: 环境配置
        :type EnvConf: list of Pair
        :param StorageConfs: 存储配置
        :type StorageConfs: list of StorageConf
        :param Status: 运行状态
        :type Status: str
        :param Vpc: 私有网络
        :type Vpc: str
        :param SubnetId: 子网网络
        :type SubnetId: str
        :param CreateDate: 创建时间
        :type CreateDate: str
        :param ModifyDate: 修改时间
        :type ModifyDate: str
        :param StorageMountConfs: 挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageMountConfs: list of StorageMountConf
        :param VersionName: 版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param LogOutputConf: 日志输出配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param ApplicationName: 服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param ApplicationDescription: 服务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationDescription: str
        :param EnvironmentName: 环境名称
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        :param EnvironmentId: 环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentId: str
        :param PublicDomain: 公网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicDomain: str
        :param EnablePublicAccess: 是否开通公网访问
注意：此字段可能返回 null，表示取不到有效值。
        :type EnablePublicAccess: bool
        :param CurrentInstances: 现有的实例
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentInstances: int
        :param ExpectedInstances: 期望的实例
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectedInstances: int
        :param CodingLanguage: 编程语言
注意：此字段可能返回 null，表示取不到有效值。
        :type CodingLanguage: str
        :param PkgName: 程序包名
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgName: str
        :param EsEnable: 是否启用弹性伸缩
注意：此字段可能返回 null，表示取不到有效值。
        :type EsEnable: int
        :param EsStrategy: 弹性策略
注意：此字段可能返回 null，表示取不到有效值。
        :type EsStrategy: int
        :param ImageTag: 镜像tag
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTag: str
        :param LogEnable: 是否启用log
注意：此字段可能返回 null，表示取不到有效值。
        :type LogEnable: int
        :param MinAliveInstances: 最小实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinAliveInstances: str
        :param SecurityGroupIds: 安全组
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        :param ImageCommand: 镜像命令
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageCommand: str
        :param ImageArgs: 镜像命令参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageArgs: list of str
        :param UseRegistryDefaultConfig: 是否使用默认注册中心配置
注意：此字段可能返回 null，表示取不到有效值。
        :type UseRegistryDefaultConfig: bool
        :param Service: eks 访问设置
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param SettingConfs: 挂载配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SettingConfs: list of MountedSettingConf
        :param LogConfs: log path数组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LogConfs: list of str
        :param PostStart: 启动后立即执行的脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type PostStart: str
        :param PreStop: 停止前执行的脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type PreStop: str
        :param Liveness: 存活探针配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Liveness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param Readiness: 就绪探针配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Readiness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param HorizontalAutoscaler: 弹性策略
注意：此字段可能返回 null，表示取不到有效值。
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param CronHorizontalAutoscaler: 定时弹性策略
注意：此字段可能返回 null，表示取不到有效值。
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param Zones: 应用实际可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: list of str
        :param LastDeployDate: 最新部署时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastDeployDate: str
        :param LastDeploySuccessDate: 最新部署成功时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastDeploySuccessDate: str
        :param NodeInfos: 应用所在node信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInfos: list of NodeInfo
        :param ImageType: image类型 -0 为demo -1为正常image
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageType: int
        :param EnableTracing: 是否启用调用链组件
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableTracing: int
        :param EnableTracingReport: 是否开启调用链上报，只有 EnableTracing=1 时生效（参数已弃用）
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableTracingReport: int
        :param RepoType: 镜像类型：0-个人镜像、1-企业镜像、2-公有镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoType: int
        :param BatchDeployStatus: 分批发布子状态：batch_updating、batch_updating_waiting_confirm
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchDeployStatus: str
        :param ApmInstanceId: APM 资源 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApmInstanceId: str
        :param WorkloadInfo: 工作负载信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadInfo: :class:`tencentcloud.tem.v20210701.models.WorkloadInfo`
        :param SpeedUp: 是否启用应用加速
注意：此字段可能返回 null，表示取不到有效值。
        :type SpeedUp: bool
        :param StartupProbe: 启动检测探针配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StartupProbe: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param OsFlavour: 操作系统版本，可选参数：
- ALPINE
- CENTOS
注意：此字段可能返回 null，表示取不到有效值。
        :type OsFlavour: str
        :param RepoServer: 镜像仓库server
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoServer: str
        :param UnderDeploying: 是否正在发布中
注意：此字段可能返回 null，表示取不到有效值。
        :type UnderDeploying: bool
        :param EnablePrometheusConf: 监控业务指标监控
注意：此字段可能返回 null，表示取不到有效值。
        :type EnablePrometheusConf: :class:`tencentcloud.tem.v20210701.models.EnablePrometheusConf`
        :param StoppedManually: 是否为手动停止
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppedManually: bool
        :param TcrInstanceId: tcr实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TcrInstanceId: str
        :param EnableMetrics: 1：开始自动metrics采集（open-telemetry）；
0：关闭metrics采集；
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableMetrics: int
        :param AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param SubAccountUin: 用户SubAccountUin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param Uin: 用户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param GroupId: 应用分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param EnableRegistry: 是否启用注册中心
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableRegistry: int
        :param AutoscalerList: 弹性伸缩数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalerList: list of Autoscaler
        :param Modifier: 修改人
注意：此字段可能返回 null，表示取不到有效值。
        :type Modifier: str
        :param Creator: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param DeployStrategyConf: 部署策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`
        :param PodList: 实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param ConfEdited: 发布时配置是否有修改
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfEdited: bool
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.VersionId = None
        self.ApplicationId = None
        self.DeployMode = None
        self.JdkVersion = None
        self.Description = None
        self.DeployVersion = None
        self.PublishMode = None
        self.JvmOpts = None
        self.InitPodNum = None
        self.CpuSpec = None
        self.MemorySpec = None
        self.ImgRepo = None
        self.ImgName = None
        self.ImgVersion = None
        self.EsInfo = None
        self.EnvConf = None
        self.StorageConfs = None
        self.Status = None
        self.Vpc = None
        self.SubnetId = None
        self.CreateDate = None
        self.ModifyDate = None
        self.StorageMountConfs = None
        self.VersionName = None
        self.LogOutputConf = None
        self.ApplicationName = None
        self.ApplicationDescription = None
        self.EnvironmentName = None
        self.EnvironmentId = None
        self.PublicDomain = None
        self.EnablePublicAccess = None
        self.CurrentInstances = None
        self.ExpectedInstances = None
        self.CodingLanguage = None
        self.PkgName = None
        self.EsEnable = None
        self.EsStrategy = None
        self.ImageTag = None
        self.LogEnable = None
        self.MinAliveInstances = None
        self.SecurityGroupIds = None
        self.ImageCommand = None
        self.ImageArgs = None
        self.UseRegistryDefaultConfig = None
        self.Service = None
        self.SettingConfs = None
        self.LogConfs = None
        self.PostStart = None
        self.PreStop = None
        self.Liveness = None
        self.Readiness = None
        self.HorizontalAutoscaler = None
        self.CronHorizontalAutoscaler = None
        self.Zones = None
        self.LastDeployDate = None
        self.LastDeploySuccessDate = None
        self.NodeInfos = None
        self.ImageType = None
        self.EnableTracing = None
        self.EnableTracingReport = None
        self.RepoType = None
        self.BatchDeployStatus = None
        self.ApmInstanceId = None
        self.WorkloadInfo = None
        self.SpeedUp = None
        self.StartupProbe = None
        self.OsFlavour = None
        self.RepoServer = None
        self.UnderDeploying = None
        self.EnablePrometheusConf = None
        self.StoppedManually = None
        self.TcrInstanceId = None
        self.EnableMetrics = None
        self.AppId = None
        self.SubAccountUin = None
        self.Uin = None
        self.Region = None
        self.GroupId = None
        self.EnableRegistry = None
        self.AutoscalerList = None
        self.Modifier = None
        self.Creator = None
        self.DeployStrategyConf = None
        self.PodList = None
        self.ConfEdited = None
        self.Tags = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.ApplicationId = params.get("ApplicationId")
        self.DeployMode = params.get("DeployMode")
        self.JdkVersion = params.get("JdkVersion")
        self.Description = params.get("Description")
        self.DeployVersion = params.get("DeployVersion")
        self.PublishMode = params.get("PublishMode")
        self.JvmOpts = params.get("JvmOpts")
        self.InitPodNum = params.get("InitPodNum")
        self.CpuSpec = params.get("CpuSpec")
        self.MemorySpec = params.get("MemorySpec")
        self.ImgRepo = params.get("ImgRepo")
        self.ImgName = params.get("ImgName")
        self.ImgVersion = params.get("ImgVersion")
        if params.get("EsInfo") is not None:
            self.EsInfo = EsInfo()
            self.EsInfo._deserialize(params.get("EsInfo"))
        if params.get("EnvConf") is not None:
            self.EnvConf = []
            for item in params.get("EnvConf"):
                obj = Pair()
                obj._deserialize(item)
                self.EnvConf.append(obj)
        if params.get("StorageConfs") is not None:
            self.StorageConfs = []
            for item in params.get("StorageConfs"):
                obj = StorageConf()
                obj._deserialize(item)
                self.StorageConfs.append(obj)
        self.Status = params.get("Status")
        self.Vpc = params.get("Vpc")
        self.SubnetId = params.get("SubnetId")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        if params.get("StorageMountConfs") is not None:
            self.StorageMountConfs = []
            for item in params.get("StorageMountConfs"):
                obj = StorageMountConf()
                obj._deserialize(item)
                self.StorageMountConfs.append(obj)
        self.VersionName = params.get("VersionName")
        if params.get("LogOutputConf") is not None:
            self.LogOutputConf = LogOutputConf()
            self.LogOutputConf._deserialize(params.get("LogOutputConf"))
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationDescription = params.get("ApplicationDescription")
        self.EnvironmentName = params.get("EnvironmentName")
        self.EnvironmentId = params.get("EnvironmentId")
        self.PublicDomain = params.get("PublicDomain")
        self.EnablePublicAccess = params.get("EnablePublicAccess")
        self.CurrentInstances = params.get("CurrentInstances")
        self.ExpectedInstances = params.get("ExpectedInstances")
        self.CodingLanguage = params.get("CodingLanguage")
        self.PkgName = params.get("PkgName")
        self.EsEnable = params.get("EsEnable")
        self.EsStrategy = params.get("EsStrategy")
        self.ImageTag = params.get("ImageTag")
        self.LogEnable = params.get("LogEnable")
        self.MinAliveInstances = params.get("MinAliveInstances")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.ImageCommand = params.get("ImageCommand")
        self.ImageArgs = params.get("ImageArgs")
        self.UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("Service") is not None:
            self.Service = EksService()
            self.Service._deserialize(params.get("Service"))
        if params.get("SettingConfs") is not None:
            self.SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self.SettingConfs.append(obj)
        self.LogConfs = params.get("LogConfs")
        self.PostStart = params.get("PostStart")
        self.PreStop = params.get("PreStop")
        if params.get("Liveness") is not None:
            self.Liveness = HealthCheckConfig()
            self.Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self.Readiness = HealthCheckConfig()
            self.Readiness._deserialize(params.get("Readiness"))
        if params.get("HorizontalAutoscaler") is not None:
            self.HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self.HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self.CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self.CronHorizontalAutoscaler.append(obj)
        self.Zones = params.get("Zones")
        self.LastDeployDate = params.get("LastDeployDate")
        self.LastDeploySuccessDate = params.get("LastDeploySuccessDate")
        if params.get("NodeInfos") is not None:
            self.NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfos.append(obj)
        self.ImageType = params.get("ImageType")
        self.EnableTracing = params.get("EnableTracing")
        self.EnableTracingReport = params.get("EnableTracingReport")
        self.RepoType = params.get("RepoType")
        self.BatchDeployStatus = params.get("BatchDeployStatus")
        self.ApmInstanceId = params.get("ApmInstanceId")
        if params.get("WorkloadInfo") is not None:
            self.WorkloadInfo = WorkloadInfo()
            self.WorkloadInfo._deserialize(params.get("WorkloadInfo"))
        self.SpeedUp = params.get("SpeedUp")
        if params.get("StartupProbe") is not None:
            self.StartupProbe = HealthCheckConfig()
            self.StartupProbe._deserialize(params.get("StartupProbe"))
        self.OsFlavour = params.get("OsFlavour")
        self.RepoServer = params.get("RepoServer")
        self.UnderDeploying = params.get("UnderDeploying")
        if params.get("EnablePrometheusConf") is not None:
            self.EnablePrometheusConf = EnablePrometheusConf()
            self.EnablePrometheusConf._deserialize(params.get("EnablePrometheusConf"))
        self.StoppedManually = params.get("StoppedManually")
        self.TcrInstanceId = params.get("TcrInstanceId")
        self.EnableMetrics = params.get("EnableMetrics")
        self.AppId = params.get("AppId")
        self.SubAccountUin = params.get("SubAccountUin")
        self.Uin = params.get("Uin")
        self.Region = params.get("Region")
        self.GroupId = params.get("GroupId")
        self.EnableRegistry = params.get("EnableRegistry")
        if params.get("AutoscalerList") is not None:
            self.AutoscalerList = []
            for item in params.get("AutoscalerList"):
                obj = Autoscaler()
                obj._deserialize(item)
                self.AutoscalerList.append(obj)
        self.Modifier = params.get("Modifier")
        self.Creator = params.get("Creator")
        if params.get("DeployStrategyConf") is not None:
            self.DeployStrategyConf = DeployStrategyConf()
            self.DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("PodList") is not None:
            self.PodList = DescribeRunPodPage()
            self.PodList._deserialize(params.get("PodList"))
        self.ConfEdited = params.get("ConfEdited")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UseDefaultRepoParameters(AbstractModel):
    """创建应用，创建仓库参数

    """

    def __init__(self):
        r"""
        :param EnterpriseInstanceName: 企业版实例名
注意：此字段可能返回 null，表示取不到有效值。
        :type EnterpriseInstanceName: str
        :param EnterpriseInstanceChargeType: 企业版收费类型  0 按量收费   1 包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :type EnterpriseInstanceChargeType: int
        :param EnterpriseInstanceType: 企业版规格：basic-基础班 ，standard-标准版，premium-高级版
注意：此字段可能返回 null，表示取不到有效值。
        :type EnterpriseInstanceType: str
        """
        self.EnterpriseInstanceName = None
        self.EnterpriseInstanceChargeType = None
        self.EnterpriseInstanceType = None


    def _deserialize(self, params):
        self.EnterpriseInstanceName = params.get("EnterpriseInstanceName")
        self.EnterpriseInstanceChargeType = params.get("EnterpriseInstanceChargeType")
        self.EnterpriseInstanceType = params.get("EnterpriseInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkloadInfo(AbstractModel):
    """工作负载详情

    """

    def __init__(self):
        r"""
        :param ClusterId: 资源 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ApplicationName: 应用名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param VersionName: 版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param ReadyReplicas: Ready实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadyReplicas: int
        :param Replicas: 实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param UpdatedReplicas: Updated实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedReplicas: int
        :param UpdatedReadyReplicas: UpdatedReady实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedReadyReplicas: int
        :param UpdateRevision: 更新版本
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateRevision: str
        :param CurrentRevision: 当前版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentRevision: str
        """
        self.ClusterId = None
        self.ApplicationName = None
        self.VersionName = None
        self.ReadyReplicas = None
        self.Replicas = None
        self.UpdatedReplicas = None
        self.UpdatedReadyReplicas = None
        self.UpdateRevision = None
        self.CurrentRevision = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ApplicationName = params.get("ApplicationName")
        self.VersionName = params.get("VersionName")
        self.ReadyReplicas = params.get("ReadyReplicas")
        self.Replicas = params.get("Replicas")
        self.UpdatedReplicas = params.get("UpdatedReplicas")
        self.UpdatedReadyReplicas = params.get("UpdatedReadyReplicas")
        self.UpdateRevision = params.get("UpdateRevision")
        self.CurrentRevision = params.get("CurrentRevision")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        