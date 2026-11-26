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


class BlockProjectRequest(AbstractModel):
    r"""BlockProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _Status: <p>操作类型，目前支持 Ban表示封禁项目， Normal表示解封项目。</p><p>枚举值：</p><ul><li>Ban： 表示封禁项目</li><li>Normal： 表示解封项目</li></ul>
        :type Status: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._Status = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        r"""<p>操作类型，目前支持 Ban表示封禁项目， Normal表示解封项目。</p><p>枚举值：</p><ul><li>Ban： 表示封禁项目</li><li>Normal： 表示解封项目</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlockProjectResponse(AbstractModel):
    r"""BlockProject返回参数结构体

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


class CosCredentials(AbstractModel):
    r"""COS 临时密钥

    """

    def __init__(self):
        r"""
        :param _TmpSecretId: <p>临时 SecretId</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretId: str
        :param _TmpSecretKey: <p>临时 SecretKey</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretKey: str
        :param _Token: <p>临时 Token</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        """
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._Token = None

    @property
    def TmpSecretId(self):
        r"""<p>临时 SecretId</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        r"""<p>临时 SecretKey</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def Token(self):
        r"""<p>临时 Token</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeploymentRequest(AbstractModel):
    r"""CreateDeployment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _ViaMeta: <p>触发来源。Github、ReDeploy、Api、Webhook、Upload、Coding、Gitee、Gitlab</p>
        :type ViaMeta: str
        :param _Env: <p>环境 slug。Production、Preview 或自定义环境</p>
        :type Env: str
        :param _Provider: <p>代码来源。上传制品传 Upload</p>
        :type Provider: str
        :param _DistType: <p>制品类型。Zip 或 Folder</p>
        :type DistType: str
        :param _TempBucketPath: <p>已上传制品在临时桶中的对象路径</p>
        :type TempBucketPath: str
        :param _RepoBranch: <p>构建分支</p>
        :type RepoBranch: str
        :param _RepoCommitHash: <p>提交哈希</p>
        :type RepoCommitHash: str
        :param _RepoCommitMsg: <p>提交说明</p>
        :type RepoCommitMsg: str
        :param _BuildFrom: <p>构建来源</p>
        :type BuildFrom: str
        :param _TemplateId: <p>模板 ID</p>
        :type TemplateId: str
        :param _CiSpec: <p>构建规格。当前服务端仍从 edgeone.json 读取，此字段先保留</p>
        :type CiSpec: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._ViaMeta = None
        self._Env = None
        self._Provider = None
        self._DistType = None
        self._TempBucketPath = None
        self._RepoBranch = None
        self._RepoCommitHash = None
        self._RepoCommitMsg = None
        self._BuildFrom = None
        self._TemplateId = None
        self._CiSpec = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ViaMeta(self):
        r"""<p>触发来源。Github、ReDeploy、Api、Webhook、Upload、Coding、Gitee、Gitlab</p>
        :rtype: str
        """
        return self._ViaMeta

    @ViaMeta.setter
    def ViaMeta(self, ViaMeta):
        self._ViaMeta = ViaMeta

    @property
    def Env(self):
        r"""<p>环境 slug。Production、Preview 或自定义环境</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Provider(self):
        r"""<p>代码来源。上传制品传 Upload</p>
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def DistType(self):
        r"""<p>制品类型。Zip 或 Folder</p>
        :rtype: str
        """
        return self._DistType

    @DistType.setter
    def DistType(self, DistType):
        self._DistType = DistType

    @property
    def TempBucketPath(self):
        r"""<p>已上传制品在临时桶中的对象路径</p>
        :rtype: str
        """
        return self._TempBucketPath

    @TempBucketPath.setter
    def TempBucketPath(self, TempBucketPath):
        self._TempBucketPath = TempBucketPath

    @property
    def RepoBranch(self):
        r"""<p>构建分支</p>
        :rtype: str
        """
        return self._RepoBranch

    @RepoBranch.setter
    def RepoBranch(self, RepoBranch):
        self._RepoBranch = RepoBranch

    @property
    def RepoCommitHash(self):
        r"""<p>提交哈希</p>
        :rtype: str
        """
        return self._RepoCommitHash

    @RepoCommitHash.setter
    def RepoCommitHash(self, RepoCommitHash):
        self._RepoCommitHash = RepoCommitHash

    @property
    def RepoCommitMsg(self):
        r"""<p>提交说明</p>
        :rtype: str
        """
        return self._RepoCommitMsg

    @RepoCommitMsg.setter
    def RepoCommitMsg(self, RepoCommitMsg):
        self._RepoCommitMsg = RepoCommitMsg

    @property
    def BuildFrom(self):
        r"""<p>构建来源</p>
        :rtype: str
        """
        return self._BuildFrom

    @BuildFrom.setter
    def BuildFrom(self, BuildFrom):
        self._BuildFrom = BuildFrom

    @property
    def TemplateId(self):
        r"""<p>模板 ID</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def CiSpec(self):
        r"""<p>构建规格。当前服务端仍从 edgeone.json 读取，此字段先保留</p>
        :rtype: str
        """
        return self._CiSpec

    @CiSpec.setter
    def CiSpec(self, CiSpec):
        self._CiSpec = CiSpec


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._ViaMeta = params.get("ViaMeta")
        self._Env = params.get("Env")
        self._Provider = params.get("Provider")
        self._DistType = params.get("DistType")
        self._TempBucketPath = params.get("TempBucketPath")
        self._RepoBranch = params.get("RepoBranch")
        self._RepoCommitHash = params.get("RepoCommitHash")
        self._RepoCommitMsg = params.get("RepoCommitMsg")
        self._BuildFrom = params.get("BuildFrom")
        self._TemplateId = params.get("TemplateId")
        self._CiSpec = params.get("CiSpec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeploymentResponse(AbstractModel):
    r"""CreateDeployment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeploymentId: <p>部署 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploymentId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeploymentId = None
        self._RequestId = None

    @property
    def DeploymentId(self):
        r"""<p>部署 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId

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
        self._DeploymentId = params.get("DeploymentId")
        self._RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    r"""CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _Name: <p>项目名称</p>
        :type Name: str
        :param _Channel: <p>创建来源。Template、Custom、CLI、Guest</p>
        :type Channel: str
        :param _Provider: <p>代码来源。Upload、Github、Gitee、Gitlab、Coding</p>
        :type Provider: str
        :param _Source: <p>接入方标识</p>
        :type Source: str
        :param _Area: <p>加速区域。mainland、overseas、global</p>
        :type Area: str
        :param _NodeJsVersion: <p>Node.js 版本。14.21.3、16.20.2、18.20.4、20.18.0、22.11.0、22.17.1、22.21.1、24.5.0、24.11.0、24.18.0</p>
        :type NodeJsVersion: str
        :param _RootDir: <p>项目根目录</p>
        :type RootDir: str
        :param _OutputDir: <p>构建产物目录</p>
        :type OutputDir: str
        :param _BuildCmd: <p>构建命令</p>
        :type BuildCmd: str
        :param _InstallCmd: <p>安装命令</p>
        :type InstallCmd: str
        :param _Framework: <p>框架</p>
        :type Framework: str
        :param _TemplateId: <p>模板 ID</p>
        :type TemplateId: str
        :param _RepoUrl: <p>仓库地址</p>
        :type RepoUrl: str
        :param _RepoOwner: <p>仓库所有者</p>
        :type RepoOwner: str
        :param _RepoName: <p>仓库名称</p>
        :type RepoName: str
        :param _RepoBranch: <p>生产分支</p>
        :type RepoBranch: str
        :param _EnvVars: <p>初始环境变量</p>
        :type EnvVars: list of EnvVar
        :param _Namespace: <p>Coding 命名空间。Provider 为 Coding 时使用</p>
        :type Namespace: str
        :param _CodingProjectId: <p>Coding 项目 ID。Provider 为 Coding 时使用</p>
        :type CodingProjectId: int
        """
        self._ZoneId = None
        self._Name = None
        self._Channel = None
        self._Provider = None
        self._Source = None
        self._Area = None
        self._NodeJsVersion = None
        self._RootDir = None
        self._OutputDir = None
        self._BuildCmd = None
        self._InstallCmd = None
        self._Framework = None
        self._TemplateId = None
        self._RepoUrl = None
        self._RepoOwner = None
        self._RepoName = None
        self._RepoBranch = None
        self._EnvVars = None
        self._Namespace = None
        self._CodingProjectId = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Name(self):
        r"""<p>项目名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Channel(self):
        r"""<p>创建来源。Template、Custom、CLI、Guest</p>
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def Provider(self):
        r"""<p>代码来源。Upload、Github、Gitee、Gitlab、Coding</p>
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def Source(self):
        r"""<p>接入方标识</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Area(self):
        r"""<p>加速区域。mainland、overseas、global</p>
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def NodeJsVersion(self):
        r"""<p>Node.js 版本。14.21.3、16.20.2、18.20.4、20.18.0、22.11.0、22.17.1、22.21.1、24.5.0、24.11.0、24.18.0</p>
        :rtype: str
        """
        return self._NodeJsVersion

    @NodeJsVersion.setter
    def NodeJsVersion(self, NodeJsVersion):
        self._NodeJsVersion = NodeJsVersion

    @property
    def RootDir(self):
        r"""<p>项目根目录</p>
        :rtype: str
        """
        return self._RootDir

    @RootDir.setter
    def RootDir(self, RootDir):
        self._RootDir = RootDir

    @property
    def OutputDir(self):
        r"""<p>构建产物目录</p>
        :rtype: str
        """
        return self._OutputDir

    @OutputDir.setter
    def OutputDir(self, OutputDir):
        self._OutputDir = OutputDir

    @property
    def BuildCmd(self):
        r"""<p>构建命令</p>
        :rtype: str
        """
        return self._BuildCmd

    @BuildCmd.setter
    def BuildCmd(self, BuildCmd):
        self._BuildCmd = BuildCmd

    @property
    def InstallCmd(self):
        r"""<p>安装命令</p>
        :rtype: str
        """
        return self._InstallCmd

    @InstallCmd.setter
    def InstallCmd(self, InstallCmd):
        self._InstallCmd = InstallCmd

    @property
    def Framework(self):
        r"""<p>框架</p>
        :rtype: str
        """
        return self._Framework

    @Framework.setter
    def Framework(self, Framework):
        self._Framework = Framework

    @property
    def TemplateId(self):
        r"""<p>模板 ID</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RepoUrl(self):
        r"""<p>仓库地址</p>
        :rtype: str
        """
        return self._RepoUrl

    @RepoUrl.setter
    def RepoUrl(self, RepoUrl):
        self._RepoUrl = RepoUrl

    @property
    def RepoOwner(self):
        r"""<p>仓库所有者</p>
        :rtype: str
        """
        return self._RepoOwner

    @RepoOwner.setter
    def RepoOwner(self, RepoOwner):
        self._RepoOwner = RepoOwner

    @property
    def RepoName(self):
        r"""<p>仓库名称</p>
        :rtype: str
        """
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def RepoBranch(self):
        r"""<p>生产分支</p>
        :rtype: str
        """
        return self._RepoBranch

    @RepoBranch.setter
    def RepoBranch(self, RepoBranch):
        self._RepoBranch = RepoBranch

    @property
    def EnvVars(self):
        r"""<p>初始环境变量</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars

    @property
    def Namespace(self):
        r"""<p>Coding 命名空间。Provider 为 Coding 时使用</p>
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def CodingProjectId(self):
        r"""<p>Coding 项目 ID。Provider 为 Coding 时使用</p>
        :rtype: int
        """
        return self._CodingProjectId

    @CodingProjectId.setter
    def CodingProjectId(self, CodingProjectId):
        self._CodingProjectId = CodingProjectId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Name = params.get("Name")
        self._Channel = params.get("Channel")
        self._Provider = params.get("Provider")
        self._Source = params.get("Source")
        self._Area = params.get("Area")
        self._NodeJsVersion = params.get("NodeJsVersion")
        self._RootDir = params.get("RootDir")
        self._OutputDir = params.get("OutputDir")
        self._BuildCmd = params.get("BuildCmd")
        self._InstallCmd = params.get("InstallCmd")
        self._Framework = params.get("Framework")
        self._TemplateId = params.get("TemplateId")
        self._RepoUrl = params.get("RepoUrl")
        self._RepoOwner = params.get("RepoOwner")
        self._RepoName = params.get("RepoName")
        self._RepoBranch = params.get("RepoBranch")
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        self._Namespace = params.get("Namespace")
        self._CodingProjectId = params.get("CodingProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    r"""CreateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: <p>项目 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectId = None
        self._RequestId = None

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
        self._ProjectId = params.get("ProjectId")
        self._RequestId = params.get("RequestId")


class CreateZoneCustomDomainRequest(AbstractModel):
    r"""CreateZoneCustomDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _Domain: <p>自定义域名</p>
        :type Domain: str
        :param _Env: <p>环境 slug。不传时由后端决定</p>
        :type Env: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._Domain = None
        self._Env = None

    @property
    def ZoneId(self):
        r"""<p>站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Domain(self):
        r"""<p>自定义域名</p>
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Env(self):
        r"""<p>环境 slug。不传时由后端决定</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._Domain = params.get("Domain")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateZoneCustomDomainResponse(AbstractModel):
    r"""CreateZoneCustomDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: <p>域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Id: <p>域名配置 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domain = None
        self._Id = None
        self._RequestId = None

    @property
    def Domain(self):
        r"""<p>域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Id(self):
        r"""<p>域名配置 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Domain = params.get("Domain")
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CustomDomainInput(AbstractModel):
    r"""绑定自定义域名时的域名项

    """

    def __init__(self):
        r"""
        :param _Domain: <p>域名</p>
        :type Domain: str
        :param _CertificateId: <p>证书 ID</p>
        :type CertificateId: str
        :param _Status: <p>校验状态。Verify、Pass、Fail</p>
        :type Status: str
        :param _NoCertificate: <p>是否不申请证书</p>
        :type NoCertificate: bool
        """
        self._Domain = None
        self._CertificateId = None
        self._Status = None
        self._NoCertificate = None

    @property
    def Domain(self):
        r"""<p>域名</p>
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertificateId(self):
        r"""<p>证书 ID</p>
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Status(self):
        r"""<p>校验状态。Verify、Pass、Fail</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NoCertificate(self):
        r"""<p>是否不申请证书</p>
        :rtype: bool
        """
        return self._NoCertificate

    @NoCertificate.setter
    def NoCertificate(self, NoCertificate):
        self._NoCertificate = NoCertificate


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertificateId = params.get("CertificateId")
        self._Status = params.get("Status")
        self._NoCertificate = params.get("NoCertificate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomDomainItem(AbstractModel):
    r"""自定义域名

    """

    def __init__(self):
        r"""
        :param _Domain: <p>域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        r"""<p>域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectCustomDomainsRequest(AbstractModel):
    r"""DeleteProjectCustomDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _CustomDomains: <p>要解绑的域名</p>
        :type CustomDomains: list of str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._CustomDomains = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CustomDomains(self):
        r"""<p>要解绑的域名</p>
        :rtype: list of str
        """
        return self._CustomDomains

    @CustomDomains.setter
    def CustomDomains(self, CustomDomains):
        self._CustomDomains = CustomDomains


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._CustomDomains = params.get("CustomDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectCustomDomainsResponse(AbstractModel):
    r"""DeleteProjectCustomDomains返回参数结构体

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


class DeleteProjectEnvsRequest(AbstractModel):
    r"""DeleteProjectEnvs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _EnvVars: <p>要删除的环境变量。传 Key（或 Id），Value 必填但不参与匹配</p>
        :type EnvVars: list of EnvVar
        """
        self._ZoneId = None
        self._ProjectId = None
        self._EnvVars = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EnvVars(self):
        r"""<p>要删除的环境变量。传 Key（或 Id），Value 必填但不参与匹配</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectEnvsResponse(AbstractModel):
    r"""DeleteProjectEnvs返回参数结构体

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


class DeleteProjectRequest(AbstractModel):
    r"""DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        """
        self._ZoneId = None
        self._ProjectId = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    r"""DeleteProject返回参数结构体

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


class Deployment(AbstractModel):
    r"""部署记录

    """

    def __init__(self):
        r"""
        :param _DeploymentId: <p>部署 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploymentId: str
        :param _ProjectId: <p>项目 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _Status: <p>Success、Failed、Process、Invalid、Pending、Timeout、Cancelled</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _OriginalStatus: <p>部署被移除前的原始状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalStatus: str
        :param _Code: <p>构建退出码，0 表示成功</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _BuildCost: <p>构建耗时，单位毫秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildCost: str
        :param _ViaMeta: <p>触发来源。Github、ReDeploy、Api、Coding、Gitee、Upload、Gitlab</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ViaMeta: str
        :param _Env: <p>环境 slug</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Env: str
        :param _RepoBranch: <p>分支</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoBranch: str
        :param _RepoCommitHash: <p>提交哈希</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoCommitHash: str
        :param _RepoCommitMsg: <p>提交说明</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoCommitMsg: str
        :param _PreviewUrl: <p>本次部署的访问地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param _ProjectUrl: <p>项目默认域名地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectUrl: str
        :param _UsedInProd: <p>是否为当前生产版本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedInProd: bool
        :param _CoverUrl: <p>封面地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverUrl: str
        :param _MetaData: <p>路由配置，JSON 字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: str
        :param _DplRepoUrl: <p>本次部署使用的仓库地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DplRepoUrl: str
        :param _CreatedOn: <p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: str
        :param _ModifiedOn: <p>更新时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedOn: str
        """
        self._DeploymentId = None
        self._ProjectId = None
        self._Status = None
        self._OriginalStatus = None
        self._Code = None
        self._BuildCost = None
        self._ViaMeta = None
        self._Env = None
        self._RepoBranch = None
        self._RepoCommitHash = None
        self._RepoCommitMsg = None
        self._PreviewUrl = None
        self._ProjectUrl = None
        self._UsedInProd = None
        self._CoverUrl = None
        self._MetaData = None
        self._DplRepoUrl = None
        self._CreatedOn = None
        self._ModifiedOn = None

    @property
    def DeploymentId(self):
        r"""<p>部署 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        r"""<p>Success、Failed、Process、Invalid、Pending、Timeout、Cancelled</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OriginalStatus(self):
        r"""<p>部署被移除前的原始状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OriginalStatus

    @OriginalStatus.setter
    def OriginalStatus(self, OriginalStatus):
        self._OriginalStatus = OriginalStatus

    @property
    def Code(self):
        r"""<p>构建退出码，0 表示成功</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def BuildCost(self):
        r"""<p>构建耗时，单位毫秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BuildCost

    @BuildCost.setter
    def BuildCost(self, BuildCost):
        self._BuildCost = BuildCost

    @property
    def ViaMeta(self):
        r"""<p>触发来源。Github、ReDeploy、Api、Coding、Gitee、Upload、Gitlab</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ViaMeta

    @ViaMeta.setter
    def ViaMeta(self, ViaMeta):
        self._ViaMeta = ViaMeta

    @property
    def Env(self):
        r"""<p>环境 slug</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def RepoBranch(self):
        r"""<p>分支</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RepoBranch

    @RepoBranch.setter
    def RepoBranch(self, RepoBranch):
        self._RepoBranch = RepoBranch

    @property
    def RepoCommitHash(self):
        r"""<p>提交哈希</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RepoCommitHash

    @RepoCommitHash.setter
    def RepoCommitHash(self, RepoCommitHash):
        self._RepoCommitHash = RepoCommitHash

    @property
    def RepoCommitMsg(self):
        r"""<p>提交说明</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RepoCommitMsg

    @RepoCommitMsg.setter
    def RepoCommitMsg(self, RepoCommitMsg):
        self._RepoCommitMsg = RepoCommitMsg

    @property
    def PreviewUrl(self):
        r"""<p>本次部署的访问地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def ProjectUrl(self):
        r"""<p>项目默认域名地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectUrl

    @ProjectUrl.setter
    def ProjectUrl(self, ProjectUrl):
        self._ProjectUrl = ProjectUrl

    @property
    def UsedInProd(self):
        r"""<p>是否为当前生产版本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._UsedInProd

    @UsedInProd.setter
    def UsedInProd(self, UsedInProd):
        self._UsedInProd = UsedInProd

    @property
    def CoverUrl(self):
        r"""<p>封面地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CoverUrl

    @CoverUrl.setter
    def CoverUrl(self, CoverUrl):
        self._CoverUrl = CoverUrl

    @property
    def MetaData(self):
        r"""<p>路由配置，JSON 字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData

    @property
    def DplRepoUrl(self):
        r"""<p>本次部署使用的仓库地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DplRepoUrl

    @DplRepoUrl.setter
    def DplRepoUrl(self, DplRepoUrl):
        self._DplRepoUrl = DplRepoUrl

    @property
    def CreatedOn(self):
        r"""<p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        r"""<p>更新时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn


    def _deserialize(self, params):
        self._DeploymentId = params.get("DeploymentId")
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._OriginalStatus = params.get("OriginalStatus")
        self._Code = params.get("Code")
        self._BuildCost = params.get("BuildCost")
        self._ViaMeta = params.get("ViaMeta")
        self._Env = params.get("Env")
        self._RepoBranch = params.get("RepoBranch")
        self._RepoCommitHash = params.get("RepoCommitHash")
        self._RepoCommitMsg = params.get("RepoCommitMsg")
        self._PreviewUrl = params.get("PreviewUrl")
        self._ProjectUrl = params.get("ProjectUrl")
        self._UsedInProd = params.get("UsedInProd")
        self._CoverUrl = params.get("CoverUrl")
        self._MetaData = params.get("MetaData")
        self._DplRepoUrl = params.get("DplRepoUrl")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeploymentFilter(AbstractModel):
    r"""部署列表过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: <p>过滤字段。ProjectId、DeploymentId、Name、Status、StartTime、EndTime、RepoBranch</p>
        :type Name: str
        :param _Values: <p>过滤值</p>
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""<p>过滤字段。ProjectId、DeploymentId、Name、Status、StartTime、EndTime、RepoBranch</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>过滤值</p>
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCosTempTokenRequest(AbstractModel):
    r"""DescribeCosTempToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectName: <p>项目名称。临时路径按它拼接</p>
        :type ProjectName: str
        :param _ProjectId: <p>项目 ID。不传 ProjectName 时用来反查项目名</p>
        :type ProjectId: str
        """
        self._ZoneId = None
        self._ProjectName = None
        self._ProjectId = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectName(self):
        r"""<p>项目名称。临时路径按它拼接</p>
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectId(self):
        r"""<p>项目 ID。不传 ProjectName 时用来反查项目名</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCosTempTokenResponse(AbstractModel):
    r"""DescribeCosTempToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Bucket: <p>COS 桶</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param _Region: <p>COS 地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _TargetPath: <p>上传路径，格式 appId/projectName/时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetPath: str
        :param _ExpiredTime: <p>临时密钥过期时间，Unix 秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: int
        :param _Expiration: <p>临时密钥过期时间，ISO 8601</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Expiration: str
        :param _Credentials: <p>临时密钥</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Credentials: :class:`tencentcloud.makers.v20261113.models.CosCredentials`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Bucket = None
        self._Region = None
        self._TargetPath = None
        self._ExpiredTime = None
        self._Expiration = None
        self._Credentials = None
        self._RequestId = None

    @property
    def Bucket(self):
        r"""<p>COS 桶</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        r"""<p>COS 地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TargetPath(self):
        r"""<p>上传路径，格式 appId/projectName/时间戳</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath

    @property
    def ExpiredTime(self):
        r"""<p>临时密钥过期时间，Unix 秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Expiration(self):
        r"""<p>临时密钥过期时间，ISO 8601</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Credentials(self):
        r"""<p>临时密钥</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.CosCredentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

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
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._TargetPath = params.get("TargetPath")
        self._ExpiredTime = params.get("ExpiredTime")
        self._Expiration = params.get("Expiration")
        if params.get("Credentials") is not None:
            self._Credentials = CosCredentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._RequestId = params.get("RequestId")


class DescribeDeploymentLogRequest(AbstractModel):
    r"""DescribeDeploymentLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _DeploymentId: <p>部署 ID</p>
        :type DeploymentId: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._DeploymentId = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeploymentId(self):
        r"""<p>部署 ID</p>
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._DeploymentId = params.get("DeploymentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeploymentLogResponse(AbstractModel):
    r"""DescribeDeploymentLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogUrl: <p>构建日志地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LogUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogUrl = None
        self._RequestId = None

    @property
    def LogUrl(self):
        r"""<p>构建日志地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogUrl

    @LogUrl.setter
    def LogUrl(self, LogUrl):
        self._LogUrl = LogUrl

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
        self._LogUrl = params.get("LogUrl")
        self._RequestId = params.get("RequestId")


class DescribeDeploymentsRequest(AbstractModel):
    r"""DescribeDeployments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _DeploymentIds: <p>按部署 ID 查询</p>
        :type DeploymentIds: list of str
        :param _Filters: <p>过滤条件</p>
        :type Filters: list of DeploymentFilter
        :param _Offset: <p>偏移</p>
        :type Offset: int
        :param _Limit: <p>每页数量，最大 100</p>
        :type Limit: int
        :param _OrderBy: <p>CreatedOn 或 ModifiedOn</p>
        :type OrderBy: str
        :param _OrderType: <p>Asc 或 Desc</p>
        :type OrderType: str
        :param _StartTime: <p>开始时间</p>
        :type StartTime: str
        :param _EndTime: <p>结束时间</p>
        :type EndTime: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._DeploymentIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderType = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeploymentIds(self):
        r"""<p>按部署 ID 查询</p>
        :rtype: list of str
        """
        return self._DeploymentIds

    @DeploymentIds.setter
    def DeploymentIds(self, DeploymentIds):
        self._DeploymentIds = DeploymentIds

    @property
    def Filters(self):
        r"""<p>过滤条件</p>
        :rtype: list of DeploymentFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""<p>偏移</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>每页数量，最大 100</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        r"""<p>CreatedOn 或 ModifiedOn</p>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""<p>Asc 或 Desc</p>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def StartTime(self):
        r"""<p>开始时间</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>结束时间</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._DeploymentIds = params.get("DeploymentIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DeploymentFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeploymentsResponse(AbstractModel):
    r"""DescribeDeployments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Deployments: <p>部署列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployments: list of Deployment
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Deployments = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Deployments(self):
        r"""<p>部署列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Deployment
        """
        return self._Deployments

    @Deployments.setter
    def Deployments(self, Deployments):
        self._Deployments = Deployments

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Deployments") is not None:
            self._Deployments = []
            for item in params.get("Deployments"):
                obj = Deployment()
                obj._deserialize(item)
                self._Deployments.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    r"""DescribeEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        """
        self._ZoneId = None
        self._ProjectId = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentsResponse(AbstractModel):
    r"""DescribeEnvironments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Environments: <p>环境列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Environments: list of Environment
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Environments = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Environments(self):
        r"""<p>环境列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Environment
        """
        return self._Environments

    @Environments.setter
    def Environments(self, Environments):
        self._Environments = Environments

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Environments") is not None:
            self._Environments = []
            for item in params.get("Environments"):
                obj = Environment()
                obj._deserialize(item)
                self._Environments.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectEnvsRequest(AbstractModel):
    r"""DescribeProjectEnvs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _Env: <p>只返回该环境 slug 的变量</p>
        :type Env: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._Env = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Env(self):
        r"""<p>只返回该环境 slug 的变量</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectEnvsResponse(AbstractModel):
    r"""DescribeProjectEnvs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvVars: <p>环境变量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvVars: list of EnvVar
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvVars = None
        self._RequestId = None

    @property
    def EnvVars(self):
        r"""<p>环境变量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars

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
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    r"""DescribeProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _Offset: <p>页码偏移，从 0 开始。后端跳过 Offset * Limit 条</p>
        :type Offset: int
        :param _Limit: <p>每页数量，最大 100</p>
        :type Limit: int
        :param _Filters: <p>过滤条件。Name 取值 ProjectId、Name、Status、Provider</p>
        :type Filters: list of ProjectFilter
        :param _ProjectIds: <p>按项目 ID 查询</p>
        :type ProjectIds: list of str
        :param _OrderBy: <p>排序字段。CreatedOn、ModifiedOn。默认 CreatedOn</p>
        :type OrderBy: str
        :param _OrderType: <p>排序方向。Asc、Desc、ASC、DESC。默认 DESC</p>
        :type OrderType: str
        :param _Source: <p>来源。drop 时只返回 Upload 项目</p>
        :type Source: str
        :param _Query: <p>按项目名称模糊搜索</p>
        :type Query: str
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._ProjectIds = None
        self._OrderBy = None
        self._OrderType = None
        self._Source = None
        self._Query = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        r"""<p>页码偏移，从 0 开始。后端跳过 Offset * Limit 条</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>每页数量，最大 100</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>过滤条件。Name 取值 ProjectId、Name、Status、Provider</p>
        :rtype: list of ProjectFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ProjectIds(self):
        r"""<p>按项目 ID 查询</p>
        :rtype: list of str
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def OrderBy(self):
        r"""<p>排序字段。CreatedOn、ModifiedOn。默认 CreatedOn</p>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""<p>排序方向。Asc、Desc、ASC、DESC。默认 DESC</p>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def Source(self):
        r"""<p>来源。drop 时只返回 Upload 项目</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Query(self):
        r"""<p>按项目名称模糊搜索</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ProjectFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ProjectIds = params.get("ProjectIds")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._Source = params.get("Source")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    r"""DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Projects: <p>项目列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Projects: list of Project
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Projects = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Projects(self):
        r"""<p>项目列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Project
        """
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Projects") is not None:
            self._Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self._Projects.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneCustomDomainsRequest(AbstractModel):
    r"""DescribeZoneCustomDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _CustomDomains: <p>只查询这些域名。不传则返回项目下的域名</p>
        :type CustomDomains: list of CustomDomainInput
        """
        self._ZoneId = None
        self._ProjectId = None
        self._CustomDomains = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CustomDomains(self):
        r"""<p>只查询这些域名。不传则返回项目下的域名</p>
        :rtype: list of CustomDomainInput
        """
        return self._CustomDomains

    @CustomDomains.setter
    def CustomDomains(self, CustomDomains):
        self._CustomDomains = CustomDomains


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        if params.get("CustomDomains") is not None:
            self._CustomDomains = []
            for item in params.get("CustomDomains"):
                obj = CustomDomainInput()
                obj._deserialize(item)
                self._CustomDomains.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneCustomDomainsResponse(AbstractModel):
    r"""DescribeZoneCustomDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _PagesDomains: <p>域名列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PagesDomains: list of ZoneDomain
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PagesDomains = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PagesDomains(self):
        r"""<p>域名列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ZoneDomain
        """
        return self._PagesDomains

    @PagesDomains.setter
    def PagesDomains(self, PagesDomains):
        self._PagesDomains = PagesDomains

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
        self._TotalCount = params.get("TotalCount")
        if params.get("PagesDomains") is not None:
            self._PagesDomains = []
            for item in params.get("PagesDomains"):
                obj = ZoneDomain()
                obj._deserialize(item)
                self._PagesDomains.append(obj)
        self._RequestId = params.get("RequestId")


class DnsVerification(AbstractModel):
    r"""DNS 归属校验记录

    """

    def __init__(self):
        r"""
        :param _RecordType: <p>记录类型，TXT</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordType: str
        :param _Subdomain: <p>主机记录</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Subdomain: str
        :param _RecordValue: <p>记录值</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordValue: str
        """
        self._RecordType = None
        self._Subdomain = None
        self._RecordValue = None

    @property
    def RecordType(self):
        r"""<p>记录类型，TXT</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def Subdomain(self):
        r"""<p>主机记录</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def RecordValue(self):
        r"""<p>记录值</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue


    def _deserialize(self, params):
        self._RecordType = params.get("RecordType")
        self._Subdomain = params.get("Subdomain")
        self._RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvVar(AbstractModel):
    r"""环境变量。Env 缺省或空数组表示全局，写入时展开为项目当前全部环境

    """

    def __init__(self):
        r"""
        :param _Key: <p>变量名，最长 255</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: <p>变量值，最长 1000</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Id: <p>变量 ID。创建时不传</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Comment: <p>备注，最长 255</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _Env: <p>生效环境 slug，例如 Production、Preview。同 Key 的多行环境不能重叠</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Env: list of str
        """
        self._Key = None
        self._Value = None
        self._Id = None
        self._Comment = None
        self._Env = None

    @property
    def Key(self):
        r"""<p>变量名，最长 255</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>变量值，最长 1000</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Id(self):
        r"""<p>变量 ID。创建时不传</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Comment(self):
        r"""<p>备注，最长 255</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Env(self):
        r"""<p>生效环境 slug，例如 Production、Preview。同 Key 的多行环境不能重叠</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Id = params.get("Id")
        self._Comment = params.get("Comment")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Environment(AbstractModel):
    r"""环境

    """

    def __init__(self):
        r"""
        :param _Slug: <p>环境标识，创建后不可改</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Slug: str
        :param _Name: <p>环境名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Type: <p>Production、Preview、Custom</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Branches: <p>关联分支，支持通配</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Branches: list of str
        :param _AutoDeploy: <p>是否自动部署。Production 恒为 true</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoDeploy: bool
        :param _CustomDomains: <p>绑定的自定义域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomDomains: list of str
        :param _EnvVars: <p>环境变量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvVars: list of EnvironmentEnvVar
        :param _CreatedOn: <p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: str
        :param _ModifiedOn: <p>更新时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedOn: str
        """
        self._Slug = None
        self._Name = None
        self._Type = None
        self._Branches = None
        self._AutoDeploy = None
        self._CustomDomains = None
        self._EnvVars = None
        self._CreatedOn = None
        self._ModifiedOn = None

    @property
    def Slug(self):
        r"""<p>环境标识，创建后不可改</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Slug

    @Slug.setter
    def Slug(self, Slug):
        self._Slug = Slug

    @property
    def Name(self):
        r"""<p>环境名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""<p>Production、Preview、Custom</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Branches(self):
        r"""<p>关联分支，支持通配</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Branches

    @Branches.setter
    def Branches(self, Branches):
        self._Branches = Branches

    @property
    def AutoDeploy(self):
        r"""<p>是否自动部署。Production 恒为 true</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AutoDeploy

    @AutoDeploy.setter
    def AutoDeploy(self, AutoDeploy):
        self._AutoDeploy = AutoDeploy

    @property
    def CustomDomains(self):
        r"""<p>绑定的自定义域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CustomDomains

    @CustomDomains.setter
    def CustomDomains(self, CustomDomains):
        self._CustomDomains = CustomDomains

    @property
    def EnvVars(self):
        r"""<p>环境变量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EnvironmentEnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars

    @property
    def CreatedOn(self):
        r"""<p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        r"""<p>更新时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn


    def _deserialize(self, params):
        self._Slug = params.get("Slug")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Branches = params.get("Branches")
        self._AutoDeploy = params.get("AutoDeploy")
        self._CustomDomains = params.get("CustomDomains")
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvironmentEnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentEnvVar(AbstractModel):
    r"""环境上的变量

    """

    def __init__(self):
        r"""
        :param _Id: <p>变量 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Key: <p>变量名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: <p>变量值</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Comment: <p>备注</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _Env: <p>生效环境 slug</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Env: list of str
        """
        self._Id = None
        self._Key = None
        self._Value = None
        self._Comment = None
        self._Env = None

    @property
    def Id(self):
        r"""<p>变量 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Key(self):
        r"""<p>变量名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>变量值</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Comment(self):
        r"""<p>备注</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Env(self):
        r"""<p>生效环境 slug</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Comment = params.get("Comment")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileVerification(AbstractModel):
    r"""文件归属校验信息

    """

    def __init__(self):
        r"""
        :param _Path: <p>校验文件路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Content: <p>校验文件内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self._Path = None
        self._Content = None

    @property
    def Path(self):
        r"""<p>校验文件路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Content(self):
        r"""<p>校验文件内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirectConfig(AbstractModel):
    r"""强制 HTTPS 跳转

    """

    def __init__(self):
        r"""
        :param _Switch: <p>on 或 off</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _RedirectStatusCode: <p>301、302、307、308</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectStatusCode: int
        """
        self._Switch = None
        self._RedirectStatusCode = None

    @property
    def Switch(self):
        r"""<p>on 或 off</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RedirectStatusCode(self):
        r"""<p>301、302、307、308</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RedirectStatusCode

    @RedirectStatusCode.setter
    def RedirectStatusCode(self, RedirectStatusCode):
        self._RedirectStatusCode = RedirectStatusCode


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RedirectStatusCode = params.get("RedirectStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HstsConfig(AbstractModel):
    r"""HSTS 配置

    """

    def __init__(self):
        r"""
        :param _Switch: <p>on 或 off</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _MaxAge: <p>有效期，秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: int
        :param _IncludeSubDomains: <p>on 或 off</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeSubDomains: str
        :param _Preload: <p>on 或 off</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Preload: str
        """
        self._Switch = None
        self._MaxAge = None
        self._IncludeSubDomains = None
        self._Preload = None

    @property
    def Switch(self):
        r"""<p>on 或 off</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxAge(self):
        r"""<p>有效期，秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def IncludeSubDomains(self):
        r"""<p>on 或 off</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IncludeSubDomains

    @IncludeSubDomains.setter
    def IncludeSubDomains(self, IncludeSubDomains):
        self._IncludeSubDomains = IncludeSubDomains

    @property
    def Preload(self):
        r"""<p>on 或 off</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Preload

    @Preload.setter
    def Preload(self, Preload):
        self._Preload = Preload


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxAge = params.get("MaxAge")
        self._IncludeSubDomains = params.get("IncludeSubDomains")
        self._Preload = params.get("Preload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectEnvsRequest(AbstractModel):
    r"""ModifyProjectEnvs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _EnvVars: <p>要写入的环境变量</p>
        :type EnvVars: list of EnvVar
        """
        self._ZoneId = None
        self._ProjectId = None
        self._EnvVars = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EnvVars(self):
        r"""<p>要写入的环境变量</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectEnvsResponse(AbstractModel):
    r"""ModifyProjectEnvs返回参数结构体

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


class ModifyProjectRequest(AbstractModel):
    r"""ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers 站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _Name: <p>项目名称</p>
        :type Name: str
        :param _RootDir: <p>项目根目录</p>
        :type RootDir: str
        :param _OutputDir: <p>构建产物目录</p>
        :type OutputDir: str
        :param _BuildCmd: <p>构建命令</p>
        :type BuildCmd: str
        :param _InstallCmd: <p>安装命令</p>
        :type InstallCmd: str
        :param _Framework: <p>框架</p>
        :type Framework: str
        :param _CoverUrl: <p>封面地址</p>
        :type CoverUrl: str
        :param _NodeJsVersion: <p>Node.js 版本</p>
        :type NodeJsVersion: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._Name = None
        self._RootDir = None
        self._OutputDir = None
        self._BuildCmd = None
        self._InstallCmd = None
        self._Framework = None
        self._CoverUrl = None
        self._NodeJsVersion = None

    @property
    def ZoneId(self):
        r"""<p>Makers 站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        r"""<p>项目名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RootDir(self):
        r"""<p>项目根目录</p>
        :rtype: str
        """
        return self._RootDir

    @RootDir.setter
    def RootDir(self, RootDir):
        self._RootDir = RootDir

    @property
    def OutputDir(self):
        r"""<p>构建产物目录</p>
        :rtype: str
        """
        return self._OutputDir

    @OutputDir.setter
    def OutputDir(self, OutputDir):
        self._OutputDir = OutputDir

    @property
    def BuildCmd(self):
        r"""<p>构建命令</p>
        :rtype: str
        """
        return self._BuildCmd

    @BuildCmd.setter
    def BuildCmd(self, BuildCmd):
        self._BuildCmd = BuildCmd

    @property
    def InstallCmd(self):
        r"""<p>安装命令</p>
        :rtype: str
        """
        return self._InstallCmd

    @InstallCmd.setter
    def InstallCmd(self, InstallCmd):
        self._InstallCmd = InstallCmd

    @property
    def Framework(self):
        r"""<p>框架</p>
        :rtype: str
        """
        return self._Framework

    @Framework.setter
    def Framework(self, Framework):
        self._Framework = Framework

    @property
    def CoverUrl(self):
        r"""<p>封面地址</p>
        :rtype: str
        """
        return self._CoverUrl

    @CoverUrl.setter
    def CoverUrl(self, CoverUrl):
        self._CoverUrl = CoverUrl

    @property
    def NodeJsVersion(self):
        r"""<p>Node.js 版本</p>
        :rtype: str
        """
        return self._NodeJsVersion

    @NodeJsVersion.setter
    def NodeJsVersion(self, NodeJsVersion):
        self._NodeJsVersion = NodeJsVersion


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._RootDir = params.get("RootDir")
        self._OutputDir = params.get("OutputDir")
        self._BuildCmd = params.get("BuildCmd")
        self._InstallCmd = params.get("InstallCmd")
        self._Framework = params.get("Framework")
        self._CoverUrl = params.get("CoverUrl")
        self._NodeJsVersion = params.get("NodeJsVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    r"""ModifyProject返回参数结构体

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


class ModifyZoneCustomDomainEnvRequest(AbstractModel):
    r"""ModifyZoneCustomDomainEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>站点 ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>项目 ID</p>
        :type ProjectId: str
        :param _Domain: <p>域名</p>
        :type Domain: str
        :param _Env: <p>目标环境 slug</p>
        :type Env: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._Domain = None
        self._Env = None

    @property
    def ZoneId(self):
        r"""<p>站点 ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Domain(self):
        r"""<p>域名</p>
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Env(self):
        r"""<p>目标环境 slug</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._Domain = params.get("Domain")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneCustomDomainEnvResponse(AbstractModel):
    r"""ModifyZoneCustomDomainEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: <p>域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Env: <p>切换后的环境 slug</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Env: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domain = None
        self._Env = None
        self._RequestId = None

    @property
    def Domain(self):
        r"""<p>域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Env(self):
        r"""<p>切换后的环境 slug</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

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
        self._Domain = params.get("Domain")
        self._Env = params.get("Env")
        self._RequestId = params.get("RequestId")


class NsVerification(AbstractModel):
    r"""NS 归属校验信息。Makers 目前恒为 null

    """

    def __init__(self):
        r"""
        :param _NameServers: <p>NS 服务器</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type NameServers: list of str
        """
        self._NameServers = None

    @property
    def NameServers(self):
        r"""<p>NS 服务器</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers


    def _deserialize(self, params):
        self._NameServers = params.get("NameServers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OwnershipVerification(AbstractModel):
    r"""域名归属校验信息

    """

    def __init__(self):
        r"""
        :param _DnsVerification: <p>DNS 校验</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsVerification: :class:`tencentcloud.makers.v20261113.models.DnsVerification`
        :param _FileVerification: <p>文件校验</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type FileVerification: :class:`tencentcloud.makers.v20261113.models.FileVerification`
        :param _NsVerification: <p>NS 校验</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type NsVerification: :class:`tencentcloud.makers.v20261113.models.NsVerification`
        """
        self._DnsVerification = None
        self._FileVerification = None
        self._NsVerification = None

    @property
    def DnsVerification(self):
        r"""<p>DNS 校验</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.DnsVerification`
        """
        return self._DnsVerification

    @DnsVerification.setter
    def DnsVerification(self, DnsVerification):
        self._DnsVerification = DnsVerification

    @property
    def FileVerification(self):
        r"""<p>文件校验</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.FileVerification`
        """
        return self._FileVerification

    @FileVerification.setter
    def FileVerification(self, FileVerification):
        self._FileVerification = FileVerification

    @property
    def NsVerification(self):
        r"""<p>NS 校验</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.NsVerification`
        """
        return self._NsVerification

    @NsVerification.setter
    def NsVerification(self, NsVerification):
        self._NsVerification = NsVerification


    def _deserialize(self, params):
        if params.get("DnsVerification") is not None:
            self._DnsVerification = DnsVerification()
            self._DnsVerification._deserialize(params.get("DnsVerification"))
        if params.get("FileVerification") is not None:
            self._FileVerification = FileVerification()
            self._FileVerification._deserialize(params.get("FileVerification"))
        if params.get("NsVerification") is not None:
            self._NsVerification = NsVerification()
            self._NsVerification._deserialize(params.get("NsVerification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Project(AbstractModel):
    r"""项目。字段与 DescribeProjects 的实际返回一致

    """

    def __init__(self):
        r"""
        :param _ProjectId: <p>项目 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _Name: <p>项目名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Status: <p>项目状态。Normal、Ban、Unlink、Process、Pending、Offline</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ZoneId: <p>站点 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _Area: <p>加速区域。mainland、overseas、global</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        :param _Provider: <p>代码来源。Github、Gitee、Coding、Upload、Gitlab、Bitbucket、Cnb</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Provider: str
        :param _Channel: <p>创建来源。Template、Custom、CLI、Guest</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Channel: str
        :param _PresetDomain: <p>预设域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PresetDomain: str
        :param _PresetDomainStatus: <p>预设域名状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PresetDomainStatus: str
        :param _RootDir: <p>项目根目录</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RootDir: str
        :param _OutputDir: <p>构建产物目录</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputDir: str
        :param _BuildCmd: <p>构建命令</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildCmd: str
        :param _InstallCmd: <p>安装命令</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InstallCmd: str
        :param _Framework: <p>框架</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Framework: str
        :param _NodejsVersion: <p>Node.js 版本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type NodejsVersion: str
        :param _RepoUrl: <p>仓库地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoUrl: str
        :param _RepoOwner: <p>仓库所有者</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoOwner: str
        :param _RepoName: <p>仓库名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoName: str
        :param _RepoBranch: <p>生产分支</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoBranch: str
        :param _RepoPreBranches: <p>预览分支</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoPreBranches: list of str
        :param _Regions: <p>部署地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Regions: :class:`tencentcloud.makers.v20261113.models.Regions`
        :param _EnvVars: <p>环境变量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvVars: list of ProjectEnvVar
        :param _CustomDomains: <p>自定义域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomDomains: list of CustomDomainItem
        :param _Deployment: <p>最近一次部署</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployment: :class:`tencentcloud.makers.v20261113.models.ProjectDeployment`
        :param _IsAgent: <p>是否 Agent 项目。1 是，0 否</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAgent: int
        :param _AgentFramework: <p>Agent 框架。非 Agent 项目为空</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentFramework: str
        :param _IsTld: <p>是否命中用户级泛域名。1 是，0 否</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsTld: int
        :param _CreatedOn: <p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: str
        :param _ModifiedOn: <p>更新时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedOn: str
        :param _BuildMachine: <p>构建规格客户契约</p><p>枚举值：</p><ul><li>standard： 4C6G，默认档，所有套餐可用</li><li>enhanced： 8C14G，专业版及以上可用；低配套餐声明时按 standard 处理并提示升级</li></ul><p>默认值：standard</p>
        :type BuildMachine: str
        """
        self._ProjectId = None
        self._Name = None
        self._Status = None
        self._ZoneId = None
        self._Area = None
        self._Provider = None
        self._Channel = None
        self._PresetDomain = None
        self._PresetDomainStatus = None
        self._RootDir = None
        self._OutputDir = None
        self._BuildCmd = None
        self._InstallCmd = None
        self._Framework = None
        self._NodejsVersion = None
        self._RepoUrl = None
        self._RepoOwner = None
        self._RepoName = None
        self._RepoBranch = None
        self._RepoPreBranches = None
        self._Regions = None
        self._EnvVars = None
        self._CustomDomains = None
        self._Deployment = None
        self._IsAgent = None
        self._AgentFramework = None
        self._IsTld = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._BuildMachine = None

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        r"""<p>项目名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""<p>项目状态。Normal、Ban、Unlink、Process、Pending、Offline</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ZoneId(self):
        r"""<p>站点 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Area(self):
        r"""<p>加速区域。mainland、overseas、global</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Provider(self):
        r"""<p>代码来源。Github、Gitee、Coding、Upload、Gitlab、Bitbucket、Cnb</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def Channel(self):
        r"""<p>创建来源。Template、Custom、CLI、Guest</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def PresetDomain(self):
        r"""<p>预设域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PresetDomain

    @PresetDomain.setter
    def PresetDomain(self, PresetDomain):
        self._PresetDomain = PresetDomain

    @property
    def PresetDomainStatus(self):
        r"""<p>预设域名状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PresetDomainStatus

    @PresetDomainStatus.setter
    def PresetDomainStatus(self, PresetDomainStatus):
        self._PresetDomainStatus = PresetDomainStatus

    @property
    def RootDir(self):
        r"""<p>项目根目录</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RootDir

    @RootDir.setter
    def RootDir(self, RootDir):
        self._RootDir = RootDir

    @property
    def OutputDir(self):
        r"""<p>构建产物目录</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OutputDir

    @OutputDir.setter
    def OutputDir(self, OutputDir):
        self._OutputDir = OutputDir

    @property
    def BuildCmd(self):
        r"""<p>构建命令</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BuildCmd

    @BuildCmd.setter
    def BuildCmd(self, BuildCmd):
        self._BuildCmd = BuildCmd

    @property
    def InstallCmd(self):
        r"""<p>安装命令</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstallCmd

    @InstallCmd.setter
    def InstallCmd(self, InstallCmd):
        self._InstallCmd = InstallCmd

    @property
    def Framework(self):
        r"""<p>框架</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Framework

    @Framework.setter
    def Framework(self, Framework):
        self._Framework = Framework

    @property
    def NodejsVersion(self):
        r"""<p>Node.js 版本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodejsVersion

    @NodejsVersion.setter
    def NodejsVersion(self, NodejsVersion):
        self._NodejsVersion = NodejsVersion

    @property
    def RepoUrl(self):
        r"""<p>仓库地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RepoUrl

    @RepoUrl.setter
    def RepoUrl(self, RepoUrl):
        self._RepoUrl = RepoUrl

    @property
    def RepoOwner(self):
        r"""<p>仓库所有者</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RepoOwner

    @RepoOwner.setter
    def RepoOwner(self, RepoOwner):
        self._RepoOwner = RepoOwner

    @property
    def RepoName(self):
        r"""<p>仓库名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def RepoBranch(self):
        r"""<p>生产分支</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RepoBranch

    @RepoBranch.setter
    def RepoBranch(self, RepoBranch):
        self._RepoBranch = RepoBranch

    @property
    def RepoPreBranches(self):
        r"""<p>预览分支</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RepoPreBranches

    @RepoPreBranches.setter
    def RepoPreBranches(self, RepoPreBranches):
        self._RepoPreBranches = RepoPreBranches

    @property
    def Regions(self):
        r"""<p>部署地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.Regions`
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def EnvVars(self):
        r"""<p>环境变量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ProjectEnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars

    @property
    def CustomDomains(self):
        r"""<p>自定义域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CustomDomainItem
        """
        return self._CustomDomains

    @CustomDomains.setter
    def CustomDomains(self, CustomDomains):
        self._CustomDomains = CustomDomains

    @property
    def Deployment(self):
        r"""<p>最近一次部署</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.ProjectDeployment`
        """
        return self._Deployment

    @Deployment.setter
    def Deployment(self, Deployment):
        self._Deployment = Deployment

    @property
    def IsAgent(self):
        r"""<p>是否 Agent 项目。1 是，0 否</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsAgent

    @IsAgent.setter
    def IsAgent(self, IsAgent):
        self._IsAgent = IsAgent

    @property
    def AgentFramework(self):
        r"""<p>Agent 框架。非 Agent 项目为空</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentFramework

    @AgentFramework.setter
    def AgentFramework(self, AgentFramework):
        self._AgentFramework = AgentFramework

    @property
    def IsTld(self):
        r"""<p>是否命中用户级泛域名。1 是，0 否</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsTld

    @IsTld.setter
    def IsTld(self, IsTld):
        self._IsTld = IsTld

    @property
    def CreatedOn(self):
        r"""<p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        r"""<p>更新时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def BuildMachine(self):
        r"""<p>构建规格客户契约</p><p>枚举值：</p><ul><li>standard： 4C6G，默认档，所有套餐可用</li><li>enhanced： 8C14G，专业版及以上可用；低配套餐声明时按 standard 处理并提示升级</li></ul><p>默认值：standard</p>
        :rtype: str
        """
        return self._BuildMachine

    @BuildMachine.setter
    def BuildMachine(self, BuildMachine):
        self._BuildMachine = BuildMachine


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._ZoneId = params.get("ZoneId")
        self._Area = params.get("Area")
        self._Provider = params.get("Provider")
        self._Channel = params.get("Channel")
        self._PresetDomain = params.get("PresetDomain")
        self._PresetDomainStatus = params.get("PresetDomainStatus")
        self._RootDir = params.get("RootDir")
        self._OutputDir = params.get("OutputDir")
        self._BuildCmd = params.get("BuildCmd")
        self._InstallCmd = params.get("InstallCmd")
        self._Framework = params.get("Framework")
        self._NodejsVersion = params.get("NodejsVersion")
        self._RepoUrl = params.get("RepoUrl")
        self._RepoOwner = params.get("RepoOwner")
        self._RepoName = params.get("RepoName")
        self._RepoBranch = params.get("RepoBranch")
        self._RepoPreBranches = params.get("RepoPreBranches")
        if params.get("Regions") is not None:
            self._Regions = Regions()
            self._Regions._deserialize(params.get("Regions"))
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = ProjectEnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        if params.get("CustomDomains") is not None:
            self._CustomDomains = []
            for item in params.get("CustomDomains"):
                obj = CustomDomainItem()
                obj._deserialize(item)
                self._CustomDomains.append(obj)
        if params.get("Deployment") is not None:
            self._Deployment = ProjectDeployment()
            self._Deployment._deserialize(params.get("Deployment"))
        self._IsAgent = params.get("IsAgent")
        self._AgentFramework = params.get("AgentFramework")
        self._IsTld = params.get("IsTld")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        self._BuildMachine = params.get("BuildMachine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectDeployment(AbstractModel):
    r"""项目最近一次部署

    """

    def __init__(self):
        r"""
        :param _DeploymentId: <p>部署 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploymentId: str
        :param _ProjectId: <p>项目 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _Status: <p>部署状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _BuildCost: <p>构建耗时，单位毫秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildCost: str
        :param _ViaMeta: <p>触发来源</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ViaMeta: str
        :param _Env: <p>环境 slug</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Env: str
        :param _RepoBranch: <p>分支</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoBranch: str
        :param _RepoCommitHash: <p>提交哈希</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoCommitHash: str
        :param _RepoCommitMsg: <p>提交说明</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoCommitMsg: str
        :param _PreviewUrl: <p>预览地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param _CoverUrl: <p>封面地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverUrl: str
        :param _CreatedOn: <p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: str
        :param _ModifiedOn: <p>更新时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedOn: str
        :param _DplRepoUrl: <p>本次部署使用的仓库地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DplRepoUrl: str
        """
        self._DeploymentId = None
        self._ProjectId = None
        self._Status = None
        self._BuildCost = None
        self._ViaMeta = None
        self._Env = None
        self._RepoBranch = None
        self._RepoCommitHash = None
        self._RepoCommitMsg = None
        self._PreviewUrl = None
        self._CoverUrl = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._DplRepoUrl = None

    @property
    def DeploymentId(self):
        r"""<p>部署 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId

    @property
    def ProjectId(self):
        r"""<p>项目 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        r"""<p>部署状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BuildCost(self):
        r"""<p>构建耗时，单位毫秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BuildCost

    @BuildCost.setter
    def BuildCost(self, BuildCost):
        self._BuildCost = BuildCost

    @property
    def ViaMeta(self):
        r"""<p>触发来源</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ViaMeta

    @ViaMeta.setter
    def ViaMeta(self, ViaMeta):
        self._ViaMeta = ViaMeta

    @property
    def Env(self):
        r"""<p>环境 slug</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def RepoBranch(self):
        r"""<p>分支</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RepoBranch

    @RepoBranch.setter
    def RepoBranch(self, RepoBranch):
        self._RepoBranch = RepoBranch

    @property
    def RepoCommitHash(self):
        r"""<p>提交哈希</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RepoCommitHash

    @RepoCommitHash.setter
    def RepoCommitHash(self, RepoCommitHash):
        self._RepoCommitHash = RepoCommitHash

    @property
    def RepoCommitMsg(self):
        r"""<p>提交说明</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RepoCommitMsg

    @RepoCommitMsg.setter
    def RepoCommitMsg(self, RepoCommitMsg):
        self._RepoCommitMsg = RepoCommitMsg

    @property
    def PreviewUrl(self):
        r"""<p>预览地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def CoverUrl(self):
        r"""<p>封面地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CoverUrl

    @CoverUrl.setter
    def CoverUrl(self, CoverUrl):
        self._CoverUrl = CoverUrl

    @property
    def CreatedOn(self):
        r"""<p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        r"""<p>更新时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def DplRepoUrl(self):
        r"""<p>本次部署使用的仓库地址</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DplRepoUrl

    @DplRepoUrl.setter
    def DplRepoUrl(self, DplRepoUrl):
        self._DplRepoUrl = DplRepoUrl


    def _deserialize(self, params):
        self._DeploymentId = params.get("DeploymentId")
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._BuildCost = params.get("BuildCost")
        self._ViaMeta = params.get("ViaMeta")
        self._Env = params.get("Env")
        self._RepoBranch = params.get("RepoBranch")
        self._RepoCommitHash = params.get("RepoCommitHash")
        self._RepoCommitMsg = params.get("RepoCommitMsg")
        self._PreviewUrl = params.get("PreviewUrl")
        self._CoverUrl = params.get("CoverUrl")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        self._DplRepoUrl = params.get("DplRepoUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectEnvVar(AbstractModel):
    r"""项目列表里返回的环境变量，只有键和值

    """

    def __init__(self):
        r"""
        :param _Key: <p>变量名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: <p>变量值</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>变量名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>变量值</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectFilter(AbstractModel):
    r"""项目列表过滤条件。同一条件的 Values 之间为或

    """

    def __init__(self):
        r"""
        :param _Name: <p>过滤字段。ProjectId、Name、Status、Provider</p>
        :type Name: str
        :param _Values: <p>过滤值</p>
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""<p>过滤字段。ProjectId、Name、Status、Provider</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>过滤值</p>
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Regions(AbstractModel):
    r"""项目部署地域

    """

    def __init__(self):
        r"""
        :param _Mainland: <p>中国大陆地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Mainland: list of str
        :param _Overseas: <p>海外地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Overseas: list of str
        """
        self._Mainland = None
        self._Overseas = None

    @property
    def Mainland(self):
        r"""<p>中国大陆地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Mainland

    @Mainland.setter
    def Mainland(self, Mainland):
        self._Mainland = Mainland

    @property
    def Overseas(self):
        r"""<p>海外地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Overseas

    @Overseas.setter
    def Overseas(self, Overseas):
        self._Overseas = Overseas


    def _deserialize(self, params):
        self._Mainland = params.get("Mainland")
        self._Overseas = params.get("Overseas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchConfig(AbstractModel):
    r"""开关配置

    """

    def __init__(self):
        r"""
        :param _Switch: <p>on 或 off</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        r"""<p>on 或 off</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDomain(AbstractModel):
    r"""站点下的自定义域名

    """

    def __init__(self):
        r"""
        :param _Type: <p>Custom 或 Preset</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Domain: <p>域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Status: <p>域名状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Env: <p>绑定的环境 slug，默认 Production</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Env: str
        :param _ZoneId: <p>站点 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _Area: <p>加速区域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        :param _Cname: <p>CNAME</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param _MainDomain: <p>主域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type MainDomain: str
        :param _Ipv6: <p>IPv6</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        :param _Http2: <p>HTTP/2</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Http2: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        :param _OcspStapling: <p>OCSP</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OcspStapling: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        :param _ForceRedirect: <p>强制 HTTPS</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.makers.v20261113.models.ForceRedirectConfig`
        :param _Hsts: <p>HSTS</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Hsts: :class:`tencentcloud.makers.v20261113.models.HstsConfig`
        :param _OwnershipVerification: <p>归属校验</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnershipVerification: :class:`tencentcloud.makers.v20261113.models.OwnershipVerification`
        """
        self._Type = None
        self._Domain = None
        self._Status = None
        self._Env = None
        self._ZoneId = None
        self._Area = None
        self._Cname = None
        self._MainDomain = None
        self._Ipv6 = None
        self._Http2 = None
        self._OcspStapling = None
        self._ForceRedirect = None
        self._Hsts = None
        self._OwnershipVerification = None

    @property
    def Type(self):
        r"""<p>Custom 或 Preset</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Domain(self):
        r"""<p>域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        r"""<p>域名状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Env(self):
        r"""<p>绑定的环境 slug，默认 Production</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def ZoneId(self):
        r"""<p>站点 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Area(self):
        r"""<p>加速区域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Cname(self):
        r"""<p>CNAME</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def MainDomain(self):
        r"""<p>主域名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MainDomain

    @MainDomain.setter
    def MainDomain(self, MainDomain):
        self._MainDomain = MainDomain

    @property
    def Ipv6(self):
        r"""<p>IPv6</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        """
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def Http2(self):
        r"""<p>HTTP/2</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        """
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def OcspStapling(self):
        r"""<p>OCSP</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        """
        return self._OcspStapling

    @OcspStapling.setter
    def OcspStapling(self, OcspStapling):
        self._OcspStapling = OcspStapling

    @property
    def ForceRedirect(self):
        r"""<p>强制 HTTPS</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.ForceRedirectConfig`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Hsts(self):
        r"""<p>HSTS</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.HstsConfig`
        """
        return self._Hsts

    @Hsts.setter
    def Hsts(self, Hsts):
        self._Hsts = Hsts

    @property
    def OwnershipVerification(self):
        r"""<p>归属校验</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.makers.v20261113.models.OwnershipVerification`
        """
        return self._OwnershipVerification

    @OwnershipVerification.setter
    def OwnershipVerification(self, OwnershipVerification):
        self._OwnershipVerification = OwnershipVerification


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._Env = params.get("Env")
        self._ZoneId = params.get("ZoneId")
        self._Area = params.get("Area")
        self._Cname = params.get("Cname")
        self._MainDomain = params.get("MainDomain")
        if params.get("Ipv6") is not None:
            self._Ipv6 = SwitchConfig()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Http2") is not None:
            self._Http2 = SwitchConfig()
            self._Http2._deserialize(params.get("Http2"))
        if params.get("OcspStapling") is not None:
            self._OcspStapling = SwitchConfig()
            self._OcspStapling._deserialize(params.get("OcspStapling"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirectConfig()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Hsts") is not None:
            self._Hsts = HstsConfig()
            self._Hsts._deserialize(params.get("Hsts"))
        if params.get("OwnershipVerification") is not None:
            self._OwnershipVerification = OwnershipVerification()
            self._OwnershipVerification._deserialize(params.get("OwnershipVerification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        