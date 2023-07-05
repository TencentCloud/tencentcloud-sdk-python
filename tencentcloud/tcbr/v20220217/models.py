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


class BuildPacksInfo(AbstractModel):
    """BuildPacks信息

    """

    def __init__(self):
        r"""
        :param _BaseImage: 基础镜像
        :type BaseImage: str
        :param _EntryPoint: 启动命令
        :type EntryPoint: str
        :param _RepoLanguage: 语言
        :type RepoLanguage: str
        :param _UploadFilename: 上传文件名
        :type UploadFilename: str
        """
        self._BaseImage = None
        self._EntryPoint = None
        self._RepoLanguage = None
        self._UploadFilename = None

    @property
    def BaseImage(self):
        return self._BaseImage

    @BaseImage.setter
    def BaseImage(self, BaseImage):
        self._BaseImage = BaseImage

    @property
    def EntryPoint(self):
        return self._EntryPoint

    @EntryPoint.setter
    def EntryPoint(self, EntryPoint):
        self._EntryPoint = EntryPoint

    @property
    def RepoLanguage(self):
        return self._RepoLanguage

    @RepoLanguage.setter
    def RepoLanguage(self, RepoLanguage):
        self._RepoLanguage = RepoLanguage

    @property
    def UploadFilename(self):
        return self._UploadFilename

    @UploadFilename.setter
    def UploadFilename(self, UploadFilename):
        self._UploadFilename = UploadFilename


    def _deserialize(self, params):
        self._BaseImage = params.get("BaseImage")
        self._EntryPoint = params.get("EntryPoint")
        self._RepoLanguage = params.get("RepoLanguage")
        self._UploadFilename = params.get("UploadFilename")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsInfo(AbstractModel):
    """cls日志信息

    """

    def __init__(self):
        r"""
        :param _ClsRegion: cls所属地域
        :type ClsRegion: str
        :param _ClsLogsetId: cls日志集ID
        :type ClsLogsetId: str
        :param _ClsTopicId: cls日志主题ID
        :type ClsTopicId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._ClsRegion = None
        self._ClsLogsetId = None
        self._ClsTopicId = None
        self._CreateTime = None

    @property
    def ClsRegion(self):
        return self._ClsRegion

    @ClsRegion.setter
    def ClsRegion(self, ClsRegion):
        self._ClsRegion = ClsRegion

    @property
    def ClsLogsetId(self):
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsTopicId(self):
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ClsRegion = params.get("ClsRegion")
        self._ClsLogsetId = params.get("ClsLogsetId")
        self._ClsTopicId = params.get("ClsTopicId")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRunEnvRequest(AbstractModel):
    """CreateCloudRunEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageType: Trial,Standard,Professional,Enterprise
        :type PackageType: str
        :param _Alias: 环境别名，要以a-z开头，不能包含 a-z,0-9,- 以外的字符
        :type Alias: str
        :param _FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。
        :type FreeQuota: str
        :param _Flag: 订单标记。建议使用方统一转大小写之后再判断。
QuickStart：快速启动来源
Activity：活动来源
        :type Flag: str
        :param _VpcId: 私有网络Id
        :type VpcId: str
        :param _SubNetIds: 子网列表
        :type SubNetIds: list of str
        :param _ReqKey: 请求key 用于防重
        :type ReqKey: str
        :param _Source: 来源：wechat | cloud
        :type Source: str
        :param _Channel: 渠道：wechat | cloud
        :type Channel: str
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._PackageType = None
        self._Alias = None
        self._FreeQuota = None
        self._Flag = None
        self._VpcId = None
        self._SubNetIds = None
        self._ReqKey = None
        self._Source = None
        self._Channel = None
        self._EnvId = None

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def FreeQuota(self):
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubNetIds(self):
        return self._SubNetIds

    @SubNetIds.setter
    def SubNetIds(self, SubNetIds):
        self._SubNetIds = SubNetIds

    @property
    def ReqKey(self):
        return self._ReqKey

    @ReqKey.setter
    def ReqKey(self, ReqKey):
        self._ReqKey = ReqKey

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._PackageType = params.get("PackageType")
        self._Alias = params.get("Alias")
        self._FreeQuota = params.get("FreeQuota")
        self._Flag = params.get("Flag")
        self._VpcId = params.get("VpcId")
        self._SubNetIds = params.get("SubNetIds")
        self._ReqKey = params.get("ReqKey")
        self._Source = params.get("Source")
        self._Channel = params.get("Channel")
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRunEnvResponse(AbstractModel):
    """CreateCloudRunEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _TranId: 后付费订单号
        :type TranId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvId = None
        self._TranId = None
        self._RequestId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._TranId = params.get("TranId")
        self._RequestId = params.get("RequestId")


class CreateCloudRunServerRequest(AbstractModel):
    """CreateCloudRunServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _DeployInfo: 部署信息
        :type DeployInfo: :class:`tencentcloud.tcbr.v20220217.models.DeployParam`
        :param _ServerConfig: 服务配置信息
        :type ServerConfig: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        """
        self._EnvId = None
        self._ServerName = None
        self._DeployInfo = None
        self._ServerConfig = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def DeployInfo(self):
        return self._DeployInfo

    @DeployInfo.setter
    def DeployInfo(self, DeployInfo):
        self._DeployInfo = DeployInfo

    @property
    def ServerConfig(self):
        return self._ServerConfig

    @ServerConfig.setter
    def ServerConfig(self, ServerConfig):
        self._ServerConfig = ServerConfig


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        if params.get("DeployInfo") is not None:
            self._DeployInfo = DeployParam()
            self._DeployInfo._deserialize(params.get("DeployInfo"))
        if params.get("ServerConfig") is not None:
            self._ServerConfig = ServerBaseConfig()
            self._ServerConfig._deserialize(params.get("ServerConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRunServerResponse(AbstractModel):
    """CreateCloudRunServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 一键部署任务Id，微信云托管，暂时用不到
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DatabasesInfo(AbstractModel):
    """数据库资源信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库唯一标识
        :type InstanceId: str
        :param _Status: 状态。包含以下取值：
<li>INITIALIZING：资源初始化中</li>
<li>RUNNING：运行中，可正常使用的状态</li>
<li>UNUSABLE：禁用，不可用</li>
<li>OVERDUE：资源过期</li>
        :type Status: str
        :param _Region: 所属地域。
当前支持ap-shanghai
        :type Region: str
        """
        self._InstanceId = None
        self._Status = None
        self._Region = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployParam(AbstractModel):
    """部署参数

    """

    def __init__(self):
        r"""
        :param _DeployType: 部署类型：package/image/repository/pipeline/jar/war
        :type DeployType: str
        :param _ImageUrl: 部署类型为image时传入
        :type ImageUrl: str
        :param _PackageName: 部署类型为package时传入
        :type PackageName: str
        :param _PackageVersion: 部署类型为package时传入
        :type PackageVersion: str
        :param _DeployRemark: 部署备注
        :type DeployRemark: str
        :param _RepoInfo: 代码仓库信息
        :type RepoInfo: :class:`tencentcloud.tcbr.v20220217.models.RepositoryInfo`
        :param _BuildPacks: 无Dockerfile时填写
        :type BuildPacks: :class:`tencentcloud.tcbr.v20220217.models.BuildPacksInfo`
        :param _ReleaseType: 发布类型 GRAY | FULL
        :type ReleaseType: str
        """
        self._DeployType = None
        self._ImageUrl = None
        self._PackageName = None
        self._PackageVersion = None
        self._DeployRemark = None
        self._RepoInfo = None
        self._BuildPacks = None
        self._ReleaseType = None

    @property
    def DeployType(self):
        return self._DeployType

    @DeployType.setter
    def DeployType(self, DeployType):
        self._DeployType = DeployType

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def DeployRemark(self):
        return self._DeployRemark

    @DeployRemark.setter
    def DeployRemark(self, DeployRemark):
        self._DeployRemark = DeployRemark

    @property
    def RepoInfo(self):
        return self._RepoInfo

    @RepoInfo.setter
    def RepoInfo(self, RepoInfo):
        self._RepoInfo = RepoInfo

    @property
    def BuildPacks(self):
        return self._BuildPacks

    @BuildPacks.setter
    def BuildPacks(self, BuildPacks):
        self._BuildPacks = BuildPacks

    @property
    def ReleaseType(self):
        return self._ReleaseType

    @ReleaseType.setter
    def ReleaseType(self, ReleaseType):
        self._ReleaseType = ReleaseType


    def _deserialize(self, params):
        self._DeployType = params.get("DeployType")
        self._ImageUrl = params.get("ImageUrl")
        self._PackageName = params.get("PackageName")
        self._PackageVersion = params.get("PackageVersion")
        self._DeployRemark = params.get("DeployRemark")
        if params.get("RepoInfo") is not None:
            self._RepoInfo = RepositoryInfo()
            self._RepoInfo._deserialize(params.get("RepoInfo"))
        if params.get("BuildPacks") is not None:
            self._BuildPacks = BuildPacksInfo()
            self._BuildPacks._deserialize(params.get("BuildPacks"))
        self._ReleaseType = params.get("ReleaseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunEnvsRequest(AbstractModel):
    """DescribeCloudRunEnvs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID，如果传了这个参数则只返回该环境的相关信息
        :type EnvId: str
        :param _IsVisible: 指定Channels字段为可见渠道列表或不可见渠道列表
如只想获取渠道A的环境 就填写IsVisible= true,Channels = ["A"], 过滤渠道A拉取其他渠道环境时填写IsVisible= false,Channels = ["A"]
        :type IsVisible: bool
        :param _Channels: 渠道列表，代表可见或不可见渠道由IsVisible参数指定
        :type Channels: list of str
        """
        self._EnvId = None
        self._IsVisible = None
        self._Channels = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def IsVisible(self):
        return self._IsVisible

    @IsVisible.setter
    def IsVisible(self, IsVisible):
        self._IsVisible = IsVisible

    @property
    def Channels(self):
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._IsVisible = params.get("IsVisible")
        self._Channels = params.get("Channels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunEnvsResponse(AbstractModel):
    """DescribeCloudRunEnvs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvList: 环境信息列表
        :type EnvList: list of EnvInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvList = None
        self._RequestId = None

    @property
    def EnvList(self):
        return self._EnvList

    @EnvList.setter
    def EnvList(self, EnvList):
        self._EnvList = EnvList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnvList") is not None:
            self._EnvList = []
            for item in params.get("EnvList"):
                obj = EnvInfo()
                obj._deserialize(item)
                self._EnvList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudRunServerDetailRequest(AbstractModel):
    """DescribeCloudRunServerDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        """
        self._EnvId = None
        self._ServerName = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunServerDetailResponse(AbstractModel):
    """DescribeCloudRunServerDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BaseInfo: 服务基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseInfo: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseInfo`
        :param _ServerConfig: 服务配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerConfig: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        :param _OnlineVersionInfos: 在线版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineVersionInfos: list of OnlineVersionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BaseInfo = None
        self._ServerConfig = None
        self._OnlineVersionInfos = None
        self._RequestId = None

    @property
    def BaseInfo(self):
        return self._BaseInfo

    @BaseInfo.setter
    def BaseInfo(self, BaseInfo):
        self._BaseInfo = BaseInfo

    @property
    def ServerConfig(self):
        return self._ServerConfig

    @ServerConfig.setter
    def ServerConfig(self, ServerConfig):
        self._ServerConfig = ServerConfig

    @property
    def OnlineVersionInfos(self):
        return self._OnlineVersionInfos

    @OnlineVersionInfos.setter
    def OnlineVersionInfos(self, OnlineVersionInfos):
        self._OnlineVersionInfos = OnlineVersionInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BaseInfo") is not None:
            self._BaseInfo = ServerBaseInfo()
            self._BaseInfo._deserialize(params.get("BaseInfo"))
        if params.get("ServerConfig") is not None:
            self._ServerConfig = ServerBaseConfig()
            self._ServerConfig._deserialize(params.get("ServerConfig"))
        if params.get("OnlineVersionInfos") is not None:
            self._OnlineVersionInfos = []
            for item in params.get("OnlineVersionInfos"):
                obj = OnlineVersionInfo()
                obj._deserialize(item)
                self._OnlineVersionInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudRunServersRequest(AbstractModel):
    """DescribeCloudRunServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _PageSize: 默认为9， 最大为30
不传或传0时 取默认9
大于30时取30
        :type PageSize: int
        :param _PageNum: 不传或传0时 会默认为1
        :type PageNum: int
        """
        self._EnvId = None
        self._PageSize = None
        self._PageNum = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunServersResponse(AbstractModel):
    """DescribeCloudRunServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServerList: 服务列表
        :type ServerList: list of ServerBaseInfo
        :param _Total: 服务总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServerList = None
        self._Total = None
        self._RequestId = None

    @property
    def ServerList(self):
        return self._ServerList

    @ServerList.setter
    def ServerList(self, ServerList):
        self._ServerList = ServerList

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServerList") is not None:
            self._ServerList = []
            for item in params.get("ServerList"):
                obj = ServerBaseInfo()
                obj._deserialize(item)
                self._ServerList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeEnvBaseInfoRequest(AbstractModel):
    """DescribeEnvBaseInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境 Id
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvBaseInfoResponse(AbstractModel):
    """DescribeEnvBaseInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvBaseInfo: 环境基础信息
        :type EnvBaseInfo: :class:`tencentcloud.tcbr.v20220217.models.EnvBaseInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvBaseInfo = None
        self._RequestId = None

    @property
    def EnvBaseInfo(self):
        return self._EnvBaseInfo

    @EnvBaseInfo.setter
    def EnvBaseInfo(self, EnvBaseInfo):
        self._EnvBaseInfo = EnvBaseInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnvBaseInfo") is not None:
            self._EnvBaseInfo = EnvBaseInfo()
            self._EnvBaseInfo._deserialize(params.get("EnvBaseInfo"))
        self._RequestId = params.get("RequestId")


class DescribeServerManageTaskRequest(AbstractModel):
    """DescribeServerManageTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _TaskId: 任务Id
        :type TaskId: int
        :param _OperatorRemark: 操作标识
        :type OperatorRemark: str
        """
        self._EnvId = None
        self._ServerName = None
        self._TaskId = None
        self._OperatorRemark = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def OperatorRemark(self):
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._TaskId = params.get("TaskId")
        self._OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerManageTaskResponse(AbstractModel):
    """DescribeServerManageTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsExist: 是否存在
        :type IsExist: bool
        :param _Task: 任务信息
        :type Task: :class:`tencentcloud.tcbr.v20220217.models.ServerManageTaskInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsExist = None
        self._Task = None
        self._RequestId = None

    @property
    def IsExist(self):
        return self._IsExist

    @IsExist.setter
    def IsExist(self, IsExist):
        self._IsExist = IsExist

    @property
    def Task(self):
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsExist = params.get("IsExist")
        if params.get("Task") is not None:
            self._Task = ServerManageTaskInfo()
            self._Task._deserialize(params.get("Task"))
        self._RequestId = params.get("RequestId")


class EnvBaseInfo(AbstractModel):
    """环境基础信息

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _PackageType: 套餐类型：Trial ｜ Standard ｜ Professional ｜ Enterprise
        :type PackageType: str
        :param _VpcId: VPC Id
        :type VpcId: str
        :param _CreateTime: 环境创建时间
        :type CreateTime: str
        :param _Alias: 环境别名
        :type Alias: str
        :param _Status: 环境状态
        :type Status: str
        :param _Region: 环境地域
        :type Region: str
        :param _EnvType: 环境类型 tcbr ｜ run
        :type EnvType: str
        :param _SubnetIds: 子网id
        :type SubnetIds: str
        """
        self._EnvId = None
        self._PackageType = None
        self._VpcId = None
        self._CreateTime = None
        self._Alias = None
        self._Status = None
        self._Region = None
        self._EnvType = None
        self._SubnetIds = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._PackageType = params.get("PackageType")
        self._VpcId = params.get("VpcId")
        self._CreateTime = params.get("CreateTime")
        self._Alias = params.get("Alias")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._EnvType = params.get("EnvType")
        self._SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvInfo(AbstractModel):
    """环境信息

    """

    def __init__(self):
        r"""
        :param _EnvId: 账户下该环境唯一标识
        :type EnvId: str
        :param _Source: 环境来源。包含以下取值：
<li>miniapp：微信小程序</li>
<li>qcloud ：腾讯云</li>
        :type Source: str
        :param _Alias: 环境别名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符
        :type Alias: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 最后修改时间
        :type UpdateTime: str
        :param _Status: 环境状态。包含以下取值：
<li>NORMAL：正常可用</li>
<li>UNAVAILABLE：服务不可用，可能是尚未初始化或者初始化过程中</li>
        :type Status: str
        :param _IsAutoDegrade: 是否到期自动降为免费版
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAutoDegrade: bool
        :param _EnvChannel: 环境渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvChannel: str
        :param _PayMode: 支付方式。包含以下取值：
<li> prepayment：预付费</li>
<li> postpaid：后付费</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param _IsDefault: 是否为默认环境
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: bool
        :param _Region: 环境所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _EnvType: 环境类型：baas, run, hosting, weda,tcbr
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvType: str
        :param _Databases: 数据库列表
        :type Databases: list of DatabasesInfo
        :param _Storages: 存储列表
        :type Storages: list of StorageInfo
        :param _Functions: 函数列表
        :type Functions: list of FunctionInfo
        :param _LogServices: 云日志服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogServices: list of LogServiceInfo
        :param _StaticStorages: 静态资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StaticStorages: list of StaticStorageInfo
        :param _Tags: 环境标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _CustomLogServices: 自定义日志服务
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLogServices: list of ClsInfo
        :param _PackageId: tcb产品套餐ID，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param _PackageName: 套餐中文名称，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        """
        self._EnvId = None
        self._Source = None
        self._Alias = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Status = None
        self._IsAutoDegrade = None
        self._EnvChannel = None
        self._PayMode = None
        self._IsDefault = None
        self._Region = None
        self._EnvType = None
        self._Databases = None
        self._Storages = None
        self._Functions = None
        self._LogServices = None
        self._StaticStorages = None
        self._Tags = None
        self._CustomLogServices = None
        self._PackageId = None
        self._PackageName = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsAutoDegrade(self):
        return self._IsAutoDegrade

    @IsAutoDegrade.setter
    def IsAutoDegrade(self, IsAutoDegrade):
        self._IsAutoDegrade = IsAutoDegrade

    @property
    def EnvChannel(self):
        return self._EnvChannel

    @EnvChannel.setter
    def EnvChannel(self, EnvChannel):
        self._EnvChannel = EnvChannel

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def Databases(self):
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def Storages(self):
        return self._Storages

    @Storages.setter
    def Storages(self, Storages):
        self._Storages = Storages

    @property
    def Functions(self):
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def LogServices(self):
        return self._LogServices

    @LogServices.setter
    def LogServices(self, LogServices):
        self._LogServices = LogServices

    @property
    def StaticStorages(self):
        return self._StaticStorages

    @StaticStorages.setter
    def StaticStorages(self, StaticStorages):
        self._StaticStorages = StaticStorages

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CustomLogServices(self):
        return self._CustomLogServices

    @CustomLogServices.setter
    def CustomLogServices(self, CustomLogServices):
        self._CustomLogServices = CustomLogServices

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Source = params.get("Source")
        self._Alias = params.get("Alias")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._IsAutoDegrade = params.get("IsAutoDegrade")
        self._EnvChannel = params.get("EnvChannel")
        self._PayMode = params.get("PayMode")
        self._IsDefault = params.get("IsDefault")
        self._Region = params.get("Region")
        self._EnvType = params.get("EnvType")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = DatabasesInfo()
                obj._deserialize(item)
                self._Databases.append(obj)
        if params.get("Storages") is not None:
            self._Storages = []
            for item in params.get("Storages"):
                obj = StorageInfo()
                obj._deserialize(item)
                self._Storages.append(obj)
        if params.get("Functions") is not None:
            self._Functions = []
            for item in params.get("Functions"):
                obj = FunctionInfo()
                obj._deserialize(item)
                self._Functions.append(obj)
        if params.get("LogServices") is not None:
            self._LogServices = []
            for item in params.get("LogServices"):
                obj = LogServiceInfo()
                obj._deserialize(item)
                self._LogServices.append(obj)
        if params.get("StaticStorages") is not None:
            self._StaticStorages = []
            for item in params.get("StaticStorages"):
                obj = StaticStorageInfo()
                obj._deserialize(item)
                self._StaticStorages.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("CustomLogServices") is not None:
            self._CustomLogServices = []
            for item in params.get("CustomLogServices"):
                obj = ClsInfo()
                obj._deserialize(item)
                self._CustomLogServices.append(obj)
        self._PackageId = params.get("PackageId")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionInfo(AbstractModel):
    """函数的信息

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Region: 所属地域。
当前支持ap-shanghai
        :type Region: str
        """
        self._Namespace = None
        self._Region = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HpaPolicy(AbstractModel):
    """扩缩容入参

    """

    def __init__(self):
        r"""
        :param _PolicyType: 扩缩容类型
        :type PolicyType: str
        :param _PolicyThreshold: 扩缩容阈值
        :type PolicyThreshold: int
        """
        self._PolicyType = None
        self._PolicyThreshold = None

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyThreshold(self):
        return self._PolicyThreshold

    @PolicyThreshold.setter
    def PolicyThreshold(self, PolicyThreshold):
        self._PolicyThreshold = PolicyThreshold


    def _deserialize(self, params):
        self._PolicyType = params.get("PolicyType")
        self._PolicyThreshold = params.get("PolicyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogServiceInfo(AbstractModel):
    """云日志服务相关信息

    """

    def __init__(self):
        r"""
        :param _LogsetName: log名
        :type LogsetName: str
        :param _LogsetId: log-id
        :type LogsetId: str
        :param _TopicName: topic名
        :type TopicName: str
        :param _TopicId: topic-id
        :type TopicId: str
        :param _Region: cls日志所属地域
        :type Region: str
        """
        self._LogsetName = None
        self._LogsetId = None
        self._TopicName = None
        self._TopicId = None
        self._Region = None

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._LogsetName = params.get("LogsetName")
        self._LogsetId = params.get("LogsetId")
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectKV(AbstractModel):
    """通用Key Value

    """

    def __init__(self):
        r"""
        :param _Key: 键值对Key
        :type Key: str
        :param _Value: 键值对Value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class OnlineVersionInfo(AbstractModel):
    """在线版本信息

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _ImageUrl: 镜像url
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param _FlowRatio: 流量
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowRatio: str
        """
        self._VersionName = None
        self._ImageUrl = None
        self._FlowRatio = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def FlowRatio(self):
        return self._FlowRatio

    @FlowRatio.setter
    def FlowRatio(self, FlowRatio):
        self._FlowRatio = FlowRatio


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._ImageUrl = params.get("ImageUrl")
        self._FlowRatio = params.get("FlowRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateServerManageRequest(AbstractModel):
    """OperateServerManage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _TaskId: 任报Id
        :type TaskId: int
        :param _OperateType: 操作类型:cancel | go_back | done
        :type OperateType: str
        :param _OperatorRemark: 操作标识
        :type OperatorRemark: str
        """
        self._EnvId = None
        self._ServerName = None
        self._TaskId = None
        self._OperateType = None
        self._OperatorRemark = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def OperateType(self):
        return self._OperateType

    @OperateType.setter
    def OperateType(self, OperateType):
        self._OperateType = OperateType

    @property
    def OperatorRemark(self):
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._TaskId = params.get("TaskId")
        self._OperateType = params.get("OperateType")
        self._OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateServerManageResponse(AbstractModel):
    """OperateServerManage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReleaseGrayRequest(AbstractModel):
    """ReleaseGray请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _GrayType: 灰度类型
        :type GrayType: str
        :param _TrafficType: 流量类型
        :type TrafficType: str
        :param _VersionFlowItems: 流量策略
        :type VersionFlowItems: list of VersionFlowInfo
        :param _OperatorRemark: 操作标识
        :type OperatorRemark: str
        :param _GrayFlowRatio: 流量比例
        :type GrayFlowRatio: int
        """
        self._EnvId = None
        self._ServerName = None
        self._GrayType = None
        self._TrafficType = None
        self._VersionFlowItems = None
        self._OperatorRemark = None
        self._GrayFlowRatio = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def GrayType(self):
        return self._GrayType

    @GrayType.setter
    def GrayType(self, GrayType):
        self._GrayType = GrayType

    @property
    def TrafficType(self):
        return self._TrafficType

    @TrafficType.setter
    def TrafficType(self, TrafficType):
        self._TrafficType = TrafficType

    @property
    def VersionFlowItems(self):
        return self._VersionFlowItems

    @VersionFlowItems.setter
    def VersionFlowItems(self, VersionFlowItems):
        self._VersionFlowItems = VersionFlowItems

    @property
    def OperatorRemark(self):
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark

    @property
    def GrayFlowRatio(self):
        return self._GrayFlowRatio

    @GrayFlowRatio.setter
    def GrayFlowRatio(self, GrayFlowRatio):
        self._GrayFlowRatio = GrayFlowRatio


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._GrayType = params.get("GrayType")
        self._TrafficType = params.get("TrafficType")
        if params.get("VersionFlowItems") is not None:
            self._VersionFlowItems = []
            for item in params.get("VersionFlowItems"):
                obj = VersionFlowInfo()
                obj._deserialize(item)
                self._VersionFlowItems.append(obj)
        self._OperatorRemark = params.get("OperatorRemark")
        self._GrayFlowRatio = params.get("GrayFlowRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseGrayResponse(AbstractModel):
    """ReleaseGray返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RepositoryInfo(AbstractModel):
    """代码仓库信息

    """

    def __init__(self):
        r"""
        :param _Source: git source
        :type Source: str
        :param _Repo: 仓库名
        :type Repo: str
        :param _Branch: 分支名
        :type Branch: str
        """
        self._Source = None
        self._Repo = None
        self._Branch = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Repo(self):
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def Branch(self):
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Repo = params.get("Repo")
        self._Branch = params.get("Branch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerBaseConfig(AbstractModel):
    """服务基础配置信息

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境 Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _OpenAccessTypes: 是否开启公网访问
        :type OpenAccessTypes: list of str
        :param _Cpu: Cpu 规格
        :type Cpu: float
        :param _Mem: Mem 规格
        :type Mem: float
        :param _MinNum: 最小副本数
        :type MinNum: int
        :param _MaxNum: 最大副本数
        :type MaxNum: int
        :param _PolicyDetails: 扩缩容配置
        :type PolicyDetails: list of HpaPolicy
        :param _CustomLogs: 日志采集路径
        :type CustomLogs: str
        :param _EnvParams: 环境变量
        :type EnvParams: str
        :param _InitialDelaySeconds: 延迟检测时间
        :type InitialDelaySeconds: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Port: 服务端口
        :type Port: int
        :param _HasDockerfile: 是否有Dockerfile
        :type HasDockerfile: bool
        :param _Dockerfile: Dockerfile 文件名
        :type Dockerfile: str
        :param _BuildDir: 构建目录
        :type BuildDir: str
        :param _LogType: 日志类型: none | default | custom
        :type LogType: str
        :param _LogSetId: cls setId
        :type LogSetId: str
        :param _LogTopicId: cls 主题id
        :type LogTopicId: str
        :param _LogParseType: 解析类型：json ｜ line
        :type LogParseType: str
        """
        self._EnvId = None
        self._ServerName = None
        self._OpenAccessTypes = None
        self._Cpu = None
        self._Mem = None
        self._MinNum = None
        self._MaxNum = None
        self._PolicyDetails = None
        self._CustomLogs = None
        self._EnvParams = None
        self._InitialDelaySeconds = None
        self._CreateTime = None
        self._Port = None
        self._HasDockerfile = None
        self._Dockerfile = None
        self._BuildDir = None
        self._LogType = None
        self._LogSetId = None
        self._LogTopicId = None
        self._LogParseType = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def OpenAccessTypes(self):
        return self._OpenAccessTypes

    @OpenAccessTypes.setter
    def OpenAccessTypes(self, OpenAccessTypes):
        self._OpenAccessTypes = OpenAccessTypes

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def MinNum(self):
        return self._MinNum

    @MinNum.setter
    def MinNum(self, MinNum):
        self._MinNum = MinNum

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum

    @property
    def PolicyDetails(self):
        return self._PolicyDetails

    @PolicyDetails.setter
    def PolicyDetails(self, PolicyDetails):
        self._PolicyDetails = PolicyDetails

    @property
    def CustomLogs(self):
        return self._CustomLogs

    @CustomLogs.setter
    def CustomLogs(self, CustomLogs):
        self._CustomLogs = CustomLogs

    @property
    def EnvParams(self):
        return self._EnvParams

    @EnvParams.setter
    def EnvParams(self, EnvParams):
        self._EnvParams = EnvParams

    @property
    def InitialDelaySeconds(self):
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def HasDockerfile(self):
        return self._HasDockerfile

    @HasDockerfile.setter
    def HasDockerfile(self, HasDockerfile):
        self._HasDockerfile = HasDockerfile

    @property
    def Dockerfile(self):
        return self._Dockerfile

    @Dockerfile.setter
    def Dockerfile(self, Dockerfile):
        self._Dockerfile = Dockerfile

    @property
    def BuildDir(self):
        return self._BuildDir

    @BuildDir.setter
    def BuildDir(self, BuildDir):
        self._BuildDir = BuildDir

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def LogSetId(self):
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def LogTopicId(self):
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def LogParseType(self):
        return self._LogParseType

    @LogParseType.setter
    def LogParseType(self, LogParseType):
        self._LogParseType = LogParseType


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._OpenAccessTypes = params.get("OpenAccessTypes")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._MinNum = params.get("MinNum")
        self._MaxNum = params.get("MaxNum")
        if params.get("PolicyDetails") is not None:
            self._PolicyDetails = []
            for item in params.get("PolicyDetails"):
                obj = HpaPolicy()
                obj._deserialize(item)
                self._PolicyDetails.append(obj)
        self._CustomLogs = params.get("CustomLogs")
        self._EnvParams = params.get("EnvParams")
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        self._CreateTime = params.get("CreateTime")
        self._Port = params.get("Port")
        self._HasDockerfile = params.get("HasDockerfile")
        self._Dockerfile = params.get("Dockerfile")
        self._BuildDir = params.get("BuildDir")
        self._LogType = params.get("LogType")
        self._LogSetId = params.get("LogSetId")
        self._LogTopicId = params.get("LogTopicId")
        self._LogParseType = params.get("LogParseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerBaseInfo(AbstractModel):
    """服务基本信息

    """

    def __init__(self):
        r"""
        :param _ServerName: 服务名
        :type ServerName: str
        :param _DefaultDomainName: 默认服务域名
        :type DefaultDomainName: str
        :param _CustomDomainName: 自定义域名
        :type CustomDomainName: str
        :param _Status: 服务状态：running/deploying/deploy_failed
        :type Status: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _AccessTypes: 公网访问类型
        :type AccessTypes: list of str
        :param _CustomDomainNames: 展示自定义域名
        :type CustomDomainNames: list of str
        """
        self._ServerName = None
        self._DefaultDomainName = None
        self._CustomDomainName = None
        self._Status = None
        self._UpdateTime = None
        self._AccessTypes = None
        self._CustomDomainNames = None

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def DefaultDomainName(self):
        return self._DefaultDomainName

    @DefaultDomainName.setter
    def DefaultDomainName(self, DefaultDomainName):
        self._DefaultDomainName = DefaultDomainName

    @property
    def CustomDomainName(self):
        return self._CustomDomainName

    @CustomDomainName.setter
    def CustomDomainName(self, CustomDomainName):
        self._CustomDomainName = CustomDomainName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AccessTypes(self):
        return self._AccessTypes

    @AccessTypes.setter
    def AccessTypes(self, AccessTypes):
        self._AccessTypes = AccessTypes

    @property
    def CustomDomainNames(self):
        return self._CustomDomainNames

    @CustomDomainNames.setter
    def CustomDomainNames(self, CustomDomainNames):
        self._CustomDomainNames = CustomDomainNames


    def _deserialize(self, params):
        self._ServerName = params.get("ServerName")
        self._DefaultDomainName = params.get("DefaultDomainName")
        self._CustomDomainName = params.get("CustomDomainName")
        self._Status = params.get("Status")
        self._UpdateTime = params.get("UpdateTime")
        self._AccessTypes = params.get("AccessTypes")
        self._CustomDomainNames = params.get("CustomDomainNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerManageTaskInfo(AbstractModel):
    """服务管理任务信息

    """

    def __init__(self):
        r"""
        :param _Id: 任务Id
        :type Id: int
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ChangeType: 变更类型
        :type ChangeType: str
        :param _ReleaseType: 发布类型
        :type ReleaseType: str
        :param _DeployType: 部署类型
        :type DeployType: str
        :param _PreVersionName: 上一个版本名
        :type PreVersionName: str
        :param _VersionName: 版本名
        :type VersionName: str
        :param _PipelineId: 流水线Id
        :type PipelineId: int
        :param _PipelineTaskId: 流水线任务Id
        :type PipelineTaskId: int
        :param _ReleaseId: 发布单Id
        :type ReleaseId: int
        :param _Status: 状态
        :type Status: str
        :param _Steps: 步骤信息
        :type Steps: list of TaskStepInfo
        :param _FailReason: 失败原因
        :type FailReason: str
        :param _OperatorRemark: 操作标识
        :type OperatorRemark: str
        """
        self._Id = None
        self._EnvId = None
        self._ServerName = None
        self._CreateTime = None
        self._ChangeType = None
        self._ReleaseType = None
        self._DeployType = None
        self._PreVersionName = None
        self._VersionName = None
        self._PipelineId = None
        self._PipelineTaskId = None
        self._ReleaseId = None
        self._Status = None
        self._Steps = None
        self._FailReason = None
        self._OperatorRemark = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChangeType(self):
        return self._ChangeType

    @ChangeType.setter
    def ChangeType(self, ChangeType):
        self._ChangeType = ChangeType

    @property
    def ReleaseType(self):
        return self._ReleaseType

    @ReleaseType.setter
    def ReleaseType(self, ReleaseType):
        self._ReleaseType = ReleaseType

    @property
    def DeployType(self):
        return self._DeployType

    @DeployType.setter
    def DeployType(self, DeployType):
        self._DeployType = DeployType

    @property
    def PreVersionName(self):
        return self._PreVersionName

    @PreVersionName.setter
    def PreVersionName(self, PreVersionName):
        self._PreVersionName = PreVersionName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def PipelineId(self):
        return self._PipelineId

    @PipelineId.setter
    def PipelineId(self, PipelineId):
        self._PipelineId = PipelineId

    @property
    def PipelineTaskId(self):
        return self._PipelineTaskId

    @PipelineTaskId.setter
    def PipelineTaskId(self, PipelineTaskId):
        self._PipelineTaskId = PipelineTaskId

    @property
    def ReleaseId(self):
        return self._ReleaseId

    @ReleaseId.setter
    def ReleaseId(self, ReleaseId):
        self._ReleaseId = ReleaseId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Steps(self):
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps

    @property
    def FailReason(self):
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def OperatorRemark(self):
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._CreateTime = params.get("CreateTime")
        self._ChangeType = params.get("ChangeType")
        self._ReleaseType = params.get("ReleaseType")
        self._DeployType = params.get("DeployType")
        self._PreVersionName = params.get("PreVersionName")
        self._VersionName = params.get("VersionName")
        self._PipelineId = params.get("PipelineId")
        self._PipelineTaskId = params.get("PipelineTaskId")
        self._ReleaseId = params.get("ReleaseId")
        self._Status = params.get("Status")
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = TaskStepInfo()
                obj._deserialize(item)
                self._Steps.append(obj)
        self._FailReason = params.get("FailReason")
        self._OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaticStorageInfo(AbstractModel):
    """静态CDN资源信息

    """

    def __init__(self):
        r"""
        :param _StaticDomain: 静态CDN域名
        :type StaticDomain: str
        :param _DefaultDirName: 静态CDN默认文件夹，当前为根目录
        :type DefaultDirName: str
        :param _Status: 资源状态(process/online/offline/init)
        :type Status: str
        :param _Region: cos所属区域
        :type Region: str
        :param _Bucket: bucket信息
        :type Bucket: str
        """
        self._StaticDomain = None
        self._DefaultDirName = None
        self._Status = None
        self._Region = None
        self._Bucket = None

    @property
    def StaticDomain(self):
        return self._StaticDomain

    @StaticDomain.setter
    def StaticDomain(self, StaticDomain):
        self._StaticDomain = StaticDomain

    @property
    def DefaultDirName(self):
        return self._DefaultDirName

    @DefaultDirName.setter
    def DefaultDirName(self, DefaultDirName):
        self._DefaultDirName = DefaultDirName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._StaticDomain = params.get("StaticDomain")
        self._DefaultDirName = params.get("DefaultDirName")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageInfo(AbstractModel):
    """StorageInfo 资源信息

    """

    def __init__(self):
        r"""
        :param _Region: 资源所属地域。
当前支持ap-shanghai
        :type Region: str
        :param _Bucket: 桶名，存储资源的唯一标识
        :type Bucket: str
        :param _CdnDomain: cdn 域名
        :type CdnDomain: str
        :param _AppId: 资源所属用户的腾讯云appId
        :type AppId: str
        """
        self._Region = None
        self._Bucket = None
        self._CdnDomain = None
        self._AppId = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def CdnDomain(self):
        return self._CdnDomain

    @CdnDomain.setter
    def CdnDomain(self, CdnDomain):
        self._CdnDomain = CdnDomain

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._CdnDomain = params.get("CdnDomain")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class TaskStepInfo(AbstractModel):
    """任务步骤信息

    """

    def __init__(self):
        r"""
        :param _Name: 步骤名
        :type Name: str
        :param _Status: 未启动："todo"
运行中："running"
失败："failed"
成功结束："finished"
        :type Status: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _CostTime: 消耗时间：秒
        :type CostTime: int
        :param _FailReason: 失败原因
        :type FailReason: str
        """
        self._Name = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._CostTime = None
        self._FailReason = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CostTime(self):
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def FailReason(self):
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CostTime = params.get("CostTime")
        self._FailReason = params.get("FailReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudRunServerRequest(AbstractModel):
    """UpdateCloudRunServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _DeployInfo: 部署信息
        :type DeployInfo: :class:`tencentcloud.tcbr.v20220217.models.DeployParam`
        :param _ServerConfig: 服务配置信息
        :type ServerConfig: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        """
        self._EnvId = None
        self._ServerName = None
        self._DeployInfo = None
        self._ServerConfig = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def DeployInfo(self):
        return self._DeployInfo

    @DeployInfo.setter
    def DeployInfo(self, DeployInfo):
        self._DeployInfo = DeployInfo

    @property
    def ServerConfig(self):
        return self._ServerConfig

    @ServerConfig.setter
    def ServerConfig(self, ServerConfig):
        self._ServerConfig = ServerConfig


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        if params.get("DeployInfo") is not None:
            self._DeployInfo = DeployParam()
            self._DeployInfo._deserialize(params.get("DeployInfo"))
        if params.get("ServerConfig") is not None:
            self._ServerConfig = ServerBaseConfig()
            self._ServerConfig._deserialize(params.get("ServerConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudRunServerResponse(AbstractModel):
    """UpdateCloudRunServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _TaskId: 一键部署任务Id，暂时用不到
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class VersionFlowInfo(AbstractModel):
    """版本流量信息

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名
        :type VersionName: str
        :param _IsDefaultPriority: 是否默认版本
        :type IsDefaultPriority: bool
        :param _FlowRatio: 流量比例
        :type FlowRatio: int
        :param _UrlParam: 测试KV值
        :type UrlParam: :class:`tencentcloud.tcbr.v20220217.models.ObjectKV`
        :param _Priority: 权重
        :type Priority: int
        """
        self._VersionName = None
        self._IsDefaultPriority = None
        self._FlowRatio = None
        self._UrlParam = None
        self._Priority = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def IsDefaultPriority(self):
        return self._IsDefaultPriority

    @IsDefaultPriority.setter
    def IsDefaultPriority(self, IsDefaultPriority):
        self._IsDefaultPriority = IsDefaultPriority

    @property
    def FlowRatio(self):
        return self._FlowRatio

    @FlowRatio.setter
    def FlowRatio(self, FlowRatio):
        self._FlowRatio = FlowRatio

    @property
    def UrlParam(self):
        return self._UrlParam

    @UrlParam.setter
    def UrlParam(self, UrlParam):
        self._UrlParam = UrlParam

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._IsDefaultPriority = params.get("IsDefaultPriority")
        self._FlowRatio = params.get("FlowRatio")
        if params.get("UrlParam") is not None:
            self._UrlParam = ObjectKV()
            self._UrlParam._deserialize(params.get("UrlParam"))
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        