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


class CosToken(AbstractModel):
    r"""Cos token

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
        r"""唯一请求 ID
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def Bucket(self):
        r"""存储桶桶名
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        r"""存储桶所在区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TmpSecretId(self):
        r"""临时密钥的SecretId
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        r"""临时密钥的SecretKey
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def SessionToken(self):
        r"""临时密钥的 sessionToken
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def StartTime(self):
        r"""临时密钥获取的开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        r"""临时密钥的 expiredTime
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def FullPath(self):
        r"""包完整路径
        :rtype: str
        """
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
        


class CreateCosTokenRequest(AbstractModel):
    r"""CreateCosToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _VersionId: 服务版本ID
        :type VersionId: str
        :param _PkgName: 包名
        :type PkgName: str
        :param _OptType: optType 1上传  2查询
        :type OptType: int
        :param _SourceChannel: 来源 channel
        :type SourceChannel: int
        """
        self._ServiceId = None
        self._VersionId = None
        self._PkgName = None
        self._OptType = None
        self._SourceChannel = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def VersionId(self):
        r"""服务版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def PkgName(self):
        r"""包名
        :rtype: str
        """
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def OptType(self):
        r"""optType 1上传  2查询
        :rtype: int
        """
        return self._OptType

    @OptType.setter
    def OptType(self, OptType):
        self._OptType = OptType

    @property
    def SourceChannel(self):
        r"""来源 channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._VersionId = params.get("VersionId")
        self._PkgName = params.get("PkgName")
        self._OptType = params.get("OptType")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosTokenResponse(AbstractModel):
    r"""CreateCosToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 成功时为CosToken对象，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tem.v20201221.models.CosToken`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""成功时为CosToken对象，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tem.v20201221.models.CosToken`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CosToken()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateCosTokenV2Request(AbstractModel):
    r"""CreateCosTokenV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _PkgName: 包名
        :type PkgName: str
        :param _OptType: optType 1上传  2查询
        :type OptType: int
        :param _SourceChannel: 来源 channel
        :type SourceChannel: int
        :param _TimeVersion: 充当deployVersion入参
        :type TimeVersion: str
        """
        self._ServiceId = None
        self._PkgName = None
        self._OptType = None
        self._SourceChannel = None
        self._TimeVersion = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def PkgName(self):
        r"""包名
        :rtype: str
        """
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def OptType(self):
        r"""optType 1上传  2查询
        :rtype: int
        """
        return self._OptType

    @OptType.setter
    def OptType(self, OptType):
        self._OptType = OptType

    @property
    def SourceChannel(self):
        r"""来源 channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def TimeVersion(self):
        r"""充当deployVersion入参
        :rtype: str
        """
        return self._TimeVersion

    @TimeVersion.setter
    def TimeVersion(self, TimeVersion):
        self._TimeVersion = TimeVersion


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
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
        


class CreateCosTokenV2Response(AbstractModel):
    r"""CreateCosTokenV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 成功时为CosToken对象，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tem.v20201221.models.CosToken`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""成功时为CosToken对象，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tem.v20201221.models.CosToken`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CosToken()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    r"""CreateNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _Vpc: 私有网络名称
        :type Vpc: str
        :param _SubnetIds: 子网列表
        :type SubnetIds: list of str
        :param _Description: 命名空间描述
        :type Description: str
        :param _K8sVersion: K8s version
        :type K8sVersion: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _EnableTswTraceService: 是否开启tsw服务
        :type EnableTswTraceService: bool
        """
        self._NamespaceName = None
        self._Vpc = None
        self._SubnetIds = None
        self._Description = None
        self._K8sVersion = None
        self._SourceChannel = None
        self._EnableTswTraceService = None

    @property
    def NamespaceName(self):
        r"""命名空间名称
        :rtype: str
        """
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Vpc(self):
        r"""私有网络名称
        :rtype: str
        """
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def SubnetIds(self):
        r"""子网列表
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def Description(self):
        r"""命名空间描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def K8sVersion(self):
        r"""K8s version
        :rtype: str
        """
        return self._K8sVersion

    @K8sVersion.setter
    def K8sVersion(self, K8sVersion):
        self._K8sVersion = K8sVersion

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnableTswTraceService(self):
        r"""是否开启tsw服务
        :rtype: bool
        """
        return self._EnableTswTraceService

    @EnableTswTraceService.setter
    def EnableTswTraceService(self, EnableTswTraceService):
        self._EnableTswTraceService = EnableTswTraceService


    def _deserialize(self, params):
        self._NamespaceName = params.get("NamespaceName")
        self._Vpc = params.get("Vpc")
        self._SubnetIds = params.get("SubnetIds")
        self._Description = params.get("Description")
        self._K8sVersion = params.get("K8sVersion")
        self._SourceChannel = params.get("SourceChannel")
        self._EnableTswTraceService = params.get("EnableTswTraceService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    r"""CreateNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 成功时为命名空间ID，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""成功时为命名空间ID，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateResourceRequest(AbstractModel):
    r"""CreateResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NamespaceId: 命名空间 Id
        :type NamespaceId: str
        :param _ResourceType: 资源类型，目前支持文件系统：CFS；日志服务：CLS；注册中心：TSE_SRE
        :type ResourceType: str
        :param _ResourceId: 资源 Id
        :type ResourceId: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._NamespaceId = None
        self._ResourceType = None
        self._ResourceId = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        r"""命名空间 Id
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def ResourceType(self):
        r"""资源类型，目前支持文件系统：CFS；日志服务：CLS；注册中心：TSE_SRE
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceId(self):
        r"""资源 Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceId = params.get("ResourceId")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceResponse(AbstractModel):
    r"""CreateResource返回参数结构体

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
        r"""成功与否
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateServiceV2Request(AbstractModel):
    r"""CreateServiceV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceName: 服务名
        :type ServiceName: str
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
        :param _SubnetList: 服务所在子网
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
        """
        self._ServiceName = None
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

    @property
    def ServiceName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UseDefaultImageService(self):
        r"""是否使用默认镜像服务 1-是，0-否
        :rtype: int
        """
        return self._UseDefaultImageService

    @UseDefaultImageService.setter
    def UseDefaultImageService(self, UseDefaultImageService):
        self._UseDefaultImageService = UseDefaultImageService

    @property
    def RepoType(self):
        r"""如果是绑定仓库，绑定的仓库类型，0-个人版，1-企业版
        :rtype: int
        """
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def InstanceId(self):
        r"""企业版镜像服务的实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RepoServer(self):
        r"""绑定镜像服务器地址
        :rtype: str
        """
        return self._RepoServer

    @RepoServer.setter
    def RepoServer(self, RepoServer):
        self._RepoServer = RepoServer

    @property
    def RepoName(self):
        r"""绑定镜像仓库名
        :rtype: str
        """
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def SubnetList(self):
        r"""服务所在子网
        :rtype: list of str
        """
        return self._SubnetList

    @SubnetList.setter
    def SubnetList(self, SubnetList):
        self._SubnetList = SubnetList

    @property
    def CodingLanguage(self):
        r"""编程语言 
- JAVA
- OTHER
        :rtype: str
        """
        return self._CodingLanguage

    @CodingLanguage.setter
    def CodingLanguage(self, CodingLanguage):
        self._CodingLanguage = CodingLanguage

    @property
    def DeployMode(self):
        r"""部署方式 
- IMAGE
- JAR
- WAR
        :rtype: str
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceV2Response(AbstractModel):
    r"""CreateServiceV2返回参数结构体

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
        r"""服务code
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteIngressRequest(AbstractModel):
    r"""DeleteIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NamespaceId: tem NamespaceId
        :type NamespaceId: str
        :param _EksNamespace: eks namespace 名
        :type EksNamespace: str
        :param _Name: ingress 规则名
        :type Name: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._NamespaceId = None
        self._EksNamespace = None
        self._Name = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        r"""tem NamespaceId
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def EksNamespace(self):
        r"""eks namespace 名
        :rtype: str
        """
        return self._EksNamespace

    @EksNamespace.setter
    def EksNamespace(self, EksNamespace):
        self._EksNamespace = EksNamespace

    @property
    def Name(self):
        r"""ingress 规则名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._EksNamespace = params.get("EksNamespace")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIngressResponse(AbstractModel):
    r"""DeleteIngress返回参数结构体

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
        r"""是否删除成功
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeployServiceV2Request(AbstractModel):
    r"""DeployServiceV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _ContainerPort: 容器端口
        :type ContainerPort: int
        :param _InitPodNum: 初始化 pod 数
        :type InitPodNum: int
        :param _CpuSpec: cpu规格
        :type CpuSpec: float
        :param _MemorySpec: 内存规格
        :type MemorySpec: float
        :param _NamespaceId: 环境ID
        :type NamespaceId: str
        :param _ImgRepo: 镜像仓库
        :type ImgRepo: str
        :param _VersionDesc: 版本描述信息
        :type VersionDesc: str
        :param _JvmOpts: 启动参数
        :type JvmOpts: str
        :param _EsInfo: 弹性伸缩配置，不传默认不启用弹性伸缩配置
        :type EsInfo: :class:`tencentcloud.tem.v20201221.models.EsInfo`
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
- KONA：使用 kona jdk。
- OPEN：使用 open jdk。
        :type JdkVersion: str
        :param _SecurityGroupIds: 安全组ID s
        :type SecurityGroupIds: list of str
        :param _LogOutputConf: 日志输出配置
        :type LogOutputConf: :class:`tencentcloud.tem.v20201221.models.LogOutputConf`
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _Description: 版本描述
        :type Description: str
        :param _ImageCommand: 镜像命令
        :type ImageCommand: str
        :param _ImageArgs: 镜像命令参数
        :type ImageArgs: list of str
        :param _PortMappings: 服务端口映射
        :type PortMappings: list of PortMapping
        :param _UseRegistryDefaultConfig: 是否添加默认注册中心配置
        :type UseRegistryDefaultConfig: bool
        :param _SettingConfs: 挂载配置信息
        :type SettingConfs: list of MountedSettingConf
        :param _EksService: eks 访问设置
        :type EksService: :class:`tencentcloud.tem.v20201221.models.EksService`
        :param _VersionId: 要回滚到的历史版本id
        :type VersionId: str
        :param _PostStart: 启动后执行的脚本
        :type PostStart: str
        :param _PreStop: 停止前执行的脚本
        :type PreStop: str
        :param _DeployStrategyConf: 分批发布策略配置
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20201221.models.DeployStrategyConf`
        :param _Liveness: 存活探针配置
        :type Liveness: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        :param _Readiness: 就绪探针配置
        :type Readiness: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        """
        self._ServiceId = None
        self._ContainerPort = None
        self._InitPodNum = None
        self._CpuSpec = None
        self._MemorySpec = None
        self._NamespaceId = None
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
        self._PortMappings = None
        self._UseRegistryDefaultConfig = None
        self._SettingConfs = None
        self._EksService = None
        self._VersionId = None
        self._PostStart = None
        self._PreStop = None
        self._DeployStrategyConf = None
        self._Liveness = None
        self._Readiness = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ContainerPort(self):
        r"""容器端口
        :rtype: int
        """
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def InitPodNum(self):
        r"""初始化 pod 数
        :rtype: int
        """
        return self._InitPodNum

    @InitPodNum.setter
    def InitPodNum(self, InitPodNum):
        self._InitPodNum = InitPodNum

    @property
    def CpuSpec(self):
        r"""cpu规格
        :rtype: float
        """
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def MemorySpec(self):
        r"""内存规格
        :rtype: float
        """
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def NamespaceId(self):
        r"""环境ID
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def ImgRepo(self):
        r"""镜像仓库
        :rtype: str
        """
        return self._ImgRepo

    @ImgRepo.setter
    def ImgRepo(self, ImgRepo):
        self._ImgRepo = ImgRepo

    @property
    def VersionDesc(self):
        r"""版本描述信息
        :rtype: str
        """
        return self._VersionDesc

    @VersionDesc.setter
    def VersionDesc(self, VersionDesc):
        self._VersionDesc = VersionDesc

    @property
    def JvmOpts(self):
        r"""启动参数
        :rtype: str
        """
        return self._JvmOpts

    @JvmOpts.setter
    def JvmOpts(self, JvmOpts):
        self._JvmOpts = JvmOpts

    @property
    def EsInfo(self):
        r"""弹性伸缩配置，不传默认不启用弹性伸缩配置
        :rtype: :class:`tencentcloud.tem.v20201221.models.EsInfo`
        """
        return self._EsInfo

    @EsInfo.setter
    def EsInfo(self, EsInfo):
        self._EsInfo = EsInfo

    @property
    def EnvConf(self):
        r"""环境变量配置
        :rtype: list of Pair
        """
        return self._EnvConf

    @EnvConf.setter
    def EnvConf(self, EnvConf):
        self._EnvConf = EnvConf

    @property
    def LogConfs(self):
        r"""日志配置
        :rtype: list of str
        """
        return self._LogConfs

    @LogConfs.setter
    def LogConfs(self, LogConfs):
        self._LogConfs = LogConfs

    @property
    def StorageConfs(self):
        r"""数据卷配置
        :rtype: list of StorageConf
        """
        return self._StorageConfs

    @StorageConfs.setter
    def StorageConfs(self, StorageConfs):
        self._StorageConfs = StorageConfs

    @property
    def StorageMountConfs(self):
        r"""数据卷挂载配置
        :rtype: list of StorageMountConf
        """
        return self._StorageMountConfs

    @StorageMountConfs.setter
    def StorageMountConfs(self, StorageMountConfs):
        self._StorageMountConfs = StorageMountConfs

    @property
    def DeployMode(self):
        r"""部署类型。
- JAR：通过 jar 包部署
- WAR：通过 war 包部署
- IMAGE：通过镜像部署
        :rtype: str
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def DeployVersion(self):
        r"""部署类型为 IMAGE 时，该参数表示镜像 tag。
部署类型为 JAR/WAR 时，该参数表示包版本号。
        :rtype: str
        """
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def PkgName(self):
        r"""包名。使用 JAR 包或者 WAR 包部署的时候必填。
        :rtype: str
        """
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def JdkVersion(self):
        r"""JDK 版本。
- KONA：使用 kona jdk。
- OPEN：使用 open jdk。
        :rtype: str
        """
        return self._JdkVersion

    @JdkVersion.setter
    def JdkVersion(self, JdkVersion):
        self._JdkVersion = JdkVersion

    @property
    def SecurityGroupIds(self):
        r"""安全组ID s
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def LogOutputConf(self):
        r"""日志输出配置
        :rtype: :class:`tencentcloud.tem.v20201221.models.LogOutputConf`
        """
        return self._LogOutputConf

    @LogOutputConf.setter
    def LogOutputConf(self, LogOutputConf):
        self._LogOutputConf = LogOutputConf

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Description(self):
        r"""版本描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ImageCommand(self):
        r"""镜像命令
        :rtype: str
        """
        return self._ImageCommand

    @ImageCommand.setter
    def ImageCommand(self, ImageCommand):
        self._ImageCommand = ImageCommand

    @property
    def ImageArgs(self):
        r"""镜像命令参数
        :rtype: list of str
        """
        return self._ImageArgs

    @ImageArgs.setter
    def ImageArgs(self, ImageArgs):
        self._ImageArgs = ImageArgs

    @property
    def PortMappings(self):
        r"""服务端口映射
        :rtype: list of PortMapping
        """
        return self._PortMappings

    @PortMappings.setter
    def PortMappings(self, PortMappings):
        self._PortMappings = PortMappings

    @property
    def UseRegistryDefaultConfig(self):
        r"""是否添加默认注册中心配置
        :rtype: bool
        """
        return self._UseRegistryDefaultConfig

    @UseRegistryDefaultConfig.setter
    def UseRegistryDefaultConfig(self, UseRegistryDefaultConfig):
        self._UseRegistryDefaultConfig = UseRegistryDefaultConfig

    @property
    def SettingConfs(self):
        r"""挂载配置信息
        :rtype: list of MountedSettingConf
        """
        return self._SettingConfs

    @SettingConfs.setter
    def SettingConfs(self, SettingConfs):
        self._SettingConfs = SettingConfs

    @property
    def EksService(self):
        r"""eks 访问设置
        :rtype: :class:`tencentcloud.tem.v20201221.models.EksService`
        """
        return self._EksService

    @EksService.setter
    def EksService(self, EksService):
        self._EksService = EksService

    @property
    def VersionId(self):
        r"""要回滚到的历史版本id
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def PostStart(self):
        r"""启动后执行的脚本
        :rtype: str
        """
        return self._PostStart

    @PostStart.setter
    def PostStart(self, PostStart):
        self._PostStart = PostStart

    @property
    def PreStop(self):
        r"""停止前执行的脚本
        :rtype: str
        """
        return self._PreStop

    @PreStop.setter
    def PreStop(self, PreStop):
        self._PreStop = PreStop

    @property
    def DeployStrategyConf(self):
        r"""分批发布策略配置
        :rtype: :class:`tencentcloud.tem.v20201221.models.DeployStrategyConf`
        """
        return self._DeployStrategyConf

    @DeployStrategyConf.setter
    def DeployStrategyConf(self, DeployStrategyConf):
        self._DeployStrategyConf = DeployStrategyConf

    @property
    def Liveness(self):
        r"""存活探针配置
        :rtype: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        """
        return self._Liveness

    @Liveness.setter
    def Liveness(self, Liveness):
        self._Liveness = Liveness

    @property
    def Readiness(self):
        r"""就绪探针配置
        :rtype: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        """
        return self._Readiness

    @Readiness.setter
    def Readiness(self, Readiness):
        self._Readiness = Readiness


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ContainerPort = params.get("ContainerPort")
        self._InitPodNum = params.get("InitPodNum")
        self._CpuSpec = params.get("CpuSpec")
        self._MemorySpec = params.get("MemorySpec")
        self._NamespaceId = params.get("NamespaceId")
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
        if params.get("PortMappings") is not None:
            self._PortMappings = []
            for item in params.get("PortMappings"):
                obj = PortMapping()
                obj._deserialize(item)
                self._PortMappings.append(obj)
        self._UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("SettingConfs") is not None:
            self._SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self._SettingConfs.append(obj)
        if params.get("EksService") is not None:
            self._EksService = EksService()
            self._EksService._deserialize(params.get("EksService"))
        self._VersionId = params.get("VersionId")
        self._PostStart = params.get("PostStart")
        self._PreStop = params.get("PreStop")
        if params.get("DeployStrategyConf") is not None:
            self._DeployStrategyConf = DeployStrategyConf()
            self._DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("Liveness") is not None:
            self._Liveness = HealthCheckConfig()
            self._Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self._Readiness = HealthCheckConfig()
            self._Readiness._deserialize(params.get("Readiness"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployServiceV2Response(AbstractModel):
    r"""DeployServiceV2返回参数结构体

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
        r"""版本ID（前端可忽略）
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeployStrategyConf(AbstractModel):
    r"""分批发布策略配置

    """

    def __init__(self):
        r"""
        :param _TotalBatchCount: 总分批数
        :type TotalBatchCount: int
        :param _BetaBatchNum: beta分批实例数
        :type BetaBatchNum: int
        :param _DeployStrategyType: 分批策略：0-全自动，1-全手动，beta分批一定是手动的，这里的策略指定的是剩余批次
        :type DeployStrategyType: int
        :param _BatchInterval: 每批暂停间隔
        :type BatchInterval: int
        """
        self._TotalBatchCount = None
        self._BetaBatchNum = None
        self._DeployStrategyType = None
        self._BatchInterval = None

    @property
    def TotalBatchCount(self):
        r"""总分批数
        :rtype: int
        """
        return self._TotalBatchCount

    @TotalBatchCount.setter
    def TotalBatchCount(self, TotalBatchCount):
        self._TotalBatchCount = TotalBatchCount

    @property
    def BetaBatchNum(self):
        r"""beta分批实例数
        :rtype: int
        """
        return self._BetaBatchNum

    @BetaBatchNum.setter
    def BetaBatchNum(self, BetaBatchNum):
        self._BetaBatchNum = BetaBatchNum

    @property
    def DeployStrategyType(self):
        r"""分批策略：0-全自动，1-全手动，beta分批一定是手动的，这里的策略指定的是剩余批次
        :rtype: int
        """
        return self._DeployStrategyType

    @DeployStrategyType.setter
    def DeployStrategyType(self, DeployStrategyType):
        self._DeployStrategyType = DeployStrategyType

    @property
    def BatchInterval(self):
        r"""每批暂停间隔
        :rtype: int
        """
        return self._BatchInterval

    @BatchInterval.setter
    def BatchInterval(self, BatchInterval):
        self._BatchInterval = BatchInterval


    def _deserialize(self, params):
        self._TotalBatchCount = params.get("TotalBatchCount")
        self._BetaBatchNum = params.get("BetaBatchNum")
        self._DeployStrategyType = params.get("DeployStrategyType")
        self._BatchInterval = params.get("BatchInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressRequest(AbstractModel):
    r"""DescribeIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NamespaceId: tem namespaceId
        :type NamespaceId: str
        :param _EksNamespace: eks namespace 名
        :type EksNamespace: str
        :param _Name: ingress 规则名
        :type Name: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._NamespaceId = None
        self._EksNamespace = None
        self._Name = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        r"""tem namespaceId
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def EksNamespace(self):
        r"""eks namespace 名
        :rtype: str
        """
        return self._EksNamespace

    @EksNamespace.setter
    def EksNamespace(self, EksNamespace):
        self._EksNamespace = EksNamespace

    @property
    def Name(self):
        r"""ingress 规则名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._EksNamespace = params.get("EksNamespace")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressResponse(AbstractModel):
    r"""DescribeIngress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: Ingress 规则配置
        :type Result: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Ingress 规则配置
        :rtype: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""DescribeIngresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NamespaceId: namespace id
        :type NamespaceId: str
        :param _EksNamespace: namespace
        :type EksNamespace: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _Names: ingress 规则名列表
        :type Names: list of str
        """
        self._NamespaceId = None
        self._EksNamespace = None
        self._SourceChannel = None
        self._Names = None

    @property
    def NamespaceId(self):
        r"""namespace id
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def EksNamespace(self):
        r"""namespace
        :rtype: str
        """
        return self._EksNamespace

    @EksNamespace.setter
    def EksNamespace(self, EksNamespace):
        self._EksNamespace = EksNamespace

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Names(self):
        r"""ingress 规则名列表
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._EksNamespace = params.get("EksNamespace")
        self._SourceChannel = params.get("SourceChannel")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressesResponse(AbstractModel):
    r"""DescribeIngresses返回参数结构体

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
        r"""ingress 数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IngressInfo
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeNamespacesRequest(AbstractModel):
    r"""DescribeNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页limit
        :type Limit: int
        :param _Offset: 分页下标
        :type Offset: int
        :param _SourceChannel: 来源source
        :type SourceChannel: int
        """
        self._Limit = None
        self._Offset = None
        self._SourceChannel = None

    @property
    def Limit(self):
        r"""分页limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页下标
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SourceChannel(self):
        r"""来源source
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacesResponse(AbstractModel):
    r"""DescribeNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20201221.models.NamespacePage`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回结果
        :rtype: :class:`tencentcloud.tem.v20201221.models.NamespacePage`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = NamespacePage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeRelatedIngressesRequest(AbstractModel):
    r"""DescribeRelatedIngresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NamespaceId: 环境 id
        :type NamespaceId: str
        :param _EksNamespace: EKS namespace
        :type EksNamespace: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        :param _ServiceId: 服务 ID
        :type ServiceId: str
        """
        self._NamespaceId = None
        self._EksNamespace = None
        self._SourceChannel = None
        self._ServiceId = None

    @property
    def NamespaceId(self):
        r"""环境 id
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def EksNamespace(self):
        r"""EKS namespace
        :rtype: str
        """
        return self._EksNamespace

    @EksNamespace.setter
    def EksNamespace(self, EksNamespace):
        self._EksNamespace = EksNamespace

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def ServiceId(self):
        r"""服务 ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._EksNamespace = params.get("EksNamespace")
        self._SourceChannel = params.get("SourceChannel")
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelatedIngressesResponse(AbstractModel):
    r"""DescribeRelatedIngresses返回参数结构体

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
        r"""ingress 数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IngressInfo
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""版本pod列表

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
        r"""分页下标
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""单页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""请求id
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def PodList(self):
        r"""条目
        :rtype: list of RunVersionPod
        """
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
        


class DescribeServiceRunPodListV2Request(AbstractModel):
    r"""DescribeServiceRunPodListV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NamespaceId: 环境id
        :type NamespaceId: str
        :param _ServiceId: 服务名id
        :type ServiceId: str
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
        self._NamespaceId = None
        self._ServiceId = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._PodName = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        r"""环境id
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def ServiceId(self):
        r"""服务名id
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        r"""单页条数，默认值20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页下标，默认值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        r"""实例状态 
- Running 
- Pending 
- Error
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PodName(self):
        r"""实例名字
        :rtype: str
        """
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._ServiceId = params.get("ServiceId")
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
        


class DescribeServiceRunPodListV2Response(AbstractModel):
    r"""DescribeServiceRunPodListV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20201221.models.DescribeRunPodPage`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回结果
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeRunPodPage`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeRunPodPage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class EksService(AbstractModel):
    r"""eks service info

    """

    def __init__(self):
        r"""
        :param _Name: service name
        :type Name: str
        :param _Ports: 可用端口
        :type Ports: list of int
        :param _Yaml: yaml 内容
        :type Yaml: str
        :param _ServiceName: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
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
        """
        self._Name = None
        self._Ports = None
        self._Yaml = None
        self._ServiceName = None
        self._VersionName = None
        self._ClusterIp = None
        self._ExternalIp = None
        self._Type = None
        self._SubnetId = None
        self._LoadBalanceId = None
        self._PortMappings = None

    @property
    def Name(self):
        r"""service name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Ports(self):
        r"""可用端口
        :rtype: list of int
        """
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Yaml(self):
        r"""yaml 内容
        :rtype: str
        """
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def ServiceName(self):
        r"""服务名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def VersionName(self):
        r"""版本名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def ClusterIp(self):
        r"""内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ClusterIp

    @ClusterIp.setter
    def ClusterIp(self, ClusterIp):
        self._ClusterIp = ClusterIp

    @property
    def ExternalIp(self):
        r"""外网ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExternalIp

    @ExternalIp.setter
    def ExternalIp(self, ExternalIp):
        self._ExternalIp = ExternalIp

    @property
    def Type(self):
        r"""访问类型，可选值：
- EXTERNAL（公网访问）
- VPC（vpc内访问）
- CLUSTER（集群内访问）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubnetId(self):
        r"""子网ID，只在类型为vpc访问时才有值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def LoadBalanceId(self):
        r"""负载均衡ID，只在外网访问和vpc内访问才有值，默认自动创建
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalanceId

    @LoadBalanceId.setter
    def LoadBalanceId(self, LoadBalanceId):
        self._LoadBalanceId = LoadBalanceId

    @property
    def PortMappings(self):
        r"""端口映射
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PortMapping
        """
        return self._PortMappings

    @PortMappings.setter
    def PortMappings(self, PortMappings):
        self._PortMappings = PortMappings


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Ports = params.get("Ports")
        self._Yaml = params.get("Yaml")
        self._ServiceName = params.get("ServiceName")
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsInfo(AbstractModel):
    r"""弹性伸缩配置

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
        r"""最小实例数
        :rtype: int
        """
        return self._MinAliveInstances

    @MinAliveInstances.setter
    def MinAliveInstances(self, MinAliveInstances):
        self._MinAliveInstances = MinAliveInstances

    @property
    def MaxAliveInstances(self):
        r"""最大实例数
        :rtype: int
        """
        return self._MaxAliveInstances

    @MaxAliveInstances.setter
    def MaxAliveInstances(self, MaxAliveInstances):
        self._MaxAliveInstances = MaxAliveInstances

    @property
    def EsStrategy(self):
        r"""弹性策略,1:cpu，2:内存
        :rtype: int
        """
        return self._EsStrategy

    @EsStrategy.setter
    def EsStrategy(self, EsStrategy):
        self._EsStrategy = EsStrategy

    @property
    def Threshold(self):
        r"""弹性扩缩容条件值
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def VersionId(self):
        r"""版本Id
        :rtype: str
        """
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
        


class GenerateDownloadUrlRequest(AbstractModel):
    r"""GenerateDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _PkgName: 包名
        :type PkgName: str
        :param _DeployVersion: 需要下载的包版本
        :type DeployVersion: str
        :param _SourceChannel: 来源 channel
        :type SourceChannel: int
        """
        self._ServiceId = None
        self._PkgName = None
        self._DeployVersion = None
        self._SourceChannel = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def PkgName(self):
        r"""包名
        :rtype: str
        """
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def DeployVersion(self):
        r"""需要下载的包版本
        :rtype: str
        """
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def SourceChannel(self):
        r"""来源 channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
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
        


class GenerateDownloadUrlResponse(AbstractModel):
    r"""GenerateDownloadUrl返回参数结构体

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
        r"""包下载临时链接
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class HealthCheckConfig(AbstractModel):
    r"""健康检查配置

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
        r"""支持的健康检查类型，如 HttpGet，TcpSocket，Exec
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Protocol(self):
        r"""仅当健康检查类型为 HttpGet 时有效，表示协议类型，如 HTTP，HTTPS
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Path(self):
        r"""仅当健康检查类型为 HttpGet 时有效，表示请求路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Exec(self):
        r"""仅当健康检查类型为 Exec 时有效，表示执行的脚本内容
        :rtype: str
        """
        return self._Exec

    @Exec.setter
    def Exec(self, Exec):
        self._Exec = Exec

    @property
    def Port(self):
        r"""仅当健康检查类型为 HttpGet\TcpSocket 时有效，表示请求路径
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InitialDelaySeconds(self):
        r"""检查延迟开始时间，单位为秒，默认为 0
        :rtype: int
        """
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def TimeoutSeconds(self):
        r"""超时时间，单位为秒，默认为 1
        :rtype: int
        """
        return self._TimeoutSeconds

    @TimeoutSeconds.setter
    def TimeoutSeconds(self, TimeoutSeconds):
        self._TimeoutSeconds = TimeoutSeconds

    @property
    def PeriodSeconds(self):
        r"""间隔时间，单位为秒，默认为 10
        :rtype: int
        """
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
        


class IngressInfo(AbstractModel):
    r"""Ingress 配置

    """

    def __init__(self):
        r"""
        :param _NamespaceId: tem namespaceId
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param _EksNamespace: eks namespace
        :type EksNamespace: str
        :param _AddressIPVersion: ip version
        :type AddressIPVersion: str
        :param _Name: ingress name
        :type Name: str
        :param _Rules: rules 配置
        :type Rules: list of IngressRule
        :param _ClbId: clb ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClbId: str
        :param _Tls: tls 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tls: list of IngressTls
        :param _ClusterId: eks clusterId
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
        """
        self._NamespaceId = None
        self._EksNamespace = None
        self._AddressIPVersion = None
        self._Name = None
        self._Rules = None
        self._ClbId = None
        self._Tls = None
        self._ClusterId = None
        self._Vip = None
        self._CreateTime = None
        self._Mixed = None

    @property
    def NamespaceId(self):
        r"""tem namespaceId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def EksNamespace(self):
        r"""eks namespace
        :rtype: str
        """
        return self._EksNamespace

    @EksNamespace.setter
    def EksNamespace(self, EksNamespace):
        self._EksNamespace = EksNamespace

    @property
    def AddressIPVersion(self):
        r"""ip version
        :rtype: str
        """
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def Name(self):
        r"""ingress name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rules(self):
        r"""rules 配置
        :rtype: list of IngressRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def ClbId(self):
        r"""clb ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClbId

    @ClbId.setter
    def ClbId(self, ClbId):
        self._ClbId = ClbId

    @property
    def Tls(self):
        r"""tls 配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IngressTls
        """
        return self._Tls

    @Tls.setter
    def Tls(self, Tls):
        self._Tls = Tls

    @property
    def ClusterId(self):
        r"""eks clusterId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Vip(self):
        r"""clb ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Mixed(self):
        r"""是否混合 https，默认 false，可选值 true 代表有 https 协议监听
        :rtype: bool
        """
        return self._Mixed

    @Mixed.setter
    def Mixed(self, Mixed):
        self._Mixed = Mixed


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._EksNamespace = params.get("EksNamespace")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._Name = params.get("Name")
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRule(AbstractModel):
    r"""ingress rule 配置

    """

    def __init__(self):
        r"""
        :param _Http: ingress rule value
        :type Http: :class:`tencentcloud.tem.v20201221.models.IngressRuleValue`
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
        r"""ingress rule value
        :rtype: :class:`tencentcloud.tem.v20201221.models.IngressRuleValue`
        """
        return self._Http

    @Http.setter
    def Http(self, Http):
        self._Http = Http

    @property
    def Host(self):
        r"""host 地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Protocol(self):
        r"""协议，选项为 http， https，默认为 http
        :rtype: str
        """
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
    r"""Ingress 规则 backend 配置

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
        r"""eks service 名
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServicePort(self):
        r"""eks service 端口
        :rtype: int
        """
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
    r"""Ingress Rule Path 配置

    """

    def __init__(self):
        r"""
        :param _Path: path 信息
        :type Path: str
        :param _Backend: backend 配置
        :type Backend: :class:`tencentcloud.tem.v20201221.models.IngressRuleBackend`
        """
        self._Path = None
        self._Backend = None

    @property
    def Path(self):
        r"""path 信息
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Backend(self):
        r"""backend 配置
        :rtype: :class:`tencentcloud.tem.v20201221.models.IngressRuleBackend`
        """
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
    r"""Ingress Rule Value 配置

    """

    def __init__(self):
        r"""
        :param _Paths: rule 整体配置
        :type Paths: list of IngressRulePath
        """
        self._Paths = None

    @property
    def Paths(self):
        r"""rule 整体配置
        :rtype: list of IngressRulePath
        """
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
    r"""ingress tls 配置

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
        r"""host 数组, 空数组表示全部域名的默认证书
        :rtype: list of str
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def SecretName(self):
        r"""secret name，如使用证书，则填空字符串
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def CertificateId(self):
        r"""SSL Certificate Id
        :rtype: str
        """
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
        


class LogOutputConf(AbstractModel):
    r"""日志输出配置

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
        r"""日志消费端类型
        :rtype: str
        """
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType

    @property
    def ClsLogsetName(self):
        r"""cls日志集
        :rtype: str
        """
        return self._ClsLogsetName

    @ClsLogsetName.setter
    def ClsLogsetName(self, ClsLogsetName):
        self._ClsLogsetName = ClsLogsetName

    @property
    def ClsLogTopicId(self):
        r"""cls日志主题
        :rtype: str
        """
        return self._ClsLogTopicId

    @ClsLogTopicId.setter
    def ClsLogTopicId(self, ClsLogTopicId):
        self._ClsLogTopicId = ClsLogTopicId

    @property
    def ClsLogsetId(self):
        r"""cls日志集id
        :rtype: str
        """
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsLogTopicName(self):
        r"""cls日志名称
        :rtype: str
        """
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
        


class ModifyIngressRequest(AbstractModel):
    r"""ModifyIngress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ingress: Ingress 规则配置
        :type Ingress: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._Ingress = None
        self._SourceChannel = None

    @property
    def Ingress(self):
        r"""Ingress 规则配置
        :rtype: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
        """
        return self._Ingress

    @Ingress.setter
    def Ingress(self, Ingress):
        self._Ingress = Ingress

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
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
    r"""ModifyIngress返回参数结构体

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
        r"""创建成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyNamespaceRequest(AbstractModel):
    r"""ModifyNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NamespaceId: 环境id
        :type NamespaceId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _Description: 命名空间描述
        :type Description: str
        :param _Vpc: 私有网络名称
        :type Vpc: str
        :param _SubnetIds: 子网网络
        :type SubnetIds: list of str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._NamespaceId = None
        self._NamespaceName = None
        self._Description = None
        self._Vpc = None
        self._SubnetIds = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        r"""环境id
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def NamespaceName(self):
        r"""命名空间名称
        :rtype: str
        """
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Description(self):
        r"""命名空间描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Vpc(self):
        r"""私有网络名称
        :rtype: str
        """
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def SubnetIds(self):
        r"""子网网络
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._NamespaceName = params.get("NamespaceName")
        self._Description = params.get("Description")
        self._Vpc = params.get("Vpc")
        self._SubnetIds = params.get("SubnetIds")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNamespaceResponse(AbstractModel):
    r"""ModifyNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 成功时为命名空间ID，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""成功时为命名空间ID，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyServiceInfoRequest(AbstractModel):
    r"""ModifyServiceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _Description: 描述
        :type Description: str
        :param _SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self._ServiceId = None
        self._Description = None
        self._SourceChannel = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Description = params.get("Description")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceInfoResponse(AbstractModel):
    r"""ModifyServiceInfo返回参数结构体

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
        r"""成功与否
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class MountedSettingConf(AbstractModel):
    r"""挂载配置信息

    """

    def __init__(self):
        r"""
        :param _ConfigDataName: 配置名称
        :type ConfigDataName: str
        :param _MountedPath: 挂载路径
        :type MountedPath: str
        :param _Data: 配置内容
        :type Data: list of Pair
        """
        self._ConfigDataName = None
        self._MountedPath = None
        self._Data = None

    @property
    def ConfigDataName(self):
        r"""配置名称
        :rtype: str
        """
        return self._ConfigDataName

    @ConfigDataName.setter
    def ConfigDataName(self, ConfigDataName):
        self._ConfigDataName = ConfigDataName

    @property
    def MountedPath(self):
        r"""挂载路径
        :rtype: str
        """
        return self._MountedPath

    @MountedPath.setter
    def MountedPath(self, MountedPath):
        self._MountedPath = MountedPath

    @property
    def Data(self):
        r"""配置内容
        :rtype: list of Pair
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._ConfigDataName = params.get("ConfigDataName")
        self._MountedPath = params.get("MountedPath")
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
        


class NamespacePage(AbstractModel):
    r"""命名空间分页

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
        """
        self._Records = None
        self._Total = None
        self._Size = None
        self._Pages = None

    @property
    def Records(self):
        r"""分页内容
        :rtype: list of TemNamespaceInfo
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Size(self):
        r"""条目数
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Pages(self):
        r"""页数
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pair(AbstractModel):
    r"""键值对

    """

    def __init__(self):
        r"""
        :param _Key: 建
        :type Key: str
        :param _Value: 值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""建
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""值
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
        


class PortMapping(AbstractModel):
    r"""服务端口映射

    """

    def __init__(self):
        r"""
        :param _Port: 端口
        :type Port: int
        :param _TargetPort: 映射端口
        :type TargetPort: int
        :param _Protocol: 协议栈 TCP/UDP
        :type Protocol: str
        """
        self._Port = None
        self._TargetPort = None
        self._Protocol = None

    @property
    def Port(self):
        r"""端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetPort(self):
        r"""映射端口
        :rtype: int
        """
        return self._TargetPort

    @TargetPort.setter
    def TargetPort(self, TargetPort):
        self._TargetPort = TargetPort

    @property
    def Protocol(self):
        r"""协议栈 TCP/UDP
        :rtype: str
        """
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
        


class RestartServiceRunPodRequest(AbstractModel):
    r"""RestartServiceRunPod请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NamespaceId: 环境id
        :type NamespaceId: str
        :param _ServiceId: 服务名id
        :type ServiceId: str
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
        self._NamespaceId = None
        self._ServiceId = None
        self._PodName = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        r"""环境id
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def ServiceId(self):
        r"""服务名id
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def PodName(self):
        r"""名字
        :rtype: str
        """
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Limit(self):
        r"""单页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页下标
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        r"""pod状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceChannel(self):
        r"""来源渠道
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._ServiceId = params.get("ServiceId")
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
        


class RestartServiceRunPodResponse(AbstractModel):
    r"""RestartServiceRunPod返回参数结构体

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
        r"""返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class RunVersionPod(AbstractModel):
    r"""版本pod

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
        """
        self._Webshell = None
        self._PodId = None
        self._Status = None
        self._CreateTime = None
        self._PodIp = None
        self._Zone = None
        self._DeployVersion = None
        self._RestartCount = None

    @property
    def Webshell(self):
        r"""shell地址
        :rtype: str
        """
        return self._Webshell

    @Webshell.setter
    def Webshell(self, Webshell):
        self._Webshell = Webshell

    @property
    def PodId(self):
        r"""pod的id
        :rtype: str
        """
        return self._PodId

    @PodId.setter
    def PodId(self, PodId):
        self._PodId = PodId

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
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PodIp(self):
        r"""实例的ip
        :rtype: str
        """
        return self._PodIp

    @PodIp.setter
    def PodIp(self, PodIp):
        self._PodIp = PodIp

    @property
    def Zone(self):
        r"""可用区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DeployVersion(self):
        r"""部署版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def RestartCount(self):
        r"""重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount


    def _deserialize(self, params):
        self._Webshell = params.get("Webshell")
        self._PodId = params.get("PodId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._PodIp = params.get("PodIp")
        self._Zone = params.get("Zone")
        self._DeployVersion = params.get("DeployVersion")
        self._RestartCount = params.get("RestartCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageConf(AbstractModel):
    r"""存储卷配置

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
        r"""存储卷名称
        :rtype: str
        """
        return self._StorageVolName

    @StorageVolName.setter
    def StorageVolName(self, StorageVolName):
        self._StorageVolName = StorageVolName

    @property
    def StorageVolPath(self):
        r"""存储卷路径
        :rtype: str
        """
        return self._StorageVolPath

    @StorageVolPath.setter
    def StorageVolPath(self, StorageVolPath):
        self._StorageVolPath = StorageVolPath

    @property
    def StorageVolIp(self):
        r"""存储卷IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
    r"""数据卷挂载信息

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
        r"""数据卷名
        :rtype: str
        """
        return self._VolumeName

    @VolumeName.setter
    def VolumeName(self, VolumeName):
        self._VolumeName = VolumeName

    @property
    def MountPath(self):
        r"""数据卷绑定路径
        :rtype: str
        """
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
        


class TemNamespaceInfo(AbstractModel):
    r"""命名空间对象

    """

    def __init__(self):
        r"""
        :param _NamespaceId: 命名空间id
        :type NamespaceId: str
        :param _Channel: 渠道
        :type Channel: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _Region: 区域名称
        :type Region: str
        :param _Description: 命名空间描述
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
        :param _ServiceNum: 服务数
        :type ServiceNum: int
        :param _RunInstancesNum: 运行实例数
        :type RunInstancesNum: int
        :param _SubnetId: 子网络
        :type SubnetId: str
        :param _TcbEnvStatus: tcb环境状态
        :type TcbEnvStatus: str
        :param _ClusterStatus: eks cluster status
        :type ClusterStatus: str
        :param _EnableTswTraceService: 是否开启tsw
        :type EnableTswTraceService: bool
        """
        self._NamespaceId = None
        self._Channel = None
        self._NamespaceName = None
        self._Region = None
        self._Description = None
        self._Status = None
        self._Vpc = None
        self._CreateDate = None
        self._ModifyDate = None
        self._Modifier = None
        self._Creator = None
        self._ServiceNum = None
        self._RunInstancesNum = None
        self._SubnetId = None
        self._TcbEnvStatus = None
        self._ClusterStatus = None
        self._EnableTswTraceService = None

    @property
    def NamespaceId(self):
        r"""命名空间id
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Channel(self):
        r"""渠道
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def NamespaceName(self):
        r"""命名空间名称
        :rtype: str
        """
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Region(self):
        r"""区域名称
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Description(self):
        r"""命名空间描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        r"""状态,1:已销毁;0:正常
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vpc(self):
        r"""vpc网络
        :rtype: str
        """
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def CreateDate(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        r"""修改时间
        :rtype: str
        """
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def Modifier(self):
        r"""修改人
        :rtype: str
        """
        return self._Modifier

    @Modifier.setter
    def Modifier(self, Modifier):
        self._Modifier = Modifier

    @property
    def Creator(self):
        r"""创建人
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def ServiceNum(self):
        r"""服务数
        :rtype: int
        """
        return self._ServiceNum

    @ServiceNum.setter
    def ServiceNum(self, ServiceNum):
        self._ServiceNum = ServiceNum

    @property
    def RunInstancesNum(self):
        r"""运行实例数
        :rtype: int
        """
        return self._RunInstancesNum

    @RunInstancesNum.setter
    def RunInstancesNum(self, RunInstancesNum):
        self._RunInstancesNum = RunInstancesNum

    @property
    def SubnetId(self):
        r"""子网络
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def TcbEnvStatus(self):
        r"""tcb环境状态
        :rtype: str
        """
        return self._TcbEnvStatus

    @TcbEnvStatus.setter
    def TcbEnvStatus(self, TcbEnvStatus):
        self._TcbEnvStatus = TcbEnvStatus

    @property
    def ClusterStatus(self):
        r"""eks cluster status
        :rtype: str
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def EnableTswTraceService(self):
        r"""是否开启tsw
        :rtype: bool
        """
        return self._EnableTswTraceService

    @EnableTswTraceService.setter
    def EnableTswTraceService(self, EnableTswTraceService):
        self._EnableTswTraceService = EnableTswTraceService


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._Channel = params.get("Channel")
        self._NamespaceName = params.get("NamespaceName")
        self._Region = params.get("Region")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Vpc = params.get("Vpc")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        self._Modifier = params.get("Modifier")
        self._Creator = params.get("Creator")
        self._ServiceNum = params.get("ServiceNum")
        self._RunInstancesNum = params.get("RunInstancesNum")
        self._SubnetId = params.get("SubnetId")
        self._TcbEnvStatus = params.get("TcbEnvStatus")
        self._ClusterStatus = params.get("ClusterStatus")
        self._EnableTswTraceService = params.get("EnableTswTraceService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        