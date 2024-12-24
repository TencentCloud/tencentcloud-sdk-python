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


class ApplicationVersion(AbstractModel):
    """应用版本。

    """

    def __init__(self):
        r"""
        :param _Type: 版本类型。
        :type Type: str
        :param _ApplicationVersionId: 版本ID。
        :type ApplicationVersionId: str
        :param _Name: 发布名称。
        :type Name: str
        :param _Description: 发布描述。
        :type Description: str
        :param _Entrypoint: 入口文件。
        :type Entrypoint: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _CreatorName: 创建者名称。
        :type CreatorName: str
        :param _CreatorId: 创建者ID。
        :type CreatorId: str
        :param _GitInfo: Git信息。
        :type GitInfo: str
        :param _GitSource: Git信息。
        :type GitSource: :class:`tencentcloud.omics.v20221128.models.GitInfo`
        :param _CosSource: COS信息。
        :type CosSource: :class:`tencentcloud.omics.v20221128.models.CosFileInfo`
        """
        self._Type = None
        self._ApplicationVersionId = None
        self._Name = None
        self._Description = None
        self._Entrypoint = None
        self._CreateTime = None
        self._CreatorName = None
        self._CreatorId = None
        self._GitInfo = None
        self._GitSource = None
        self._CosSource = None

    @property
    def Type(self):
        """版本类型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ApplicationVersionId(self):
        """版本ID。
        :rtype: str
        """
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId

    @property
    def Name(self):
        """发布名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """发布描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Entrypoint(self):
        """入口文件。
        :rtype: str
        """
        return self._Entrypoint

    @Entrypoint.setter
    def Entrypoint(self, Entrypoint):
        self._Entrypoint = Entrypoint

    @property
    def CreateTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreatorName(self):
        """创建者名称。
        :rtype: str
        """
        return self._CreatorName

    @CreatorName.setter
    def CreatorName(self, CreatorName):
        self._CreatorName = CreatorName

    @property
    def CreatorId(self):
        """创建者ID。
        :rtype: str
        """
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def GitInfo(self):
        warnings.warn("parameter `GitInfo` is deprecated", DeprecationWarning) 

        """Git信息。
        :rtype: str
        """
        return self._GitInfo

    @GitInfo.setter
    def GitInfo(self, GitInfo):
        warnings.warn("parameter `GitInfo` is deprecated", DeprecationWarning) 

        self._GitInfo = GitInfo

    @property
    def GitSource(self):
        """Git信息。
        :rtype: :class:`tencentcloud.omics.v20221128.models.GitInfo`
        """
        return self._GitSource

    @GitSource.setter
    def GitSource(self, GitSource):
        self._GitSource = GitSource

    @property
    def CosSource(self):
        """COS信息。
        :rtype: :class:`tencentcloud.omics.v20221128.models.CosFileInfo`
        """
        return self._CosSource

    @CosSource.setter
    def CosSource(self, CosSource):
        self._CosSource = CosSource


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Entrypoint = params.get("Entrypoint")
        self._CreateTime = params.get("CreateTime")
        self._CreatorName = params.get("CreatorName")
        self._CreatorId = params.get("CreatorId")
        self._GitInfo = params.get("GitInfo")
        if params.get("GitSource") is not None:
            self._GitSource = GitInfo()
            self._GitSource._deserialize(params.get("GitSource"))
        if params.get("CosSource") is not None:
            self._CosSource = CosFileInfo()
            self._CosSource._deserialize(params.get("CosSource"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CVMOption(AbstractModel):
    """云服务器配置。

    """

    def __init__(self):
        r"""
        :param _Zone: 云服务器可用区。
        :type Zone: str
        :param _InstanceType: 云服务器实例规格。
        :type InstanceType: str
        """
        self._Zone = None
        self._InstanceType = None

    @property
    def Zone(self):
        """云服务器可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        """云服务器实例规格。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheInfo(AbstractModel):
    """缓存信息。

    """

    def __init__(self):
        r"""
        :param _CacheClearDelay: 缓存清理时间(小时)。
        :type CacheClearDelay: int
        :param _CacheClearTime: 缓存清理计划时间。
        :type CacheClearTime: str
        :param _CacheCleared: 缓存是否已被清理。
        :type CacheCleared: bool
        """
        self._CacheClearDelay = None
        self._CacheClearTime = None
        self._CacheCleared = None

    @property
    def CacheClearDelay(self):
        """缓存清理时间(小时)。
        :rtype: int
        """
        return self._CacheClearDelay

    @CacheClearDelay.setter
    def CacheClearDelay(self, CacheClearDelay):
        self._CacheClearDelay = CacheClearDelay

    @property
    def CacheClearTime(self):
        """缓存清理计划时间。
        :rtype: str
        """
        return self._CacheClearTime

    @CacheClearTime.setter
    def CacheClearTime(self, CacheClearTime):
        self._CacheClearTime = CacheClearTime

    @property
    def CacheCleared(self):
        """缓存是否已被清理。
        :rtype: bool
        """
        return self._CacheCleared

    @CacheCleared.setter
    def CacheCleared(self, CacheCleared):
        self._CacheCleared = CacheCleared


    def _deserialize(self, params):
        self._CacheClearDelay = params.get("CacheClearDelay")
        self._CacheClearTime = params.get("CacheClearTime")
        self._CacheCleared = params.get("CacheCleared")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterOption(AbstractModel):
    """计算集群配置。

    """

    def __init__(self):
        r"""
        :param _Zone: 计算集群可用区。
        :type Zone: str
        :param _Type: 计算集群类型，取值范围：
- KUBERNETES
        :type Type: str
        :param _ServiceCidr: 计算集群Service CIDR，不能与VPC网段重合。
        :type ServiceCidr: str
        :param _ResourceQuota: 资源配额。
        :type ResourceQuota: :class:`tencentcloud.omics.v20221128.models.ResourceQuota`
        :param _LimitRange: 限制范围。
        :type LimitRange: :class:`tencentcloud.omics.v20221128.models.LimitRange`
        """
        self._Zone = None
        self._Type = None
        self._ServiceCidr = None
        self._ResourceQuota = None
        self._LimitRange = None

    @property
    def Zone(self):
        """计算集群可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Type(self):
        """计算集群类型，取值范围：
- KUBERNETES
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ServiceCidr(self):
        """计算集群Service CIDR，不能与VPC网段重合。
        :rtype: str
        """
        return self._ServiceCidr

    @ServiceCidr.setter
    def ServiceCidr(self, ServiceCidr):
        self._ServiceCidr = ServiceCidr

    @property
    def ResourceQuota(self):
        """资源配额。
        :rtype: :class:`tencentcloud.omics.v20221128.models.ResourceQuota`
        """
        return self._ResourceQuota

    @ResourceQuota.setter
    def ResourceQuota(self, ResourceQuota):
        self._ResourceQuota = ResourceQuota

    @property
    def LimitRange(self):
        """限制范围。
        :rtype: :class:`tencentcloud.omics.v20221128.models.LimitRange`
        """
        return self._LimitRange

    @LimitRange.setter
    def LimitRange(self, LimitRange):
        self._LimitRange = LimitRange


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Type = params.get("Type")
        self._ServiceCidr = params.get("ServiceCidr")
        if params.get("ResourceQuota") is not None:
            self._ResourceQuota = ResourceQuota()
            self._ResourceQuota._deserialize(params.get("ResourceQuota"))
        if params.get("LimitRange") is not None:
            self._LimitRange = LimitRange()
            self._LimitRange._deserialize(params.get("LimitRange"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosFileInfo(AbstractModel):
    """COS 文件信息

    """

    def __init__(self):
        r"""
        :param _Bucket: 存储桶。
        :type Bucket: str
        :param _Uri: COS文件地址。
        :type Uri: str
        :param _Region: 地域。
        :type Region: str
        """
        self._Bucket = None
        self._Uri = None
        self._Region = None

    @property
    def Bucket(self):
        """存储桶。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Uri(self):
        """COS文件地址。
        :rtype: str
        """
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def Region(self):
        """地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Uri = params.get("Uri")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 环境名称。
        :type Name: str
        :param _Config: 环境配置信息。
        :type Config: :class:`tencentcloud.omics.v20221128.models.EnvironmentConfig`
        :param _Description: 环境描述。
        :type Description: str
        :param _IsDefault: 是否为默认环境。
        :type IsDefault: bool
        """
        self._Name = None
        self._Config = None
        self._Description = None
        self._IsDefault = None

    @property
    def Name(self):
        """环境名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Config(self):
        """环境配置信息。
        :rtype: :class:`tencentcloud.omics.v20221128.models.EnvironmentConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Description(self):
        """环境描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsDefault(self):
        """是否为默认环境。
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Config") is not None:
            self._Config = EnvironmentConfig()
            self._Config._deserialize(params.get("Config"))
        self._Description = params.get("Description")
        self._IsDefault = params.get("IsDefault")
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
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param _WorkflowUuid: 工作流UUID。
        :type WorkflowUuid: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvironmentId = None
        self._WorkflowUuid = None
        self._RequestId = None

    @property
    def EnvironmentId(self):
        """环境ID。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def WorkflowUuid(self):
        """工作流UUID。
        :rtype: str
        """
        return self._WorkflowUuid

    @WorkflowUuid.setter
    def WorkflowUuid(self, WorkflowUuid):
        self._WorkflowUuid = WorkflowUuid

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._WorkflowUuid = params.get("WorkflowUuid")
        self._RequestId = params.get("RequestId")


class CreateVolumeRequest(AbstractModel):
    """CreateVolume请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param _Name: 名称。
        :type Name: str
        :param _Type: 缓存卷类型，取值范围：
* SHARED：多点挂载共享存储
        :type Type: str
        :param _Spec: 缓存卷规格，取值范围：

- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
        :type Spec: str
        :param _Description: 描述。
        :type Description: str
        :param _Capacity: 缓存卷大小（GB），Turbo系列需要指定。
        :type Capacity: int
        """
        self._EnvironmentId = None
        self._Name = None
        self._Type = None
        self._Spec = None
        self._Description = None
        self._Capacity = None

    @property
    def EnvironmentId(self):
        """环境ID。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        """名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """缓存卷类型，取值范围：
* SHARED：多点挂载共享存储
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Spec(self):
        """缓存卷规格，取值范围：

- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def Description(self):
        """描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Capacity(self):
        """缓存卷大小（GB），Turbo系列需要指定。
        :rtype: int
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Spec = params.get("Spec")
        self._Description = params.get("Description")
        self._Capacity = params.get("Capacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVolumeResponse(AbstractModel):
    """CreateVolume返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VolumeId: 缓存卷ID。
        :type VolumeId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VolumeId = None
        self._RequestId = None

    @property
    def VolumeId(self):
        """缓存卷ID。
        :rtype: str
        """
        return self._VolumeId

    @VolumeId.setter
    def VolumeId(self, VolumeId):
        self._VolumeId = VolumeId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VolumeId = params.get("VolumeId")
        self._RequestId = params.get("RequestId")


class DatabaseOption(AbstractModel):
    """数据库配置。

    """

    def __init__(self):
        r"""
        :param _Zone: 数据库可用区。
        :type Zone: str
        """
        self._Zone = None

    @property
    def Zone(self):
        """数据库可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentRequest(AbstractModel):
    """DeleteEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        """
        self._EnvironmentId = None

    @property
    def EnvironmentId(self):
        """环境ID。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentResponse(AbstractModel):
    """DeleteEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkflowUuid: 工作流UUID。
        :type WorkflowUuid: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkflowUuid = None
        self._RequestId = None

    @property
    def WorkflowUuid(self):
        """工作流UUID。
        :rtype: str
        """
        return self._WorkflowUuid

    @WorkflowUuid.setter
    def WorkflowUuid(self, WorkflowUuid):
        self._WorkflowUuid = WorkflowUuid

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WorkflowUuid = params.get("WorkflowUuid")
        self._RequestId = params.get("RequestId")


class DeleteVolumeDataRequest(AbstractModel):
    """DeleteVolumeData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VolumeId: 缓存卷ID。
        :type VolumeId: str
        :param _Path: 需要删除的路径。
        :type Path: str
        """
        self._VolumeId = None
        self._Path = None

    @property
    def VolumeId(self):
        """缓存卷ID。
        :rtype: str
        """
        return self._VolumeId

    @VolumeId.setter
    def VolumeId(self, VolumeId):
        self._VolumeId = VolumeId

    @property
    def Path(self):
        """需要删除的路径。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._VolumeId = params.get("VolumeId")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVolumeDataResponse(AbstractModel):
    """DeleteVolumeData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteVolumeRequest(AbstractModel):
    """DeleteVolume请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VolumeId: 缓存卷ID。
        :type VolumeId: str
        """
        self._VolumeId = None

    @property
    def VolumeId(self):
        """缓存卷ID。
        :rtype: str
        """
        return self._VolumeId

    @VolumeId.setter
    def VolumeId(self, VolumeId):
        self._VolumeId = VolumeId


    def _deserialize(self, params):
        self._VolumeId = params.get("VolumeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVolumeResponse(AbstractModel):
    """DeleteVolume返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Filters: 过滤器，支持过滤字段：
- EnvironmentId：环境ID
- Name：名称
- Status：环境状态
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤器，支持过滤字段：
- EnvironmentId：环境ID
- Name：名称
- Status：环境状态
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
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
        :param _TotalCount: 符合条件的数量。
        :type TotalCount: int
        :param _Environments: 环境详情列表。
        :type Environments: list of Environment
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Environments = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Environments(self):
        """环境详情列表。
        :rtype: list of Environment
        """
        return self._Environments

    @Environments.setter
    def Environments(self, Environments):
        self._Environments = Environments

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeRunGroupsRequest(AbstractModel):
    """DescribeRunGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID。
（不填使用指定地域下的默认项目）
        :type ProjectId: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤器，支持过滤字段：
- Name：任务批次名称
- RunGroupId：任务批次ID
- Status：任务批次状态
- ApplicationId：应用ID
- Type：类型（支持WDL，NEXTFLOW）
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        """项目ID。
（不填使用指定地域下的默认项目）
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Limit(self):
        """返回数量，默认为10，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """过滤器，支持过滤字段：
- Name：任务批次名称
- RunGroupId：任务批次ID
- Status：任务批次状态
- ApplicationId：应用ID
- Type：类型（支持WDL，NEXTFLOW）
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRunGroupsResponse(AbstractModel):
    """DescribeRunGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的数量。
        :type TotalCount: int
        :param _RunGroups: 任务批次列表。
        :type RunGroups: list of RunGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RunGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RunGroups(self):
        """任务批次列表。
        :rtype: list of RunGroup
        """
        return self._RunGroups

    @RunGroups.setter
    def RunGroups(self, RunGroups):
        self._RunGroups = RunGroups

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RunGroups") is not None:
            self._RunGroups = []
            for item in params.get("RunGroups"):
                obj = RunGroup()
                obj._deserialize(item)
                self._RunGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRunsRequest(AbstractModel):
    """DescribeRuns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID。
（不填使用指定地域下的默认项目）
        :type ProjectId: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤器，支持过滤字段：
- RunGroupId：任务批次ID
- Status：任务状态
- RunUuid：任务UUID
- ApplicationId：应用ID
- UserDefinedId：用户定义ID（批量运行表格第一列）
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        """项目ID。
（不填使用指定地域下的默认项目）
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Limit(self):
        """返回数量，默认为10，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """过滤器，支持过滤字段：
- RunGroupId：任务批次ID
- Status：任务状态
- RunUuid：任务UUID
- ApplicationId：应用ID
- UserDefinedId：用户定义ID（批量运行表格第一列）
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRunsResponse(AbstractModel):
    """DescribeRuns返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的数量。
        :type TotalCount: int
        :param _Runs: 任务列表。
        :type Runs: list of Run
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Runs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Runs(self):
        """任务列表。
        :rtype: list of Run
        """
        return self._Runs

    @Runs.setter
    def Runs(self, Runs):
        self._Runs = Runs

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Runs") is not None:
            self._Runs = []
            for item in params.get("Runs"):
                obj = Run()
                obj._deserialize(item)
                self._Runs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤器，支持过滤字段：
- Name：表格名称
- TableId：表格ID
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        """项目ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Limit(self):
        """返回数量，默认为10，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """过滤器，支持过滤字段：
- Name：表格名称
- TableId：表格ID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesResponse(AbstractModel):
    """DescribeTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数。
        :type TotalCount: int
        :param _Tables: 表格列表。
        :type Tables: list of Table
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tables = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """结果总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tables(self):
        """表格列表。
        :rtype: list of Table
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = Table()
                obj._deserialize(item)
                self._Tables.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTablesRowsRequest(AbstractModel):
    """DescribeTablesRows请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _TableId: 表格ID。
        :type TableId: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤器，支持过滤字段：
- Tr：表格数据，支持模糊查询
- TableRowUuid：表格行UUID
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._TableId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        """项目ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TableId(self):
        """表格ID。
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def Limit(self):
        """返回数量，默认为10，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """过滤器，支持过滤字段：
- Tr：表格数据，支持模糊查询
- TableRowUuid：表格行UUID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TableId = params.get("TableId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesRowsResponse(AbstractModel):
    """DescribeTablesRows返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数。
        :type TotalCount: int
        :param _Rows: 表格行列表。
        :type Rows: list of TableRow
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """结果总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        """表格行列表。
        :rtype: list of TableRow
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TableRow()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVolumesRequest(AbstractModel):
    """DescribeVolumes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤器，支持过滤字段：
- Name：名称
- IsDefault：是否为默认
        :type Filters: list of Filter
        """
        self._EnvironmentId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def EnvironmentId(self):
        """环境ID。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """过滤器，支持过滤字段：
- Name：名称
- IsDefault：是否为默认
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVolumesResponse(AbstractModel):
    """DescribeVolumes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Volumes: 缓存卷。
        :type Volumes: list of Volume
        :param _TotalCount: 符合条件的数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Volumes = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Volumes(self):
        """缓存卷。
        :rtype: list of Volume
        """
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def TotalCount(self):
        """符合条件的数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self._Volumes.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """组学平台环境详情。

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param _Name: 环境名称。
        :type Name: str
        :param _Description: 环境描述信息。
        :type Description: str
        :param _Region: 环境地域。
        :type Region: str
        :param _Type: 环境类型，取值范围：
- KUBERNETES：Kubernetes容器集群
- HPC：HPC高性能计算集群
        :type Type: str
        :param _Status: 环境状态，取值范围：
- INITIALIZING：创建中
- INITIALIZATION_ERROR：创建失败
- RUNNING：运行中
- ERROR：异常
- DELETING：正在删除
- DELETE_ERROR：删除失败
        :type Status: str
        :param _Available: 环境是否可用。环境需要可用才能投递计算任务。
        :type Available: bool
        :param _IsDefault: 环境是否为默认环境。
        :type IsDefault: bool
        :param _IsManaged: 环境是否为托管环境。
        :type IsManaged: bool
        :param _Message: 环境信息。
        :type Message: str
        :param _ResourceIds: 云资源ID。
        :type ResourceIds: :class:`tencentcloud.omics.v20221128.models.ResourceIds`
        :param _LastWorkflowUuid: 上个工作流UUID。
        :type LastWorkflowUuid: str
        :param _CreationTime: 创建时间。
        :type CreationTime: str
        """
        self._EnvironmentId = None
        self._Name = None
        self._Description = None
        self._Region = None
        self._Type = None
        self._Status = None
        self._Available = None
        self._IsDefault = None
        self._IsManaged = None
        self._Message = None
        self._ResourceIds = None
        self._LastWorkflowUuid = None
        self._CreationTime = None

    @property
    def EnvironmentId(self):
        """环境ID。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        """环境名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """环境描述信息。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Region(self):
        """环境地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Type(self):
        """环境类型，取值范围：
- KUBERNETES：Kubernetes容器集群
- HPC：HPC高性能计算集群
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """环境状态，取值范围：
- INITIALIZING：创建中
- INITIALIZATION_ERROR：创建失败
- RUNNING：运行中
- ERROR：异常
- DELETING：正在删除
- DELETE_ERROR：删除失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Available(self):
        """环境是否可用。环境需要可用才能投递计算任务。
        :rtype: bool
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def IsDefault(self):
        """环境是否为默认环境。
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def IsManaged(self):
        """环境是否为托管环境。
        :rtype: bool
        """
        return self._IsManaged

    @IsManaged.setter
    def IsManaged(self, IsManaged):
        self._IsManaged = IsManaged

    @property
    def Message(self):
        """环境信息。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ResourceIds(self):
        """云资源ID。
        :rtype: :class:`tencentcloud.omics.v20221128.models.ResourceIds`
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def LastWorkflowUuid(self):
        """上个工作流UUID。
        :rtype: str
        """
        return self._LastWorkflowUuid

    @LastWorkflowUuid.setter
    def LastWorkflowUuid(self, LastWorkflowUuid):
        self._LastWorkflowUuid = LastWorkflowUuid

    @property
    def CreationTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Region = params.get("Region")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Available = params.get("Available")
        self._IsDefault = params.get("IsDefault")
        self._IsManaged = params.get("IsManaged")
        self._Message = params.get("Message")
        if params.get("ResourceIds") is not None:
            self._ResourceIds = ResourceIds()
            self._ResourceIds._deserialize(params.get("ResourceIds"))
        self._LastWorkflowUuid = params.get("LastWorkflowUuid")
        self._CreationTime = params.get("CreationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentConfig(AbstractModel):
    """环境配置。

    """

    def __init__(self):
        r"""
        :param _VPCOption: 私有网络配置。
        :type VPCOption: :class:`tencentcloud.omics.v20221128.models.VPCOption`
        :param _ClusterOption: 计算集群配置。
        :type ClusterOption: :class:`tencentcloud.omics.v20221128.models.ClusterOption`
        :param _DatabaseOption: 数据库配置。
        :type DatabaseOption: :class:`tencentcloud.omics.v20221128.models.DatabaseOption`
        :param _StorageOption: 存储配置。
        :type StorageOption: :class:`tencentcloud.omics.v20221128.models.StorageOption`
        :param _CVMOption: 云服务器配置。
        :type CVMOption: :class:`tencentcloud.omics.v20221128.models.CVMOption`
        :param _SecurityGroupOption: 安全组配置。
        :type SecurityGroupOption: :class:`tencentcloud.omics.v20221128.models.SecurityGroupOption`
        """
        self._VPCOption = None
        self._ClusterOption = None
        self._DatabaseOption = None
        self._StorageOption = None
        self._CVMOption = None
        self._SecurityGroupOption = None

    @property
    def VPCOption(self):
        """私有网络配置。
        :rtype: :class:`tencentcloud.omics.v20221128.models.VPCOption`
        """
        return self._VPCOption

    @VPCOption.setter
    def VPCOption(self, VPCOption):
        self._VPCOption = VPCOption

    @property
    def ClusterOption(self):
        """计算集群配置。
        :rtype: :class:`tencentcloud.omics.v20221128.models.ClusterOption`
        """
        return self._ClusterOption

    @ClusterOption.setter
    def ClusterOption(self, ClusterOption):
        self._ClusterOption = ClusterOption

    @property
    def DatabaseOption(self):
        """数据库配置。
        :rtype: :class:`tencentcloud.omics.v20221128.models.DatabaseOption`
        """
        return self._DatabaseOption

    @DatabaseOption.setter
    def DatabaseOption(self, DatabaseOption):
        self._DatabaseOption = DatabaseOption

    @property
    def StorageOption(self):
        """存储配置。
        :rtype: :class:`tencentcloud.omics.v20221128.models.StorageOption`
        """
        return self._StorageOption

    @StorageOption.setter
    def StorageOption(self, StorageOption):
        self._StorageOption = StorageOption

    @property
    def CVMOption(self):
        """云服务器配置。
        :rtype: :class:`tencentcloud.omics.v20221128.models.CVMOption`
        """
        return self._CVMOption

    @CVMOption.setter
    def CVMOption(self, CVMOption):
        self._CVMOption = CVMOption

    @property
    def SecurityGroupOption(self):
        """安全组配置。
        :rtype: :class:`tencentcloud.omics.v20221128.models.SecurityGroupOption`
        """
        return self._SecurityGroupOption

    @SecurityGroupOption.setter
    def SecurityGroupOption(self, SecurityGroupOption):
        self._SecurityGroupOption = SecurityGroupOption


    def _deserialize(self, params):
        if params.get("VPCOption") is not None:
            self._VPCOption = VPCOption()
            self._VPCOption._deserialize(params.get("VPCOption"))
        if params.get("ClusterOption") is not None:
            self._ClusterOption = ClusterOption()
            self._ClusterOption._deserialize(params.get("ClusterOption"))
        if params.get("DatabaseOption") is not None:
            self._DatabaseOption = DatabaseOption()
            self._DatabaseOption._deserialize(params.get("DatabaseOption"))
        if params.get("StorageOption") is not None:
            self._StorageOption = StorageOption()
            self._StorageOption._deserialize(params.get("StorageOption"))
        if params.get("CVMOption") is not None:
            self._CVMOption = CVMOption()
            self._CVMOption._deserialize(params.get("CVMOption"))
        if params.get("SecurityGroupOption") is not None:
            self._SecurityGroupOption = SecurityGroupOption()
            self._SecurityGroupOption._deserialize(params.get("SecurityGroupOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecutionTime(AbstractModel):
    """执行时间。

    """

    def __init__(self):
        r"""
        :param _SubmitTime: 提交时间。
        :type SubmitTime: str
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        """
        self._SubmitTime = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SubmitTime(self):
        """提交时间。
        :rtype: str
        """
        return self._SubmitTime

    @SubmitTime.setter
    def SubmitTime(self, SubmitTime):
        self._SubmitTime = SubmitTime

    @property
    def StartTime(self):
        """开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SubmitTime = params.get("SubmitTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。

    - 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。

    - 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段。
        :type Name: str
        :param _Values: 过滤字段值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """过滤字段。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """过滤字段值。
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
        


class GetRunCallsRequest(AbstractModel):
    """GetRunCalls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RunUuid: 任务Uuid。
        :type RunUuid: str
        :param _Path: 作业路径
        :type Path: str
        :param _ProjectId: 项目ID。
（不填使用指定地域下的默认项目）
        :type ProjectId: str
        """
        self._RunUuid = None
        self._Path = None
        self._ProjectId = None

    @property
    def RunUuid(self):
        """任务Uuid。
        :rtype: str
        """
        return self._RunUuid

    @RunUuid.setter
    def RunUuid(self, RunUuid):
        self._RunUuid = RunUuid

    @property
    def Path(self):
        """作业路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def ProjectId(self):
        """项目ID。
（不填使用指定地域下的默认项目）
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._RunUuid = params.get("RunUuid")
        self._Path = params.get("Path")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRunCallsResponse(AbstractModel):
    """GetRunCalls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Calls: 作业详情。
        :type Calls: list of RunMetadata
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Calls = None
        self._RequestId = None

    @property
    def Calls(self):
        """作业详情。
        :rtype: list of RunMetadata
        """
        return self._Calls

    @Calls.setter
    def Calls(self, Calls):
        self._Calls = Calls

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Calls") is not None:
            self._Calls = []
            for item in params.get("Calls"):
                obj = RunMetadata()
                obj._deserialize(item)
                self._Calls.append(obj)
        self._RequestId = params.get("RequestId")


class GetRunMetadataFileRequest(AbstractModel):
    """GetRunMetadataFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RunUuid: 任务Uuid。
        :type RunUuid: str
        :param _ProjectId: 项目ID。
（不填使用指定地域下的默认项目）
        :type ProjectId: str
        :param _Key: 需要获取的文件名。

默认支持以下文件：
- nextflow.log

提交时NFOption中report指定为true时，额外支持以下文件：
- execution_report.html
- execution_timeline.html
- execution_trace.txt
- pipeline_dag.html
        :type Key: str
        :param _Keys: 需要批量获取的文件名。

默认支持以下文件：
- nextflow.log

提交时NFOption中report指定为true时，额外支持以下文件：
- execution_report.html
- execution_timeline.html
- execution_trace.txt
- pipeline_dag.html
        :type Keys: list of str
        """
        self._RunUuid = None
        self._ProjectId = None
        self._Key = None
        self._Keys = None

    @property
    def RunUuid(self):
        """任务Uuid。
        :rtype: str
        """
        return self._RunUuid

    @RunUuid.setter
    def RunUuid(self, RunUuid):
        self._RunUuid = RunUuid

    @property
    def ProjectId(self):
        """项目ID。
（不填使用指定地域下的默认项目）
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Key(self):
        """需要获取的文件名。

默认支持以下文件：
- nextflow.log

提交时NFOption中report指定为true时，额外支持以下文件：
- execution_report.html
- execution_timeline.html
- execution_trace.txt
- pipeline_dag.html
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Keys(self):
        """需要批量获取的文件名。

默认支持以下文件：
- nextflow.log

提交时NFOption中report指定为true时，额外支持以下文件：
- execution_report.html
- execution_timeline.html
- execution_trace.txt
- pipeline_dag.html
        :rtype: list of str
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys


    def _deserialize(self, params):
        self._RunUuid = params.get("RunUuid")
        self._ProjectId = params.get("ProjectId")
        self._Key = params.get("Key")
        self._Keys = params.get("Keys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRunMetadataFileResponse(AbstractModel):
    """GetRunMetadataFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CosSignedUrl: 文件预签名链接，一分钟内有效。
        :type CosSignedUrl: str
        :param _CosSignedUrls: 批量文件预签名链接，一分钟内有效。
        :type CosSignedUrls: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CosSignedUrl = None
        self._CosSignedUrls = None
        self._RequestId = None

    @property
    def CosSignedUrl(self):
        """文件预签名链接，一分钟内有效。
        :rtype: str
        """
        return self._CosSignedUrl

    @CosSignedUrl.setter
    def CosSignedUrl(self, CosSignedUrl):
        self._CosSignedUrl = CosSignedUrl

    @property
    def CosSignedUrls(self):
        """批量文件预签名链接，一分钟内有效。
        :rtype: list of str
        """
        return self._CosSignedUrls

    @CosSignedUrls.setter
    def CosSignedUrls(self, CosSignedUrls):
        self._CosSignedUrls = CosSignedUrls

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CosSignedUrl = params.get("CosSignedUrl")
        self._CosSignedUrls = params.get("CosSignedUrls")
        self._RequestId = params.get("RequestId")


class GetRunStatusRequest(AbstractModel):
    """GetRunStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RunUuid: 任务Uuid。
        :type RunUuid: str
        :param _ProjectId: 项目ID。
（不填使用指定地域下的默认项目）
        :type ProjectId: str
        """
        self._RunUuid = None
        self._ProjectId = None

    @property
    def RunUuid(self):
        """任务Uuid。
        :rtype: str
        """
        return self._RunUuid

    @RunUuid.setter
    def RunUuid(self, RunUuid):
        self._RunUuid = RunUuid

    @property
    def ProjectId(self):
        """项目ID。
（不填使用指定地域下的默认项目）
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._RunUuid = params.get("RunUuid")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRunStatusResponse(AbstractModel):
    """GetRunStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Metadata: 作业详情。
        :type Metadata: :class:`tencentcloud.omics.v20221128.models.RunMetadata`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Metadata = None
        self._RequestId = None

    @property
    def Metadata(self):
        """作业详情。
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunMetadata`
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Metadata") is not None:
            self._Metadata = RunMetadata()
            self._Metadata._deserialize(params.get("Metadata"))
        self._RequestId = params.get("RequestId")


class GitInfo(AbstractModel):
    """Git信息。

    """

    def __init__(self):
        r"""
        :param _GitHttpPath: Git地址。
        :type GitHttpPath: str
        :param _GitUserName: Git用户名。
        :type GitUserName: str
        :param _GitTokenOrPassword: Git密码或者Token。
        :type GitTokenOrPassword: str
        :param _Branch: 分支。
        :type Branch: str
        :param _Tag: 标签。
        :type Tag: str
        """
        self._GitHttpPath = None
        self._GitUserName = None
        self._GitTokenOrPassword = None
        self._Branch = None
        self._Tag = None

    @property
    def GitHttpPath(self):
        """Git地址。
        :rtype: str
        """
        return self._GitHttpPath

    @GitHttpPath.setter
    def GitHttpPath(self, GitHttpPath):
        self._GitHttpPath = GitHttpPath

    @property
    def GitUserName(self):
        """Git用户名。
        :rtype: str
        """
        return self._GitUserName

    @GitUserName.setter
    def GitUserName(self, GitUserName):
        self._GitUserName = GitUserName

    @property
    def GitTokenOrPassword(self):
        """Git密码或者Token。
        :rtype: str
        """
        return self._GitTokenOrPassword

    @GitTokenOrPassword.setter
    def GitTokenOrPassword(self, GitTokenOrPassword):
        self._GitTokenOrPassword = GitTokenOrPassword

    @property
    def Branch(self):
        """分支。
        :rtype: str
        """
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def Tag(self):
        """标签。
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._GitHttpPath = params.get("GitHttpPath")
        self._GitUserName = params.get("GitUserName")
        self._GitTokenOrPassword = params.get("GitTokenOrPassword")
        self._Branch = params.get("Branch")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportTableFileRequest(AbstractModel):
    """ImportTableFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 表格关联的项目ID。
        :type ProjectId: str
        :param _Name: 表格名称。最多支持200个字符。
        :type Name: str
        :param _CosUri: 表格文件Cos对象路径。
        :type CosUri: str
        :param _DataType: 表格文件中每列的数据类型，支持的类型包括：Int、Float、String、File、Boolean、Array[Int]、Array[Float]、Array[String]、Array[File]、Array[Boolean]
        :type DataType: list of str
        :param _Description: 表格描述。最多支持500个字符。
        :type Description: str
        """
        self._ProjectId = None
        self._Name = None
        self._CosUri = None
        self._DataType = None
        self._Description = None

    @property
    def ProjectId(self):
        """表格关联的项目ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        """表格名称。最多支持200个字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CosUri(self):
        """表格文件Cos对象路径。
        :rtype: str
        """
        return self._CosUri

    @CosUri.setter
    def CosUri(self, CosUri):
        self._CosUri = CosUri

    @property
    def DataType(self):
        """表格文件中每列的数据类型，支持的类型包括：Int、Float、String、File、Boolean、Array[Int]、Array[Float]、Array[String]、Array[File]、Array[Boolean]
        :rtype: list of str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def Description(self):
        """表格描述。最多支持500个字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._CosUri = params.get("CosUri")
        self._DataType = params.get("DataType")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportTableFileResponse(AbstractModel):
    """ImportTableFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TableId: 表格ID。
        :type TableId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableId = None
        self._RequestId = None

    @property
    def TableId(self):
        """表格ID。
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TableId = params.get("TableId")
        self._RequestId = params.get("RequestId")


class LimitRange(AbstractModel):
    """资源限制范围。

    """

    def __init__(self):
        r"""
        :param _MaxCPU: 最大CPU设置
        :type MaxCPU: str
        :param _MaxMemory: 最大内存设置（单位：Mi，Gi，Ti，M，G，T）
        :type MaxMemory: str
        """
        self._MaxCPU = None
        self._MaxMemory = None

    @property
    def MaxCPU(self):
        """最大CPU设置
        :rtype: str
        """
        return self._MaxCPU

    @MaxCPU.setter
    def MaxCPU(self, MaxCPU):
        self._MaxCPU = MaxCPU

    @property
    def MaxMemory(self):
        """最大内存设置（单位：Mi，Gi，Ti，M，G，T）
        :rtype: str
        """
        return self._MaxMemory

    @MaxMemory.setter
    def MaxMemory(self, MaxMemory):
        self._MaxMemory = MaxMemory


    def _deserialize(self, params):
        self._MaxCPU = params.get("MaxCPU")
        self._MaxMemory = params.get("MaxMemory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVolumeRequest(AbstractModel):
    """ModifyVolume请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VolumeId: 缓存卷ID。
        :type VolumeId: str
        :param _Name: 名称。
        :type Name: str
        :param _Description: 描述。
        :type Description: str
        """
        self._VolumeId = None
        self._Name = None
        self._Description = None

    @property
    def VolumeId(self):
        """缓存卷ID。
        :rtype: str
        """
        return self._VolumeId

    @VolumeId.setter
    def VolumeId(self, VolumeId):
        self._VolumeId = VolumeId

    @property
    def Name(self):
        """名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._VolumeId = params.get("VolumeId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVolumeResponse(AbstractModel):
    """ModifyVolume返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NFOption(AbstractModel):
    """Nextflow选项。

    """

    def __init__(self):
        r"""
        :param _Config: Config。
        :type Config: str
        :param _Profile: Profile。
        :type Profile: str
        :param _Report: Report。
        :type Report: bool
        :param _Resume: Resume。
        :type Resume: bool
        :param _NFVersion: Nextflow引擎版本，取值范围：
- 22.10.7
- 23.10.1
        :type NFVersion: str
        :param _LaunchDir: 启动路径。可填写指定缓存卷内的绝对路径，nextflow run 命令将在此路径执行。当WorkDir为COS路径时必填；当WorkDir为缓存卷路径时选填，不填默认使用WorkDir作为LaunchDir。
        :type LaunchDir: str
        """
        self._Config = None
        self._Profile = None
        self._Report = None
        self._Resume = None
        self._NFVersion = None
        self._LaunchDir = None

    @property
    def Config(self):
        """Config。
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Profile(self):
        """Profile。
        :rtype: str
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Report(self):
        """Report。
        :rtype: bool
        """
        return self._Report

    @Report.setter
    def Report(self, Report):
        self._Report = Report

    @property
    def Resume(self):
        """Resume。
        :rtype: bool
        """
        return self._Resume

    @Resume.setter
    def Resume(self, Resume):
        self._Resume = Resume

    @property
    def NFVersion(self):
        """Nextflow引擎版本，取值范围：
- 22.10.7
- 23.10.1
        :rtype: str
        """
        return self._NFVersion

    @NFVersion.setter
    def NFVersion(self, NFVersion):
        self._NFVersion = NFVersion

    @property
    def LaunchDir(self):
        """启动路径。可填写指定缓存卷内的绝对路径，nextflow run 命令将在此路径执行。当WorkDir为COS路径时必填；当WorkDir为缓存卷路径时选填，不填默认使用WorkDir作为LaunchDir。
        :rtype: str
        """
        return self._LaunchDir

    @LaunchDir.setter
    def LaunchDir(self, LaunchDir):
        self._LaunchDir = LaunchDir


    def _deserialize(self, params):
        self._Config = params.get("Config")
        self._Profile = params.get("Profile")
        self._Report = params.get("Report")
        self._Resume = params.get("Resume")
        self._NFVersion = params.get("NFVersion")
        self._LaunchDir = params.get("LaunchDir")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceIds(AbstractModel):
    """云资源ID。

    """

    def __init__(self):
        r"""
        :param _VPCId: 私有网络ID。
        :type VPCId: str
        :param _SubnetId: 子网ID。
        :type SubnetId: str
        :param _SecurityGroupId: 安全组ID。
        :type SecurityGroupId: str
        :param _TDSQLCId: TDSQL-C Mysql版数据库ID。
        :type TDSQLCId: str
        :param _CFSId: 文件存储ID。
        :type CFSId: str
        :param _CFSStorageType: 文件存储类型：取值范围：
- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
        :type CFSStorageType: str
        :param _CVMId: 云服务器ID。
        :type CVMId: str
        :param _EKSId: 弹性容器集群ID。
        :type EKSId: str
        """
        self._VPCId = None
        self._SubnetId = None
        self._SecurityGroupId = None
        self._TDSQLCId = None
        self._CFSId = None
        self._CFSStorageType = None
        self._CVMId = None
        self._EKSId = None

    @property
    def VPCId(self):
        """私有网络ID。
        :rtype: str
        """
        return self._VPCId

    @VPCId.setter
    def VPCId(self, VPCId):
        self._VPCId = VPCId

    @property
    def SubnetId(self):
        """子网ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SecurityGroupId(self):
        """安全组ID。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def TDSQLCId(self):
        """TDSQL-C Mysql版数据库ID。
        :rtype: str
        """
        return self._TDSQLCId

    @TDSQLCId.setter
    def TDSQLCId(self, TDSQLCId):
        self._TDSQLCId = TDSQLCId

    @property
    def CFSId(self):
        """文件存储ID。
        :rtype: str
        """
        return self._CFSId

    @CFSId.setter
    def CFSId(self, CFSId):
        self._CFSId = CFSId

    @property
    def CFSStorageType(self):
        """文件存储类型：取值范围：
- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
        :rtype: str
        """
        return self._CFSStorageType

    @CFSStorageType.setter
    def CFSStorageType(self, CFSStorageType):
        self._CFSStorageType = CFSStorageType

    @property
    def CVMId(self):
        """云服务器ID。
        :rtype: str
        """
        return self._CVMId

    @CVMId.setter
    def CVMId(self, CVMId):
        self._CVMId = CVMId

    @property
    def EKSId(self):
        """弹性容器集群ID。
        :rtype: str
        """
        return self._EKSId

    @EKSId.setter
    def EKSId(self, EKSId):
        self._EKSId = EKSId


    def _deserialize(self, params):
        self._VPCId = params.get("VPCId")
        self._SubnetId = params.get("SubnetId")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._TDSQLCId = params.get("TDSQLCId")
        self._CFSId = params.get("CFSId")
        self._CFSStorageType = params.get("CFSStorageType")
        self._CVMId = params.get("CVMId")
        self._EKSId = params.get("EKSId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceQuota(AbstractModel):
    """资源配额。

    """

    def __init__(self):
        r"""
        :param _CPULimit: CPU Limit设置。
        :type CPULimit: str
        :param _MemoryLimit: 内存Limit设置（单位：Mi，Gi，Ti，M，G，T）
        :type MemoryLimit: str
        :param _Pods: Pods数量设置
        :type Pods: str
        """
        self._CPULimit = None
        self._MemoryLimit = None
        self._Pods = None

    @property
    def CPULimit(self):
        """CPU Limit设置。
        :rtype: str
        """
        return self._CPULimit

    @CPULimit.setter
    def CPULimit(self, CPULimit):
        self._CPULimit = CPULimit

    @property
    def MemoryLimit(self):
        """内存Limit设置（单位：Mi，Gi，Ti，M，G，T）
        :rtype: str
        """
        return self._MemoryLimit

    @MemoryLimit.setter
    def MemoryLimit(self, MemoryLimit):
        self._MemoryLimit = MemoryLimit

    @property
    def Pods(self):
        """Pods数量设置
        :rtype: str
        """
        return self._Pods

    @Pods.setter
    def Pods(self, Pods):
        self._Pods = Pods


    def _deserialize(self, params):
        self._CPULimit = params.get("CPULimit")
        self._MemoryLimit = params.get("MemoryLimit")
        self._Pods = params.get("Pods")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryRunsRequest(AbstractModel):
    """RetryRuns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID。（不填使用指定地域下的默认项目）
        :type ProjectId: str
        :param _RunGroupId: 需要重试的任务批次ID。
        :type RunGroupId: str
        :param _RunUuids: 需要重试的任务UUID。
        :type RunUuids: list of str
        :param _WDLOption: WDL运行选项，不填使用被重试的任务批次运行选项。
        :type WDLOption: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param _NFOption: Nextflow运行选项，不填使用被重试的任务批次运行选项。
        :type NFOption: :class:`tencentcloud.omics.v20221128.models.NFOption`
        """
        self._ProjectId = None
        self._RunGroupId = None
        self._RunUuids = None
        self._WDLOption = None
        self._NFOption = None

    @property
    def ProjectId(self):
        """项目ID。（不填使用指定地域下的默认项目）
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RunGroupId(self):
        """需要重试的任务批次ID。
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def RunUuids(self):
        """需要重试的任务UUID。
        :rtype: list of str
        """
        return self._RunUuids

    @RunUuids.setter
    def RunUuids(self, RunUuids):
        self._RunUuids = RunUuids

    @property
    def WDLOption(self):
        """WDL运行选项，不填使用被重试的任务批次运行选项。
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunOption`
        """
        return self._WDLOption

    @WDLOption.setter
    def WDLOption(self, WDLOption):
        self._WDLOption = WDLOption

    @property
    def NFOption(self):
        """Nextflow运行选项，不填使用被重试的任务批次运行选项。
        :rtype: :class:`tencentcloud.omics.v20221128.models.NFOption`
        """
        return self._NFOption

    @NFOption.setter
    def NFOption(self, NFOption):
        self._NFOption = NFOption


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RunGroupId = params.get("RunGroupId")
        self._RunUuids = params.get("RunUuids")
        if params.get("WDLOption") is not None:
            self._WDLOption = RunOption()
            self._WDLOption._deserialize(params.get("WDLOption"))
        if params.get("NFOption") is not None:
            self._NFOption = NFOption()
            self._NFOption._deserialize(params.get("NFOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryRunsResponse(AbstractModel):
    """RetryRuns返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RunGroupId: 新的任务批次ID。
        :type RunGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RunGroupId = None
        self._RequestId = None

    @property
    def RunGroupId(self):
        """新的任务批次ID。
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RunGroupId = params.get("RunGroupId")
        self._RequestId = params.get("RequestId")


class Run(AbstractModel):
    """任务。

    """

    def __init__(self):
        r"""
        :param _RunUuid: 任务UUID。
        :type RunUuid: str
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _ApplicationId: 应用ID。
        :type ApplicationId: str
        :param _RunGroupId: 任务批次ID。
        :type RunGroupId: str
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param _UserDefinedId: 用户定义ID，单例运行为空。
        :type UserDefinedId: str
        :param _TableId: 表格ID，单例运行为空。
        :type TableId: str
        :param _TableRowUuid: 表格行UUID，单例运行为空。
        :type TableRowUuid: str
        :param _Status: 任务状态。
        :type Status: str
        :param _Input: 任务输入。
        :type Input: str
        :param _Option: 运行选项。
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param _ExecutionTime: 执行时间。
        :type ExecutionTime: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        :param _Cache: 缓存信息。
        :type Cache: :class:`tencentcloud.omics.v20221128.models.CacheInfo`
        :param _ErrorMessage: 错误信息。
        :type ErrorMessage: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        """
        self._RunUuid = None
        self._ProjectId = None
        self._ApplicationId = None
        self._RunGroupId = None
        self._EnvironmentId = None
        self._UserDefinedId = None
        self._TableId = None
        self._TableRowUuid = None
        self._Status = None
        self._Input = None
        self._Option = None
        self._ExecutionTime = None
        self._Cache = None
        self._ErrorMessage = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def RunUuid(self):
        """任务UUID。
        :rtype: str
        """
        return self._RunUuid

    @RunUuid.setter
    def RunUuid(self, RunUuid):
        self._RunUuid = RunUuid

    @property
    def ProjectId(self):
        """项目ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ApplicationId(self):
        """应用ID。
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def RunGroupId(self):
        """任务批次ID。
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def EnvironmentId(self):
        """环境ID。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def UserDefinedId(self):
        """用户定义ID，单例运行为空。
        :rtype: str
        """
        return self._UserDefinedId

    @UserDefinedId.setter
    def UserDefinedId(self, UserDefinedId):
        self._UserDefinedId = UserDefinedId

    @property
    def TableId(self):
        """表格ID，单例运行为空。
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def TableRowUuid(self):
        """表格行UUID，单例运行为空。
        :rtype: str
        """
        return self._TableRowUuid

    @TableRowUuid.setter
    def TableRowUuid(self, TableRowUuid):
        self._TableRowUuid = TableRowUuid

    @property
    def Status(self):
        """任务状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Input(self):
        """任务输入。
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Option(self):
        warnings.warn("parameter `Option` is deprecated", DeprecationWarning) 

        """运行选项。
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunOption`
        """
        return self._Option

    @Option.setter
    def Option(self, Option):
        warnings.warn("parameter `Option` is deprecated", DeprecationWarning) 

        self._Option = Option

    @property
    def ExecutionTime(self):
        """执行时间。
        :rtype: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        """
        return self._ExecutionTime

    @ExecutionTime.setter
    def ExecutionTime(self, ExecutionTime):
        self._ExecutionTime = ExecutionTime

    @property
    def Cache(self):
        """缓存信息。
        :rtype: :class:`tencentcloud.omics.v20221128.models.CacheInfo`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def ErrorMessage(self):
        """错误信息。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def CreateTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._RunUuid = params.get("RunUuid")
        self._ProjectId = params.get("ProjectId")
        self._ApplicationId = params.get("ApplicationId")
        self._RunGroupId = params.get("RunGroupId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._UserDefinedId = params.get("UserDefinedId")
        self._TableId = params.get("TableId")
        self._TableRowUuid = params.get("TableRowUuid")
        self._Status = params.get("Status")
        self._Input = params.get("Input")
        if params.get("Option") is not None:
            self._Option = RunOption()
            self._Option._deserialize(params.get("Option"))
        if params.get("ExecutionTime") is not None:
            self._ExecutionTime = ExecutionTime()
            self._ExecutionTime._deserialize(params.get("ExecutionTime"))
        if params.get("Cache") is not None:
            self._Cache = CacheInfo()
            self._Cache._deserialize(params.get("Cache"))
        self._ErrorMessage = params.get("ErrorMessage")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunApplicationRequest(AbstractModel):
    """RunApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID。
        :type ApplicationId: str
        :param _Name: 任务批次名称。
        :type Name: str
        :param _EnvironmentId: 投递环境ID。
        :type EnvironmentId: str
        :param _ProjectId: 项目ID。（不填使用指定地域下的默认项目）
        :type ProjectId: str
        :param _Description: 任务批次描述。
        :type Description: str
        :param _InputCosUri: 任务输入COS地址。（InputBase64和InputCosUri必选其一）
        :type InputCosUri: str
        :param _InputBase64: 任务输入JSON。需要进行base64编码。（InputBase64和InputCosUri必选其一）
        :type InputBase64: str
        :param _TableId: 批量投递表格ID，不填表示单例投递。
        :type TableId: str
        :param _TableRowUuids: 批量投递表格行UUID。不填表示表格全部行。
        :type TableRowUuids: list of str
        :param _CacheClearDelay: 任务缓存清理时间（小时）。不填或0表示不清理。
        :type CacheClearDelay: int
        :param _ApplicationVersionId: 应用版本ID。不填表示使用当前最新版本。
        :type ApplicationVersionId: str
        :param _Option: WDL运行选项。
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param _NFOption: Nextflow运行选项。
        :type NFOption: :class:`tencentcloud.omics.v20221128.models.NFOption`
        :param _WorkDir: 工作目录，当前仅支持Nextflow。可填写指定缓存卷内的绝对路径或者COS路径，不填使用默认缓存卷内的默认路径。如果使用COS路径，NFOption中LaunchDir需填写指定缓存卷内的绝对路径作为启动路径。
        :type WorkDir: str
        :param _AccessMode: 访问模式，不填默认私有。取值范围
- PRIVATE：私有应用
- PUBLIC：公共应用
        :type AccessMode: str
        :param _VolumeIds: 缓存卷ID，不填使用默认缓存卷，暂时仅支持Nextflow。
        :type VolumeIds: list of str
        """
        self._ApplicationId = None
        self._Name = None
        self._EnvironmentId = None
        self._ProjectId = None
        self._Description = None
        self._InputCosUri = None
        self._InputBase64 = None
        self._TableId = None
        self._TableRowUuids = None
        self._CacheClearDelay = None
        self._ApplicationVersionId = None
        self._Option = None
        self._NFOption = None
        self._WorkDir = None
        self._AccessMode = None
        self._VolumeIds = None

    @property
    def ApplicationId(self):
        """应用ID。
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Name(self):
        """任务批次名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnvironmentId(self):
        """投递环境ID。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ProjectId(self):
        """项目ID。（不填使用指定地域下的默认项目）
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Description(self):
        """任务批次描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InputCosUri(self):
        """任务输入COS地址。（InputBase64和InputCosUri必选其一）
        :rtype: str
        """
        return self._InputCosUri

    @InputCosUri.setter
    def InputCosUri(self, InputCosUri):
        self._InputCosUri = InputCosUri

    @property
    def InputBase64(self):
        """任务输入JSON。需要进行base64编码。（InputBase64和InputCosUri必选其一）
        :rtype: str
        """
        return self._InputBase64

    @InputBase64.setter
    def InputBase64(self, InputBase64):
        self._InputBase64 = InputBase64

    @property
    def TableId(self):
        """批量投递表格ID，不填表示单例投递。
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def TableRowUuids(self):
        """批量投递表格行UUID。不填表示表格全部行。
        :rtype: list of str
        """
        return self._TableRowUuids

    @TableRowUuids.setter
    def TableRowUuids(self, TableRowUuids):
        self._TableRowUuids = TableRowUuids

    @property
    def CacheClearDelay(self):
        """任务缓存清理时间（小时）。不填或0表示不清理。
        :rtype: int
        """
        return self._CacheClearDelay

    @CacheClearDelay.setter
    def CacheClearDelay(self, CacheClearDelay):
        self._CacheClearDelay = CacheClearDelay

    @property
    def ApplicationVersionId(self):
        """应用版本ID。不填表示使用当前最新版本。
        :rtype: str
        """
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId

    @property
    def Option(self):
        """WDL运行选项。
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunOption`
        """
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option

    @property
    def NFOption(self):
        """Nextflow运行选项。
        :rtype: :class:`tencentcloud.omics.v20221128.models.NFOption`
        """
        return self._NFOption

    @NFOption.setter
    def NFOption(self, NFOption):
        self._NFOption = NFOption

    @property
    def WorkDir(self):
        """工作目录，当前仅支持Nextflow。可填写指定缓存卷内的绝对路径或者COS路径，不填使用默认缓存卷内的默认路径。如果使用COS路径，NFOption中LaunchDir需填写指定缓存卷内的绝对路径作为启动路径。
        :rtype: str
        """
        return self._WorkDir

    @WorkDir.setter
    def WorkDir(self, WorkDir):
        self._WorkDir = WorkDir

    @property
    def AccessMode(self):
        """访问模式，不填默认私有。取值范围
- PRIVATE：私有应用
- PUBLIC：公共应用
        :rtype: str
        """
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def VolumeIds(self):
        """缓存卷ID，不填使用默认缓存卷，暂时仅支持Nextflow。
        :rtype: list of str
        """
        return self._VolumeIds

    @VolumeIds.setter
    def VolumeIds(self, VolumeIds):
        self._VolumeIds = VolumeIds


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._Name = params.get("Name")
        self._EnvironmentId = params.get("EnvironmentId")
        self._ProjectId = params.get("ProjectId")
        self._Description = params.get("Description")
        self._InputCosUri = params.get("InputCosUri")
        self._InputBase64 = params.get("InputBase64")
        self._TableId = params.get("TableId")
        self._TableRowUuids = params.get("TableRowUuids")
        self._CacheClearDelay = params.get("CacheClearDelay")
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        if params.get("Option") is not None:
            self._Option = RunOption()
            self._Option._deserialize(params.get("Option"))
        if params.get("NFOption") is not None:
            self._NFOption = NFOption()
            self._NFOption._deserialize(params.get("NFOption"))
        self._WorkDir = params.get("WorkDir")
        self._AccessMode = params.get("AccessMode")
        self._VolumeIds = params.get("VolumeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunApplicationResponse(AbstractModel):
    """RunApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RunGroupId: 任务批次ID。
        :type RunGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RunGroupId = None
        self._RequestId = None

    @property
    def RunGroupId(self):
        """任务批次ID。
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RunGroupId = params.get("RunGroupId")
        self._RequestId = params.get("RequestId")


class RunGroup(AbstractModel):
    """任务。

    """

    def __init__(self):
        r"""
        :param _RunGroupId: 任务批次ID。
        :type RunGroupId: str
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _ProjectName: 项目名称。
        :type ProjectName: str
        :param _ApplicationId: 应用ID。
        :type ApplicationId: str
        :param _ApplicationName: 应用名称。
        :type ApplicationName: str
        :param _ApplicationType: 应用类型。
        :type ApplicationType: str
        :param _ApplicationVersion: 应用版本。
        :type ApplicationVersion: :class:`tencentcloud.omics.v20221128.models.ApplicationVersion`
        :param _AccessMode: 应用访问类型：
- PRIVATE 私有应用
- PUBLIC 公共应用
        :type AccessMode: str
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param _EnvironmentName: 环境名称。
        :type EnvironmentName: str
        :param _TableId: 表格ID，单例运行为空。
        :type TableId: str
        :param _Name: 任务名称。
        :type Name: str
        :param _Description: 任务描述。
        :type Description: str
        :param _Status: 任务状态。
        :type Status: str
        :param _Type: 任务批次类型 ：
- WDL
- NEXTFLOW
        :type Type: str
        :param _WorkDir: 工作目录。
        :type WorkDir: str
        :param _Input: 任务输入。
        :type Input: str
        :param _InputType: 任务输入类型：
- JSON: 导入JSON
- MANUAL: 手动输入
- COS: COS文件
        :type InputType: str
        :param _InputCosUri: 输入COS地址。
        :type InputCosUri: str
        :param _InputTemplateId: 输入模版ID。
        :type InputTemplateId: str
        :param _Option: WDL运行选项。
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param _NFOption: Nextflow运行选项。
        :type NFOption: :class:`tencentcloud.omics.v20221128.models.NFOption`
        :param _Volumes: 使用的缓存卷。
        :type Volumes: list of VolumeInfo
        :param _TotalRun: 任务总数量。
        :type TotalRun: int
        :param _RunStatusCounts: 各状态任务的数量。
        :type RunStatusCounts: list of RunStatusCount
        :param _ExecutionTime: 执行时间。
        :type ExecutionTime: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        :param _ErrorMessage: 错误信息。
        :type ErrorMessage: str
        :param _ResultNotify: 运行结果通知方式。
        :type ResultNotify: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        :param _Creator: 创建者。
        :type Creator: str
        :param _CreatorId: 创建者ID。
        :type CreatorId: str
        """
        self._RunGroupId = None
        self._ProjectId = None
        self._ProjectName = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._ApplicationType = None
        self._ApplicationVersion = None
        self._AccessMode = None
        self._EnvironmentId = None
        self._EnvironmentName = None
        self._TableId = None
        self._Name = None
        self._Description = None
        self._Status = None
        self._Type = None
        self._WorkDir = None
        self._Input = None
        self._InputType = None
        self._InputCosUri = None
        self._InputTemplateId = None
        self._Option = None
        self._NFOption = None
        self._Volumes = None
        self._TotalRun = None
        self._RunStatusCounts = None
        self._ExecutionTime = None
        self._ErrorMessage = None
        self._ResultNotify = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Creator = None
        self._CreatorId = None

    @property
    def RunGroupId(self):
        """任务批次ID。
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def ProjectId(self):
        """项目ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """项目名称。
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ApplicationId(self):
        """应用ID。
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        """应用名称。
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ApplicationType(self):
        """应用类型。
        :rtype: str
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ApplicationVersion(self):
        """应用版本。
        :rtype: :class:`tencentcloud.omics.v20221128.models.ApplicationVersion`
        """
        return self._ApplicationVersion

    @ApplicationVersion.setter
    def ApplicationVersion(self, ApplicationVersion):
        self._ApplicationVersion = ApplicationVersion

    @property
    def AccessMode(self):
        """应用访问类型：
- PRIVATE 私有应用
- PUBLIC 公共应用
        :rtype: str
        """
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def EnvironmentId(self):
        """环境ID。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def EnvironmentName(self):
        """环境名称。
        :rtype: str
        """
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def TableId(self):
        """表格ID，单例运行为空。
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def Name(self):
        """任务名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """任务描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        """任务状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        """任务批次类型 ：
- WDL
- NEXTFLOW
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def WorkDir(self):
        """工作目录。
        :rtype: str
        """
        return self._WorkDir

    @WorkDir.setter
    def WorkDir(self, WorkDir):
        self._WorkDir = WorkDir

    @property
    def Input(self):
        """任务输入。
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def InputType(self):
        """任务输入类型：
- JSON: 导入JSON
- MANUAL: 手动输入
- COS: COS文件
        :rtype: str
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def InputCosUri(self):
        """输入COS地址。
        :rtype: str
        """
        return self._InputCosUri

    @InputCosUri.setter
    def InputCosUri(self, InputCosUri):
        self._InputCosUri = InputCosUri

    @property
    def InputTemplateId(self):
        """输入模版ID。
        :rtype: str
        """
        return self._InputTemplateId

    @InputTemplateId.setter
    def InputTemplateId(self, InputTemplateId):
        self._InputTemplateId = InputTemplateId

    @property
    def Option(self):
        """WDL运行选项。
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunOption`
        """
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option

    @property
    def NFOption(self):
        """Nextflow运行选项。
        :rtype: :class:`tencentcloud.omics.v20221128.models.NFOption`
        """
        return self._NFOption

    @NFOption.setter
    def NFOption(self, NFOption):
        self._NFOption = NFOption

    @property
    def Volumes(self):
        """使用的缓存卷。
        :rtype: list of VolumeInfo
        """
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def TotalRun(self):
        """任务总数量。
        :rtype: int
        """
        return self._TotalRun

    @TotalRun.setter
    def TotalRun(self, TotalRun):
        self._TotalRun = TotalRun

    @property
    def RunStatusCounts(self):
        """各状态任务的数量。
        :rtype: list of RunStatusCount
        """
        return self._RunStatusCounts

    @RunStatusCounts.setter
    def RunStatusCounts(self, RunStatusCounts):
        self._RunStatusCounts = RunStatusCounts

    @property
    def ExecutionTime(self):
        """执行时间。
        :rtype: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        """
        return self._ExecutionTime

    @ExecutionTime.setter
    def ExecutionTime(self, ExecutionTime):
        self._ExecutionTime = ExecutionTime

    @property
    def ErrorMessage(self):
        """错误信息。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultNotify(self):
        """运行结果通知方式。
        :rtype: str
        """
        return self._ResultNotify

    @ResultNotify.setter
    def ResultNotify(self, ResultNotify):
        self._ResultNotify = ResultNotify

    @property
    def CreateTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Creator(self):
        """创建者。
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatorId(self):
        """创建者ID。
        :rtype: str
        """
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId


    def _deserialize(self, params):
        self._RunGroupId = params.get("RunGroupId")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._ApplicationType = params.get("ApplicationType")
        if params.get("ApplicationVersion") is not None:
            self._ApplicationVersion = ApplicationVersion()
            self._ApplicationVersion._deserialize(params.get("ApplicationVersion"))
        self._AccessMode = params.get("AccessMode")
        self._EnvironmentId = params.get("EnvironmentId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._TableId = params.get("TableId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._WorkDir = params.get("WorkDir")
        self._Input = params.get("Input")
        self._InputType = params.get("InputType")
        self._InputCosUri = params.get("InputCosUri")
        self._InputTemplateId = params.get("InputTemplateId")
        if params.get("Option") is not None:
            self._Option = RunOption()
            self._Option._deserialize(params.get("Option"))
        if params.get("NFOption") is not None:
            self._NFOption = NFOption()
            self._NFOption._deserialize(params.get("NFOption"))
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = VolumeInfo()
                obj._deserialize(item)
                self._Volumes.append(obj)
        self._TotalRun = params.get("TotalRun")
        if params.get("RunStatusCounts") is not None:
            self._RunStatusCounts = []
            for item in params.get("RunStatusCounts"):
                obj = RunStatusCount()
                obj._deserialize(item)
                self._RunStatusCounts.append(obj)
        if params.get("ExecutionTime") is not None:
            self._ExecutionTime = ExecutionTime()
            self._ExecutionTime._deserialize(params.get("ExecutionTime"))
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultNotify = params.get("ResultNotify")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Creator = params.get("Creator")
        self._CreatorId = params.get("CreatorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMetadata(AbstractModel):
    """任务作业详情。

    """

    def __init__(self):
        r"""
        :param _RunType: 任务类型。
        :type RunType: str
        :param _RunId: 任务ID。
        :type RunId: str
        :param _ParentId: 父层ID。
        :type ParentId: str
        :param _JobId: 作业ID。
        :type JobId: str
        :param _CallName: 作业名称。
        :type CallName: str
        :param _ScatterIndex: Scatter索引。
        :type ScatterIndex: str
        :param _Input: 输入。
        :type Input: str
        :param _Output: 输出。
        :type Output: str
        :param _Status: 状态
        :type Status: str
        :param _ErrorMessage: 错误信息。
        :type ErrorMessage: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _SubmitTime: 提交时间。
        :type SubmitTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _Command: 命令行。
        :type Command: str
        :param _Runtime: 运行时。
        :type Runtime: str
        :param _Preprocess: 预处理。
        :type Preprocess: bool
        :param _PostProcess: 后处理。
        :type PostProcess: bool
        :param _CallCached: Cache命中
        :type CallCached: bool
        :param _WorkDir: 工作目录。
        :type WorkDir: str
        :param _Stdout: 标准输出。
        :type Stdout: str
        :param _Stderr: 错误输出。
        :type Stderr: str
        :param _Meta: 其他信息。
        :type Meta: str
        """
        self._RunType = None
        self._RunId = None
        self._ParentId = None
        self._JobId = None
        self._CallName = None
        self._ScatterIndex = None
        self._Input = None
        self._Output = None
        self._Status = None
        self._ErrorMessage = None
        self._StartTime = None
        self._SubmitTime = None
        self._EndTime = None
        self._Command = None
        self._Runtime = None
        self._Preprocess = None
        self._PostProcess = None
        self._CallCached = None
        self._WorkDir = None
        self._Stdout = None
        self._Stderr = None
        self._Meta = None

    @property
    def RunType(self):
        """任务类型。
        :rtype: str
        """
        return self._RunType

    @RunType.setter
    def RunType(self, RunType):
        self._RunType = RunType

    @property
    def RunId(self):
        """任务ID。
        :rtype: str
        """
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def ParentId(self):
        """父层ID。
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def JobId(self):
        """作业ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CallName(self):
        """作业名称。
        :rtype: str
        """
        return self._CallName

    @CallName.setter
    def CallName(self, CallName):
        self._CallName = CallName

    @property
    def ScatterIndex(self):
        """Scatter索引。
        :rtype: str
        """
        return self._ScatterIndex

    @ScatterIndex.setter
    def ScatterIndex(self, ScatterIndex):
        self._ScatterIndex = ScatterIndex

    @property
    def Input(self):
        """输入。
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        """输出。
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Status(self):
        """状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMessage(self):
        """错误信息。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def SubmitTime(self):
        """提交时间。
        :rtype: str
        """
        return self._SubmitTime

    @SubmitTime.setter
    def SubmitTime(self, SubmitTime):
        self._SubmitTime = SubmitTime

    @property
    def EndTime(self):
        """结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Command(self):
        """命令行。
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Runtime(self):
        """运行时。
        :rtype: str
        """
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def Preprocess(self):
        """预处理。
        :rtype: bool
        """
        return self._Preprocess

    @Preprocess.setter
    def Preprocess(self, Preprocess):
        self._Preprocess = Preprocess

    @property
    def PostProcess(self):
        """后处理。
        :rtype: bool
        """
        return self._PostProcess

    @PostProcess.setter
    def PostProcess(self, PostProcess):
        self._PostProcess = PostProcess

    @property
    def CallCached(self):
        """Cache命中
        :rtype: bool
        """
        return self._CallCached

    @CallCached.setter
    def CallCached(self, CallCached):
        self._CallCached = CallCached

    @property
    def WorkDir(self):
        """工作目录。
        :rtype: str
        """
        return self._WorkDir

    @WorkDir.setter
    def WorkDir(self, WorkDir):
        self._WorkDir = WorkDir

    @property
    def Stdout(self):
        """标准输出。
        :rtype: str
        """
        return self._Stdout

    @Stdout.setter
    def Stdout(self, Stdout):
        self._Stdout = Stdout

    @property
    def Stderr(self):
        """错误输出。
        :rtype: str
        """
        return self._Stderr

    @Stderr.setter
    def Stderr(self, Stderr):
        self._Stderr = Stderr

    @property
    def Meta(self):
        """其他信息。
        :rtype: str
        """
        return self._Meta

    @Meta.setter
    def Meta(self, Meta):
        self._Meta = Meta


    def _deserialize(self, params):
        self._RunType = params.get("RunType")
        self._RunId = params.get("RunId")
        self._ParentId = params.get("ParentId")
        self._JobId = params.get("JobId")
        self._CallName = params.get("CallName")
        self._ScatterIndex = params.get("ScatterIndex")
        self._Input = params.get("Input")
        self._Output = params.get("Output")
        self._Status = params.get("Status")
        self._ErrorMessage = params.get("ErrorMessage")
        self._StartTime = params.get("StartTime")
        self._SubmitTime = params.get("SubmitTime")
        self._EndTime = params.get("EndTime")
        self._Command = params.get("Command")
        self._Runtime = params.get("Runtime")
        self._Preprocess = params.get("Preprocess")
        self._PostProcess = params.get("PostProcess")
        self._CallCached = params.get("CallCached")
        self._WorkDir = params.get("WorkDir")
        self._Stdout = params.get("Stdout")
        self._Stderr = params.get("Stderr")
        self._Meta = params.get("Meta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunOption(AbstractModel):
    """运行应用选项。

    """

    def __init__(self):
        r"""
        :param _FailureMode: 运行失败模式，取值范围：
- ContinueWhilePossible
- NoNewCalls
        :type FailureMode: str
        :param _UseCallCache: 是否使用Call-Caching功能。
        :type UseCallCache: bool
        :param _UseErrorOnHold: 是否使用错误挂起功能。
        :type UseErrorOnHold: bool
        :param _FinalWorkflowOutputsDir: 输出归档COS路径。
        :type FinalWorkflowOutputsDir: str
        :param _UseRelativeOutputPaths: 是否使用相对目录归档输出。
        :type UseRelativeOutputPaths: bool
        :param _AddRunInfoToOutputDir: 是否添加运行信息到输出目录中
        :type AddRunInfoToOutputDir: bool
        """
        self._FailureMode = None
        self._UseCallCache = None
        self._UseErrorOnHold = None
        self._FinalWorkflowOutputsDir = None
        self._UseRelativeOutputPaths = None
        self._AddRunInfoToOutputDir = None

    @property
    def FailureMode(self):
        """运行失败模式，取值范围：
- ContinueWhilePossible
- NoNewCalls
        :rtype: str
        """
        return self._FailureMode

    @FailureMode.setter
    def FailureMode(self, FailureMode):
        self._FailureMode = FailureMode

    @property
    def UseCallCache(self):
        """是否使用Call-Caching功能。
        :rtype: bool
        """
        return self._UseCallCache

    @UseCallCache.setter
    def UseCallCache(self, UseCallCache):
        self._UseCallCache = UseCallCache

    @property
    def UseErrorOnHold(self):
        """是否使用错误挂起功能。
        :rtype: bool
        """
        return self._UseErrorOnHold

    @UseErrorOnHold.setter
    def UseErrorOnHold(self, UseErrorOnHold):
        self._UseErrorOnHold = UseErrorOnHold

    @property
    def FinalWorkflowOutputsDir(self):
        """输出归档COS路径。
        :rtype: str
        """
        return self._FinalWorkflowOutputsDir

    @FinalWorkflowOutputsDir.setter
    def FinalWorkflowOutputsDir(self, FinalWorkflowOutputsDir):
        self._FinalWorkflowOutputsDir = FinalWorkflowOutputsDir

    @property
    def UseRelativeOutputPaths(self):
        """是否使用相对目录归档输出。
        :rtype: bool
        """
        return self._UseRelativeOutputPaths

    @UseRelativeOutputPaths.setter
    def UseRelativeOutputPaths(self, UseRelativeOutputPaths):
        self._UseRelativeOutputPaths = UseRelativeOutputPaths

    @property
    def AddRunInfoToOutputDir(self):
        """是否添加运行信息到输出目录中
        :rtype: bool
        """
        return self._AddRunInfoToOutputDir

    @AddRunInfoToOutputDir.setter
    def AddRunInfoToOutputDir(self, AddRunInfoToOutputDir):
        self._AddRunInfoToOutputDir = AddRunInfoToOutputDir


    def _deserialize(self, params):
        self._FailureMode = params.get("FailureMode")
        self._UseCallCache = params.get("UseCallCache")
        self._UseErrorOnHold = params.get("UseErrorOnHold")
        self._FinalWorkflowOutputsDir = params.get("FinalWorkflowOutputsDir")
        self._UseRelativeOutputPaths = params.get("UseRelativeOutputPaths")
        self._AddRunInfoToOutputDir = params.get("AddRunInfoToOutputDir")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunStatusCount(AbstractModel):
    """任务运行状态。

    """

    def __init__(self):
        r"""
        :param _Status: 状态。
        :type Status: str
        :param _Count: 数量。
        :type Count: int
        """
        self._Status = None
        self._Count = None

    @property
    def Status(self):
        """状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Count(self):
        """数量。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunWorkflowRequest(AbstractModel):
    """RunWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 任务批次名称。
        :type Name: str
        :param _EnvironmentId: 投递环境ID。
        :type EnvironmentId: str
        :param _GitSource: 工作流Git仓库信息。
        :type GitSource: :class:`tencentcloud.omics.v20221128.models.GitInfo`
        :param _Type: 工作流类型。

支持类型：
- NEXTFLOW
        :type Type: str
        :param _NFOption: Nextflow选项。
        :type NFOption: :class:`tencentcloud.omics.v20221128.models.NFOption`
        :param _ProjectId: 项目ID。
（不填使用指定地域下的默认项目）
        :type ProjectId: str
        :param _Description: 任务批次描述。
        :type Description: str
        :param _InputBase64: 任务输入JSON。需要进行base64编码。
（InputBase64和InputCosUri必选其一）
        :type InputBase64: str
        :param _InputCosUri: 任务输入COS地址。
（InputBase64和InputCosUri必选其一）
        :type InputCosUri: str
        :param _CacheClearDelay: 任务缓存清理时间（小时）。不填或0表示不清理。
        :type CacheClearDelay: int
        :param _WorkDir: 工作目录，可填写指定缓存卷内的绝对路径，不填使用默认缓存卷内的默认路径，暂时仅支持Nextflow。
        :type WorkDir: str
        :param _VolumeIds: 缓存卷ID，不填使用默认缓存卷，暂时仅支持Nextflow。
        :type VolumeIds: list of str
        :param _Entrypoint: 工作流入口文件，不填使用默认入口文件。
        :type Entrypoint: str
        """
        self._Name = None
        self._EnvironmentId = None
        self._GitSource = None
        self._Type = None
        self._NFOption = None
        self._ProjectId = None
        self._Description = None
        self._InputBase64 = None
        self._InputCosUri = None
        self._CacheClearDelay = None
        self._WorkDir = None
        self._VolumeIds = None
        self._Entrypoint = None

    @property
    def Name(self):
        """任务批次名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnvironmentId(self):
        """投递环境ID。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def GitSource(self):
        """工作流Git仓库信息。
        :rtype: :class:`tencentcloud.omics.v20221128.models.GitInfo`
        """
        return self._GitSource

    @GitSource.setter
    def GitSource(self, GitSource):
        self._GitSource = GitSource

    @property
    def Type(self):
        """工作流类型。

支持类型：
- NEXTFLOW
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NFOption(self):
        """Nextflow选项。
        :rtype: :class:`tencentcloud.omics.v20221128.models.NFOption`
        """
        return self._NFOption

    @NFOption.setter
    def NFOption(self, NFOption):
        self._NFOption = NFOption

    @property
    def ProjectId(self):
        """项目ID。
（不填使用指定地域下的默认项目）
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Description(self):
        """任务批次描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InputBase64(self):
        """任务输入JSON。需要进行base64编码。
（InputBase64和InputCosUri必选其一）
        :rtype: str
        """
        return self._InputBase64

    @InputBase64.setter
    def InputBase64(self, InputBase64):
        self._InputBase64 = InputBase64

    @property
    def InputCosUri(self):
        """任务输入COS地址。
（InputBase64和InputCosUri必选其一）
        :rtype: str
        """
        return self._InputCosUri

    @InputCosUri.setter
    def InputCosUri(self, InputCosUri):
        self._InputCosUri = InputCosUri

    @property
    def CacheClearDelay(self):
        """任务缓存清理时间（小时）。不填或0表示不清理。
        :rtype: int
        """
        return self._CacheClearDelay

    @CacheClearDelay.setter
    def CacheClearDelay(self, CacheClearDelay):
        self._CacheClearDelay = CacheClearDelay

    @property
    def WorkDir(self):
        """工作目录，可填写指定缓存卷内的绝对路径，不填使用默认缓存卷内的默认路径，暂时仅支持Nextflow。
        :rtype: str
        """
        return self._WorkDir

    @WorkDir.setter
    def WorkDir(self, WorkDir):
        self._WorkDir = WorkDir

    @property
    def VolumeIds(self):
        """缓存卷ID，不填使用默认缓存卷，暂时仅支持Nextflow。
        :rtype: list of str
        """
        return self._VolumeIds

    @VolumeIds.setter
    def VolumeIds(self, VolumeIds):
        self._VolumeIds = VolumeIds

    @property
    def Entrypoint(self):
        """工作流入口文件，不填使用默认入口文件。
        :rtype: str
        """
        return self._Entrypoint

    @Entrypoint.setter
    def Entrypoint(self, Entrypoint):
        self._Entrypoint = Entrypoint


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EnvironmentId = params.get("EnvironmentId")
        if params.get("GitSource") is not None:
            self._GitSource = GitInfo()
            self._GitSource._deserialize(params.get("GitSource"))
        self._Type = params.get("Type")
        if params.get("NFOption") is not None:
            self._NFOption = NFOption()
            self._NFOption._deserialize(params.get("NFOption"))
        self._ProjectId = params.get("ProjectId")
        self._Description = params.get("Description")
        self._InputBase64 = params.get("InputBase64")
        self._InputCosUri = params.get("InputCosUri")
        self._CacheClearDelay = params.get("CacheClearDelay")
        self._WorkDir = params.get("WorkDir")
        self._VolumeIds = params.get("VolumeIds")
        self._Entrypoint = params.get("Entrypoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunWorkflowResponse(AbstractModel):
    """RunWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RunGroupId: 任务批次ID。
        :type RunGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RunGroupId = None
        self._RequestId = None

    @property
    def RunGroupId(self):
        """任务批次ID。
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RunGroupId = params.get("RunGroupId")
        self._RequestId = params.get("RequestId")


class SecurityGroupOption(AbstractModel):
    """安全组配置。

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组ID。
        :type SecurityGroupId: str
        """
        self._SecurityGroupId = None

    @property
    def SecurityGroupId(self):
        """安全组ID。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageOption(AbstractModel):
    """文件存储配置。

    """

    def __init__(self):
        r"""
        :param _StorageType: 文件存储类型，取值范围：
- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
        :type StorageType: str
        :param _Zone: 文件存储可用区。
        :type Zone: str
        :param _Capacity: 文件系统容量，turbo系列必填，单位为GiB。 
- turbo标准型起售40TiB，即40960GiB；扩容步长20TiB，即20480 GiB。
- turbo性能型起售20TiB，即20480 GiB；扩容步长10TiB，即10240 GiB。
        :type Capacity: int
        """
        self._StorageType = None
        self._Zone = None
        self._Capacity = None

    @property
    def StorageType(self):
        """文件存储类型，取值范围：
- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Zone(self):
        """文件存储可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Capacity(self):
        """文件系统容量，turbo系列必填，单位为GiB。 
- turbo标准型起售40TiB，即40960GiB；扩容步长20TiB，即20480 GiB。
- turbo性能型起售20TiB，即20480 GiB；扩容步长10TiB，即10240 GiB。
        :rtype: int
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity


    def _deserialize(self, params):
        self._StorageType = params.get("StorageType")
        self._Zone = params.get("Zone")
        self._Capacity = params.get("Capacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Table(AbstractModel):
    """表格。

    """

    def __init__(self):
        r"""
        :param _TableId: 表格ID
        :type TableId: str
        :param _ProjectId: 关联项目ID
        :type ProjectId: str
        :param _Name: 表格名称
        :type Name: str
        :param _Description: 表格描述
        :type Description: str
        :param _Columns: 表格列
        :type Columns: list of TableColumn
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Creator: 创建人
        :type Creator: str
        :param _CreatorId: 创建人ID
        :type CreatorId: str
        """
        self._TableId = None
        self._ProjectId = None
        self._Name = None
        self._Description = None
        self._Columns = None
        self._CreateTime = None
        self._Creator = None
        self._CreatorId = None

    @property
    def TableId(self):
        """表格ID
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def ProjectId(self):
        """关联项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        """表格名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """表格描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Columns(self):
        """表格列
        :rtype: list of TableColumn
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Creator(self):
        """创建人
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatorId(self):
        """创建人ID
        :rtype: str
        """
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId


    def _deserialize(self, params):
        self._TableId = params.get("TableId")
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = TableColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._Creator = params.get("Creator")
        self._CreatorId = params.get("CreatorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableColumn(AbstractModel):
    """表格列。

    """

    def __init__(self):
        r"""
        :param _Header: 列名称
        :type Header: str
        :param _DataType: 列数据类型
        :type DataType: str
        """
        self._Header = None
        self._DataType = None

    @property
    def Header(self):
        """列名称
        :rtype: str
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def DataType(self):
        """列数据类型
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType


    def _deserialize(self, params):
        self._Header = params.get("Header")
        self._DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableRow(AbstractModel):
    """表格行。

    """

    def __init__(self):
        r"""
        :param _TableRowUuid: 表格行UUID。
        :type TableRowUuid: str
        :param _Content: 表格行内容。
        :type Content: list of str
        """
        self._TableRowUuid = None
        self._Content = None

    @property
    def TableRowUuid(self):
        """表格行UUID。
        :rtype: str
        """
        return self._TableRowUuid

    @TableRowUuid.setter
    def TableRowUuid(self, TableRowUuid):
        self._TableRowUuid = TableRowUuid

    @property
    def Content(self):
        """表格行内容。
        :rtype: list of str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._TableRowUuid = params.get("TableRowUuid")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateRunGroupRequest(AbstractModel):
    """TerminateRunGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RunGroupId: 任务批次ID。
        :type RunGroupId: str
        :param _ProjectId: 项目ID。
（不填使用指定地域下的默认项目）
        :type ProjectId: str
        """
        self._RunGroupId = None
        self._ProjectId = None

    @property
    def RunGroupId(self):
        """任务批次ID。
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def ProjectId(self):
        """项目ID。
（不填使用指定地域下的默认项目）
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._RunGroupId = params.get("RunGroupId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateRunGroupResponse(AbstractModel):
    """TerminateRunGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class VPCOption(AbstractModel):
    """私有网络配置。

    """

    def __init__(self):
        r"""
        :param _VPCId: 私有网络ID（VPCId和VPCCIDRBlock必选其一。若使用VPCId，则使用现用私有网络；若使用VPCCIDRBlock，则创建新的私有网络）
        :type VPCId: str
        :param _SubnetId: 子网ID（SubnetId和SubnetZone&SubnetCIDRBlock必选其一。若使用SubnetId，则使用现用子网；若使用SubnetZone&SubnetCIDRBlock，则创建新的子网）
        :type SubnetId: str
        :param _SubnetZone: 子网可用区。
        :type SubnetZone: str
        :param _VPCCIDRBlock: 私有网络CIDR。
        :type VPCCIDRBlock: str
        :param _SubnetCIDRBlock: 子网CIDR。
        :type SubnetCIDRBlock: str
        """
        self._VPCId = None
        self._SubnetId = None
        self._SubnetZone = None
        self._VPCCIDRBlock = None
        self._SubnetCIDRBlock = None

    @property
    def VPCId(self):
        """私有网络ID（VPCId和VPCCIDRBlock必选其一。若使用VPCId，则使用现用私有网络；若使用VPCCIDRBlock，则创建新的私有网络）
        :rtype: str
        """
        return self._VPCId

    @VPCId.setter
    def VPCId(self, VPCId):
        self._VPCId = VPCId

    @property
    def SubnetId(self):
        """子网ID（SubnetId和SubnetZone&SubnetCIDRBlock必选其一。若使用SubnetId，则使用现用子网；若使用SubnetZone&SubnetCIDRBlock，则创建新的子网）
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetZone(self):
        """子网可用区。
        :rtype: str
        """
        return self._SubnetZone

    @SubnetZone.setter
    def SubnetZone(self, SubnetZone):
        self._SubnetZone = SubnetZone

    @property
    def VPCCIDRBlock(self):
        """私有网络CIDR。
        :rtype: str
        """
        return self._VPCCIDRBlock

    @VPCCIDRBlock.setter
    def VPCCIDRBlock(self, VPCCIDRBlock):
        self._VPCCIDRBlock = VPCCIDRBlock

    @property
    def SubnetCIDRBlock(self):
        """子网CIDR。
        :rtype: str
        """
        return self._SubnetCIDRBlock

    @SubnetCIDRBlock.setter
    def SubnetCIDRBlock(self, SubnetCIDRBlock):
        self._SubnetCIDRBlock = SubnetCIDRBlock


    def _deserialize(self, params):
        self._VPCId = params.get("VPCId")
        self._SubnetId = params.get("SubnetId")
        self._SubnetZone = params.get("SubnetZone")
        self._VPCCIDRBlock = params.get("VPCCIDRBlock")
        self._SubnetCIDRBlock = params.get("SubnetCIDRBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Volume(AbstractModel):
    """缓存卷。

    """

    def __init__(self):
        r"""
        :param _VolumeId: 缓存卷ID。
        :type VolumeId: str
        :param _Name: 名称。
        :type Name: str
        :param _Description: 描述。
        :type Description: str
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param _Type: 缓存卷类型，取值范围：
* SHARED：多点挂载共享存储
        :type Type: str
        :param _Spec: 缓存卷规格，取值范围：

- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
        :type Spec: str
        :param _Capacity: 缓存卷大小（GB）。
        :type Capacity: int
        :param _Usage: 缓存卷使用量（Byte）。
        :type Usage: int
        :param _BandwidthLimit: 缓存卷吞吐上限（MiB/s）。
        :type BandwidthLimit: float
        :param _DefaultMountPath: 默认挂载路径。
        :type DefaultMountPath: str
        :param _IsDefault: 是否为默认缓存卷。
        :type IsDefault: bool
        :param _Status: 状态。
        :type Status: str
        """
        self._VolumeId = None
        self._Name = None
        self._Description = None
        self._EnvironmentId = None
        self._Type = None
        self._Spec = None
        self._Capacity = None
        self._Usage = None
        self._BandwidthLimit = None
        self._DefaultMountPath = None
        self._IsDefault = None
        self._Status = None

    @property
    def VolumeId(self):
        """缓存卷ID。
        :rtype: str
        """
        return self._VolumeId

    @VolumeId.setter
    def VolumeId(self, VolumeId):
        self._VolumeId = VolumeId

    @property
    def Name(self):
        """名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EnvironmentId(self):
        """环境ID。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Type(self):
        """缓存卷类型，取值范围：
* SHARED：多点挂载共享存储
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Spec(self):
        """缓存卷规格，取值范围：

- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def Capacity(self):
        """缓存卷大小（GB）。
        :rtype: int
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def Usage(self):
        """缓存卷使用量（Byte）。
        :rtype: int
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def BandwidthLimit(self):
        """缓存卷吞吐上限（MiB/s）。
        :rtype: float
        """
        return self._BandwidthLimit

    @BandwidthLimit.setter
    def BandwidthLimit(self, BandwidthLimit):
        self._BandwidthLimit = BandwidthLimit

    @property
    def DefaultMountPath(self):
        """默认挂载路径。
        :rtype: str
        """
        return self._DefaultMountPath

    @DefaultMountPath.setter
    def DefaultMountPath(self, DefaultMountPath):
        self._DefaultMountPath = DefaultMountPath

    @property
    def IsDefault(self):
        """是否为默认缓存卷。
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def Status(self):
        """状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._VolumeId = params.get("VolumeId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._EnvironmentId = params.get("EnvironmentId")
        self._Type = params.get("Type")
        self._Spec = params.get("Spec")
        self._Capacity = params.get("Capacity")
        self._Usage = params.get("Usage")
        self._BandwidthLimit = params.get("BandwidthLimit")
        self._DefaultMountPath = params.get("DefaultMountPath")
        self._IsDefault = params.get("IsDefault")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeInfo(AbstractModel):
    """缓存卷信息。

    """

    def __init__(self):
        r"""
        :param _VolumeId: 缓存卷ID。
        :type VolumeId: str
        :param _Name: 名称。
        :type Name: str
        :param _MountPath: 挂载路径。
        :type MountPath: str
        """
        self._VolumeId = None
        self._Name = None
        self._MountPath = None

    @property
    def VolumeId(self):
        """缓存卷ID。
        :rtype: str
        """
        return self._VolumeId

    @VolumeId.setter
    def VolumeId(self, VolumeId):
        self._VolumeId = VolumeId

    @property
    def Name(self):
        """名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MountPath(self):
        """挂载路径。
        :rtype: str
        """
        return self._MountPath

    @MountPath.setter
    def MountPath(self, MountPath):
        self._MountPath = MountPath


    def _deserialize(self, params):
        self._VolumeId = params.get("VolumeId")
        self._Name = params.get("Name")
        self._MountPath = params.get("MountPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        