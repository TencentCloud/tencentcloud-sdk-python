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
        :param _MinReplicas: 弹性伸缩最小实例数
        :type MinReplicas: int
        :param _MaxReplicas: 弹性伸缩最大实例数
        :type MaxReplicas: int
        :param _HorizontalAutoscaler: 指标弹性伸缩策略
注意：此字段可能返回 null，表示取不到有效值。
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param _CronHorizontalAutoscaler: 定时弹性伸缩策略
注意：此字段可能返回 null，表示取不到有效值。
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param _AutoscalerId: 弹性伸缩ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalerId: str
        :param _AutoscalerName: 弹性伸缩名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalerName: str
        :param _Description: 弹性伸缩描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateDate: 创建日期
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param _ModifyDate: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyDate: str
        :param _EnableDate: 启用时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableDate: str
        :param _Enabled: 是否启用
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self._MinReplicas = None
        self._MaxReplicas = None
        self._HorizontalAutoscaler = None
        self._CronHorizontalAutoscaler = None
        self._AutoscalerId = None
        self._AutoscalerName = None
        self._Description = None
        self._CreateDate = None
        self._ModifyDate = None
        self._EnableDate = None
        self._Enabled = None

    @property
    def MinReplicas(self):
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def HorizontalAutoscaler(self):
        return self._HorizontalAutoscaler

    @HorizontalAutoscaler.setter
    def HorizontalAutoscaler(self, HorizontalAutoscaler):
        self._HorizontalAutoscaler = HorizontalAutoscaler

    @property
    def CronHorizontalAutoscaler(self):
        return self._CronHorizontalAutoscaler

    @CronHorizontalAutoscaler.setter
    def CronHorizontalAutoscaler(self, CronHorizontalAutoscaler):
        self._CronHorizontalAutoscaler = CronHorizontalAutoscaler

    @property
    def AutoscalerId(self):
        return self._AutoscalerId

    @AutoscalerId.setter
    def AutoscalerId(self, AutoscalerId):
        self._AutoscalerId = AutoscalerId

    @property
    def AutoscalerName(self):
        return self._AutoscalerName

    @AutoscalerName.setter
    def AutoscalerName(self, AutoscalerName):
        self._AutoscalerName = AutoscalerName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def EnableDate(self):
        return self._EnableDate

    @EnableDate.setter
    def EnableDate(self, EnableDate):
        self._EnableDate = EnableDate

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("HorizontalAutoscaler") is not None:
            self._HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self._HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self._CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self._CronHorizontalAutoscaler.append(obj)
        self._AutoscalerId = params.get("AutoscalerId")
        self._AutoscalerName = params.get("AutoscalerName")
        self._Description = params.get("Description")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        self._EnableDate = params.get("EnableDate")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigData(AbstractModel):
    """配置

    """

    def __init__(self):
        r"""
        :param _Name: 配置名称
        :type Name: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _RelatedApplications: 关联的服务列表
        :type RelatedApplications: list of TemService
        :param _Data: 配置条目
        :type Data: list of Pair
        """
        self._Name = None
        self._CreateTime = None
        self._RelatedApplications = None
        self._Data = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RelatedApplications(self):
        return self._RelatedApplications

    @RelatedApplications.setter
    def RelatedApplications(self, RelatedApplications):
        self._RelatedApplications = RelatedApplications

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        if params.get("RelatedApplications") is not None:
            self._RelatedApplications = []
            for item in params.get("RelatedApplications"):
                obj = TemService()
                obj._deserialize(item)
                self._RelatedApplications.append(obj)
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosToken(AbstractModel):
    """Cos token

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID
        :type RequestId: str
        :param _Bucket: 存储桶桶名
        :type Bucket: str
        :param _Region: 存储桶所在区域
        :type Region: str
        :param _TmpSecretId: 临时密钥的SecretId
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时密钥的SecretKey
        :type TmpSecretKey: str
        :param _SessionToken: 临时密钥的 sessionToken
        :type SessionToken: str
        :param _StartTime: 临时密钥获取的开始时间
        :type StartTime: str
        :param _ExpiredTime: 临时密钥的 expiredTime
        :type ExpiredTime: str
        :param _FullPath: 包完整路径
        :type FullPath: str
        """
        self._RequestId = None
        self._Bucket = None
        self._Region = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._SessionToken = None
        self._StartTime = None
        self._ExpiredTime = None
        self._FullPath = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def SessionToken(self):
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def FullPath(self):
        return self._FullPath

    @FullPath.setter
    def FullPath(self, FullPath):
        self._FullPath = FullPath


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._SessionToken = params.get("SessionToken")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._FullPath = params.get("FullPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationAutoscalerRequest(AbstractModel):
    """CreateApplicationAutoscaler请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _Autoscaler: 弹性伸缩策略
        :type Autoscaler: :class:`tencentcloud.tem.v20210701.models.Autoscaler`
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._Autoscaler = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Autoscaler(self):
        return self._Autoscaler

    @Autoscaler.setter
    def Autoscaler(self, Autoscaler):
        self._Autoscaler = Autoscaler


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        if params.get("Autoscaler") is not None:
            self._Autoscaler = Autoscaler()
            self._Autoscaler._deserialize(params.get("Autoscaler"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationAutoscalerResponse(AbstractModel):
    """CreateApplicationAutoscaler返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 弹性伸缩策略组合ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateApplicationRequest(AbstractModel):
    """CreateApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationName: 应用名
        :type ApplicationName: str
        :param _Description: 描述
        :type Description: str
        :param _UseDefaultImageService: 是否使用默认镜像服务 1-是，0-否
        :type UseDefaultImageService: int
        :param _RepoType: 如果是绑定仓库，绑定的仓库类型，0-个人版，1-企业版
        :type RepoType: int
        :param _InstanceId: 企业版镜像服务的实例id
        :type InstanceId: str
        :param _RepoServer: 绑定镜像服务器地址
        :type RepoServer: str
        :param _RepoName: 绑定镜像仓库名
        :type RepoName: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _SubnetList: 应用所在子网
        :type SubnetList: list of str
        :param _CodingLanguage: 编程语言 
- JAVA
- OTHER
        :type CodingLanguage: str
        :param _DeployMode: 部署方式 
- IMAGE
- JAR
- WAR
        :type DeployMode: str
        :param _EnableTracing: 是否开启 Java 应用的 APM 自动上报功能，1 表示启用；0 表示关闭
        :type EnableTracing: int
        :param _UseDefaultImageServiceParameters: 使用默认镜像服务额外参数
        :type UseDefaultImageServiceParameters: :class:`tencentcloud.tem.v20210701.models.UseDefaultRepoParameters`
        :param _Tags: 标签
        :type Tags: list of Tag
        """
        self._ApplicationName = None
        self._Description = None
        self._UseDefaultImageService = None
        self._RepoType = None
        self._InstanceId = None
        self._RepoServer = None
        self._RepoName = None
        self._SourceChannel = None
        self._SubnetList = None
        self._CodingLanguage = None
        self._DeployMode = None
        self._EnableTracing = None
        self._UseDefaultImageServiceParameters = None
        self._Tags = None

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UseDefaultImageService(self):
        return self._UseDefaultImageService

    @UseDefaultImageService.setter
    def UseDefaultImageService(self, UseDefaultImageService):
        self._UseDefaultImageService = UseDefaultImageService

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RepoServer(self):
        return self._RepoServer

    @RepoServer.setter
    def RepoServer(self, RepoServer):
        self._RepoServer = RepoServer

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def SubnetList(self):
        return self._SubnetList

    @SubnetList.setter
    def SubnetList(self, SubnetList):
        self._SubnetList = SubnetList

    @property
    def CodingLanguage(self):
        return self._CodingLanguage

    @CodingLanguage.setter
    def CodingLanguage(self, CodingLanguage):
        self._CodingLanguage = CodingLanguage

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def EnableTracing(self):
        return self._EnableTracing

    @EnableTracing.setter
    def EnableTracing(self, EnableTracing):
        self._EnableTracing = EnableTracing

    @property
    def UseDefaultImageServiceParameters(self):
        return self._UseDefaultImageServiceParameters

    @UseDefaultImageServiceParameters.setter
    def UseDefaultImageServiceParameters(self, UseDefaultImageServiceParameters):
        self._UseDefaultImageServiceParameters = UseDefaultImageServiceParameters

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ApplicationName = params.get("ApplicationName")
        self._Description = params.get("Description")
        self._UseDefaultImageService = params.get("UseDefaultImageService")
        self._RepoType = params.get("RepoType")
        self._InstanceId = params.get("InstanceId")
        self._RepoServer = params.get("RepoServer")
        self._RepoName = params.get("RepoName")
        self._SourceChannel = params.get("SourceChannel")
        self._SubnetList = params.get("SubnetList")
        self._CodingLanguage = params.get("CodingLanguage")
        self._DeployMode = params.get("DeployMode")
        self._EnableTracing = params.get("EnableTracing")
        if params.get("UseDefaultImageServiceParameters") is not None:
            self._UseDefaultImageServiceParameters = UseDefaultRepoParameters()
            self._UseDefaultImageServiceParameters._deserialize(params.get("UseDefaultImageServiceParameters"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationResponse(AbstractModel):
    """CreateApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 服务code
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateApplicationServiceRequest(AbstractModel):
    """CreateApplicationService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _Service: 访问方式详情
        :type Service: :class:`tencentcloud.tem.v20210701.models.ServicePortMapping`
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._Service = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        if params.get("Service") is not None:
            self._Service = ServicePortMapping()
            self._Service._deserialize(params.get("Service"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationServiceResponse(AbstractModel):
    """CreateApplicationService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateConfigDataRequest(AbstractModel):
    """CreateConfigData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param _Name: 配置名
        :type Name: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _Data: 配置信息
        :type Data: list of Pair
        """
        self._EnvironmentId = None
        self._Name = None
        self._SourceChannel = None
        self._Data = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigDataResponse(AbstractModel):
    """CreateConfigData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateCosTokenRequest(AbstractModel):
    """CreateCosToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _PkgName: 包名
        :type PkgName: str
        :param _OptType: optType 1上传  2查询
        :type OptType: int
        :param _SourceChannel: 来源 channel
        :type SourceChannel: int
        :param _TimeVersion: 充当deployVersion入参
        :type TimeVersion: str
        """
        self._ApplicationId = None
        self._PkgName = None
        self._OptType = None
        self._SourceChannel = None
        self._TimeVersion = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PkgName(self):
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def OptType(self):
        return self._OptType

    @OptType.setter
    def OptType(self, OptType):
        self._OptType = OptType

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def TimeVersion(self):
        return self._TimeVersion

    @TimeVersion.setter
    def TimeVersion(self, TimeVersion):
        self._TimeVersion = TimeVersion


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._PkgName = params.get("PkgName")
        self._OptType = params.get("OptType")
        self._SourceChannel = params.get("SourceChannel")
        self._TimeVersion = params.get("TimeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosTokenResponse(AbstractModel):
    """CreateCosToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 成功时为CosToken对象，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tem.v20210701.models.CosToken`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CosToken()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentName: 环境名称
        :type EnvironmentName: str
        :param _Description: 环境描述
        :type Description: str
        :param _Vpc: 私有网络名称
        :type Vpc: str
        :param _SubnetIds: 子网列表
        :type SubnetIds: list of str
        :param _K8sVersion: K8s version
        :type K8sVersion: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _EnableTswTraceService: 是否开启tsw服务
        :type EnableTswTraceService: bool
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _EnvType: 环境类型：test、pre、prod
        :type EnvType: str
        :param _CreateRegion: 创建环境的region
        :type CreateRegion: str
        :param _SetupVpc: 是否创建私有网络
        :type SetupVpc: bool
        :param _SetupPrometheus: 是否创建 Prometheus 实例
        :type SetupPrometheus: bool
        :param _PrometheusId: prometheus 实例 id
        :type PrometheusId: str
        :param _ApmId: apm id
        :type ApmId: str
        """
        self._EnvironmentName = None
        self._Description = None
        self._Vpc = None
        self._SubnetIds = None
        self._K8sVersion = None
        self._SourceChannel = None
        self._EnableTswTraceService = None
        self._Tags = None
        self._EnvType = None
        self._CreateRegion = None
        self._SetupVpc = None
        self._SetupPrometheus = None
        self._PrometheusId = None
        self._ApmId = None

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Vpc(self):
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def K8sVersion(self):
        return self._K8sVersion

    @K8sVersion.setter
    def K8sVersion(self, K8sVersion):
        self._K8sVersion = K8sVersion

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnableTswTraceService(self):
        return self._EnableTswTraceService

    @EnableTswTraceService.setter
    def EnableTswTraceService(self, EnableTswTraceService):
        self._EnableTswTraceService = EnableTswTraceService

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def CreateRegion(self):
        return self._CreateRegion

    @CreateRegion.setter
    def CreateRegion(self, CreateRegion):
        self._CreateRegion = CreateRegion

    @property
    def SetupVpc(self):
        return self._SetupVpc

    @SetupVpc.setter
    def SetupVpc(self, SetupVpc):
        self._SetupVpc = SetupVpc

    @property
    def SetupPrometheus(self):
        return self._SetupPrometheus

    @SetupPrometheus.setter
    def SetupPrometheus(self, SetupPrometheus):
        self._SetupPrometheus = SetupPrometheus

    @property
    def PrometheusId(self):
        return self._PrometheusId

    @PrometheusId.setter
    def PrometheusId(self, PrometheusId):
        self._PrometheusId = PrometheusId

    @property
    def ApmId(self):
        return self._ApmId

    @ApmId.setter
    def ApmId(self, ApmId):
        self._ApmId = ApmId


    def _deserialize(self, params):
        self._EnvironmentName = params.get("EnvironmentName")
        self._Description = params.get("Description")
        self._Vpc = params.get("Vpc")
        self._SubnetIds = params.get("SubnetIds")
        self._K8sVersion = params.get("K8sVersion")
        self._SourceChannel = params.get("SourceChannel")
        self._EnableTswTraceService = params.get("EnableTswTraceService")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._EnvType = params.get("EnvType")
        self._CreateRegion = params.get("CreateRegion")
        self._SetupVpc = params.get("SetupVpc")
        self._SetupPrometheus = params.get("SetupPrometheus")
        self._PrometheusId = params.get("PrometheusId")
        self._ApmId = params.get("ApmId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 成功时为环境ID，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateLogConfigRequest(AbstractModel):
    """CreateLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param _Name: 配置名
        :type Name: str
        :param _InputType: 收集类型，container_stdout 为标准输出；container_file 为文件；
        :type InputType: str
        :param _ApplicationId: 应用 ID
        :type ApplicationId: str
        :param _LogsetId: 日志集 ID
        :type LogsetId: str
        :param _TopicId: 日志主题 ID
        :type TopicId: str
        :param _LogType: 日志提取模式，minimalist_log 为单行全文；multiline_log 为多行全文；json_log 为 json格式；fullregex_log 为单行正则；multiline_fullregex_log 为多行正则
        :type LogType: str
        :param _BeginningRegex: 首行正则表达式，当LogType=multiline_log 时生效
        :type BeginningRegex: str
        :param _LogPath: 收集文件目录，当 InputType=container_file 时生效
        :type LogPath: str
        :param _FilePattern: 收集文件名模式，当 InputType=container_file 时生效
        :type FilePattern: str
        :param _ExtractRule: 导出规则
        :type ExtractRule: :class:`tencentcloud.tem.v20210701.models.LogConfigExtractRule`
        """
        self._EnvironmentId = None
        self._Name = None
        self._InputType = None
        self._ApplicationId = None
        self._LogsetId = None
        self._TopicId = None
        self._LogType = None
        self._BeginningRegex = None
        self._LogPath = None
        self._FilePattern = None
        self._ExtractRule = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def BeginningRegex(self):
        return self._BeginningRegex

    @BeginningRegex.setter
    def BeginningRegex(self, BeginningRegex):
        self._BeginningRegex = BeginningRegex

    @property
    def LogPath(self):
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath

    @property
    def FilePattern(self):
        return self._FilePattern

    @FilePattern.setter
    def FilePattern(self, FilePattern):
        self._FilePattern = FilePattern

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._InputType = params.get("InputType")
        self._ApplicationId = params.get("ApplicationId")
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._LogType = params.get("LogType")
        self._BeginningRegex = params.get("BeginningRegex")
        self._LogPath = params.get("LogPath")
        self._FilePattern = params.get("FilePattern")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = LogConfigExtractRule()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogConfigResponse(AbstractModel):
    """CreateLogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateResourceRequest(AbstractModel):
    """CreateResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 Id
        :type EnvironmentId: str
        :param _ResourceType: 资源类型，目前支持文件系统：CFS；日志服务：CLS；注册中心：TSE_SRE
        :type ResourceType: str
        :param _ResourceId: 资源 Id
        :type ResourceId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _ResourceFrom: 资源来源，目前支持：existing，已有资源；creating，自动创建
        :type ResourceFrom: str
        :param _ResourceConfig: 设置 resource 的额外配置
        :type ResourceConfig: str
        """
        self._EnvironmentId = None
        self._ResourceType = None
        self._ResourceId = None
        self._SourceChannel = None
        self._ResourceFrom = None
        self._ResourceConfig = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def ResourceFrom(self):
        return self._ResourceFrom

    @ResourceFrom.setter
    def ResourceFrom(self, ResourceFrom):
        self._ResourceFrom = ResourceFrom

    @property
    def ResourceConfig(self):
        return self._ResourceConfig

    @ResourceConfig.setter
    def ResourceConfig(self, ResourceConfig):
        self._ResourceConfig = ResourceConfig


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceId = params.get("ResourceId")
        self._SourceChannel = params.get("SourceChannel")
        self._ResourceFrom = params.get("ResourceFrom")
        self._ResourceConfig = params.get("ResourceConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceResponse(AbstractModel):
    """CreateResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 成功与否
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CronHorizontalAutoscaler(AbstractModel):
    """定时伸缩策略

    """

    def __init__(self):
        r"""
        :param _Name: 定时伸缩策略名称
        :type Name: str
        :param _Period: 策略周期
* * *，三个范围，第一个是天，第二个是月，第三个是周，中间用空格隔开
例子：
* * * （每天）
* * 0-3 （每周日到周三）
1,11,21 * *（每个月1号，11号，21号）
        :type Period: str
        :param _Schedules: 定时伸缩策略明细
        :type Schedules: list of CronHorizontalAutoscalerSchedule
        :param _Enabled: 是否启用
        :type Enabled: bool
        :param _Priority: 策略优先级，值越大优先级越高，0为最小值
        :type Priority: int
        """
        self._Name = None
        self._Period = None
        self._Schedules = None
        self._Enabled = None
        self._Priority = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Schedules(self):
        return self._Schedules

    @Schedules.setter
    def Schedules(self, Schedules):
        self._Schedules = Schedules

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Period = params.get("Period")
        if params.get("Schedules") is not None:
            self._Schedules = []
            for item in params.get("Schedules"):
                obj = CronHorizontalAutoscalerSchedule()
                obj._deserialize(item)
                self._Schedules.append(obj)
        self._Enabled = params.get("Enabled")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CronHorizontalAutoscalerSchedule(AbstractModel):
    """定时伸缩策略明细

    """

    def __init__(self):
        r"""
        :param _StartAt: 触发事件，小时分钟，用:分割
例如
00:00（零点零分触发）
        :type StartAt: str
        :param _TargetReplicas: 目标实例数（不大于50）
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetReplicas: int
        """
        self._StartAt = None
        self._TargetReplicas = None

    @property
    def StartAt(self):
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def TargetReplicas(self):
        return self._TargetReplicas

    @TargetReplicas.setter
    def TargetReplicas(self, TargetReplicas):
        self._TargetReplicas = TargetReplicas


    def _deserialize(self, params):
        self._StartAt = params.get("StartAt")
        self._TargetReplicas = params.get("TargetReplicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationAutoscalerRequest(AbstractModel):
    """DeleteApplicationAutoscaler请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _AutoscalerId: 弹性伸缩策略ID
        :type AutoscalerId: str
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._AutoscalerId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def AutoscalerId(self):
        return self._AutoscalerId

    @AutoscalerId.setter
    def AutoscalerId(self, AutoscalerId):
        self._AutoscalerId = AutoscalerId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationAutoscalerResponse(AbstractModel):
    """DeleteApplicationAutoscaler返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteApplicationRequest(AbstractModel):
    """DeleteApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务Id
        :type ApplicationId: str
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _DeleteApplicationIfNoRunningVersion: 当服务没有任何运行版本时，是否删除此服务
        :type DeleteApplicationIfNoRunningVersion: bool
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._DeleteApplicationIfNoRunningVersion = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def DeleteApplicationIfNoRunningVersion(self):
        return self._DeleteApplicationIfNoRunningVersion

    @DeleteApplicationIfNoRunningVersion.setter
    def DeleteApplicationIfNoRunningVersion(self, DeleteApplicationIfNoRunningVersion):
        self._DeleteApplicationIfNoRunningVersion = DeleteApplicationIfNoRunningVersion


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._DeleteApplicationIfNoRunningVersion = params.get("DeleteApplicationIfNoRunningVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationResponse(AbstractModel):
    """DeleteApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteApplicationServiceRequest(AbstractModel):
    """DeleteApplicationService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _ServiceName: 访问方式服务名
        :type ServiceName: str
        """
        self._ApplicationId = None
        self._SourceChannel = None
        self._EnvironmentId = None
        self._ServiceName = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._SourceChannel = params.get("SourceChannel")
        self._EnvironmentId = params.get("EnvironmentId")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationServiceResponse(AbstractModel):
    """DeleteApplicationService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteIngressRequest(AbstractModel):
    """DeleteIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _ClusterNamespace: 环境 namespace
        :type ClusterNamespace: str
        :param _IngressName: ingress 规则名
        :type IngressName: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._ClusterNamespace = None
        self._IngressName = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterNamespace(self):
        return self._ClusterNamespace

    @ClusterNamespace.setter
    def ClusterNamespace(self, ClusterNamespace):
        self._ClusterNamespace = ClusterNamespace

    @property
    def IngressName(self):
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterNamespace = params.get("ClusterNamespace")
        self._IngressName = params.get("IngressName")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIngressResponse(AbstractModel):
    """DeleteIngress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否删除成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeployApplicationRequest(AbstractModel):
    """DeployApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _InitPodNum: 初始化 pod 数
        :type InitPodNum: int
        :param _CpuSpec: cpu规格
        :type CpuSpec: float
        :param _MemorySpec: 内存规格
        :type MemorySpec: float
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _ImgRepo: 镜像仓库
        :type ImgRepo: str
        :param _VersionDesc: 版本描述信息
        :type VersionDesc: str
        :param _JvmOpts: 启动参数
        :type JvmOpts: str
        :param _EsInfo: 弹性伸缩配置（已废弃，请使用HorizontalAutoscaler设置弹性策略）
        :type EsInfo: :class:`tencentcloud.tem.v20210701.models.EsInfo`
        :param _EnvConf: 环境变量配置
        :type EnvConf: list of Pair
        :param _LogConfs: 日志配置
        :type LogConfs: list of str
        :param _StorageConfs: 数据卷配置
        :type StorageConfs: list of StorageConf
        :param _StorageMountConfs: 数据卷挂载配置
        :type StorageMountConfs: list of StorageMountConf
        :param _DeployMode: 部署类型。
- JAR：通过 jar 包部署
- WAR：通过 war 包部署
- IMAGE：通过镜像部署
        :type DeployMode: str
        :param _DeployVersion: 部署类型为 IMAGE 时，该参数表示镜像 tag。
部署类型为 JAR/WAR 时，该参数表示包版本号。
        :type DeployVersion: str
        :param _PkgName: 包名。使用 JAR 包或者 WAR 包部署的时候必填。
        :type PkgName: str
        :param _JdkVersion: JDK 版本。
- KONA:8：使用 kona jdk 8。
- OPEN:8：使用 open jdk 8。
- KONA:11：使用 kona jdk 11。
- OPEN:11：使用 open jdk 11。
        :type JdkVersion: str
        :param _SecurityGroupIds: 安全组ID s
        :type SecurityGroupIds: list of str
        :param _LogOutputConf: 日志输出配置
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _Description: 版本描述
        :type Description: str
        :param _ImageCommand: 镜像命令
        :type ImageCommand: str
        :param _ImageArgs: 镜像命令参数
        :type ImageArgs: list of str
        :param _UseRegistryDefaultConfig: 是否添加默认注册中心配置
        :type UseRegistryDefaultConfig: bool
        :param _SettingConfs: 挂载配置信息
        :type SettingConfs: list of MountedSettingConf
        :param _Service: 应用访问设置
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param _VersionId: 要回滚到的历史版本id
        :type VersionId: str
        :param _PostStart: 启动后执行的脚本
        :type PostStart: str
        :param _PreStop: 停止前执行的脚本
        :type PreStop: str
        :param _Liveness: 存活探针配置
        :type Liveness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _Readiness: 就绪探针配置
        :type Readiness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _DeployStrategyConf: 分批发布策略配置
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`
        :param _HorizontalAutoscaler: 弹性策略（已弃用，请使用弹性伸缩策略组合相关接口）
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param _CronHorizontalAutoscaler: 定时弹性策略（已弃用，请使用弹性伸缩策略组合相关接口）
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param _LogEnable: 是否启用log，1为启用，0为不启用
        :type LogEnable: int
        :param _ConfEdited: （除开镜像配置）配置是否修改
        :type ConfEdited: bool
        :param _SpeedUp: 是否开启应用加速
        :type SpeedUp: bool
        :param _StartupProbe: 启动探针配置
        :type StartupProbe: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _OsFlavour: 操作系统版本；
当选择openjdk时，可选参数：
- ALPINE
- CENTOS
当选择konajdk时，可选参数：
- ALPINE
- TENCENTOS
        :type OsFlavour: str
        :param _EnablePrometheusConf: metrics业务指标监控配置
        :type EnablePrometheusConf: :class:`tencentcloud.tem.v20210701.models.EnablePrometheusConf`
        :param _EnableTracing: 1：开始自动apm采集（skywalking）；
0：关闭apm采集；
        :type EnableTracing: int
        :param _EnableMetrics: 1：开始自动metrics采集（open-telemetry）；
0：关闭metrics采集；
        :type EnableMetrics: int
        :param _TcrInstanceId: 镜像部署时，选择的tcr实例id
        :type TcrInstanceId: str
        :param _RepoServer: 镜像部署时，选择的镜像服务器地址
        :type RepoServer: str
        :param _RepoType: 镜像部署时，仓库类型：0：个人仓库；1：企业版；2：公共仓库；3：tem托管仓库；4：demo仓库
        :type RepoType: int
        """
        self._ApplicationId = None
        self._InitPodNum = None
        self._CpuSpec = None
        self._MemorySpec = None
        self._EnvironmentId = None
        self._ImgRepo = None
        self._VersionDesc = None
        self._JvmOpts = None
        self._EsInfo = None
        self._EnvConf = None
        self._LogConfs = None
        self._StorageConfs = None
        self._StorageMountConfs = None
        self._DeployMode = None
        self._DeployVersion = None
        self._PkgName = None
        self._JdkVersion = None
        self._SecurityGroupIds = None
        self._LogOutputConf = None
        self._SourceChannel = None
        self._Description = None
        self._ImageCommand = None
        self._ImageArgs = None
        self._UseRegistryDefaultConfig = None
        self._SettingConfs = None
        self._Service = None
        self._VersionId = None
        self._PostStart = None
        self._PreStop = None
        self._Liveness = None
        self._Readiness = None
        self._DeployStrategyConf = None
        self._HorizontalAutoscaler = None
        self._CronHorizontalAutoscaler = None
        self._LogEnable = None
        self._ConfEdited = None
        self._SpeedUp = None
        self._StartupProbe = None
        self._OsFlavour = None
        self._EnablePrometheusConf = None
        self._EnableTracing = None
        self._EnableMetrics = None
        self._TcrInstanceId = None
        self._RepoServer = None
        self._RepoType = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def InitPodNum(self):
        return self._InitPodNum

    @InitPodNum.setter
    def InitPodNum(self, InitPodNum):
        self._InitPodNum = InitPodNum

    @property
    def CpuSpec(self):
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def MemorySpec(self):
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ImgRepo(self):
        return self._ImgRepo

    @ImgRepo.setter
    def ImgRepo(self, ImgRepo):
        self._ImgRepo = ImgRepo

    @property
    def VersionDesc(self):
        return self._VersionDesc

    @VersionDesc.setter
    def VersionDesc(self, VersionDesc):
        self._VersionDesc = VersionDesc

    @property
    def JvmOpts(self):
        return self._JvmOpts

    @JvmOpts.setter
    def JvmOpts(self, JvmOpts):
        self._JvmOpts = JvmOpts

    @property
    def EsInfo(self):
        return self._EsInfo

    @EsInfo.setter
    def EsInfo(self, EsInfo):
        self._EsInfo = EsInfo

    @property
    def EnvConf(self):
        return self._EnvConf

    @EnvConf.setter
    def EnvConf(self, EnvConf):
        self._EnvConf = EnvConf

    @property
    def LogConfs(self):
        return self._LogConfs

    @LogConfs.setter
    def LogConfs(self, LogConfs):
        self._LogConfs = LogConfs

    @property
    def StorageConfs(self):
        return self._StorageConfs

    @StorageConfs.setter
    def StorageConfs(self, StorageConfs):
        self._StorageConfs = StorageConfs

    @property
    def StorageMountConfs(self):
        return self._StorageMountConfs

    @StorageMountConfs.setter
    def StorageMountConfs(self, StorageMountConfs):
        self._StorageMountConfs = StorageMountConfs

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def DeployVersion(self):
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def PkgName(self):
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def JdkVersion(self):
        return self._JdkVersion

    @JdkVersion.setter
    def JdkVersion(self, JdkVersion):
        self._JdkVersion = JdkVersion

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def LogOutputConf(self):
        return self._LogOutputConf

    @LogOutputConf.setter
    def LogOutputConf(self, LogOutputConf):
        self._LogOutputConf = LogOutputConf

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ImageCommand(self):
        return self._ImageCommand

    @ImageCommand.setter
    def ImageCommand(self, ImageCommand):
        self._ImageCommand = ImageCommand

    @property
    def ImageArgs(self):
        return self._ImageArgs

    @ImageArgs.setter
    def ImageArgs(self, ImageArgs):
        self._ImageArgs = ImageArgs

    @property
    def UseRegistryDefaultConfig(self):
        return self._UseRegistryDefaultConfig

    @UseRegistryDefaultConfig.setter
    def UseRegistryDefaultConfig(self, UseRegistryDefaultConfig):
        self._UseRegistryDefaultConfig = UseRegistryDefaultConfig

    @property
    def SettingConfs(self):
        return self._SettingConfs

    @SettingConfs.setter
    def SettingConfs(self, SettingConfs):
        self._SettingConfs = SettingConfs

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def PostStart(self):
        return self._PostStart

    @PostStart.setter
    def PostStart(self, PostStart):
        self._PostStart = PostStart

    @property
    def PreStop(self):
        return self._PreStop

    @PreStop.setter
    def PreStop(self, PreStop):
        self._PreStop = PreStop

    @property
    def Liveness(self):
        return self._Liveness

    @Liveness.setter
    def Liveness(self, Liveness):
        self._Liveness = Liveness

    @property
    def Readiness(self):
        return self._Readiness

    @Readiness.setter
    def Readiness(self, Readiness):
        self._Readiness = Readiness

    @property
    def DeployStrategyConf(self):
        return self._DeployStrategyConf

    @DeployStrategyConf.setter
    def DeployStrategyConf(self, DeployStrategyConf):
        self._DeployStrategyConf = DeployStrategyConf

    @property
    def HorizontalAutoscaler(self):
        return self._HorizontalAutoscaler

    @HorizontalAutoscaler.setter
    def HorizontalAutoscaler(self, HorizontalAutoscaler):
        self._HorizontalAutoscaler = HorizontalAutoscaler

    @property
    def CronHorizontalAutoscaler(self):
        return self._CronHorizontalAutoscaler

    @CronHorizontalAutoscaler.setter
    def CronHorizontalAutoscaler(self, CronHorizontalAutoscaler):
        self._CronHorizontalAutoscaler = CronHorizontalAutoscaler

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def ConfEdited(self):
        return self._ConfEdited

    @ConfEdited.setter
    def ConfEdited(self, ConfEdited):
        self._ConfEdited = ConfEdited

    @property
    def SpeedUp(self):
        return self._SpeedUp

    @SpeedUp.setter
    def SpeedUp(self, SpeedUp):
        self._SpeedUp = SpeedUp

    @property
    def StartupProbe(self):
        return self._StartupProbe

    @StartupProbe.setter
    def StartupProbe(self, StartupProbe):
        self._StartupProbe = StartupProbe

    @property
    def OsFlavour(self):
        return self._OsFlavour

    @OsFlavour.setter
    def OsFlavour(self, OsFlavour):
        self._OsFlavour = OsFlavour

    @property
    def EnablePrometheusConf(self):
        return self._EnablePrometheusConf

    @EnablePrometheusConf.setter
    def EnablePrometheusConf(self, EnablePrometheusConf):
        self._EnablePrometheusConf = EnablePrometheusConf

    @property
    def EnableTracing(self):
        return self._EnableTracing

    @EnableTracing.setter
    def EnableTracing(self, EnableTracing):
        self._EnableTracing = EnableTracing

    @property
    def EnableMetrics(self):
        return self._EnableMetrics

    @EnableMetrics.setter
    def EnableMetrics(self, EnableMetrics):
        self._EnableMetrics = EnableMetrics

    @property
    def TcrInstanceId(self):
        return self._TcrInstanceId

    @TcrInstanceId.setter
    def TcrInstanceId(self, TcrInstanceId):
        self._TcrInstanceId = TcrInstanceId

    @property
    def RepoServer(self):
        return self._RepoServer

    @RepoServer.setter
    def RepoServer(self, RepoServer):
        self._RepoServer = RepoServer

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._InitPodNum = params.get("InitPodNum")
        self._CpuSpec = params.get("CpuSpec")
        self._MemorySpec = params.get("MemorySpec")
        self._EnvironmentId = params.get("EnvironmentId")
        self._ImgRepo = params.get("ImgRepo")
        self._VersionDesc = params.get("VersionDesc")
        self._JvmOpts = params.get("JvmOpts")
        if params.get("EsInfo") is not None:
            self._EsInfo = EsInfo()
            self._EsInfo._deserialize(params.get("EsInfo"))
        if params.get("EnvConf") is not None:
            self._EnvConf = []
            for item in params.get("EnvConf"):
                obj = Pair()
                obj._deserialize(item)
                self._EnvConf.append(obj)
        self._LogConfs = params.get("LogConfs")
        if params.get("StorageConfs") is not None:
            self._StorageConfs = []
            for item in params.get("StorageConfs"):
                obj = StorageConf()
                obj._deserialize(item)
                self._StorageConfs.append(obj)
        if params.get("StorageMountConfs") is not None:
            self._StorageMountConfs = []
            for item in params.get("StorageMountConfs"):
                obj = StorageMountConf()
                obj._deserialize(item)
                self._StorageMountConfs.append(obj)
        self._DeployMode = params.get("DeployMode")
        self._DeployVersion = params.get("DeployVersion")
        self._PkgName = params.get("PkgName")
        self._JdkVersion = params.get("JdkVersion")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LogOutputConf") is not None:
            self._LogOutputConf = LogOutputConf()
            self._LogOutputConf._deserialize(params.get("LogOutputConf"))
        self._SourceChannel = params.get("SourceChannel")
        self._Description = params.get("Description")
        self._ImageCommand = params.get("ImageCommand")
        self._ImageArgs = params.get("ImageArgs")
        self._UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("SettingConfs") is not None:
            self._SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self._SettingConfs.append(obj)
        if params.get("Service") is not None:
            self._Service = EksService()
            self._Service._deserialize(params.get("Service"))
        self._VersionId = params.get("VersionId")
        self._PostStart = params.get("PostStart")
        self._PreStop = params.get("PreStop")
        if params.get("Liveness") is not None:
            self._Liveness = HealthCheckConfig()
            self._Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self._Readiness = HealthCheckConfig()
            self._Readiness._deserialize(params.get("Readiness"))
        if params.get("DeployStrategyConf") is not None:
            self._DeployStrategyConf = DeployStrategyConf()
            self._DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("HorizontalAutoscaler") is not None:
            self._HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self._HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self._CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self._CronHorizontalAutoscaler.append(obj)
        self._LogEnable = params.get("LogEnable")
        self._ConfEdited = params.get("ConfEdited")
        self._SpeedUp = params.get("SpeedUp")
        if params.get("StartupProbe") is not None:
            self._StartupProbe = HealthCheckConfig()
            self._StartupProbe._deserialize(params.get("StartupProbe"))
        self._OsFlavour = params.get("OsFlavour")
        if params.get("EnablePrometheusConf") is not None:
            self._EnablePrometheusConf = EnablePrometheusConf()
            self._EnablePrometheusConf._deserialize(params.get("EnablePrometheusConf"))
        self._EnableTracing = params.get("EnableTracing")
        self._EnableMetrics = params.get("EnableMetrics")
        self._TcrInstanceId = params.get("TcrInstanceId")
        self._RepoServer = params.get("RepoServer")
        self._RepoType = params.get("RepoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployApplicationResponse(AbstractModel):
    """DeployApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 版本ID（前端可忽略）
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeployServiceBatchDetail(AbstractModel):
    """分批发布单批次详情

    """

    def __init__(self):
        r"""
        :param _OldPodList: 旧实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OldPodList: :class:`tencentcloud.tem.v20210701.models.DeployServicePodDetail`
        :param _NewPodList: 新实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NewPodList: :class:`tencentcloud.tem.v20210701.models.DeployServicePodDetail`
        :param _BatchStatus: 当前批次状态："WaitForTimeExceed", "WaitForResume", "Deploying", "Finish", "NotStart"
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchStatus: str
        :param _PodNum: 该批次预计旧实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PodNum: int
        :param _BatchIndex: 批次id
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchIndex: int
        :param _OldPods: 旧实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OldPods: list of DeployServicePodDetail
        :param _NewPods: 新实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NewPods: list of DeployServicePodDetail
        :param _NextBatchStartTime: =0：手动确认批次；>0：下一批次开始时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type NextBatchStartTime: int
        """
        self._OldPodList = None
        self._NewPodList = None
        self._BatchStatus = None
        self._PodNum = None
        self._BatchIndex = None
        self._OldPods = None
        self._NewPods = None
        self._NextBatchStartTime = None

    @property
    def OldPodList(self):
        return self._OldPodList

    @OldPodList.setter
    def OldPodList(self, OldPodList):
        self._OldPodList = OldPodList

    @property
    def NewPodList(self):
        return self._NewPodList

    @NewPodList.setter
    def NewPodList(self, NewPodList):
        self._NewPodList = NewPodList

    @property
    def BatchStatus(self):
        return self._BatchStatus

    @BatchStatus.setter
    def BatchStatus(self, BatchStatus):
        self._BatchStatus = BatchStatus

    @property
    def PodNum(self):
        return self._PodNum

    @PodNum.setter
    def PodNum(self, PodNum):
        self._PodNum = PodNum

    @property
    def BatchIndex(self):
        return self._BatchIndex

    @BatchIndex.setter
    def BatchIndex(self, BatchIndex):
        self._BatchIndex = BatchIndex

    @property
    def OldPods(self):
        return self._OldPods

    @OldPods.setter
    def OldPods(self, OldPods):
        self._OldPods = OldPods

    @property
    def NewPods(self):
        return self._NewPods

    @NewPods.setter
    def NewPods(self, NewPods):
        self._NewPods = NewPods

    @property
    def NextBatchStartTime(self):
        return self._NextBatchStartTime

    @NextBatchStartTime.setter
    def NextBatchStartTime(self, NextBatchStartTime):
        self._NextBatchStartTime = NextBatchStartTime


    def _deserialize(self, params):
        if params.get("OldPodList") is not None:
            self._OldPodList = DeployServicePodDetail()
            self._OldPodList._deserialize(params.get("OldPodList"))
        if params.get("NewPodList") is not None:
            self._NewPodList = DeployServicePodDetail()
            self._NewPodList._deserialize(params.get("NewPodList"))
        self._BatchStatus = params.get("BatchStatus")
        self._PodNum = params.get("PodNum")
        self._BatchIndex = params.get("BatchIndex")
        if params.get("OldPods") is not None:
            self._OldPods = []
            for item in params.get("OldPods"):
                obj = DeployServicePodDetail()
                obj._deserialize(item)
                self._OldPods.append(obj)
        if params.get("NewPods") is not None:
            self._NewPods = []
            for item in params.get("NewPods"):
                obj = DeployServicePodDetail()
                obj._deserialize(item)
                self._NewPods.append(obj)
        self._NextBatchStartTime = params.get("NextBatchStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployServicePodDetail(AbstractModel):
    """分批发布单批次详情

    """

    def __init__(self):
        r"""
        :param _PodId: pod Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PodId: str
        :param _PodStatus: pod状态
注意：此字段可能返回 null，表示取不到有效值。
        :type PodStatus: list of str
        :param _PodVersion: pod版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PodVersion: str
        :param _CreateTime: pod创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Zone: pod所在可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _Webshell: webshell地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Webshell: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._PodId = None
        self._PodStatus = None
        self._PodVersion = None
        self._CreateTime = None
        self._Zone = None
        self._Webshell = None
        self._Status = None

    @property
    def PodId(self):
        return self._PodId

    @PodId.setter
    def PodId(self, PodId):
        self._PodId = PodId

    @property
    def PodStatus(self):
        return self._PodStatus

    @PodStatus.setter
    def PodStatus(self, PodStatus):
        self._PodStatus = PodStatus

    @property
    def PodVersion(self):
        return self._PodVersion

    @PodVersion.setter
    def PodVersion(self, PodVersion):
        self._PodVersion = PodVersion

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Webshell(self):
        return self._Webshell

    @Webshell.setter
    def Webshell(self, Webshell):
        self._Webshell = Webshell

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PodId = params.get("PodId")
        self._PodStatus = params.get("PodStatus")
        self._PodVersion = params.get("PodVersion")
        self._CreateTime = params.get("CreateTime")
        self._Zone = params.get("Zone")
        self._Webshell = params.get("Webshell")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployStrategyConf(AbstractModel):
    """分批发布策略配置

    """

    def __init__(self):
        r"""
        :param _TotalBatchCount: 总分批数
        :type TotalBatchCount: int
        :param _BetaBatchNum: beta分批实例数
        :type BetaBatchNum: int
        :param _DeployStrategyType: 分批策略：0-全自动，1-全手动，2-beta分批，beta批一定是手动的，3-首次发布
        :type DeployStrategyType: int
        :param _BatchInterval: 每批暂停间隔
        :type BatchInterval: int
        :param _MinAvailable: 最小可用实例数
        :type MinAvailable: int
        :param _Force: 是否强制发布
        :type Force: bool
        """
        self._TotalBatchCount = None
        self._BetaBatchNum = None
        self._DeployStrategyType = None
        self._BatchInterval = None
        self._MinAvailable = None
        self._Force = None

    @property
    def TotalBatchCount(self):
        return self._TotalBatchCount

    @TotalBatchCount.setter
    def TotalBatchCount(self, TotalBatchCount):
        self._TotalBatchCount = TotalBatchCount

    @property
    def BetaBatchNum(self):
        return self._BetaBatchNum

    @BetaBatchNum.setter
    def BetaBatchNum(self, BetaBatchNum):
        self._BetaBatchNum = BetaBatchNum

    @property
    def DeployStrategyType(self):
        return self._DeployStrategyType

    @DeployStrategyType.setter
    def DeployStrategyType(self, DeployStrategyType):
        self._DeployStrategyType = DeployStrategyType

    @property
    def BatchInterval(self):
        return self._BatchInterval

    @BatchInterval.setter
    def BatchInterval(self, BatchInterval):
        self._BatchInterval = BatchInterval

    @property
    def MinAvailable(self):
        return self._MinAvailable

    @MinAvailable.setter
    def MinAvailable(self, MinAvailable):
        self._MinAvailable = MinAvailable

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._TotalBatchCount = params.get("TotalBatchCount")
        self._BetaBatchNum = params.get("BetaBatchNum")
        self._DeployStrategyType = params.get("DeployStrategyType")
        self._BatchInterval = params.get("BatchInterval")
        self._MinAvailable = params.get("MinAvailable")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationAutoscalerListRequest(AbstractModel):
    """DescribeApplicationAutoscalerList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationAutoscalerListResponse(AbstractModel):
    """DescribeApplicationAutoscalerList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 弹性伸缩策略组合
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of Autoscaler
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = Autoscaler()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApplicationInfoRequest(AbstractModel):
    """DescribeApplicationInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务版本ID
        :type ApplicationId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        """
        self._ApplicationId = None
        self._SourceChannel = None
        self._EnvironmentId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._SourceChannel = params.get("SourceChannel")
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationInfoResponse(AbstractModel):
    """DescribeApplicationInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20210701.models.TemServiceVersionInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = TemServiceVersionInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationPodsRequest(AbstractModel):
    """DescribeApplicationPods请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境id
        :type EnvironmentId: str
        :param _ApplicationId: 应用id
        :type ApplicationId: str
        :param _Limit: 单页条数，默认值20
        :type Limit: int
        :param _Offset: 分页下标，默认值0
        :type Offset: int
        :param _Status: 实例状态 
- Running 
- Pending 
- Error
        :type Status: str
        :param _PodName: 实例名字
        :type PodName: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._ApplicationId = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._PodName = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ApplicationId = params.get("ApplicationId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._PodName = params.get("PodName")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationPodsResponse(AbstractModel):
    """DescribeApplicationPods返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeRunPodPage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationServiceListRequest(AbstractModel):
    """DescribeApplicationServiceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: namespace id
        :type EnvironmentId: str
        :param _ApplicationId: 服务ID
        :type ApplicationId: str
        :param _SourceChannel: xx
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._ApplicationId = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ApplicationId = params.get("ApplicationId")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationServiceListResponse(AbstractModel):
    """DescribeApplicationServiceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 应用 EKS Service 列表
        :type Result: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = EksService()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationsRequest(AbstractModel):
    """DescribeApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 命名空间ID
        :type EnvironmentId: str
        :param _Limit: 分页Limit
        :type Limit: int
        :param _Offset: 分页offset
        :type Offset: int
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _Keyword: 搜索关键字
        :type Keyword: str
        :param _Filters: 查询过滤器
        :type Filters: list of QueryFilter
        :param _SortInfo: 排序字段
        :type SortInfo: :class:`tencentcloud.tem.v20210701.models.SortType`
        """
        self._EnvironmentId = None
        self._Limit = None
        self._Offset = None
        self._SourceChannel = None
        self._ApplicationId = None
        self._Keyword = None
        self._Filters = None
        self._SortInfo = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortInfo(self):
        return self._SortInfo

    @SortInfo.setter
    def SortInfo(self, SortInfo):
        self._SortInfo = SortInfo


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SourceChannel = params.get("SourceChannel")
        self._ApplicationId = params.get("ApplicationId")
        self._Keyword = params.get("Keyword")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("SortInfo") is not None:
            self._SortInfo = SortType()
            self._SortInfo._deserialize(params.get("SortInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsResponse(AbstractModel):
    """DescribeApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20210701.models.ServicePage`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServicePage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationsStatusRequest(AbstractModel):
    """DescribeApplicationsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        """
        self._SourceChannel = None
        self._EnvironmentId = None

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._SourceChannel = params.get("SourceChannel")
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsStatusResponse(AbstractModel):
    """DescribeApplicationsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: list of ServiceVersionBrief
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ServiceVersionBrief()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigDataListPage(AbstractModel):
    """配置信息的分页列表

    """

    def __init__(self):
        r"""
        :param _Records: 记录
        :type Records: list of ConfigData
        :param _ContinueToken: 分页游标，用以查询下一页
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinueToken: str
        :param _RemainingCount: 剩余数目
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainingCount: int
        """
        self._Records = None
        self._ContinueToken = None
        self._RemainingCount = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def ContinueToken(self):
        return self._ContinueToken

    @ContinueToken.setter
    def ContinueToken(self, ContinueToken):
        self._ContinueToken = ContinueToken

    @property
    def RemainingCount(self):
        return self._RemainingCount

    @RemainingCount.setter
    def RemainingCount(self, RemainingCount):
        self._RemainingCount = RemainingCount


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = ConfigData()
                obj._deserialize(item)
                self._Records.append(obj)
        self._ContinueToken = params.get("ContinueToken")
        self._RemainingCount = params.get("RemainingCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataListRequest(AbstractModel):
    """DescribeConfigDataList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _ContinueToken: 查询游标
        :type ContinueToken: str
        :param _Limit: 分页 limit
        :type Limit: int
        """
        self._EnvironmentId = None
        self._SourceChannel = None
        self._ContinueToken = None
        self._Limit = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def ContinueToken(self):
        return self._ContinueToken

    @ContinueToken.setter
    def ContinueToken(self, ContinueToken):
        self._ContinueToken = ContinueToken

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._ContinueToken = params.get("ContinueToken")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataListResponse(AbstractModel):
    """DescribeConfigDataList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 配置列表
        :type Result: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataListPage`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeConfigDataListPage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeConfigDataRequest(AbstractModel):
    """DescribeConfigData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param _Name: 配置名
        :type Name: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._Name = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataResponse(AbstractModel):
    """DescribeConfigData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 配置
        :type Result: :class:`tencentcloud.tem.v20210701.models.ConfigData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ConfigData()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDeployApplicationDetailRequest(AbstractModel):
    """DescribeDeployApplicationDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _EnvironmentId: 环境id
        :type EnvironmentId: str
        :param _VersionId: 版本部署id
        :type VersionId: str
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._VersionId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployApplicationDetailResponse(AbstractModel):
    """DescribeDeployApplicationDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 分批发布结果详情
        :type Result: :class:`tencentcloud.tem.v20210701.models.TemDeployApplicationDetailInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = TemDeployApplicationDetailInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentRequest(AbstractModel):
    """DescribeEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 命名空间id
        :type EnvironmentId: str
        :param _SourceChannel: 来源Channel
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentResponse(AbstractModel):
    """DescribeEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 环境信息
        :type Result: :class:`tencentcloud.tem.v20210701.models.NamespaceInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = NamespaceInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentStatusRequest(AbstractModel):
    """DescribeEnvironmentStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentIds: 命名空间id
        :type EnvironmentIds: list of str
        :param _SourceChannel: 来源Channel
        :type SourceChannel: int
        """
        self._EnvironmentIds = None
        self._SourceChannel = None

    @property
    def EnvironmentIds(self):
        return self._EnvironmentIds

    @EnvironmentIds.setter
    def EnvironmentIds(self, EnvironmentIds):
        self._EnvironmentIds = EnvironmentIds

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentIds = params.get("EnvironmentIds")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentStatusResponse(AbstractModel):
    """DescribeEnvironmentStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回状态列表
        :type Result: list of NamespaceStatusInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = NamespaceStatusInfo()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页limit
        :type Limit: int
        :param _Offset: 分页下标
        :type Offset: int
        :param _SourceChannel: 来源source
        :type SourceChannel: int
        :param _Filters: 查询过滤器
        :type Filters: list of QueryFilter
        :param _SortInfo: 排序字段
        :type SortInfo: :class:`tencentcloud.tem.v20210701.models.SortType`
        :param _EnvironmentId: 环境id
        :type EnvironmentId: str
        """
        self._Limit = None
        self._Offset = None
        self._SourceChannel = None
        self._Filters = None
        self._SortInfo = None
        self._EnvironmentId = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortInfo(self):
        return self._SortInfo

    @SortInfo.setter
    def SortInfo(self, SortInfo):
        self._SortInfo = SortInfo

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SourceChannel = params.get("SourceChannel")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("SortInfo") is not None:
            self._SortInfo = SortType()
            self._SortInfo._deserialize(params.get("SortInfo"))
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20210701.models.NamespacePage`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = NamespacePage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeIngressRequest(AbstractModel):
    """DescribeIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _ClusterNamespace: 环境namespace
        :type ClusterNamespace: str
        :param _IngressName: ingress 规则名
        :type IngressName: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._ClusterNamespace = None
        self._IngressName = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterNamespace(self):
        return self._ClusterNamespace

    @ClusterNamespace.setter
    def ClusterNamespace(self, ClusterNamespace):
        self._ClusterNamespace = ClusterNamespace

    @property
    def IngressName(self):
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterNamespace = params.get("ClusterNamespace")
        self._IngressName = params.get("IngressName")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressResponse(AbstractModel):
    """DescribeIngress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: Ingress 规则配置
        :type Result: :class:`tencentcloud.tem.v20210701.models.IngressInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = IngressInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeIngressesRequest(AbstractModel):
    """DescribeIngresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 id
        :type EnvironmentId: str
        :param _ClusterNamespace: 环境 namespace
        :type ClusterNamespace: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _IngressNames: ingress 规则名列表
        :type IngressNames: list of str
        """
        self._EnvironmentId = None
        self._ClusterNamespace = None
        self._SourceChannel = None
        self._IngressNames = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterNamespace(self):
        return self._ClusterNamespace

    @ClusterNamespace.setter
    def ClusterNamespace(self, ClusterNamespace):
        self._ClusterNamespace = ClusterNamespace

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def IngressNames(self):
        return self._IngressNames

    @IngressNames.setter
    def IngressNames(self, IngressNames):
        self._IngressNames = IngressNames


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterNamespace = params.get("ClusterNamespace")
        self._SourceChannel = params.get("SourceChannel")
        self._IngressNames = params.get("IngressNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressesResponse(AbstractModel):
    """DescribeIngresses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: ingress 数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of IngressInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = IngressInfo()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogConfigRequest(AbstractModel):
    """DescribeLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param _Name: 配置名
        :type Name: str
        :param _ApplicationId: 应用 ID
        :type ApplicationId: str
        """
        self._EnvironmentId = None
        self._Name = None
        self._ApplicationId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogConfigResponse(AbstractModel):
    """DescribeLogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 配置
        :type Result: :class:`tencentcloud.tem.v20210701.models.LogConfig`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = LogConfig()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePagedLogConfigListRequest(AbstractModel):
    """DescribePagedLogConfigList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param _ApplicationId: 应用 ID
        :type ApplicationId: str
        :param _ApplicationName: 应用名
        :type ApplicationName: str
        :param _Name: 规则名
        :type Name: str
        :param _Limit: 分页大小，默认 20
        :type Limit: int
        :param _ContinueToken: 翻页游标
        :type ContinueToken: str
        """
        self._EnvironmentId = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._Name = None
        self._Limit = None
        self._ContinueToken = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ContinueToken(self):
        return self._ContinueToken

    @ContinueToken.setter
    def ContinueToken(self, ContinueToken):
        self._ContinueToken = ContinueToken


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._Name = params.get("Name")
        self._Limit = params.get("Limit")
        self._ContinueToken = params.get("ContinueToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePagedLogConfigListResponse(AbstractModel):
    """DescribePagedLogConfigList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 日志收集配置列表
        :type Result: :class:`tencentcloud.tem.v20210701.models.LogConfigListPage`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = LogConfigListPage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeRelatedIngressesRequest(AbstractModel):
    """DescribeRelatedIngresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 id
        :type EnvironmentId: str
        :param _ClusterNamespace: 环境 namespace
        :type ClusterNamespace: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _ApplicationId: 应用 ID
        :type ApplicationId: str
        """
        self._EnvironmentId = None
        self._ClusterNamespace = None
        self._SourceChannel = None
        self._ApplicationId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterNamespace(self):
        return self._ClusterNamespace

    @ClusterNamespace.setter
    def ClusterNamespace(self, ClusterNamespace):
        self._ClusterNamespace = ClusterNamespace

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterNamespace = params.get("ClusterNamespace")
        self._SourceChannel = params.get("SourceChannel")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelatedIngressesResponse(AbstractModel):
    """DescribeRelatedIngresses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: ingress 数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of IngressInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = IngressInfo()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRunPodPage(AbstractModel):
    """版本pod列表

    """

    def __init__(self):
        r"""
        :param _Offset: 分页下标
        :type Offset: int
        :param _Limit: 单页条数
        :type Limit: int
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 请求id
        :type RequestId: str
        :param _PodList: 条目
        :type PodList: list of RunVersionPod
        """
        self._Offset = None
        self._Limit = None
        self._TotalCount = None
        self._RequestId = None
        self._PodList = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def PodList(self):
        return self._PodList

    @PodList.setter
    def PodList(self, PodList):
        self._PodList = PodList


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")
        if params.get("PodList") is not None:
            self._PodList = []
            for item in params.get("PodList"):
                obj = RunVersionPod()
                obj._deserialize(item)
                self._PodList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyConfigDataRequest(AbstractModel):
    """DestroyConfigData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param _Name: 配置名
        :type Name: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._Name = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyConfigDataResponse(AbstractModel):
    """DestroyConfigData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DestroyEnvironmentRequest(AbstractModel):
    """DestroyEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 命名空间ID
        :type EnvironmentId: str
        :param _SourceChannel: Namespace
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyEnvironmentResponse(AbstractModel):
    """DestroyEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DestroyLogConfigRequest(AbstractModel):
    """DestroyLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param _Name: 配置名
        :type Name: str
        :param _ApplicationId: 应用 ID
        :type ApplicationId: str
        """
        self._EnvironmentId = None
        self._Name = None
        self._ApplicationId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyLogConfigResponse(AbstractModel):
    """DestroyLogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DisableApplicationAutoscalerRequest(AbstractModel):
    """DisableApplicationAutoscaler请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _AutoscalerId: 弹性伸缩策略ID
        :type AutoscalerId: str
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._AutoscalerId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def AutoscalerId(self):
        return self._AutoscalerId

    @AutoscalerId.setter
    def AutoscalerId(self, AutoscalerId):
        self._AutoscalerId = AutoscalerId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableApplicationAutoscalerResponse(AbstractModel):
    """DisableApplicationAutoscaler返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class EksService(AbstractModel):
    """eks service info

    """

    def __init__(self):
        r"""
        :param _Name: service name
        :type Name: str
        :param _Ports: 可用端口
        :type Ports: list of int
        :param _Yaml: yaml 内容
        :type Yaml: str
        :param _ApplicationName: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param _VersionName: 版本名
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _ClusterIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIp: list of str
        :param _ExternalIp: 外网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalIp: str
        :param _Type: 访问类型，可选值：
- EXTERNAL（公网访问）
- VPC（vpc内访问）
- CLUSTER（集群内访问）
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _SubnetId: 子网ID，只在类型为vpc访问时才有值
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _LoadBalanceId: 负载均衡ID，只在外网访问和vpc内访问才有值，默认自动创建
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalanceId: str
        :param _PortMappings: 端口映射
注意：此字段可能返回 null，表示取不到有效值。
        :type PortMappings: list of PortMapping
        :param _ServicePortMappingList: 每种类型访问配置详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ServicePortMappingList: list of ServicePortMapping
        :param _FlushAll: 刷新复写所有类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FlushAll: bool
        :param _EnableRegistryNextDeploy: 1: 下次部署自动注入注册中心信息；0：不注入
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableRegistryNextDeploy: int
        :param _ApplicationId: 返回应用id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param _AllIpDone: 所有服务IP是否已经ready
注意：此字段可能返回 null，表示取不到有效值。
        :type AllIpDone: bool
        :param _ExternalDomain: clb 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalDomain: str
        """
        self._Name = None
        self._Ports = None
        self._Yaml = None
        self._ApplicationName = None
        self._VersionName = None
        self._ClusterIp = None
        self._ExternalIp = None
        self._Type = None
        self._SubnetId = None
        self._LoadBalanceId = None
        self._PortMappings = None
        self._ServicePortMappingList = None
        self._FlushAll = None
        self._EnableRegistryNextDeploy = None
        self._ApplicationId = None
        self._AllIpDone = None
        self._ExternalDomain = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def ClusterIp(self):
        return self._ClusterIp

    @ClusterIp.setter
    def ClusterIp(self, ClusterIp):
        self._ClusterIp = ClusterIp

    @property
    def ExternalIp(self):
        return self._ExternalIp

    @ExternalIp.setter
    def ExternalIp(self, ExternalIp):
        self._ExternalIp = ExternalIp

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def LoadBalanceId(self):
        return self._LoadBalanceId

    @LoadBalanceId.setter
    def LoadBalanceId(self, LoadBalanceId):
        self._LoadBalanceId = LoadBalanceId

    @property
    def PortMappings(self):
        return self._PortMappings

    @PortMappings.setter
    def PortMappings(self, PortMappings):
        self._PortMappings = PortMappings

    @property
    def ServicePortMappingList(self):
        return self._ServicePortMappingList

    @ServicePortMappingList.setter
    def ServicePortMappingList(self, ServicePortMappingList):
        self._ServicePortMappingList = ServicePortMappingList

    @property
    def FlushAll(self):
        return self._FlushAll

    @FlushAll.setter
    def FlushAll(self, FlushAll):
        self._FlushAll = FlushAll

    @property
    def EnableRegistryNextDeploy(self):
        return self._EnableRegistryNextDeploy

    @EnableRegistryNextDeploy.setter
    def EnableRegistryNextDeploy(self, EnableRegistryNextDeploy):
        self._EnableRegistryNextDeploy = EnableRegistryNextDeploy

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AllIpDone(self):
        return self._AllIpDone

    @AllIpDone.setter
    def AllIpDone(self, AllIpDone):
        self._AllIpDone = AllIpDone

    @property
    def ExternalDomain(self):
        return self._ExternalDomain

    @ExternalDomain.setter
    def ExternalDomain(self, ExternalDomain):
        self._ExternalDomain = ExternalDomain


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Ports = params.get("Ports")
        self._Yaml = params.get("Yaml")
        self._ApplicationName = params.get("ApplicationName")
        self._VersionName = params.get("VersionName")
        self._ClusterIp = params.get("ClusterIp")
        self._ExternalIp = params.get("ExternalIp")
        self._Type = params.get("Type")
        self._SubnetId = params.get("SubnetId")
        self._LoadBalanceId = params.get("LoadBalanceId")
        if params.get("PortMappings") is not None:
            self._PortMappings = []
            for item in params.get("PortMappings"):
                obj = PortMapping()
                obj._deserialize(item)
                self._PortMappings.append(obj)
        if params.get("ServicePortMappingList") is not None:
            self._ServicePortMappingList = []
            for item in params.get("ServicePortMappingList"):
                obj = ServicePortMapping()
                obj._deserialize(item)
                self._ServicePortMappingList.append(obj)
        self._FlushAll = params.get("FlushAll")
        self._EnableRegistryNextDeploy = params.get("EnableRegistryNextDeploy")
        self._ApplicationId = params.get("ApplicationId")
        self._AllIpDone = params.get("AllIpDone")
        self._ExternalDomain = params.get("ExternalDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApplicationAutoscalerRequest(AbstractModel):
    """EnableApplicationAutoscaler请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _AutoscalerId: 弹性伸缩策略ID
        :type AutoscalerId: str
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._AutoscalerId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def AutoscalerId(self):
        return self._AutoscalerId

    @AutoscalerId.setter
    def AutoscalerId(self, AutoscalerId):
        self._AutoscalerId = AutoscalerId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApplicationAutoscalerResponse(AbstractModel):
    """EnableApplicationAutoscaler返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class EnablePrometheusConf(AbstractModel):
    """开启prometheus监控配置

    """

    def __init__(self):
        r"""
        :param _Port: 应用开放的监听端口
        :type Port: int
        :param _Path: 业务指标暴露的url path
        :type Path: str
        """
        self._Port = None
        self._Path = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsInfo(AbstractModel):
    """弹性伸缩配置

    """

    def __init__(self):
        r"""
        :param _MinAliveInstances: 最小实例数
        :type MinAliveInstances: int
        :param _MaxAliveInstances: 最大实例数
        :type MaxAliveInstances: int
        :param _EsStrategy: 弹性策略,1:cpu，2:内存
        :type EsStrategy: int
        :param _Threshold: 弹性扩缩容条件值
        :type Threshold: int
        :param _VersionId: 版本Id
        :type VersionId: str
        """
        self._MinAliveInstances = None
        self._MaxAliveInstances = None
        self._EsStrategy = None
        self._Threshold = None
        self._VersionId = None

    @property
    def MinAliveInstances(self):
        return self._MinAliveInstances

    @MinAliveInstances.setter
    def MinAliveInstances(self, MinAliveInstances):
        self._MinAliveInstances = MinAliveInstances

    @property
    def MaxAliveInstances(self):
        return self._MaxAliveInstances

    @MaxAliveInstances.setter
    def MaxAliveInstances(self, MaxAliveInstances):
        self._MaxAliveInstances = MaxAliveInstances

    @property
    def EsStrategy(self):
        return self._EsStrategy

    @EsStrategy.setter
    def EsStrategy(self, EsStrategy):
        self._EsStrategy = EsStrategy

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._MinAliveInstances = params.get("MinAliveInstances")
        self._MaxAliveInstances = params.get("MaxAliveInstances")
        self._EsStrategy = params.get("EsStrategy")
        self._Threshold = params.get("Threshold")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateApplicationPackageDownloadUrlRequest(AbstractModel):
    """GenerateApplicationPackageDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _PkgName: 包名
        :type PkgName: str
        :param _DeployVersion: 需要下载的包版本
        :type DeployVersion: str
        :param _SourceChannel: 来源 channel
        :type SourceChannel: int
        """
        self._ApplicationId = None
        self._PkgName = None
        self._DeployVersion = None
        self._SourceChannel = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PkgName(self):
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def DeployVersion(self):
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._PkgName = params.get("PkgName")
        self._DeployVersion = params.get("DeployVersion")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateApplicationPackageDownloadUrlResponse(AbstractModel):
    """GenerateApplicationPackageDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 包下载临时链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class HealthCheckConfig(AbstractModel):
    """健康检查配置

    """

    def __init__(self):
        r"""
        :param _Type: 支持的健康检查类型，如 HttpGet，TcpSocket，Exec
        :type Type: str
        :param _Protocol: 仅当健康检查类型为 HttpGet 时有效，表示协议类型，如 HTTP，HTTPS
        :type Protocol: str
        :param _Path: 仅当健康检查类型为 HttpGet 时有效，表示请求路径
        :type Path: str
        :param _Exec: 仅当健康检查类型为 Exec 时有效，表示执行的脚本内容
        :type Exec: str
        :param _Port: 仅当健康检查类型为 HttpGet\TcpSocket 时有效，表示请求路径
        :type Port: int
        :param _InitialDelaySeconds: 检查延迟开始时间，单位为秒，默认为 0
        :type InitialDelaySeconds: int
        :param _TimeoutSeconds: 超时时间，单位为秒，默认为 1
        :type TimeoutSeconds: int
        :param _PeriodSeconds: 间隔时间，单位为秒，默认为 10
        :type PeriodSeconds: int
        """
        self._Type = None
        self._Protocol = None
        self._Path = None
        self._Exec = None
        self._Port = None
        self._InitialDelaySeconds = None
        self._TimeoutSeconds = None
        self._PeriodSeconds = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Exec(self):
        return self._Exec

    @Exec.setter
    def Exec(self, Exec):
        self._Exec = Exec

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InitialDelaySeconds(self):
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def TimeoutSeconds(self):
        return self._TimeoutSeconds

    @TimeoutSeconds.setter
    def TimeoutSeconds(self, TimeoutSeconds):
        self._TimeoutSeconds = TimeoutSeconds

    @property
    def PeriodSeconds(self):
        return self._PeriodSeconds

    @PeriodSeconds.setter
    def PeriodSeconds(self, PeriodSeconds):
        self._PeriodSeconds = PeriodSeconds


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Protocol = params.get("Protocol")
        self._Path = params.get("Path")
        self._Exec = params.get("Exec")
        self._Port = params.get("Port")
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        self._TimeoutSeconds = params.get("TimeoutSeconds")
        self._PeriodSeconds = params.get("PeriodSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HorizontalAutoscaler(AbstractModel):
    """弹性伸缩策略

    """

    def __init__(self):
        r"""
        :param _MinReplicas: 最小实例数（可以不传）
        :type MinReplicas: int
        :param _MaxReplicas: 最大实例数（可以不传）
        :type MaxReplicas: int
        :param _Metrics: 指标度量
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
        :param _Threshold: 阈值（整数）
        :type Threshold: int
        :param _Enabled: 是否启用
        :type Enabled: bool
        :param _DoubleThreshold: 阈值（小数，优先使用）
注意：此字段可能返回 null，表示取不到有效值。
        :type DoubleThreshold: float
        """
        self._MinReplicas = None
        self._MaxReplicas = None
        self._Metrics = None
        self._Threshold = None
        self._Enabled = None
        self._DoubleThreshold = None

    @property
    def MinReplicas(self):
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def DoubleThreshold(self):
        return self._DoubleThreshold

    @DoubleThreshold.setter
    def DoubleThreshold(self, DoubleThreshold):
        self._DoubleThreshold = DoubleThreshold


    def _deserialize(self, params):
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        self._Metrics = params.get("Metrics")
        self._Threshold = params.get("Threshold")
        self._Enabled = params.get("Enabled")
        self._DoubleThreshold = params.get("DoubleThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressInfo(AbstractModel):
    """Ingress 配置

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentId: str
        :param _ClusterNamespace: 环境namespace
        :type ClusterNamespace: str
        :param _AddressIPVersion: ip version
        :type AddressIPVersion: str
        :param _IngressName: ingress name
        :type IngressName: str
        :param _Rules: rules 配置
        :type Rules: list of IngressRule
        :param _ClbId: clb ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClbId: str
        :param _Tls: tls 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tls: list of IngressTls
        :param _ClusterId: 环境集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _Vip: clb ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Mixed: 是否混合 https，默认 false，可选值 true 代表有 https 协议监听
        :type Mixed: bool
        :param _RewriteType: 重定向模式，可选值：
- AUTO（自动重定向http到https）
- NONE（不使用重定向）
注意：此字段可能返回 null，表示取不到有效值。
        :type RewriteType: str
        :param _Domain: clb 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        """
        self._EnvironmentId = None
        self._ClusterNamespace = None
        self._AddressIPVersion = None
        self._IngressName = None
        self._Rules = None
        self._ClbId = None
        self._Tls = None
        self._ClusterId = None
        self._Vip = None
        self._CreateTime = None
        self._Mixed = None
        self._RewriteType = None
        self._Domain = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterNamespace(self):
        return self._ClusterNamespace

    @ClusterNamespace.setter
    def ClusterNamespace(self, ClusterNamespace):
        self._ClusterNamespace = ClusterNamespace

    @property
    def AddressIPVersion(self):
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def IngressName(self):
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def ClbId(self):
        return self._ClbId

    @ClbId.setter
    def ClbId(self, ClbId):
        self._ClbId = ClbId

    @property
    def Tls(self):
        return self._Tls

    @Tls.setter
    def Tls(self, Tls):
        self._Tls = Tls

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Mixed(self):
        return self._Mixed

    @Mixed.setter
    def Mixed(self, Mixed):
        self._Mixed = Mixed

    @property
    def RewriteType(self):
        return self._RewriteType

    @RewriteType.setter
    def RewriteType(self, RewriteType):
        self._RewriteType = RewriteType

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterNamespace = params.get("ClusterNamespace")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._IngressName = params.get("IngressName")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = IngressRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._ClbId = params.get("ClbId")
        if params.get("Tls") is not None:
            self._Tls = []
            for item in params.get("Tls"):
                obj = IngressTls()
                obj._deserialize(item)
                self._Tls.append(obj)
        self._ClusterId = params.get("ClusterId")
        self._Vip = params.get("Vip")
        self._CreateTime = params.get("CreateTime")
        self._Mixed = params.get("Mixed")
        self._RewriteType = params.get("RewriteType")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRule(AbstractModel):
    """ingress rule 配置

    """

    def __init__(self):
        r"""
        :param _Http: ingress rule value
        :type Http: :class:`tencentcloud.tem.v20210701.models.IngressRuleValue`
        :param _Host: host 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param _Protocol: 协议，选项为 http， https，默认为 http
        :type Protocol: str
        """
        self._Http = None
        self._Host = None
        self._Protocol = None

    @property
    def Http(self):
        return self._Http

    @Http.setter
    def Http(self, Http):
        self._Http = Http

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        if params.get("Http") is not None:
            self._Http = IngressRuleValue()
            self._Http._deserialize(params.get("Http"))
        self._Host = params.get("Host")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRuleBackend(AbstractModel):
    """Ingress 规则 backend 配置

    """

    def __init__(self):
        r"""
        :param _ServiceName: eks service 名
        :type ServiceName: str
        :param _ServicePort: eks service 端口
        :type ServicePort: int
        """
        self._ServiceName = None
        self._ServicePort = None

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServicePort(self):
        return self._ServicePort

    @ServicePort.setter
    def ServicePort(self, ServicePort):
        self._ServicePort = ServicePort


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._ServicePort = params.get("ServicePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRulePath(AbstractModel):
    """Ingress Rule Path 配置

    """

    def __init__(self):
        r"""
        :param _Path: path 信息
        :type Path: str
        :param _Backend: backend 配置
        :type Backend: :class:`tencentcloud.tem.v20210701.models.IngressRuleBackend`
        """
        self._Path = None
        self._Backend = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Backend(self):
        return self._Backend

    @Backend.setter
    def Backend(self, Backend):
        self._Backend = Backend


    def _deserialize(self, params):
        self._Path = params.get("Path")
        if params.get("Backend") is not None:
            self._Backend = IngressRuleBackend()
            self._Backend._deserialize(params.get("Backend"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRuleValue(AbstractModel):
    """Ingress Rule Value 配置

    """

    def __init__(self):
        r"""
        :param _Paths: rule 整体配置
        :type Paths: list of IngressRulePath
        """
        self._Paths = None

    @property
    def Paths(self):
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths


    def _deserialize(self, params):
        if params.get("Paths") is not None:
            self._Paths = []
            for item in params.get("Paths"):
                obj = IngressRulePath()
                obj._deserialize(item)
                self._Paths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressTls(AbstractModel):
    """ingress tls 配置

    """

    def __init__(self):
        r"""
        :param _Hosts: host 数组, 空数组表示全部域名的默认证书
        :type Hosts: list of str
        :param _SecretName: secret name，如使用证书，则填空字符串
        :type SecretName: str
        :param _CertificateId: SSL Certificate Id
        :type CertificateId: str
        """
        self._Hosts = None
        self._SecretName = None
        self._CertificateId = None

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._Hosts = params.get("Hosts")
        self._SecretName = params.get("SecretName")
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfig(AbstractModel):
    """日志收集配置

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _InputType: 收集类型，container_stdout 为标准输出；container_file 为文件；
        :type InputType: str
        :param _LogsetId: 日志集 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetId: str
        :param _TopicId: 日志主题 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _LogType: 日志提取模式，minimalist_log 为单行全文；multiline_log 为多行全文；  fullregex_log 为单行正则； multiline_fullregex_log 为多行正则； json_log 为 json；
        :type LogType: str
        :param _BeginningRegex: 首行正则表达式，当 LogType 为多行全文、多行正则时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginningRegex: str
        :param _LogPath: 收集文件目录，当 InputType=container_file 时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type LogPath: str
        :param _FilePattern: 收集文件名模式，当 InputType=container_file 时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePattern: str
        :param _CreateDate: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param _ModifyDate: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyDate: str
        :param _ApplicationId: 应用 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param _ApplicationName: 应用名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param _ExtractRule: 导出规则
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtractRule: :class:`tencentcloud.tem.v20210701.models.LogConfigExtractRule`
        """
        self._Name = None
        self._InputType = None
        self._LogsetId = None
        self._TopicId = None
        self._LogType = None
        self._BeginningRegex = None
        self._LogPath = None
        self._FilePattern = None
        self._CreateDate = None
        self._ModifyDate = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._ExtractRule = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def BeginningRegex(self):
        return self._BeginningRegex

    @BeginningRegex.setter
    def BeginningRegex(self, BeginningRegex):
        self._BeginningRegex = BeginningRegex

    @property
    def LogPath(self):
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath

    @property
    def FilePattern(self):
        return self._FilePattern

    @FilePattern.setter
    def FilePattern(self, FilePattern):
        self._FilePattern = FilePattern

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._InputType = params.get("InputType")
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._LogType = params.get("LogType")
        self._BeginningRegex = params.get("BeginningRegex")
        self._LogPath = params.get("LogPath")
        self._FilePattern = params.get("FilePattern")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = LogConfigExtractRule()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfigExtractRule(AbstractModel):
    """日志采集的导出规则配置

    """

    def __init__(self):
        r"""
        :param _BeginningRegex: 首行正则表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginningRegex: str
        :param _Keys: 提取结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of str
        :param _FilterKeys: 过滤键
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterKeys: list of str
        :param _FilterRegex: 过滤值
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterRegex: list of str
        :param _LogRegex: 日志正则表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type LogRegex: str
        :param _TimeKey: 时间字段
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeKey: str
        :param _TimeFormat: 时间格式
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeFormat: str
        :param _UnMatchUpload: 是否上传解析失败日志
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchUpload: str
        :param _UnMatchedKey: 解析失败日志的键名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchedKey: str
        :param _Backtracking: tracking
注意：此字段可能返回 null，表示取不到有效值。
        :type Backtracking: str
        :param _Delimiter: 分隔符
注意：此字段可能返回 null，表示取不到有效值。
        :type Delimiter: str
        """
        self._BeginningRegex = None
        self._Keys = None
        self._FilterKeys = None
        self._FilterRegex = None
        self._LogRegex = None
        self._TimeKey = None
        self._TimeFormat = None
        self._UnMatchUpload = None
        self._UnMatchedKey = None
        self._Backtracking = None
        self._Delimiter = None

    @property
    def BeginningRegex(self):
        return self._BeginningRegex

    @BeginningRegex.setter
    def BeginningRegex(self, BeginningRegex):
        self._BeginningRegex = BeginningRegex

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def FilterKeys(self):
        return self._FilterKeys

    @FilterKeys.setter
    def FilterKeys(self, FilterKeys):
        self._FilterKeys = FilterKeys

    @property
    def FilterRegex(self):
        return self._FilterRegex

    @FilterRegex.setter
    def FilterRegex(self, FilterRegex):
        self._FilterRegex = FilterRegex

    @property
    def LogRegex(self):
        return self._LogRegex

    @LogRegex.setter
    def LogRegex(self, LogRegex):
        self._LogRegex = LogRegex

    @property
    def TimeKey(self):
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def UnMatchUpload(self):
        return self._UnMatchUpload

    @UnMatchUpload.setter
    def UnMatchUpload(self, UnMatchUpload):
        self._UnMatchUpload = UnMatchUpload

    @property
    def UnMatchedKey(self):
        return self._UnMatchedKey

    @UnMatchedKey.setter
    def UnMatchedKey(self, UnMatchedKey):
        self._UnMatchedKey = UnMatchedKey

    @property
    def Backtracking(self):
        return self._Backtracking

    @Backtracking.setter
    def Backtracking(self, Backtracking):
        self._Backtracking = Backtracking

    @property
    def Delimiter(self):
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter


    def _deserialize(self, params):
        self._BeginningRegex = params.get("BeginningRegex")
        self._Keys = params.get("Keys")
        self._FilterKeys = params.get("FilterKeys")
        self._FilterRegex = params.get("FilterRegex")
        self._LogRegex = params.get("LogRegex")
        self._TimeKey = params.get("TimeKey")
        self._TimeFormat = params.get("TimeFormat")
        self._UnMatchUpload = params.get("UnMatchUpload")
        self._UnMatchedKey = params.get("UnMatchedKey")
        self._Backtracking = params.get("Backtracking")
        self._Delimiter = params.get("Delimiter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfigListPage(AbstractModel):
    """LogConfig 列表结果

    """

    def __init__(self):
        r"""
        :param _Records: 记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Records: list of LogConfig
        :param _ContinueToken: 翻页游标
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinueToken: str
        """
        self._Records = None
        self._ContinueToken = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def ContinueToken(self):
        return self._ContinueToken

    @ContinueToken.setter
    def ContinueToken(self, ContinueToken):
        self._ContinueToken = ContinueToken


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = LogConfig()
                obj._deserialize(item)
                self._Records.append(obj)
        self._ContinueToken = params.get("ContinueToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogOutputConf(AbstractModel):
    """日志输出配置

    """

    def __init__(self):
        r"""
        :param _OutputType: 日志消费端类型
        :type OutputType: str
        :param _ClsLogsetName: cls日志集
        :type ClsLogsetName: str
        :param _ClsLogTopicId: cls日志主题
        :type ClsLogTopicId: str
        :param _ClsLogsetId: cls日志集id
        :type ClsLogsetId: str
        :param _ClsLogTopicName: cls日志名称
        :type ClsLogTopicName: str
        """
        self._OutputType = None
        self._ClsLogsetName = None
        self._ClsLogTopicId = None
        self._ClsLogsetId = None
        self._ClsLogTopicName = None

    @property
    def OutputType(self):
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType

    @property
    def ClsLogsetName(self):
        return self._ClsLogsetName

    @ClsLogsetName.setter
    def ClsLogsetName(self, ClsLogsetName):
        self._ClsLogsetName = ClsLogsetName

    @property
    def ClsLogTopicId(self):
        return self._ClsLogTopicId

    @ClsLogTopicId.setter
    def ClsLogTopicId(self, ClsLogTopicId):
        self._ClsLogTopicId = ClsLogTopicId

    @property
    def ClsLogsetId(self):
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsLogTopicName(self):
        return self._ClsLogTopicName

    @ClsLogTopicName.setter
    def ClsLogTopicName(self, ClsLogTopicName):
        self._ClsLogTopicName = ClsLogTopicName


    def _deserialize(self, params):
        self._OutputType = params.get("OutputType")
        self._ClsLogsetName = params.get("ClsLogsetName")
        self._ClsLogTopicId = params.get("ClsLogTopicId")
        self._ClsLogsetId = params.get("ClsLogsetId")
        self._ClsLogTopicName = params.get("ClsLogTopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationAutoscalerRequest(AbstractModel):
    """ModifyApplicationAutoscaler请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _AutoscalerId: 弹性伸缩策略ID
        :type AutoscalerId: str
        :param _Autoscaler: 弹性伸缩策略
        :type Autoscaler: :class:`tencentcloud.tem.v20210701.models.Autoscaler`
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._AutoscalerId = None
        self._Autoscaler = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def AutoscalerId(self):
        return self._AutoscalerId

    @AutoscalerId.setter
    def AutoscalerId(self, AutoscalerId):
        self._AutoscalerId = AutoscalerId

    @property
    def Autoscaler(self):
        return self._Autoscaler

    @Autoscaler.setter
    def Autoscaler(self, Autoscaler):
        self._Autoscaler = Autoscaler


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._AutoscalerId = params.get("AutoscalerId")
        if params.get("Autoscaler") is not None:
            self._Autoscaler = Autoscaler()
            self._Autoscaler._deserialize(params.get("Autoscaler"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationAutoscalerResponse(AbstractModel):
    """ModifyApplicationAutoscaler返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyApplicationInfoRequest(AbstractModel):
    """ModifyApplicationInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _Description: 描述
        :type Description: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _EnableTracing: 是否开启调用链,（此参数已弃用）
        :type EnableTracing: int
        """
        self._ApplicationId = None
        self._Description = None
        self._SourceChannel = None
        self._EnableTracing = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnableTracing(self):
        return self._EnableTracing

    @EnableTracing.setter
    def EnableTracing(self, EnableTracing):
        self._EnableTracing = EnableTracing


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._Description = params.get("Description")
        self._SourceChannel = params.get("SourceChannel")
        self._EnableTracing = params.get("EnableTracing")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationInfoResponse(AbstractModel):
    """ModifyApplicationInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 成功与否
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyApplicationReplicasRequest(AbstractModel):
    """ModifyApplicationReplicas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _Replicas: 实例数量
        :type Replicas: int
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._Replicas = None
        self._SourceChannel = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._Replicas = params.get("Replicas")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationReplicasResponse(AbstractModel):
    """ModifyApplicationReplicas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyApplicationServiceRequest(AbstractModel):
    """ModifyApplicationService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _Service: 全量访问方式设置
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param _Data: 单条访问方式设置
        :type Data: :class:`tencentcloud.tem.v20210701.models.ServicePortMapping`
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._Service = None
        self._Data = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        if params.get("Service") is not None:
            self._Service = EksService()
            self._Service._deserialize(params.get("Service"))
        if params.get("Data") is not None:
            self._Data = ServicePortMapping()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationServiceResponse(AbstractModel):
    """ModifyApplicationService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyConfigDataRequest(AbstractModel):
    """ModifyConfigData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param _Name: 配置名
        :type Name: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _Data: 配置信息
        :type Data: list of Pair
        """
        self._EnvironmentId = None
        self._Name = None
        self._SourceChannel = None
        self._Data = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigDataResponse(AbstractModel):
    """ModifyConfigData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 编辑是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyEnvironmentRequest(AbstractModel):
    """ModifyEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境id
        :type EnvironmentId: str
        :param _EnvironmentName: 环境名称
        :type EnvironmentName: str
        :param _Description: 环境描述
        :type Description: str
        :param _Vpc: 私有网络名称
        :type Vpc: str
        :param _SubnetIds: 子网网络
        :type SubnetIds: list of str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _EnvType: 环境类型：test、pre、prod
        :type EnvType: str
        """
        self._EnvironmentId = None
        self._EnvironmentName = None
        self._Description = None
        self._Vpc = None
        self._SubnetIds = None
        self._SourceChannel = None
        self._EnvType = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Vpc(self):
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Description = params.get("Description")
        self._Vpc = params.get("Vpc")
        self._SubnetIds = params.get("SubnetIds")
        self._SourceChannel = params.get("SourceChannel")
        self._EnvType = params.get("EnvType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentResponse(AbstractModel):
    """ModifyEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 成功时为环境ID，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyIngressRequest(AbstractModel):
    """ModifyIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ingress: Ingress 规则配置
        :type Ingress: :class:`tencentcloud.tem.v20210701.models.IngressInfo`
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._Ingress = None
        self._SourceChannel = None

    @property
    def Ingress(self):
        return self._Ingress

    @Ingress.setter
    def Ingress(self, Ingress):
        self._Ingress = Ingress

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        if params.get("Ingress") is not None:
            self._Ingress = IngressInfo()
            self._Ingress._deserialize(params.get("Ingress"))
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIngressResponse(AbstractModel):
    """ModifyIngress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyLogConfigRequest(AbstractModel):
    """ModifyLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境 ID
        :type EnvironmentId: str
        :param _Name: 配置名
        :type Name: str
        :param _Data: 日志收集配置信息
        :type Data: :class:`tencentcloud.tem.v20210701.models.LogConfig`
        :param _ApplicationId: 应用 ID
        :type ApplicationId: str
        """
        self._EnvironmentId = None
        self._Name = None
        self._Data = None
        self._ApplicationId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        if params.get("Data") is not None:
            self._Data = LogConfig()
            self._Data._deserialize(params.get("Data"))
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLogConfigResponse(AbstractModel):
    """ModifyLogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 编辑是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class MountedSettingConf(AbstractModel):
    """挂载配置信息

    """

    def __init__(self):
        r"""
        :param _ConfigDataName: 配置名称
        :type ConfigDataName: str
        :param _MountedPath: 挂载路径
        :type MountedPath: str
        :param _Data: 配置内容
        :type Data: list of Pair
        :param _SecretDataName: 加密配置名称
        :type SecretDataName: str
        """
        self._ConfigDataName = None
        self._MountedPath = None
        self._Data = None
        self._SecretDataName = None

    @property
    def ConfigDataName(self):
        return self._ConfigDataName

    @ConfigDataName.setter
    def ConfigDataName(self, ConfigDataName):
        self._ConfigDataName = ConfigDataName

    @property
    def MountedPath(self):
        return self._MountedPath

    @MountedPath.setter
    def MountedPath(self, MountedPath):
        self._MountedPath = MountedPath

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def SecretDataName(self):
        return self._SecretDataName

    @SecretDataName.setter
    def SecretDataName(self, SecretDataName):
        self._SecretDataName = SecretDataName


    def _deserialize(self, params):
        self._ConfigDataName = params.get("ConfigDataName")
        self._MountedPath = params.get("MountedPath")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self._Data.append(obj)
        self._SecretDataName = params.get("SecretDataName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceInfo(AbstractModel):
    """Namespace 基础信息

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: ID 信息
        :type EnvironmentId: str
        :param _NamespaceName: 名字（已弃用）
        :type NamespaceName: str
        :param _Region: 地域
        :type Region: str
        :param _VpcId: vpc id
        :type VpcId: str
        :param _SubnetIds: subnet id 数组
        :type SubnetIds: list of str
        :param _Description: 描述
        :type Description: str
        :param _CreatedDate: 创建时间
        :type CreatedDate: str
        :param _EnvironmentName: 环境名称
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        :param _ApmInstanceId: APM 资源 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApmInstanceId: str
        :param _Locked: 环境是否上锁，1为上锁，0则未上锁
注意：此字段可能返回 null，表示取不到有效值。
        :type Locked: int
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _EnvType: 环境类型：test、pre、prod
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvType: str
        """
        self._EnvironmentId = None
        self._NamespaceName = None
        self._Region = None
        self._VpcId = None
        self._SubnetIds = None
        self._Description = None
        self._CreatedDate = None
        self._EnvironmentName = None
        self._ApmInstanceId = None
        self._Locked = None
        self._Tags = None
        self._EnvType = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApmInstanceId(self):
        return self._ApmInstanceId

    @ApmInstanceId.setter
    def ApmInstanceId(self, ApmInstanceId):
        self._ApmInstanceId = ApmInstanceId

    @property
    def Locked(self):
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._NamespaceName = params.get("NamespaceName")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._Description = params.get("Description")
        self._CreatedDate = params.get("CreatedDate")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApmInstanceId = params.get("ApmInstanceId")
        self._Locked = params.get("Locked")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._EnvType = params.get("EnvType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespacePage(AbstractModel):
    """命名空间分页

    """

    def __init__(self):
        r"""
        :param _Records: 分页内容
        :type Records: list of TemNamespaceInfo
        :param _Total: 总数
        :type Total: int
        :param _Size: 条目数
        :type Size: int
        :param _Pages: 页数
        :type Pages: int
        :param _Current: 当前条目
注意：此字段可能返回 null，表示取不到有效值。
        :type Current: int
        """
        self._Records = None
        self._Total = None
        self._Size = None
        self._Pages = None
        self._Current = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Pages(self):
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Current(self):
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = TemNamespaceInfo()
                obj._deserialize(item)
                self._Records.append(obj)
        self._Total = params.get("Total")
        self._Size = params.get("Size")
        self._Pages = params.get("Pages")
        self._Current = params.get("Current")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceStatusInfo(AbstractModel):
    """命名空间状态

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 命名空间id
        :type EnvironmentId: str
        :param _EnvironmentName: 命名空间名称
        :type EnvironmentName: str
        :param _ClusterId: TCB envId | EKS clusterId
        :type ClusterId: str
        :param _ClusterStatus: 环境状态
        :type ClusterStatus: str
        :param _EnvironmentStartingStatus: 环境启动状态（不在启动中为null）
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentStartingStatus: :class:`tencentcloud.tem.v20210701.models.TemEnvironmentStartingStatus`
        :param _EnvironmentStoppingStatus: 环境停止状态（不在停止中为null）
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentStoppingStatus: :class:`tencentcloud.tem.v20210701.models.TemEnvironmentStoppingStatus`
        """
        self._EnvironmentId = None
        self._EnvironmentName = None
        self._ClusterId = None
        self._ClusterStatus = None
        self._EnvironmentStartingStatus = None
        self._EnvironmentStoppingStatus = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def EnvironmentStartingStatus(self):
        return self._EnvironmentStartingStatus

    @EnvironmentStartingStatus.setter
    def EnvironmentStartingStatus(self, EnvironmentStartingStatus):
        self._EnvironmentStartingStatus = EnvironmentStartingStatus

    @property
    def EnvironmentStoppingStatus(self):
        return self._EnvironmentStoppingStatus

    @EnvironmentStoppingStatus.setter
    def EnvironmentStoppingStatus(self, EnvironmentStoppingStatus):
        self._EnvironmentStoppingStatus = EnvironmentStoppingStatus


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ClusterId = params.get("ClusterId")
        self._ClusterStatus = params.get("ClusterStatus")
        if params.get("EnvironmentStartingStatus") is not None:
            self._EnvironmentStartingStatus = TemEnvironmentStartingStatus()
            self._EnvironmentStartingStatus._deserialize(params.get("EnvironmentStartingStatus"))
        if params.get("EnvironmentStoppingStatus") is not None:
            self._EnvironmentStoppingStatus = TemEnvironmentStoppingStatus()
            self._EnvironmentStoppingStatus._deserialize(params.get("EnvironmentStoppingStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """node信息

    """

    def __init__(self):
        r"""
        :param _Name: node名字
        :type Name: str
        :param _Zone: node可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _SubnetId: node子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _AvailableIpCount: 可用IP数
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableIpCount: str
        :param _Cidr: cidr块
注意：此字段可能返回 null，表示取不到有效值。
        :type Cidr: str
        """
        self._Name = None
        self._Zone = None
        self._SubnetId = None
        self._AvailableIpCount = None
        self._Cidr = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AvailableIpCount(self):
        return self._AvailableIpCount

    @AvailableIpCount.setter
    def AvailableIpCount(self, AvailableIpCount):
        self._AvailableIpCount = AvailableIpCount

    @property
    def Cidr(self):
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Zone = params.get("Zone")
        self._SubnetId = params.get("SubnetId")
        self._AvailableIpCount = params.get("AvailableIpCount")
        self._Cidr = params.get("Cidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pair(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param _Key: 键
        :type Key: str
        :param _Value: 值
        :type Value: str
        :param _Type: 类型，default 为自定义，reserved 为系统变量，referenced 为引用配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Config: 配置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: str
        :param _Secret: 加密配置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Secret: str
        """
        self._Key = None
        self._Value = None
        self._Type = None
        self._Config = None
        self._Secret = None

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

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Secret(self):
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Type = params.get("Type")
        self._Config = params.get("Config")
        self._Secret = params.get("Secret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortMapping(AbstractModel):
    """服务端口映射

    """

    def __init__(self):
        r"""
        :param _Port: 端口
        :type Port: int
        :param _TargetPort: 映射端口
        :type TargetPort: int
        :param _Protocol: 协议栈 TCP/UDP
        :type Protocol: str
        :param _ServiceName: k8s service名称
        :type ServiceName: str
        """
        self._Port = None
        self._TargetPort = None
        self._Protocol = None
        self._ServiceName = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetPort(self):
        return self._TargetPort

    @TargetPort.setter
    def TargetPort(self, TargetPort):
        self._TargetPort = TargetPort

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._TargetPort = params.get("TargetPort")
        self._Protocol = params.get("Protocol")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilter(AbstractModel):
    """查询过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 查询字段名称
        :type Name: str
        :param _Value: 查询字段值
        :type Value: list of str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
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
        


class RestartApplicationPodRequest(AbstractModel):
    """RestartApplicationPod请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境id
        :type EnvironmentId: str
        :param _ApplicationId: 应用id
        :type ApplicationId: str
        :param _PodName: 名字
        :type PodName: str
        :param _Limit: 单页条数
        :type Limit: int
        :param _Offset: 分页下标
        :type Offset: int
        :param _Status: pod状态
        :type Status: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._ApplicationId = None
        self._PodName = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ApplicationId = params.get("ApplicationId")
        self._PodName = params.get("PodName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartApplicationPodResponse(AbstractModel):
    """RestartApplicationPod返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class RestartApplicationRequest(AbstractModel):
    """RestartApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        """
        self._ApplicationId = None
        self._SourceChannel = None
        self._EnvironmentId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._SourceChannel = params.get("SourceChannel")
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartApplicationResponse(AbstractModel):
    """RestartApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ResumeDeployApplicationRequest(AbstractModel):
    """ResumeDeployApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 需要开始下一批次的服务id
        :type ApplicationId: str
        :param _EnvironmentId: 环境id
        :type EnvironmentId: str
        """
        self._ApplicationId = None
        self._EnvironmentId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeDeployApplicationResponse(AbstractModel):
    """ResumeDeployApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class RevertDeployApplicationRequest(AbstractModel):
    """RevertDeployApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 需要回滚的服务id
        :type ApplicationId: str
        :param _EnvironmentId: 需要回滚的服务所在环境id
        :type EnvironmentId: str
        """
        self._ApplicationId = None
        self._EnvironmentId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevertDeployApplicationResponse(AbstractModel):
    """RevertDeployApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class RollingUpdateApplicationByVersionRequest(AbstractModel):
    """RollingUpdateApplicationByVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        :param _DeployVersion: 更新版本，IMAGE 部署为 tag 值；JAR/WAR 部署 为 Version
        :type DeployVersion: str
        :param _PackageName: JAR/WAR 包名，仅 JAR/WAR 部署时必填
        :type PackageName: str
        :param _From: 请求来源平台，含 IntelliJ，Coding
        :type From: str
        :param _DeployStrategyType: 部署策略，AUTO 为全自动；BETA 为小批量验证后自动；MANUAL 为全手动；
        :type DeployStrategyType: str
        :param _TotalBatchCount: 发布批次数
        :type TotalBatchCount: int
        :param _BatchInterval: 批次间隔时间
        :type BatchInterval: int
        :param _BetaBatchNum: 小批量验证批次的实例数
        :type BetaBatchNum: int
        :param _MinAvailable: 发布过程中保障的最小可用实例数
        :type MinAvailable: int
        :param _Force: 是否强制发布
        :type Force: bool
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._DeployVersion = None
        self._PackageName = None
        self._From = None
        self._DeployStrategyType = None
        self._TotalBatchCount = None
        self._BatchInterval = None
        self._BetaBatchNum = None
        self._MinAvailable = None
        self._Force = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def DeployVersion(self):
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def DeployStrategyType(self):
        return self._DeployStrategyType

    @DeployStrategyType.setter
    def DeployStrategyType(self, DeployStrategyType):
        self._DeployStrategyType = DeployStrategyType

    @property
    def TotalBatchCount(self):
        return self._TotalBatchCount

    @TotalBatchCount.setter
    def TotalBatchCount(self, TotalBatchCount):
        self._TotalBatchCount = TotalBatchCount

    @property
    def BatchInterval(self):
        return self._BatchInterval

    @BatchInterval.setter
    def BatchInterval(self, BatchInterval):
        self._BatchInterval = BatchInterval

    @property
    def BetaBatchNum(self):
        return self._BetaBatchNum

    @BetaBatchNum.setter
    def BetaBatchNum(self, BetaBatchNum):
        self._BetaBatchNum = BetaBatchNum

    @property
    def MinAvailable(self):
        return self._MinAvailable

    @MinAvailable.setter
    def MinAvailable(self, MinAvailable):
        self._MinAvailable = MinAvailable

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._DeployVersion = params.get("DeployVersion")
        self._PackageName = params.get("PackageName")
        self._From = params.get("From")
        self._DeployStrategyType = params.get("DeployStrategyType")
        self._TotalBatchCount = params.get("TotalBatchCount")
        self._BatchInterval = params.get("BatchInterval")
        self._BetaBatchNum = params.get("BetaBatchNum")
        self._MinAvailable = params.get("MinAvailable")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollingUpdateApplicationByVersionResponse(AbstractModel):
    """RollingUpdateApplicationByVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 版本ID
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class RunVersionPod(AbstractModel):
    """应用实例

    """

    def __init__(self):
        r"""
        :param _Webshell: shell地址
        :type Webshell: str
        :param _PodId: pod的id
        :type PodId: str
        :param _Status: 状态
        :type Status: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _PodIp: 实例的ip
        :type PodIp: str
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _DeployVersion: 部署版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployVersion: str
        :param _RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param _Ready: pod是否就绪
注意：此字段可能返回 null，表示取不到有效值。
        :type Ready: bool
        :param _ContainerState: 容器状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerState: str
        :param _NodeInfo: 实例所在节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInfo: :class:`tencentcloud.tem.v20210701.models.NodeInfo`
        :param _StartTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _Unhealthy: 是否健康
注意：此字段可能返回 null，表示取不到有效值。
        :type Unhealthy: bool
        :param _UnhealthyWarningMsg: 不健康时的提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UnhealthyWarningMsg: str
        :param _VersionId: 版本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: str
        :param _ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        """
        self._Webshell = None
        self._PodId = None
        self._Status = None
        self._CreateTime = None
        self._PodIp = None
        self._Zone = None
        self._DeployVersion = None
        self._RestartCount = None
        self._Ready = None
        self._ContainerState = None
        self._NodeInfo = None
        self._StartTime = None
        self._Unhealthy = None
        self._UnhealthyWarningMsg = None
        self._VersionId = None
        self._ApplicationName = None

    @property
    def Webshell(self):
        return self._Webshell

    @Webshell.setter
    def Webshell(self, Webshell):
        self._Webshell = Webshell

    @property
    def PodId(self):
        return self._PodId

    @PodId.setter
    def PodId(self, PodId):
        self._PodId = PodId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PodIp(self):
        return self._PodIp

    @PodIp.setter
    def PodIp(self, PodIp):
        self._PodIp = PodIp

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DeployVersion(self):
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def RestartCount(self):
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def ContainerState(self):
        return self._ContainerState

    @ContainerState.setter
    def ContainerState(self, ContainerState):
        self._ContainerState = ContainerState

    @property
    def NodeInfo(self):
        return self._NodeInfo

    @NodeInfo.setter
    def NodeInfo(self, NodeInfo):
        self._NodeInfo = NodeInfo

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Unhealthy(self):
        return self._Unhealthy

    @Unhealthy.setter
    def Unhealthy(self, Unhealthy):
        self._Unhealthy = Unhealthy

    @property
    def UnhealthyWarningMsg(self):
        return self._UnhealthyWarningMsg

    @UnhealthyWarningMsg.setter
    def UnhealthyWarningMsg(self, UnhealthyWarningMsg):
        self._UnhealthyWarningMsg = UnhealthyWarningMsg

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName


    def _deserialize(self, params):
        self._Webshell = params.get("Webshell")
        self._PodId = params.get("PodId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._PodIp = params.get("PodIp")
        self._Zone = params.get("Zone")
        self._DeployVersion = params.get("DeployVersion")
        self._RestartCount = params.get("RestartCount")
        self._Ready = params.get("Ready")
        self._ContainerState = params.get("ContainerState")
        if params.get("NodeInfo") is not None:
            self._NodeInfo = NodeInfo()
            self._NodeInfo._deserialize(params.get("NodeInfo"))
        self._StartTime = params.get("StartTime")
        self._Unhealthy = params.get("Unhealthy")
        self._UnhealthyWarningMsg = params.get("UnhealthyWarningMsg")
        self._VersionId = params.get("VersionId")
        self._ApplicationName = params.get("ApplicationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePage(AbstractModel):
    """服务分页

    """

    def __init__(self):
        r"""
        :param _Records: 条目
        :type Records: list of TemService
        :param _Total: 总数
        :type Total: int
        :param _Size: 条目
        :type Size: int
        :param _Pages: 页数
        :type Pages: int
        :param _Current: 当前条数
注意：此字段可能返回 null，表示取不到有效值。
        :type Current: int
        """
        self._Records = None
        self._Total = None
        self._Size = None
        self._Pages = None
        self._Current = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Pages(self):
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Current(self):
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = TemService()
                obj._deserialize(item)
                self._Records.append(obj)
        self._Total = params.get("Total")
        self._Size = params.get("Size")
        self._Pages = params.get("Pages")
        self._Current = params.get("Current")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePortMapping(AbstractModel):
    """端口映射详细信息结构体

    """

    def __init__(self):
        r"""
        :param _Type: 服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _ServiceName: 服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _ClusterIp: 集群内访问vip
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIp: str
        :param _ExternalIp: 集群外方位vip
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalIp: str
        :param _SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _LoadBalanceId: LoadBalance Id
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalanceId: str
        :param _Yaml: yaml 内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param _Ports: 暴露端口列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Ports: list of int
        :param _PortMappingItemList: 端口映射数组
注意：此字段可能返回 null，表示取不到有效值。
        :type PortMappingItemList: list of ServicePortMappingItem
        :param _ExternalDomain: clb domain
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalDomain: str
        """
        self._Type = None
        self._ServiceName = None
        self._ClusterIp = None
        self._ExternalIp = None
        self._SubnetId = None
        self._VpcId = None
        self._LoadBalanceId = None
        self._Yaml = None
        self._Ports = None
        self._PortMappingItemList = None
        self._ExternalDomain = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ClusterIp(self):
        return self._ClusterIp

    @ClusterIp.setter
    def ClusterIp(self, ClusterIp):
        self._ClusterIp = ClusterIp

    @property
    def ExternalIp(self):
        return self._ExternalIp

    @ExternalIp.setter
    def ExternalIp(self, ExternalIp):
        self._ExternalIp = ExternalIp

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def LoadBalanceId(self):
        return self._LoadBalanceId

    @LoadBalanceId.setter
    def LoadBalanceId(self, LoadBalanceId):
        self._LoadBalanceId = LoadBalanceId

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def PortMappingItemList(self):
        return self._PortMappingItemList

    @PortMappingItemList.setter
    def PortMappingItemList(self, PortMappingItemList):
        self._PortMappingItemList = PortMappingItemList

    @property
    def ExternalDomain(self):
        return self._ExternalDomain

    @ExternalDomain.setter
    def ExternalDomain(self, ExternalDomain):
        self._ExternalDomain = ExternalDomain


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ServiceName = params.get("ServiceName")
        self._ClusterIp = params.get("ClusterIp")
        self._ExternalIp = params.get("ExternalIp")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._LoadBalanceId = params.get("LoadBalanceId")
        self._Yaml = params.get("Yaml")
        self._Ports = params.get("Ports")
        if params.get("PortMappingItemList") is not None:
            self._PortMappingItemList = []
            for item in params.get("PortMappingItemList"):
                obj = ServicePortMappingItem()
                obj._deserialize(item)
                self._PortMappingItemList.append(obj)
        self._ExternalDomain = params.get("ExternalDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePortMappingItem(AbstractModel):
    """服务端口映射条目

    """

    def __init__(self):
        r"""
        :param _Port: 应用访问端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _TargetPort: 应用监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetPort: int
        :param _Protocol: 协议类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        """
        self._Port = None
        self._TargetPort = None
        self._Protocol = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetPort(self):
        return self._TargetPort

    @TargetPort.setter
    def TargetPort(self, TargetPort):
        self._TargetPort = TargetPort

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._TargetPort = params.get("TargetPort")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceVersionBrief(AbstractModel):
    """服务版本信息列表

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名称
        :type VersionName: str
        :param _Status: 状态
        :type Status: str
        :param _EnableEs: 是否启动弹性 -- 已废弃
        :type EnableEs: int
        :param _CurrentInstances: 当前实例
        :type CurrentInstances: int
        :param _VersionId: version的id
        :type VersionId: str
        :param _LogOutputConf: 日志输出配置 -- 已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param _ExpectedInstances: 期望实例
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectedInstances: int
        :param _DeployMode: 部署方式
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMode: str
        :param _BuildTaskId: 建构任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildTaskId: str
        :param _EnvironmentId: 环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentId: str
        :param _EnvironmentName: 环境name
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        :param _ApplicationId: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param _ApplicationName: 服务name
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param _UnderDeploying: 是否正在发布中
注意：此字段可能返回 null，表示取不到有效值。
        :type UnderDeploying: bool
        :param _BatchDeployStatus: 分批次部署状态
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchDeployStatus: str
        :param _Zones: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: list of str
        :param _NodeInfos: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInfos: list of NodeInfo
        :param _PodList: 实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param _WorkloadInfo: 工作负载信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadInfo: :class:`tencentcloud.tem.v20210701.models.WorkloadInfo`
        :param _CreateDate: 创建日期
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param _RegionId: 地域id
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        """
        self._VersionName = None
        self._Status = None
        self._EnableEs = None
        self._CurrentInstances = None
        self._VersionId = None
        self._LogOutputConf = None
        self._ExpectedInstances = None
        self._DeployMode = None
        self._BuildTaskId = None
        self._EnvironmentId = None
        self._EnvironmentName = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._UnderDeploying = None
        self._BatchDeployStatus = None
        self._Zones = None
        self._NodeInfos = None
        self._PodList = None
        self._WorkloadInfo = None
        self._CreateDate = None
        self._RegionId = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EnableEs(self):
        return self._EnableEs

    @EnableEs.setter
    def EnableEs(self, EnableEs):
        self._EnableEs = EnableEs

    @property
    def CurrentInstances(self):
        return self._CurrentInstances

    @CurrentInstances.setter
    def CurrentInstances(self, CurrentInstances):
        self._CurrentInstances = CurrentInstances

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def LogOutputConf(self):
        return self._LogOutputConf

    @LogOutputConf.setter
    def LogOutputConf(self, LogOutputConf):
        self._LogOutputConf = LogOutputConf

    @property
    def ExpectedInstances(self):
        return self._ExpectedInstances

    @ExpectedInstances.setter
    def ExpectedInstances(self, ExpectedInstances):
        self._ExpectedInstances = ExpectedInstances

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def BuildTaskId(self):
        return self._BuildTaskId

    @BuildTaskId.setter
    def BuildTaskId(self, BuildTaskId):
        self._BuildTaskId = BuildTaskId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def UnderDeploying(self):
        return self._UnderDeploying

    @UnderDeploying.setter
    def UnderDeploying(self, UnderDeploying):
        self._UnderDeploying = UnderDeploying

    @property
    def BatchDeployStatus(self):
        return self._BatchDeployStatus

    @BatchDeployStatus.setter
    def BatchDeployStatus(self, BatchDeployStatus):
        self._BatchDeployStatus = BatchDeployStatus

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def NodeInfos(self):
        return self._NodeInfos

    @NodeInfos.setter
    def NodeInfos(self, NodeInfos):
        self._NodeInfos = NodeInfos

    @property
    def PodList(self):
        return self._PodList

    @PodList.setter
    def PodList(self, PodList):
        self._PodList = PodList

    @property
    def WorkloadInfo(self):
        return self._WorkloadInfo

    @WorkloadInfo.setter
    def WorkloadInfo(self, WorkloadInfo):
        self._WorkloadInfo = WorkloadInfo

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._Status = params.get("Status")
        self._EnableEs = params.get("EnableEs")
        self._CurrentInstances = params.get("CurrentInstances")
        self._VersionId = params.get("VersionId")
        if params.get("LogOutputConf") is not None:
            self._LogOutputConf = LogOutputConf()
            self._LogOutputConf._deserialize(params.get("LogOutputConf"))
        self._ExpectedInstances = params.get("ExpectedInstances")
        self._DeployMode = params.get("DeployMode")
        self._BuildTaskId = params.get("BuildTaskId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._UnderDeploying = params.get("UnderDeploying")
        self._BatchDeployStatus = params.get("BatchDeployStatus")
        self._Zones = params.get("Zones")
        if params.get("NodeInfos") is not None:
            self._NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodeInfos.append(obj)
        if params.get("PodList") is not None:
            self._PodList = DescribeRunPodPage()
            self._PodList._deserialize(params.get("PodList"))
        if params.get("WorkloadInfo") is not None:
            self._WorkloadInfo = WorkloadInfo()
            self._WorkloadInfo._deserialize(params.get("WorkloadInfo"))
        self._CreateDate = params.get("CreateDate")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortType(AbstractModel):
    """查询过滤器

    """

    def __init__(self):
        r"""
        :param _Key: 排序字段名称
        :type Key: str
        :param _Type: 0：升序，1：倒序
        :type Type: int
        """
        self._Key = None
        self._Type = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopApplicationRequest(AbstractModel):
    """StopApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _EnvironmentId: 环境ID
        :type EnvironmentId: str
        """
        self._ApplicationId = None
        self._SourceChannel = None
        self._EnvironmentId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._SourceChannel = params.get("SourceChannel")
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopApplicationResponse(AbstractModel):
    """StopApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class StorageConf(AbstractModel):
    """存储卷配置

    """

    def __init__(self):
        r"""
        :param _StorageVolName: 存储卷名称
        :type StorageVolName: str
        :param _StorageVolPath: 存储卷路径
        :type StorageVolPath: str
        :param _StorageVolIp: 存储卷IP
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageVolIp: str
        """
        self._StorageVolName = None
        self._StorageVolPath = None
        self._StorageVolIp = None

    @property
    def StorageVolName(self):
        return self._StorageVolName

    @StorageVolName.setter
    def StorageVolName(self, StorageVolName):
        self._StorageVolName = StorageVolName

    @property
    def StorageVolPath(self):
        return self._StorageVolPath

    @StorageVolPath.setter
    def StorageVolPath(self, StorageVolPath):
        self._StorageVolPath = StorageVolPath

    @property
    def StorageVolIp(self):
        return self._StorageVolIp

    @StorageVolIp.setter
    def StorageVolIp(self, StorageVolIp):
        self._StorageVolIp = StorageVolIp


    def _deserialize(self, params):
        self._StorageVolName = params.get("StorageVolName")
        self._StorageVolPath = params.get("StorageVolPath")
        self._StorageVolIp = params.get("StorageVolIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageMountConf(AbstractModel):
    """数据卷挂载信息

    """

    def __init__(self):
        r"""
        :param _VolumeName: 数据卷名
        :type VolumeName: str
        :param _MountPath: 数据卷绑定路径
        :type MountPath: str
        """
        self._VolumeName = None
        self._MountPath = None

    @property
    def VolumeName(self):
        return self._VolumeName

    @VolumeName.setter
    def VolumeName(self, VolumeName):
        self._VolumeName = VolumeName

    @property
    def MountPath(self):
        return self._MountPath

    @MountPath.setter
    def MountPath(self, MountPath):
        self._MountPath = MountPath


    def _deserialize(self, params):
        self._VolumeName = params.get("VolumeName")
        self._MountPath = params.get("MountPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemDeployApplicationDetailInfo(AbstractModel):
    """分批发布详情

    """

    def __init__(self):
        r"""
        :param _DeployStrategyConf: 分批发布策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Status: 当前状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _BetaBatchDetail: beta分批详情
注意：此字段可能返回 null，表示取不到有效值。
        :type BetaBatchDetail: :class:`tencentcloud.tem.v20210701.models.DeployServiceBatchDetail`
        :param _OtherBatchDetail: 其他分批详情
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherBatchDetail: list of DeployServiceBatchDetail
        :param _OldVersionPodList: 老版本pod列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OldVersionPodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param _CurrentBatchIndex: 当前批次id
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentBatchIndex: int
        :param _ErrorMessage: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _CurrentBatchStatus: 当前批次状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentBatchStatus: str
        :param _NewDeployVersion: 新版本version
注意：此字段可能返回 null，表示取不到有效值。
        :type NewDeployVersion: str
        :param _OldDeployVersion: 旧版本version
注意：此字段可能返回 null，表示取不到有效值。
        :type OldDeployVersion: str
        :param _NewVersionPackageInfo: 包名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NewVersionPackageInfo: str
        :param _NextBatchStartTime: 下一批次开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type NextBatchStartTime: int
        """
        self._DeployStrategyConf = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._BetaBatchDetail = None
        self._OtherBatchDetail = None
        self._OldVersionPodList = None
        self._CurrentBatchIndex = None
        self._ErrorMessage = None
        self._CurrentBatchStatus = None
        self._NewDeployVersion = None
        self._OldDeployVersion = None
        self._NewVersionPackageInfo = None
        self._NextBatchStartTime = None

    @property
    def DeployStrategyConf(self):
        return self._DeployStrategyConf

    @DeployStrategyConf.setter
    def DeployStrategyConf(self, DeployStrategyConf):
        self._DeployStrategyConf = DeployStrategyConf

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BetaBatchDetail(self):
        return self._BetaBatchDetail

    @BetaBatchDetail.setter
    def BetaBatchDetail(self, BetaBatchDetail):
        self._BetaBatchDetail = BetaBatchDetail

    @property
    def OtherBatchDetail(self):
        return self._OtherBatchDetail

    @OtherBatchDetail.setter
    def OtherBatchDetail(self, OtherBatchDetail):
        self._OtherBatchDetail = OtherBatchDetail

    @property
    def OldVersionPodList(self):
        return self._OldVersionPodList

    @OldVersionPodList.setter
    def OldVersionPodList(self, OldVersionPodList):
        self._OldVersionPodList = OldVersionPodList

    @property
    def CurrentBatchIndex(self):
        return self._CurrentBatchIndex

    @CurrentBatchIndex.setter
    def CurrentBatchIndex(self, CurrentBatchIndex):
        self._CurrentBatchIndex = CurrentBatchIndex

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def CurrentBatchStatus(self):
        return self._CurrentBatchStatus

    @CurrentBatchStatus.setter
    def CurrentBatchStatus(self, CurrentBatchStatus):
        self._CurrentBatchStatus = CurrentBatchStatus

    @property
    def NewDeployVersion(self):
        return self._NewDeployVersion

    @NewDeployVersion.setter
    def NewDeployVersion(self, NewDeployVersion):
        self._NewDeployVersion = NewDeployVersion

    @property
    def OldDeployVersion(self):
        return self._OldDeployVersion

    @OldDeployVersion.setter
    def OldDeployVersion(self, OldDeployVersion):
        self._OldDeployVersion = OldDeployVersion

    @property
    def NewVersionPackageInfo(self):
        return self._NewVersionPackageInfo

    @NewVersionPackageInfo.setter
    def NewVersionPackageInfo(self, NewVersionPackageInfo):
        self._NewVersionPackageInfo = NewVersionPackageInfo

    @property
    def NextBatchStartTime(self):
        return self._NextBatchStartTime

    @NextBatchStartTime.setter
    def NextBatchStartTime(self, NextBatchStartTime):
        self._NextBatchStartTime = NextBatchStartTime


    def _deserialize(self, params):
        if params.get("DeployStrategyConf") is not None:
            self._DeployStrategyConf = DeployStrategyConf()
            self._DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        if params.get("BetaBatchDetail") is not None:
            self._BetaBatchDetail = DeployServiceBatchDetail()
            self._BetaBatchDetail._deserialize(params.get("BetaBatchDetail"))
        if params.get("OtherBatchDetail") is not None:
            self._OtherBatchDetail = []
            for item in params.get("OtherBatchDetail"):
                obj = DeployServiceBatchDetail()
                obj._deserialize(item)
                self._OtherBatchDetail.append(obj)
        if params.get("OldVersionPodList") is not None:
            self._OldVersionPodList = DescribeRunPodPage()
            self._OldVersionPodList._deserialize(params.get("OldVersionPodList"))
        self._CurrentBatchIndex = params.get("CurrentBatchIndex")
        self._ErrorMessage = params.get("ErrorMessage")
        self._CurrentBatchStatus = params.get("CurrentBatchStatus")
        self._NewDeployVersion = params.get("NewDeployVersion")
        self._OldDeployVersion = params.get("OldDeployVersion")
        self._NewVersionPackageInfo = params.get("NewVersionPackageInfo")
        self._NextBatchStartTime = params.get("NextBatchStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemEnvironmentStartingStatus(AbstractModel):
    """环境启动进程（只统计由环境启动操作触发的应用数量）

    """

    def __init__(self):
        r"""
        :param _ApplicationNumNeedToStart: 需要启动的应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationNumNeedToStart: int
        :param _StartedApplicationNum: 已经启动的应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StartedApplicationNum: int
        :param _StartFailedApplicationNum: 启动失败的应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StartFailedApplicationNum: int
        """
        self._ApplicationNumNeedToStart = None
        self._StartedApplicationNum = None
        self._StartFailedApplicationNum = None

    @property
    def ApplicationNumNeedToStart(self):
        return self._ApplicationNumNeedToStart

    @ApplicationNumNeedToStart.setter
    def ApplicationNumNeedToStart(self, ApplicationNumNeedToStart):
        self._ApplicationNumNeedToStart = ApplicationNumNeedToStart

    @property
    def StartedApplicationNum(self):
        return self._StartedApplicationNum

    @StartedApplicationNum.setter
    def StartedApplicationNum(self, StartedApplicationNum):
        self._StartedApplicationNum = StartedApplicationNum

    @property
    def StartFailedApplicationNum(self):
        return self._StartFailedApplicationNum

    @StartFailedApplicationNum.setter
    def StartFailedApplicationNum(self, StartFailedApplicationNum):
        self._StartFailedApplicationNum = StartFailedApplicationNum


    def _deserialize(self, params):
        self._ApplicationNumNeedToStart = params.get("ApplicationNumNeedToStart")
        self._StartedApplicationNum = params.get("StartedApplicationNum")
        self._StartFailedApplicationNum = params.get("StartFailedApplicationNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemEnvironmentStoppingStatus(AbstractModel):
    """环境停止进程（只统计由环境停止操作触发的应用数量）

    """

    def __init__(self):
        r"""
        :param _ApplicationNumNeedToStop: 需要停止的应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationNumNeedToStop: int
        :param _StoppedApplicationNum: 已经停止的应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppedApplicationNum: int
        :param _StopFailedApplicationNum: 停止失败的应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StopFailedApplicationNum: int
        """
        self._ApplicationNumNeedToStop = None
        self._StoppedApplicationNum = None
        self._StopFailedApplicationNum = None

    @property
    def ApplicationNumNeedToStop(self):
        return self._ApplicationNumNeedToStop

    @ApplicationNumNeedToStop.setter
    def ApplicationNumNeedToStop(self, ApplicationNumNeedToStop):
        self._ApplicationNumNeedToStop = ApplicationNumNeedToStop

    @property
    def StoppedApplicationNum(self):
        return self._StoppedApplicationNum

    @StoppedApplicationNum.setter
    def StoppedApplicationNum(self, StoppedApplicationNum):
        self._StoppedApplicationNum = StoppedApplicationNum

    @property
    def StopFailedApplicationNum(self):
        return self._StopFailedApplicationNum

    @StopFailedApplicationNum.setter
    def StopFailedApplicationNum(self, StopFailedApplicationNum):
        self._StopFailedApplicationNum = StopFailedApplicationNum


    def _deserialize(self, params):
        self._ApplicationNumNeedToStop = params.get("ApplicationNumNeedToStop")
        self._StoppedApplicationNum = params.get("StoppedApplicationNum")
        self._StopFailedApplicationNum = params.get("StopFailedApplicationNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemNamespaceInfo(AbstractModel):
    """命名空间对象

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境id
        :type EnvironmentId: str
        :param _Channel: 渠道
        :type Channel: str
        :param _EnvironmentName: 环境名称
        :type EnvironmentName: str
        :param _Region: 区域名称
        :type Region: str
        :param _Description: 环境描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Status: 状态,1:已销毁;0:正常
        :type Status: int
        :param _Vpc: vpc网络
        :type Vpc: str
        :param _CreateDate: 创建时间
        :type CreateDate: str
        :param _ModifyDate: 修改时间
        :type ModifyDate: str
        :param _Modifier: 修改人
        :type Modifier: str
        :param _Creator: 创建人
        :type Creator: str
        :param _ApplicationNum: 应用数
        :type ApplicationNum: int
        :param _RunInstancesNum: 运行实例数
        :type RunInstancesNum: int
        :param _SubnetId: 子网络
        :type SubnetId: str
        :param _ClusterStatus: 环境集群 status
        :type ClusterStatus: str
        :param _EnableTswTraceService: 是否开启tsw
        :type EnableTswTraceService: bool
        :param _Locked: 环境锁，1为上锁，0则为上锁
        :type Locked: int
        :param _AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _Uin: 用户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _SubAccountUin: 用户SubAccountUin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _HasAuthority: 资源是否有权限
注意：此字段可能返回 null，表示取不到有效值。
        :type HasAuthority: bool
        :param _EnvType: 环境类型: test、pre、prod
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvType: str
        :param _RegionId: 地域码
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        """
        self._EnvironmentId = None
        self._Channel = None
        self._EnvironmentName = None
        self._Region = None
        self._Description = None
        self._Status = None
        self._Vpc = None
        self._CreateDate = None
        self._ModifyDate = None
        self._Modifier = None
        self._Creator = None
        self._ApplicationNum = None
        self._RunInstancesNum = None
        self._SubnetId = None
        self._ClusterStatus = None
        self._EnableTswTraceService = None
        self._Locked = None
        self._AppId = None
        self._Uin = None
        self._SubAccountUin = None
        self._ClusterId = None
        self._Tags = None
        self._HasAuthority = None
        self._EnvType = None
        self._RegionId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vpc(self):
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def Modifier(self):
        return self._Modifier

    @Modifier.setter
    def Modifier(self, Modifier):
        self._Modifier = Modifier

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def ApplicationNum(self):
        return self._ApplicationNum

    @ApplicationNum.setter
    def ApplicationNum(self, ApplicationNum):
        self._ApplicationNum = ApplicationNum

    @property
    def RunInstancesNum(self):
        return self._RunInstancesNum

    @RunInstancesNum.setter
    def RunInstancesNum(self, RunInstancesNum):
        self._RunInstancesNum = RunInstancesNum

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def EnableTswTraceService(self):
        return self._EnableTswTraceService

    @EnableTswTraceService.setter
    def EnableTswTraceService(self, EnableTswTraceService):
        self._EnableTswTraceService = EnableTswTraceService

    @property
    def Locked(self):
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HasAuthority(self):
        return self._HasAuthority

    @HasAuthority.setter
    def HasAuthority(self, HasAuthority):
        self._HasAuthority = HasAuthority

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Channel = params.get("Channel")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Region = params.get("Region")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Vpc = params.get("Vpc")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        self._Modifier = params.get("Modifier")
        self._Creator = params.get("Creator")
        self._ApplicationNum = params.get("ApplicationNum")
        self._RunInstancesNum = params.get("RunInstancesNum")
        self._SubnetId = params.get("SubnetId")
        self._ClusterStatus = params.get("ClusterStatus")
        self._EnableTswTraceService = params.get("EnableTswTraceService")
        self._Locked = params.get("Locked")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._ClusterId = params.get("ClusterId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HasAuthority = params.get("HasAuthority")
        self._EnvType = params.get("EnvType")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemService(AbstractModel):
    """服务

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 主键
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param _ApplicationName: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _EnvironmentId: 命名空间id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentId: str
        :param _CreateDate: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param _ModifyDate: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyDate: str
        :param _Modifier: 修改人
注意：此字段可能返回 null，表示取不到有效值。
        :type Modifier: str
        :param _Creator: 创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _RepoType: tcr个人版or企业版
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoType: int
        :param _InstanceId: 企业版实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _RepoName: 镜像仓库名
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoName: str
        :param _CodingLanguage: 编程语言
注意：此字段可能返回 null，表示取不到有效值。
        :type CodingLanguage: str
        :param _DeployMode: 部署方式
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMode: str
        :param _EnvironmentName: 环境名称
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        :param _ActiveVersions: 服务当前运行环境的实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveVersions: list of ServiceVersionBrief
        :param _EnableTracing: 是否启用链路追踪
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableTracing: int
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _HasAuthority: 是否有资源权限
注意：此字段可能返回 null，表示取不到有效值。
        :type HasAuthority: bool
        """
        self._ApplicationId = None
        self._ApplicationName = None
        self._Description = None
        self._EnvironmentId = None
        self._CreateDate = None
        self._ModifyDate = None
        self._Modifier = None
        self._Creator = None
        self._RepoType = None
        self._InstanceId = None
        self._RepoName = None
        self._CodingLanguage = None
        self._DeployMode = None
        self._EnvironmentName = None
        self._ActiveVersions = None
        self._EnableTracing = None
        self._Tags = None
        self._HasAuthority = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def Modifier(self):
        return self._Modifier

    @Modifier.setter
    def Modifier(self, Modifier):
        self._Modifier = Modifier

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def CodingLanguage(self):
        return self._CodingLanguage

    @CodingLanguage.setter
    def CodingLanguage(self, CodingLanguage):
        self._CodingLanguage = CodingLanguage

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ActiveVersions(self):
        return self._ActiveVersions

    @ActiveVersions.setter
    def ActiveVersions(self, ActiveVersions):
        self._ActiveVersions = ActiveVersions

    @property
    def EnableTracing(self):
        return self._EnableTracing

    @EnableTracing.setter
    def EnableTracing(self, EnableTracing):
        self._EnableTracing = EnableTracing

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HasAuthority(self):
        return self._HasAuthority

    @HasAuthority.setter
    def HasAuthority(self, HasAuthority):
        self._HasAuthority = HasAuthority


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._Description = params.get("Description")
        self._EnvironmentId = params.get("EnvironmentId")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        self._Modifier = params.get("Modifier")
        self._Creator = params.get("Creator")
        self._RepoType = params.get("RepoType")
        self._InstanceId = params.get("InstanceId")
        self._RepoName = params.get("RepoName")
        self._CodingLanguage = params.get("CodingLanguage")
        self._DeployMode = params.get("DeployMode")
        self._EnvironmentName = params.get("EnvironmentName")
        if params.get("ActiveVersions") is not None:
            self._ActiveVersions = []
            for item in params.get("ActiveVersions"):
                obj = ServiceVersionBrief()
                obj._deserialize(item)
                self._ActiveVersions.append(obj)
        self._EnableTracing = params.get("EnableTracing")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HasAuthority = params.get("HasAuthority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemServiceVersionInfo(AbstractModel):
    """版本信息

    """

    def __init__(self):
        r"""
        :param _VersionId: 主键
        :type VersionId: str
        :param _ApplicationId: 服务id
        :type ApplicationId: str
        :param _DeployMode: 部署方式
        :type DeployMode: str
        :param _JdkVersion: jdk版本
        :type JdkVersion: str
        :param _Description: 描述
        :type Description: str
        :param _DeployVersion: 部署版本
        :type DeployVersion: str
        :param _PublishMode: 发布方式
        :type PublishMode: str
        :param _JvmOpts: 启动参数
        :type JvmOpts: str
        :param _InitPodNum: 初始实例
        :type InitPodNum: int
        :param _CpuSpec: cpu规格
        :type CpuSpec: float
        :param _MemorySpec: 内存规格
        :type MemorySpec: float
        :param _ImgRepo: 镜像路径
        :type ImgRepo: str
        :param _ImgName: 镜像名称
        :type ImgName: str
        :param _ImgVersion: 镜像版本
        :type ImgVersion: str
        :param _EsInfo: 弹性配置
注意：此字段可能返回 null，表示取不到有效值。
        :type EsInfo: :class:`tencentcloud.tem.v20210701.models.EsInfo`
        :param _EnvConf: 环境配置
        :type EnvConf: list of Pair
        :param _StorageConfs: 存储配置
        :type StorageConfs: list of StorageConf
        :param _Status: 运行状态
        :type Status: str
        :param _Vpc: 私有网络
        :type Vpc: str
        :param _SubnetId: 子网网络
        :type SubnetId: str
        :param _CreateDate: 创建时间
        :type CreateDate: str
        :param _ModifyDate: 修改时间
        :type ModifyDate: str
        :param _StorageMountConfs: 挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageMountConfs: list of StorageMountConf
        :param _VersionName: 版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _LogOutputConf: 日志输出配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param _ApplicationName: 服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param _ApplicationDescription: 服务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationDescription: str
        :param _EnvironmentName: 环境名称
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        :param _EnvironmentId: 环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentId: str
        :param _PublicDomain: 公网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicDomain: str
        :param _EnablePublicAccess: 是否开通公网访问
注意：此字段可能返回 null，表示取不到有效值。
        :type EnablePublicAccess: bool
        :param _CurrentInstances: 现有的实例
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentInstances: int
        :param _ExpectedInstances: 期望的实例
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectedInstances: int
        :param _CodingLanguage: 编程语言
注意：此字段可能返回 null，表示取不到有效值。
        :type CodingLanguage: str
        :param _PkgName: 程序包名
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgName: str
        :param _EsEnable: 是否启用弹性伸缩
注意：此字段可能返回 null，表示取不到有效值。
        :type EsEnable: int
        :param _EsStrategy: 弹性策略
注意：此字段可能返回 null，表示取不到有效值。
        :type EsStrategy: int
        :param _ImageTag: 镜像tag
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTag: str
        :param _LogEnable: 是否启用log
注意：此字段可能返回 null，表示取不到有效值。
        :type LogEnable: int
        :param _MinAliveInstances: 最小实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinAliveInstances: str
        :param _SecurityGroupIds: 安全组
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        :param _ImageCommand: 镜像命令
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageCommand: str
        :param _ImageArgs: 镜像命令参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageArgs: list of str
        :param _UseRegistryDefaultConfig: 是否使用默认注册中心配置
注意：此字段可能返回 null，表示取不到有效值。
        :type UseRegistryDefaultConfig: bool
        :param _Service: eks 访问设置
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param _SettingConfs: 挂载配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SettingConfs: list of MountedSettingConf
        :param _LogConfs: log path数组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LogConfs: list of str
        :param _PostStart: 启动后立即执行的脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type PostStart: str
        :param _PreStop: 停止前执行的脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type PreStop: str
        :param _Liveness: 存活探针配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Liveness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _Readiness: 就绪探针配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Readiness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _HorizontalAutoscaler: 弹性策略
注意：此字段可能返回 null，表示取不到有效值。
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param _CronHorizontalAutoscaler: 定时弹性策略
注意：此字段可能返回 null，表示取不到有效值。
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param _Zones: 应用实际可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: list of str
        :param _LastDeployDate: 最新部署时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastDeployDate: str
        :param _LastDeploySuccessDate: 最新部署成功时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastDeploySuccessDate: str
        :param _NodeInfos: 应用所在node信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInfos: list of NodeInfo
        :param _ImageType: image类型 -0 为demo -1为正常image
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageType: int
        :param _EnableTracing: 是否启用调用链组件
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableTracing: int
        :param _EnableTracingReport: 是否开启调用链上报，只有 EnableTracing=1 时生效（参数已弃用）
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableTracingReport: int
        :param _RepoType: 镜像类型：0-个人镜像、1-企业镜像、2-公有镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoType: int
        :param _BatchDeployStatus: 分批发布子状态：batch_updating、batch_updating_waiting_confirm
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchDeployStatus: str
        :param _ApmInstanceId: APM 资源 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApmInstanceId: str
        :param _WorkloadInfo: 工作负载信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadInfo: :class:`tencentcloud.tem.v20210701.models.WorkloadInfo`
        :param _SpeedUp: 是否启用应用加速
注意：此字段可能返回 null，表示取不到有效值。
        :type SpeedUp: bool
        :param _StartupProbe: 启动检测探针配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StartupProbe: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _OsFlavour: 操作系统版本，可选参数：
- ALPINE
- CENTOS
注意：此字段可能返回 null，表示取不到有效值。
        :type OsFlavour: str
        :param _RepoServer: 镜像仓库server
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoServer: str
        :param _UnderDeploying: 是否正在发布中
注意：此字段可能返回 null，表示取不到有效值。
        :type UnderDeploying: bool
        :param _EnablePrometheusConf: 监控业务指标监控
注意：此字段可能返回 null，表示取不到有效值。
        :type EnablePrometheusConf: :class:`tencentcloud.tem.v20210701.models.EnablePrometheusConf`
        :param _StoppedManually: 是否为手动停止
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppedManually: bool
        :param _TcrInstanceId: tcr实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TcrInstanceId: str
        :param _EnableMetrics: 1：开始自动metrics采集（open-telemetry）；
0：关闭metrics采集；
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableMetrics: int
        :param _AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _SubAccountUin: 用户SubAccountUin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _Uin: 用户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _GroupId: 应用分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _EnableRegistry: 是否启用注册中心
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableRegistry: int
        :param _AutoscalerList: 弹性伸缩数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalerList: list of Autoscaler
        :param _Modifier: 修改人
注意：此字段可能返回 null，表示取不到有效值。
        :type Modifier: str
        :param _Creator: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _DeployStrategyConf: 部署策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`
        :param _PodList: 实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param _ConfEdited: 发布时配置是否有修改
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfEdited: bool
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _PreStopEncoded: 是否编码
注意：此字段可能返回 null，表示取不到有效值。
        :type PreStopEncoded: str
        :param _PostStartEncoded: 是否编码
注意：此字段可能返回 null，表示取不到有效值。
        :type PostStartEncoded: str
        """
        self._VersionId = None
        self._ApplicationId = None
        self._DeployMode = None
        self._JdkVersion = None
        self._Description = None
        self._DeployVersion = None
        self._PublishMode = None
        self._JvmOpts = None
        self._InitPodNum = None
        self._CpuSpec = None
        self._MemorySpec = None
        self._ImgRepo = None
        self._ImgName = None
        self._ImgVersion = None
        self._EsInfo = None
        self._EnvConf = None
        self._StorageConfs = None
        self._Status = None
        self._Vpc = None
        self._SubnetId = None
        self._CreateDate = None
        self._ModifyDate = None
        self._StorageMountConfs = None
        self._VersionName = None
        self._LogOutputConf = None
        self._ApplicationName = None
        self._ApplicationDescription = None
        self._EnvironmentName = None
        self._EnvironmentId = None
        self._PublicDomain = None
        self._EnablePublicAccess = None
        self._CurrentInstances = None
        self._ExpectedInstances = None
        self._CodingLanguage = None
        self._PkgName = None
        self._EsEnable = None
        self._EsStrategy = None
        self._ImageTag = None
        self._LogEnable = None
        self._MinAliveInstances = None
        self._SecurityGroupIds = None
        self._ImageCommand = None
        self._ImageArgs = None
        self._UseRegistryDefaultConfig = None
        self._Service = None
        self._SettingConfs = None
        self._LogConfs = None
        self._PostStart = None
        self._PreStop = None
        self._Liveness = None
        self._Readiness = None
        self._HorizontalAutoscaler = None
        self._CronHorizontalAutoscaler = None
        self._Zones = None
        self._LastDeployDate = None
        self._LastDeploySuccessDate = None
        self._NodeInfos = None
        self._ImageType = None
        self._EnableTracing = None
        self._EnableTracingReport = None
        self._RepoType = None
        self._BatchDeployStatus = None
        self._ApmInstanceId = None
        self._WorkloadInfo = None
        self._SpeedUp = None
        self._StartupProbe = None
        self._OsFlavour = None
        self._RepoServer = None
        self._UnderDeploying = None
        self._EnablePrometheusConf = None
        self._StoppedManually = None
        self._TcrInstanceId = None
        self._EnableMetrics = None
        self._AppId = None
        self._SubAccountUin = None
        self._Uin = None
        self._Region = None
        self._GroupId = None
        self._EnableRegistry = None
        self._AutoscalerList = None
        self._Modifier = None
        self._Creator = None
        self._DeployStrategyConf = None
        self._PodList = None
        self._ConfEdited = None
        self._Tags = None
        self._PreStopEncoded = None
        self._PostStartEncoded = None

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def JdkVersion(self):
        return self._JdkVersion

    @JdkVersion.setter
    def JdkVersion(self, JdkVersion):
        self._JdkVersion = JdkVersion

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DeployVersion(self):
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def PublishMode(self):
        return self._PublishMode

    @PublishMode.setter
    def PublishMode(self, PublishMode):
        self._PublishMode = PublishMode

    @property
    def JvmOpts(self):
        return self._JvmOpts

    @JvmOpts.setter
    def JvmOpts(self, JvmOpts):
        self._JvmOpts = JvmOpts

    @property
    def InitPodNum(self):
        return self._InitPodNum

    @InitPodNum.setter
    def InitPodNum(self, InitPodNum):
        self._InitPodNum = InitPodNum

    @property
    def CpuSpec(self):
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def MemorySpec(self):
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def ImgRepo(self):
        return self._ImgRepo

    @ImgRepo.setter
    def ImgRepo(self, ImgRepo):
        self._ImgRepo = ImgRepo

    @property
    def ImgName(self):
        return self._ImgName

    @ImgName.setter
    def ImgName(self, ImgName):
        self._ImgName = ImgName

    @property
    def ImgVersion(self):
        return self._ImgVersion

    @ImgVersion.setter
    def ImgVersion(self, ImgVersion):
        self._ImgVersion = ImgVersion

    @property
    def EsInfo(self):
        return self._EsInfo

    @EsInfo.setter
    def EsInfo(self, EsInfo):
        self._EsInfo = EsInfo

    @property
    def EnvConf(self):
        return self._EnvConf

    @EnvConf.setter
    def EnvConf(self, EnvConf):
        self._EnvConf = EnvConf

    @property
    def StorageConfs(self):
        return self._StorageConfs

    @StorageConfs.setter
    def StorageConfs(self, StorageConfs):
        self._StorageConfs = StorageConfs

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vpc(self):
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def StorageMountConfs(self):
        return self._StorageMountConfs

    @StorageMountConfs.setter
    def StorageMountConfs(self, StorageMountConfs):
        self._StorageMountConfs = StorageMountConfs

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def LogOutputConf(self):
        return self._LogOutputConf

    @LogOutputConf.setter
    def LogOutputConf(self, LogOutputConf):
        self._LogOutputConf = LogOutputConf

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ApplicationDescription(self):
        return self._ApplicationDescription

    @ApplicationDescription.setter
    def ApplicationDescription(self, ApplicationDescription):
        self._ApplicationDescription = ApplicationDescription

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def PublicDomain(self):
        return self._PublicDomain

    @PublicDomain.setter
    def PublicDomain(self, PublicDomain):
        self._PublicDomain = PublicDomain

    @property
    def EnablePublicAccess(self):
        return self._EnablePublicAccess

    @EnablePublicAccess.setter
    def EnablePublicAccess(self, EnablePublicAccess):
        self._EnablePublicAccess = EnablePublicAccess

    @property
    def CurrentInstances(self):
        return self._CurrentInstances

    @CurrentInstances.setter
    def CurrentInstances(self, CurrentInstances):
        self._CurrentInstances = CurrentInstances

    @property
    def ExpectedInstances(self):
        return self._ExpectedInstances

    @ExpectedInstances.setter
    def ExpectedInstances(self, ExpectedInstances):
        self._ExpectedInstances = ExpectedInstances

    @property
    def CodingLanguage(self):
        return self._CodingLanguage

    @CodingLanguage.setter
    def CodingLanguage(self, CodingLanguage):
        self._CodingLanguage = CodingLanguage

    @property
    def PkgName(self):
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def EsEnable(self):
        return self._EsEnable

    @EsEnable.setter
    def EsEnable(self, EsEnable):
        self._EsEnable = EsEnable

    @property
    def EsStrategy(self):
        return self._EsStrategy

    @EsStrategy.setter
    def EsStrategy(self, EsStrategy):
        self._EsStrategy = EsStrategy

    @property
    def ImageTag(self):
        return self._ImageTag

    @ImageTag.setter
    def ImageTag(self, ImageTag):
        self._ImageTag = ImageTag

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def MinAliveInstances(self):
        return self._MinAliveInstances

    @MinAliveInstances.setter
    def MinAliveInstances(self, MinAliveInstances):
        self._MinAliveInstances = MinAliveInstances

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ImageCommand(self):
        return self._ImageCommand

    @ImageCommand.setter
    def ImageCommand(self, ImageCommand):
        self._ImageCommand = ImageCommand

    @property
    def ImageArgs(self):
        return self._ImageArgs

    @ImageArgs.setter
    def ImageArgs(self, ImageArgs):
        self._ImageArgs = ImageArgs

    @property
    def UseRegistryDefaultConfig(self):
        return self._UseRegistryDefaultConfig

    @UseRegistryDefaultConfig.setter
    def UseRegistryDefaultConfig(self, UseRegistryDefaultConfig):
        self._UseRegistryDefaultConfig = UseRegistryDefaultConfig

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def SettingConfs(self):
        return self._SettingConfs

    @SettingConfs.setter
    def SettingConfs(self, SettingConfs):
        self._SettingConfs = SettingConfs

    @property
    def LogConfs(self):
        return self._LogConfs

    @LogConfs.setter
    def LogConfs(self, LogConfs):
        self._LogConfs = LogConfs

    @property
    def PostStart(self):
        return self._PostStart

    @PostStart.setter
    def PostStart(self, PostStart):
        self._PostStart = PostStart

    @property
    def PreStop(self):
        return self._PreStop

    @PreStop.setter
    def PreStop(self, PreStop):
        self._PreStop = PreStop

    @property
    def Liveness(self):
        return self._Liveness

    @Liveness.setter
    def Liveness(self, Liveness):
        self._Liveness = Liveness

    @property
    def Readiness(self):
        return self._Readiness

    @Readiness.setter
    def Readiness(self, Readiness):
        self._Readiness = Readiness

    @property
    def HorizontalAutoscaler(self):
        return self._HorizontalAutoscaler

    @HorizontalAutoscaler.setter
    def HorizontalAutoscaler(self, HorizontalAutoscaler):
        self._HorizontalAutoscaler = HorizontalAutoscaler

    @property
    def CronHorizontalAutoscaler(self):
        return self._CronHorizontalAutoscaler

    @CronHorizontalAutoscaler.setter
    def CronHorizontalAutoscaler(self, CronHorizontalAutoscaler):
        self._CronHorizontalAutoscaler = CronHorizontalAutoscaler

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def LastDeployDate(self):
        return self._LastDeployDate

    @LastDeployDate.setter
    def LastDeployDate(self, LastDeployDate):
        self._LastDeployDate = LastDeployDate

    @property
    def LastDeploySuccessDate(self):
        return self._LastDeploySuccessDate

    @LastDeploySuccessDate.setter
    def LastDeploySuccessDate(self, LastDeploySuccessDate):
        self._LastDeploySuccessDate = LastDeploySuccessDate

    @property
    def NodeInfos(self):
        return self._NodeInfos

    @NodeInfos.setter
    def NodeInfos(self, NodeInfos):
        self._NodeInfos = NodeInfos

    @property
    def ImageType(self):
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def EnableTracing(self):
        return self._EnableTracing

    @EnableTracing.setter
    def EnableTracing(self, EnableTracing):
        self._EnableTracing = EnableTracing

    @property
    def EnableTracingReport(self):
        return self._EnableTracingReport

    @EnableTracingReport.setter
    def EnableTracingReport(self, EnableTracingReport):
        self._EnableTracingReport = EnableTracingReport

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def BatchDeployStatus(self):
        return self._BatchDeployStatus

    @BatchDeployStatus.setter
    def BatchDeployStatus(self, BatchDeployStatus):
        self._BatchDeployStatus = BatchDeployStatus

    @property
    def ApmInstanceId(self):
        return self._ApmInstanceId

    @ApmInstanceId.setter
    def ApmInstanceId(self, ApmInstanceId):
        self._ApmInstanceId = ApmInstanceId

    @property
    def WorkloadInfo(self):
        return self._WorkloadInfo

    @WorkloadInfo.setter
    def WorkloadInfo(self, WorkloadInfo):
        self._WorkloadInfo = WorkloadInfo

    @property
    def SpeedUp(self):
        return self._SpeedUp

    @SpeedUp.setter
    def SpeedUp(self, SpeedUp):
        self._SpeedUp = SpeedUp

    @property
    def StartupProbe(self):
        return self._StartupProbe

    @StartupProbe.setter
    def StartupProbe(self, StartupProbe):
        self._StartupProbe = StartupProbe

    @property
    def OsFlavour(self):
        return self._OsFlavour

    @OsFlavour.setter
    def OsFlavour(self, OsFlavour):
        self._OsFlavour = OsFlavour

    @property
    def RepoServer(self):
        return self._RepoServer

    @RepoServer.setter
    def RepoServer(self, RepoServer):
        self._RepoServer = RepoServer

    @property
    def UnderDeploying(self):
        return self._UnderDeploying

    @UnderDeploying.setter
    def UnderDeploying(self, UnderDeploying):
        self._UnderDeploying = UnderDeploying

    @property
    def EnablePrometheusConf(self):
        return self._EnablePrometheusConf

    @EnablePrometheusConf.setter
    def EnablePrometheusConf(self, EnablePrometheusConf):
        self._EnablePrometheusConf = EnablePrometheusConf

    @property
    def StoppedManually(self):
        return self._StoppedManually

    @StoppedManually.setter
    def StoppedManually(self, StoppedManually):
        self._StoppedManually = StoppedManually

    @property
    def TcrInstanceId(self):
        return self._TcrInstanceId

    @TcrInstanceId.setter
    def TcrInstanceId(self, TcrInstanceId):
        self._TcrInstanceId = TcrInstanceId

    @property
    def EnableMetrics(self):
        return self._EnableMetrics

    @EnableMetrics.setter
    def EnableMetrics(self, EnableMetrics):
        self._EnableMetrics = EnableMetrics

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableRegistry(self):
        return self._EnableRegistry

    @EnableRegistry.setter
    def EnableRegistry(self, EnableRegistry):
        self._EnableRegistry = EnableRegistry

    @property
    def AutoscalerList(self):
        return self._AutoscalerList

    @AutoscalerList.setter
    def AutoscalerList(self, AutoscalerList):
        self._AutoscalerList = AutoscalerList

    @property
    def Modifier(self):
        return self._Modifier

    @Modifier.setter
    def Modifier(self, Modifier):
        self._Modifier = Modifier

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def DeployStrategyConf(self):
        return self._DeployStrategyConf

    @DeployStrategyConf.setter
    def DeployStrategyConf(self, DeployStrategyConf):
        self._DeployStrategyConf = DeployStrategyConf

    @property
    def PodList(self):
        return self._PodList

    @PodList.setter
    def PodList(self, PodList):
        self._PodList = PodList

    @property
    def ConfEdited(self):
        return self._ConfEdited

    @ConfEdited.setter
    def ConfEdited(self, ConfEdited):
        self._ConfEdited = ConfEdited

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PreStopEncoded(self):
        return self._PreStopEncoded

    @PreStopEncoded.setter
    def PreStopEncoded(self, PreStopEncoded):
        self._PreStopEncoded = PreStopEncoded

    @property
    def PostStartEncoded(self):
        return self._PostStartEncoded

    @PostStartEncoded.setter
    def PostStartEncoded(self, PostStartEncoded):
        self._PostStartEncoded = PostStartEncoded


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._ApplicationId = params.get("ApplicationId")
        self._DeployMode = params.get("DeployMode")
        self._JdkVersion = params.get("JdkVersion")
        self._Description = params.get("Description")
        self._DeployVersion = params.get("DeployVersion")
        self._PublishMode = params.get("PublishMode")
        self._JvmOpts = params.get("JvmOpts")
        self._InitPodNum = params.get("InitPodNum")
        self._CpuSpec = params.get("CpuSpec")
        self._MemorySpec = params.get("MemorySpec")
        self._ImgRepo = params.get("ImgRepo")
        self._ImgName = params.get("ImgName")
        self._ImgVersion = params.get("ImgVersion")
        if params.get("EsInfo") is not None:
            self._EsInfo = EsInfo()
            self._EsInfo._deserialize(params.get("EsInfo"))
        if params.get("EnvConf") is not None:
            self._EnvConf = []
            for item in params.get("EnvConf"):
                obj = Pair()
                obj._deserialize(item)
                self._EnvConf.append(obj)
        if params.get("StorageConfs") is not None:
            self._StorageConfs = []
            for item in params.get("StorageConfs"):
                obj = StorageConf()
                obj._deserialize(item)
                self._StorageConfs.append(obj)
        self._Status = params.get("Status")
        self._Vpc = params.get("Vpc")
        self._SubnetId = params.get("SubnetId")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        if params.get("StorageMountConfs") is not None:
            self._StorageMountConfs = []
            for item in params.get("StorageMountConfs"):
                obj = StorageMountConf()
                obj._deserialize(item)
                self._StorageMountConfs.append(obj)
        self._VersionName = params.get("VersionName")
        if params.get("LogOutputConf") is not None:
            self._LogOutputConf = LogOutputConf()
            self._LogOutputConf._deserialize(params.get("LogOutputConf"))
        self._ApplicationName = params.get("ApplicationName")
        self._ApplicationDescription = params.get("ApplicationDescription")
        self._EnvironmentName = params.get("EnvironmentName")
        self._EnvironmentId = params.get("EnvironmentId")
        self._PublicDomain = params.get("PublicDomain")
        self._EnablePublicAccess = params.get("EnablePublicAccess")
        self._CurrentInstances = params.get("CurrentInstances")
        self._ExpectedInstances = params.get("ExpectedInstances")
        self._CodingLanguage = params.get("CodingLanguage")
        self._PkgName = params.get("PkgName")
        self._EsEnable = params.get("EsEnable")
        self._EsStrategy = params.get("EsStrategy")
        self._ImageTag = params.get("ImageTag")
        self._LogEnable = params.get("LogEnable")
        self._MinAliveInstances = params.get("MinAliveInstances")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._ImageCommand = params.get("ImageCommand")
        self._ImageArgs = params.get("ImageArgs")
        self._UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("Service") is not None:
            self._Service = EksService()
            self._Service._deserialize(params.get("Service"))
        if params.get("SettingConfs") is not None:
            self._SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self._SettingConfs.append(obj)
        self._LogConfs = params.get("LogConfs")
        self._PostStart = params.get("PostStart")
        self._PreStop = params.get("PreStop")
        if params.get("Liveness") is not None:
            self._Liveness = HealthCheckConfig()
            self._Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self._Readiness = HealthCheckConfig()
            self._Readiness._deserialize(params.get("Readiness"))
        if params.get("HorizontalAutoscaler") is not None:
            self._HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self._HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self._CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self._CronHorizontalAutoscaler.append(obj)
        self._Zones = params.get("Zones")
        self._LastDeployDate = params.get("LastDeployDate")
        self._LastDeploySuccessDate = params.get("LastDeploySuccessDate")
        if params.get("NodeInfos") is not None:
            self._NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodeInfos.append(obj)
        self._ImageType = params.get("ImageType")
        self._EnableTracing = params.get("EnableTracing")
        self._EnableTracingReport = params.get("EnableTracingReport")
        self._RepoType = params.get("RepoType")
        self._BatchDeployStatus = params.get("BatchDeployStatus")
        self._ApmInstanceId = params.get("ApmInstanceId")
        if params.get("WorkloadInfo") is not None:
            self._WorkloadInfo = WorkloadInfo()
            self._WorkloadInfo._deserialize(params.get("WorkloadInfo"))
        self._SpeedUp = params.get("SpeedUp")
        if params.get("StartupProbe") is not None:
            self._StartupProbe = HealthCheckConfig()
            self._StartupProbe._deserialize(params.get("StartupProbe"))
        self._OsFlavour = params.get("OsFlavour")
        self._RepoServer = params.get("RepoServer")
        self._UnderDeploying = params.get("UnderDeploying")
        if params.get("EnablePrometheusConf") is not None:
            self._EnablePrometheusConf = EnablePrometheusConf()
            self._EnablePrometheusConf._deserialize(params.get("EnablePrometheusConf"))
        self._StoppedManually = params.get("StoppedManually")
        self._TcrInstanceId = params.get("TcrInstanceId")
        self._EnableMetrics = params.get("EnableMetrics")
        self._AppId = params.get("AppId")
        self._SubAccountUin = params.get("SubAccountUin")
        self._Uin = params.get("Uin")
        self._Region = params.get("Region")
        self._GroupId = params.get("GroupId")
        self._EnableRegistry = params.get("EnableRegistry")
        if params.get("AutoscalerList") is not None:
            self._AutoscalerList = []
            for item in params.get("AutoscalerList"):
                obj = Autoscaler()
                obj._deserialize(item)
                self._AutoscalerList.append(obj)
        self._Modifier = params.get("Modifier")
        self._Creator = params.get("Creator")
        if params.get("DeployStrategyConf") is not None:
            self._DeployStrategyConf = DeployStrategyConf()
            self._DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("PodList") is not None:
            self._PodList = DescribeRunPodPage()
            self._PodList._deserialize(params.get("PodList"))
        self._ConfEdited = params.get("ConfEdited")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PreStopEncoded = params.get("PreStopEncoded")
        self._PostStartEncoded = params.get("PostStartEncoded")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UseDefaultRepoParameters(AbstractModel):
    """创建应用，创建仓库参数

    """

    def __init__(self):
        r"""
        :param _EnterpriseInstanceName: 企业版实例名
注意：此字段可能返回 null，表示取不到有效值。
        :type EnterpriseInstanceName: str
        :param _EnterpriseInstanceChargeType: 企业版收费类型  0 按量收费   1 包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :type EnterpriseInstanceChargeType: int
        :param _EnterpriseInstanceType: 企业版规格：basic-基础班 ，standard-标准版，premium-高级版
注意：此字段可能返回 null，表示取不到有效值。
        :type EnterpriseInstanceType: str
        """
        self._EnterpriseInstanceName = None
        self._EnterpriseInstanceChargeType = None
        self._EnterpriseInstanceType = None

    @property
    def EnterpriseInstanceName(self):
        return self._EnterpriseInstanceName

    @EnterpriseInstanceName.setter
    def EnterpriseInstanceName(self, EnterpriseInstanceName):
        self._EnterpriseInstanceName = EnterpriseInstanceName

    @property
    def EnterpriseInstanceChargeType(self):
        return self._EnterpriseInstanceChargeType

    @EnterpriseInstanceChargeType.setter
    def EnterpriseInstanceChargeType(self, EnterpriseInstanceChargeType):
        self._EnterpriseInstanceChargeType = EnterpriseInstanceChargeType

    @property
    def EnterpriseInstanceType(self):
        return self._EnterpriseInstanceType

    @EnterpriseInstanceType.setter
    def EnterpriseInstanceType(self, EnterpriseInstanceType):
        self._EnterpriseInstanceType = EnterpriseInstanceType


    def _deserialize(self, params):
        self._EnterpriseInstanceName = params.get("EnterpriseInstanceName")
        self._EnterpriseInstanceChargeType = params.get("EnterpriseInstanceChargeType")
        self._EnterpriseInstanceType = params.get("EnterpriseInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkloadInfo(AbstractModel):
    """工作负载详情

    """

    def __init__(self):
        r"""
        :param _ClusterId: 资源 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ApplicationName: 应用名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param _VersionName: 版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _ReadyReplicas: Ready实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadyReplicas: int
        :param _Replicas: 实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param _UpdatedReplicas: Updated实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedReplicas: int
        :param _UpdatedReadyReplicas: UpdatedReady实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedReadyReplicas: int
        :param _UpdateRevision: 更新版本
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateRevision: str
        :param _CurrentRevision: 当前版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentRevision: str
        """
        self._ClusterId = None
        self._ApplicationName = None
        self._VersionName = None
        self._ReadyReplicas = None
        self._Replicas = None
        self._UpdatedReplicas = None
        self._UpdatedReadyReplicas = None
        self._UpdateRevision = None
        self._CurrentRevision = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def ReadyReplicas(self):
        return self._ReadyReplicas

    @ReadyReplicas.setter
    def ReadyReplicas(self, ReadyReplicas):
        self._ReadyReplicas = ReadyReplicas

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def UpdatedReplicas(self):
        return self._UpdatedReplicas

    @UpdatedReplicas.setter
    def UpdatedReplicas(self, UpdatedReplicas):
        self._UpdatedReplicas = UpdatedReplicas

    @property
    def UpdatedReadyReplicas(self):
        return self._UpdatedReadyReplicas

    @UpdatedReadyReplicas.setter
    def UpdatedReadyReplicas(self, UpdatedReadyReplicas):
        self._UpdatedReadyReplicas = UpdatedReadyReplicas

    @property
    def UpdateRevision(self):
        return self._UpdateRevision

    @UpdateRevision.setter
    def UpdateRevision(self, UpdateRevision):
        self._UpdateRevision = UpdateRevision

    @property
    def CurrentRevision(self):
        return self._CurrentRevision

    @CurrentRevision.setter
    def CurrentRevision(self, CurrentRevision):
        self._CurrentRevision = CurrentRevision


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ApplicationName = params.get("ApplicationName")
        self._VersionName = params.get("VersionName")
        self._ReadyReplicas = params.get("ReadyReplicas")
        self._Replicas = params.get("Replicas")
        self._UpdatedReplicas = params.get("UpdatedReplicas")
        self._UpdatedReadyReplicas = params.get("UpdatedReadyReplicas")
        self._UpdateRevision = params.get("UpdateRevision")
        self._CurrentRevision = params.get("CurrentRevision")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        