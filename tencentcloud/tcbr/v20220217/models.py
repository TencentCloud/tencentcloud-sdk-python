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


class BuildPacksInfo(AbstractModel):
    r"""BuildPacks信息

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
        :param _LanguageVersion: 语言版本
        :type LanguageVersion: str
        """
        self._BaseImage = None
        self._EntryPoint = None
        self._RepoLanguage = None
        self._UploadFilename = None
        self._LanguageVersion = None

    @property
    def BaseImage(self):
        r"""基础镜像
        :rtype: str
        """
        return self._BaseImage

    @BaseImage.setter
    def BaseImage(self, BaseImage):
        self._BaseImage = BaseImage

    @property
    def EntryPoint(self):
        r"""启动命令
        :rtype: str
        """
        return self._EntryPoint

    @EntryPoint.setter
    def EntryPoint(self, EntryPoint):
        self._EntryPoint = EntryPoint

    @property
    def RepoLanguage(self):
        r"""语言
        :rtype: str
        """
        return self._RepoLanguage

    @RepoLanguage.setter
    def RepoLanguage(self, RepoLanguage):
        self._RepoLanguage = RepoLanguage

    @property
    def UploadFilename(self):
        r"""上传文件名
        :rtype: str
        """
        return self._UploadFilename

    @UploadFilename.setter
    def UploadFilename(self, UploadFilename):
        self._UploadFilename = UploadFilename

    @property
    def LanguageVersion(self):
        r"""语言版本
        :rtype: str
        """
        return self._LanguageVersion

    @LanguageVersion.setter
    def LanguageVersion(self, LanguageVersion):
        self._LanguageVersion = LanguageVersion


    def _deserialize(self, params):
        self._BaseImage = params.get("BaseImage")
        self._EntryPoint = params.get("EntryPoint")
        self._RepoLanguage = params.get("RepoLanguage")
        self._UploadFilename = params.get("UploadFilename")
        self._LanguageVersion = params.get("LanguageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsInfo(AbstractModel):
    r"""cls日志信息

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
        r"""cls所属地域
        :rtype: str
        """
        return self._ClsRegion

    @ClsRegion.setter
    def ClsRegion(self, ClsRegion):
        self._ClsRegion = ClsRegion

    @property
    def ClsLogsetId(self):
        r"""cls日志集ID
        :rtype: str
        """
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsTopicId(self):
        r"""cls日志主题ID
        :rtype: str
        """
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
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
    r"""CreateCloudRunEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageType: <p>Trial,Standard,Professional,Enterprise</p>
        :type PackageType: str
        :param _Alias: <p>环境别名，要以a-z开头，不能包含 a-z,0-9,- 以外的字符</p>
        :type Alias: str
        :param _FreeQuota: <p>用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。</p>
        :type FreeQuota: str
        :param _Flag: <p>订单标记。建议使用方统一转大小写之后再判断。QuickStart：快速启动来源Activity：活动来源</p>
        :type Flag: str
        :param _VpcId: <p>私有网络Id</p>
        :type VpcId: str
        :param _SubNetIds: <p>子网列表</p>
        :type SubNetIds: list of str
        :param _ReqKey: <p>请求key 用于防重</p>
        :type ReqKey: str
        :param _Source: <p>来源：wechat | cloud | weda</p>
        :type Source: str
        :param _Channel: <p>渠道：wechat | cloud | weda</p>
        :type Channel: str
        :param _EnvId: <p>环境ID 云开发平台必填</p>
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
        r"""<p>Trial,Standard,Professional,Enterprise</p>
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Alias(self):
        r"""<p>环境别名，要以a-z开头，不能包含 a-z,0-9,- 以外的字符</p>
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def FreeQuota(self):
        r"""<p>用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。</p>
        :rtype: str
        """
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def Flag(self):
        r"""<p>订单标记。建议使用方统一转大小写之后再判断。QuickStart：快速启动来源Activity：活动来源</p>
        :rtype: str
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def VpcId(self):
        r"""<p>私有网络Id</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubNetIds(self):
        r"""<p>子网列表</p>
        :rtype: list of str
        """
        return self._SubNetIds

    @SubNetIds.setter
    def SubNetIds(self, SubNetIds):
        self._SubNetIds = SubNetIds

    @property
    def ReqKey(self):
        r"""<p>请求key 用于防重</p>
        :rtype: str
        """
        return self._ReqKey

    @ReqKey.setter
    def ReqKey(self, ReqKey):
        self._ReqKey = ReqKey

    @property
    def Source(self):
        r"""<p>来源：wechat | cloud | weda</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Channel(self):
        r"""<p>渠道：wechat | cloud | weda</p>
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def EnvId(self):
        r"""<p>环境ID 云开发平台必填</p>
        :rtype: str
        """
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
    r"""CreateCloudRunEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: <p>环境Id</p>
        :type EnvId: str
        :param _TranId: <p>后付费订单号</p>
        :type TranId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvId = None
        self._TranId = None
        self._RequestId = None

    @property
    def EnvId(self):
        r"""<p>环境Id</p>
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def TranId(self):
        r"""<p>后付费订单号</p>
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

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
        self._EnvId = params.get("EnvId")
        self._TranId = params.get("TranId")
        self._RequestId = params.get("RequestId")


class CreateCloudRunServerRequest(AbstractModel):
    r"""CreateCloudRunServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: <p>环境Id</p>
        :type EnvId: str
        :param _ServerName: <p>服务名</p>
        :type ServerName: str
        :param _DeployInfo: <p>部署信息</p>
        :type DeployInfo: :class:`tencentcloud.tcbr.v20220217.models.DeployParam`
        :param _ServerConfig: <p>服务配置信息(已废弃)</p>
        :type ServerConfig: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        :param _Items: <p>服务配置信息</p>
        :type Items: list of DiffConfigItem
        :param _VpcInfo: <p>vpc 信息</p>
        :type VpcInfo: :class:`tencentcloud.tcbr.v20220217.models.CreateVpcInfo`
        """
        self._EnvId = None
        self._ServerName = None
        self._DeployInfo = None
        self._ServerConfig = None
        self._Items = None
        self._VpcInfo = None

    @property
    def EnvId(self):
        r"""<p>环境Id</p>
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""<p>服务名</p>
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def DeployInfo(self):
        r"""<p>部署信息</p>
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DeployParam`
        """
        return self._DeployInfo

    @DeployInfo.setter
    def DeployInfo(self, DeployInfo):
        self._DeployInfo = DeployInfo

    @property
    def ServerConfig(self):
        r"""<p>服务配置信息(已废弃)</p>
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        """
        return self._ServerConfig

    @ServerConfig.setter
    def ServerConfig(self, ServerConfig):
        self._ServerConfig = ServerConfig

    @property
    def Items(self):
        r"""<p>服务配置信息</p>
        :rtype: list of DiffConfigItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def VpcInfo(self):
        r"""<p>vpc 信息</p>
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.CreateVpcInfo`
        """
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        if params.get("DeployInfo") is not None:
            self._DeployInfo = DeployParam()
            self._DeployInfo._deserialize(params.get("DeployInfo"))
        if params.get("ServerConfig") is not None:
            self._ServerConfig = ServerBaseConfig()
            self._ServerConfig._deserialize(params.get("ServerConfig"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DiffConfigItem()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("VpcInfo") is not None:
            self._VpcInfo = CreateVpcInfo()
            self._VpcInfo._deserialize(params.get("VpcInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRunServerResponse(AbstractModel):
    r"""CreateCloudRunServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>一键部署任务Id，微信云托管，暂时用不到</p>
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>一键部署任务Id，微信云托管，暂时用不到</p>
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateVpcInfo(AbstractModel):
    r"""创建 vpc 信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id
        :type VpcId: str
        :param _CreateType: 1 新建 2 指定
        :type CreateType: int
        :param _SubnetIds: 子网ID列表
        :type SubnetIds: list of str
        """
        self._VpcId = None
        self._CreateType = None
        self._SubnetIds = None

    @property
    def VpcId(self):
        r"""vpc id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def CreateType(self):
        r"""1 新建 2 指定
        :rtype: int
        """
        return self._CreateType

    @CreateType.setter
    def CreateType(self, CreateType):
        self._CreateType = CreateType

    @property
    def SubnetIds(self):
        r"""子网ID列表
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._CreateType = params.get("CreateType")
        self._SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasesInfo(AbstractModel):
    r"""数据库资源信息

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
        r"""数据库唯一标识
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        r"""状态。包含以下取值：
<li>INITIALIZING：资源初始化中</li>
<li>RUNNING：运行中，可正常使用的状态</li>
<li>UNUSABLE：禁用，不可用</li>
<li>OVERDUE：资源过期</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""所属地域。
当前支持ap-shanghai
        :rtype: str
        """
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
        


class DeleteCloudRunServerRequest(AbstractModel):
    r"""DeleteCloudRunServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _OperatorRemark: 操作人信息
        :type OperatorRemark: str
        """
        self._EnvId = None
        self._ServerName = None
        self._OperatorRemark = None

    @property
    def EnvId(self):
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def OperatorRemark(self):
        r"""操作人信息
        :rtype: str
        """
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudRunServerResponse(AbstractModel):
    r"""DeleteCloudRunServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除结果：success / failed
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""删除结果：success / failed
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteCloudRunVersionsRequest(AbstractModel):
    r"""DeleteCloudRunVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境 Id
        :type EnvId: str
        :param _IsDeleteServer: 是否删除服务，只有最后一个版本的时候才生效
        :type IsDeleteServer: bool
        :param _IsDeleteImage: 只有删除服务的时候，才生效
        :type IsDeleteImage: bool
        :param _SimpleVersions: 删除版本的信息
        :type SimpleVersions: list of SimpleVersion
        :param _OperatorRemark: 操作备注
        :type OperatorRemark: str
        """
        self._EnvId = None
        self._IsDeleteServer = None
        self._IsDeleteImage = None
        self._SimpleVersions = None
        self._OperatorRemark = None

    @property
    def EnvId(self):
        r"""环境 Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def IsDeleteServer(self):
        r"""是否删除服务，只有最后一个版本的时候才生效
        :rtype: bool
        """
        return self._IsDeleteServer

    @IsDeleteServer.setter
    def IsDeleteServer(self, IsDeleteServer):
        self._IsDeleteServer = IsDeleteServer

    @property
    def IsDeleteImage(self):
        r"""只有删除服务的时候，才生效
        :rtype: bool
        """
        return self._IsDeleteImage

    @IsDeleteImage.setter
    def IsDeleteImage(self, IsDeleteImage):
        self._IsDeleteImage = IsDeleteImage

    @property
    def SimpleVersions(self):
        r"""删除版本的信息
        :rtype: list of SimpleVersion
        """
        return self._SimpleVersions

    @SimpleVersions.setter
    def SimpleVersions(self, SimpleVersions):
        self._SimpleVersions = SimpleVersions

    @property
    def OperatorRemark(self):
        r"""操作备注
        :rtype: str
        """
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._IsDeleteServer = params.get("IsDeleteServer")
        self._IsDeleteImage = params.get("IsDeleteImage")
        if params.get("SimpleVersions") is not None:
            self._SimpleVersions = []
            for item in params.get("SimpleVersions"):
                obj = SimpleVersion()
                obj._deserialize(item)
                self._SimpleVersions.append(obj)
        self._OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudRunVersionsResponse(AbstractModel):
    r"""DeleteCloudRunVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: succ | fail | partial
        :type Result: str
        :param _FailVersions: 删除失败的版本列表
        :type FailVersions: list of FailDeleteVersions
        :param _SuccessVersions: 删除成功的版本列表
        :type SuccessVersions: list of SuccessDeleteVersions
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._FailVersions = None
        self._SuccessVersions = None
        self._RequestId = None

    @property
    def Result(self):
        r"""succ | fail | partial
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def FailVersions(self):
        r"""删除失败的版本列表
        :rtype: list of FailDeleteVersions
        """
        return self._FailVersions

    @FailVersions.setter
    def FailVersions(self, FailVersions):
        self._FailVersions = FailVersions

    @property
    def SuccessVersions(self):
        r"""删除成功的版本列表
        :rtype: list of SuccessDeleteVersions
        """
        return self._SuccessVersions

    @SuccessVersions.setter
    def SuccessVersions(self, SuccessVersions):
        self._SuccessVersions = SuccessVersions

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
        self._Result = params.get("Result")
        if params.get("FailVersions") is not None:
            self._FailVersions = []
            for item in params.get("FailVersions"):
                obj = FailDeleteVersions()
                obj._deserialize(item)
                self._FailVersions.append(obj)
        if params.get("SuccessVersions") is not None:
            self._SuccessVersions = []
            for item in params.get("SuccessVersions"):
                obj = SuccessDeleteVersions()
                obj._deserialize(item)
                self._SuccessVersions.append(obj)
        self._RequestId = params.get("RequestId")


class DeployParam(AbstractModel):
    r"""部署参数

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
        r"""部署类型：package/image/repository/pipeline/jar/war
        :rtype: str
        """
        return self._DeployType

    @DeployType.setter
    def DeployType(self, DeployType):
        self._DeployType = DeployType

    @property
    def ImageUrl(self):
        r"""部署类型为image时传入
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def PackageName(self):
        r"""部署类型为package时传入
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        r"""部署类型为package时传入
        :rtype: str
        """
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def DeployRemark(self):
        r"""部署备注
        :rtype: str
        """
        return self._DeployRemark

    @DeployRemark.setter
    def DeployRemark(self, DeployRemark):
        self._DeployRemark = DeployRemark

    @property
    def RepoInfo(self):
        r"""代码仓库信息
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.RepositoryInfo`
        """
        return self._RepoInfo

    @RepoInfo.setter
    def RepoInfo(self, RepoInfo):
        self._RepoInfo = RepoInfo

    @property
    def BuildPacks(self):
        r"""无Dockerfile时填写
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.BuildPacksInfo`
        """
        return self._BuildPacks

    @BuildPacks.setter
    def BuildPacks(self, BuildPacks):
        self._BuildPacks = BuildPacks

    @property
    def ReleaseType(self):
        r"""发布类型 GRAY | FULL
        :rtype: str
        """
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
        


class DeployRecord(AbstractModel):
    r"""云托管实例的部署记录, 包括扩缩容状态和流量分配情况

    """

    def __init__(self):
        r"""
        :param _DeployId: 部署Id
        :type DeployId: str
        :param _DeployTime: 部署开始时间
        :type DeployTime: str
        :param _Status: 状态：running/deploying/deploy_failed
        :type Status: str
        :param _RunId: 部署运行Id 用户查询部署日志
        :type RunId: str
        :param _BuildId: 构建Id
        :type BuildId: int
        :param _FlowRatio: 流量比例
        :type FlowRatio: int
        :param _ImageUrl: 镜像url
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param _ScaleStatus: 缩容状态 缩容为 zero 否则为空
        :type ScaleStatus: str
        :param _HasTraffic: 是否分配流量
        :type HasTraffic: bool
        :param _TrafficType: 流量分配方式, FLOW: 百分比分配; URL_PARAMS: 匹配 query 参数; HEADERS: 匹配请求 Header
        :type TrafficType: str
        :param _IsReleasing: 当前版本是否在发布中
        :type IsReleasing: bool
        """
        self._DeployId = None
        self._DeployTime = None
        self._Status = None
        self._RunId = None
        self._BuildId = None
        self._FlowRatio = None
        self._ImageUrl = None
        self._ScaleStatus = None
        self._HasTraffic = None
        self._TrafficType = None
        self._IsReleasing = None

    @property
    def DeployId(self):
        r"""部署Id
        :rtype: str
        """
        return self._DeployId

    @DeployId.setter
    def DeployId(self, DeployId):
        self._DeployId = DeployId

    @property
    def DeployTime(self):
        r"""部署开始时间
        :rtype: str
        """
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime

    @property
    def Status(self):
        r"""状态：running/deploying/deploy_failed
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RunId(self):
        r"""部署运行Id 用户查询部署日志
        :rtype: str
        """
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def BuildId(self):
        r"""构建Id
        :rtype: int
        """
        return self._BuildId

    @BuildId.setter
    def BuildId(self, BuildId):
        self._BuildId = BuildId

    @property
    def FlowRatio(self):
        r"""流量比例
        :rtype: int
        """
        return self._FlowRatio

    @FlowRatio.setter
    def FlowRatio(self, FlowRatio):
        self._FlowRatio = FlowRatio

    @property
    def ImageUrl(self):
        r"""镜像url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ScaleStatus(self):
        r"""缩容状态 缩容为 zero 否则为空
        :rtype: str
        """
        return self._ScaleStatus

    @ScaleStatus.setter
    def ScaleStatus(self, ScaleStatus):
        self._ScaleStatus = ScaleStatus

    @property
    def HasTraffic(self):
        r"""是否分配流量
        :rtype: bool
        """
        return self._HasTraffic

    @HasTraffic.setter
    def HasTraffic(self, HasTraffic):
        self._HasTraffic = HasTraffic

    @property
    def TrafficType(self):
        r"""流量分配方式, FLOW: 百分比分配; URL_PARAMS: 匹配 query 参数; HEADERS: 匹配请求 Header
        :rtype: str
        """
        return self._TrafficType

    @TrafficType.setter
    def TrafficType(self, TrafficType):
        self._TrafficType = TrafficType

    @property
    def IsReleasing(self):
        r"""当前版本是否在发布中
        :rtype: bool
        """
        return self._IsReleasing

    @IsReleasing.setter
    def IsReleasing(self, IsReleasing):
        self._IsReleasing = IsReleasing


    def _deserialize(self, params):
        self._DeployId = params.get("DeployId")
        self._DeployTime = params.get("DeployTime")
        self._Status = params.get("Status")
        self._RunId = params.get("RunId")
        self._BuildId = params.get("BuildId")
        self._FlowRatio = params.get("FlowRatio")
        self._ImageUrl = params.get("ImageUrl")
        self._ScaleStatus = params.get("ScaleStatus")
        self._HasTraffic = params.get("HasTraffic")
        self._TrafficType = params.get("TrafficType")
        self._IsReleasing = params.get("IsReleasing")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunDeployRecordRequest(AbstractModel):
    r"""DescribeCloudRunDeployRecord请求参数结构体

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
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
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
        


class DescribeCloudRunDeployRecordResponse(AbstractModel):
    r"""DescribeCloudRunDeployRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecords: 部署列表
        :type DeployRecords: list of DeployRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployRecords = None
        self._RequestId = None

    @property
    def DeployRecords(self):
        r"""部署列表
        :rtype: list of DeployRecord
        """
        return self._DeployRecords

    @DeployRecords.setter
    def DeployRecords(self, DeployRecords):
        self._DeployRecords = DeployRecords

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
        if params.get("DeployRecords") is not None:
            self._DeployRecords = []
            for item in params.get("DeployRecords"):
                obj = DeployRecord()
                obj._deserialize(item)
                self._DeployRecords.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudRunEnvsRequest(AbstractModel):
    r"""DescribeCloudRunEnvs请求参数结构体

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
        r"""环境ID，如果传了这个参数则只返回该环境的相关信息
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def IsVisible(self):
        r"""指定Channels字段为可见渠道列表或不可见渠道列表
如只想获取渠道A的环境 就填写IsVisible= true,Channels = ["A"], 过滤渠道A拉取其他渠道环境时填写IsVisible= false,Channels = ["A"]
        :rtype: bool
        """
        return self._IsVisible

    @IsVisible.setter
    def IsVisible(self, IsVisible):
        self._IsVisible = IsVisible

    @property
    def Channels(self):
        r"""渠道列表，代表可见或不可见渠道由IsVisible参数指定
        :rtype: list of str
        """
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
    r"""DescribeCloudRunEnvs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvList: 环境信息列表
        :type EnvList: list of EnvInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvList = None
        self._RequestId = None

    @property
    def EnvList(self):
        r"""环境信息列表
        :rtype: list of EnvInfo
        """
        return self._EnvList

    @EnvList.setter
    def EnvList(self, EnvList):
        self._EnvList = EnvList

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
        if params.get("EnvList") is not None:
            self._EnvList = []
            for item in params.get("EnvList"):
                obj = EnvInfo()
                obj._deserialize(item)
                self._EnvList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudRunPodListRequest(AbstractModel):
    r"""DescribeCloudRunPodList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _VersionName: 版本名
        :type VersionName: str
        :param _PageSize: 默认为10， 最大为50
不传或传0时 取默认10
大于50时取50
        :type PageSize: int
        :param _PageNum: 不传或传0时 会默认为1
        :type PageNum: int
        """
        self._EnvId = None
        self._ServerName = None
        self._VersionName = None
        self._PageSize = None
        self._PageNum = None

    @property
    def EnvId(self):
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        r"""版本名
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def PageSize(self):
        r"""默认为10， 最大为50
不传或传0时 取默认10
大于50时取50
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        r"""不传或传0时 会默认为1
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunPodListResponse(AbstractModel):
    r"""DescribeCloudRunPodList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PodList: pod实例列表
        :type PodList: list of VersionPodInstance
        :param _TotalCount: pod总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PodList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PodList(self):
        r"""pod实例列表
        :rtype: list of VersionPodInstance
        """
        return self._PodList

    @PodList.setter
    def PodList(self, PodList):
        self._PodList = PodList

    @property
    def TotalCount(self):
        r"""pod总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("PodList") is not None:
            self._PodList = []
            for item in params.get("PodList"):
                obj = VersionPodInstance()
                obj._deserialize(item)
                self._PodList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCloudRunProcessLogRequest(AbstractModel):
    r"""DescribeCloudRunProcessLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境 Id
        :type EnvId: str
        :param _RunId: 操作 Id
        :type RunId: str
        """
        self._EnvId = None
        self._RunId = None

    @property
    def EnvId(self):
        r"""环境 Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def RunId(self):
        r"""操作 Id
        :rtype: str
        """
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._RunId = params.get("RunId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunProcessLogResponse(AbstractModel):
    r"""DescribeCloudRunProcessLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Logs: 运行日志列表
        :type Logs: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Logs = None
        self._RequestId = None

    @property
    def Logs(self):
        r"""运行日志列表
        :rtype: list of str
        """
        return self._Logs

    @Logs.setter
    def Logs(self, Logs):
        self._Logs = Logs

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
        self._Logs = params.get("Logs")
        self._RequestId = params.get("RequestId")


class DescribeCloudRunServerDetailRequest(AbstractModel):
    r"""DescribeCloudRunServerDetail请求参数结构体

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
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
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
    r"""DescribeCloudRunServerDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BaseInfo: 服务基本信息
        :type BaseInfo: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseInfo`
        :param _ServerConfig: 服务配置信息
        :type ServerConfig: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        :param _OnlineVersionInfos: 在线版本信息
        :type OnlineVersionInfos: list of OnlineVersionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BaseInfo = None
        self._ServerConfig = None
        self._OnlineVersionInfos = None
        self._RequestId = None

    @property
    def BaseInfo(self):
        r"""服务基本信息
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseInfo`
        """
        return self._BaseInfo

    @BaseInfo.setter
    def BaseInfo(self, BaseInfo):
        self._BaseInfo = BaseInfo

    @property
    def ServerConfig(self):
        r"""服务配置信息
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        """
        return self._ServerConfig

    @ServerConfig.setter
    def ServerConfig(self, ServerConfig):
        self._ServerConfig = ServerConfig

    @property
    def OnlineVersionInfos(self):
        r"""在线版本信息
        :rtype: list of OnlineVersionInfo
        """
        return self._OnlineVersionInfos

    @OnlineVersionInfos.setter
    def OnlineVersionInfos(self, OnlineVersionInfos):
        self._OnlineVersionInfos = OnlineVersionInfos

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
    r"""DescribeCloudRunServers请求参数结构体

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
        :param _ServerName: 服务名
        :type ServerName: str
        :param _ServerType: 服务类型：function | container
        :type ServerType: str
        :param _VpcId: vpcId
        :type VpcId: str
        """
        self._EnvId = None
        self._PageSize = None
        self._PageNum = None
        self._ServerName = None
        self._ServerType = None
        self._VpcId = None

    @property
    def EnvId(self):
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def PageSize(self):
        r"""默认为9， 最大为30
不传或传0时 取默认9
大于30时取30
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        r"""不传或传0时 会默认为1
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def ServerType(self):
        r"""服务类型：function | container
        :rtype: str
        """
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def VpcId(self):
        r"""vpcId
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._ServerName = params.get("ServerName")
        self._ServerType = params.get("ServerType")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunServersResponse(AbstractModel):
    r"""DescribeCloudRunServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServerList: 服务列表
        :type ServerList: list of ServerBaseInfo
        :param _Total: 服务总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServerList = None
        self._Total = None
        self._RequestId = None

    @property
    def ServerList(self):
        r"""服务列表
        :rtype: list of ServerBaseInfo
        """
        return self._ServerList

    @ServerList.setter
    def ServerList(self, ServerList):
        self._ServerList = ServerList

    @property
    def Total(self):
        r"""服务总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("ServerList") is not None:
            self._ServerList = []
            for item in params.get("ServerList"):
                obj = ServerBaseInfo()
                obj._deserialize(item)
                self._ServerList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeEnvBaseInfoRequest(AbstractModel):
    r"""DescribeEnvBaseInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: <p>环境 Id</p>
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        r"""<p>环境 Id</p>
        :rtype: str
        """
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
    r"""DescribeEnvBaseInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvBaseInfo: <p>环境基础信息</p>
        :type EnvBaseInfo: :class:`tencentcloud.tcbr.v20220217.models.EnvBaseInfo`
        :param _IsExist: <p>是否存在</p>
        :type IsExist: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvBaseInfo = None
        self._IsExist = None
        self._RequestId = None

    @property
    def EnvBaseInfo(self):
        r"""<p>环境基础信息</p>
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.EnvBaseInfo`
        """
        return self._EnvBaseInfo

    @EnvBaseInfo.setter
    def EnvBaseInfo(self, EnvBaseInfo):
        self._EnvBaseInfo = EnvBaseInfo

    @property
    def IsExist(self):
        r"""<p>是否存在</p>
        :rtype: bool
        """
        return self._IsExist

    @IsExist.setter
    def IsExist(self, IsExist):
        self._IsExist = IsExist

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
        if params.get("EnvBaseInfo") is not None:
            self._EnvBaseInfo = EnvBaseInfo()
            self._EnvBaseInfo._deserialize(params.get("EnvBaseInfo"))
        self._IsExist = params.get("IsExist")
        self._RequestId = params.get("RequestId")


class DescribeReleaseOrderRequest(AbstractModel):
    r"""DescribeReleaseOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境 Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _Status: 发布单状态
        :type Status: str
        """
        self._EnvId = None
        self._ServerName = None
        self._Status = None

    @property
    def EnvId(self):
        r"""环境 Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def Status(self):
        r"""发布单状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseOrderResponse(AbstractModel):
    r"""DescribeReleaseOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsExist: 是否存在
        :type IsExist: bool
        :param _ReleaseOrderInfo: 发布单信息
        :type ReleaseOrderInfo: :class:`tencentcloud.tcbr.v20220217.models.ReleaseOrderInfo`
        :param _LastReleasedSuccessTime: 上一次成功发布时间
        :type LastReleasedSuccessTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsExist = None
        self._ReleaseOrderInfo = None
        self._LastReleasedSuccessTime = None
        self._RequestId = None

    @property
    def IsExist(self):
        r"""是否存在
        :rtype: bool
        """
        return self._IsExist

    @IsExist.setter
    def IsExist(self, IsExist):
        self._IsExist = IsExist

    @property
    def ReleaseOrderInfo(self):
        r"""发布单信息
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.ReleaseOrderInfo`
        """
        return self._ReleaseOrderInfo

    @ReleaseOrderInfo.setter
    def ReleaseOrderInfo(self, ReleaseOrderInfo):
        self._ReleaseOrderInfo = ReleaseOrderInfo

    @property
    def LastReleasedSuccessTime(self):
        r"""上一次成功发布时间
        :rtype: str
        """
        return self._LastReleasedSuccessTime

    @LastReleasedSuccessTime.setter
    def LastReleasedSuccessTime(self, LastReleasedSuccessTime):
        self._LastReleasedSuccessTime = LastReleasedSuccessTime

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
        self._IsExist = params.get("IsExist")
        if params.get("ReleaseOrderInfo") is not None:
            self._ReleaseOrderInfo = ReleaseOrderInfo()
            self._ReleaseOrderInfo._deserialize(params.get("ReleaseOrderInfo"))
        self._LastReleasedSuccessTime = params.get("LastReleasedSuccessTime")
        self._RequestId = params.get("RequestId")


class DescribeServerManageTaskRequest(AbstractModel):
    r"""DescribeServerManageTask请求参数结构体

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
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def OperatorRemark(self):
        r"""操作标识
        :rtype: str
        """
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
    r"""DescribeServerManageTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsExist: 是否存在
        :type IsExist: bool
        :param _Task: 任务信息
        :type Task: :class:`tencentcloud.tcbr.v20220217.models.ServerManageTaskInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsExist = None
        self._Task = None
        self._RequestId = None

    @property
    def IsExist(self):
        r"""是否存在
        :rtype: bool
        """
        return self._IsExist

    @IsExist.setter
    def IsExist(self, IsExist):
        self._IsExist = IsExist

    @property
    def Task(self):
        r"""任务信息
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.ServerManageTaskInfo`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

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
        self._IsExist = params.get("IsExist")
        if params.get("Task") is not None:
            self._Task = ServerManageTaskInfo()
            self._Task._deserialize(params.get("Task"))
        self._RequestId = params.get("RequestId")


class DescribeVersionDetailRequest(AbstractModel):
    r"""DescribeVersionDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: <p>环境Id</p>
        :type EnvId: str
        :param _ServerName: <p>服务名</p>
        :type ServerName: str
        :param _VersionName: <p>版本名</p>
        :type VersionName: str
        :param _Channel: <p>channel</p>
        :type Channel: str
        """
        self._EnvId = None
        self._ServerName = None
        self._VersionName = None
        self._Channel = None

    @property
    def EnvId(self):
        r"""<p>环境Id</p>
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""<p>服务名</p>
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        r"""<p>版本名</p>
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Channel(self):
        r"""<p>channel</p>
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVersionDetailResponse(AbstractModel):
    r"""DescribeVersionDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>版本名</p>
        :type Name: str
        :param _Port: <p>端口号</p>
        :type Port: int
        :param _Cpu: <p>cpu 规格</p>
        :type Cpu: float
        :param _Mem: <p>mem 规格</p>
        :type Mem: float
        :param _MinNum: <p>最小副本数</p>
        :type MinNum: int
        :param _MaxNum: <p>最大副本数</p>
        :type MaxNum: int
        :param _PolicyDetails: <p>扩缩容策略</p>
        :type PolicyDetails: list of HpaPolicy
        :param _Dockerfile: <p>Dockerfile path</p>
        :type Dockerfile: str
        :param _BuildDir: <p>目标目录</p>
        :type BuildDir: str
        :param _EnvParams: <p>环境变量</p>
        :type EnvParams: str
        :param _Status: <p>状态</p>
        :type Status: str
        :param _CreatedTime: <p>创建时间</p>
        :type CreatedTime: str
        :param _UpdatedTime: <p>更新时间</p>
        :type UpdatedTime: str
        :param _LogPath: <p>日志采集路径</p>
        :type LogPath: str
        :param _EntryPoint: <p>entryPoint</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EntryPoint: str
        :param _Cmd: <p>Cmd</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Cmd: str
        :param _VpcConf: <p>vpc conf</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcConf: :class:`tencentcloud.tcbr.v20220217.models.VpcConf`
        :param _VolumesConf: <p>volume conf</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumesConf: list of VolumeConf
        :param _BuildPacks: <p>buildpack 信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildPacks: :class:`tencentcloud.tcbr.v20220217.models.BuildPacksInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Port = None
        self._Cpu = None
        self._Mem = None
        self._MinNum = None
        self._MaxNum = None
        self._PolicyDetails = None
        self._Dockerfile = None
        self._BuildDir = None
        self._EnvParams = None
        self._Status = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._LogPath = None
        self._EntryPoint = None
        self._Cmd = None
        self._VpcConf = None
        self._VolumesConf = None
        self._BuildPacks = None
        self._RequestId = None

    @property
    def Name(self):
        r"""<p>版本名</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Port(self):
        r"""<p>端口号</p>
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Cpu(self):
        r"""<p>cpu 规格</p>
        :rtype: float
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        r"""<p>mem 规格</p>
        :rtype: float
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def MinNum(self):
        r"""<p>最小副本数</p>
        :rtype: int
        """
        return self._MinNum

    @MinNum.setter
    def MinNum(self, MinNum):
        self._MinNum = MinNum

    @property
    def MaxNum(self):
        r"""<p>最大副本数</p>
        :rtype: int
        """
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum

    @property
    def PolicyDetails(self):
        r"""<p>扩缩容策略</p>
        :rtype: list of HpaPolicy
        """
        return self._PolicyDetails

    @PolicyDetails.setter
    def PolicyDetails(self, PolicyDetails):
        self._PolicyDetails = PolicyDetails

    @property
    def Dockerfile(self):
        r"""<p>Dockerfile path</p>
        :rtype: str
        """
        return self._Dockerfile

    @Dockerfile.setter
    def Dockerfile(self, Dockerfile):
        self._Dockerfile = Dockerfile

    @property
    def BuildDir(self):
        r"""<p>目标目录</p>
        :rtype: str
        """
        return self._BuildDir

    @BuildDir.setter
    def BuildDir(self, BuildDir):
        self._BuildDir = BuildDir

    @property
    def EnvParams(self):
        r"""<p>环境变量</p>
        :rtype: str
        """
        return self._EnvParams

    @EnvParams.setter
    def EnvParams(self, EnvParams):
        self._EnvParams = EnvParams

    @property
    def Status(self):
        r"""<p>状态</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""<p>更新时间</p>
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def LogPath(self):
        r"""<p>日志采集路径</p>
        :rtype: str
        """
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath

    @property
    def EntryPoint(self):
        r"""<p>entryPoint</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EntryPoint

    @EntryPoint.setter
    def EntryPoint(self, EntryPoint):
        self._EntryPoint = EntryPoint

    @property
    def Cmd(self):
        r"""<p>Cmd</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def VpcConf(self):
        r"""<p>vpc conf</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.VpcConf`
        """
        return self._VpcConf

    @VpcConf.setter
    def VpcConf(self, VpcConf):
        self._VpcConf = VpcConf

    @property
    def VolumesConf(self):
        r"""<p>volume conf</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VolumeConf
        """
        return self._VolumesConf

    @VolumesConf.setter
    def VolumesConf(self, VolumesConf):
        self._VolumesConf = VolumesConf

    @property
    def BuildPacks(self):
        r"""<p>buildpack 信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.BuildPacksInfo`
        """
        return self._BuildPacks

    @BuildPacks.setter
    def BuildPacks(self, BuildPacks):
        self._BuildPacks = BuildPacks

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
        self._Name = params.get("Name")
        self._Port = params.get("Port")
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
        self._Dockerfile = params.get("Dockerfile")
        self._BuildDir = params.get("BuildDir")
        self._EnvParams = params.get("EnvParams")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._LogPath = params.get("LogPath")
        self._EntryPoint = params.get("EntryPoint")
        self._Cmd = params.get("Cmd")
        if params.get("VpcConf") is not None:
            self._VpcConf = VpcConf()
            self._VpcConf._deserialize(params.get("VpcConf"))
        if params.get("VolumesConf") is not None:
            self._VolumesConf = []
            for item in params.get("VolumesConf"):
                obj = VolumeConf()
                obj._deserialize(item)
                self._VolumesConf.append(obj)
        if params.get("BuildPacks") is not None:
            self._BuildPacks = BuildPacksInfo()
            self._BuildPacks._deserialize(params.get("BuildPacks"))
        self._RequestId = params.get("RequestId")


class DiffConfigItem(AbstractModel):
    r"""服务配置入参

    """

    def __init__(self):
        r"""
        :param _Key: 配置项 Key
MinNum 最小副本数
MaxNum 最大副本数
PolicyDetails 扩缩容策略
AccessTypes 访问类型
TimerScale 定时扩缩容
InternalAccess 内网访问
OperationMode 运行模式 noScale | condScale | alwaysScale | custom ｜ manualScale
SessionAffinity 会话亲和性 open | close
CpuSpecs cpu 规格
MemSpecs mem规格
EnvParam 环境变量
LogPath 日志采集路径
Port 端口
Dockerfile dockerfile 文件名
BuildDir 目标目录
Tag 服务标签
LogType 日志类型 none | default | custom 
LogSetId 日志集Id
LogTopicId 日志主题ID
LogParseType 日志解析类型 json ｜ line
EntryPoint entrypoint 命令
Cmd cmd命令
VpcConf 网络信息
        :type Key: str
        :param _Value: 字符串类型配置项值
InternalAccess、OperationMode、SessionAffinity、EnvParam、LogPath、Dockerfile、BuildDir、Tag、LogType、LogSetId、LogTopicId、LogParseType
        :type Value: str
        :param _IntValue: int 类型配置项值
MinNum、MaxNum、Port
        :type IntValue: int
        :param _BoolValue: bool 类型配置项值
        :type BoolValue: bool
        :param _FloatValue: 浮点型配置项值
CpuSpecs、MemSpecs
        :type FloatValue: float
        :param _ArrayValue: 字符串数组配置项值
AccessTypes，EntryPoint，Cmd
        :type ArrayValue: list of str
        :param _PolicyDetails: 扩缩容策略配置项值
        :type PolicyDetails: list of HpaPolicy
        :param _TimerScale: 定时扩缩容配置项值
        :type TimerScale: list of TimerScale
        :param _VpcConf: 配置内网访问时网络信息
        :type VpcConf: :class:`tencentcloud.tcbr.v20220217.models.VpcConf`
        :param _VolumesConf: 存储配置信息
        :type VolumesConf: list of VolumeConf
        """
        self._Key = None
        self._Value = None
        self._IntValue = None
        self._BoolValue = None
        self._FloatValue = None
        self._ArrayValue = None
        self._PolicyDetails = None
        self._TimerScale = None
        self._VpcConf = None
        self._VolumesConf = None

    @property
    def Key(self):
        r"""配置项 Key
MinNum 最小副本数
MaxNum 最大副本数
PolicyDetails 扩缩容策略
AccessTypes 访问类型
TimerScale 定时扩缩容
InternalAccess 内网访问
OperationMode 运行模式 noScale | condScale | alwaysScale | custom ｜ manualScale
SessionAffinity 会话亲和性 open | close
CpuSpecs cpu 规格
MemSpecs mem规格
EnvParam 环境变量
LogPath 日志采集路径
Port 端口
Dockerfile dockerfile 文件名
BuildDir 目标目录
Tag 服务标签
LogType 日志类型 none | default | custom 
LogSetId 日志集Id
LogTopicId 日志主题ID
LogParseType 日志解析类型 json ｜ line
EntryPoint entrypoint 命令
Cmd cmd命令
VpcConf 网络信息
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""字符串类型配置项值
InternalAccess、OperationMode、SessionAffinity、EnvParam、LogPath、Dockerfile、BuildDir、Tag、LogType、LogSetId、LogTopicId、LogParseType
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def IntValue(self):
        r"""int 类型配置项值
MinNum、MaxNum、Port
        :rtype: int
        """
        return self._IntValue

    @IntValue.setter
    def IntValue(self, IntValue):
        self._IntValue = IntValue

    @property
    def BoolValue(self):
        r"""bool 类型配置项值
        :rtype: bool
        """
        return self._BoolValue

    @BoolValue.setter
    def BoolValue(self, BoolValue):
        self._BoolValue = BoolValue

    @property
    def FloatValue(self):
        r"""浮点型配置项值
CpuSpecs、MemSpecs
        :rtype: float
        """
        return self._FloatValue

    @FloatValue.setter
    def FloatValue(self, FloatValue):
        self._FloatValue = FloatValue

    @property
    def ArrayValue(self):
        r"""字符串数组配置项值
AccessTypes，EntryPoint，Cmd
        :rtype: list of str
        """
        return self._ArrayValue

    @ArrayValue.setter
    def ArrayValue(self, ArrayValue):
        self._ArrayValue = ArrayValue

    @property
    def PolicyDetails(self):
        r"""扩缩容策略配置项值
        :rtype: list of HpaPolicy
        """
        return self._PolicyDetails

    @PolicyDetails.setter
    def PolicyDetails(self, PolicyDetails):
        self._PolicyDetails = PolicyDetails

    @property
    def TimerScale(self):
        r"""定时扩缩容配置项值
        :rtype: list of TimerScale
        """
        return self._TimerScale

    @TimerScale.setter
    def TimerScale(self, TimerScale):
        self._TimerScale = TimerScale

    @property
    def VpcConf(self):
        r"""配置内网访问时网络信息
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.VpcConf`
        """
        return self._VpcConf

    @VpcConf.setter
    def VpcConf(self, VpcConf):
        self._VpcConf = VpcConf

    @property
    def VolumesConf(self):
        r"""存储配置信息
        :rtype: list of VolumeConf
        """
        return self._VolumesConf

    @VolumesConf.setter
    def VolumesConf(self, VolumesConf):
        self._VolumesConf = VolumesConf


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._IntValue = params.get("IntValue")
        self._BoolValue = params.get("BoolValue")
        self._FloatValue = params.get("FloatValue")
        self._ArrayValue = params.get("ArrayValue")
        if params.get("PolicyDetails") is not None:
            self._PolicyDetails = []
            for item in params.get("PolicyDetails"):
                obj = HpaPolicy()
                obj._deserialize(item)
                self._PolicyDetails.append(obj)
        if params.get("TimerScale") is not None:
            self._TimerScale = []
            for item in params.get("TimerScale"):
                obj = TimerScale()
                obj._deserialize(item)
                self._TimerScale.append(obj)
        if params.get("VpcConf") is not None:
            self._VpcConf = VpcConf()
            self._VpcConf._deserialize(params.get("VpcConf"))
        if params.get("VolumesConf") is not None:
            self._VolumesConf = []
            for item in params.get("VolumesConf"):
                obj = VolumeConf()
                obj._deserialize(item)
                self._VolumesConf.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvBaseInfo(AbstractModel):
    r"""环境基础信息

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
        :param _Recycle: 回收标志，为空则表示正常，recycle表示已回收
        :type Recycle: str
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
        self._Recycle = None

    @property
    def EnvId(self):
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def PackageType(self):
        r"""套餐类型：Trial ｜ Standard ｜ Professional ｜ Enterprise
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def VpcId(self):
        r"""VPC Id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def CreateTime(self):
        r"""环境创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Alias(self):
        r"""环境别名
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        r"""环境状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""环境地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def EnvType(self):
        r"""环境类型 tcbr ｜ run
        :rtype: str
        """
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def SubnetIds(self):
        r"""子网id
        :rtype: str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def Recycle(self):
        r"""回收标志，为空则表示正常，recycle表示已回收
        :rtype: str
        """
        return self._Recycle

    @Recycle.setter
    def Recycle(self, Recycle):
        self._Recycle = Recycle


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
        self._Recycle = params.get("Recycle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvInfo(AbstractModel):
    r"""环境信息

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
        :type IsAutoDegrade: bool
        :param _EnvChannel: 环境渠道
        :type EnvChannel: str
        :param _PayMode: 支付方式。包含以下取值：
<li> prepayment：预付费</li>
<li> postpaid：后付费</li>
        :type PayMode: str
        :param _IsDefault: 是否为默认环境
        :type IsDefault: bool
        :param _Region: 环境所属地域
        :type Region: str
        :param _EnvType: 环境类型：baas, run, hosting, weda,tcbr
        :type EnvType: str
        :param _Databases: 数据库列表
        :type Databases: list of DatabasesInfo
        :param _Storages: 存储列表
        :type Storages: list of StorageInfo
        :param _Functions: 函数列表
        :type Functions: list of FunctionInfo
        :param _LogServices: 云日志服务列表
        :type LogServices: list of LogServiceInfo
        :param _StaticStorages: 静态资源信息
        :type StaticStorages: list of StaticStorageInfo
        :param _Tags: 环境标签列表
        :type Tags: list of Tag
        :param _CustomLogServices: 自定义日志服务
        :type CustomLogServices: list of ClsInfo
        :param _PackageId: tcb产品套餐ID，参考DescribePackages接口的返回值。
        :type PackageId: str
        :param _PackageName: 套餐中文名称，参考DescribePackages接口的返回值。
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
        r"""账户下该环境唯一标识
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Source(self):
        r"""环境来源。包含以下取值：
<li>miniapp：微信小程序</li>
<li>qcloud ：腾讯云</li>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Alias(self):
        r"""环境别名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""最后修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        r"""环境状态。包含以下取值：
<li>NORMAL：正常可用</li>
<li>UNAVAILABLE：服务不可用，可能是尚未初始化或者初始化过程中</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsAutoDegrade(self):
        r"""是否到期自动降为免费版
        :rtype: bool
        """
        return self._IsAutoDegrade

    @IsAutoDegrade.setter
    def IsAutoDegrade(self, IsAutoDegrade):
        self._IsAutoDegrade = IsAutoDegrade

    @property
    def EnvChannel(self):
        r"""环境渠道
        :rtype: str
        """
        return self._EnvChannel

    @EnvChannel.setter
    def EnvChannel(self, EnvChannel):
        self._EnvChannel = EnvChannel

    @property
    def PayMode(self):
        r"""支付方式。包含以下取值：
<li> prepayment：预付费</li>
<li> postpaid：后付费</li>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def IsDefault(self):
        r"""是否为默认环境
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def Region(self):
        r"""环境所属地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def EnvType(self):
        r"""环境类型：baas, run, hosting, weda,tcbr
        :rtype: str
        """
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def Databases(self):
        r"""数据库列表
        :rtype: list of DatabasesInfo
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def Storages(self):
        r"""存储列表
        :rtype: list of StorageInfo
        """
        return self._Storages

    @Storages.setter
    def Storages(self, Storages):
        self._Storages = Storages

    @property
    def Functions(self):
        r"""函数列表
        :rtype: list of FunctionInfo
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def LogServices(self):
        r"""云日志服务列表
        :rtype: list of LogServiceInfo
        """
        return self._LogServices

    @LogServices.setter
    def LogServices(self, LogServices):
        self._LogServices = LogServices

    @property
    def StaticStorages(self):
        r"""静态资源信息
        :rtype: list of StaticStorageInfo
        """
        return self._StaticStorages

    @StaticStorages.setter
    def StaticStorages(self, StaticStorages):
        self._StaticStorages = StaticStorages

    @property
    def Tags(self):
        r"""环境标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CustomLogServices(self):
        r"""自定义日志服务
        :rtype: list of ClsInfo
        """
        return self._CustomLogServices

    @CustomLogServices.setter
    def CustomLogServices(self, CustomLogServices):
        self._CustomLogServices = CustomLogServices

    @property
    def PackageId(self):
        r"""tcb产品套餐ID，参考DescribePackages接口的返回值。
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        r"""套餐中文名称，参考DescribePackages接口的返回值。
        :rtype: str
        """
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
        


class FailDeleteVersions(AbstractModel):
    r"""删除失败版本信息

    """

    def __init__(self):
        r"""
        :param _Version: 删除失败版本信息
        :type Version: :class:`tencentcloud.tcbr.v20220217.models.SimpleVersion`
        :param _ErrorCode: 删除失败错误码
        :type ErrorCode: int
        :param _ErrorMsg: 删除失败错误信息
        :type ErrorMsg: str
        :param _RequestId: 删除操作 RequestId
        :type RequestId: str
        """
        self._Version = None
        self._ErrorCode = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def Version(self):
        r"""删除失败版本信息
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.SimpleVersion`
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ErrorCode(self):
        r"""删除失败错误码
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        r"""删除失败错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        r"""删除操作 RequestId
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Version") is not None:
            self._Version = SimpleVersion()
            self._Version._deserialize(params.get("Version"))
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionInfo(AbstractModel):
    r"""函数的信息

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
        r"""命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Region(self):
        r"""所属地域。
当前支持ap-shanghai
        :rtype: str
        """
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
    r"""扩缩容入参

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
        r"""扩缩容类型
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyThreshold(self):
        r"""扩缩容阈值
        :rtype: int
        """
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
        


class LogObject(AbstractModel):
    r"""CLS日志单条信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志属于的 topic ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _TopicName: 日志主题的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _Timestamp: 日志时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _Content: 日志内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _FileName: 采集路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _Source: 日志来源设备
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _PkgLogId: 日志唯一标识
        :type PkgLogId: str
        """
        self._TopicId = None
        self._TopicName = None
        self._Timestamp = None
        self._Content = None
        self._FileName = None
        self._Source = None
        self._PkgLogId = None

    @property
    def TopicId(self):
        r"""日志属于的 topic ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        r"""日志主题的名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Timestamp(self):
        r"""日志时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Content(self):
        r"""日志内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FileName(self):
        r"""采集路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Source(self):
        r"""日志来源设备
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def PkgLogId(self):
        r"""日志唯一标识
        :rtype: str
        """
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Timestamp = params.get("Timestamp")
        self._Content = params.get("Content")
        self._FileName = params.get("FileName")
        self._Source = params.get("Source")
        self._PkgLogId = params.get("PkgLogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogResObject(AbstractModel):
    r"""CLS日志结果

    """

    def __init__(self):
        r"""
        :param _Context: 获取更多检索结果的游标
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _ListOver: 搜索结果是否已经全部返回
注意：此字段可能返回 null，表示取不到有效值。
        :type ListOver: bool
        :param _Results: 日志内容信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of LogObject
        """
        self._Context = None
        self._ListOver = None
        self._Results = None

    @property
    def Context(self):
        r"""获取更多检索结果的游标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        r"""搜索结果是否已经全部返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Results(self):
        r"""日志内容信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LogObject
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = LogObject()
                obj._deserialize(item)
                self._Results.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogServiceInfo(AbstractModel):
    r"""云日志服务相关信息

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
        r"""log名
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def LogsetId(self):
        r"""log-id
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicName(self):
        r"""topic名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        r"""topic-id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Region(self):
        r"""cls日志所属地域
        :rtype: str
        """
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
    r"""通用Key Value

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
        r"""键值对Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""键值对Value
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
        


class ObjectKVPriority(AbstractModel):
    r"""通用键值权重对

    """

    def __init__(self):
        r"""
        :param _Key: 键值对Key
        :type Key: str
        :param _Value: 键值对Value
        :type Value: str
        :param _Priority: 键值对权重
        :type Priority: int
        """
        self._Key = None
        self._Value = None
        self._Priority = None

    @property
    def Key(self):
        r"""键值对Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""键值对Value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Priority(self):
        r"""键值对权重
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OnlineVersionInfo(AbstractModel):
    r"""在线版本信息

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名
        :type VersionName: str
        :param _ImageUrl: 镜像url
        :type ImageUrl: str
        :param _FlowRatio: 流量
        :type FlowRatio: str
        """
        self._VersionName = None
        self._ImageUrl = None
        self._FlowRatio = None

    @property
    def VersionName(self):
        r"""版本名
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def ImageUrl(self):
        r"""镜像url
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def FlowRatio(self):
        r"""流量
        :rtype: str
        """
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
    r"""OperateServerManage请求参数结构体

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
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def TaskId(self):
        r"""任报Id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def OperateType(self):
        r"""操作类型:cancel | go_back | done
        :rtype: str
        """
        return self._OperateType

    @OperateType.setter
    def OperateType(self, OperateType):
        self._OperateType = OperateType

    @property
    def OperatorRemark(self):
        r"""操作标识
        :rtype: str
        """
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
    r"""OperateServerManage返回参数结构体

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


class ReleaseGrayRequest(AbstractModel):
    r"""ReleaseGray请求参数结构体

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
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def GrayType(self):
        r"""灰度类型
        :rtype: str
        """
        return self._GrayType

    @GrayType.setter
    def GrayType(self, GrayType):
        self._GrayType = GrayType

    @property
    def TrafficType(self):
        r"""流量类型
        :rtype: str
        """
        return self._TrafficType

    @TrafficType.setter
    def TrafficType(self, TrafficType):
        self._TrafficType = TrafficType

    @property
    def VersionFlowItems(self):
        r"""流量策略
        :rtype: list of VersionFlowInfo
        """
        return self._VersionFlowItems

    @VersionFlowItems.setter
    def VersionFlowItems(self, VersionFlowItems):
        self._VersionFlowItems = VersionFlowItems

    @property
    def OperatorRemark(self):
        r"""操作标识
        :rtype: str
        """
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark

    @property
    def GrayFlowRatio(self):
        r"""流量比例
        :rtype: int
        """
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
    r"""ReleaseGray返回参数结构体

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


class ReleaseOrderInfo(AbstractModel):
    r"""发布单信息

    """

    def __init__(self):
        r"""
        :param _Id: 发布单Id
        :type Id: int
        :param _ServerName: 服务名
        :type ServerName: str
        :param _CurrentVersion: 当前版本
        :type CurrentVersion: :class:`tencentcloud.tcbr.v20220217.models.VersionInfo`
        :param _ReleaseVersion: 发布版本
        :type ReleaseVersion: :class:`tencentcloud.tcbr.v20220217.models.VersionInfo`
        :param _GrayStatus: 灰度状态
        :type GrayStatus: str
        :param _ReleaseStatus: 发布状态
        :type ReleaseStatus: str
        :param _TrafficTypeValues: 流量值
        :type TrafficTypeValues: list of ObjectKV
        :param _TrafficType: 流量类型
        :type TrafficType: str
        :param _FlowRatio: 百分比
        :type FlowRatio: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _IsReleasing: 是否发布中
        :type IsReleasing: bool
        """
        self._Id = None
        self._ServerName = None
        self._CurrentVersion = None
        self._ReleaseVersion = None
        self._GrayStatus = None
        self._ReleaseStatus = None
        self._TrafficTypeValues = None
        self._TrafficType = None
        self._FlowRatio = None
        self._CreateTime = None
        self._IsReleasing = None

    @property
    def Id(self):
        r"""发布单Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def CurrentVersion(self):
        r"""当前版本
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.VersionInfo`
        """
        return self._CurrentVersion

    @CurrentVersion.setter
    def CurrentVersion(self, CurrentVersion):
        self._CurrentVersion = CurrentVersion

    @property
    def ReleaseVersion(self):
        r"""发布版本
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.VersionInfo`
        """
        return self._ReleaseVersion

    @ReleaseVersion.setter
    def ReleaseVersion(self, ReleaseVersion):
        self._ReleaseVersion = ReleaseVersion

    @property
    def GrayStatus(self):
        r"""灰度状态
        :rtype: str
        """
        return self._GrayStatus

    @GrayStatus.setter
    def GrayStatus(self, GrayStatus):
        self._GrayStatus = GrayStatus

    @property
    def ReleaseStatus(self):
        r"""发布状态
        :rtype: str
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus

    @property
    def TrafficTypeValues(self):
        r"""流量值
        :rtype: list of ObjectKV
        """
        return self._TrafficTypeValues

    @TrafficTypeValues.setter
    def TrafficTypeValues(self, TrafficTypeValues):
        self._TrafficTypeValues = TrafficTypeValues

    @property
    def TrafficType(self):
        r"""流量类型
        :rtype: str
        """
        return self._TrafficType

    @TrafficType.setter
    def TrafficType(self, TrafficType):
        self._TrafficType = TrafficType

    @property
    def FlowRatio(self):
        r"""百分比
        :rtype: int
        """
        return self._FlowRatio

    @FlowRatio.setter
    def FlowRatio(self, FlowRatio):
        self._FlowRatio = FlowRatio

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsReleasing(self):
        r"""是否发布中
        :rtype: bool
        """
        return self._IsReleasing

    @IsReleasing.setter
    def IsReleasing(self, IsReleasing):
        self._IsReleasing = IsReleasing


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ServerName = params.get("ServerName")
        if params.get("CurrentVersion") is not None:
            self._CurrentVersion = VersionInfo()
            self._CurrentVersion._deserialize(params.get("CurrentVersion"))
        if params.get("ReleaseVersion") is not None:
            self._ReleaseVersion = VersionInfo()
            self._ReleaseVersion._deserialize(params.get("ReleaseVersion"))
        self._GrayStatus = params.get("GrayStatus")
        self._ReleaseStatus = params.get("ReleaseStatus")
        if params.get("TrafficTypeValues") is not None:
            self._TrafficTypeValues = []
            for item in params.get("TrafficTypeValues"):
                obj = ObjectKV()
                obj._deserialize(item)
                self._TrafficTypeValues.append(obj)
        self._TrafficType = params.get("TrafficType")
        self._FlowRatio = params.get("FlowRatio")
        self._CreateTime = params.get("CreateTime")
        self._IsReleasing = params.get("IsReleasing")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepositoryInfo(AbstractModel):
    r"""代码仓库信息

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
        r"""git source
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Repo(self):
        r"""仓库名
        :rtype: str
        """
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def Branch(self):
        r"""分支名
        :rtype: str
        """
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
        


class SearchClsLogRequest(AbstractModel):
    r"""SearchClsLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _QueryString: 查询语句，详情参考 https://cloud.tencent.com/document/product/614/47044
        :type QueryString: str
        :param _Limit: 单次要返回的日志条数，单次返回的最大条数为100
        :type Limit: int
        :param _Context: 加载更多使用，透传上次返回的 context 值，获取后续的日志内容，通过游标最多可获取10000条，请尽可能缩小时间范围
        :type Context: str
        :param _Sort: 按时间排序 asc（升序）或者 desc（降序），默认为 desc
        :type Sort: str
        :param _UseLucene: 是否使用Lucene语法，默认为false
        :type UseLucene: bool
        :param _LogType: 日志类型
        :type LogType: int
        """
        self._EnvId = None
        self._StartTime = None
        self._EndTime = None
        self._QueryString = None
        self._Limit = None
        self._Context = None
        self._Sort = None
        self._UseLucene = None
        self._LogType = None

    @property
    def EnvId(self):
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def QueryString(self):
        r"""查询语句，详情参考 https://cloud.tencent.com/document/product/614/47044
        :rtype: str
        """
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString

    @property
    def Limit(self):
        r"""单次要返回的日志条数，单次返回的最大条数为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        r"""加载更多使用，透传上次返回的 context 值，获取后续的日志内容，通过游标最多可获取10000条，请尽可能缩小时间范围
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Sort(self):
        r"""按时间排序 asc（升序）或者 desc（降序），默认为 desc
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def UseLucene(self):
        r"""是否使用Lucene语法，默认为false
        :rtype: bool
        """
        return self._UseLucene

    @UseLucene.setter
    def UseLucene(self, UseLucene):
        self._UseLucene = UseLucene

    @property
    def LogType(self):
        r"""日志类型
        :rtype: int
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._QueryString = params.get("QueryString")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Sort = params.get("Sort")
        self._UseLucene = params.get("UseLucene")
        self._LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClsLogResponse(AbstractModel):
    r"""SearchClsLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogResults: 日志内容结果
        :type LogResults: :class:`tencentcloud.tcbr.v20220217.models.LogResObject`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogResults = None
        self._RequestId = None

    @property
    def LogResults(self):
        r"""日志内容结果
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.LogResObject`
        """
        return self._LogResults

    @LogResults.setter
    def LogResults(self, LogResults):
        self._LogResults = LogResults

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
        if params.get("LogResults") is not None:
            self._LogResults = LogResObject()
            self._LogResults._deserialize(params.get("LogResults"))
        self._RequestId = params.get("RequestId")


class ServerBaseConfig(AbstractModel):
    r"""服务基础配置信息

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
        :param _Tag: 服务标签, function: 函数托管
        :type Tag: str
        :param _InternalAccess: 内网访问开关 close | open
        :type InternalAccess: str
        :param _InternalDomain: 内网域名
        :type InternalDomain: str
        :param _OperationMode: 运行模式
        :type OperationMode: str
        :param _TimerScale: 定时扩缩容配置
        :type TimerScale: list of TimerScale
        :param _EntryPoint: Dockerfile EntryPoint 参数
        :type EntryPoint: list of str
        :param _Cmd: Dockerfile Cmd 参数
        :type Cmd: list of str
        :param _SessionAffinity: 会话亲和性开关
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAffinity: str
        :param _VpcConf: Vpc 配置参数
        :type VpcConf: :class:`tencentcloud.tcbr.v20220217.models.VpcConf`
        :param _VolumesConf: 存储配置信息
        :type VolumesConf: list of VolumeConf
        :param _LinkImageRegistry: 关联镜像密钥
        :type LinkImageRegistry: str
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
        self._Tag = None
        self._InternalAccess = None
        self._InternalDomain = None
        self._OperationMode = None
        self._TimerScale = None
        self._EntryPoint = None
        self._Cmd = None
        self._SessionAffinity = None
        self._VpcConf = None
        self._VolumesConf = None
        self._LinkImageRegistry = None

    @property
    def EnvId(self):
        r"""环境 Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def OpenAccessTypes(self):
        r"""是否开启公网访问
        :rtype: list of str
        """
        return self._OpenAccessTypes

    @OpenAccessTypes.setter
    def OpenAccessTypes(self, OpenAccessTypes):
        self._OpenAccessTypes = OpenAccessTypes

    @property
    def Cpu(self):
        r"""Cpu 规格
        :rtype: float
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        r"""Mem 规格
        :rtype: float
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def MinNum(self):
        r"""最小副本数
        :rtype: int
        """
        return self._MinNum

    @MinNum.setter
    def MinNum(self, MinNum):
        self._MinNum = MinNum

    @property
    def MaxNum(self):
        r"""最大副本数
        :rtype: int
        """
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum

    @property
    def PolicyDetails(self):
        r"""扩缩容配置
        :rtype: list of HpaPolicy
        """
        return self._PolicyDetails

    @PolicyDetails.setter
    def PolicyDetails(self, PolicyDetails):
        self._PolicyDetails = PolicyDetails

    @property
    def CustomLogs(self):
        r"""日志采集路径
        :rtype: str
        """
        return self._CustomLogs

    @CustomLogs.setter
    def CustomLogs(self, CustomLogs):
        self._CustomLogs = CustomLogs

    @property
    def EnvParams(self):
        r"""环境变量
        :rtype: str
        """
        return self._EnvParams

    @EnvParams.setter
    def EnvParams(self, EnvParams):
        self._EnvParams = EnvParams

    @property
    def InitialDelaySeconds(self):
        r"""延迟检测时间
        :rtype: int
        """
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Port(self):
        r"""服务端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def HasDockerfile(self):
        r"""是否有Dockerfile
        :rtype: bool
        """
        return self._HasDockerfile

    @HasDockerfile.setter
    def HasDockerfile(self, HasDockerfile):
        self._HasDockerfile = HasDockerfile

    @property
    def Dockerfile(self):
        r"""Dockerfile 文件名
        :rtype: str
        """
        return self._Dockerfile

    @Dockerfile.setter
    def Dockerfile(self, Dockerfile):
        self._Dockerfile = Dockerfile

    @property
    def BuildDir(self):
        r"""构建目录
        :rtype: str
        """
        return self._BuildDir

    @BuildDir.setter
    def BuildDir(self, BuildDir):
        self._BuildDir = BuildDir

    @property
    def LogType(self):
        r"""日志类型: none | default | custom
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def LogSetId(self):
        r"""cls setId
        :rtype: str
        """
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def LogTopicId(self):
        r"""cls 主题id
        :rtype: str
        """
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def LogParseType(self):
        r"""解析类型：json ｜ line
        :rtype: str
        """
        return self._LogParseType

    @LogParseType.setter
    def LogParseType(self, LogParseType):
        self._LogParseType = LogParseType

    @property
    def Tag(self):
        r"""服务标签, function: 函数托管
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def InternalAccess(self):
        r"""内网访问开关 close | open
        :rtype: str
        """
        return self._InternalAccess

    @InternalAccess.setter
    def InternalAccess(self, InternalAccess):
        self._InternalAccess = InternalAccess

    @property
    def InternalDomain(self):
        r"""内网域名
        :rtype: str
        """
        return self._InternalDomain

    @InternalDomain.setter
    def InternalDomain(self, InternalDomain):
        self._InternalDomain = InternalDomain

    @property
    def OperationMode(self):
        r"""运行模式
        :rtype: str
        """
        return self._OperationMode

    @OperationMode.setter
    def OperationMode(self, OperationMode):
        self._OperationMode = OperationMode

    @property
    def TimerScale(self):
        r"""定时扩缩容配置
        :rtype: list of TimerScale
        """
        return self._TimerScale

    @TimerScale.setter
    def TimerScale(self, TimerScale):
        self._TimerScale = TimerScale

    @property
    def EntryPoint(self):
        r"""Dockerfile EntryPoint 参数
        :rtype: list of str
        """
        return self._EntryPoint

    @EntryPoint.setter
    def EntryPoint(self, EntryPoint):
        self._EntryPoint = EntryPoint

    @property
    def Cmd(self):
        r"""Dockerfile Cmd 参数
        :rtype: list of str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def SessionAffinity(self):
        r"""会话亲和性开关
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionAffinity

    @SessionAffinity.setter
    def SessionAffinity(self, SessionAffinity):
        self._SessionAffinity = SessionAffinity

    @property
    def VpcConf(self):
        r"""Vpc 配置参数
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.VpcConf`
        """
        return self._VpcConf

    @VpcConf.setter
    def VpcConf(self, VpcConf):
        self._VpcConf = VpcConf

    @property
    def VolumesConf(self):
        r"""存储配置信息
        :rtype: list of VolumeConf
        """
        return self._VolumesConf

    @VolumesConf.setter
    def VolumesConf(self, VolumesConf):
        self._VolumesConf = VolumesConf

    @property
    def LinkImageRegistry(self):
        r"""关联镜像密钥
        :rtype: str
        """
        return self._LinkImageRegistry

    @LinkImageRegistry.setter
    def LinkImageRegistry(self, LinkImageRegistry):
        self._LinkImageRegistry = LinkImageRegistry


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
        self._Tag = params.get("Tag")
        self._InternalAccess = params.get("InternalAccess")
        self._InternalDomain = params.get("InternalDomain")
        self._OperationMode = params.get("OperationMode")
        if params.get("TimerScale") is not None:
            self._TimerScale = []
            for item in params.get("TimerScale"):
                obj = TimerScale()
                obj._deserialize(item)
                self._TimerScale.append(obj)
        self._EntryPoint = params.get("EntryPoint")
        self._Cmd = params.get("Cmd")
        self._SessionAffinity = params.get("SessionAffinity")
        if params.get("VpcConf") is not None:
            self._VpcConf = VpcConf()
            self._VpcConf._deserialize(params.get("VpcConf"))
        if params.get("VolumesConf") is not None:
            self._VolumesConf = []
            for item in params.get("VolumesConf"):
                obj = VolumeConf()
                obj._deserialize(item)
                self._VolumesConf.append(obj)
        self._LinkImageRegistry = params.get("LinkImageRegistry")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerBaseInfo(AbstractModel):
    r"""服务基本信息

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
        :param _ServerType: 服务类型: function 云函数2.0；container 容器服务
        :type ServerType: str
        :param _TrafficType: 流量类型，目前只有 FLOW
        :type TrafficType: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._ServerName = None
        self._DefaultDomainName = None
        self._CustomDomainName = None
        self._Status = None
        self._UpdateTime = None
        self._AccessTypes = None
        self._CustomDomainNames = None
        self._ServerType = None
        self._TrafficType = None
        self._CreateTime = None

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def DefaultDomainName(self):
        r"""默认服务域名
        :rtype: str
        """
        return self._DefaultDomainName

    @DefaultDomainName.setter
    def DefaultDomainName(self, DefaultDomainName):
        self._DefaultDomainName = DefaultDomainName

    @property
    def CustomDomainName(self):
        r"""自定义域名
        :rtype: str
        """
        return self._CustomDomainName

    @CustomDomainName.setter
    def CustomDomainName(self, CustomDomainName):
        self._CustomDomainName = CustomDomainName

    @property
    def Status(self):
        r"""服务状态：running/deploying/deploy_failed
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AccessTypes(self):
        r"""公网访问类型
        :rtype: list of str
        """
        return self._AccessTypes

    @AccessTypes.setter
    def AccessTypes(self, AccessTypes):
        self._AccessTypes = AccessTypes

    @property
    def CustomDomainNames(self):
        r"""展示自定义域名
        :rtype: list of str
        """
        return self._CustomDomainNames

    @CustomDomainNames.setter
    def CustomDomainNames(self, CustomDomainNames):
        self._CustomDomainNames = CustomDomainNames

    @property
    def ServerType(self):
        r"""服务类型: function 云函数2.0；container 容器服务
        :rtype: str
        """
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def TrafficType(self):
        r"""流量类型，目前只有 FLOW
        :rtype: str
        """
        return self._TrafficType

    @TrafficType.setter
    def TrafficType(self, TrafficType):
        self._TrafficType = TrafficType

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ServerName = params.get("ServerName")
        self._DefaultDomainName = params.get("DefaultDomainName")
        self._CustomDomainName = params.get("CustomDomainName")
        self._Status = params.get("Status")
        self._UpdateTime = params.get("UpdateTime")
        self._AccessTypes = params.get("AccessTypes")
        self._CustomDomainNames = params.get("CustomDomainNames")
        self._ServerType = params.get("ServerType")
        self._TrafficType = params.get("TrafficType")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerManageTaskInfo(AbstractModel):
    r"""服务管理任务信息

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
        r"""任务Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def EnvId(self):
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChangeType(self):
        r"""变更类型
        :rtype: str
        """
        return self._ChangeType

    @ChangeType.setter
    def ChangeType(self, ChangeType):
        self._ChangeType = ChangeType

    @property
    def ReleaseType(self):
        r"""发布类型
        :rtype: str
        """
        return self._ReleaseType

    @ReleaseType.setter
    def ReleaseType(self, ReleaseType):
        self._ReleaseType = ReleaseType

    @property
    def DeployType(self):
        r"""部署类型
        :rtype: str
        """
        return self._DeployType

    @DeployType.setter
    def DeployType(self, DeployType):
        self._DeployType = DeployType

    @property
    def PreVersionName(self):
        r"""上一个版本名
        :rtype: str
        """
        return self._PreVersionName

    @PreVersionName.setter
    def PreVersionName(self, PreVersionName):
        self._PreVersionName = PreVersionName

    @property
    def VersionName(self):
        r"""版本名
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def PipelineId(self):
        r"""流水线Id
        :rtype: int
        """
        return self._PipelineId

    @PipelineId.setter
    def PipelineId(self, PipelineId):
        self._PipelineId = PipelineId

    @property
    def PipelineTaskId(self):
        r"""流水线任务Id
        :rtype: int
        """
        return self._PipelineTaskId

    @PipelineTaskId.setter
    def PipelineTaskId(self, PipelineTaskId):
        self._PipelineTaskId = PipelineTaskId

    @property
    def ReleaseId(self):
        r"""发布单Id
        :rtype: int
        """
        return self._ReleaseId

    @ReleaseId.setter
    def ReleaseId(self, ReleaseId):
        self._ReleaseId = ReleaseId

    @property
    def Status(self):
        r"""状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Steps(self):
        r"""步骤信息
        :rtype: list of TaskStepInfo
        """
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps

    @property
    def FailReason(self):
        r"""失败原因
        :rtype: str
        """
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def OperatorRemark(self):
        r"""操作标识
        :rtype: str
        """
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
        


class SimpleVersion(AbstractModel):
    r"""删除版本时需要的简化信息

    """

    def __init__(self):
        r"""
        :param _EnvId: 要删除版本的环境 Id
        :type EnvId: str
        :param _ServerName: 要删除版本的服务名
        :type ServerName: str
        :param _VersionName: 要删除版本的版本名
        :type VersionName: str
        """
        self._EnvId = None
        self._ServerName = None
        self._VersionName = None

    @property
    def EnvId(self):
        r"""要删除版本的环境 Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""要删除版本的服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        r"""要删除版本的版本名
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaticStorageInfo(AbstractModel):
    r"""静态CDN资源信息

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
        r"""静态CDN域名
        :rtype: str
        """
        return self._StaticDomain

    @StaticDomain.setter
    def StaticDomain(self, StaticDomain):
        self._StaticDomain = StaticDomain

    @property
    def DefaultDirName(self):
        r"""静态CDN默认文件夹，当前为根目录
        :rtype: str
        """
        return self._DefaultDirName

    @DefaultDirName.setter
    def DefaultDirName(self, DefaultDirName):
        self._DefaultDirName = DefaultDirName

    @property
    def Status(self):
        r"""资源状态(process/online/offline/init)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""cos所属区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""bucket信息
        :rtype: str
        """
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
    r"""StorageInfo 资源信息

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
        r"""资源所属地域。
当前支持ap-shanghai
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""桶名，存储资源的唯一标识
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def CdnDomain(self):
        r"""cdn 域名
        :rtype: str
        """
        return self._CdnDomain

    @CdnDomain.setter
    def CdnDomain(self, CdnDomain):
        self._CdnDomain = CdnDomain

    @property
    def AppId(self):
        r"""资源所属用户的腾讯云appId
        :rtype: str
        """
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
        


class SubmitServerRollbackRequest(AbstractModel):
    r"""SubmitServerRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _CurrentVersionName: 当前版本
        :type CurrentVersionName: str
        :param _RollbackVersionName: 回滚版本
        :type RollbackVersionName: str
        :param _OperatorRemark: 操作标识
        :type OperatorRemark: str
        """
        self._EnvId = None
        self._ServerName = None
        self._CurrentVersionName = None
        self._RollbackVersionName = None
        self._OperatorRemark = None

    @property
    def EnvId(self):
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def CurrentVersionName(self):
        r"""当前版本
        :rtype: str
        """
        return self._CurrentVersionName

    @CurrentVersionName.setter
    def CurrentVersionName(self, CurrentVersionName):
        self._CurrentVersionName = CurrentVersionName

    @property
    def RollbackVersionName(self):
        r"""回滚版本
        :rtype: str
        """
        return self._RollbackVersionName

    @RollbackVersionName.setter
    def RollbackVersionName(self, RollbackVersionName):
        self._RollbackVersionName = RollbackVersionName

    @property
    def OperatorRemark(self):
        r"""操作标识
        :rtype: str
        """
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._CurrentVersionName = params.get("CurrentVersionName")
        self._RollbackVersionName = params.get("RollbackVersionName")
        self._OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitServerRollbackResponse(AbstractModel):
    r"""SubmitServerRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SuccessDeleteVersions(AbstractModel):
    r"""删除成功的版本信息

    """

    def __init__(self):
        r"""
        :param _Version: 版本简化信息
        :type Version: :class:`tencentcloud.tcbr.v20220217.models.SimpleVersion`
        :param _RequestId: 删除版本的 RequestId
        :type RequestId: str
        :param _Result: 删除版本结果
        :type Result: str
        """
        self._Version = None
        self._RequestId = None
        self._Result = None

    @property
    def Version(self):
        r"""版本简化信息
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.SimpleVersion`
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def RequestId(self):
        r"""删除版本的 RequestId
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def Result(self):
        r"""删除版本结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        if params.get("Version") is not None:
            self._Version = SimpleVersion()
            self._Version._deserialize(params.get("Version"))
        self._RequestId = params.get("RequestId")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签键值对

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
        r"""标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值
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
        


class TaskStepInfo(AbstractModel):
    r"""任务步骤信息

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
        r"""步骤名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""未启动："todo"
运行中："running"
失败："failed"
成功结束："finished"
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CostTime(self):
        r"""消耗时间：秒
        :rtype: int
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def FailReason(self):
        r"""失败原因
        :rtype: str
        """
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
        


class TimerScale(AbstractModel):
    r"""定时扩缩容配置

    """

    def __init__(self):
        r"""
        :param _CycleType: 循环类型
        :type CycleType: str
        :param _StartDate: 循环起始
        :type StartDate: str
        :param _EndDate: 循环结束
        :type EndDate: str
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _ReplicaNum: 副本个数
        :type ReplicaNum: int
        """
        self._CycleType = None
        self._StartDate = None
        self._EndDate = None
        self._StartTime = None
        self._EndTime = None
        self._ReplicaNum = None

    @property
    def CycleType(self):
        r"""循环类型
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def StartDate(self):
        r"""循环起始
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""循环结束
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def StartTime(self):
        r"""起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ReplicaNum(self):
        r"""副本个数
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum


    def _deserialize(self, params):
        self._CycleType = params.get("CycleType")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ReplicaNum = params.get("ReplicaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudRunServerRequest(AbstractModel):
    r"""UpdateCloudRunServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: <p>环境Id</p>
        :type EnvId: str
        :param _ServerName: <p>服务名</p>
        :type ServerName: str
        :param _DeployInfo: <p>部署信息</p>
        :type DeployInfo: :class:`tencentcloud.tcbr.v20220217.models.DeployParam`
        :param _ServerConfig: <p>服务配置信息(已废弃)</p>
        :type ServerConfig: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        :param _Business: <p>业务类型，默认tcr</p>
        :type Business: str
        :param _Items: <p>服务配置信息</p>
        :type Items: list of DiffConfigItem
        """
        self._EnvId = None
        self._ServerName = None
        self._DeployInfo = None
        self._ServerConfig = None
        self._Business = None
        self._Items = None

    @property
    def EnvId(self):
        r"""<p>环境Id</p>
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        r"""<p>服务名</p>
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def DeployInfo(self):
        r"""<p>部署信息</p>
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DeployParam`
        """
        return self._DeployInfo

    @DeployInfo.setter
    def DeployInfo(self, DeployInfo):
        self._DeployInfo = DeployInfo

    @property
    def ServerConfig(self):
        r"""<p>服务配置信息(已废弃)</p>
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        """
        return self._ServerConfig

    @ServerConfig.setter
    def ServerConfig(self, ServerConfig):
        self._ServerConfig = ServerConfig

    @property
    def Business(self):
        r"""<p>业务类型，默认tcr</p>
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Items(self):
        r"""<p>服务配置信息</p>
        :rtype: list of DiffConfigItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        if params.get("DeployInfo") is not None:
            self._DeployInfo = DeployParam()
            self._DeployInfo._deserialize(params.get("DeployInfo"))
        if params.get("ServerConfig") is not None:
            self._ServerConfig = ServerBaseConfig()
            self._ServerConfig._deserialize(params.get("ServerConfig"))
        self._Business = params.get("Business")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DiffConfigItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudRunServerResponse(AbstractModel):
    r"""UpdateCloudRunServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: <p>环境Id</p>
        :type EnvId: str
        :param _TaskId: <p>一键部署任务Id，暂时用不到</p>
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def EnvId(self):
        r"""<p>环境Id</p>
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def TaskId(self):
        r"""<p>一键部署任务Id，暂时用不到</p>
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._EnvId = params.get("EnvId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class VersionFlowInfo(AbstractModel):
    r"""版本流量信息

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
        r"""版本名
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def IsDefaultPriority(self):
        r"""是否默认版本
        :rtype: bool
        """
        return self._IsDefaultPriority

    @IsDefaultPriority.setter
    def IsDefaultPriority(self, IsDefaultPriority):
        self._IsDefaultPriority = IsDefaultPriority

    @property
    def FlowRatio(self):
        r"""流量比例
        :rtype: int
        """
        return self._FlowRatio

    @FlowRatio.setter
    def FlowRatio(self, FlowRatio):
        self._FlowRatio = FlowRatio

    @property
    def UrlParam(self):
        r"""测试KV值
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.ObjectKV`
        """
        return self._UrlParam

    @UrlParam.setter
    def UrlParam(self, UrlParam):
        self._UrlParam = UrlParam

    @property
    def Priority(self):
        r"""权重
        :rtype: int
        """
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
        


class VersionInfo(AbstractModel):
    r"""版本信息

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名
        :type VersionName: str
        :param _FlowRatio: 流量比例
        :type FlowRatio: int
        :param _Status: 版本状态
        :type Status: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _UpdatedTime: 更新时间
        :type UpdatedTime: str
        :param _BuildId: 构建Id
        :type BuildId: int
        :param _UploadType: 上传方式
        :type UploadType: str
        :param _Remark: 操作标识
        :type Remark: str
        :param _UrlParam: 测试参数
        :type UrlParam: :class:`tencentcloud.tcbr.v20220217.models.ObjectKV`
        :param _Priority: 权重
        :type Priority: int
        :param _IsDefaultPriority: 是否默认
        :type IsDefaultPriority: bool
        :param _FlowParams: 流量参数
        :type FlowParams: list of ObjectKVPriority
        :param _MinReplicas: 最小副本数
        :type MinReplicas: int
        :param _MaxReplicas: 最大副本数
        :type MaxReplicas: int
        :param _RunId: 操作Id
        :type RunId: str
        :param _Percent: 百分比
        :type Percent: int
        :param _CurrentReplicas: 当前副本数
        :type CurrentReplicas: int
        :param _Architecture: 架构类型
        :type Architecture: str
        """
        self._VersionName = None
        self._FlowRatio = None
        self._Status = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._BuildId = None
        self._UploadType = None
        self._Remark = None
        self._UrlParam = None
        self._Priority = None
        self._IsDefaultPriority = None
        self._FlowParams = None
        self._MinReplicas = None
        self._MaxReplicas = None
        self._RunId = None
        self._Percent = None
        self._CurrentReplicas = None
        self._Architecture = None

    @property
    def VersionName(self):
        r"""版本名
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def FlowRatio(self):
        r"""流量比例
        :rtype: int
        """
        return self._FlowRatio

    @FlowRatio.setter
    def FlowRatio(self, FlowRatio):
        self._FlowRatio = FlowRatio

    @property
    def Status(self):
        r"""版本状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def BuildId(self):
        r"""构建Id
        :rtype: int
        """
        return self._BuildId

    @BuildId.setter
    def BuildId(self, BuildId):
        self._BuildId = BuildId

    @property
    def UploadType(self):
        r"""上传方式
        :rtype: str
        """
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def Remark(self):
        r"""操作标识
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def UrlParam(self):
        r"""测试参数
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.ObjectKV`
        """
        return self._UrlParam

    @UrlParam.setter
    def UrlParam(self, UrlParam):
        self._UrlParam = UrlParam

    @property
    def Priority(self):
        r"""权重
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def IsDefaultPriority(self):
        r"""是否默认
        :rtype: bool
        """
        return self._IsDefaultPriority

    @IsDefaultPriority.setter
    def IsDefaultPriority(self, IsDefaultPriority):
        self._IsDefaultPriority = IsDefaultPriority

    @property
    def FlowParams(self):
        r"""流量参数
        :rtype: list of ObjectKVPriority
        """
        return self._FlowParams

    @FlowParams.setter
    def FlowParams(self, FlowParams):
        self._FlowParams = FlowParams

    @property
    def MinReplicas(self):
        r"""最小副本数
        :rtype: int
        """
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        r"""最大副本数
        :rtype: int
        """
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def RunId(self):
        r"""操作Id
        :rtype: str
        """
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def Percent(self):
        r"""百分比
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def CurrentReplicas(self):
        r"""当前副本数
        :rtype: int
        """
        return self._CurrentReplicas

    @CurrentReplicas.setter
    def CurrentReplicas(self, CurrentReplicas):
        self._CurrentReplicas = CurrentReplicas

    @property
    def Architecture(self):
        r"""架构类型
        :rtype: str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._FlowRatio = params.get("FlowRatio")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._BuildId = params.get("BuildId")
        self._UploadType = params.get("UploadType")
        self._Remark = params.get("Remark")
        if params.get("UrlParam") is not None:
            self._UrlParam = ObjectKV()
            self._UrlParam._deserialize(params.get("UrlParam"))
        self._Priority = params.get("Priority")
        self._IsDefaultPriority = params.get("IsDefaultPriority")
        if params.get("FlowParams") is not None:
            self._FlowParams = []
            for item in params.get("FlowParams"):
                obj = ObjectKVPriority()
                obj._deserialize(item)
                self._FlowParams.append(obj)
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        self._RunId = params.get("RunId")
        self._Percent = params.get("Percent")
        self._CurrentReplicas = params.get("CurrentReplicas")
        self._Architecture = params.get("Architecture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionPodInstance(AbstractModel):
    r"""版本Pod实例信息

    """

    def __init__(self):
        r"""
        :param _Webshell: 实例webshell链接
        :type Webshell: str
        :param _PodId: 实例Id
        :type PodId: str
        :param _Status: 实例状态
        :type Status: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._Webshell = None
        self._PodId = None
        self._Status = None
        self._CreateTime = None

    @property
    def Webshell(self):
        r"""实例webshell链接
        :rtype: str
        """
        return self._Webshell

    @Webshell.setter
    def Webshell(self, Webshell):
        self._Webshell = Webshell

    @property
    def PodId(self):
        r"""实例Id
        :rtype: str
        """
        return self._PodId

    @PodId.setter
    def PodId(self, PodId):
        self._PodId = PodId

    @property
    def Status(self):
        r"""实例状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Webshell = params.get("Webshell")
        self._PodId = params.get("PodId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeConf(AbstractModel):
    r"""存储配置

    """

    def __init__(self):
        r"""
        :param _Type: 存储类型
        :type Type: str
        :param _BucketName: 对象存储桶名称
        :type BucketName: str
        :param _Endpoint: 存储连接地址
        :type Endpoint: str
        :param _KeyID: 存储连接用户密码
        :type KeyID: str
        :param _DstPath: 存储挂载目的目录
        :type DstPath: str
        :param _SrcPath: 存储挂载源目录
        :type SrcPath: str
        """
        self._Type = None
        self._BucketName = None
        self._Endpoint = None
        self._KeyID = None
        self._DstPath = None
        self._SrcPath = None

    @property
    def Type(self):
        r"""存储类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BucketName(self):
        r"""对象存储桶名称
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def Endpoint(self):
        r"""存储连接地址
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def KeyID(self):
        r"""存储连接用户密码
        :rtype: str
        """
        return self._KeyID

    @KeyID.setter
    def KeyID(self, KeyID):
        self._KeyID = KeyID

    @property
    def DstPath(self):
        r"""存储挂载目的目录
        :rtype: str
        """
        return self._DstPath

    @DstPath.setter
    def DstPath(self, DstPath):
        self._DstPath = DstPath

    @property
    def SrcPath(self):
        r"""存储挂载源目录
        :rtype: str
        """
        return self._SrcPath

    @SrcPath.setter
    def SrcPath(self, SrcPath):
        self._SrcPath = SrcPath


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._BucketName = params.get("BucketName")
        self._Endpoint = params.get("Endpoint")
        self._KeyID = params.get("KeyID")
        self._DstPath = params.get("DstPath")
        self._SrcPath = params.get("SrcPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcConf(AbstractModel):
    r"""云托管服务 Vpc 配置

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id
        :type VpcId: str
        :param _VpcCIDR: vpc 网段
        :type VpcCIDR: str
        :param _SubnetId: subnet id
        :type SubnetId: str
        :param _SubnetCIDR: subnet 网段
        :type SubnetCIDR: str
        """
        self._VpcId = None
        self._VpcCIDR = None
        self._SubnetId = None
        self._SubnetCIDR = None

    @property
    def VpcId(self):
        r"""vpc id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcCIDR(self):
        r"""vpc 网段
        :rtype: str
        """
        return self._VpcCIDR

    @VpcCIDR.setter
    def VpcCIDR(self, VpcCIDR):
        self._VpcCIDR = VpcCIDR

    @property
    def SubnetId(self):
        r"""subnet id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetCIDR(self):
        r"""subnet 网段
        :rtype: str
        """
        return self._SubnetCIDR

    @SubnetCIDR.setter
    def SubnetCIDR(self, SubnetCIDR):
        self._SubnetCIDR = SubnetCIDR


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcCIDR = params.get("VpcCIDR")
        self._SubnetId = params.get("SubnetId")
        self._SubnetCIDR = params.get("SubnetCIDR")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        