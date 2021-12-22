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
        :param Host: 域名
        :type Host: str
        :param Vip: VIP
        :type Vip: str
        """
        self.Host = None
        self.Vip = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Alias(AbstractModel):
    """函数的版本别名

    """

    def __init__(self):
        r"""
        :param FunctionVersion: 别名指向的主版本
        :type FunctionVersion: str
        :param Name: 别名的名称
        :type Name: str
        :param RoutingConfig: 别名的路由信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param AddTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param ModTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModTime: str
        """
        self.FunctionVersion = None
        self.Name = None
        self.RoutingConfig = None
        self.Description = None
        self.AddTime = None
        self.ModTime = None


    def _deserialize(self, params):
        self.FunctionVersion = params.get("FunctionVersion")
        self.Name = params.get("Name")
        if params.get("RoutingConfig") is not None:
            self.RoutingConfig = RoutingConfig()
            self.RoutingConfig._deserialize(params.get("RoutingConfig"))
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.ModTime = params.get("ModTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncEvent(AbstractModel):
    """异步事件

    """

    def __init__(self):
        r"""
        :param InvokeRequestId: 调用请求id
        :type InvokeRequestId: str
        :param InvokeType: 调用类型
        :type InvokeType: str
        :param Qualifier: 函数版本
        :type Qualifier: str
        :param Status: 事件状态，RUNNING 表示运行中, FINISHED 表示调用成功, ABORTED 表示调用终止, FAILED 表示调用失败
        :type Status: str
        :param StartTime: 调用开始时间，格式: "%Y-%m-%d %H:%M:%S.%f"
        :type StartTime: str
        :param EndTime: 调用结束时间，格式: "%Y-%m-%d %H:%M:%S.%f"
        :type EndTime: str
        """
        self.InvokeRequestId = None
        self.InvokeType = None
        self.Qualifier = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InvokeRequestId = params.get("InvokeRequestId")
        self.InvokeType = params.get("InvokeType")
        self.Qualifier = params.get("Qualifier")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncEventStatus(AbstractModel):
    """异步事件状态

    """

    def __init__(self):
        r"""
        :param Status: 异步事件状态，RUNNING 表示运行中, FINISHED 表示调用成功, ABORTED 表示调用终止, FAILED 表示调用失败。
        :type Status: str
        :param StatusCode: 请求状态码
        :type StatusCode: int
        :param InvokeRequestId: 异步执行请求 Id
        :type InvokeRequestId: str
        """
        self.Status = None
        self.StatusCode = None
        self.InvokeRequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.StatusCode = params.get("StatusCode")
        self.InvokeRequestId = params.get("InvokeRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncTriggerConfig(AbstractModel):
    """函数的异步重试配置详情

    """

    def __init__(self):
        r"""
        :param RetryConfig: 用户错误的异步重试重试配置
        :type RetryConfig: list of RetryConfig
        :param MsgTTL: 消息保留时间
        :type MsgTTL: int
        """
        self.RetryConfig = None
        self.MsgTTL = None


    def _deserialize(self, params):
        if params.get("RetryConfig") is not None:
            self.RetryConfig = []
            for item in params.get("RetryConfig"):
                obj = RetryConfig()
                obj._deserialize(item)
                self.RetryConfig.append(obj)
        self.MsgTTL = params.get("MsgTTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CfsConfig(AbstractModel):
    """文件系统(cfs)配置描述

    """

    def __init__(self):
        r"""
        :param CfsInsList: 文件系统信息列表
        :type CfsInsList: list of CfsInsInfo
        """
        self.CfsInsList = None


    def _deserialize(self, params):
        if params.get("CfsInsList") is not None:
            self.CfsInsList = []
            for item in params.get("CfsInsList"):
                obj = CfsInsInfo()
                obj._deserialize(item)
                self.CfsInsList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CfsInsInfo(AbstractModel):
    """云函数关联的cfs配置信息

    """

    def __init__(self):
        r"""
        :param UserId: 用户id
        :type UserId: str
        :param UserGroupId: 用户组id
        :type UserGroupId: str
        :param CfsId: 文件系统实例id
        :type CfsId: str
        :param MountInsId: 文件系统挂载点id
        :type MountInsId: str
        :param LocalMountDir: 本地挂载点
        :type LocalMountDir: str
        :param RemoteMountDir: 远程挂载点
        :type RemoteMountDir: str
        :param IpAddress: 文件系统ip，配置 cfs 时无需填写。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpAddress: str
        :param MountVpcId: 文件系统所在的私有网络id，配置 cfs 时无需填写。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MountVpcId: str
        :param MountSubnetId: 文件系统所在私有网络的子网id，配置 cfs 时无需填写。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MountSubnetId: str
        """
        self.UserId = None
        self.UserGroupId = None
        self.CfsId = None
        self.MountInsId = None
        self.LocalMountDir = None
        self.RemoteMountDir = None
        self.IpAddress = None
        self.MountVpcId = None
        self.MountSubnetId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserGroupId = params.get("UserGroupId")
        self.CfsId = params.get("CfsId")
        self.MountInsId = params.get("MountInsId")
        self.LocalMountDir = params.get("LocalMountDir")
        self.RemoteMountDir = params.get("RemoteMountDir")
        self.IpAddress = params.get("IpAddress")
        self.MountVpcId = params.get("MountVpcId")
        self.MountSubnetId = params.get("MountSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Code(AbstractModel):
    """函数代码

    """

    def __init__(self):
        r"""
        :param CosBucketName: 对象存储桶名称（填写存储桶名称自定义部分，不包含-appid）
        :type CosBucketName: str
        :param CosObjectName: 对象存储中代码包文件路径，以/开头
        :type CosObjectName: str
        :param ZipFile: 包含函数代码文件及其依赖项的 zip 格式文件，zip包大小上限为 50MB，使用该接口时要求将 zip 文件的内容转成 base64 编码
        :type ZipFile: str
        :param CosBucketRegion: 对象存储的地域，地域为北京时需要传入ap-beijing,北京一区时需要传递ap-beijing-1，其他的地域不需要传递。
        :type CosBucketRegion: str
        :param DemoId: 如果是通过Demo创建的话，需要传入DemoId
        :type DemoId: str
        :param TempCosObjectName: 如果是从TempCos创建的话，需要传入TempCosObjectName
        :type TempCosObjectName: str
        :param GitUrl: Git地址。该功能已下线。
        :type GitUrl: str
        :param GitUserName: Git用户名。该功能已下线。
        :type GitUserName: str
        :param GitPassword: Git密码。该功能已下线。
        :type GitPassword: str
        :param GitPasswordSecret: 加密后的Git密码，一般无需指定。该功能已下线。
        :type GitPasswordSecret: str
        :param GitBranch: Git分支。该功能已下线。
        :type GitBranch: str
        :param GitDirectory: 代码在Git仓库中的路径。该功能已下线。
        :type GitDirectory: str
        :param GitCommitId: 指定要拉取的版本。该功能已下线。
        :type GitCommitId: str
        :param GitUserNameSecret: 加密后的Git用户名，一般无需指定。该功能已下线。
        :type GitUserNameSecret: str
        :param ImageConfig: 镜像部署时配置TCR镜像信息
        :type ImageConfig: :class:`tencentcloud.scf.v20180416.models.ImageConfig`
        """
        self.CosBucketName = None
        self.CosObjectName = None
        self.ZipFile = None
        self.CosBucketRegion = None
        self.DemoId = None
        self.TempCosObjectName = None
        self.GitUrl = None
        self.GitUserName = None
        self.GitPassword = None
        self.GitPasswordSecret = None
        self.GitBranch = None
        self.GitDirectory = None
        self.GitCommitId = None
        self.GitUserNameSecret = None
        self.ImageConfig = None


    def _deserialize(self, params):
        self.CosBucketName = params.get("CosBucketName")
        self.CosObjectName = params.get("CosObjectName")
        self.ZipFile = params.get("ZipFile")
        self.CosBucketRegion = params.get("CosBucketRegion")
        self.DemoId = params.get("DemoId")
        self.TempCosObjectName = params.get("TempCosObjectName")
        self.GitUrl = params.get("GitUrl")
        self.GitUserName = params.get("GitUserName")
        self.GitPassword = params.get("GitPassword")
        self.GitPasswordSecret = params.get("GitPasswordSecret")
        self.GitBranch = params.get("GitBranch")
        self.GitDirectory = params.get("GitDirectory")
        self.GitCommitId = params.get("GitCommitId")
        self.GitUserNameSecret = params.get("GitUserNameSecret")
        if params.get("ImageConfig") is not None:
            self.ImageConfig = ImageConfig()
            self.ImageConfig._deserialize(params.get("ImageConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFunctionRequest(AbstractModel):
    """CopyFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 要复制的函数的名称
        :type FunctionName: str
        :param NewFunctionName: 新函数的名称
        :type NewFunctionName: str
        :param Namespace: 要复制的函数所在的命名空间，默认为default
        :type Namespace: str
        :param TargetNamespace: 将函数复制到的命名空间，默认为default
        :type TargetNamespace: str
        :param Description: 新函数的描述
        :type Description: str
        :param TargetRegion: 要将函数复制到的地域，不填则默认为当前地域
        :type TargetRegion: str
        :param Override: 如果目标Namespace下已有同名函数，是否覆盖，默认为否
（注意：如果选择覆盖，会导致同名函数被删除，请慎重操作）
TRUE：覆盖同名函数
FALSE：不覆盖同名函数
        :type Override: bool
        :param CopyConfiguration: 是否复制函数的属性，包括环境变量、内存、超时、函数描述、标签、VPC等，默认为是。
TRUE：复制函数配置
FALSE：不复制函数配置
        :type CopyConfiguration: bool
        """
        self.FunctionName = None
        self.NewFunctionName = None
        self.Namespace = None
        self.TargetNamespace = None
        self.Description = None
        self.TargetRegion = None
        self.Override = None
        self.CopyConfiguration = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.NewFunctionName = params.get("NewFunctionName")
        self.Namespace = params.get("Namespace")
        self.TargetNamespace = params.get("TargetNamespace")
        self.Description = params.get("Description")
        self.TargetRegion = params.get("TargetRegion")
        self.Override = params.get("Override")
        self.CopyConfiguration = params.get("CopyConfiguration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFunctionResponse(AbstractModel):
    """CopyFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAliasRequest(AbstractModel):
    """CreateAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 别名的名称，在函数级别中唯一，只能包含字母、数字、'_'和‘-’，且必须以字母开头，长度限制为1-64
        :type Name: str
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param FunctionVersion: 别名指向的主版本
        :type FunctionVersion: str
        :param Namespace: 函数所在的命名空间
        :type Namespace: str
        :param RoutingConfig: 别名的请求路由配置
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param Description: 别名的描述信息
        :type Description: str
        """
        self.Name = None
        self.FunctionName = None
        self.FunctionVersion = None
        self.Namespace = None
        self.RoutingConfig = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.FunctionName = params.get("FunctionName")
        self.FunctionVersion = params.get("FunctionVersion")
        self.Namespace = params.get("Namespace")
        if params.get("RoutingConfig") is not None:
            self.RoutingConfig = RoutingConfig()
            self.RoutingConfig._deserialize(params.get("RoutingConfig"))
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAliasResponse(AbstractModel):
    """CreateAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFunctionRequest(AbstractModel):
    """CreateFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 创建的函数名称，函数名称支持26个英文字母大小写、数字、连接符和下划线，第一个字符只能以字母开头，最后一个字符不能为连接符或者下划线，名称长度2-60
        :type FunctionName: str
        :param Code: 函数代码. 注意：不能同时指定Cos、ZipFile或 DemoId。
        :type Code: :class:`tencentcloud.scf.v20180416.models.Code`
        :param Handler: 函数处理方法名称，名称格式支持 "文件名称.方法名称" 形式（java 名称格式 包名.类名::方法名），文件名称和函数名称之间以"."隔开，文件名称和函数名称要求以字母开始和结尾，中间允许插入字母、数字、下划线和连接符，文件名称和函数名字的长度要求是 2-60 个字符
        :type Handler: str
        :param Description: 函数描述,最大支持 1000 个英文字母、数字、空格、逗号、换行符和英文句号，支持中文
        :type Description: str
        :param MemorySize: 函数运行时内存大小，默认为 128M，可选范围 64、128MB-3072MB，并且以 128MB 为阶梯
        :type MemorySize: int
        :param Timeout: 函数最长执行时间，单位为秒，可选值范围 1-900 秒，默认为 3 秒
        :type Timeout: int
        :param Environment: 函数的环境变量
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param Runtime: 函数运行环境，目前仅支持 Python2.7，Python3.6，Nodejs6.10，Nodejs8.9，Nodejs10.15，Nodejs12.16， Php5， Php7，Go1，Java8 和 CustomRuntime，默认Python2.7
        :type Runtime: str
        :param VpcConfig: 函数的私有网络配置
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        :param Role: 函数绑定的角色
        :type Role: str
        :param InstallDependency: [在线依赖安装](https://cloud.tencent.com/document/product/583/37920)，TRUE 表示安装，默认值为 FALSE。仅支持 Node.js 函数。
        :type InstallDependency: str
        :param ClsLogsetId: 函数日志投递到的CLS LogsetID
        :type ClsLogsetId: str
        :param ClsTopicId: 函数日志投递到的CLS TopicID
        :type ClsTopicId: str
        :param Type: 函数类型，默认值为Event，创建触发器函数请填写Event，创建HTTP函数级服务请填写HTTP
        :type Type: str
        :param CodeSource: CodeSource 代码来源，支持ZipFile, Cos, Demo 其中之一
        :type CodeSource: str
        :param Layers: 函数要关联的Layer版本列表，Layer会按照在列表中顺序依次覆盖。
        :type Layers: list of LayerVersionSimple
        :param DeadLetterConfig: 死信队列参数
        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`
        :param PublicNetConfig: 公网访问配置
        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigIn`
        :param CfsConfig: 文件系统配置参数，用于云函数挂载文件系统
        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`
        :param InitTimeout: 函数初始化超时时间，默认 65s，镜像部署函数默认 90s。
        :type InitTimeout: int
        :param Tags: 函数 Tag 参数，以键值对数组形式传入
        :type Tags: list of Tag
        :param AsyncRunEnable: 是否开启异步属性，TRUE 为开启，FALSE为关闭
        :type AsyncRunEnable: str
        :param TraceEnable: 是否开启事件追踪，TRUE 为开启，FALSE为关闭
        :type TraceEnable: str
        :param ProtocolType: HTTP函数支持的访问协议。当前支持WebSockets协议，值为WS
        :type ProtocolType: str
        :param ProtocolParams: HTTP函数配置ProtocolType访问协议，当前协议可配置的参数
        :type ProtocolParams: :class:`tencentcloud.scf.v20180416.models.ProtocolParams`
        """
        self.FunctionName = None
        self.Code = None
        self.Handler = None
        self.Description = None
        self.MemorySize = None
        self.Timeout = None
        self.Environment = None
        self.Runtime = None
        self.VpcConfig = None
        self.Namespace = None
        self.Role = None
        self.InstallDependency = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.Type = None
        self.CodeSource = None
        self.Layers = None
        self.DeadLetterConfig = None
        self.PublicNetConfig = None
        self.CfsConfig = None
        self.InitTimeout = None
        self.Tags = None
        self.AsyncRunEnable = None
        self.TraceEnable = None
        self.ProtocolType = None
        self.ProtocolParams = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        if params.get("Code") is not None:
            self.Code = Code()
            self.Code._deserialize(params.get("Code"))
        self.Handler = params.get("Handler")
        self.Description = params.get("Description")
        self.MemorySize = params.get("MemorySize")
        self.Timeout = params.get("Timeout")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        self.Runtime = params.get("Runtime")
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.Namespace = params.get("Namespace")
        self.Role = params.get("Role")
        self.InstallDependency = params.get("InstallDependency")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.Type = params.get("Type")
        self.CodeSource = params.get("CodeSource")
        if params.get("Layers") is not None:
            self.Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionSimple()
                obj._deserialize(item)
                self.Layers.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self.DeadLetterConfig = DeadLetterConfig()
            self.DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        if params.get("PublicNetConfig") is not None:
            self.PublicNetConfig = PublicNetConfigIn()
            self.PublicNetConfig._deserialize(params.get("PublicNetConfig"))
        if params.get("CfsConfig") is not None:
            self.CfsConfig = CfsConfig()
            self.CfsConfig._deserialize(params.get("CfsConfig"))
        self.InitTimeout = params.get("InitTimeout")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AsyncRunEnable = params.get("AsyncRunEnable")
        self.TraceEnable = params.get("TraceEnable")
        self.ProtocolType = params.get("ProtocolType")
        if params.get("ProtocolParams") is not None:
            self.ProtocolParams = ProtocolParams()
            self.ProtocolParams._deserialize(params.get("ProtocolParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFunctionResponse(AbstractModel):
    """CreateFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间名称
        :type Namespace: str
        :param Description: 命名空间描述
        :type Description: str
        """
        self.Namespace = None
        self.Description = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTriggerRequest(AbstractModel):
    """CreateTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 新建触发器绑定的函数名称
        :type FunctionName: str
        :param TriggerName: 新建触发器名称。如果是定时触发器，名称支持英文字母、数字、连接符和下划线，最长100个字符；如果是cos触发器，需要是对应cos存储桶适用于XML API的访问域名(例如:5401-5ff414-12345.cos.ap-shanghai.myqcloud.com);如果是其他触发器，见具体触发器绑定参数的说明
        :type TriggerName: str
        :param Type: 触发器类型，目前支持 cos 、cmq、 timer、 ckafka、apigw类型。创建 cls 触发器请参考[CLS 创建投递 SCF 任务](https://cloud.tencent.com/document/product/614/61096)。
        :type Type: str
        :param TriggerDesc: 触发器对应的参数，可见具体[触发器描述说明](https://cloud.tencent.com/document/product/583/39901)
        :type TriggerDesc: str
        :param Namespace: 函数的命名空间
        :type Namespace: str
        :param Qualifier: 函数的版本
        :type Qualifier: str
        :param Enable: 触发器的初始是能状态 OPEN表示开启 CLOSE表示关闭
        :type Enable: str
        :param CustomArgument: 用户自定义参数，仅支持timer触发器
        :type CustomArgument: str
        """
        self.FunctionName = None
        self.TriggerName = None
        self.Type = None
        self.TriggerDesc = None
        self.Namespace = None
        self.Qualifier = None
        self.Enable = None
        self.CustomArgument = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        self.Enable = params.get("Enable")
        self.CustomArgument = params.get("CustomArgument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTriggerResponse(AbstractModel):
    """CreateTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param TriggerInfo: 触发器信息
        :type TriggerInfo: :class:`tencentcloud.scf.v20180416.models.Trigger`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TriggerInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TriggerInfo") is not None:
            self.TriggerInfo = Trigger()
            self.TriggerInfo._deserialize(params.get("TriggerInfo"))
        self.RequestId = params.get("RequestId")


class DeadLetterConfig(AbstractModel):
    """死信队列参数

    """

    def __init__(self):
        r"""
        :param Type: 死信队列模式
        :type Type: str
        :param Name: 死信队列名称
        :type Name: str
        :param FilterType: 死信队列主题模式的标签形式
        :type FilterType: str
        """
        self.Type = None
        self.Name = None
        self.FilterType = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasRequest(AbstractModel):
    """DeleteAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param Name: 别名的名称
        :type Name: str
        :param Namespace: 函数所在的命名空间
        :type Namespace: str
        """
        self.FunctionName = None
        self.Name = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasResponse(AbstractModel):
    """DeleteAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFunctionRequest(AbstractModel):
    """DeleteFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 要删除的函数名称
        :type FunctionName: str
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        :param Qualifier: 函数版本，如果删除版本的话传入版本号，不传入改字段删除函数下的所有版本
        :type Qualifier: str
        """
        self.FunctionName = None
        self.Namespace = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFunctionResponse(AbstractModel):
    """DeleteFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLayerVersionRequest(AbstractModel):
    """DeleteLayerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param LayerName: 层名称
        :type LayerName: str
        :param LayerVersion: 版本号
        :type LayerVersion: int
        """
        self.LayerName = None
        self.LayerVersion = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.LayerVersion = params.get("LayerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLayerVersionResponse(AbstractModel):
    """DeleteLayerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间名称
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProvisionedConcurrencyConfigRequest(AbstractModel):
    """DeleteProvisionedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 需要删除预置并发的函数的名称
        :type FunctionName: str
        :param Qualifier: 函数的版本号
        :type Qualifier: str
        :param Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        """
        self.FunctionName = None
        self.Qualifier = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProvisionedConcurrencyConfigResponse(AbstractModel):
    """DeleteProvisionedConcurrencyConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReservedConcurrencyConfigRequest(AbstractModel):
    """DeleteReservedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 需要删除最大独占配额的函数的名称
        :type FunctionName: str
        :param Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        """
        self.FunctionName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReservedConcurrencyConfigResponse(AbstractModel):
    """DeleteReservedConcurrencyConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTriggerRequest(AbstractModel):
    """DeleteTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数的名称
        :type FunctionName: str
        :param TriggerName: 要删除的触发器名称
        :type TriggerName: str
        :param Type: 要删除的触发器类型，目前支持 cos 、cmq、 timer、ckafka 类型
        :type Type: str
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        :param TriggerDesc: 如果删除的触发器类型为 COS 触发器，该字段为必填值，存放 JSON 格式的数据 {"event":"cos:ObjectCreated:*"}，数据内容和 SetTrigger 接口中该字段的格式相同；如果删除的触发器类型为定时触发器或 CMQ 触发器，可以不指定该字段
        :type TriggerDesc: str
        :param Qualifier: 函数的版本信息
        :type Qualifier: str
        """
        self.FunctionName = None
        self.TriggerName = None
        self.Type = None
        self.Namespace = None
        self.TriggerDesc = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.Namespace = params.get("Namespace")
        self.TriggerDesc = params.get("TriggerDesc")
        self.Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTriggerResponse(AbstractModel):
    """DeleteTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EipConfigIn(AbstractModel):
    """公网访问固定ip配置

    """

    def __init__(self):
        r"""
        :param EipStatus: Eip开启状态，取值['ENABLE','DISABLE']
        :type EipStatus: str
        """
        self.EipStatus = None


    def _deserialize(self, params):
        self.EipStatus = params.get("EipStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipConfigOut(AbstractModel):
    """公网访问固定ip配置

    """

    def __init__(self):
        r"""
        :param EipStatus: 是否是固定IP，["ENABLE","DISABLE"]
        :type EipStatus: str
        :param EipAddress: IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EipAddress: list of str
        """
        self.EipStatus = None
        self.EipAddress = None


    def _deserialize(self, params):
        self.EipStatus = params.get("EipStatus")
        self.EipAddress = params.get("EipAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipOutConfig(AbstractModel):
    """EipOutConfig

    """

    def __init__(self):
        r"""
        :param EipFixed: 是否是固定IP，["TRUE","FALSE"]
        :type EipFixed: str
        :param Eips: IP列表
        :type Eips: list of str
        """
        self.EipFixed = None
        self.Eips = None


    def _deserialize(self, params):
        self.EipFixed = params.get("EipFixed")
        self.Eips = params.get("Eips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Environment(AbstractModel):
    """函数的环境变量参数

    """

    def __init__(self):
        r"""
        :param Variables: 环境变量数组
        :type Variables: list of Variable
        """
        self.Variables = None


    def _deserialize(self, params):
        if params.get("Variables") is not None:
            self.Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self.Variables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Name: 需要过滤的字段。过滤条件数量限制为10。
Name可选值：VpcId, SubnetId, ClsTopicId, ClsLogsetId, Role, CfsId, CfsMountInsId, Eip；Values 长度限制为1。
Name可选值：Status, Runtime, FunctionType, PublicNetStatus, AsyncRunEnable, TraceEnable；Values 长度限制为20。
当 Name = Runtime 时，CustomImage 表示过滤镜像类型函数。
        :type Name: str
        :param Values: 字段的过滤值。
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Function(AbstractModel):
    """函数列表

    """

    def __init__(self):
        r"""
        :param ModTime: 修改时间
        :type ModTime: str
        :param AddTime: 创建时间
        :type AddTime: str
        :param Runtime: 运行时
        :type Runtime: str
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param FunctionId: 函数ID
        :type FunctionId: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Status: 函数状态，状态值及流转[参考此处](https://cloud.tencent.com/document/product/583/47175)
        :type Status: str
        :param StatusDesc: 函数状态详情
        :type StatusDesc: str
        :param Description: 函数描述
        :type Description: str
        :param Tags: 函数标签
        :type Tags: list of Tag
        :param Type: 函数类型，取值为 HTTP 或者 Event
        :type Type: str
        :param StatusReasons: 函数状态失败原因
        :type StatusReasons: list of StatusReason
        :param TotalProvisionedConcurrencyMem: 函数所有版本预置并发内存总和
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalProvisionedConcurrencyMem: int
        :param ReservedConcurrencyMem: 函数并发保留内存
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedConcurrencyMem: int
        :param AsyncRunEnable: 函数异步属性，取值 TRUE 或者 FALSE
        :type AsyncRunEnable: str
        :param TraceEnable: 异步函数是否开启调用追踪，取值 TRUE 或者 FALSE
        :type TraceEnable: str
        """
        self.ModTime = None
        self.AddTime = None
        self.Runtime = None
        self.FunctionName = None
        self.FunctionId = None
        self.Namespace = None
        self.Status = None
        self.StatusDesc = None
        self.Description = None
        self.Tags = None
        self.Type = None
        self.StatusReasons = None
        self.TotalProvisionedConcurrencyMem = None
        self.ReservedConcurrencyMem = None
        self.AsyncRunEnable = None
        self.TraceEnable = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.AddTime = params.get("AddTime")
        self.Runtime = params.get("Runtime")
        self.FunctionName = params.get("FunctionName")
        self.FunctionId = params.get("FunctionId")
        self.Namespace = params.get("Namespace")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.Description = params.get("Description")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Type = params.get("Type")
        if params.get("StatusReasons") is not None:
            self.StatusReasons = []
            for item in params.get("StatusReasons"):
                obj = StatusReason()
                obj._deserialize(item)
                self.StatusReasons.append(obj)
        self.TotalProvisionedConcurrencyMem = params.get("TotalProvisionedConcurrencyMem")
        self.ReservedConcurrencyMem = params.get("ReservedConcurrencyMem")
        self.AsyncRunEnable = params.get("AsyncRunEnable")
        self.TraceEnable = params.get("TraceEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionLog(AbstractModel):
    """日志信息

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数的名称
        :type FunctionName: str
        :param RetMsg: 函数执行完成后的返回值
        :type RetMsg: str
        :param RequestId: 执行该函数对应的requestId
        :type RequestId: str
        :param StartTime: 函数开始执行时的时间点
        :type StartTime: str
        :param RetCode: 函数执行结果，如果是 0 表示执行成功，其他值表示失败
        :type RetCode: int
        :param InvokeFinished: 函数调用是否结束，如果是 1 表示执行结束，其他值表示调用异常
        :type InvokeFinished: int
        :param Duration: 函数执行耗时，单位为 ms
        :type Duration: float
        :param BillDuration: 函数计费时间，根据 duration 向上取最近的 100ms，单位为ms
        :type BillDuration: int
        :param MemUsage: 函数执行时消耗实际内存大小，单位为 Byte
        :type MemUsage: int
        :param Log: 函数执行过程中的日志输出
        :type Log: str
        :param Level: 日志等级
        :type Level: str
        :param Source: 日志来源
        :type Source: str
        :param RetryNum: 重试次数
        :type RetryNum: int
        """
        self.FunctionName = None
        self.RetMsg = None
        self.RequestId = None
        self.StartTime = None
        self.RetCode = None
        self.InvokeFinished = None
        self.Duration = None
        self.BillDuration = None
        self.MemUsage = None
        self.Log = None
        self.Level = None
        self.Source = None
        self.RetryNum = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.RetMsg = params.get("RetMsg")
        self.RequestId = params.get("RequestId")
        self.StartTime = params.get("StartTime")
        self.RetCode = params.get("RetCode")
        self.InvokeFinished = params.get("InvokeFinished")
        self.Duration = params.get("Duration")
        self.BillDuration = params.get("BillDuration")
        self.MemUsage = params.get("MemUsage")
        self.Log = params.get("Log")
        self.Level = params.get("Level")
        self.Source = params.get("Source")
        self.RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionVersion(AbstractModel):
    """函数版本信息

    """

    def __init__(self):
        r"""
        :param Version: 函数版本名称
        :type Version: str
        :param Description: 版本描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param AddTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param ModTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModTime: str
        :param Status: 版本状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.Version = None
        self.Description = None
        self.AddTime = None
        self.ModTime = None
        self.Status = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.ModTime = params.get("ModTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param AccountUsage: 命名空间已使用的信息
        :type AccountUsage: :class:`tencentcloud.scf.v20180416.models.UsageInfo`
        :param AccountLimit: 命名空间限制的信息
        :type AccountLimit: :class:`tencentcloud.scf.v20180416.models.LimitsInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccountUsage = None
        self.AccountLimit = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccountUsage") is not None:
            self.AccountUsage = UsageInfo()
            self.AccountUsage._deserialize(params.get("AccountUsage"))
        if params.get("AccountLimit") is not None:
            self.AccountLimit = LimitsInfo()
            self.AccountLimit._deserialize(params.get("AccountLimit"))
        self.RequestId = params.get("RequestId")


class GetAliasRequest(AbstractModel):
    """GetAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param Name: 别名的名称
        :type Name: str
        :param Namespace: 函数所在的命名空间
        :type Namespace: str
        """
        self.FunctionName = None
        self.Name = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAliasResponse(AbstractModel):
    """GetAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionVersion: 别名指向的主版本
        :type FunctionVersion: str
        :param Name: 别名的名称
        :type Name: str
        :param RoutingConfig: 别名的路由信息
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param Description: 别名的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param AddTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param ModTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FunctionVersion = None
        self.Name = None
        self.RoutingConfig = None
        self.Description = None
        self.AddTime = None
        self.ModTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionVersion = params.get("FunctionVersion")
        self.Name = params.get("Name")
        if params.get("RoutingConfig") is not None:
            self.RoutingConfig = RoutingConfig()
            self.RoutingConfig._deserialize(params.get("RoutingConfig"))
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.ModTime = params.get("ModTime")
        self.RequestId = params.get("RequestId")


class GetAsyncEventStatusRequest(AbstractModel):
    """GetAsyncEventStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param InvokeRequestId: 异步执行请求 id
        :type InvokeRequestId: str
        """
        self.InvokeRequestId = None


    def _deserialize(self, params):
        self.InvokeRequestId = params.get("InvokeRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAsyncEventStatusResponse(AbstractModel):
    """GetAsyncEventStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 异步事件状态
        :type Result: :class:`tencentcloud.scf.v20180416.models.AsyncEventStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AsyncEventStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class GetFunctionAddressRequest(AbstractModel):
    """GetFunctionAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数的名称
        :type FunctionName: str
        :param Qualifier: 函数的版本
        :type Qualifier: str
        :param Namespace: 函数的命名空间
        :type Namespace: str
        """
        self.FunctionName = None
        self.Qualifier = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionAddressResponse(AbstractModel):
    """GetFunctionAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 函数的Cos地址
        :type Url: str
        :param CodeSha256: 函数的SHA256编码
        :type CodeSha256: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.CodeSha256 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.CodeSha256 = params.get("CodeSha256")
        self.RequestId = params.get("RequestId")


class GetFunctionEventInvokeConfigRequest(AbstractModel):
    """GetFunctionEventInvokeConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        :param Qualifier: 函数版本，默认为$LATEST
        :type Qualifier: str
        """
        self.FunctionName = None
        self.Namespace = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionEventInvokeConfigResponse(AbstractModel):
    """GetFunctionEventInvokeConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncTriggerConfig: 异步重试配置信息
        :type AsyncTriggerConfig: :class:`tencentcloud.scf.v20180416.models.AsyncTriggerConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncTriggerConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AsyncTriggerConfig") is not None:
            self.AsyncTriggerConfig = AsyncTriggerConfig()
            self.AsyncTriggerConfig._deserialize(params.get("AsyncTriggerConfig"))
        self.RequestId = params.get("RequestId")


class GetFunctionLogsRequest(AbstractModel):
    """GetFunctionLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数的名称。
- 为保证[获取函数运行日志](https://cloud.tencent.com/document/product/583/18583)接口`GetFunctionLogs`兼容性，输入参数`FunctionName`仍为非必填项，但建议填写该参数，否则可能导致日志获取失败。
- 函数关联日志服务后，建议使用[日志服务](https://cloud.tencent.com/document/product/614/16875)相关接口以获得最佳日志检索体验。
        :type FunctionName: str
        :param Offset: 数据的偏移量，Offset+Limit不能大于10000
        :type Offset: int
        :param Limit: 返回数据的长度，Offset+Limit不能大于10000
        :type Limit: int
        :param Order: 以升序还是降序的方式对日志进行排序，可选值 desc和 asc
        :type Order: str
        :param OrderBy: 根据某个字段排序日志,支持以下字段：function_name, duration, mem_usage, start_time
        :type OrderBy: str
        :param Filter: 日志过滤条件。可用来区分正确和错误日志，filter.RetCode=not0 表示只返回错误日志，filter.RetCode=is0 表示只返回正确日志，不传，则返回所有日志
        :type Filter: :class:`tencentcloud.scf.v20180416.models.LogFilter`
        :param Namespace: 函数的命名空间
        :type Namespace: str
        :param Qualifier: 函数的版本
        :type Qualifier: str
        :param FunctionRequestId: 执行该函数对应的requestId
        :type FunctionRequestId: str
        :param StartTime: 查询的具体日期，例如：2017-05-16 20:00:00，只能与endtime相差一天之内
        :type StartTime: str
        :param EndTime: 查询的具体日期，例如：2017-05-16 20:59:59，只能与startTime相差一天之内
        :type EndTime: str
        :param SearchContext: 该字段已下线
        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`
        """
        self.FunctionName = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderBy = None
        self.Filter = None
        self.Namespace = None
        self.Qualifier = None
        self.FunctionRequestId = None
        self.StartTime = None
        self.EndTime = None
        self.SearchContext = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self.Filter = LogFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        self.FunctionRequestId = params.get("FunctionRequestId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("SearchContext") is not None:
            self.SearchContext = LogSearchContext()
            self.SearchContext._deserialize(params.get("SearchContext"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionLogsResponse(AbstractModel):
    """GetFunctionLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 函数日志的总数
        :type TotalCount: int
        :param Data: 函数日志信息
        :type Data: list of FunctionLog
        :param SearchContext: 该字段已下线
        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.SearchContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = FunctionLog()
                obj._deserialize(item)
                self.Data.append(obj)
        if params.get("SearchContext") is not None:
            self.SearchContext = LogSearchContext()
            self.SearchContext._deserialize(params.get("SearchContext"))
        self.RequestId = params.get("RequestId")


class GetFunctionRequest(AbstractModel):
    """GetFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 需要获取详情的函数名称
        :type FunctionName: str
        :param Qualifier: 函数的版本号
        :type Qualifier: str
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        :param ShowCode: 是否显示代码, TRUE表示显示代码，FALSE表示不显示代码,大于1M的入口文件不会显示
        :type ShowCode: str
        """
        self.FunctionName = None
        self.Qualifier = None
        self.Namespace = None
        self.ShowCode = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Namespace = params.get("Namespace")
        self.ShowCode = params.get("ShowCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionResponse(AbstractModel):
    """GetFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param ModTime: 函数的最后修改时间
        :type ModTime: str
        :param CodeInfo: 函数的代码
        :type CodeInfo: str
        :param Description: 函数的描述信息
        :type Description: str
        :param Triggers: 函数的触发器列表
        :type Triggers: list of Trigger
        :param Handler: 函数的入口
        :type Handler: str
        :param CodeSize: 函数代码大小
        :type CodeSize: int
        :param Timeout: 函数的超时时间
        :type Timeout: int
        :param FunctionVersion: 函数的版本
        :type FunctionVersion: str
        :param MemorySize: 函数的最大可用内存
        :type MemorySize: int
        :param Runtime: 函数的运行环境
        :type Runtime: str
        :param FunctionName: 函数的名称
        :type FunctionName: str
        :param VpcConfig: 函数的私有网络
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        :param UseGpu: 是否使用GPU
        :type UseGpu: str
        :param Environment: 函数的环境变量
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param CodeResult: 代码是否正确
        :type CodeResult: str
        :param CodeError: 代码错误信息
        :type CodeError: str
        :param ErrNo: 代码错误码
        :type ErrNo: int
        :param Namespace: 函数的命名空间
        :type Namespace: str
        :param Role: 函数绑定的角色
        :type Role: str
        :param InstallDependency: 是否自动安装依赖
        :type InstallDependency: str
        :param Status: 函数状态，状态值及流转[参考说明](https://cloud.tencent.com/document/product/583/47175)
        :type Status: str
        :param StatusDesc: 状态描述
        :type StatusDesc: str
        :param ClsLogsetId: 日志投递到的Cls日志集
        :type ClsLogsetId: str
        :param ClsTopicId: 日志投递到的Cls Topic
        :type ClsTopicId: str
        :param FunctionId: 函数ID
        :type FunctionId: str
        :param Tags: 函数的标签列表
        :type Tags: list of Tag
        :param EipConfig: EipConfig配置
        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipOutConfig`
        :param AccessInfo: 域名信息
        :type AccessInfo: :class:`tencentcloud.scf.v20180416.models.AccessInfo`
        :param Type: 函数类型，取值为HTTP或者Event
        :type Type: str
        :param L5Enable: 是否启用L5
        :type L5Enable: str
        :param Layers: 函数关联的Layer版本信息
        :type Layers: list of LayerVersionInfo
        :param DeadLetterConfig: 函数关联的死信队列信息
        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`
        :param AddTime: 函数创建回见
        :type AddTime: str
        :param PublicNetConfig: 公网访问配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigOut`
        :param OnsEnable: 是否启用Ons
注意：此字段可能返回 null，表示取不到有效值。
        :type OnsEnable: str
        :param CfsConfig: 文件系统配置参数，用于云函数挂载文件系统
注意：此字段可能返回 null，表示取不到有效值。
        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`
        :param AvailableStatus: 函数的计费状态，状态值[参考此处](https://cloud.tencent.com/document/product/583/47175#.E5.87.BD.E6.95.B0.E8.AE.A1.E8.B4.B9.E7.8A.B6.E6.80.81)
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableStatus: str
        :param Qualifier: 函数版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Qualifier: str
        :param InitTimeout: 函数初始化超时时间
        :type InitTimeout: int
        :param StatusReasons: 函数状态失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusReasons: list of StatusReason
        :param AsyncRunEnable: 是否开启异步属性
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRunEnable: str
        :param TraceEnable: 是否开启事件追踪
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceEnable: str
        :param ProtocolType: HTTP函数支持的访问协议。当前支持WebSockets协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolType: str
        :param ProtocolParams: HTTP函数配置ProtocolType访问协议，当前协议配置的参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolParams: :class:`tencentcloud.scf.v20180416.models.ProtocolParams`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModTime = None
        self.CodeInfo = None
        self.Description = None
        self.Triggers = None
        self.Handler = None
        self.CodeSize = None
        self.Timeout = None
        self.FunctionVersion = None
        self.MemorySize = None
        self.Runtime = None
        self.FunctionName = None
        self.VpcConfig = None
        self.UseGpu = None
        self.Environment = None
        self.CodeResult = None
        self.CodeError = None
        self.ErrNo = None
        self.Namespace = None
        self.Role = None
        self.InstallDependency = None
        self.Status = None
        self.StatusDesc = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.FunctionId = None
        self.Tags = None
        self.EipConfig = None
        self.AccessInfo = None
        self.Type = None
        self.L5Enable = None
        self.Layers = None
        self.DeadLetterConfig = None
        self.AddTime = None
        self.PublicNetConfig = None
        self.OnsEnable = None
        self.CfsConfig = None
        self.AvailableStatus = None
        self.Qualifier = None
        self.InitTimeout = None
        self.StatusReasons = None
        self.AsyncRunEnable = None
        self.TraceEnable = None
        self.ProtocolType = None
        self.ProtocolParams = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.CodeInfo = params.get("CodeInfo")
        self.Description = params.get("Description")
        if params.get("Triggers") is not None:
            self.Triggers = []
            for item in params.get("Triggers"):
                obj = Trigger()
                obj._deserialize(item)
                self.Triggers.append(obj)
        self.Handler = params.get("Handler")
        self.CodeSize = params.get("CodeSize")
        self.Timeout = params.get("Timeout")
        self.FunctionVersion = params.get("FunctionVersion")
        self.MemorySize = params.get("MemorySize")
        self.Runtime = params.get("Runtime")
        self.FunctionName = params.get("FunctionName")
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.UseGpu = params.get("UseGpu")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        self.CodeResult = params.get("CodeResult")
        self.CodeError = params.get("CodeError")
        self.ErrNo = params.get("ErrNo")
        self.Namespace = params.get("Namespace")
        self.Role = params.get("Role")
        self.InstallDependency = params.get("InstallDependency")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.FunctionId = params.get("FunctionId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("EipConfig") is not None:
            self.EipConfig = EipOutConfig()
            self.EipConfig._deserialize(params.get("EipConfig"))
        if params.get("AccessInfo") is not None:
            self.AccessInfo = AccessInfo()
            self.AccessInfo._deserialize(params.get("AccessInfo"))
        self.Type = params.get("Type")
        self.L5Enable = params.get("L5Enable")
        if params.get("Layers") is not None:
            self.Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionInfo()
                obj._deserialize(item)
                self.Layers.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self.DeadLetterConfig = DeadLetterConfig()
            self.DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        self.AddTime = params.get("AddTime")
        if params.get("PublicNetConfig") is not None:
            self.PublicNetConfig = PublicNetConfigOut()
            self.PublicNetConfig._deserialize(params.get("PublicNetConfig"))
        self.OnsEnable = params.get("OnsEnable")
        if params.get("CfsConfig") is not None:
            self.CfsConfig = CfsConfig()
            self.CfsConfig._deserialize(params.get("CfsConfig"))
        self.AvailableStatus = params.get("AvailableStatus")
        self.Qualifier = params.get("Qualifier")
        self.InitTimeout = params.get("InitTimeout")
        if params.get("StatusReasons") is not None:
            self.StatusReasons = []
            for item in params.get("StatusReasons"):
                obj = StatusReason()
                obj._deserialize(item)
                self.StatusReasons.append(obj)
        self.AsyncRunEnable = params.get("AsyncRunEnable")
        self.TraceEnable = params.get("TraceEnable")
        self.ProtocolType = params.get("ProtocolType")
        if params.get("ProtocolParams") is not None:
            self.ProtocolParams = ProtocolParams()
            self.ProtocolParams._deserialize(params.get("ProtocolParams"))
        self.RequestId = params.get("RequestId")


class GetLayerVersionRequest(AbstractModel):
    """GetLayerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param LayerName: 层名称
        :type LayerName: str
        :param LayerVersion: 版本号
        :type LayerVersion: int
        """
        self.LayerName = None
        self.LayerVersion = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.LayerVersion = params.get("LayerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLayerVersionResponse(AbstractModel):
    """GetLayerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompatibleRuntimes: 适配的运行时
        :type CompatibleRuntimes: list of str
        :param CodeSha256: 层中版本文件的SHA256编码
        :type CodeSha256: str
        :param Location: 层中版本文件的下载地址
        :type Location: str
        :param AddTime: 版本的创建时间
        :type AddTime: str
        :param Description: 版本的描述
        :type Description: str
        :param LicenseInfo: 许可证信息
        :type LicenseInfo: str
        :param LayerVersion: 版本号
        :type LayerVersion: int
        :param LayerName: 层名称
        :type LayerName: str
        :param Status: 层的具体版本当前状态，可能取值：
Active 正常
Publishing  发布中
PublishFailed  发布失败
Deleted 已删除
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompatibleRuntimes = None
        self.CodeSha256 = None
        self.Location = None
        self.AddTime = None
        self.Description = None
        self.LicenseInfo = None
        self.LayerVersion = None
        self.LayerName = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompatibleRuntimes = params.get("CompatibleRuntimes")
        self.CodeSha256 = params.get("CodeSha256")
        self.Location = params.get("Location")
        self.AddTime = params.get("AddTime")
        self.Description = params.get("Description")
        self.LicenseInfo = params.get("LicenseInfo")
        self.LayerVersion = params.get("LayerVersion")
        self.LayerName = params.get("LayerName")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class GetProvisionedConcurrencyConfigRequest(AbstractModel):
    """GetProvisionedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 需要获取预置并发详情的函数名称。
        :type FunctionName: str
        :param Namespace: 函数所在的命名空间，默认为default。
        :type Namespace: str
        :param Qualifier: 函数版本号，不传则返回函数所有版本的预置并发信息。
        :type Qualifier: str
        """
        self.FunctionName = None
        self.Namespace = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetProvisionedConcurrencyConfigResponse(AbstractModel):
    """GetProvisionedConcurrencyConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param UnallocatedConcurrencyNum: 该函数剩余可配置的预置并发数。
        :type UnallocatedConcurrencyNum: int
        :param Allocated: 函数已预置的并发配置详情。
        :type Allocated: list of VersionProvisionedConcurrencyInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UnallocatedConcurrencyNum = None
        self.Allocated = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UnallocatedConcurrencyNum = params.get("UnallocatedConcurrencyNum")
        if params.get("Allocated") is not None:
            self.Allocated = []
            for item in params.get("Allocated"):
                obj = VersionProvisionedConcurrencyInfo()
                obj._deserialize(item)
                self.Allocated.append(obj)
        self.RequestId = params.get("RequestId")


class GetRequestStatusRequest(AbstractModel):
    """GetRequestStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param FunctionRequestId: 需要查询状态的请求 id
        :type FunctionRequestId: str
        :param Namespace: 函数的所在的命名空间
        :type Namespace: str
        :param StartTime: 查询的开始时间，例如：2017-05-16 20:00:00，不填默认为当前时间 - 15min
        :type StartTime: str
        :param EndTime: 查询的结束时间，例如：2017-05-16 20:59:59，不填默认为当前时间。EndTime 需要晚于 StartTime。
        :type EndTime: str
        """
        self.FunctionName = None
        self.FunctionRequestId = None
        self.Namespace = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.FunctionRequestId = params.get("FunctionRequestId")
        self.Namespace = params.get("Namespace")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestStatusResponse(AbstractModel):
    """GetRequestStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 函数运行状态的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Data: 函数运行状态数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of RequestStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RequestStatus()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class GetReservedConcurrencyConfigRequest(AbstractModel):
    """GetReservedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 需要获取最大独占配额详情的函数名称。
        :type FunctionName: str
        :param Namespace: 函数所在的命名空间，默认为default。
        :type Namespace: str
        """
        self.FunctionName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetReservedConcurrencyConfigResponse(AbstractModel):
    """GetReservedConcurrencyConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReservedMem: 该函数的最大独占配额。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMem: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReservedMem = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReservedMem = params.get("ReservedMem")
        self.RequestId = params.get("RequestId")


class ImageConfig(AbstractModel):
    """TCR镜像信息描述

    """

    def __init__(self):
        r"""
        :param ImageType: 镜像仓库类型，个人版或者企业版：personal/enterprise
        :type ImageType: str
        :param ImageUri: {domain}/{namespace}/{imageName}:{tag}@{digest}
        :type ImageUri: str
        :param RegistryId: 用于企业版TCR获取镜像拉取临时凭证，ImageType为"enterprise"时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryId: str
        :param EntryPoint: 参数已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type EntryPoint: str
        :param Command: 容器的启动命令。该参数为可选参数，如果不填写，则默认使用 Dockerfile 中的 Entrypoint。传入规范，填写可运行的指令，例如 python
注意：此字段可能返回 null，表示取不到有效值。
        :type Command: str
        :param Args: 容器的启动参数。该参数为可选参数，如果不填写，则默认使用 Dockerfile 中的 CMD。传入规范，以“空格”作为参数的分割标识，例如 -u app.py
注意：此字段可能返回 null，表示取不到有效值。
        :type Args: str
        """
        self.ImageType = None
        self.ImageUri = None
        self.RegistryId = None
        self.EntryPoint = None
        self.Command = None
        self.Args = None


    def _deserialize(self, params):
        self.ImageType = params.get("ImageType")
        self.ImageUri = params.get("ImageUri")
        self.RegistryId = params.get("RegistryId")
        self.EntryPoint = params.get("EntryPoint")
        self.Command = params.get("Command")
        self.Args = params.get("Args")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeFunctionRequest(AbstractModel):
    """InvokeFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param Qualifier: 触发函数的版本号或别名，默认值为$DEFAULT
        :type Qualifier: str
        :param Event: 运行函数时的参数，以json格式传入，最大支持的参数长度是 6MB。该字段信息对应函数 [event 入参](https://cloud.tencent.com/document/product/583/9210#.E5.87.BD.E6.95.B0.E5.85.A5.E5.8F.82.3Ca-id.3D.22input.22.3E.3C.2Fa.3E)。
        :type Event: str
        :param LogType: 返回值会包含4KB的日志，可选值为None和Tail，默认值为None。当该值为Tail时，返回参数中的Log字段会包含对应的函数执行日志
        :type LogType: str
        :param Namespace: 命名空间，不填默认为 default
        :type Namespace: str
        :param RoutingKey: 函数灰度流量控制调用，以json格式传入，例如{"k":"v"}，注意kv都需要是字符串类型，最大支持的参数长度是1024字节
        :type RoutingKey: str
        """
        self.FunctionName = None
        self.Qualifier = None
        self.Event = None
        self.LogType = None
        self.Namespace = None
        self.RoutingKey = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Event = params.get("Event")
        self.LogType = params.get("LogType")
        self.Namespace = params.get("Namespace")
        self.RoutingKey = params.get("RoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeFunctionResponse(AbstractModel):
    """InvokeFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 函数执行结果
        :type Result: :class:`tencentcloud.scf.v20180416.models.Result`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Result()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class InvokeRequest(AbstractModel):
    """Invoke请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param InvocationType: 同步调用请使用[同步 Invoke 调用接口](https://cloud.tencent.com/document/product/583/58400) 或填写同步调用参数 RequestResponse ，建议使用同步调用接口以获取最佳性能；异步调用填写 Event；默认为同步。接口超时时间为 300s，更长超时时间请使用异步调用。
        :type InvocationType: str
        :param Qualifier: 触发函数的版本号或别名，默认值为 $LATEST
        :type Qualifier: str
        :param ClientContext: 运行函数时的参数，以json格式传入，同步调用最大支持 6MB，异步调用最大支持 128 KB。该字段信息对应函数 [event 入参](https://cloud.tencent.com/document/product/583/9210#.E5.87.BD.E6.95.B0.E5.85.A5.E5.8F.82.3Ca-id.3D.22input.22.3E.3C.2Fa.3E)。
        :type ClientContext: str
        :param LogType: 异步调用该字段返回为空。
        :type LogType: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param RoutingKey: 函数灰度流量控制调用，以json格式传入，例如{"k":"v"}，注意kv都需要是字符串类型，最大支持的参数长度是1024字节
        :type RoutingKey: str
        """
        self.FunctionName = None
        self.InvocationType = None
        self.Qualifier = None
        self.ClientContext = None
        self.LogType = None
        self.Namespace = None
        self.RoutingKey = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.InvocationType = params.get("InvocationType")
        self.Qualifier = params.get("Qualifier")
        self.ClientContext = params.get("ClientContext")
        self.LogType = params.get("LogType")
        self.Namespace = params.get("Namespace")
        self.RoutingKey = params.get("RoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeResponse(AbstractModel):
    """Invoke返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 函数执行结果
        :type Result: :class:`tencentcloud.scf.v20180416.models.Result`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Result()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class LayerVersionInfo(AbstractModel):
    """层版本信息

    """

    def __init__(self):
        r"""
        :param CompatibleRuntimes: 版本适用的运行时
注意：此字段可能返回 null，表示取不到有效值。
        :type CompatibleRuntimes: list of str
        :param AddTime: 创建时间
        :type AddTime: str
        :param Description: 版本描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param LicenseInfo: 许可证信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseInfo: str
        :param LayerVersion: 版本号
        :type LayerVersion: int
        :param LayerName: 层名称
        :type LayerName: str
        :param Status: 层的具体版本当前状态，状态值[参考此处](https://cloud.tencent.com/document/product/583/47175#.E5.B1.82.EF.BC.88layer.EF.BC.89.E7.8A.B6.E6.80.81)
        :type Status: str
        """
        self.CompatibleRuntimes = None
        self.AddTime = None
        self.Description = None
        self.LicenseInfo = None
        self.LayerVersion = None
        self.LayerName = None
        self.Status = None


    def _deserialize(self, params):
        self.CompatibleRuntimes = params.get("CompatibleRuntimes")
        self.AddTime = params.get("AddTime")
        self.Description = params.get("Description")
        self.LicenseInfo = params.get("LicenseInfo")
        self.LayerVersion = params.get("LayerVersion")
        self.LayerName = params.get("LayerName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LayerVersionSimple(AbstractModel):
    """指定某个Layer版本

    """

    def __init__(self):
        r"""
        :param LayerName: layer名称
        :type LayerName: str
        :param LayerVersion: 版本号
        :type LayerVersion: int
        """
        self.LayerName = None
        self.LayerVersion = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.LayerVersion = params.get("LayerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LimitsInfo(AbstractModel):
    """限制信息

    """

    def __init__(self):
        r"""
        :param NamespacesCount: 命名空间个数限制
        :type NamespacesCount: int
        :param Namespace: 命名空间限制信息
        :type Namespace: list of NamespaceLimit
        """
        self.NamespacesCount = None
        self.Namespace = None


    def _deserialize(self, params):
        self.NamespacesCount = params.get("NamespacesCount")
        if params.get("Namespace") is not None:
            self.Namespace = []
            for item in params.get("Namespace"):
                obj = NamespaceLimit()
                obj._deserialize(item)
                self.Namespace.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAliasesRequest(AbstractModel):
    """ListAliases请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param Namespace: 函数所在的命名空间
        :type Namespace: str
        :param FunctionVersion: 如果提供此参数，则只返回与该函数版本有关联的别名
        :type FunctionVersion: str
        :param Offset: 数据偏移量，默认值为 0
        :type Offset: str
        :param Limit: 返回数据长度，默认值为 20
        :type Limit: str
        """
        self.FunctionName = None
        self.Namespace = None
        self.FunctionVersion = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.FunctionVersion = params.get("FunctionVersion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAliasesResponse(AbstractModel):
    """ListAliases返回参数结构体

    """

    def __init__(self):
        r"""
        :param Aliases: 别名列表
        :type Aliases: list of Alias
        :param TotalCount: 别名总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Aliases = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Aliases") is not None:
            self.Aliases = []
            for item in params.get("Aliases"):
                obj = Alias()
                obj._deserialize(item)
                self.Aliases.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListAsyncEventsRequest(AbstractModel):
    """ListAsyncEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Qualifier: 过滤条件，函数版本
        :type Qualifier: str
        :param InvokeType: 过滤条件，调用类型列表
        :type InvokeType: list of str
        :param Status: 过滤条件，事件状态列表
        :type Status: list of str
        :param StartTimeInterval: 过滤条件，开始执行时间左闭右开区间
        :type StartTimeInterval: :class:`tencentcloud.scf.v20180416.models.TimeInterval`
        :param EndTimeInterval: 过滤条件，结束执行时间左闭右开区间
        :type EndTimeInterval: :class:`tencentcloud.scf.v20180416.models.TimeInterval`
        :param Order: 可选值 ASC 和 DESC，默认 DESC
        :type Order: str
        :param Orderby: 可选值 StartTime 和 EndTime，默认值 StartTime
        :type Orderby: str
        :param Offset: 数据偏移量，默认值为 0
        :type Offset: int
        :param Limit: 返回数据长度，默认值为 20，最大值 100
        :type Limit: int
        :param InvokeRequestId: 过滤条件，事件调用请求id
        :type InvokeRequestId: str
        """
        self.FunctionName = None
        self.Namespace = None
        self.Qualifier = None
        self.InvokeType = None
        self.Status = None
        self.StartTimeInterval = None
        self.EndTimeInterval = None
        self.Order = None
        self.Orderby = None
        self.Offset = None
        self.Limit = None
        self.InvokeRequestId = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        self.InvokeType = params.get("InvokeType")
        self.Status = params.get("Status")
        if params.get("StartTimeInterval") is not None:
            self.StartTimeInterval = TimeInterval()
            self.StartTimeInterval._deserialize(params.get("StartTimeInterval"))
        if params.get("EndTimeInterval") is not None:
            self.EndTimeInterval = TimeInterval()
            self.EndTimeInterval._deserialize(params.get("EndTimeInterval"))
        self.Order = params.get("Order")
        self.Orderby = params.get("Orderby")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InvokeRequestId = params.get("InvokeRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAsyncEventsResponse(AbstractModel):
    """ListAsyncEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 满足过滤条件的事件总数
        :type TotalCount: int
        :param EventList: 异步事件列表
        :type EventList: list of AsyncEvent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EventList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EventList") is not None:
            self.EventList = []
            for item in params.get("EventList"):
                obj = AsyncEvent()
                obj._deserialize(item)
                self.EventList.append(obj)
        self.RequestId = params.get("RequestId")


class ListFunctionsRequest(AbstractModel):
    """ListFunctions请求参数结构体

    """

    def __init__(self):
        r"""
        :param Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC
        :type Order: str
        :param Orderby: 根据哪个字段进行返回结果排序,支持以下字段：AddTime, ModTime, FunctionName
        :type Orderby: str
        :param Offset: 数据偏移量，默认值为 0
        :type Offset: int
        :param Limit: 返回数据长度，默认值为 20
        :type Limit: int
        :param SearchKey: 支持FunctionName模糊匹配
        :type SearchKey: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Description: 函数描述，支持模糊搜索
        :type Description: str
        :param Filters: 过滤条件。
- tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        """
        self.Order = None
        self.Orderby = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.Namespace = None
        self.Description = None
        self.Filters = None


    def _deserialize(self, params):
        self.Order = params.get("Order")
        self.Orderby = params.get("Orderby")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
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
        


class ListFunctionsResponse(AbstractModel):
    """ListFunctions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Functions: 函数列表
        :type Functions: list of Function
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Functions = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Functions") is not None:
            self.Functions = []
            for item in params.get("Functions"):
                obj = Function()
                obj._deserialize(item)
                self.Functions.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListLayerVersionsRequest(AbstractModel):
    """ListLayerVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param LayerName: 层名称
        :type LayerName: str
        :param CompatibleRuntime: 适配的运行时
        :type CompatibleRuntime: list of str
        """
        self.LayerName = None
        self.CompatibleRuntime = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.CompatibleRuntime = params.get("CompatibleRuntime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLayerVersionsResponse(AbstractModel):
    """ListLayerVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param LayerVersions: 层版本列表
        :type LayerVersions: list of LayerVersionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LayerVersions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LayerVersions") is not None:
            self.LayerVersions = []
            for item in params.get("LayerVersions"):
                obj = LayerVersionInfo()
                obj._deserialize(item)
                self.LayerVersions.append(obj)
        self.RequestId = params.get("RequestId")


class ListLayersRequest(AbstractModel):
    """ListLayers请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompatibleRuntime: 适配的运行时
        :type CompatibleRuntime: str
        :param Offset: 偏移位置
        :type Offset: int
        :param Limit: 查询数目限制
        :type Limit: int
        :param SearchKey: 查询key，模糊匹配名称
        :type SearchKey: str
        """
        self.CompatibleRuntime = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.CompatibleRuntime = params.get("CompatibleRuntime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLayersResponse(AbstractModel):
    """ListLayers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Layers: 层列表
        :type Layers: list of LayerVersionInfo
        :param TotalCount: 层总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Layers = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Layers") is not None:
            self.Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionInfo()
                obj._deserialize(item)
                self.Layers.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListNamespacesRequest(AbstractModel):
    """ListNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数据长度，默认值为 20
        :type Limit: int
        :param Offset: 数据的偏移量，默认值为 0
        :type Offset: int
        :param Orderby: 根据哪个字段进行返回结果排序,支持以下字段：Name,Updatetime
        :type Orderby: str
        :param Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC
        :type Order: str
        :param SearchKey: 关键字匹配搜索，Key 可选值为 Namespace 和 Description，多个搜索条件之间是与的关系
        :type SearchKey: list of SearchKey
        """
        self.Limit = None
        self.Offset = None
        self.Orderby = None
        self.Order = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Orderby = params.get("Orderby")
        self.Order = params.get("Order")
        if params.get("SearchKey") is not None:
            self.SearchKey = []
            for item in params.get("SearchKey"):
                obj = SearchKey()
                obj._deserialize(item)
                self.SearchKey.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListNamespacesResponse(AbstractModel):
    """ListNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param Namespaces: namespace详情
        :type Namespaces: list of Namespace
        :param TotalCount: 返回的namespace数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Namespaces = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Namespaces") is not None:
            self.Namespaces = []
            for item in params.get("Namespaces"):
                obj = Namespace()
                obj._deserialize(item)
                self.Namespaces.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListTriggersRequest(AbstractModel):
    """ListTriggers请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param Namespace: 命名空间，默认是default
        :type Namespace: str
        :param Offset: 数据偏移量，默认值为 0
        :type Offset: int
        :param Limit: 返回数据长度，默认值为 20
        :type Limit: int
        :param OrderBy: 根据哪个字段进行返回结果排序,支持以下字段：add_time，mod_time，默认mod_time
        :type OrderBy: str
        :param Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC，默认DESC
        :type Order: str
        :param Filters: * Qualifier:
函数版本，别名
        :type Filters: list of Filter
        """
        self.FunctionName = None
        self.Namespace = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.Order = None
        self.Filters = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.Order = params.get("Order")
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
        


class ListTriggersResponse(AbstractModel):
    """ListTriggers返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 触发器总数
        :type TotalCount: int
        :param Triggers: 触发器列表
        :type Triggers: list of TriggerInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Triggers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Triggers") is not None:
            self.Triggers = []
            for item in params.get("Triggers"):
                obj = TriggerInfo()
                obj._deserialize(item)
                self.Triggers.append(obj)
        self.RequestId = params.get("RequestId")


class ListVersionByFunctionRequest(AbstractModel):
    """ListVersionByFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名
        :type FunctionName: str
        :param Namespace: 函数所在命名空间
        :type Namespace: str
        :param Offset: 数据偏移量，默认值为 0
        :type Offset: int
        :param Limit: 返回数据长度，默认值为 20
        :type Limit: int
        :param Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC
        :type Order: str
        :param OrderBy: 根据哪个字段进行返回结果排序,支持以下字段：AddTime, ModTime
        :type OrderBy: str
        """
        self.FunctionName = None
        self.Namespace = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderBy = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListVersionByFunctionResponse(AbstractModel):
    """ListVersionByFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionVersion: 函数版本。
        :type FunctionVersion: list of str
        :param Versions: 函数版本列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Versions: list of FunctionVersion
        :param TotalCount: 函数版本总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FunctionVersion = None
        self.Versions = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionVersion = params.get("FunctionVersion")
        if params.get("Versions") is not None:
            self.Versions = []
            for item in params.get("Versions"):
                obj = FunctionVersion()
                obj._deserialize(item)
                self.Versions.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class LogFilter(AbstractModel):
    """日志过滤条件，用于区分正确与错误日志

    """

    def __init__(self):
        r"""
        :param RetCode: filter.RetCode的取值有：
not0 表示只返回错误日志，
is0 表示只返回正确日志，
TimeLimitExceeded 返回函数调用发生超时的日志，
ResourceLimitExceeded 返回函数调用发生资源超限的日志，
UserCodeException 返回函数调用发生用户代码错误的日志，
无输入则返回所有日志。
        :type RetCode: str
        """
        self.RetCode = None


    def _deserialize(self, params):
        self.RetCode = params.get("RetCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogSearchContext(AbstractModel):
    """日志搜索上下文

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: str
        :param Limit: 日志条数
        :type Limit: int
        :param Keyword: 日志关键词
        :type Keyword: str
        :param Type: 日志类型，支持Application和Platform，默认为Application
        :type Type: str
        """
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Type = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Namespace(AbstractModel):
    """命名空间

    """

    def __init__(self):
        r"""
        :param ModTime: 命名空间创建时间
        :type ModTime: str
        :param AddTime: 命名空间修改时间
        :type AddTime: str
        :param Description: 命名空间描述
        :type Description: str
        :param Name: 命名空间名称
        :type Name: str
        :param Type: 默认default，TCB表示是小程序云开发创建的
        :type Type: str
        """
        self.ModTime = None
        self.AddTime = None
        self.Description = None
        self.Name = None
        self.Type = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.AddTime = params.get("AddTime")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceLimit(AbstractModel):
    """命名空间限制

    """

    def __init__(self):
        r"""
        :param FunctionsCount: 函数总数
        :type FunctionsCount: int
        :param Trigger: Trigger信息
        :type Trigger: :class:`tencentcloud.scf.v20180416.models.TriggerCount`
        :param Namespace: Namespace名称
        :type Namespace: str
        :param ConcurrentExecutions: 并发量
        :type ConcurrentExecutions: int
        :param TimeoutLimit: Timeout限制
        :type TimeoutLimit: int
        :param TestModelLimit: 测试事件限制
注意：此字段可能返回 null，表示取不到有效值。
        :type TestModelLimit: int
        :param InitTimeoutLimit: 初始化超时限制
        :type InitTimeoutLimit: int
        :param RetryNumLimit: 异步重试次数限制
        :type RetryNumLimit: int
        :param MinMsgTTL: 异步重试消息保留时间下限
        :type MinMsgTTL: int
        :param MaxMsgTTL: 异步重试消息保留时间上限
        :type MaxMsgTTL: int
        """
        self.FunctionsCount = None
        self.Trigger = None
        self.Namespace = None
        self.ConcurrentExecutions = None
        self.TimeoutLimit = None
        self.TestModelLimit = None
        self.InitTimeoutLimit = None
        self.RetryNumLimit = None
        self.MinMsgTTL = None
        self.MaxMsgTTL = None


    def _deserialize(self, params):
        self.FunctionsCount = params.get("FunctionsCount")
        if params.get("Trigger") is not None:
            self.Trigger = TriggerCount()
            self.Trigger._deserialize(params.get("Trigger"))
        self.Namespace = params.get("Namespace")
        self.ConcurrentExecutions = params.get("ConcurrentExecutions")
        self.TimeoutLimit = params.get("TimeoutLimit")
        self.TestModelLimit = params.get("TestModelLimit")
        self.InitTimeoutLimit = params.get("InitTimeoutLimit")
        self.RetryNumLimit = params.get("RetryNumLimit")
        self.MinMsgTTL = params.get("MinMsgTTL")
        self.MaxMsgTTL = params.get("MaxMsgTTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceUsage(AbstractModel):
    """名称空间已使用信息

    """

    def __init__(self):
        r"""
        :param Functions: 函数数组
        :type Functions: list of str
        :param Namespace: 命名空间名称
        :type Namespace: str
        :param FunctionsCount: 命名空间函数个数
        :type FunctionsCount: int
        """
        self.Functions = None
        self.Namespace = None
        self.FunctionsCount = None


    def _deserialize(self, params):
        self.Functions = params.get("Functions")
        self.Namespace = params.get("Namespace")
        self.FunctionsCount = params.get("FunctionsCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolParams(AbstractModel):
    """HTTP函数支持其他访问协议的参数

    """

    def __init__(self):
        r"""
        :param WSParams: WebSockets协议支持的参数
注意：此字段可能返回 null，表示取不到有效值。
        :type WSParams: :class:`tencentcloud.scf.v20180416.models.WSParams`
        """
        self.WSParams = None


    def _deserialize(self, params):
        if params.get("WSParams") is not None:
            self.WSParams = WSParams()
            self.WSParams._deserialize(params.get("WSParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicNetConfigIn(AbstractModel):
    """公网访问配置

    """

    def __init__(self):
        r"""
        :param PublicNetStatus: 是否开启公网访问能力取值['DISABLE','ENABLE']
        :type PublicNetStatus: str
        :param EipConfig: Eip配置
        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipConfigIn`
        """
        self.PublicNetStatus = None
        self.EipConfig = None


    def _deserialize(self, params):
        self.PublicNetStatus = params.get("PublicNetStatus")
        if params.get("EipConfig") is not None:
            self.EipConfig = EipConfigIn()
            self.EipConfig._deserialize(params.get("EipConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicNetConfigOut(AbstractModel):
    """公网访问配置

    """

    def __init__(self):
        r"""
        :param PublicNetStatus: 是否开启公网访问能力取值['DISABLE','ENABLE']
        :type PublicNetStatus: str
        :param EipConfig: Eip配置
        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipConfigOut`
        """
        self.PublicNetStatus = None
        self.EipConfig = None


    def _deserialize(self, params):
        self.PublicNetStatus = params.get("PublicNetStatus")
        if params.get("EipConfig") is not None:
            self.EipConfig = EipConfigOut()
            self.EipConfig._deserialize(params.get("EipConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishLayerVersionRequest(AbstractModel):
    """PublishLayerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param LayerName: 层名称，支持26个英文字母大小写、数字、连接符和下划线，第一个字符只能以字母开头，最后一个字符不能为连接符或者下划线，名称长度1-64
        :type LayerName: str
        :param CompatibleRuntimes: 层适用的运行时，可多选，可选的值对应函数的 Runtime 可选值。
        :type CompatibleRuntimes: list of str
        :param Content: 层的文件来源或文件内容
        :type Content: :class:`tencentcloud.scf.v20180416.models.Code`
        :param Description: 层的版本的描述
        :type Description: str
        :param LicenseInfo: 层的软件许可证
        :type LicenseInfo: str
        """
        self.LayerName = None
        self.CompatibleRuntimes = None
        self.Content = None
        self.Description = None
        self.LicenseInfo = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.CompatibleRuntimes = params.get("CompatibleRuntimes")
        if params.get("Content") is not None:
            self.Content = Code()
            self.Content._deserialize(params.get("Content"))
        self.Description = params.get("Description")
        self.LicenseInfo = params.get("LicenseInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishLayerVersionResponse(AbstractModel):
    """PublishLayerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param LayerVersion: 本次创建的层的版本号
        :type LayerVersion: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LayerVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LayerVersion = params.get("LayerVersion")
        self.RequestId = params.get("RequestId")


class PublishVersionRequest(AbstractModel):
    """PublishVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 发布函数的名称
        :type FunctionName: str
        :param Description: 函数的描述
        :type Description: str
        :param Namespace: 函数的命名空间
        :type Namespace: str
        """
        self.FunctionName = None
        self.Description = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Description = params.get("Description")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishVersionResponse(AbstractModel):
    """PublishVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionVersion: 函数的版本
        :type FunctionVersion: str
        :param CodeSize: 代码大小
        :type CodeSize: int
        :param MemorySize: 最大可用内存
        :type MemorySize: int
        :param Description: 函数的描述
        :type Description: str
        :param Handler: 函数的入口
        :type Handler: str
        :param Timeout: 函数的超时时间
        :type Timeout: int
        :param Runtime: 函数的运行环境
        :type Runtime: str
        :param Namespace: 函数的命名空间
        :type Namespace: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FunctionVersion = None
        self.CodeSize = None
        self.MemorySize = None
        self.Description = None
        self.Handler = None
        self.Timeout = None
        self.Runtime = None
        self.Namespace = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionVersion = params.get("FunctionVersion")
        self.CodeSize = params.get("CodeSize")
        self.MemorySize = params.get("MemorySize")
        self.Description = params.get("Description")
        self.Handler = params.get("Handler")
        self.Timeout = params.get("Timeout")
        self.Runtime = params.get("Runtime")
        self.Namespace = params.get("Namespace")
        self.RequestId = params.get("RequestId")


class PutProvisionedConcurrencyConfigRequest(AbstractModel):
    """PutProvisionedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 需要设置预置并发的函数的名称
        :type FunctionName: str
        :param Qualifier: 函数的版本号，注：$LATEST版本不支持预置并发
        :type Qualifier: str
        :param VersionProvisionedConcurrencyNum: 预置并发数量，注：所有版本的预置并发数总和存在上限限制，当前的上限是：函数最大并发配额 - 100
        :type VersionProvisionedConcurrencyNum: int
        :param Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        :param TriggerActions: 定时预置任务
        :type TriggerActions: list of TriggerAction
        """
        self.FunctionName = None
        self.Qualifier = None
        self.VersionProvisionedConcurrencyNum = None
        self.Namespace = None
        self.TriggerActions = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.VersionProvisionedConcurrencyNum = params.get("VersionProvisionedConcurrencyNum")
        self.Namespace = params.get("Namespace")
        if params.get("TriggerActions") is not None:
            self.TriggerActions = []
            for item in params.get("TriggerActions"):
                obj = TriggerAction()
                obj._deserialize(item)
                self.TriggerActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutProvisionedConcurrencyConfigResponse(AbstractModel):
    """PutProvisionedConcurrencyConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PutReservedConcurrencyConfigRequest(AbstractModel):
    """PutReservedConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 需要设置最大独占配额的函数的名称
        :type FunctionName: str
        :param ReservedConcurrencyMem: 函数最大独占配额，注：函数的最大独占配额内存总和上限：用户总并发内存配额 - 12800
        :type ReservedConcurrencyMem: int
        :param Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        """
        self.FunctionName = None
        self.ReservedConcurrencyMem = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.ReservedConcurrencyMem = params.get("ReservedConcurrencyMem")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutReservedConcurrencyConfigResponse(AbstractModel):
    """PutReservedConcurrencyConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PutTotalConcurrencyConfigRequest(AbstractModel):
    """PutTotalConcurrencyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param TotalConcurrencyMem: 账号并发内存配额，注：账号并发内存配额下限：用户已用并发内存总额 + 12800
        :type TotalConcurrencyMem: int
        :param Namespace: 命名空间，默认为default
        :type Namespace: str
        """
        self.TotalConcurrencyMem = None
        self.Namespace = None


    def _deserialize(self, params):
        self.TotalConcurrencyMem = params.get("TotalConcurrencyMem")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutTotalConcurrencyConfigResponse(AbstractModel):
    """PutTotalConcurrencyConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RequestStatus(AbstractModel):
    """函数运行状态

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数的名称
        :type FunctionName: str
        :param RetMsg: 函数执行完成后的返回值
        :type RetMsg: str
        :param RequestId: 查询的请求 id
        :type RequestId: str
        :param StartTime: 请求开始时间
        :type StartTime: str
        :param RetCode: 请求执行结果， 0 表示执行成功，1表示运行中，-1 表示执行异常。
        :type RetCode: int
        :param Duration: 请求运行耗时，单位：ms
        :type Duration: float
        :param MemUsage: 请求消耗内存，单位为 MB
        :type MemUsage: float
        :param RetryNum: 重试次数
        :type RetryNum: int
        """
        self.FunctionName = None
        self.RetMsg = None
        self.RequestId = None
        self.StartTime = None
        self.RetCode = None
        self.Duration = None
        self.MemUsage = None
        self.RetryNum = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.RetMsg = params.get("RetMsg")
        self.RequestId = params.get("RequestId")
        self.StartTime = params.get("StartTime")
        self.RetCode = params.get("RetCode")
        self.Duration = params.get("Duration")
        self.MemUsage = params.get("MemUsage")
        self.RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Result(AbstractModel):
    """运行函数的返回

    """

    def __init__(self):
        r"""
        :param Log: 表示执行过程中的日志输出，异步调用返回为空
        :type Log: str
        :param RetMsg: 表示执行函数的返回，异步调用返回为空
        :type RetMsg: str
        :param ErrMsg: 表示执行函数的错误返回信息，异步调用返回为空
        :type ErrMsg: str
        :param MemUsage: 执行函数时的内存大小，单位为Byte，异步调用返回为空
        :type MemUsage: int
        :param Duration: 表示执行函数的耗时，单位是毫秒，异步调用返回为空
        :type Duration: float
        :param BillDuration: 表示函数的计费耗时，单位是毫秒，异步调用返回为空
        :type BillDuration: int
        :param FunctionRequestId: 此次函数执行的Id
        :type FunctionRequestId: str
        :param InvokeResult: 0为正确，异步调用返回为空
        :type InvokeResult: int
        """
        self.Log = None
        self.RetMsg = None
        self.ErrMsg = None
        self.MemUsage = None
        self.Duration = None
        self.BillDuration = None
        self.FunctionRequestId = None
        self.InvokeResult = None


    def _deserialize(self, params):
        self.Log = params.get("Log")
        self.RetMsg = params.get("RetMsg")
        self.ErrMsg = params.get("ErrMsg")
        self.MemUsage = params.get("MemUsage")
        self.Duration = params.get("Duration")
        self.BillDuration = params.get("BillDuration")
        self.FunctionRequestId = params.get("FunctionRequestId")
        self.InvokeResult = params.get("InvokeResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryConfig(AbstractModel):
    """异步重试配置

    """

    def __init__(self):
        r"""
        :param RetryNum: 重试次数
        :type RetryNum: int
        """
        self.RetryNum = None


    def _deserialize(self, params):
        self.RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoutingConfig(AbstractModel):
    """别名的版本路由配置

    """

    def __init__(self):
        r"""
        :param AdditionalVersionWeights: 随机权重路由附加版本
        :type AdditionalVersionWeights: list of VersionWeight
        :param AddtionVersionMatchs: 规则路由附加版本
        :type AddtionVersionMatchs: list of VersionMatch
        """
        self.AdditionalVersionWeights = None
        self.AddtionVersionMatchs = None


    def _deserialize(self, params):
        if params.get("AdditionalVersionWeights") is not None:
            self.AdditionalVersionWeights = []
            for item in params.get("AdditionalVersionWeights"):
                obj = VersionWeight()
                obj._deserialize(item)
                self.AdditionalVersionWeights.append(obj)
        if params.get("AddtionVersionMatchs") is not None:
            self.AddtionVersionMatchs = []
            for item in params.get("AddtionVersionMatchs"):
                obj = VersionMatch()
                obj._deserialize(item)
                self.AddtionVersionMatchs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKey(AbstractModel):
    """包含搜索关键字和对应的内容

    """

    def __init__(self):
        r"""
        :param Key: 搜索关键字
        :type Key: str
        :param Value: 搜索内容
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
        


class StatusReason(AbstractModel):
    """状态原因描述

    """

    def __init__(self):
        r"""
        :param ErrorCode: 错误码
        :type ErrorCode: str
        :param ErrorMessage: 错误描述
        :type ErrorMessage: str
        """
        self.ErrorCode = None
        self.ErrorMessage = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """函数标签

    """

    def __init__(self):
        r"""
        :param Key: 标签的key
        :type Key: str
        :param Value: 标签的value
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
        


class TerminateAsyncEventRequest(AbstractModel):
    """TerminateAsyncEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param InvokeRequestId: 终止的调用请求id
        :type InvokeRequestId: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param GraceShutdown: 该参数已下线
        :type GraceShutdown: bool
        """
        self.FunctionName = None
        self.InvokeRequestId = None
        self.Namespace = None
        self.GraceShutdown = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.InvokeRequestId = params.get("InvokeRequestId")
        self.Namespace = params.get("Namespace")
        self.GraceShutdown = params.get("GraceShutdown")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateAsyncEventResponse(AbstractModel):
    """TerminateAsyncEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TimeInterval(AbstractModel):
    """左闭右开时间区间，包括起始时间和结束时间，格式为"%Y-%m-%d %H:%M:%S"

    """

    def __init__(self):
        r"""
        :param Start: 起始时间（包括在内），格式"%Y-%m-%d %H:%M:%S"
        :type Start: str
        :param End: 结束时间（不包括在内），格式"%Y-%m-%d %H:%M:%S"
        :type End: str
        """
        self.Start = None
        self.End = None


    def _deserialize(self, params):
        self.Start = params.get("Start")
        self.End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Trigger(AbstractModel):
    """触发器类型

    """

    def __init__(self):
        r"""
        :param ModTime: 触发器最后修改时间
        :type ModTime: str
        :param Type: 触发器类型
        :type Type: str
        :param TriggerDesc: 触发器详细配置
        :type TriggerDesc: str
        :param TriggerName: 触发器名称
        :type TriggerName: str
        :param AddTime: 触发器创建时间
        :type AddTime: str
        :param Enable: 使能开关
        :type Enable: int
        :param CustomArgument: 客户自定义参数
        :type CustomArgument: str
        :param AvailableStatus: 触发器状态
        :type AvailableStatus: str
        :param ResourceId: 触发器最小资源ID
        :type ResourceId: str
        :param BindStatus: 触发器和云函数绑定状态
        :type BindStatus: str
        :param TriggerAttribute: 触发器类型，双向表示两侧控制台均可操作，单向表示SCF控制台单向创建
        :type TriggerAttribute: str
        :param Qualifier: 触发器绑定的别名或版本
        :type Qualifier: str
        """
        self.ModTime = None
        self.Type = None
        self.TriggerDesc = None
        self.TriggerName = None
        self.AddTime = None
        self.Enable = None
        self.CustomArgument = None
        self.AvailableStatus = None
        self.ResourceId = None
        self.BindStatus = None
        self.TriggerAttribute = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.TriggerName = params.get("TriggerName")
        self.AddTime = params.get("AddTime")
        self.Enable = params.get("Enable")
        self.CustomArgument = params.get("CustomArgument")
        self.AvailableStatus = params.get("AvailableStatus")
        self.ResourceId = params.get("ResourceId")
        self.BindStatus = params.get("BindStatus")
        self.TriggerAttribute = params.get("TriggerAttribute")
        self.Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerAction(AbstractModel):
    """预置定时任务动作

    """

    def __init__(self):
        r"""
        :param TriggerName: 定时预置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerName: str
        :param TriggerProvisionedConcurrencyNum: 定时预置并发数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerProvisionedConcurrencyNum: int
        :param TriggerCronConfig: 设置定时触发器的时间配置，cron表达式。Cron 表达式有七个必需字段，按空格分隔。
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerCronConfig: str
        """
        self.TriggerName = None
        self.TriggerProvisionedConcurrencyNum = None
        self.TriggerCronConfig = None


    def _deserialize(self, params):
        self.TriggerName = params.get("TriggerName")
        self.TriggerProvisionedConcurrencyNum = params.get("TriggerProvisionedConcurrencyNum")
        self.TriggerCronConfig = params.get("TriggerCronConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerCount(AbstractModel):
    """TriggerCount描述不同类型触发器的数量

    """

    def __init__(self):
        r"""
        :param Cos: Cos触发器数量
        :type Cos: int
        :param Timer: Timer触发器数量
        :type Timer: int
        :param Cmq: Cmq触发器数量
        :type Cmq: int
        :param Total: 触发器总数
        :type Total: int
        :param Ckafka: Ckafka触发器数量
        :type Ckafka: int
        :param Apigw: Apigw触发器数量
        :type Apigw: int
        :param Cls: Cls触发器数量
        :type Cls: int
        :param Clb: Clb触发器数量
        :type Clb: int
        :param Mps: Mps触发器数量
        :type Mps: int
        :param Cm: Cm触发器数量
        :type Cm: int
        :param Vod: Vod触发器数量
        :type Vod: int
        """
        self.Cos = None
        self.Timer = None
        self.Cmq = None
        self.Total = None
        self.Ckafka = None
        self.Apigw = None
        self.Cls = None
        self.Clb = None
        self.Mps = None
        self.Cm = None
        self.Vod = None


    def _deserialize(self, params):
        self.Cos = params.get("Cos")
        self.Timer = params.get("Timer")
        self.Cmq = params.get("Cmq")
        self.Total = params.get("Total")
        self.Ckafka = params.get("Ckafka")
        self.Apigw = params.get("Apigw")
        self.Cls = params.get("Cls")
        self.Clb = params.get("Clb")
        self.Mps = params.get("Mps")
        self.Cm = params.get("Cm")
        self.Vod = params.get("Vod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerInfo(AbstractModel):
    """触发器信息

    """

    def __init__(self):
        r"""
        :param Enable: 使能开关
        :type Enable: int
        :param Qualifier: 函数版本或别名
        :type Qualifier: str
        :param TriggerName: 触发器名称
        :type TriggerName: str
        :param Type: 触发器类型
        :type Type: str
        :param TriggerDesc: 触发器详细配置
        :type TriggerDesc: str
        :param AvailableStatus: 触发器是否可用
        :type AvailableStatus: str
        :param CustomArgument: 客户自定义参数
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomArgument: str
        :param AddTime: 触发器创建时间
        :type AddTime: str
        :param ModTime: 触发器最后修改时间
        :type ModTime: str
        :param ResourceId: 触发器最小资源ID
        :type ResourceId: str
        :param BindStatus: 触发器和云函数绑定状态
        :type BindStatus: str
        :param TriggerAttribute: 触发器类型，双向表示两侧控制台均可操作，单向表示SCF控制台单向创建
        :type TriggerAttribute: str
        """
        self.Enable = None
        self.Qualifier = None
        self.TriggerName = None
        self.Type = None
        self.TriggerDesc = None
        self.AvailableStatus = None
        self.CustomArgument = None
        self.AddTime = None
        self.ModTime = None
        self.ResourceId = None
        self.BindStatus = None
        self.TriggerAttribute = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.Qualifier = params.get("Qualifier")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.AvailableStatus = params.get("AvailableStatus")
        self.CustomArgument = params.get("CustomArgument")
        self.AddTime = params.get("AddTime")
        self.ModTime = params.get("ModTime")
        self.ResourceId = params.get("ResourceId")
        self.BindStatus = params.get("BindStatus")
        self.TriggerAttribute = params.get("TriggerAttribute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param Name: 别名的名称
        :type Name: str
        :param FunctionVersion: 别名指向的主版本
        :type FunctionVersion: str
        :param Namespace: 函数所在的命名空间
        :type Namespace: str
        :param RoutingConfig: 别名的路由信息，需要为别名指定附加版本时，必须提供此参数
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param Description: 别名的描述
        :type Description: str
        """
        self.FunctionName = None
        self.Name = None
        self.FunctionVersion = None
        self.Namespace = None
        self.RoutingConfig = None
        self.Description = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Name = params.get("Name")
        self.FunctionVersion = params.get("FunctionVersion")
        self.Namespace = params.get("Namespace")
        if params.get("RoutingConfig") is not None:
            self.RoutingConfig = RoutingConfig()
            self.RoutingConfig._deserialize(params.get("RoutingConfig"))
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFunctionCodeRequest(AbstractModel):
    """UpdateFunctionCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 要修改的函数名称
        :type FunctionName: str
        :param Handler: 函数处理方法名称。名称格式支持“文件名称.函数名称”形式（java 名称格式 包名.类名::方法名），文件名称和函数名称之间以"."隔开，文件名称和函数名称要求以字母开始和结尾，中间允许插入字母、数字、下划线和连接符，文件名称和函数名字的长度要求 2-60 个字符
        :type Handler: str
        :param CosBucketName: 对象存储桶名称
        :type CosBucketName: str
        :param CosObjectName: 对象存储对象路径
        :type CosObjectName: str
        :param ZipFile: 包含函数代码文件及其依赖项的 zip 格式文件，使用该接口时要求将 zip 文件的内容转成 base64 编码，最大支持20M
        :type ZipFile: str
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        :param CosBucketRegion: 对象存储的地域，注：北京分为ap-beijing和ap-beijing-1
        :type CosBucketRegion: str
        :param InstallDependency: 是否自动安装依赖
        :type InstallDependency: str
        :param EnvId: 函数所属环境
        :type EnvId: str
        :param Publish: 在更新时是否同步发布新版本，默认为：FALSE，不发布
        :type Publish: str
        :param Code: 函数代码
        :type Code: :class:`tencentcloud.scf.v20180416.models.Code`
        :param CodeSource: 代码来源方式，支持 ZipFile, Cos, Inline 之一
        :type CodeSource: str
        """
        self.FunctionName = None
        self.Handler = None
        self.CosBucketName = None
        self.CosObjectName = None
        self.ZipFile = None
        self.Namespace = None
        self.CosBucketRegion = None
        self.InstallDependency = None
        self.EnvId = None
        self.Publish = None
        self.Code = None
        self.CodeSource = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Handler = params.get("Handler")
        self.CosBucketName = params.get("CosBucketName")
        self.CosObjectName = params.get("CosObjectName")
        self.ZipFile = params.get("ZipFile")
        self.Namespace = params.get("Namespace")
        self.CosBucketRegion = params.get("CosBucketRegion")
        self.InstallDependency = params.get("InstallDependency")
        self.EnvId = params.get("EnvId")
        self.Publish = params.get("Publish")
        if params.get("Code") is not None:
            self.Code = Code()
            self.Code._deserialize(params.get("Code"))
        self.CodeSource = params.get("CodeSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFunctionCodeResponse(AbstractModel):
    """UpdateFunctionCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFunctionConfigurationRequest(AbstractModel):
    """UpdateFunctionConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 要修改的函数名称
        :type FunctionName: str
        :param Description: 函数描述。最大支持 1000 个英文字母、数字、空格、逗号和英文句号，支持中文
        :type Description: str
        :param MemorySize: 函数运行时内存大小，默认为 128 M，可选范64M、128 M-3072 M，以 128MB 为阶梯。
        :type MemorySize: int
        :param Timeout: 函数最长执行时间，单位为秒，可选值范 1-900 秒，默认为 3 秒
        :type Timeout: int
        :param Runtime: 函数运行环境，目前仅支持 Python2.7，Python3.6，Nodejs6.10，Nodejs8.9，Nodejs10.15，Nodejs12.16， PHP5， PHP7，Go1 ， Java8和CustomRuntime
        :type Runtime: str
        :param Environment: 函数的环境变量
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param Namespace: 函数所属命名空间
        :type Namespace: str
        :param VpcConfig: 函数的私有网络配置
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        :param Role: 函数绑定的角色
        :type Role: str
        :param InstallDependency: [在线依赖安装](https://cloud.tencent.com/document/product/583/37920)，TRUE 表示安装，默认值为 FALSE。仅支持 Node.js 函数。
        :type InstallDependency: str
        :param ClsLogsetId: 日志投递到的cls日志集ID
        :type ClsLogsetId: str
        :param ClsTopicId: 日志投递到的cls Topic ID
        :type ClsTopicId: str
        :param Publish: 在更新时是否同步发布新版本，默认为：FALSE，不发布新版本
        :type Publish: str
        :param L5Enable: 是否开启L5访问能力，TRUE 为开启，FALSE为关闭
        :type L5Enable: str
        :param Layers: 函数要关联的层版本列表，层的版本会按照在列表中顺序依次覆盖。
        :type Layers: list of LayerVersionSimple
        :param DeadLetterConfig: 函数关联的死信队列信息
        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`
        :param PublicNetConfig: 公网访问配置
        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigIn`
        :param CfsConfig: 文件系统配置入参，用于云函数绑定CFS文件系统
        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`
        :param InitTimeout: 函数初始化执行超时时间
        :type InitTimeout: int
        :param ProtocolParams: HTTP函数配置ProtocolType访问协议，当前协议可配置的参数
        :type ProtocolParams: :class:`tencentcloud.scf.v20180416.models.ProtocolParams`
        """
        self.FunctionName = None
        self.Description = None
        self.MemorySize = None
        self.Timeout = None
        self.Runtime = None
        self.Environment = None
        self.Namespace = None
        self.VpcConfig = None
        self.Role = None
        self.InstallDependency = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.Publish = None
        self.L5Enable = None
        self.Layers = None
        self.DeadLetterConfig = None
        self.PublicNetConfig = None
        self.CfsConfig = None
        self.InitTimeout = None
        self.ProtocolParams = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Description = params.get("Description")
        self.MemorySize = params.get("MemorySize")
        self.Timeout = params.get("Timeout")
        self.Runtime = params.get("Runtime")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        self.Namespace = params.get("Namespace")
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.Role = params.get("Role")
        self.InstallDependency = params.get("InstallDependency")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.Publish = params.get("Publish")
        self.L5Enable = params.get("L5Enable")
        if params.get("Layers") is not None:
            self.Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionSimple()
                obj._deserialize(item)
                self.Layers.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self.DeadLetterConfig = DeadLetterConfig()
            self.DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        if params.get("PublicNetConfig") is not None:
            self.PublicNetConfig = PublicNetConfigIn()
            self.PublicNetConfig._deserialize(params.get("PublicNetConfig"))
        if params.get("CfsConfig") is not None:
            self.CfsConfig = CfsConfig()
            self.CfsConfig._deserialize(params.get("CfsConfig"))
        self.InitTimeout = params.get("InitTimeout")
        if params.get("ProtocolParams") is not None:
            self.ProtocolParams = ProtocolParams()
            self.ProtocolParams._deserialize(params.get("ProtocolParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFunctionConfigurationResponse(AbstractModel):
    """UpdateFunctionConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFunctionEventInvokeConfigRequest(AbstractModel):
    """UpdateFunctionEventInvokeConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncTriggerConfig: 异步重试配置信息
        :type AsyncTriggerConfig: :class:`tencentcloud.scf.v20180416.models.AsyncTriggerConfig`
        :param FunctionName: 函数名称
        :type FunctionName: str
        :param Namespace: 函数所属命名空间，默认为default
        :type Namespace: str
        """
        self.AsyncTriggerConfig = None
        self.FunctionName = None
        self.Namespace = None


    def _deserialize(self, params):
        if params.get("AsyncTriggerConfig") is not None:
            self.AsyncTriggerConfig = AsyncTriggerConfig()
            self.AsyncTriggerConfig._deserialize(params.get("AsyncTriggerConfig"))
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFunctionEventInvokeConfigResponse(AbstractModel):
    """UpdateFunctionEventInvokeConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateNamespaceRequest(AbstractModel):
    """UpdateNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间名称
        :type Namespace: str
        :param Description: 命名空间描述
        :type Description: str
        """
        self.Namespace = None
        self.Description = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateNamespaceResponse(AbstractModel):
    """UpdateNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UsageInfo(AbstractModel):
    """已使用的信息

    """

    def __init__(self):
        r"""
        :param NamespacesCount: 命名空间个数
        :type NamespacesCount: int
        :param Namespace: 命名空间详情
        :type Namespace: list of NamespaceUsage
        :param TotalConcurrencyMem: 当前地域用户并发内存配额上限
        :type TotalConcurrencyMem: int
        :param TotalAllocatedConcurrencyMem: 当前地域用户已配置并发内存额度
        :type TotalAllocatedConcurrencyMem: int
        :param UserConcurrencyMemLimit: 用户实际配置的账号并发配额
        :type UserConcurrencyMemLimit: int
        """
        self.NamespacesCount = None
        self.Namespace = None
        self.TotalConcurrencyMem = None
        self.TotalAllocatedConcurrencyMem = None
        self.UserConcurrencyMemLimit = None


    def _deserialize(self, params):
        self.NamespacesCount = params.get("NamespacesCount")
        if params.get("Namespace") is not None:
            self.Namespace = []
            for item in params.get("Namespace"):
                obj = NamespaceUsage()
                obj._deserialize(item)
                self.Namespace.append(obj)
        self.TotalConcurrencyMem = params.get("TotalConcurrencyMem")
        self.TotalAllocatedConcurrencyMem = params.get("TotalAllocatedConcurrencyMem")
        self.UserConcurrencyMemLimit = params.get("UserConcurrencyMemLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Variable(AbstractModel):
    """变量参数

    """

    def __init__(self):
        r"""
        :param Key: 变量的名称
        :type Key: str
        :param Value: 变量的值
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
        


class VersionMatch(AbstractModel):
    """带有匹配规则的函数版本

    """

    def __init__(self):
        r"""
        :param Version: 函数版本名称
        :type Version: str
        :param Key: 匹配规则的key，调用时通过传key来匹配规则路由到指定版本
header方式：
key填写"invoke.headers.User"，并在 invoke 调用函数时传参 RoutingKey：{"User":"value"}规则匹配调用
        :type Key: str
        :param Method: 匹配方式。取值范围：
range：范围匹配
exact：字符串精确匹配
        :type Method: str
        :param Expression: range 匹配规则要求：
需要为开区间或闭区间描述 (a,b) [a,b]，其中 a、b 均为整数
exact 匹配规则要求：
字符串精确匹配
        :type Expression: str
        """
        self.Version = None
        self.Key = None
        self.Method = None
        self.Expression = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Key = params.get("Key")
        self.Method = params.get("Method")
        self.Expression = params.get("Expression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionProvisionedConcurrencyInfo(AbstractModel):
    """函数版本的预置并发信息，包括设置预置并发数、已完成预置的并发数和预置任务状态。

    """

    def __init__(self):
        r"""
        :param AllocatedProvisionedConcurrencyNum: 设置的预置并发数。
        :type AllocatedProvisionedConcurrencyNum: int
        :param AvailableProvisionedConcurrencyNum: 当前已完成预置的并发数。
        :type AvailableProvisionedConcurrencyNum: int
        :param Status: 预置任务状态，Done表示已完成，InProgress表示进行中，Failed表示部分或全部失败。
        :type Status: str
        :param StatusReason: 对预置任务状态Status的说明。
        :type StatusReason: str
        :param Qualifier: 函数版本号
        :type Qualifier: str
        :param TriggerActions: 预置并发定时任务。
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerActions: list of TriggerAction
        """
        self.AllocatedProvisionedConcurrencyNum = None
        self.AvailableProvisionedConcurrencyNum = None
        self.Status = None
        self.StatusReason = None
        self.Qualifier = None
        self.TriggerActions = None


    def _deserialize(self, params):
        self.AllocatedProvisionedConcurrencyNum = params.get("AllocatedProvisionedConcurrencyNum")
        self.AvailableProvisionedConcurrencyNum = params.get("AvailableProvisionedConcurrencyNum")
        self.Status = params.get("Status")
        self.StatusReason = params.get("StatusReason")
        self.Qualifier = params.get("Qualifier")
        if params.get("TriggerActions") is not None:
            self.TriggerActions = []
            for item in params.get("TriggerActions"):
                obj = TriggerAction()
                obj._deserialize(item)
                self.TriggerActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionWeight(AbstractModel):
    """带有权重的函数版本

    """

    def __init__(self):
        r"""
        :param Version: 函数版本名称
        :type Version: str
        :param Weight: 该版本的权重
        :type Weight: float
        """
        self.Version = None
        self.Weight = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcConfig(AbstractModel):
    """私有网络参数配置

    """

    def __init__(self):
        r"""
        :param VpcId: 私有网络 的 Id
        :type VpcId: str
        :param SubnetId: 子网的 Id
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WSParams(AbstractModel):
    """HTTP函数通过WebSockets协议访问时的参数

    """

    def __init__(self):
        r"""
        :param IdleTimeOut: 空闲超时时间, 单位秒，默认15s。可配置范围1~1800s。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdleTimeOut: int
        """
        self.IdleTimeOut = None


    def _deserialize(self, params):
        self.IdleTimeOut = params.get("IdleTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        