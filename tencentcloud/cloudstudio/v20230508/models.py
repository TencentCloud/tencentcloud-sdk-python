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


class CreateWorkspaceRequest(AbstractModel):
    """CreateWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 工作空间名称
        :type Name: str
        :param Description: 工作空间描述
        :type Description: str
        :param Specs: 工作空间规格。Standard: 2C4G, Calculation: 4C8G, Profession: 8C16G. 默认是 Standard。
        :type Specs: str
        :param Image: 工作空间基础镜像名称, 默认会使用 All In One 镜像
        :type Image: str
        :param Repository: Git 仓库. 工作空间启动时会自动克隆该仓库
        :type Repository: :class:`tencentcloud.cloudstudio.v20230508.models.GitRepository`
        :param Envs: 环境变量. 会被注入到工作空间中
        :type Envs: list of Env
        :param Extensions: 预装插件. 工作空间启动时, 会自动安装这些插件 
        :type Extensions: list of str
        :param Lifecycle: 工作空间生命周期钩子.  分为三个阶段 init, start, destroy. 分别表示工作空间数据初始化阶段, 工作空间启动阶段, 工作空间关闭阶段.  用户可以自定义 shell 命令. 
        :type Lifecycle: :class:`tencentcloud.cloudstudio.v20230508.models.LifeCycle`
        """
        self.Name = None
        self.Description = None
        self.Specs = None
        self.Image = None
        self.Repository = None
        self.Envs = None
        self.Extensions = None
        self.Lifecycle = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Specs = params.get("Specs")
        self.Image = params.get("Image")
        if params.get("Repository") is not None:
            self.Repository = GitRepository()
            self.Repository._deserialize(params.get("Repository"))
        if params.get("Envs") is not None:
            self.Envs = []
            for item in params.get("Envs"):
                obj = Env()
                obj._deserialize(item)
                self.Envs.append(obj)
        self.Extensions = params.get("Extensions")
        if params.get("Lifecycle") is not None:
            self.Lifecycle = LifeCycle()
            self.Lifecycle._deserialize(params.get("Lifecycle"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceResponse(AbstractModel):
    """CreateWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceKey: 工作空间 SpaceKey
        :type SpaceKey: str
        :param Name: 工作空间名称
        :type Name: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SpaceKey = None
        self.Name = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SpaceKey = params.get("SpaceKey")
        self.Name = params.get("Name")
        self.RequestId = params.get("RequestId")


class CreateWorkspaceTokenRequest(AbstractModel):
    """CreateWorkspaceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceKey: 工作空间 SpaceKey
        :type SpaceKey: str
        :param TokenExpiredLimitSec: token过期时间，单位是秒，默认 3600
        :type TokenExpiredLimitSec: int
        """
        self.SpaceKey = None
        self.TokenExpiredLimitSec = None


    def _deserialize(self, params):
        self.SpaceKey = params.get("SpaceKey")
        self.TokenExpiredLimitSec = params.get("TokenExpiredLimitSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceTokenResponse(AbstractModel):
    """CreateWorkspaceToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param Token: 访问工作空间临时凭证
        :type Token: str
        :param ExpiredTime: token 过期时间
        :type ExpiredTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Token = None
        self.ExpiredTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Token = params.get("Token")
        self.ExpiredTime = params.get("ExpiredTime")
        self.RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 配置名称
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 配置值
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param Images: 镜像列表
        :type Images: list of Image
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Images = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Images") is not None:
            self.Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self.Images.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWorkspacesRequest(AbstractModel):
    """DescribeWorkspaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 工作空间名称过滤条件
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspacesResponse(AbstractModel):
    """DescribeWorkspaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 工作空间列表
        :type Data: list of WorkspaceStatusInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = WorkspaceStatusInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class Env(AbstractModel):
    """环境变量

    """

    def __init__(self):
        r"""
        :param Name: 环境变量 key
        :type Name: str
        :param Value: 环境变量 value
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GitRepository(AbstractModel):
    """Git 仓库

    """

    def __init__(self):
        r"""
        :param Url: Git 仓库地址
        :type Url: str
        :param Branch: Git 仓库分支名或 Tag 名
        :type Branch: str
        """
        self.Url = None
        self.Branch = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Branch = params.get("Branch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    """基础镜像

    """

    def __init__(self):
        r"""
        :param Name: 镜像名称
        :type Name: str
        :param Repository: 镜像仓库
        :type Repository: str
        :param Tags: tag 列表
        :type Tags: list of str
        """
        self.Name = None
        self.Repository = None
        self.Tags = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Repository = params.get("Repository")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifeCycle(AbstractModel):
    """工作空间生命周期自动执行脚本

    """

    def __init__(self):
        r"""
        :param Init: 工作空间首次初始化时执行
        :type Init: list of LifeCycleCommand
        :param Start: 每次工作空间启动时执行
        :type Start: list of LifeCycleCommand
        :param Destroy: 每次工作空间关闭时执行
        :type Destroy: list of LifeCycleCommand
        """
        self.Init = None
        self.Start = None
        self.Destroy = None


    def _deserialize(self, params):
        if params.get("Init") is not None:
            self.Init = []
            for item in params.get("Init"):
                obj = LifeCycleCommand()
                obj._deserialize(item)
                self.Init.append(obj)
        if params.get("Start") is not None:
            self.Start = []
            for item in params.get("Start"):
                obj = LifeCycleCommand()
                obj._deserialize(item)
                self.Start.append(obj)
        if params.get("Destroy") is not None:
            self.Destroy = []
            for item in params.get("Destroy"):
                obj = LifeCycleCommand()
                obj._deserialize(item)
                self.Destroy.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifeCycleCommand(AbstractModel):
    """工作空间生命周期执行指令

    """

    def __init__(self):
        r"""
        :param Name: 指令描述
        :type Name: str
        :param Command: 具体命令
        :type Command: str
        """
        self.Name = None
        self.Command = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkspaceRequest(AbstractModel):
    """ModifyWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceKey: 工作空间 SpaceKey. 更新该工作空间的属性
        :type SpaceKey: str
        :param Name: 工作空间名称
        :type Name: str
        :param Description: 工作空间描述
        :type Description: str
        :param Specs: 工作空间规格。STANDARD: 2C4G, CALCULATION: 4C8G, PROFESSION: 8C16G. 默认是 STANDARD。
        :type Specs: str
        :param Envs: 环境变量. 会被注入到工作空间中
        :type Envs: list of Env
        :param Extensions: 预装插件. 工作空间启动时, 会自动安装这些插件 
        :type Extensions: list of str
        :param Lifecycle: 工作空间生命周期钩子.  分为三个阶段 init, start, destroy. 分别表示工作空间数据初始化阶段, 工作空间启动阶段, 工作空间关闭阶段.  用户可以自定义 shell 命令. 
        :type Lifecycle: :class:`tencentcloud.cloudstudio.v20230508.models.LifeCycle`
        """
        self.SpaceKey = None
        self.Name = None
        self.Description = None
        self.Specs = None
        self.Envs = None
        self.Extensions = None
        self.Lifecycle = None


    def _deserialize(self, params):
        self.SpaceKey = params.get("SpaceKey")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Specs = params.get("Specs")
        if params.get("Envs") is not None:
            self.Envs = []
            for item in params.get("Envs"):
                obj = Env()
                obj._deserialize(item)
                self.Envs.append(obj)
        self.Extensions = params.get("Extensions")
        if params.get("Lifecycle") is not None:
            self.Lifecycle = LifeCycle()
            self.Lifecycle._deserialize(params.get("Lifecycle"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkspaceResponse(AbstractModel):
    """ModifyWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveWorkspaceRequest(AbstractModel):
    """RemoveWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceKey: 工作空间 SpaceKey
        :type SpaceKey: str
        """
        self.SpaceKey = None


    def _deserialize(self, params):
        self.SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveWorkspaceResponse(AbstractModel):
    """RemoveWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunWorkspaceRequest(AbstractModel):
    """RunWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceKey: 工作空间 SpaceKey
        :type SpaceKey: str
        """
        self.SpaceKey = None


    def _deserialize(self, params):
        self.SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunWorkspaceResponse(AbstractModel):
    """RunWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopWorkspaceRequest(AbstractModel):
    """StopWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceKey: 工作空间 SpaceKey
        :type SpaceKey: str
        """
        self.SpaceKey = None


    def _deserialize(self, params):
        self.SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopWorkspaceResponse(AbstractModel):
    """StopWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WorkspaceStatusInfo(AbstractModel):
    """获取用户工作空间返回信息

    """

    def __init__(self):
        r"""
        :param Id: 工作空间 ID
        :type Id: int
        :param Name: 工作空间名称
        :type Name: str
        :param SpaceKey: 工作空间标识
        :type SpaceKey: str
        :param Status: 工作空间状态
        :type Status: str
        :param Cpu: CPU数量
        :type Cpu: int
        :param Memory: 内存
        :type Memory: int
        :param Icon: 工作空间图标
注意：此字段可能返回 null，表示取不到有效值。
        :type Icon: str
        :param StatusReason: 工作空间状态, 异常原因
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusReason: str
        :param Description: 工作空间描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param WorkspaceType: 工作空间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceType: str
        :param VersionControlUrl: Git 仓库 HTTPS 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlUrl: str
        :param VersionControlRef: Git 仓库引用。指定分支使用 /refs/heads/{分支名}, 指定 Tag 用 /refs/tags/{Tag名}
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlRef: str
        :param LastOpsDate: 最后操作时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOpsDate: str
        :param CreateDate: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        """
        self.Id = None
        self.Name = None
        self.SpaceKey = None
        self.Status = None
        self.Cpu = None
        self.Memory = None
        self.Icon = None
        self.StatusReason = None
        self.Description = None
        self.WorkspaceType = None
        self.VersionControlUrl = None
        self.VersionControlRef = None
        self.LastOpsDate = None
        self.CreateDate = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.SpaceKey = params.get("SpaceKey")
        self.Status = params.get("Status")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Icon = params.get("Icon")
        self.StatusReason = params.get("StatusReason")
        self.Description = params.get("Description")
        self.WorkspaceType = params.get("WorkspaceType")
        self.VersionControlUrl = params.get("VersionControlUrl")
        self.VersionControlRef = params.get("VersionControlRef")
        self.LastOpsDate = params.get("LastOpsDate")
        self.CreateDate = params.get("CreateDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        