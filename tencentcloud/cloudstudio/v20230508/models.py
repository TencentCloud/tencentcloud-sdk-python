# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
    r"""CreateWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 工作空间名称, 长度限制 2~64
        :type Name: str
        :param _Description: 工作空间描述, 长度限制 0~255
        :type Description: str
        :param _Specs: 工作空间规格。Standard: 2C4G, Calculation: 4C8G, Profession: 8C16G. 默认是 Standard。
        :type Specs: str
        :param _Image: 工作空间基础镜像名称, 默认会使用 All In One 镜像, 长度限制 1~255
        :type Image: str
        :param _Repository: Git 仓库. 工作空间启动时会自动克隆该仓库
        :type Repository: :class:`tencentcloud.cloudstudio.v20230508.models.GitRepository`
        :param _Envs: 环境变量. 会被注入到工作空间中
        :type Envs: list of Env
        :param _Extensions: 预装插件. 工作空间启动时, 会自动安装这些插件。长度限制: 0~10
        :type Extensions: list of str
        :param _Lifecycle: 工作空间生命周期钩子.  分为三个阶段 init, start, destroy. 分别表示工作空间数据初始化阶段, 工作空间启动阶段, 工作空间关闭阶段.  用户可以自定义 shell 命令. 
        :type Lifecycle: :class:`tencentcloud.cloudstudio.v20230508.models.LifeCycle`
        :param _TenantAppId: 应用名称
        :type TenantAppId: int
        :param _TenantUin: 用户UIN
        :type TenantUin: str
        :param _TenantUniqVpcId: VPCID
        :type TenantUniqVpcId: str
        :param _TenantSubnetId: 子网ID
        :type TenantSubnetId: str
        :param _Region: 地域
        :type Region: str
        """
        self._Name = None
        self._Description = None
        self._Specs = None
        self._Image = None
        self._Repository = None
        self._Envs = None
        self._Extensions = None
        self._Lifecycle = None
        self._TenantAppId = None
        self._TenantUin = None
        self._TenantUniqVpcId = None
        self._TenantSubnetId = None
        self._Region = None

    @property
    def Name(self):
        r"""工作空间名称, 长度限制 2~64
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""工作空间描述, 长度限制 0~255
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Specs(self):
        r"""工作空间规格。Standard: 2C4G, Calculation: 4C8G, Profession: 8C16G. 默认是 Standard。
        :rtype: str
        """
        return self._Specs

    @Specs.setter
    def Specs(self, Specs):
        self._Specs = Specs

    @property
    def Image(self):
        r"""工作空间基础镜像名称, 默认会使用 All In One 镜像, 长度限制 1~255
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Repository(self):
        r"""Git 仓库. 工作空间启动时会自动克隆该仓库
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.GitRepository`
        """
        return self._Repository

    @Repository.setter
    def Repository(self, Repository):
        self._Repository = Repository

    @property
    def Envs(self):
        r"""环境变量. 会被注入到工作空间中
        :rtype: list of Env
        """
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def Extensions(self):
        r"""预装插件. 工作空间启动时, 会自动安装这些插件。长度限制: 0~10
        :rtype: list of str
        """
        return self._Extensions

    @Extensions.setter
    def Extensions(self, Extensions):
        self._Extensions = Extensions

    @property
    def Lifecycle(self):
        r"""工作空间生命周期钩子.  分为三个阶段 init, start, destroy. 分别表示工作空间数据初始化阶段, 工作空间启动阶段, 工作空间关闭阶段.  用户可以自定义 shell 命令. 
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.LifeCycle`
        """
        return self._Lifecycle

    @Lifecycle.setter
    def Lifecycle(self, Lifecycle):
        self._Lifecycle = Lifecycle

    @property
    def TenantAppId(self):
        r"""应用名称
        :rtype: int
        """
        return self._TenantAppId

    @TenantAppId.setter
    def TenantAppId(self, TenantAppId):
        self._TenantAppId = TenantAppId

    @property
    def TenantUin(self):
        r"""用户UIN
        :rtype: str
        """
        return self._TenantUin

    @TenantUin.setter
    def TenantUin(self, TenantUin):
        self._TenantUin = TenantUin

    @property
    def TenantUniqVpcId(self):
        r"""VPCID
        :rtype: str
        """
        return self._TenantUniqVpcId

    @TenantUniqVpcId.setter
    def TenantUniqVpcId(self, TenantUniqVpcId):
        self._TenantUniqVpcId = TenantUniqVpcId

    @property
    def TenantSubnetId(self):
        r"""子网ID
        :rtype: str
        """
        return self._TenantSubnetId

    @TenantSubnetId.setter
    def TenantSubnetId(self, TenantSubnetId):
        self._TenantSubnetId = TenantSubnetId

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Specs = params.get("Specs")
        self._Image = params.get("Image")
        if params.get("Repository") is not None:
            self._Repository = GitRepository()
            self._Repository._deserialize(params.get("Repository"))
        if params.get("Envs") is not None:
            self._Envs = []
            for item in params.get("Envs"):
                obj = Env()
                obj._deserialize(item)
                self._Envs.append(obj)
        self._Extensions = params.get("Extensions")
        if params.get("Lifecycle") is not None:
            self._Lifecycle = LifeCycle()
            self._Lifecycle._deserialize(params.get("Lifecycle"))
        self._TenantAppId = params.get("TenantAppId")
        self._TenantUin = params.get("TenantUin")
        self._TenantUniqVpcId = params.get("TenantUniqVpcId")
        self._TenantSubnetId = params.get("TenantSubnetId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceResponse(AbstractModel):
    r"""CreateWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceKey: 工作空间 SpaceKey
        :type SpaceKey: str
        :param _Name: 工作空间名称
        :type Name: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpaceKey = None
        self._Name = None
        self._RequestId = None

    @property
    def SpaceKey(self):
        r"""工作空间 SpaceKey
        :rtype: str
        """
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey

    @property
    def Name(self):
        r"""工作空间名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SpaceKey = params.get("SpaceKey")
        self._Name = params.get("Name")
        self._RequestId = params.get("RequestId")


class CreateWorkspaceTokenRequest(AbstractModel):
    r"""CreateWorkspaceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceKey: 工作空间 SpaceKey
        :type SpaceKey: str
        :param _TokenExpiredLimitSec: token过期时间，单位是秒，默认 3600
        :type TokenExpiredLimitSec: int
        :param _Policies: token 授权策略，可选值为 workspace-run-only, all。默认为 workspace-run-only
        :type Policies: list of str
        """
        self._SpaceKey = None
        self._TokenExpiredLimitSec = None
        self._Policies = None

    @property
    def SpaceKey(self):
        r"""工作空间 SpaceKey
        :rtype: str
        """
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey

    @property
    def TokenExpiredLimitSec(self):
        r"""token过期时间，单位是秒，默认 3600
        :rtype: int
        """
        return self._TokenExpiredLimitSec

    @TokenExpiredLimitSec.setter
    def TokenExpiredLimitSec(self, TokenExpiredLimitSec):
        self._TokenExpiredLimitSec = TokenExpiredLimitSec

    @property
    def Policies(self):
        r"""token 授权策略，可选值为 workspace-run-only, all。默认为 workspace-run-only
        :rtype: list of str
        """
        return self._Policies

    @Policies.setter
    def Policies(self, Policies):
        self._Policies = Policies


    def _deserialize(self, params):
        self._SpaceKey = params.get("SpaceKey")
        self._TokenExpiredLimitSec = params.get("TokenExpiredLimitSec")
        self._Policies = params.get("Policies")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceTokenResponse(AbstractModel):
    r"""CreateWorkspaceToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Token: 访问工作空间临时凭证
        :type Token: str
        :param _ExpiredTime: token 过期时间
        :type ExpiredTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def Token(self):
        r"""访问工作空间临时凭证
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiredTime(self):
        r"""token 过期时间
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    r"""DescribeConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 配置名称
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        r"""配置名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigResponse(AbstractModel):
    r"""DescribeConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 配置值
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""配置值
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    r"""DescribeImages请求参数结构体

    """


class DescribeImagesResponse(AbstractModel):
    r"""DescribeImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Images: 镜像列表
        :type Images: list of Image
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Images = None
        self._RequestId = None

    @property
    def Images(self):
        r"""镜像列表
        :rtype: list of Image
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Images") is not None:
            self._Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self._Images.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWorkspacesRequest(AbstractModel):
    r"""DescribeWorkspaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 工作空间名称过滤条件
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        r"""工作空间名称过滤条件
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspacesResponse(AbstractModel):
    r"""DescribeWorkspaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 工作空间列表
        :type Data: list of WorkspaceStatusInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""工作空间列表
        :rtype: list of WorkspaceStatusInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = WorkspaceStatusInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class Env(AbstractModel):
    r"""环境变量

    """

    def __init__(self):
        r"""
        :param _Name: 环境变量 key
        :type Name: str
        :param _Value: 环境变量 value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""环境变量 key
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""环境变量 value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GitRepository(AbstractModel):
    r"""Git 仓库

    """

    def __init__(self):
        r"""
        :param _Url: Git 仓库地址
        :type Url: str
        :param _Branch: Git 仓库分支名或 Tag 名
        :type Branch: str
        """
        self._Url = None
        self._Branch = None

    @property
    def Url(self):
        r"""Git 仓库地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Branch(self):
        r"""Git 仓库分支名或 Tag 名
        :rtype: str
        """
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Branch = params.get("Branch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    r"""基础镜像

    """

    def __init__(self):
        r"""
        :param _Name: 镜像名称
        :type Name: str
        :param _Repository: 镜像仓库
        :type Repository: str
        :param _Tags: tag 列表
        :type Tags: list of str
        """
        self._Name = None
        self._Repository = None
        self._Tags = None

    @property
    def Name(self):
        r"""镜像名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Repository(self):
        r"""镜像仓库
        :rtype: str
        """
        return self._Repository

    @Repository.setter
    def Repository(self, Repository):
        self._Repository = Repository

    @property
    def Tags(self):
        r"""tag 列表
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Repository = params.get("Repository")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifeCycle(AbstractModel):
    r"""工作空间生命周期自动执行脚本

    """

    def __init__(self):
        r"""
        :param _Init: 工作空间首次初始化时执行
        :type Init: list of LifeCycleCommand
        :param _Start: 每次工作空间启动时执行
        :type Start: list of LifeCycleCommand
        :param _Destroy: 每次工作空间关闭时执行
        :type Destroy: list of LifeCycleCommand
        """
        self._Init = None
        self._Start = None
        self._Destroy = None

    @property
    def Init(self):
        r"""工作空间首次初始化时执行
        :rtype: list of LifeCycleCommand
        """
        return self._Init

    @Init.setter
    def Init(self, Init):
        self._Init = Init

    @property
    def Start(self):
        r"""每次工作空间启动时执行
        :rtype: list of LifeCycleCommand
        """
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def Destroy(self):
        r"""每次工作空间关闭时执行
        :rtype: list of LifeCycleCommand
        """
        return self._Destroy

    @Destroy.setter
    def Destroy(self, Destroy):
        self._Destroy = Destroy


    def _deserialize(self, params):
        if params.get("Init") is not None:
            self._Init = []
            for item in params.get("Init"):
                obj = LifeCycleCommand()
                obj._deserialize(item)
                self._Init.append(obj)
        if params.get("Start") is not None:
            self._Start = []
            for item in params.get("Start"):
                obj = LifeCycleCommand()
                obj._deserialize(item)
                self._Start.append(obj)
        if params.get("Destroy") is not None:
            self._Destroy = []
            for item in params.get("Destroy"):
                obj = LifeCycleCommand()
                obj._deserialize(item)
                self._Destroy.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifeCycleCommand(AbstractModel):
    r"""工作空间生命周期执行指令

    """

    def __init__(self):
        r"""
        :param _Name: 指令描述
        :type Name: str
        :param _Command: 具体命令
        :type Command: str
        """
        self._Name = None
        self._Command = None

    @property
    def Name(self):
        r"""指令描述
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Command(self):
        r"""具体命令
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkspaceRequest(AbstractModel):
    r"""ModifyWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceKey: 工作空间 SpaceKey. 更新该工作空间的属性
        :type SpaceKey: str
        :param _Name: 工作空间名称
        :type Name: str
        :param _Description: 工作空间描述
        :type Description: str
        :param _Specs: 工作空间规格。STANDARD: 2C4G, CALCULATION: 4C8G, PROFESSION: 8C16G. 默认是 STANDARD。
        :type Specs: str
        :param _Envs: 环境变量. 会被注入到工作空间中
        :type Envs: list of Env
        :param _Extensions: 预装插件. 工作空间启动时, 会自动安装这些插件 
        :type Extensions: list of str
        :param _Lifecycle: 工作空间生命周期钩子.  分为三个阶段 init, start, destroy. 分别表示工作空间数据初始化阶段, 工作空间启动阶段, 工作空间关闭阶段.  用户可以自定义 shell 命令. 
        :type Lifecycle: :class:`tencentcloud.cloudstudio.v20230508.models.LifeCycle`
        """
        self._SpaceKey = None
        self._Name = None
        self._Description = None
        self._Specs = None
        self._Envs = None
        self._Extensions = None
        self._Lifecycle = None

    @property
    def SpaceKey(self):
        r"""工作空间 SpaceKey. 更新该工作空间的属性
        :rtype: str
        """
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey

    @property
    def Name(self):
        r"""工作空间名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""工作空间描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Specs(self):
        r"""工作空间规格。STANDARD: 2C4G, CALCULATION: 4C8G, PROFESSION: 8C16G. 默认是 STANDARD。
        :rtype: str
        """
        return self._Specs

    @Specs.setter
    def Specs(self, Specs):
        self._Specs = Specs

    @property
    def Envs(self):
        r"""环境变量. 会被注入到工作空间中
        :rtype: list of Env
        """
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def Extensions(self):
        r"""预装插件. 工作空间启动时, 会自动安装这些插件 
        :rtype: list of str
        """
        return self._Extensions

    @Extensions.setter
    def Extensions(self, Extensions):
        self._Extensions = Extensions

    @property
    def Lifecycle(self):
        r"""工作空间生命周期钩子.  分为三个阶段 init, start, destroy. 分别表示工作空间数据初始化阶段, 工作空间启动阶段, 工作空间关闭阶段.  用户可以自定义 shell 命令. 
        :rtype: :class:`tencentcloud.cloudstudio.v20230508.models.LifeCycle`
        """
        return self._Lifecycle

    @Lifecycle.setter
    def Lifecycle(self, Lifecycle):
        self._Lifecycle = Lifecycle


    def _deserialize(self, params):
        self._SpaceKey = params.get("SpaceKey")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Specs = params.get("Specs")
        if params.get("Envs") is not None:
            self._Envs = []
            for item in params.get("Envs"):
                obj = Env()
                obj._deserialize(item)
                self._Envs.append(obj)
        self._Extensions = params.get("Extensions")
        if params.get("Lifecycle") is not None:
            self._Lifecycle = LifeCycle()
            self._Lifecycle._deserialize(params.get("Lifecycle"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkspaceResponse(AbstractModel):
    r"""ModifyWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RemoveWorkspaceRequest(AbstractModel):
    r"""RemoveWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceKey: 工作空间 SpaceKey
        :type SpaceKey: str
        """
        self._SpaceKey = None

    @property
    def SpaceKey(self):
        r"""工作空间 SpaceKey
        :rtype: str
        """
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey


    def _deserialize(self, params):
        self._SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveWorkspaceResponse(AbstractModel):
    r"""RemoveWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RunWorkspaceRequest(AbstractModel):
    r"""RunWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceKey: 工作空间 SpaceKey
        :type SpaceKey: str
        """
        self._SpaceKey = None

    @property
    def SpaceKey(self):
        r"""工作空间 SpaceKey
        :rtype: str
        """
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey


    def _deserialize(self, params):
        self._SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunWorkspaceResponse(AbstractModel):
    r"""RunWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopWorkspaceRequest(AbstractModel):
    r"""StopWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceKey: 工作空间 SpaceKey
        :type SpaceKey: str
        """
        self._SpaceKey = None

    @property
    def SpaceKey(self):
        r"""工作空间 SpaceKey
        :rtype: str
        """
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey


    def _deserialize(self, params):
        self._SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopWorkspaceResponse(AbstractModel):
    r"""StopWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class WorkspaceStatusInfo(AbstractModel):
    r"""获取用户工作空间返回信息

    """

    def __init__(self):
        r"""
        :param _Id: 工作空间 ID
        :type Id: int
        :param _Name: 工作空间名称
        :type Name: str
        :param _SpaceKey: 工作空间标识
        :type SpaceKey: str
        :param _Status: 工作空间状态
        :type Status: str
        :param _Cpu: CPU数量
        :type Cpu: int
        :param _Memory: 内存
        :type Memory: int
        :param _Icon: 工作空间图标
        :type Icon: str
        :param _StatusReason: 工作空间状态, 异常原因
        :type StatusReason: str
        :param _Description: 工作空间描述
        :type Description: str
        :param _WorkspaceType: 工作空间类型
        :type WorkspaceType: str
        :param _VersionControlUrl: Git 仓库 HTTPS 地址
        :type VersionControlUrl: str
        :param _VersionControlRef: Git 仓库引用。指定分支使用 /refs/heads/{分支名}, 指定 Tag 用 /refs/tags/{Tag名}
        :type VersionControlRef: str
        :param _LastOpsDate: 最后操作时间
        :type LastOpsDate: str
        :param _CreateDate: 创建时间
        :type CreateDate: str
        """
        self._Id = None
        self._Name = None
        self._SpaceKey = None
        self._Status = None
        self._Cpu = None
        self._Memory = None
        self._Icon = None
        self._StatusReason = None
        self._Description = None
        self._WorkspaceType = None
        self._VersionControlUrl = None
        self._VersionControlRef = None
        self._LastOpsDate = None
        self._CreateDate = None

    @property
    def Id(self):
        r"""工作空间 ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""工作空间名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SpaceKey(self):
        r"""工作空间标识
        :rtype: str
        """
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey

    @property
    def Status(self):
        r"""工作空间状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Cpu(self):
        r"""CPU数量
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""内存
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Icon(self):
        r"""工作空间图标
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def StatusReason(self):
        r"""工作空间状态, 异常原因
        :rtype: str
        """
        return self._StatusReason

    @StatusReason.setter
    def StatusReason(self, StatusReason):
        self._StatusReason = StatusReason

    @property
    def Description(self):
        r"""工作空间描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WorkspaceType(self):
        r"""工作空间类型
        :rtype: str
        """
        return self._WorkspaceType

    @WorkspaceType.setter
    def WorkspaceType(self, WorkspaceType):
        self._WorkspaceType = WorkspaceType

    @property
    def VersionControlUrl(self):
        r"""Git 仓库 HTTPS 地址
        :rtype: str
        """
        return self._VersionControlUrl

    @VersionControlUrl.setter
    def VersionControlUrl(self, VersionControlUrl):
        self._VersionControlUrl = VersionControlUrl

    @property
    def VersionControlRef(self):
        r"""Git 仓库引用。指定分支使用 /refs/heads/{分支名}, 指定 Tag 用 /refs/tags/{Tag名}
        :rtype: str
        """
        return self._VersionControlRef

    @VersionControlRef.setter
    def VersionControlRef(self, VersionControlRef):
        self._VersionControlRef = VersionControlRef

    @property
    def LastOpsDate(self):
        r"""最后操作时间
        :rtype: str
        """
        return self._LastOpsDate

    @LastOpsDate.setter
    def LastOpsDate(self, LastOpsDate):
        self._LastOpsDate = LastOpsDate

    @property
    def CreateDate(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._SpaceKey = params.get("SpaceKey")
        self._Status = params.get("Status")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Icon = params.get("Icon")
        self._StatusReason = params.get("StatusReason")
        self._Description = params.get("Description")
        self._WorkspaceType = params.get("WorkspaceType")
        self._VersionControlUrl = params.get("VersionControlUrl")
        self._VersionControlRef = params.get("VersionControlRef")
        self._LastOpsDate = params.get("LastOpsDate")
        self._CreateDate = params.get("CreateDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        