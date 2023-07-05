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


class ApplicationBasicConfig(AbstractModel):
    """应用基本配置

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _WorkflowKind: 工作负载类型
        :type WorkflowKind: str
        :param _Labels: 标签信息
        :type Labels: list of Label
        :param _GridUniqKey: Grid唯一Key
        :type GridUniqKey: str
        :param _NodeSelector: NodeSelector标签
        :type NodeSelector: list of Label
        :param _Replicas: 实例数
        :type Replicas: int
        :param _AvailableReplicas: 可用实例数
        :type AvailableReplicas: int
        :param _EnableServiceLinks: 是否开启service环境变量注入pod
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableServiceLinks: bool
        """
        self._Name = None
        self._Namespace = None
        self._WorkflowKind = None
        self._Labels = None
        self._GridUniqKey = None
        self._NodeSelector = None
        self._Replicas = None
        self._AvailableReplicas = None
        self._EnableServiceLinks = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def WorkflowKind(self):
        return self._WorkflowKind

    @WorkflowKind.setter
    def WorkflowKind(self, WorkflowKind):
        self._WorkflowKind = WorkflowKind

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def GridUniqKey(self):
        return self._GridUniqKey

    @GridUniqKey.setter
    def GridUniqKey(self, GridUniqKey):
        self._GridUniqKey = GridUniqKey

    @property
    def NodeSelector(self):
        return self._NodeSelector

    @NodeSelector.setter
    def NodeSelector(self, NodeSelector):
        self._NodeSelector = NodeSelector

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def AvailableReplicas(self):
        return self._AvailableReplicas

    @AvailableReplicas.setter
    def AvailableReplicas(self, AvailableReplicas):
        self._AvailableReplicas = AvailableReplicas

    @property
    def EnableServiceLinks(self):
        return self._EnableServiceLinks

    @EnableServiceLinks.setter
    def EnableServiceLinks(self, EnableServiceLinks):
        self._EnableServiceLinks = EnableServiceLinks


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._WorkflowKind = params.get("WorkflowKind")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._GridUniqKey = params.get("GridUniqKey")
        if params.get("NodeSelector") is not None:
            self._NodeSelector = []
            for item in params.get("NodeSelector"):
                obj = Label()
                obj._deserialize(item)
                self._NodeSelector.append(obj)
        self._Replicas = params.get("Replicas")
        self._AvailableReplicas = params.get("AvailableReplicas")
        self._EnableServiceLinks = params.get("EnableServiceLinks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationBasicInfo(AbstractModel):
    """应用基本信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _ManageUrl: 管理URL地址
        :type ManageUrl: str
        :param _Description: 描述信息
        :type Description: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AllowVisualModify: 是否允许可视化修改
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowVisualModify: bool
        """
        self._Name = None
        self._ManageUrl = None
        self._Description = None
        self._CreateTime = None
        self._AllowVisualModify = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ManageUrl(self):
        return self._ManageUrl

    @ManageUrl.setter
    def ManageUrl(self, ManageUrl):
        self._ManageUrl = ManageUrl

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AllowVisualModify(self):
        return self._AllowVisualModify

    @AllowVisualModify.setter
    def AllowVisualModify(self, AllowVisualModify):
        self._AllowVisualModify = AllowVisualModify


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ManageUrl = params.get("ManageUrl")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._AllowVisualModify = params.get("AllowVisualModify")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationDeployMode(AbstractModel):
    """应用部署模式

    """

    def __init__(self):
        r"""
        :param _Type: 1:指定节点部署 2:单元部署
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _ResourceID: 资源ID
        :type ResourceID: int
        :param _ResourceName: 资源名
        :type ResourceName: str
        """
        self._Type = None
        self._ResourceID = None
        self._ResourceName = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ResourceID(self):
        return self._ResourceID

    @ResourceID.setter
    def ResourceID(self, ResourceID):
        self._ResourceID = ResourceID

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ResourceID = params.get("ResourceID")
        self._ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationStatusInfo(AbstractModel):
    """应用状态

    """

    def __init__(self):
        r"""
        :param _Id: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Name: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Version: 应用版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Status: 应用状态(1:待部署 2:部署中 3:运行中 4:待更新 5:更新中 6:待删除 7:删除中 8:已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _ManageUrl: 管理地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ManageUrl: str
        :param _WorkloadKind: 负载类型
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadKind: str
        :param _DeployMode: 应用部署模式
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMode: :class:`tencentcloud.iecp.v20210914.models.ApplicationDeployMode`
        :param _Replicas: 期望Pod数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param _AvailableReplicas: 运行Pod数
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableReplicas: int
        """
        self._Id = None
        self._Name = None
        self._Version = None
        self._Status = None
        self._StartTime = None
        self._ManageUrl = None
        self._WorkloadKind = None
        self._DeployMode = None
        self._Replicas = None
        self._AvailableReplicas = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

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
    def ManageUrl(self):
        return self._ManageUrl

    @ManageUrl.setter
    def ManageUrl(self, ManageUrl):
        self._ManageUrl = ManageUrl

    @property
    def WorkloadKind(self):
        return self._WorkloadKind

    @WorkloadKind.setter
    def WorkloadKind(self, WorkloadKind):
        self._WorkloadKind = WorkloadKind

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def AvailableReplicas(self):
        return self._AvailableReplicas

    @AvailableReplicas.setter
    def AvailableReplicas(self, AvailableReplicas):
        self._AvailableReplicas = AvailableReplicas


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Version = params.get("Version")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._ManageUrl = params.get("ManageUrl")
        self._WorkloadKind = params.get("WorkloadKind")
        if params.get("DeployMode") is not None:
            self._DeployMode = ApplicationDeployMode()
            self._DeployMode._deserialize(params.get("DeployMode"))
        self._Replicas = params.get("Replicas")
        self._AvailableReplicas = params.get("AvailableReplicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationTemplate(AbstractModel):
    """应用模板列表详情

    """

    def __init__(self):
        r"""
        :param _Id: 模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Name: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Source: 来源。1 自定义应用模板 ;  2 官方应用模板
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: int
        :param _WorkloadKind: 应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadKind: str
        :param _ManageUrl: 管理地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ManageUrl: str
        :param _DistributeTime: 发布时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DistributeTime: str
        """
        self._Id = None
        self._Name = None
        self._Source = None
        self._WorkloadKind = None
        self._ManageUrl = None
        self._DistributeTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def WorkloadKind(self):
        return self._WorkloadKind

    @WorkloadKind.setter
    def WorkloadKind(self, WorkloadKind):
        self._WorkloadKind = WorkloadKind

    @property
    def ManageUrl(self):
        return self._ManageUrl

    @ManageUrl.setter
    def ManageUrl(self, ManageUrl):
        self._ManageUrl = ManageUrl

    @property
    def DistributeTime(self):
        return self._DistributeTime

    @DistributeTime.setter
    def DistributeTime(self, DistributeTime):
        self._DistributeTime = DistributeTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Source = params.get("Source")
        self._WorkloadKind = params.get("WorkloadKind")
        self._ManageUrl = params.get("ManageUrl")
        self._DistributeTime = params.get("DistributeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyMarketComponentRequest(AbstractModel):
    """ApplyMarketComponent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 组件ID
        :type ID: int
        """
        self._ID = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyMarketComponentResponse(AbstractModel):
    """ApplyMarketComponent返回参数结构体

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


class BuildMessageRouteRequest(AbstractModel):
    """BuildMessageRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteName: 路由名字
        :type RouteName: str
        :param _SourceProductID: 源产品id
        :type SourceProductID: str
        :param _SourceDeviceNameList: 源设备名列表
        :type SourceDeviceNameList: list of str
        :param _TopicFilter: 第一个字符为 "0"或"1"，"1"表示自定义topic
        :type TopicFilter: str
        :param _Mode: http或mqtt-broker
        :type Mode: str
        :param _SourceUnitIDList: 源单元id列表
        :type SourceUnitIDList: list of str
        :param _Descript: 描述
        :type Descript: str
        :param _TargetOptions: 无
        :type TargetOptions: str
        """
        self._RouteName = None
        self._SourceProductID = None
        self._SourceDeviceNameList = None
        self._TopicFilter = None
        self._Mode = None
        self._SourceUnitIDList = None
        self._Descript = None
        self._TargetOptions = None

    @property
    def RouteName(self):
        return self._RouteName

    @RouteName.setter
    def RouteName(self, RouteName):
        self._RouteName = RouteName

    @property
    def SourceProductID(self):
        return self._SourceProductID

    @SourceProductID.setter
    def SourceProductID(self, SourceProductID):
        self._SourceProductID = SourceProductID

    @property
    def SourceDeviceNameList(self):
        return self._SourceDeviceNameList

    @SourceDeviceNameList.setter
    def SourceDeviceNameList(self, SourceDeviceNameList):
        self._SourceDeviceNameList = SourceDeviceNameList

    @property
    def TopicFilter(self):
        return self._TopicFilter

    @TopicFilter.setter
    def TopicFilter(self, TopicFilter):
        self._TopicFilter = TopicFilter

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def SourceUnitIDList(self):
        return self._SourceUnitIDList

    @SourceUnitIDList.setter
    def SourceUnitIDList(self, SourceUnitIDList):
        self._SourceUnitIDList = SourceUnitIDList

    @property
    def Descript(self):
        return self._Descript

    @Descript.setter
    def Descript(self, Descript):
        self._Descript = Descript

    @property
    def TargetOptions(self):
        return self._TargetOptions

    @TargetOptions.setter
    def TargetOptions(self, TargetOptions):
        self._TargetOptions = TargetOptions


    def _deserialize(self, params):
        self._RouteName = params.get("RouteName")
        self._SourceProductID = params.get("SourceProductID")
        self._SourceDeviceNameList = params.get("SourceDeviceNameList")
        self._TopicFilter = params.get("TopicFilter")
        self._Mode = params.get("Mode")
        self._SourceUnitIDList = params.get("SourceUnitIDList")
        self._Descript = params.get("Descript")
        self._TargetOptions = params.get("TargetOptions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuildMessageRouteResponse(AbstractModel):
    """BuildMessageRoute返回参数结构体

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


class ConfigMapBasicInfo(AbstractModel):
    """ConfigMap基本信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self._Name = None
        self._Namespace = None
        self._CreateTime = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Container(AbstractModel):
    """容器配置信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _ImageName: 镜像名
        :type ImageName: str
        :param _ImageVersion: 镜像版本
        :type ImageVersion: str
        :param _ImagePullPolicy: 镜像拉取策略(Always|Never|IfNotPresent)
        :type ImagePullPolicy: str
        :param _VolumeMounts: 卷挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeMounts: list of VolumeMount
        :param _CpuRequest: cpu最低配置
        :type CpuRequest: str
        :param _CpuLimit: cpu最高限制
        :type CpuLimit: str
        :param _MemoryRequest: 内存最低要求
        :type MemoryRequest: str
        :param _MemoryLimit: 内存最高要求
        :type MemoryLimit: str
        :param _MemoryUnit: 内存单位
        :type MemoryUnit: str
        :param _GpuLimit: gpu最高限制
        :type GpuLimit: str
        :param _ResourceMapCloud: 资源配置
        :type ResourceMapCloud: list of KeyValueObj
        :param _Envs: 环境配置
        :type Envs: list of Env
        :param _WorkingDir: 工作目录
        :type WorkingDir: str
        :param _Commands: 命令
        :type Commands: list of str
        :param _Args: 参数
        :type Args: list of str
        :param _SecurityContext: 安全配置
        :type SecurityContext: :class:`tencentcloud.iecp.v20210914.models.SecurityContext`
        :param _ReadinessProbe: 就绪探针配置
        :type ReadinessProbe: :class:`tencentcloud.iecp.v20210914.models.Probe`
        """
        self._Name = None
        self._ImageName = None
        self._ImageVersion = None
        self._ImagePullPolicy = None
        self._VolumeMounts = None
        self._CpuRequest = None
        self._CpuLimit = None
        self._MemoryRequest = None
        self._MemoryLimit = None
        self._MemoryUnit = None
        self._GpuLimit = None
        self._ResourceMapCloud = None
        self._Envs = None
        self._WorkingDir = None
        self._Commands = None
        self._Args = None
        self._SecurityContext = None
        self._ReadinessProbe = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion

    @property
    def ImagePullPolicy(self):
        return self._ImagePullPolicy

    @ImagePullPolicy.setter
    def ImagePullPolicy(self, ImagePullPolicy):
        self._ImagePullPolicy = ImagePullPolicy

    @property
    def VolumeMounts(self):
        return self._VolumeMounts

    @VolumeMounts.setter
    def VolumeMounts(self, VolumeMounts):
        self._VolumeMounts = VolumeMounts

    @property
    def CpuRequest(self):
        return self._CpuRequest

    @CpuRequest.setter
    def CpuRequest(self, CpuRequest):
        self._CpuRequest = CpuRequest

    @property
    def CpuLimit(self):
        return self._CpuLimit

    @CpuLimit.setter
    def CpuLimit(self, CpuLimit):
        self._CpuLimit = CpuLimit

    @property
    def MemoryRequest(self):
        return self._MemoryRequest

    @MemoryRequest.setter
    def MemoryRequest(self, MemoryRequest):
        self._MemoryRequest = MemoryRequest

    @property
    def MemoryLimit(self):
        return self._MemoryLimit

    @MemoryLimit.setter
    def MemoryLimit(self, MemoryLimit):
        self._MemoryLimit = MemoryLimit

    @property
    def MemoryUnit(self):
        return self._MemoryUnit

    @MemoryUnit.setter
    def MemoryUnit(self, MemoryUnit):
        self._MemoryUnit = MemoryUnit

    @property
    def GpuLimit(self):
        return self._GpuLimit

    @GpuLimit.setter
    def GpuLimit(self, GpuLimit):
        self._GpuLimit = GpuLimit

    @property
    def ResourceMapCloud(self):
        return self._ResourceMapCloud

    @ResourceMapCloud.setter
    def ResourceMapCloud(self, ResourceMapCloud):
        self._ResourceMapCloud = ResourceMapCloud

    @property
    def Envs(self):
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def WorkingDir(self):
        return self._WorkingDir

    @WorkingDir.setter
    def WorkingDir(self, WorkingDir):
        self._WorkingDir = WorkingDir

    @property
    def Commands(self):
        return self._Commands

    @Commands.setter
    def Commands(self, Commands):
        self._Commands = Commands

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def SecurityContext(self):
        return self._SecurityContext

    @SecurityContext.setter
    def SecurityContext(self, SecurityContext):
        self._SecurityContext = SecurityContext

    @property
    def ReadinessProbe(self):
        return self._ReadinessProbe

    @ReadinessProbe.setter
    def ReadinessProbe(self, ReadinessProbe):
        self._ReadinessProbe = ReadinessProbe


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ImageName = params.get("ImageName")
        self._ImageVersion = params.get("ImageVersion")
        self._ImagePullPolicy = params.get("ImagePullPolicy")
        if params.get("VolumeMounts") is not None:
            self._VolumeMounts = []
            for item in params.get("VolumeMounts"):
                obj = VolumeMount()
                obj._deserialize(item)
                self._VolumeMounts.append(obj)
        self._CpuRequest = params.get("CpuRequest")
        self._CpuLimit = params.get("CpuLimit")
        self._MemoryRequest = params.get("MemoryRequest")
        self._MemoryLimit = params.get("MemoryLimit")
        self._MemoryUnit = params.get("MemoryUnit")
        self._GpuLimit = params.get("GpuLimit")
        if params.get("ResourceMapCloud") is not None:
            self._ResourceMapCloud = []
            for item in params.get("ResourceMapCloud"):
                obj = KeyValueObj()
                obj._deserialize(item)
                self._ResourceMapCloud.append(obj)
        if params.get("Envs") is not None:
            self._Envs = []
            for item in params.get("Envs"):
                obj = Env()
                obj._deserialize(item)
                self._Envs.append(obj)
        self._WorkingDir = params.get("WorkingDir")
        self._Commands = params.get("Commands")
        self._Args = params.get("Args")
        if params.get("SecurityContext") is not None:
            self._SecurityContext = SecurityContext()
            self._SecurityContext._deserialize(params.get("SecurityContext"))
        if params.get("ReadinessProbe") is not None:
            self._ReadinessProbe = Probe()
            self._ReadinessProbe._deserialize(params.get("ReadinessProbe"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerStatus(AbstractModel):
    """容器状态

    """

    def __init__(self):
        r"""
        :param _Name: 容器名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ID: 容器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _Image: 镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param _RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param _Status: 状态
        :type Status: str
        """
        self._Name = None
        self._ID = None
        self._Image = None
        self._RestartCount = None
        self._Status = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def RestartCount(self):
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ID = params.get("ID")
        self._Image = params.get("Image")
        self._RestartCount = params.get("RestartCount")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationVisualizationRequest(AbstractModel):
    """CreateApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BasicInfo: 基本信息
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        :param _BasicConfig: 基本配置
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param _Volumes: 卷列表
        :type Volumes: list of Volume
        :param _Service: 服务配置
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param _Job: Job配置
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param _CronJob: CronJob配置
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param _RestartPolicy: 重新运行策略
        :type RestartPolicy: str
        :param _ImagePullSecrets: 镜像拉取密钥
        :type ImagePullSecrets: list of str
        :param _HorizontalPodAutoscaler: HPA配置
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        :param _InitContainers: 初始化容器列表
        :type InitContainers: list of Container
        :param _Containers: 容器列表
        :type Containers: list of Container
        """
        self._BasicInfo = None
        self._BasicConfig = None
        self._Volumes = None
        self._Service = None
        self._Job = None
        self._CronJob = None
        self._RestartPolicy = None
        self._ImagePullSecrets = None
        self._HorizontalPodAutoscaler = None
        self._InitContainers = None
        self._Containers = None

    @property
    def BasicInfo(self):
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def BasicConfig(self):
        return self._BasicConfig

    @BasicConfig.setter
    def BasicConfig(self, BasicConfig):
        self._BasicConfig = BasicConfig

    @property
    def Volumes(self):
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def CronJob(self):
        return self._CronJob

    @CronJob.setter
    def CronJob(self, CronJob):
        self._CronJob = CronJob

    @property
    def RestartPolicy(self):
        return self._RestartPolicy

    @RestartPolicy.setter
    def RestartPolicy(self, RestartPolicy):
        self._RestartPolicy = RestartPolicy

    @property
    def ImagePullSecrets(self):
        return self._ImagePullSecrets

    @ImagePullSecrets.setter
    def ImagePullSecrets(self, ImagePullSecrets):
        self._ImagePullSecrets = ImagePullSecrets

    @property
    def HorizontalPodAutoscaler(self):
        return self._HorizontalPodAutoscaler

    @HorizontalPodAutoscaler.setter
    def HorizontalPodAutoscaler(self, HorizontalPodAutoscaler):
        self._HorizontalPodAutoscaler = HorizontalPodAutoscaler

    @property
    def InitContainers(self):
        return self._InitContainers

    @InitContainers.setter
    def InitContainers(self, InitContainers):
        self._InitContainers = InitContainers

    @property
    def Containers(self):
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self._BasicInfo = ApplicationBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("BasicConfig") is not None:
            self._BasicConfig = ApplicationBasicConfig()
            self._BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self._Volumes.append(obj)
        if params.get("Service") is not None:
            self._Service = Service()
            self._Service._deserialize(params.get("Service"))
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self._CronJob = CronJob()
            self._CronJob._deserialize(params.get("CronJob"))
        self._RestartPolicy = params.get("RestartPolicy")
        self._ImagePullSecrets = params.get("ImagePullSecrets")
        if params.get("HorizontalPodAutoscaler") is not None:
            self._HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self._HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        if params.get("InitContainers") is not None:
            self._InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self._InitContainers.append(obj)
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self._Containers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationVisualizationResponse(AbstractModel):
    """CreateApplicationVisualization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationId = None
        self._RequestId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._RequestId = params.get("RequestId")


class CreateConfigMapRequest(AbstractModel):
    """CreateConfigMap请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _ConfigMapName: ConfigMap名称
        :type ConfigMapName: str
        :param _ConfigMapData: ConfigMap内容
        :type ConfigMapData: list of KeyValueObj
        :param _ConfigMapNamespace: ConfigMap命名空间,默认：default
        :type ConfigMapNamespace: str
        """
        self._EdgeUnitID = None
        self._ConfigMapName = None
        self._ConfigMapData = None
        self._ConfigMapNamespace = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def ConfigMapName(self):
        return self._ConfigMapName

    @ConfigMapName.setter
    def ConfigMapName(self, ConfigMapName):
        self._ConfigMapName = ConfigMapName

    @property
    def ConfigMapData(self):
        return self._ConfigMapData

    @ConfigMapData.setter
    def ConfigMapData(self, ConfigMapData):
        self._ConfigMapData = ConfigMapData

    @property
    def ConfigMapNamespace(self):
        return self._ConfigMapNamespace

    @ConfigMapNamespace.setter
    def ConfigMapNamespace(self, ConfigMapNamespace):
        self._ConfigMapNamespace = ConfigMapNamespace


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._ConfigMapName = params.get("ConfigMapName")
        if params.get("ConfigMapData") is not None:
            self._ConfigMapData = []
            for item in params.get("ConfigMapData"):
                obj = KeyValueObj()
                obj._deserialize(item)
                self._ConfigMapData.append(obj)
        self._ConfigMapNamespace = params.get("ConfigMapNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigMapResponse(AbstractModel):
    """CreateConfigMap返回参数结构体

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


class CreateEdgeNodeBatchRequest(AbstractModel):
    """CreateEdgeNodeBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 边缘单元ID
        :type EdgeUnitId: int
        :param _Nodes: 节点信息
        :type Nodes: list of DracoNodeInfo
        """
        self._EdgeUnitId = None
        self._Nodes = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = DracoNodeInfo()
                obj._deserialize(item)
                self._Nodes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeNodeBatchResponse(AbstractModel):
    """CreateEdgeNodeBatch返回参数结构体

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


class CreateEdgeNodeGroupRequest(AbstractModel):
    """CreateEdgeNodeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _Name: NodeGroup名称
        :type Name: str
        :param _Namespace: 命名空间，不填默认为default
        :type Namespace: str
        :param _Description: 描述
        :type Description: str
        :param _NodeUnitTemplateIDs: 模版ID数组
        :type NodeUnitTemplateIDs: list of int non-negative
        """
        self._EdgeUnitId = None
        self._Name = None
        self._Namespace = None
        self._Description = None
        self._NodeUnitTemplateIDs = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NodeUnitTemplateIDs(self):
        return self._NodeUnitTemplateIDs

    @NodeUnitTemplateIDs.setter
    def NodeUnitTemplateIDs(self, NodeUnitTemplateIDs):
        self._NodeUnitTemplateIDs = NodeUnitTemplateIDs


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Description = params.get("Description")
        self._NodeUnitTemplateIDs = params.get("NodeUnitTemplateIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeNodeGroupResponse(AbstractModel):
    """CreateEdgeNodeGroup返回参数结构体

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


class CreateEdgeNodeRequest(AbstractModel):
    """CreateEdgeNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 边缘单元ID
        :type EdgeUnitId: int
        :param _Name: 节点名称
        :type Name: str
        """
        self._EdgeUnitId = None
        self._Name = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeNodeResponse(AbstractModel):
    """CreateEdgeNode返回参数结构体

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


class CreateEdgeNodeUnitTemplateRequest(AbstractModel):
    """CreateEdgeNodeUnitTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _Name: NodeUnit模板名称
        :type Name: str
        :param _Namespace: 命名空间，默认default
        :type Namespace: str
        :param _Nodes: 包含的节点列表
        :type Nodes: list of str
        :param _Description: 描述
        :type Description: str
        """
        self._EdgeUnitId = None
        self._Name = None
        self._Namespace = None
        self._Nodes = None
        self._Description = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Nodes = params.get("Nodes")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeNodeUnitTemplateResponse(AbstractModel):
    """CreateEdgeNodeUnitTemplate返回参数结构体

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


class CreateEdgeUnitApplicationVisualizationRequest(AbstractModel):
    """CreateEdgeUnitApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BasicInfo: 基本信息
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        :param _BasicConfig: 基本配置
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _Volumes: 卷列表
        :type Volumes: list of Volume
        :param _Service: 服务配置
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param _TemplateID: 模版ID
        :type TemplateID: int
        :param _Job: Job配置
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param _CronJob: CronJob配置
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param _RestartPolicy: 重新运行策略
        :type RestartPolicy: str
        :param _ImagePullSecrets: 镜像拉取密钥
        :type ImagePullSecrets: list of str
        :param _HorizontalPodAutoscaler: HPA配置
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        :param _InitContainers: 初始化容器列表
        :type InitContainers: list of Container
        :param _Containers: 容器列表
        :type Containers: list of Container
        """
        self._BasicInfo = None
        self._BasicConfig = None
        self._EdgeUnitId = None
        self._Volumes = None
        self._Service = None
        self._TemplateID = None
        self._Job = None
        self._CronJob = None
        self._RestartPolicy = None
        self._ImagePullSecrets = None
        self._HorizontalPodAutoscaler = None
        self._InitContainers = None
        self._Containers = None

    @property
    def BasicInfo(self):
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def BasicConfig(self):
        return self._BasicConfig

    @BasicConfig.setter
    def BasicConfig(self, BasicConfig):
        self._BasicConfig = BasicConfig

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Volumes(self):
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def TemplateID(self):
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def CronJob(self):
        return self._CronJob

    @CronJob.setter
    def CronJob(self, CronJob):
        self._CronJob = CronJob

    @property
    def RestartPolicy(self):
        return self._RestartPolicy

    @RestartPolicy.setter
    def RestartPolicy(self, RestartPolicy):
        self._RestartPolicy = RestartPolicy

    @property
    def ImagePullSecrets(self):
        return self._ImagePullSecrets

    @ImagePullSecrets.setter
    def ImagePullSecrets(self, ImagePullSecrets):
        self._ImagePullSecrets = ImagePullSecrets

    @property
    def HorizontalPodAutoscaler(self):
        return self._HorizontalPodAutoscaler

    @HorizontalPodAutoscaler.setter
    def HorizontalPodAutoscaler(self, HorizontalPodAutoscaler):
        self._HorizontalPodAutoscaler = HorizontalPodAutoscaler

    @property
    def InitContainers(self):
        return self._InitContainers

    @InitContainers.setter
    def InitContainers(self, InitContainers):
        self._InitContainers = InitContainers

    @property
    def Containers(self):
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self._BasicInfo = ApplicationBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("BasicConfig") is not None:
            self._BasicConfig = ApplicationBasicConfig()
            self._BasicConfig._deserialize(params.get("BasicConfig"))
        self._EdgeUnitId = params.get("EdgeUnitId")
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self._Volumes.append(obj)
        if params.get("Service") is not None:
            self._Service = Service()
            self._Service._deserialize(params.get("Service"))
        self._TemplateID = params.get("TemplateID")
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self._CronJob = CronJob()
            self._CronJob._deserialize(params.get("CronJob"))
        self._RestartPolicy = params.get("RestartPolicy")
        self._ImagePullSecrets = params.get("ImagePullSecrets")
        if params.get("HorizontalPodAutoscaler") is not None:
            self._HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self._HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        if params.get("InitContainers") is not None:
            self._InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self._InitContainers.append(obj)
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self._Containers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeUnitApplicationVisualizationResponse(AbstractModel):
    """CreateEdgeUnitApplicationVisualization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationId = None
        self._RequestId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._RequestId = params.get("RequestId")


class CreateEdgeUnitApplicationYamlRequest(AbstractModel):
    """CreateEdgeUnitApplicationYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _Yaml: base64后的Yaml配置
        :type Yaml: str
        :param _BasicInfo: 基本信息
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        """
        self._EdgeUnitId = None
        self._Yaml = None
        self._BasicInfo = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def BasicInfo(self):
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Yaml = params.get("Yaml")
        if params.get("BasicInfo") is not None:
            self._BasicInfo = ApplicationBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeUnitApplicationYamlResponse(AbstractModel):
    """CreateEdgeUnitApplicationYaml返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationId = None
        self._RequestId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._RequestId = params.get("RequestId")


class CreateEdgeUnitCloudRequest(AbstractModel):
    """CreateEdgeUnitCloud请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 集群名称，长度小于32
        :type Name: str
        :param _K8sVersion: k8s版本，仅支持1.16.7 和 1.18.2
        :type K8sVersion: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _Description: 集群描述
        :type Description: str
        :param _PodCIDR: 集群pod cidr， 默认  10.1.0.0/16
        :type PodCIDR: str
        :param _ServiceCIDR: 集群service cidr, 默认 10.2.0.0/16
        :type ServiceCIDR: str
        :param _OpenCloudMonitor: 是否开启监控。目前内存中权限开启联系产品开通白名单
        :type OpenCloudMonitor: bool
        """
        self._Name = None
        self._K8sVersion = None
        self._VpcId = None
        self._Description = None
        self._PodCIDR = None
        self._ServiceCIDR = None
        self._OpenCloudMonitor = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def K8sVersion(self):
        return self._K8sVersion

    @K8sVersion.setter
    def K8sVersion(self, K8sVersion):
        self._K8sVersion = K8sVersion

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PodCIDR(self):
        return self._PodCIDR

    @PodCIDR.setter
    def PodCIDR(self, PodCIDR):
        self._PodCIDR = PodCIDR

    @property
    def ServiceCIDR(self):
        return self._ServiceCIDR

    @ServiceCIDR.setter
    def ServiceCIDR(self, ServiceCIDR):
        self._ServiceCIDR = ServiceCIDR

    @property
    def OpenCloudMonitor(self):
        return self._OpenCloudMonitor

    @OpenCloudMonitor.setter
    def OpenCloudMonitor(self, OpenCloudMonitor):
        self._OpenCloudMonitor = OpenCloudMonitor


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._K8sVersion = params.get("K8sVersion")
        self._VpcId = params.get("VpcId")
        self._Description = params.get("Description")
        self._PodCIDR = params.get("PodCIDR")
        self._ServiceCIDR = params.get("ServiceCIDR")
        self._OpenCloudMonitor = params.get("OpenCloudMonitor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeUnitCloudResponse(AbstractModel):
    """CreateEdgeUnitCloud返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: tke集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _EdgeUnitId: IECP集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EdgeUnitId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._EdgeUnitId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._RequestId = params.get("RequestId")


class CreateEdgeUnitDevicesRequest(AbstractModel):
    """CreateEdgeUnitDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 无
        :type EdgeUnitId: int
        :param _ProductId: 无
        :type ProductId: str
        :param _DeviceNames: 无
        :type DeviceNames: list of str
        """
        self._EdgeUnitId = None
        self._ProductId = None
        self._DeviceNames = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeUnitDevicesResponse(AbstractModel):
    """CreateEdgeUnitDevices返回参数结构体

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


class CreateIotDeviceRequest(AbstractModel):
    """CreateIotDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ProductId: 设备所属的产品id
        :type ProductId: str
        :param _Description: 描述
        :type Description: str
        :param _UnitID: 无
        :type UnitID: int
        """
        self._DeviceName = None
        self._ProductId = None
        self._Description = None
        self._UnitID = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UnitID(self):
        return self._UnitID

    @UnitID.setter
    def UnitID(self, UnitID):
        self._UnitID = UnitID


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._ProductId = params.get("ProductId")
        self._Description = params.get("Description")
        self._UnitID = params.get("UnitID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIotDeviceResponse(AbstractModel):
    """CreateIotDevice返回参数结构体

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


class CreateMessageRouteRequest(AbstractModel):
    """CreateMessageRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteName: 路由名称
        :type RouteName: str
        :param _Descript: 路由备注
        :type Descript: str
        """
        self._RouteName = None
        self._Descript = None

    @property
    def RouteName(self):
        return self._RouteName

    @RouteName.setter
    def RouteName(self, RouteName):
        self._RouteName = RouteName

    @property
    def Descript(self):
        return self._Descript

    @Descript.setter
    def Descript(self, Descript):
        self._Descript = Descript


    def _deserialize(self, params):
        self._RouteName = params.get("RouteName")
        self._Descript = params.get("Descript")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMessageRouteResponse(AbstractModel):
    """CreateMessageRoute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteID: 路由id
        :type RouteID: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RouteID = None
        self._RequestId = None

    @property
    def RouteID(self):
        return self._RouteID

    @RouteID.setter
    def RouteID(self, RouteID):
        self._RouteID = RouteID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RouteID = params.get("RouteID")
        self._RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Description: 描述信息
        :type Description: str
        """
        self._EdgeUnitID = None
        self._Namespace = None
        self._Description = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._Namespace = params.get("Namespace")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

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


class CreateSecretRequest(AbstractModel):
    """CreateSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _SecretName: secret名
        :type SecretName: str
        :param _SecretNamespace: 命名空间（默认:default）
        :type SecretNamespace: str
        :param _SecretType: secret类型(取值范围:DockerConfigJson,Opaque 默认Opaque)
        :type SecretType: str
        :param _DockerConfigJson: DockerConfig的序列化base64编码后的字符串
        :type DockerConfigJson: str
        :param _CloudData: Opaque类型的Secret内容
        :type CloudData: list of KeyValueObj
        :param _DockerConfig: DockerConfig配置
        :type DockerConfig: :class:`tencentcloud.iecp.v20210914.models.DockerConfig`
        """
        self._EdgeUnitID = None
        self._SecretName = None
        self._SecretNamespace = None
        self._SecretType = None
        self._DockerConfigJson = None
        self._CloudData = None
        self._DockerConfig = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def SecretNamespace(self):
        return self._SecretNamespace

    @SecretNamespace.setter
    def SecretNamespace(self, SecretNamespace):
        self._SecretNamespace = SecretNamespace

    @property
    def SecretType(self):
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType

    @property
    def DockerConfigJson(self):
        return self._DockerConfigJson

    @DockerConfigJson.setter
    def DockerConfigJson(self, DockerConfigJson):
        self._DockerConfigJson = DockerConfigJson

    @property
    def CloudData(self):
        return self._CloudData

    @CloudData.setter
    def CloudData(self, CloudData):
        self._CloudData = CloudData

    @property
    def DockerConfig(self):
        return self._DockerConfig

    @DockerConfig.setter
    def DockerConfig(self, DockerConfig):
        self._DockerConfig = DockerConfig


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._SecretName = params.get("SecretName")
        self._SecretNamespace = params.get("SecretNamespace")
        self._SecretType = params.get("SecretType")
        self._DockerConfigJson = params.get("DockerConfigJson")
        if params.get("CloudData") is not None:
            self._CloudData = []
            for item in params.get("CloudData"):
                obj = KeyValueObj()
                obj._deserialize(item)
                self._CloudData.append(obj)
        if params.get("DockerConfig") is not None:
            self._DockerConfig = DockerConfig()
            self._DockerConfig._deserialize(params.get("DockerConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecretResponse(AbstractModel):
    """CreateSecret返回参数结构体

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


class CreateUpdateNodeUnitRequest(AbstractModel):
    """CreateUpdateNodeUnit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NodeGroupName: NodeUnit所属的NodeGroup名称
        :type NodeGroupName: str
        :param _Namespace: 命名空间，默认为default
        :type Namespace: str
        :param _NodeUnitName: NodeUnit名称，通过模版创建可不填
        :type NodeUnitName: str
        :param _Nodes: NodeUnit包含的节点列表，通过模版创建可不填
        :type Nodes: list of str
        :param _NodeUnitTemplateIDs: NodeUnit模版ID列表
        :type NodeUnitTemplateIDs: list of int non-negative
        """
        self._EdgeUnitId = None
        self._NodeGroupName = None
        self._Namespace = None
        self._NodeUnitName = None
        self._Nodes = None
        self._NodeUnitTemplateIDs = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeGroupName(self):
        return self._NodeGroupName

    @NodeGroupName.setter
    def NodeGroupName(self, NodeGroupName):
        self._NodeGroupName = NodeGroupName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def NodeUnitName(self):
        return self._NodeUnitName

    @NodeUnitName.setter
    def NodeUnitName(self, NodeUnitName):
        self._NodeUnitName = NodeUnitName

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def NodeUnitTemplateIDs(self):
        return self._NodeUnitTemplateIDs

    @NodeUnitTemplateIDs.setter
    def NodeUnitTemplateIDs(self, NodeUnitTemplateIDs):
        self._NodeUnitTemplateIDs = NodeUnitTemplateIDs


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeGroupName = params.get("NodeGroupName")
        self._Namespace = params.get("Namespace")
        self._NodeUnitName = params.get("NodeUnitName")
        self._Nodes = params.get("Nodes")
        self._NodeUnitTemplateIDs = params.get("NodeUnitTemplateIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUpdateNodeUnitResponse(AbstractModel):
    """CreateUpdateNodeUnit返回参数结构体

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


class CreateUserTokenRequest(AbstractModel):
    """CreateUserToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Second: token过期时间，有效值是1~300秒
        :type Second: int
        """
        self._Second = None

    @property
    def Second(self):
        return self._Second

    @Second.setter
    def Second(self, Second):
        self._Second = Second


    def _deserialize(self, params):
        self._Second = params.get("Second")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserTokenResponse(AbstractModel):
    """CreateUserToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Token: 无
        :type Token: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._RequestId = None

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class CronJob(AbstractModel):
    """CronJob配置

    """

    def __init__(self):
        r"""
        :param _Schedule: 调度配置
        :type Schedule: str
        :param _StartingDeadlineSeconds: 运行时间
        :type StartingDeadlineSeconds: int
        :param _ConcurrencyPolicy: job并行策略(Allow|Forbid|Replace)
        :type ConcurrencyPolicy: str
        :param _Job: Job配置
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        """
        self._Schedule = None
        self._StartingDeadlineSeconds = None
        self._ConcurrencyPolicy = None
        self._Job = None

    @property
    def Schedule(self):
        return self._Schedule

    @Schedule.setter
    def Schedule(self, Schedule):
        self._Schedule = Schedule

    @property
    def StartingDeadlineSeconds(self):
        return self._StartingDeadlineSeconds

    @StartingDeadlineSeconds.setter
    def StartingDeadlineSeconds(self, StartingDeadlineSeconds):
        self._StartingDeadlineSeconds = StartingDeadlineSeconds

    @property
    def ConcurrencyPolicy(self):
        return self._ConcurrencyPolicy

    @ConcurrencyPolicy.setter
    def ConcurrencyPolicy(self, ConcurrencyPolicy):
        self._ConcurrencyPolicy = ConcurrencyPolicy

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job


    def _deserialize(self, params):
        self._Schedule = params.get("Schedule")
        self._StartingDeadlineSeconds = params.get("StartingDeadlineSeconds")
        self._ConcurrencyPolicy = params.get("ConcurrencyPolicy")
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationsRequest(AbstractModel):
    """DeleteApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationIds: 应用模板ID列表
        :type ApplicationIds: list of int non-negative
        """
        self._ApplicationIds = None

    @property
    def ApplicationIds(self):
        return self._ApplicationIds

    @ApplicationIds.setter
    def ApplicationIds(self, ApplicationIds):
        self._ApplicationIds = ApplicationIds


    def _deserialize(self, params):
        self._ApplicationIds = params.get("ApplicationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationsResponse(AbstractModel):
    """DeleteApplications返回参数结构体

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


class DeleteConfigMapRequest(AbstractModel):
    """DeleteConfigMap请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _ConfigMapName: ConfigMap名
        :type ConfigMapName: str
        :param _ConfigMapNamespace: ConfigMap命名空间，默认：default
        :type ConfigMapNamespace: str
        """
        self._EdgeUnitID = None
        self._ConfigMapName = None
        self._ConfigMapNamespace = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def ConfigMapName(self):
        return self._ConfigMapName

    @ConfigMapName.setter
    def ConfigMapName(self, ConfigMapName):
        self._ConfigMapName = ConfigMapName

    @property
    def ConfigMapNamespace(self):
        return self._ConfigMapNamespace

    @ConfigMapNamespace.setter
    def ConfigMapNamespace(self, ConfigMapNamespace):
        self._ConfigMapNamespace = ConfigMapNamespace


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._ConfigMapName = params.get("ConfigMapName")
        self._ConfigMapNamespace = params.get("ConfigMapNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigMapResponse(AbstractModel):
    """DeleteConfigMap返回参数结构体

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


class DeleteEdgeNodeGroupRequest(AbstractModel):
    """DeleteEdgeNodeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _Name: NodeGroup名称
        :type Name: str
        :param _Namespace: 命名空间，默认为default
        :type Namespace: str
        """
        self._EdgeUnitId = None
        self._Name = None
        self._Namespace = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeNodeGroupResponse(AbstractModel):
    """DeleteEdgeNodeGroup返回参数结构体

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


class DeleteEdgeNodeUnitTemplatesRequest(AbstractModel):
    """DeleteEdgeNodeUnitTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NodeUnitTemplateIDs: 删除的NodeUnit模板ID列表
        :type NodeUnitTemplateIDs: list of int non-negative
        """
        self._EdgeUnitId = None
        self._NodeUnitTemplateIDs = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeUnitTemplateIDs(self):
        return self._NodeUnitTemplateIDs

    @NodeUnitTemplateIDs.setter
    def NodeUnitTemplateIDs(self, NodeUnitTemplateIDs):
        self._NodeUnitTemplateIDs = NodeUnitTemplateIDs


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeUnitTemplateIDs = params.get("NodeUnitTemplateIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeNodeUnitTemplatesResponse(AbstractModel):
    """DeleteEdgeNodeUnitTemplates返回参数结构体

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


class DeleteEdgeNodesRequest(AbstractModel):
    """DeleteEdgeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NodeIds: IECP边缘节点ID列表
        :type NodeIds: list of int non-negative
        """
        self._EdgeUnitId = None
        self._NodeIds = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeIds(self):
        return self._NodeIds

    @NodeIds.setter
    def NodeIds(self, NodeIds):
        self._NodeIds = NodeIds


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeIds = params.get("NodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeNodesResponse(AbstractModel):
    """DeleteEdgeNodes返回参数结构体

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


class DeleteEdgeUnitApplicationsRequest(AbstractModel):
    """DeleteEdgeUnitApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _ApplicationIDs: 应用ID列表
        :type ApplicationIDs: list of int non-negative
        """
        self._EdgeUnitID = None
        self._ApplicationIDs = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def ApplicationIDs(self):
        return self._ApplicationIDs

    @ApplicationIDs.setter
    def ApplicationIDs(self, ApplicationIDs):
        self._ApplicationIDs = ApplicationIDs


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._ApplicationIDs = params.get("ApplicationIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeUnitApplicationsResponse(AbstractModel):
    """DeleteEdgeUnitApplications返回参数结构体

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


class DeleteEdgeUnitCloudRequest(AbstractModel):
    """DeleteEdgeUnitCloud请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 边缘集群ID
        :type EdgeUnitId: int
        """
        self._EdgeUnitId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeUnitCloudResponse(AbstractModel):
    """DeleteEdgeUnitCloud返回参数结构体

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


class DeleteEdgeUnitDeployGridItemRequest(AbstractModel):
    """DeleteEdgeUnitDeployGridItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param _GridItemName: Grid部署名称
        :type GridItemName: str
        :param _Namespace: 命名空间，默认default
        :type Namespace: str
        """
        self._EdgeUnitId = None
        self._WorkloadKind = None
        self._GridItemName = None
        self._Namespace = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def WorkloadKind(self):
        return self._WorkloadKind

    @WorkloadKind.setter
    def WorkloadKind(self, WorkloadKind):
        self._WorkloadKind = WorkloadKind

    @property
    def GridItemName(self):
        return self._GridItemName

    @GridItemName.setter
    def GridItemName(self, GridItemName):
        self._GridItemName = GridItemName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._WorkloadKind = params.get("WorkloadKind")
        self._GridItemName = params.get("GridItemName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeUnitDeployGridItemResponse(AbstractModel):
    """DeleteEdgeUnitDeployGridItem返回参数结构体

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


class DeleteEdgeUnitDevicesDevice(AbstractModel):
    """从单元批量解绑设备

    """

    def __init__(self):
        r"""
        :param _ProductId: 无
        :type ProductId: str
        :param _DeviceName: 无
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeUnitDevicesRequest(AbstractModel):
    """DeleteEdgeUnitDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 无
        :type EdgeUnitId: int
        :param _Devices: 无
        :type Devices: list of DeleteEdgeUnitDevicesDevice
        """
        self._EdgeUnitId = None
        self._Devices = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeleteEdgeUnitDevicesDevice()
                obj._deserialize(item)
                self._Devices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeUnitDevicesResponse(AbstractModel):
    """DeleteEdgeUnitDevices返回参数结构体

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


class DeleteEdgeUnitPodRequest(AbstractModel):
    """DeleteEdgeUnitPod请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterID: 集群ID
        :type ClusterID: str
        :param _PodName: Pod名称
        :type PodName: str
        :param _Namespace: 命名空间
        :type Namespace: str
        """
        self._ClusterID = None
        self._PodName = None
        self._Namespace = None

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
        self._PodName = params.get("PodName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeUnitPodResponse(AbstractModel):
    """DeleteEdgeUnitPod返回参数结构体

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


class DeleteIotDeviceBatchRequest(AbstractModel):
    """DeleteIotDeviceBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceIDList: 无
        :type DeviceIDList: list of int non-negative
        """
        self._DeviceIDList = None

    @property
    def DeviceIDList(self):
        return self._DeviceIDList

    @DeviceIDList.setter
    def DeviceIDList(self, DeviceIDList):
        self._DeviceIDList = DeviceIDList


    def _deserialize(self, params):
        self._DeviceIDList = params.get("DeviceIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIotDeviceBatchResponse(AbstractModel):
    """DeleteIotDeviceBatch返回参数结构体

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


class DeleteIotDeviceRequest(AbstractModel):
    """DeleteIotDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备id
        :type DeviceId: int
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIotDeviceResponse(AbstractModel):
    """DeleteIotDevice返回参数结构体

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


class DeleteMessageRouteRequest(AbstractModel):
    """DeleteMessageRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteID: 无
        :type RouteID: int
        """
        self._RouteID = None

    @property
    def RouteID(self):
        return self._RouteID

    @RouteID.setter
    def RouteID(self, RouteID):
        self._RouteID = RouteID


    def _deserialize(self, params):
        self._RouteID = params.get("RouteID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMessageRouteResponse(AbstractModel):
    """DeleteMessageRoute返回参数结构体

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


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _Namespace: 命名空间
        :type Namespace: str
        """
        self._EdgeUnitID = None
        self._Namespace = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回参数结构体

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


class DeleteNodeUnitRequest(AbstractModel):
    """DeleteNodeUnit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NodeGroupName: NodeUnit所属的NodeGroup名称
        :type NodeGroupName: str
        :param _NodeUnitName: NodeUnit名称
        :type NodeUnitName: str
        :param _Namespace: 命名空间，默认为default
        :type Namespace: str
        :param _Nodes: NodeUnit包含的节点列表
        :type Nodes: list of str
        """
        self._EdgeUnitId = None
        self._NodeGroupName = None
        self._NodeUnitName = None
        self._Namespace = None
        self._Nodes = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeGroupName(self):
        return self._NodeGroupName

    @NodeGroupName.setter
    def NodeGroupName(self, NodeGroupName):
        self._NodeGroupName = NodeGroupName

    @property
    def NodeUnitName(self):
        return self._NodeUnitName

    @NodeUnitName.setter
    def NodeUnitName(self, NodeUnitName):
        self._NodeUnitName = NodeUnitName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeGroupName = params.get("NodeGroupName")
        self._NodeUnitName = params.get("NodeUnitName")
        self._Namespace = params.get("Namespace")
        self._Nodes = params.get("Nodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNodeUnitResponse(AbstractModel):
    """DeleteNodeUnit返回参数结构体

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


class DeleteSecretRequest(AbstractModel):
    """DeleteSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _SecretName: secret名称
        :type SecretName: str
        :param _SecretNamespace: secret命名空间（默认:default）
        :type SecretNamespace: str
        """
        self._EdgeUnitID = None
        self._SecretName = None
        self._SecretNamespace = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def SecretNamespace(self):
        return self._SecretNamespace

    @SecretNamespace.setter
    def SecretNamespace(self, SecretNamespace):
        self._SecretNamespace = SecretNamespace


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._SecretName = params.get("SecretName")
        self._SecretNamespace = params.get("SecretNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecretResponse(AbstractModel):
    """DeleteSecret返回参数结构体

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


class DescribeApplicationVisualizationRequest(AbstractModel):
    """DescribeApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用模板ID
        :type ApplicationId: int
        """
        self._ApplicationId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationVisualizationResponse(AbstractModel):
    """DescribeApplicationVisualization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BasicInfo: 基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        :param _BasicConfig: 基本配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param _Volumes: 卷配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Volumes: list of Volume
        :param _InitContainers: 初始化容器配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InitContainers: list of Container
        :param _Containers: 容器配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Containers: list of Container
        :param _Service: 服务配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param _Job: Job配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param _CronJob: CronJob配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param _RestartPolicy: 重启策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartPolicy: str
        :param _HorizontalPodAutoscaler: HPA
注意：此字段可能返回 null，表示取不到有效值。
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        :param _ImagePullSecrets: 镜像拉取Secret
注意：此字段可能返回 null，表示取不到有效值。
        :type ImagePullSecrets: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BasicInfo = None
        self._BasicConfig = None
        self._Volumes = None
        self._InitContainers = None
        self._Containers = None
        self._Service = None
        self._Job = None
        self._CronJob = None
        self._RestartPolicy = None
        self._HorizontalPodAutoscaler = None
        self._ImagePullSecrets = None
        self._RequestId = None

    @property
    def BasicInfo(self):
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def BasicConfig(self):
        return self._BasicConfig

    @BasicConfig.setter
    def BasicConfig(self, BasicConfig):
        self._BasicConfig = BasicConfig

    @property
    def Volumes(self):
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def InitContainers(self):
        return self._InitContainers

    @InitContainers.setter
    def InitContainers(self, InitContainers):
        self._InitContainers = InitContainers

    @property
    def Containers(self):
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def CronJob(self):
        return self._CronJob

    @CronJob.setter
    def CronJob(self, CronJob):
        self._CronJob = CronJob

    @property
    def RestartPolicy(self):
        return self._RestartPolicy

    @RestartPolicy.setter
    def RestartPolicy(self, RestartPolicy):
        self._RestartPolicy = RestartPolicy

    @property
    def HorizontalPodAutoscaler(self):
        return self._HorizontalPodAutoscaler

    @HorizontalPodAutoscaler.setter
    def HorizontalPodAutoscaler(self, HorizontalPodAutoscaler):
        self._HorizontalPodAutoscaler = HorizontalPodAutoscaler

    @property
    def ImagePullSecrets(self):
        return self._ImagePullSecrets

    @ImagePullSecrets.setter
    def ImagePullSecrets(self, ImagePullSecrets):
        self._ImagePullSecrets = ImagePullSecrets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self._BasicInfo = ApplicationBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("BasicConfig") is not None:
            self._BasicConfig = ApplicationBasicConfig()
            self._BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self._Volumes.append(obj)
        if params.get("InitContainers") is not None:
            self._InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self._InitContainers.append(obj)
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self._Containers.append(obj)
        if params.get("Service") is not None:
            self._Service = Service()
            self._Service._deserialize(params.get("Service"))
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self._CronJob = CronJob()
            self._CronJob._deserialize(params.get("CronJob"))
        self._RestartPolicy = params.get("RestartPolicy")
        if params.get("HorizontalPodAutoscaler") is not None:
            self._HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self._HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        self._ImagePullSecrets = params.get("ImagePullSecrets")
        self._RequestId = params.get("RequestId")


class DescribeApplicationYamlErrorRequest(AbstractModel):
    """DescribeApplicationYamlError请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Yaml: Yaml配置
        :type Yaml: str
        """
        self._Yaml = None

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationYamlErrorResponse(AbstractModel):
    """DescribeApplicationYamlError返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckPass: 是否通过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPass: bool
        :param _ErrType: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrType: int
        :param _ErrInfo: 错误信息
        :type ErrInfo: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckPass = None
        self._ErrType = None
        self._ErrInfo = None
        self._RequestId = None

    @property
    def CheckPass(self):
        return self._CheckPass

    @CheckPass.setter
    def CheckPass(self, CheckPass):
        self._CheckPass = CheckPass

    @property
    def ErrType(self):
        return self._ErrType

    @ErrType.setter
    def ErrType(self, ErrType):
        self._ErrType = ErrType

    @property
    def ErrInfo(self):
        return self._ErrInfo

    @ErrInfo.setter
    def ErrInfo(self, ErrInfo):
        self._ErrInfo = ErrInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CheckPass = params.get("CheckPass")
        self._ErrType = params.get("ErrType")
        self._ErrInfo = params.get("ErrInfo")
        self._RequestId = params.get("RequestId")


class DescribeApplicationYamlRequest(AbstractModel):
    """DescribeApplicationYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用模板ID
        :type ApplicationId: int
        """
        self._ApplicationId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationYamlResponse(AbstractModel):
    """DescribeApplicationYaml返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Yaml: base64 后的yaml
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Yaml = None
        self._RequestId = None

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Yaml = params.get("Yaml")
        self._RequestId = params.get("RequestId")


class DescribeApplicationsRequest(AbstractModel):
    """DescribeApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NamePattern: 模糊搜索字符串
        :type NamePattern: str
        :param _Offset: 默认 0
        :type Offset: int
        :param _Limit: 默认 20
        :type Limit: int
        :param _Sort: 仅支持对 DistributeTime 字段排序，ASC/DESC
        :type Sort: list of FieldSort
        """
        self._NamePattern = None
        self._Offset = None
        self._Limit = None
        self._Sort = None

    @property
    def NamePattern(self):
        return self._NamePattern

    @NamePattern.setter
    def NamePattern(self, NamePattern):
        self._NamePattern = NamePattern

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
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._NamePattern = params.get("NamePattern")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Sort") is not None:
            self._Sort = []
            for item in params.get("Sort"):
                obj = FieldSort()
                obj._deserialize(item)
                self._Sort.append(obj)
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
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ApplicationSet: 详细列表
        :type ApplicationSet: list of ApplicationTemplate
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ApplicationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApplicationSet(self):
        return self._ApplicationSet

    @ApplicationSet.setter
    def ApplicationSet(self, ApplicationSet):
        self._ApplicationSet = ApplicationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApplicationSet") is not None:
            self._ApplicationSet = []
            for item in params.get("ApplicationSet"):
                obj = ApplicationTemplate()
                obj._deserialize(item)
                self._ApplicationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigMapRequest(AbstractModel):
    """DescribeConfigMap请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _ConfigMapName: ConfigMap名称
        :type ConfigMapName: str
        :param _ConfigMapNamespace: ConfigMap命名空间
        :type ConfigMapNamespace: str
        """
        self._EdgeUnitID = None
        self._ConfigMapName = None
        self._ConfigMapNamespace = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def ConfigMapName(self):
        return self._ConfigMapName

    @ConfigMapName.setter
    def ConfigMapName(self, ConfigMapName):
        self._ConfigMapName = ConfigMapName

    @property
    def ConfigMapNamespace(self):
        return self._ConfigMapNamespace

    @ConfigMapNamespace.setter
    def ConfigMapNamespace(self, ConfigMapNamespace):
        self._ConfigMapNamespace = ConfigMapNamespace


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._ConfigMapName = params.get("ConfigMapName")
        self._ConfigMapNamespace = params.get("ConfigMapNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigMapResponse(AbstractModel):
    """DescribeConfigMap返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Yaml: yaml配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param _Json: 配置项的json格式(base64编码)
注意：此字段可能返回 null，表示取不到有效值。
        :type Json: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Namespace = None
        self._CreateTime = None
        self._Yaml = None
        self._Json = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def Json(self):
        return self._Json

    @Json.setter
    def Json(self, Json):
        self._Json = Json

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._CreateTime = params.get("CreateTime")
        self._Yaml = params.get("Yaml")
        self._Json = params.get("Json")
        self._RequestId = params.get("RequestId")


class DescribeConfigMapYamlErrorRequest(AbstractModel):
    """DescribeConfigMapYamlError请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Yaml: yaml文件
        :type Yaml: str
        """
        self._Yaml = None

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigMapYamlErrorResponse(AbstractModel):
    """DescribeConfigMapYamlError返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckPass: 校验是通过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPass: bool
        :param _ErrType: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrType: int
        :param _ErrInfo: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrInfo: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckPass = None
        self._ErrType = None
        self._ErrInfo = None
        self._RequestId = None

    @property
    def CheckPass(self):
        return self._CheckPass

    @CheckPass.setter
    def CheckPass(self, CheckPass):
        self._CheckPass = CheckPass

    @property
    def ErrType(self):
        return self._ErrType

    @ErrType.setter
    def ErrType(self, ErrType):
        self._ErrType = ErrType

    @property
    def ErrInfo(self):
        return self._ErrInfo

    @ErrInfo.setter
    def ErrInfo(self, ErrInfo):
        self._ErrInfo = ErrInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CheckPass = params.get("CheckPass")
        self._ErrType = params.get("ErrType")
        self._ErrInfo = params.get("ErrInfo")
        self._RequestId = params.get("RequestId")


class DescribeConfigMapsRequest(AbstractModel):
    """DescribeConfigMaps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _Offset: 翻页偏移量
        :type Offset: int
        :param _Limit: 每页大小(最大100)
        :type Limit: int
        :param _ConfigMapNamespace: 命名空间
        :type ConfigMapNamespace: str
        :param _NamePattern: 模糊匹配的名称
        :type NamePattern: str
        :param _Sort: Sort.Fileld填写CreateTime Sort.Order(ASC|DESC) 默认ASC
        :type Sort: :class:`tencentcloud.iecp.v20210914.models.FieldSort`
        """
        self._EdgeUnitID = None
        self._Offset = None
        self._Limit = None
        self._ConfigMapNamespace = None
        self._NamePattern = None
        self._Sort = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

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
    def ConfigMapNamespace(self):
        return self._ConfigMapNamespace

    @ConfigMapNamespace.setter
    def ConfigMapNamespace(self, ConfigMapNamespace):
        self._ConfigMapNamespace = ConfigMapNamespace

    @property
    def NamePattern(self):
        return self._NamePattern

    @NamePattern.setter
    def NamePattern(self, NamePattern):
        self._NamePattern = NamePattern

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ConfigMapNamespace = params.get("ConfigMapNamespace")
        self._NamePattern = params.get("NamePattern")
        if params.get("Sort") is not None:
            self._Sort = FieldSort()
            self._Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigMapsResponse(AbstractModel):
    """DescribeConfigMaps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: ConfigMap列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ConfigMapBasicInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConfigMapBasicInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDracoEdgeNodeInstallerRequest(AbstractModel):
    """DescribeDracoEdgeNodeInstaller请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SN: 设备SN
        :type SN: str
        """
        self._SN = None

    @property
    def SN(self):
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN


    def _deserialize(self, params):
        self._SN = params.get("SN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDracoEdgeNodeInstallerResponse(AbstractModel):
    """DescribeDracoEdgeNodeInstaller返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OnlineInstallationCommand: 在线安装命名
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineInstallationCommand: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OnlineInstallationCommand = None
        self._RequestId = None

    @property
    def OnlineInstallationCommand(self):
        return self._OnlineInstallationCommand

    @OnlineInstallationCommand.setter
    def OnlineInstallationCommand(self, OnlineInstallationCommand):
        self._OnlineInstallationCommand = OnlineInstallationCommand

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OnlineInstallationCommand = params.get("OnlineInstallationCommand")
        self._RequestId = params.get("RequestId")


class DescribeEdgeAgentNodeInstallerRequest(AbstractModel):
    """DescribeEdgeAgentNodeInstaller请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NodeId: IECP边缘节点ID
        :type NodeId: int
        """
        self._EdgeUnitId = None
        self._NodeId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeAgentNodeInstallerResponse(AbstractModel):
    """DescribeEdgeAgentNodeInstaller返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Online: 节点在线安装信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Online: :class:`tencentcloud.iecp.v20210914.models.EdgeNodeInstallerOnline`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Online = None
        self._RequestId = None

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Online") is not None:
            self._Online = EdgeNodeInstallerOnline()
            self._Online._deserialize(params.get("Online"))
        self._RequestId = params.get("RequestId")


class DescribeEdgeDefaultVpcRequest(AbstractModel):
    """DescribeEdgeDefaultVpc请求参数结构体

    """


class DescribeEdgeDefaultVpcResponse(AbstractModel):
    """DescribeEdgeDefaultVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcCidrBlock: 网络CIDR
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcCidrBlock: str
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _SubnetCidrBlock: 子网CIDR
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetCidrBlock: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VpcId = None
        self._VpcCidrBlock = None
        self._SubnetId = None
        self._SubnetCidrBlock = None
        self._RequestId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetCidrBlock(self):
        return self._SubnetCidrBlock

    @SubnetCidrBlock.setter
    def SubnetCidrBlock(self, SubnetCidrBlock):
        self._SubnetCidrBlock = SubnetCidrBlock

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._SubnetId = params.get("SubnetId")
        self._SubnetCidrBlock = params.get("SubnetCidrBlock")
        self._RequestId = params.get("RequestId")


class DescribeEdgeNodePodContainersRequest(AbstractModel):
    """DescribeEdgeNodePodContainers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NodeId: 节点ID
        :type NodeId: int
        :param _PodName: Pod名称
        :type PodName: str
        :param _Namespace: 命名空间
        :type Namespace: str
        """
        self._EdgeUnitId = None
        self._NodeId = None
        self._PodName = None
        self._Namespace = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeId = params.get("NodeId")
        self._PodName = params.get("PodName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeNodePodContainersResponse(AbstractModel):
    """DescribeEdgeNodePodContainers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ContainerSet: Pod容器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerSet: list of EdgeNodePodContainerInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ContainerSet = None
        self._RequestId = None

    @property
    def ContainerSet(self):
        return self._ContainerSet

    @ContainerSet.setter
    def ContainerSet(self, ContainerSet):
        self._ContainerSet = ContainerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ContainerSet") is not None:
            self._ContainerSet = []
            for item in params.get("ContainerSet"):
                obj = EdgeNodePodContainerInfo()
                obj._deserialize(item)
                self._ContainerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeNodePodsRequest(AbstractModel):
    """DescribeEdgeNodePods请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NodeId: 节点ID
        :type NodeId: int
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _PodNamePattern: Pod名称过滤串
        :type PodNamePattern: str
        """
        self._EdgeUnitId = None
        self._NodeId = None
        self._Namespace = None
        self._PodNamePattern = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def PodNamePattern(self):
        return self._PodNamePattern

    @PodNamePattern.setter
    def PodNamePattern(self, PodNamePattern):
        self._PodNamePattern = PodNamePattern


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeId = params.get("NodeId")
        self._Namespace = params.get("Namespace")
        self._PodNamePattern = params.get("PodNamePattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeNodePodsResponse(AbstractModel):
    """DescribeEdgeNodePods返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PodSet: Pod列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodSet: list of EdgeNodePodInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PodSet = None
        self._RequestId = None

    @property
    def PodSet(self):
        return self._PodSet

    @PodSet.setter
    def PodSet(self, PodSet):
        self._PodSet = PodSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PodSet") is not None:
            self._PodSet = []
            for item in params.get("PodSet"):
                obj = EdgeNodePodInfo()
                obj._deserialize(item)
                self._PodSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeNodeRemarkListRequest(AbstractModel):
    """DescribeEdgeNodeRemarkList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 边缘单元ID
        :type EdgeUnitId: int
        """
        self._EdgeUnitId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeNodeRemarkListResponse(AbstractModel):
    """DescribeEdgeNodeRemarkList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Remarks: 边缘单元内的备注列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Remarks: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Remarks = None
        self._RequestId = None

    @property
    def Remarks(self):
        return self._Remarks

    @Remarks.setter
    def Remarks(self, Remarks):
        self._Remarks = Remarks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Remarks = params.get("Remarks")
        self._RequestId = params.get("RequestId")


class DescribeEdgeNodeRequest(AbstractModel):
    """DescribeEdgeNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NodeId: IECP边缘节点ID
        :type NodeId: int
        """
        self._EdgeUnitId = None
        self._NodeId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeNodeResponse(AbstractModel):
    """DescribeEdgeNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Kind: 节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Kind: str
        :param _Name: 节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Status: 节点状态 （1健康｜2异常｜3离线｜4未激活）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CpuArchitecture: CPU体系结构
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuArchitecture: str
        :param _AiChipArchitecture: AI处理器体系结构
注意：此字段可能返回 null，表示取不到有效值。
        :type AiChipArchitecture: str
        :param _Ip: IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Labels: 节点标签列表
        :type Labels: list of EdgeNodeLabel
        :param _Resource: 节点资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: :class:`tencentcloud.iecp.v20210914.models.EdgeNodeResourceInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._Kind = None
        self._Name = None
        self._Status = None
        self._CpuArchitecture = None
        self._AiChipArchitecture = None
        self._Ip = None
        self._Labels = None
        self._Resource = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

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
    def CpuArchitecture(self):
        return self._CpuArchitecture

    @CpuArchitecture.setter
    def CpuArchitecture(self, CpuArchitecture):
        self._CpuArchitecture = CpuArchitecture

    @property
    def AiChipArchitecture(self):
        return self._AiChipArchitecture

    @AiChipArchitecture.setter
    def AiChipArchitecture(self, AiChipArchitecture):
        self._AiChipArchitecture = AiChipArchitecture

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Kind = params.get("Kind")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._CpuArchitecture = params.get("CpuArchitecture")
        self._AiChipArchitecture = params.get("AiChipArchitecture")
        self._Ip = params.get("Ip")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = EdgeNodeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Resource") is not None:
            self._Resource = EdgeNodeResourceInfo()
            self._Resource._deserialize(params.get("Resource"))
        self._RequestId = params.get("RequestId")


class DescribeEdgeNodesRequest(AbstractModel):
    """DescribeEdgeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NamePattern: 边缘节点名称模糊搜索串
        :type NamePattern: str
        :param _NameMatchedList: 边缘节点名称列表，支持批量查询 ，优先于模糊查询
        :type NameMatchedList: list of str
        :param _Sort: 排序信息列表
        :type Sort: list of Sort
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 页面大小Limit
        :type Limit: int
        :param _NodeType: 节点类型
        :type NodeType: int
        """
        self._EdgeUnitId = None
        self._NamePattern = None
        self._NameMatchedList = None
        self._Sort = None
        self._Offset = None
        self._Limit = None
        self._NodeType = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NamePattern(self):
        return self._NamePattern

    @NamePattern.setter
    def NamePattern(self, NamePattern):
        self._NamePattern = NamePattern

    @property
    def NameMatchedList(self):
        return self._NameMatchedList

    @NameMatchedList.setter
    def NameMatchedList(self, NameMatchedList):
        self._NameMatchedList = NameMatchedList

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NamePattern = params.get("NamePattern")
        self._NameMatchedList = params.get("NameMatchedList")
        if params.get("Sort") is not None:
            self._Sort = []
            for item in params.get("Sort"):
                obj = Sort()
                obj._deserialize(item)
                self._Sort.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeNodesResponse(AbstractModel):
    """DescribeEdgeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 边缘节点数量
        :type TotalCount: int
        :param _NodeSet: 节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of EdgeNodeInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NodeSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = EdgeNodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeOperationLogsRequest(AbstractModel):
    """DescribeEdgeOperationLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 开始时间
        :type BeginTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 翻页大小
        :type Limit: int
        :param _Sort: 排序字段
        :type Sort: list of FieldSort
        :param _Module: 模块
        :type Module: str
        :param _Condition: 过滤条件
        :type Condition: :class:`tencentcloud.iecp.v20210914.models.OperationLogsCondition`
        """
        self._BeginTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._Sort = None
        self._Module = None
        self._Condition = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Sort") is not None:
            self._Sort = []
            for item in params.get("Sort"):
                obj = FieldSort()
                obj._deserialize(item)
                self._Sort.append(obj)
        self._Module = params.get("Module")
        if params.get("Condition") is not None:
            self._Condition = OperationLogsCondition()
            self._Condition._deserialize(params.get("Condition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeOperationLogsResponse(AbstractModel):
    """DescribeEdgeOperationLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _OperationLogSet: 操作日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationLogSet: list of OperationLog
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._OperationLogSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OperationLogSet(self):
        return self._OperationLogSet

    @OperationLogSet.setter
    def OperationLogSet(self, OperationLogSet):
        self._OperationLogSet = OperationLogSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("OperationLogSet") is not None:
            self._OperationLogSet = []
            for item in params.get("OperationLogSet"):
                obj = OperationLog()
                obj._deserialize(item)
                self._OperationLogSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgePodRequest(AbstractModel):
    """DescribeEdgePod请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Name: Pod名称
        :type Name: str
        """
        self._EdgeUnitId = None
        self._Namespace = None
        self._Name = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Namespace = params.get("Namespace")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgePodResponse(AbstractModel):
    """DescribeEdgePod返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Pod: Pod详情信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Pod: :class:`tencentcloud.iecp.v20210914.models.EdgeNodePodInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Pod = None
        self._RequestId = None

    @property
    def Pod(self):
        return self._Pod

    @Pod.setter
    def Pod(self, Pod):
        self._Pod = Pod

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Pod") is not None:
            self._Pod = EdgeNodePodInfo()
            self._Pod._deserialize(params.get("Pod"))
        self._RequestId = params.get("RequestId")


class DescribeEdgeSnNodesRequest(AbstractModel):
    """DescribeEdgeSnNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 边缘单元ID
        :type EdgeUnitId: int
        :param _NamePattern: 根据节点名称模糊匹配
        :type NamePattern: str
        :param _SNPattern: 根据设备SN模糊匹配
        :type SNPattern: str
        :param _RemarkPattern: 根据备注批次信息模糊匹配
        :type RemarkPattern: str
        :param _Offset: 默认0
        :type Offset: int
        :param _Limit: 默认20
        :type Limit: int
        """
        self._EdgeUnitId = None
        self._NamePattern = None
        self._SNPattern = None
        self._RemarkPattern = None
        self._Offset = None
        self._Limit = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NamePattern(self):
        return self._NamePattern

    @NamePattern.setter
    def NamePattern(self, NamePattern):
        self._NamePattern = NamePattern

    @property
    def SNPattern(self):
        return self._SNPattern

    @SNPattern.setter
    def SNPattern(self, SNPattern):
        self._SNPattern = SNPattern

    @property
    def RemarkPattern(self):
        return self._RemarkPattern

    @RemarkPattern.setter
    def RemarkPattern(self, RemarkPattern):
        self._RemarkPattern = RemarkPattern

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


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NamePattern = params.get("NamePattern")
        self._SNPattern = params.get("SNPattern")
        self._RemarkPattern = params.get("RemarkPattern")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeSnNodesResponse(AbstractModel):
    """DescribeEdgeSnNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足条件的总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _NodeSet: 节点详情
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of EdgeDracoNodeInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NodeSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = EdgeDracoNodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationEventsRequest(AbstractModel):
    """DescribeEdgeUnitApplicationEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self._EdgeUnitId = None
        self._ApplicationId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationEventsResponse(AbstractModel):
    """DescribeEdgeUnitApplicationEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventSet: 事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EventSet: list of Event
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventSet = None
        self._RequestId = None

    @property
    def EventSet(self):
        return self._EventSet

    @EventSet.setter
    def EventSet(self, EventSet):
        self._EventSet = EventSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EventSet") is not None:
            self._EventSet = []
            for item in params.get("EventSet"):
                obj = Event()
                obj._deserialize(item)
                self._EventSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationLogsRequest(AbstractModel):
    """DescribeEdgeUnitApplicationLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        :param _Limit: 最大条数
        :type Limit: int
        :param _PodName: Pod名
        :type PodName: str
        :param _ContainerName: 容器名
        :type ContainerName: str
        """
        self._EdgeUnitId = None
        self._ApplicationId = None
        self._Limit = None
        self._PodName = None
        self._ContainerName = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

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
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def ContainerName(self):
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._ApplicationId = params.get("ApplicationId")
        self._Limit = params.get("Limit")
        self._PodName = params.get("PodName")
        self._ContainerName = params.get("ContainerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationLogsResponse(AbstractModel):
    """DescribeEdgeUnitApplicationLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogSet: 日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogSet = None
        self._RequestId = None

    @property
    def LogSet(self):
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogSet = params.get("LogSet")
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationPodContainersRequest(AbstractModel):
    """DescribeEdgeUnitApplicationPodContainers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        :param _PodName: Pod名
        :type PodName: str
        """
        self._EdgeUnitId = None
        self._ApplicationId = None
        self._PodName = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

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


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._ApplicationId = params.get("ApplicationId")
        self._PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationPodContainersResponse(AbstractModel):
    """DescribeEdgeUnitApplicationPodContainers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ContainerSet: 容器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerSet: list of ContainerStatus
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ContainerSet = None
        self._RequestId = None

    @property
    def ContainerSet(self):
        return self._ContainerSet

    @ContainerSet.setter
    def ContainerSet(self, ContainerSet):
        self._ContainerSet = ContainerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ContainerSet") is not None:
            self._ContainerSet = []
            for item in params.get("ContainerSet"):
                obj = ContainerStatus()
                obj._deserialize(item)
                self._ContainerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationPodsRequest(AbstractModel):
    """DescribeEdgeUnitApplicationPods请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self._EdgeUnitId = None
        self._ApplicationId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationPodsResponse(AbstractModel):
    """DescribeEdgeUnitApplicationPods返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PodSet: Pod列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodSet: list of PodStatus
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PodSet = None
        self._RequestId = None

    @property
    def PodSet(self):
        return self._PodSet

    @PodSet.setter
    def PodSet(self, PodSet):
        self._PodSet = PodSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PodSet") is not None:
            self._PodSet = []
            for item in params.get("PodSet"):
                obj = PodStatus()
                obj._deserialize(item)
                self._PodSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationVisualizationRequest(AbstractModel):
    """DescribeEdgeUnitApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self._EdgeUnitId = None
        self._ApplicationId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationVisualizationResponse(AbstractModel):
    """DescribeEdgeUnitApplicationVisualization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BasicInfo: 基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        :param _BasicConfig: 基本配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param _Volumes: 卷配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Volumes: list of Volume
        :param _InitContainers: 初始化容器配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InitContainers: list of Container
        :param _Containers: 容器配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Containers: list of Container
        :param _Service: 服务配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param _Job: Job配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param _CronJob: CronJob配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param _RestartPolicy: 重启策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartPolicy: str
        :param _HorizontalPodAutoscaler: HPA
注意：此字段可能返回 null，表示取不到有效值。
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        :param _ImagePullSecrets: 镜像拉取Secret
注意：此字段可能返回 null，表示取不到有效值。
        :type ImagePullSecrets: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BasicInfo = None
        self._BasicConfig = None
        self._Volumes = None
        self._InitContainers = None
        self._Containers = None
        self._Service = None
        self._Job = None
        self._CronJob = None
        self._RestartPolicy = None
        self._HorizontalPodAutoscaler = None
        self._ImagePullSecrets = None
        self._RequestId = None

    @property
    def BasicInfo(self):
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def BasicConfig(self):
        return self._BasicConfig

    @BasicConfig.setter
    def BasicConfig(self, BasicConfig):
        self._BasicConfig = BasicConfig

    @property
    def Volumes(self):
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def InitContainers(self):
        return self._InitContainers

    @InitContainers.setter
    def InitContainers(self, InitContainers):
        self._InitContainers = InitContainers

    @property
    def Containers(self):
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def CronJob(self):
        return self._CronJob

    @CronJob.setter
    def CronJob(self, CronJob):
        self._CronJob = CronJob

    @property
    def RestartPolicy(self):
        return self._RestartPolicy

    @RestartPolicy.setter
    def RestartPolicy(self, RestartPolicy):
        self._RestartPolicy = RestartPolicy

    @property
    def HorizontalPodAutoscaler(self):
        return self._HorizontalPodAutoscaler

    @HorizontalPodAutoscaler.setter
    def HorizontalPodAutoscaler(self, HorizontalPodAutoscaler):
        self._HorizontalPodAutoscaler = HorizontalPodAutoscaler

    @property
    def ImagePullSecrets(self):
        return self._ImagePullSecrets

    @ImagePullSecrets.setter
    def ImagePullSecrets(self, ImagePullSecrets):
        self._ImagePullSecrets = ImagePullSecrets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self._BasicInfo = ApplicationBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("BasicConfig") is not None:
            self._BasicConfig = ApplicationBasicConfig()
            self._BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self._Volumes.append(obj)
        if params.get("InitContainers") is not None:
            self._InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self._InitContainers.append(obj)
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self._Containers.append(obj)
        if params.get("Service") is not None:
            self._Service = Service()
            self._Service._deserialize(params.get("Service"))
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self._CronJob = CronJob()
            self._CronJob._deserialize(params.get("CronJob"))
        self._RestartPolicy = params.get("RestartPolicy")
        if params.get("HorizontalPodAutoscaler") is not None:
            self._HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self._HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        self._ImagePullSecrets = params.get("ImagePullSecrets")
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationYamlErrorRequest(AbstractModel):
    """DescribeEdgeUnitApplicationYamlError请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Yaml: Yaml配置
        :type Yaml: str
        """
        self._Yaml = None

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationYamlErrorResponse(AbstractModel):
    """DescribeEdgeUnitApplicationYamlError返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckPass: 是否通过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPass: bool
        :param _ErrType: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrType: int
        :param _ErrInfo: 错误信息
        :type ErrInfo: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckPass = None
        self._ErrType = None
        self._ErrInfo = None
        self._RequestId = None

    @property
    def CheckPass(self):
        return self._CheckPass

    @CheckPass.setter
    def CheckPass(self, CheckPass):
        self._CheckPass = CheckPass

    @property
    def ErrType(self):
        return self._ErrType

    @ErrType.setter
    def ErrType(self, ErrType):
        self._ErrType = ErrType

    @property
    def ErrInfo(self):
        return self._ErrInfo

    @ErrInfo.setter
    def ErrInfo(self, ErrInfo):
        self._ErrInfo = ErrInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CheckPass = params.get("CheckPass")
        self._ErrType = params.get("ErrType")
        self._ErrInfo = params.get("ErrInfo")
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationYamlRequest(AbstractModel):
    """DescribeEdgeUnitApplicationYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self._EdgeUnitId = None
        self._ApplicationId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationYamlResponse(AbstractModel):
    """DescribeEdgeUnitApplicationYaml返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Yaml: Yaml配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Yaml = None
        self._RequestId = None

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Yaml = params.get("Yaml")
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationsRequest(AbstractModel):
    """DescribeEdgeUnitApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _Offset: 翻页偏移
        :type Offset: int
        :param _Limit: 翻页大小
        :type Limit: int
        :param _NamePattern: 名称模糊匹配
        :type NamePattern: str
        :param _Sort: 字段排序 (Sort.Filed为:StartTime）
        :type Sort: list of FieldSort
        :param _Namespace: 命名空间过滤
        :type Namespace: str
        """
        self._EdgeUnitId = None
        self._Offset = None
        self._Limit = None
        self._NamePattern = None
        self._Sort = None
        self._Namespace = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

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
    def NamePattern(self):
        return self._NamePattern

    @NamePattern.setter
    def NamePattern(self, NamePattern):
        self._NamePattern = NamePattern

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NamePattern = params.get("NamePattern")
        if params.get("Sort") is not None:
            self._Sort = []
            for item in params.get("Sort"):
                obj = FieldSort()
                obj._deserialize(item)
                self._Sort.append(obj)
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationsResponse(AbstractModel):
    """DescribeEdgeUnitApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ApplicationSet: 应用列表
        :type ApplicationSet: list of ApplicationStatusInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ApplicationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApplicationSet(self):
        return self._ApplicationSet

    @ApplicationSet.setter
    def ApplicationSet(self, ApplicationSet):
        self._ApplicationSet = ApplicationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApplicationSet") is not None:
            self._ApplicationSet = []
            for item in params.get("ApplicationSet"):
                obj = ApplicationStatusInfo()
                obj._deserialize(item)
                self._ApplicationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitCloudRequest(AbstractModel):
    """DescribeEdgeUnitCloud请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 边缘集群ID
        :type EdgeUnitId: int
        """
        self._EdgeUnitId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitCloudResponse(AbstractModel):
    """DescribeEdgeUnitCloud返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 边缘集群名称
        :type Name: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _LiveTime: 集群最后探活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveTime: str
        :param _MasterStatus: 集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterStatus: str
        :param _K8sVersion: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type K8sVersion: str
        :param _PodCIDR: pod cidr
注意：此字段可能返回 null，表示取不到有效值。
        :type PodCIDR: str
        :param _ServiceCIDR: service cidr
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCIDR: str
        :param _APIServerAddress: 集群内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type APIServerAddress: str
        :param _APIServerExposeAddress: 集群外网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type APIServerExposeAddress: str
        :param _UID: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UID: str
        :param _UnitID: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitID: int
        :param _Cluster: 集群标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Cluster: str
        :param _Node: 节点统计
注意：此字段可能返回 null，表示取不到有效值。
        :type Node: :class:`tencentcloud.iecp.v20210914.models.EdgeUnitStatisticItem`
        :param _Workload: 工作负载统计
注意：此字段可能返回 null，表示取不到有效值。
        :type Workload: :class:`tencentcloud.iecp.v20210914.models.EdgeUnitStatisticItem`
        :param _Grid: Grid应用统计
注意：此字段可能返回 null，表示取不到有效值。
        :type Grid: :class:`tencentcloud.iecp.v20210914.models.EdgeUnitStatisticItem`
        :param _SubDevice: 设备统计
注意：此字段可能返回 null，表示取不到有效值。
        :type SubDevice: :class:`tencentcloud.iecp.v20210914.models.EdgeUnitStatisticItem`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LiveTime = None
        self._MasterStatus = None
        self._K8sVersion = None
        self._PodCIDR = None
        self._ServiceCIDR = None
        self._APIServerAddress = None
        self._APIServerExposeAddress = None
        self._UID = None
        self._UnitID = None
        self._Cluster = None
        self._Node = None
        self._Workload = None
        self._Grid = None
        self._SubDevice = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
    def LiveTime(self):
        return self._LiveTime

    @LiveTime.setter
    def LiveTime(self, LiveTime):
        self._LiveTime = LiveTime

    @property
    def MasterStatus(self):
        return self._MasterStatus

    @MasterStatus.setter
    def MasterStatus(self, MasterStatus):
        self._MasterStatus = MasterStatus

    @property
    def K8sVersion(self):
        return self._K8sVersion

    @K8sVersion.setter
    def K8sVersion(self, K8sVersion):
        self._K8sVersion = K8sVersion

    @property
    def PodCIDR(self):
        return self._PodCIDR

    @PodCIDR.setter
    def PodCIDR(self, PodCIDR):
        self._PodCIDR = PodCIDR

    @property
    def ServiceCIDR(self):
        return self._ServiceCIDR

    @ServiceCIDR.setter
    def ServiceCIDR(self, ServiceCIDR):
        self._ServiceCIDR = ServiceCIDR

    @property
    def APIServerAddress(self):
        return self._APIServerAddress

    @APIServerAddress.setter
    def APIServerAddress(self, APIServerAddress):
        self._APIServerAddress = APIServerAddress

    @property
    def APIServerExposeAddress(self):
        return self._APIServerExposeAddress

    @APIServerExposeAddress.setter
    def APIServerExposeAddress(self, APIServerExposeAddress):
        self._APIServerExposeAddress = APIServerExposeAddress

    @property
    def UID(self):
        return self._UID

    @UID.setter
    def UID(self, UID):
        self._UID = UID

    @property
    def UnitID(self):
        return self._UnitID

    @UnitID.setter
    def UnitID(self, UnitID):
        self._UnitID = UnitID

    @property
    def Cluster(self):
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def Node(self):
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node

    @property
    def Workload(self):
        return self._Workload

    @Workload.setter
    def Workload(self, Workload):
        self._Workload = Workload

    @property
    def Grid(self):
        return self._Grid

    @Grid.setter
    def Grid(self, Grid):
        self._Grid = Grid

    @property
    def SubDevice(self):
        return self._SubDevice

    @SubDevice.setter
    def SubDevice(self, SubDevice):
        self._SubDevice = SubDevice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._LiveTime = params.get("LiveTime")
        self._MasterStatus = params.get("MasterStatus")
        self._K8sVersion = params.get("K8sVersion")
        self._PodCIDR = params.get("PodCIDR")
        self._ServiceCIDR = params.get("ServiceCIDR")
        self._APIServerAddress = params.get("APIServerAddress")
        self._APIServerExposeAddress = params.get("APIServerExposeAddress")
        self._UID = params.get("UID")
        self._UnitID = params.get("UnitID")
        self._Cluster = params.get("Cluster")
        if params.get("Node") is not None:
            self._Node = EdgeUnitStatisticItem()
            self._Node._deserialize(params.get("Node"))
        if params.get("Workload") is not None:
            self._Workload = EdgeUnitStatisticItem()
            self._Workload._deserialize(params.get("Workload"))
        if params.get("Grid") is not None:
            self._Grid = EdgeUnitStatisticItem()
            self._Grid._deserialize(params.get("Grid"))
        if params.get("SubDevice") is not None:
            self._SubDevice = EdgeUnitStatisticItem()
            self._SubDevice._deserialize(params.get("SubDevice"))
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitDeployGridItemRequest(AbstractModel):
    """DescribeEdgeUnitDeployGridItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 边缘单元ID
        :type EdgeUnitId: int
        :param _GridName: Grid名称
        :type GridName: str
        :param _WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param _Namespace: 命名空间，默认default
        :type Namespace: str
        :param _Order: 排序，默认ASC
        :type Order: str
        """
        self._EdgeUnitId = None
        self._GridName = None
        self._WorkloadKind = None
        self._Namespace = None
        self._Order = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def GridName(self):
        return self._GridName

    @GridName.setter
    def GridName(self, GridName):
        self._GridName = GridName

    @property
    def WorkloadKind(self):
        return self._WorkloadKind

    @WorkloadKind.setter
    def WorkloadKind(self, WorkloadKind):
        self._WorkloadKind = WorkloadKind

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._GridName = params.get("GridName")
        self._WorkloadKind = params.get("WorkloadKind")
        self._Namespace = params.get("Namespace")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitDeployGridItemResponse(AbstractModel):
    """DescribeEdgeUnitDeployGridItem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数
        :type TotalCount: int
        :param _DeploySet: Grid部署列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploySet: list of GridItemInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeploySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeploySet(self):
        return self._DeploySet

    @DeploySet.setter
    def DeploySet(self, DeploySet):
        self._DeploySet = DeploySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DeploySet") is not None:
            self._DeploySet = []
            for item in params.get("DeploySet"):
                obj = GridItemInfo()
                obj._deserialize(item)
                self._DeploySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitDeployGridItemYamlRequest(AbstractModel):
    """DescribeEdgeUnitDeployGridItemYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param _GridItemName: Grid部署项名称
        :type GridItemName: str
        :param _Namespace: 命名空间，默认default
        :type Namespace: str
        """
        self._EdgeUnitId = None
        self._WorkloadKind = None
        self._GridItemName = None
        self._Namespace = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def WorkloadKind(self):
        return self._WorkloadKind

    @WorkloadKind.setter
    def WorkloadKind(self, WorkloadKind):
        self._WorkloadKind = WorkloadKind

    @property
    def GridItemName(self):
        return self._GridItemName

    @GridItemName.setter
    def GridItemName(self, GridItemName):
        self._GridItemName = GridItemName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._WorkloadKind = params.get("WorkloadKind")
        self._GridItemName = params.get("GridItemName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitDeployGridItemYamlResponse(AbstractModel):
    """DescribeEdgeUnitDeployGridItemYaml返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Yaml: yaml，base64编码字符串
        :type Yaml: str
        :param _Replicas: 对应类型的副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: list of int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Yaml = None
        self._Replicas = None
        self._RequestId = None

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Yaml = params.get("Yaml")
        self._Replicas = params.get("Replicas")
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitDeployGridRequest(AbstractModel):
    """DescribeEdgeUnitDeployGrid请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _Namespace: 命名空间，默认为default
        :type Namespace: str
        :param _NamePattern: 模糊匹配
        :type NamePattern: str
        :param _Offset: 分页offset，默认为0
        :type Offset: int
        :param _Limit: 分页limit，默认为20
        :type Limit: int
        :param _Order: 排序，默认为ASC
        :type Order: str
        """
        self._EdgeUnitId = None
        self._Namespace = None
        self._NamePattern = None
        self._Offset = None
        self._Limit = None
        self._Order = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def NamePattern(self):
        return self._NamePattern

    @NamePattern.setter
    def NamePattern(self, NamePattern):
        self._NamePattern = NamePattern

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Namespace = params.get("Namespace")
        self._NamePattern = params.get("NamePattern")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitDeployGridResponse(AbstractModel):
    """DescribeEdgeUnitDeployGrid返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数
        :type TotalCount: int
        :param _GridSet: Grid列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GridSet: list of GridInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._GridSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GridSet(self):
        return self._GridSet

    @GridSet.setter
    def GridSet(self, GridSet):
        self._GridSet = GridSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("GridSet") is not None:
            self._GridSet = []
            for item in params.get("GridSet"):
                obj = GridInfo()
                obj._deserialize(item)
                self._GridSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitExtraRequest(AbstractModel):
    """DescribeEdgeUnitExtra请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        """
        self._EdgeUnitId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitExtraResponse(AbstractModel):
    """DescribeEdgeUnitExtra返回参数结构体

    """

    def __init__(self):
        r"""
        :param _APIServerType: APIServer类型
        :type APIServerType: str
        :param _APIServerURL: 域名URL
        :type APIServerURL: str
        :param _APIServerURLPort: 域名URL对应的端口
        :type APIServerURLPort: str
        :param _APIServerResolveIP: 域名URL对应的端口
        :type APIServerResolveIP: str
        :param _APIServerExposeAddress: 对外可访问的IP
        :type APIServerExposeAddress: str
        :param _IsCreatePrometheus: 是否开启监控
        :type IsCreatePrometheus: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._APIServerType = None
        self._APIServerURL = None
        self._APIServerURLPort = None
        self._APIServerResolveIP = None
        self._APIServerExposeAddress = None
        self._IsCreatePrometheus = None
        self._RequestId = None

    @property
    def APIServerType(self):
        return self._APIServerType

    @APIServerType.setter
    def APIServerType(self, APIServerType):
        self._APIServerType = APIServerType

    @property
    def APIServerURL(self):
        return self._APIServerURL

    @APIServerURL.setter
    def APIServerURL(self, APIServerURL):
        self._APIServerURL = APIServerURL

    @property
    def APIServerURLPort(self):
        return self._APIServerURLPort

    @APIServerURLPort.setter
    def APIServerURLPort(self, APIServerURLPort):
        self._APIServerURLPort = APIServerURLPort

    @property
    def APIServerResolveIP(self):
        return self._APIServerResolveIP

    @APIServerResolveIP.setter
    def APIServerResolveIP(self, APIServerResolveIP):
        self._APIServerResolveIP = APIServerResolveIP

    @property
    def APIServerExposeAddress(self):
        return self._APIServerExposeAddress

    @APIServerExposeAddress.setter
    def APIServerExposeAddress(self, APIServerExposeAddress):
        self._APIServerExposeAddress = APIServerExposeAddress

    @property
    def IsCreatePrometheus(self):
        return self._IsCreatePrometheus

    @IsCreatePrometheus.setter
    def IsCreatePrometheus(self, IsCreatePrometheus):
        self._IsCreatePrometheus = IsCreatePrometheus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._APIServerType = params.get("APIServerType")
        self._APIServerURL = params.get("APIServerURL")
        self._APIServerURLPort = params.get("APIServerURLPort")
        self._APIServerResolveIP = params.get("APIServerResolveIP")
        self._APIServerExposeAddress = params.get("APIServerExposeAddress")
        self._IsCreatePrometheus = params.get("IsCreatePrometheus")
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitGridEventsRequest(AbstractModel):
    """DescribeEdgeUnitGridEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _GridName: Grid名称
        :type GridName: str
        :param _WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param _Namespace: 命名空间，默认为default
        :type Namespace: str
        :param _NodeUnit: NodeUnit名称
        :type NodeUnit: str
        :param _PodName: Pod名称
        :type PodName: str
        """
        self._EdgeUnitId = None
        self._GridName = None
        self._WorkloadKind = None
        self._Namespace = None
        self._NodeUnit = None
        self._PodName = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def GridName(self):
        return self._GridName

    @GridName.setter
    def GridName(self, GridName):
        self._GridName = GridName

    @property
    def WorkloadKind(self):
        return self._WorkloadKind

    @WorkloadKind.setter
    def WorkloadKind(self, WorkloadKind):
        self._WorkloadKind = WorkloadKind

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def NodeUnit(self):
        return self._NodeUnit

    @NodeUnit.setter
    def NodeUnit(self, NodeUnit):
        self._NodeUnit = NodeUnit

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._GridName = params.get("GridName")
        self._WorkloadKind = params.get("WorkloadKind")
        self._Namespace = params.get("Namespace")
        self._NodeUnit = params.get("NodeUnit")
        self._PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitGridEventsResponse(AbstractModel):
    """DescribeEdgeUnitGridEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventSet: 事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EventSet: list of GridEventInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventSet = None
        self._RequestId = None

    @property
    def EventSet(self):
        return self._EventSet

    @EventSet.setter
    def EventSet(self, EventSet):
        self._EventSet = EventSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EventSet") is not None:
            self._EventSet = []
            for item in params.get("EventSet"):
                obj = GridEventInfo()
                obj._deserialize(item)
                self._EventSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitGridPodsRequest(AbstractModel):
    """DescribeEdgeUnitGridPods请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _GridName: Grid名称
        :type GridName: str
        :param _WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param _NodeUnit: NodeUnit名
        :type NodeUnit: str
        :param _Namespace: 命名空间，默认default
        :type Namespace: str
        """
        self._EdgeUnitId = None
        self._GridName = None
        self._WorkloadKind = None
        self._NodeUnit = None
        self._Namespace = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def GridName(self):
        return self._GridName

    @GridName.setter
    def GridName(self, GridName):
        self._GridName = GridName

    @property
    def WorkloadKind(self):
        return self._WorkloadKind

    @WorkloadKind.setter
    def WorkloadKind(self, WorkloadKind):
        self._WorkloadKind = WorkloadKind

    @property
    def NodeUnit(self):
        return self._NodeUnit

    @NodeUnit.setter
    def NodeUnit(self, NodeUnit):
        self._NodeUnit = NodeUnit

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._GridName = params.get("GridName")
        self._WorkloadKind = params.get("WorkloadKind")
        self._NodeUnit = params.get("NodeUnit")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitGridPodsResponse(AbstractModel):
    """DescribeEdgeUnitGridPods返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PodSet: Pod列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodSet: list of GridPodInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PodSet = None
        self._RequestId = None

    @property
    def PodSet(self):
        return self._PodSet

    @PodSet.setter
    def PodSet(self, PodSet):
        self._PodSet = PodSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PodSet") is not None:
            self._PodSet = []
            for item in params.get("PodSet"):
                obj = GridPodInfo()
                obj._deserialize(item)
                self._PodSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitMonitorStatusRequest(AbstractModel):
    """DescribeEdgeUnitMonitorStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        """
        self._EdgeUnitId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitMonitorStatusResponse(AbstractModel):
    """DescribeEdgeUnitMonitorStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorStatus: 监控状态描述：
"running" 单元监控正常运行
"deploying" 单元监控部署中
"norsc" 单元需要可用节点以部署监控
"abnormal" 单元监控异常
"none" 单元监控不可用
        :type MonitorStatus: str
        :param _IsAvailable: 监控是否就绪
        :type IsAvailable: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MonitorStatus = None
        self._IsAvailable = None
        self._RequestId = None

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def IsAvailable(self):
        return self._IsAvailable

    @IsAvailable.setter
    def IsAvailable(self, IsAvailable):
        self._IsAvailable = IsAvailable

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MonitorStatus = params.get("MonitorStatus")
        self._IsAvailable = params.get("IsAvailable")
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitNodeGroupRequest(AbstractModel):
    """DescribeEdgeUnitNodeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _Namespace: 命名空间，默认为default
        :type Namespace: str
        :param _Offset: 分页offset，默认为0
        :type Offset: int
        :param _Limit: 分页limit，默认为20
        :type Limit: int
        :param _NameFilter: 模糊匹配参数，精确匹配时失效
        :type NameFilter: str
        :param _NameMatched: 精确匹配参数
        :type NameMatched: str
        :param _Order: 按时间排序，ASC/DESC，默认为DESC
        :type Order: str
        """
        self._EdgeUnitId = None
        self._Namespace = None
        self._Offset = None
        self._Limit = None
        self._NameFilter = None
        self._NameMatched = None
        self._Order = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

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
    def NameFilter(self):
        return self._NameFilter

    @NameFilter.setter
    def NameFilter(self, NameFilter):
        self._NameFilter = NameFilter

    @property
    def NameMatched(self):
        return self._NameMatched

    @NameMatched.setter
    def NameMatched(self, NameMatched):
        self._NameMatched = NameMatched

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Namespace = params.get("Namespace")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NameFilter = params.get("NameFilter")
        self._NameMatched = params.get("NameMatched")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitNodeGroupResponse(AbstractModel):
    """DescribeEdgeUnitNodeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 记录总数
        :type Total: int
        :param _NodeGroupInfo: NodeGroup数组
        :type NodeGroupInfo: list of NodeGroupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._NodeGroupInfo = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def NodeGroupInfo(self):
        return self._NodeGroupInfo

    @NodeGroupInfo.setter
    def NodeGroupInfo(self, NodeGroupInfo):
        self._NodeGroupInfo = NodeGroupInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("NodeGroupInfo") is not None:
            self._NodeGroupInfo = []
            for item in params.get("NodeGroupInfo"):
                obj = NodeGroupInfo()
                obj._deserialize(item)
                self._NodeGroupInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitNodeUnitTemplatesRequest(AbstractModel):
    """DescribeEdgeUnitNodeUnitTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _Namespace: 命名空间，默认为default
        :type Namespace: str
        :param _Offset: 分页查询offset，默认为0
        :type Offset: int
        :param _Limit: 分页查询limit，默认为20
        :type Limit: int
        :param _NameFilter: 模糊匹配，精确匹配时失效
        :type NameFilter: str
        :param _NameMatched: 精确匹配
        :type NameMatched: str
        :param _Order: 按时间排序顺序，默认为DESC
        :type Order: str
        """
        self._EdgeUnitId = None
        self._Namespace = None
        self._Offset = None
        self._Limit = None
        self._NameFilter = None
        self._NameMatched = None
        self._Order = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

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
    def NameFilter(self):
        return self._NameFilter

    @NameFilter.setter
    def NameFilter(self, NameFilter):
        self._NameFilter = NameFilter

    @property
    def NameMatched(self):
        return self._NameMatched

    @NameMatched.setter
    def NameMatched(self, NameMatched):
        self._NameMatched = NameMatched

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Namespace = params.get("Namespace")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NameFilter = params.get("NameFilter")
        self._NameMatched = params.get("NameMatched")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitNodeUnitTemplatesResponse(AbstractModel):
    """DescribeEdgeUnitNodeUnitTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 符合查询条件的记录总数
        :type Total: int
        :param _NodeUnitTemplates: NodeUnit模板列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeUnitTemplates: list of NodeUnitTemplate
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._NodeUnitTemplates = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def NodeUnitTemplates(self):
        return self._NodeUnitTemplates

    @NodeUnitTemplates.setter
    def NodeUnitTemplates(self, NodeUnitTemplates):
        self._NodeUnitTemplates = NodeUnitTemplates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("NodeUnitTemplates") is not None:
            self._NodeUnitTemplates = []
            for item in params.get("NodeUnitTemplates"):
                obj = NodeUnitTemplate()
                obj._deserialize(item)
                self._NodeUnitTemplates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEdgeUnitsCloudRequest(AbstractModel):
    """DescribeEdgeUnitsCloud请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: limit值
        :type Limit: int
        :param _NamePattern: 集群名称模糊匹配
        :type NamePattern: str
        :param _Order: 排序，ASC/DESC(默认)
        :type Order: str
        """
        self._Offset = None
        self._Limit = None
        self._NamePattern = None
        self._Order = None

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
    def NamePattern(self):
        return self._NamePattern

    @NamePattern.setter
    def NamePattern(self, NamePattern):
        self._NamePattern = NamePattern

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NamePattern = params.get("NamePattern")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitsCloudResponse(AbstractModel):
    """DescribeEdgeUnitsCloud返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _EdgeUnitSet: 集群详情
注意：此字段可能返回 null，表示取不到有效值。
        :type EdgeUnitSet: list of EdgeCloudCluster
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._EdgeUnitSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EdgeUnitSet(self):
        return self._EdgeUnitSet

    @EdgeUnitSet.setter
    def EdgeUnitSet(self, EdgeUnitSet):
        self._EdgeUnitSet = EdgeUnitSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EdgeUnitSet") is not None:
            self._EdgeUnitSet = []
            for item in params.get("EdgeUnitSet"):
                obj = EdgeCloudCluster()
                obj._deserialize(item)
                self._EdgeUnitSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIotDeviceRequest(AbstractModel):
    """DescribeIotDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备id，传0值表示此参数无效
        :type DeviceId: int
        :param _ProductID: 无
        :type ProductID: str
        :param _DeviceName: 无
        :type DeviceName: str
        """
        self._DeviceId = None
        self._ProductID = None
        self._DeviceName = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ProductID = params.get("ProductID")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIotDeviceResponse(AbstractModel):
    """DescribeIotDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 设备id
        :type Id: int
        :param _Name: 设备名称
        :type Name: str
        :param _Version: 版本号
        :type Version: str
        :param _Cert: ssl证书
        :type Cert: str
        :param _PrivateKey: ssl私钥
        :type PrivateKey: str
        :param _Psk: psk认证密钥
        :type Psk: str
        :param _Disabled: 设备是否打开
        :type Disabled: bool
        :param _LogSetting: 设备日志
        :type LogSetting: int
        :param _LogLevel: 设备日志级别
        :type LogLevel: int
        :param _UserName: mqtt参数
        :type UserName: str
        :param _Password: mqtt参数
        :type Password: str
        :param _ClientID: mqtt参数
        :type ClientID: str
        :param _PskHex: 16进制的psk格式
        :type PskHex: str
        :param _Description: 描述
        :type Description: str
        :param _Status: 设备在线状态
        :type Status: int
        :param _Region: 无
        :type Region: str
        :param _UnitID: 无
        :type UnitID: int
        :param _UnitName: 无
        :type UnitName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._Name = None
        self._Version = None
        self._Cert = None
        self._PrivateKey = None
        self._Psk = None
        self._Disabled = None
        self._LogSetting = None
        self._LogLevel = None
        self._UserName = None
        self._Password = None
        self._ClientID = None
        self._PskHex = None
        self._Description = None
        self._Status = None
        self._Region = None
        self._UnitID = None
        self._UnitName = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def Psk(self):
        return self._Psk

    @Psk.setter
    def Psk(self, Psk):
        self._Psk = Psk

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def LogSetting(self):
        return self._LogSetting

    @LogSetting.setter
    def LogSetting(self, LogSetting):
        self._LogSetting = LogSetting

    @property
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ClientID(self):
        return self._ClientID

    @ClientID.setter
    def ClientID(self, ClientID):
        self._ClientID = ClientID

    @property
    def PskHex(self):
        return self._PskHex

    @PskHex.setter
    def PskHex(self, PskHex):
        self._PskHex = PskHex

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
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def UnitID(self):
        return self._UnitID

    @UnitID.setter
    def UnitID(self, UnitID):
        self._UnitID = UnitID

    @property
    def UnitName(self):
        return self._UnitName

    @UnitName.setter
    def UnitName(self, UnitName):
        self._UnitName = UnitName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Version = params.get("Version")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        self._Psk = params.get("Psk")
        self._Disabled = params.get("Disabled")
        self._LogSetting = params.get("LogSetting")
        self._LogLevel = params.get("LogLevel")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._ClientID = params.get("ClientID")
        self._PskHex = params.get("PskHex")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._UnitID = params.get("UnitID")
        self._UnitName = params.get("UnitName")
        self._RequestId = params.get("RequestId")


class DescribeIotDevicesRequest(AbstractModel):
    """DescribeIotDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页偏移
        :type Offset: int
        :param _Limit: 每页数量
        :type Limit: int
        :param _ProductId: 产品id
        :type ProductId: str
        :param _NamePattern: 设备名称模糊查找
        :type NamePattern: str
        :param _Versions: 版本列表
        :type Versions: list of str
        :param _Order: ASC 或 DESC
        :type Order: str
        """
        self._Offset = None
        self._Limit = None
        self._ProductId = None
        self._NamePattern = None
        self._Versions = None
        self._Order = None

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
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def NamePattern(self):
        return self._NamePattern

    @NamePattern.setter
    def NamePattern(self, NamePattern):
        self._NamePattern = NamePattern

    @property
    def Versions(self):
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProductId = params.get("ProductId")
        self._NamePattern = params.get("NamePattern")
        self._Versions = params.get("Versions")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIotDevicesResponse(AbstractModel):
    """DescribeIotDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查找条件的总数量
        :type TotalCount: int
        :param _DeviceSet: 设备列表
        :type DeviceSet: list of IotDevicesInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeviceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeviceSet(self):
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = IotDevicesInfo()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMessageRouteListRequest(AbstractModel):
    """DescribeMessageRouteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 无
        :type Limit: int
        :param _Offset: 无
        :type Offset: int
        :param _Filter: 无
        :type Filter: str
        :param _StartTime: 无
        :type StartTime: str
        :param _EndTime: 无
        :type EndTime: str
        :param _Order: 无
        :type Order: str
        """
        self._Limit = None
        self._Offset = None
        self._Filter = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None

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
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Filter = params.get("Filter")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMessageRouteListResponse(AbstractModel):
    """DescribeMessageRouteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteList: 无
        :type RouteList: list of RouteInfo
        :param _TotalCount: 无
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RouteList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RouteList(self):
        return self._RouteList

    @RouteList.setter
    def RouteList(self, RouteList):
        self._RouteList = RouteList

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


    def _deserialize(self, params):
        if params.get("RouteList") is not None:
            self._RouteList = []
            for item in params.get("RouteList"):
                obj = RouteInfo()
                obj._deserialize(item)
                self._RouteList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMonitorMetricsRequest(AbstractModel):
    """DescribeMonitorMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _QueryType: 查询维度
        :type QueryType: str
        :param _StartTime: 起始时间Unix秒时间戳
        :type StartTime: int
        :param _EndTime: 终止时间Unix秒时间戳
        :type EndTime: int
        :param _Interval: 步长（分钟）
        :type Interval: int
        :param _NodeName: 节点名称，查询节点监控时必填
        :type NodeName: str
        :param _Namespace: 命名空间，不填则默认为default
        :type Namespace: str
        :param _PodName: Pod名称，查询Pod监控时必填
        :type PodName: str
        :param _WorkloadName: Workload名称，查询Workload监控时必填
        :type WorkloadName: str
        """
        self._EdgeUnitId = None
        self._QueryType = None
        self._StartTime = None
        self._EndTime = None
        self._Interval = None
        self._NodeName = None
        self._Namespace = None
        self._PodName = None
        self._WorkloadName = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def QueryType(self):
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

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
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def WorkloadName(self):
        return self._WorkloadName

    @WorkloadName.setter
    def WorkloadName(self, WorkloadName):
        self._WorkloadName = WorkloadName


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._QueryType = params.get("QueryType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Interval = params.get("Interval")
        self._NodeName = params.get("NodeName")
        self._Namespace = params.get("Namespace")
        self._PodName = params.get("PodName")
        self._WorkloadName = params.get("WorkloadName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonitorMetricsResponse(AbstractModel):
    """DescribeMonitorMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Metrics: 查询监控指标结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Metrics: list of MonitorMetricsColumn
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Metrics = None
        self._RequestId = None

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = MonitorMetricsColumn()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNamespaceRequest(AbstractModel):
    """DescribeNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _Namespace: 命名空间名
        :type Namespace: str
        """
        self._EdgeUnitID = None
        self._Namespace = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespaceResourcesRequest(AbstractModel):
    """DescribeNamespaceResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _Namespace: 命名空间
        :type Namespace: str
        """
        self._EdgeUnitID = None
        self._Namespace = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespaceResourcesResponse(AbstractModel):
    """DescribeNamespaceResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Resources: 资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: list of NamespaceResource
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Resources = None
        self._RequestId = None

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = NamespaceResource()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNamespaceResponse(AbstractModel):
    """DescribeNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间名
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _Status: 状态 (Active|Terminating)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Protected: 是否保护-不允许删除
注意：此字段可能返回 null，表示取不到有效值。
        :type Protected: bool
        :param _Yaml: Yaml文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Namespace = None
        self._Status = None
        self._Description = None
        self._CreateTime = None
        self._Protected = None
        self._Yaml = None
        self._RequestId = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Protected(self):
        return self._Protected

    @Protected.setter
    def Protected(self, Protected):
        self._Protected = Protected

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._Protected = params.get("Protected")
        self._Yaml = params.get("Yaml")
        self._RequestId = params.get("RequestId")


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: IECP边缘单元ID
        :type EdgeUnitID: int
        :param _NamePattern: 边缘节点名称模糊搜索串
        :type NamePattern: str
        """
        self._EdgeUnitID = None
        self._NamePattern = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def NamePattern(self):
        return self._NamePattern

    @NamePattern.setter
    def NamePattern(self, NamePattern):
        self._NamePattern = NamePattern


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._NamePattern = params.get("NamePattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 命名空间信息列表
        :type Items: list of NamespaceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = NamespaceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNodeUnitRequest(AbstractModel):
    """DescribeNodeUnit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 边缘单元ID
        :type EdgeUnitId: int
        :param _NodeGroupName: NodeUnit所属的NodeGroup名称
        :type NodeGroupName: str
        :param _Namespace: 命名空间，默认default
        :type Namespace: str
        :param _Limit: 分页查询limit，默认20
        :type Limit: int
        :param _Offset: 分页查询offset，默认0
        :type Offset: int
        :param _NameFilter: 模糊匹配
        :type NameFilter: str
        """
        self._EdgeUnitId = None
        self._NodeGroupName = None
        self._Namespace = None
        self._Limit = None
        self._Offset = None
        self._NameFilter = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeGroupName(self):
        return self._NodeGroupName

    @NodeGroupName.setter
    def NodeGroupName(self, NodeGroupName):
        self._NodeGroupName = NodeGroupName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

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
    def NameFilter(self):
        return self._NameFilter

    @NameFilter.setter
    def NameFilter(self, NameFilter):
        self._NameFilter = NameFilter


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeGroupName = params.get("NodeGroupName")
        self._Namespace = params.get("Namespace")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._NameFilter = params.get("NameFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNodeUnitResponse(AbstractModel):
    """DescribeNodeUnit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的记录总数
        :type TotalCount: int
        :param _NodeGridInfo: NodeUnit信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeGridInfo: list of NodeUnitInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NodeGridInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeGridInfo(self):
        return self._NodeGridInfo

    @NodeGridInfo.setter
    def NodeGridInfo(self, NodeGridInfo):
        self._NodeGridInfo = NodeGridInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NodeGridInfo") is not None:
            self._NodeGridInfo = []
            for item in params.get("NodeGridInfo"):
                obj = NodeUnitInfo()
                obj._deserialize(item)
                self._NodeGridInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNodeUnitTemplateOnNodeGroupRequest(AbstractModel):
    """DescribeNodeUnitTemplateOnNodeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NodeGroupName: NodeGroup名称
        :type NodeGroupName: str
        :param _Namespace: 命名空间，默认default
        :type Namespace: str
        :param _NodeUnitNamePattern: 名称模糊匹配
        :type NodeUnitNamePattern: str
        :param _Offset: 分页查询offset，默认0
        :type Offset: int
        :param _Limit: 分页查询limit，默认20
        :type Limit: int
        :param _Order: 排序，默认DESC
        :type Order: str
        """
        self._EdgeUnitId = None
        self._NodeGroupName = None
        self._Namespace = None
        self._NodeUnitNamePattern = None
        self._Offset = None
        self._Limit = None
        self._Order = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeGroupName(self):
        return self._NodeGroupName

    @NodeGroupName.setter
    def NodeGroupName(self, NodeGroupName):
        self._NodeGroupName = NodeGroupName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def NodeUnitNamePattern(self):
        return self._NodeUnitNamePattern

    @NodeUnitNamePattern.setter
    def NodeUnitNamePattern(self, NodeUnitNamePattern):
        self._NodeUnitNamePattern = NodeUnitNamePattern

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeGroupName = params.get("NodeGroupName")
        self._Namespace = params.get("Namespace")
        self._NodeUnitNamePattern = params.get("NodeUnitNamePattern")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNodeUnitTemplateOnNodeGroupResponse(AbstractModel):
    """DescribeNodeUnitTemplateOnNodeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 记录总数
        :type Total: int
        :param _NodeUnitTemplates: NodeUnit模板
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeUnitTemplates: list of NodeGroupNodeUnitTemplateInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._NodeUnitTemplates = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def NodeUnitTemplates(self):
        return self._NodeUnitTemplates

    @NodeUnitTemplates.setter
    def NodeUnitTemplates(self, NodeUnitTemplates):
        self._NodeUnitTemplates = NodeUnitTemplates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("NodeUnitTemplates") is not None:
            self._NodeUnitTemplates = []
            for item in params.get("NodeUnitTemplates"):
                obj = NodeGroupNodeUnitTemplateInfo()
                obj._deserialize(item)
                self._NodeUnitTemplates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecretRequest(AbstractModel):
    """DescribeSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 边缘单元ID
        :type EdgeUnitID: int
        :param _SecretName: secret名
        :type SecretName: str
        :param _SecretNamespace: 命名空间(默认值:default）
        :type SecretNamespace: str
        """
        self._EdgeUnitID = None
        self._SecretName = None
        self._SecretNamespace = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def SecretNamespace(self):
        return self._SecretNamespace

    @SecretNamespace.setter
    def SecretNamespace(self, SecretNamespace):
        self._SecretNamespace = SecretNamespace


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._SecretName = params.get("SecretName")
        self._SecretNamespace = params.get("SecretNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecretResponse(AbstractModel):
    """DescribeSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: Secret名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Yaml: secret的yaml格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param _Json: secret的json格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Json: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Namespace = None
        self._CreateTime = None
        self._Yaml = None
        self._Json = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def Json(self):
        return self._Json

    @Json.setter
    def Json(self, Json):
        self._Json = Json

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._CreateTime = params.get("CreateTime")
        self._Yaml = params.get("Yaml")
        self._Json = params.get("Json")
        self._RequestId = params.get("RequestId")


class DescribeSecretYamlErrorRequest(AbstractModel):
    """DescribeSecretYamlError请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Yaml: yaml文件
        :type Yaml: str
        """
        self._Yaml = None

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecretYamlErrorResponse(AbstractModel):
    """DescribeSecretYamlError返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckPass: 校验是通过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPass: bool
        :param _ErrType: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrType: int
        :param _ErrInfo: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrInfo: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckPass = None
        self._ErrType = None
        self._ErrInfo = None
        self._RequestId = None

    @property
    def CheckPass(self):
        return self._CheckPass

    @CheckPass.setter
    def CheckPass(self, CheckPass):
        self._CheckPass = CheckPass

    @property
    def ErrType(self):
        return self._ErrType

    @ErrType.setter
    def ErrType(self, ErrType):
        self._ErrType = ErrType

    @property
    def ErrInfo(self):
        return self._ErrInfo

    @ErrInfo.setter
    def ErrInfo(self, ErrInfo):
        self._ErrInfo = ErrInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CheckPass = params.get("CheckPass")
        self._ErrType = params.get("ErrType")
        self._ErrInfo = params.get("ErrInfo")
        self._RequestId = params.get("RequestId")


class DescribeSecretsRequest(AbstractModel):
    """DescribeSecrets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 边缘单元ID
        :type EdgeUnitID: int
        :param _Offset: 页号
        :type Offset: int
        :param _Limit: 每页数目
        :type Limit: int
        :param _SecretNamespace: 命名空间
        :type SecretNamespace: str
        :param _NamePattern: Secret名(模糊匹配)
        :type NamePattern: str
        :param _Sort: Sort.Field:CreateTime Sort.Order:ASC|DESC
        :type Sort: :class:`tencentcloud.iecp.v20210914.models.FieldSort`
        :param _SecretType: Secret类型(DockerConfigJson或Opaque)
        :type SecretType: str
        """
        self._EdgeUnitID = None
        self._Offset = None
        self._Limit = None
        self._SecretNamespace = None
        self._NamePattern = None
        self._Sort = None
        self._SecretType = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

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
    def SecretNamespace(self):
        return self._SecretNamespace

    @SecretNamespace.setter
    def SecretNamespace(self, SecretNamespace):
        self._SecretNamespace = SecretNamespace

    @property
    def NamePattern(self):
        return self._NamePattern

    @NamePattern.setter
    def NamePattern(self, NamePattern):
        self._NamePattern = NamePattern

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SecretType(self):
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SecretNamespace = params.get("SecretNamespace")
        self._NamePattern = params.get("NamePattern")
        if params.get("Sort") is not None:
            self._Sort = FieldSort()
            self._Sort._deserialize(params.get("Sort"))
        self._SecretType = params.get("SecretType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecretsResponse(AbstractModel):
    """DescribeSecrets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Items: Secret列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of SecretItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SecretItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeYeheResourceLimitRequest(AbstractModel):
    """DescribeYeheResourceLimit请求参数结构体

    """


class DescribeYeheResourceLimitResponse(AbstractModel):
    """DescribeYeheResourceLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Uin: 用户父账号
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _CreateNodeLimit: 允许创建的节点数
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateNodeLimit: int
        :param _CreateClusterLimit: 允许创建的集群数
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateClusterLimit: int
        :param _EnablePermMonitor: 是否有监控开启权限
注意：此字段可能返回 null，表示取不到有效值。
        :type EnablePermMonitor: bool
        :param _EnablePermAdminNode: 节点是否有admin的所有权限
注意：此字段可能返回 null，表示取不到有效值。
        :type EnablePermAdminNode: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Uin = None
        self._CreateNodeLimit = None
        self._CreateClusterLimit = None
        self._EnablePermMonitor = None
        self._EnablePermAdminNode = None
        self._RequestId = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def CreateNodeLimit(self):
        return self._CreateNodeLimit

    @CreateNodeLimit.setter
    def CreateNodeLimit(self, CreateNodeLimit):
        self._CreateNodeLimit = CreateNodeLimit

    @property
    def CreateClusterLimit(self):
        return self._CreateClusterLimit

    @CreateClusterLimit.setter
    def CreateClusterLimit(self, CreateClusterLimit):
        self._CreateClusterLimit = CreateClusterLimit

    @property
    def EnablePermMonitor(self):
        return self._EnablePermMonitor

    @EnablePermMonitor.setter
    def EnablePermMonitor(self, EnablePermMonitor):
        self._EnablePermMonitor = EnablePermMonitor

    @property
    def EnablePermAdminNode(self):
        return self._EnablePermAdminNode

    @EnablePermAdminNode.setter
    def EnablePermAdminNode(self, EnablePermAdminNode):
        self._EnablePermAdminNode = EnablePermAdminNode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._CreateNodeLimit = params.get("CreateNodeLimit")
        self._CreateClusterLimit = params.get("CreateClusterLimit")
        self._EnablePermMonitor = params.get("EnablePermMonitor")
        self._EnablePermAdminNode = params.get("EnablePermAdminNode")
        self._RequestId = params.get("RequestId")


class DockerConfig(AbstractModel):
    """docker配置

    """

    def __init__(self):
        r"""
        :param _RegistryDomain: 镜像仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryDomain: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Password: 密码
        :type Password: str
        """
        self._RegistryDomain = None
        self._UserName = None
        self._Password = None

    @property
    def RegistryDomain(self):
        return self._RegistryDomain

    @RegistryDomain.setter
    def RegistryDomain(self, RegistryDomain):
        self._RegistryDomain = RegistryDomain

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._RegistryDomain = params.get("RegistryDomain")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DracoNodeInfo(AbstractModel):
    """Draco 设备预录入信息

    """

    def __init__(self):
        r"""
        :param _SN: 设备SN。SN仅支持大写字母、数字，长度限制为1~32个字符
        :type SN: str
        :param _Name: 节点名称。长度限制为1~63个字符，节点名称只支持小写英文、数字、中横线、英文句号
        :type Name: str
        :param _Remark: 节点备注
        :type Remark: str
        """
        self._SN = None
        self._Name = None
        self._Remark = None

    @property
    def SN(self):
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._SN = params.get("SN")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeCloudCluster(AbstractModel):
    """获取边缘集群列表

    """

    def __init__(self):
        r"""
        :param _EdgeId: IECP侧边缘集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EdgeId: int
        :param _ClusterId: 边缘集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _Region: 区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _K8SVersion: 集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :type K8SVersion: str
        :param _VpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _ClusterDesc: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterDesc: str
        :param _Status: 集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _PodCIDR: pod cidr
注意：此字段可能返回 null，表示取不到有效值。
        :type PodCIDR: str
        :param _ServiceCIDR: service cidr
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCIDR: str
        :param _EdgeClusterVersion: 边缘版本类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EdgeClusterVersion: str
        :param _UID: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UID: str
        """
        self._EdgeId = None
        self._ClusterId = None
        self._Region = None
        self._ClusterName = None
        self._K8SVersion = None
        self._VpcId = None
        self._ClusterDesc = None
        self._Status = None
        self._CreateTime = None
        self._PodCIDR = None
        self._ServiceCIDR = None
        self._EdgeClusterVersion = None
        self._UID = None

    @property
    def EdgeId(self):
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def K8SVersion(self):
        return self._K8SVersion

    @K8SVersion.setter
    def K8SVersion(self, K8SVersion):
        self._K8SVersion = K8SVersion

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ClusterDesc(self):
        return self._ClusterDesc

    @ClusterDesc.setter
    def ClusterDesc(self, ClusterDesc):
        self._ClusterDesc = ClusterDesc

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
    def PodCIDR(self):
        return self._PodCIDR

    @PodCIDR.setter
    def PodCIDR(self, PodCIDR):
        self._PodCIDR = PodCIDR

    @property
    def ServiceCIDR(self):
        return self._ServiceCIDR

    @ServiceCIDR.setter
    def ServiceCIDR(self, ServiceCIDR):
        self._ServiceCIDR = ServiceCIDR

    @property
    def EdgeClusterVersion(self):
        return self._EdgeClusterVersion

    @EdgeClusterVersion.setter
    def EdgeClusterVersion(self, EdgeClusterVersion):
        self._EdgeClusterVersion = EdgeClusterVersion

    @property
    def UID(self):
        return self._UID

    @UID.setter
    def UID(self, UID):
        self._UID = UID


    def _deserialize(self, params):
        self._EdgeId = params.get("EdgeId")
        self._ClusterId = params.get("ClusterId")
        self._Region = params.get("Region")
        self._ClusterName = params.get("ClusterName")
        self._K8SVersion = params.get("K8SVersion")
        self._VpcId = params.get("VpcId")
        self._ClusterDesc = params.get("ClusterDesc")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._PodCIDR = params.get("PodCIDR")
        self._ServiceCIDR = params.get("ServiceCIDR")
        self._EdgeClusterVersion = params.get("EdgeClusterVersion")
        self._UID = params.get("UID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeDracoNodeInfo(AbstractModel):
    """预注册节点的信息

    """

    def __init__(self):
        r"""
        :param _Id: 节点ID
        :type Id: int
        :param _Name: 节点名称
        :type Name: str
        :param _IsUsed: 是否已激活
        :type IsUsed: bool
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Remark: 备注信息，如批次
        :type Remark: str
        :param _SN: SN 设备号
        :type SN: str
        """
        self._Id = None
        self._Name = None
        self._IsUsed = None
        self._CreateTime = None
        self._Remark = None
        self._SN = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsUsed(self):
        return self._IsUsed

    @IsUsed.setter
    def IsUsed(self, IsUsed):
        self._IsUsed = IsUsed

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SN(self):
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._IsUsed = params.get("IsUsed")
        self._CreateTime = params.get("CreateTime")
        self._Remark = params.get("Remark")
        self._SN = params.get("SN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodeInfo(AbstractModel):
    """边缘节点信息

    """

    def __init__(self):
        r"""
        :param _Id: IECP边缘节点ID
        :type Id: int
        :param _Name: 节点名称
        :type Name: str
        :param _Status: 节点状态 （1健康｜2异常｜3离线｜4未激活）
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Resource: 节点资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: :class:`tencentcloud.iecp.v20210914.models.EdgeNodeResourceInfo`
        :param _CpuArchitecture: CPU体系结构
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuArchitecture: str
        :param _Ip: IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _OperatingSystem: 操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatingSystem: str
        :param _NodeUnits: 节点所属的NodeUnit
key：NodeUnit模版ID，Value：NodeUnit模版名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeUnits: :class:`tencentcloud.iecp.v20210914.models.KeyValueObj`
        """
        self._Id = None
        self._Name = None
        self._Status = None
        self._CreateTime = None
        self._Resource = None
        self._CpuArchitecture = None
        self._Ip = None
        self._OperatingSystem = None
        self._NodeUnits = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def CpuArchitecture(self):
        return self._CpuArchitecture

    @CpuArchitecture.setter
    def CpuArchitecture(self, CpuArchitecture):
        self._CpuArchitecture = CpuArchitecture

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def OperatingSystem(self):
        return self._OperatingSystem

    @OperatingSystem.setter
    def OperatingSystem(self, OperatingSystem):
        self._OperatingSystem = OperatingSystem

    @property
    def NodeUnits(self):
        return self._NodeUnits

    @NodeUnits.setter
    def NodeUnits(self, NodeUnits):
        self._NodeUnits = NodeUnits


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        if params.get("Resource") is not None:
            self._Resource = EdgeNodeResourceInfo()
            self._Resource._deserialize(params.get("Resource"))
        self._CpuArchitecture = params.get("CpuArchitecture")
        self._Ip = params.get("Ip")
        self._OperatingSystem = params.get("OperatingSystem")
        if params.get("NodeUnits") is not None:
            self._NodeUnits = KeyValueObj()
            self._NodeUnits._deserialize(params.get("NodeUnits"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodeInstallerOnline(AbstractModel):
    """节点在线安装信息

    """

    def __init__(self):
        r"""
        :param _ScriptName: 节点安装脚本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptName: str
        :param _ScriptDownloadUrl: 节点安装脚本下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptDownloadUrl: str
        :param _Guide: 节点安装命令
注意：此字段可能返回 null，表示取不到有效值。
        :type Guide: str
        """
        self._ScriptName = None
        self._ScriptDownloadUrl = None
        self._Guide = None

    @property
    def ScriptName(self):
        return self._ScriptName

    @ScriptName.setter
    def ScriptName(self, ScriptName):
        self._ScriptName = ScriptName

    @property
    def ScriptDownloadUrl(self):
        return self._ScriptDownloadUrl

    @ScriptDownloadUrl.setter
    def ScriptDownloadUrl(self, ScriptDownloadUrl):
        self._ScriptDownloadUrl = ScriptDownloadUrl

    @property
    def Guide(self):
        return self._Guide

    @Guide.setter
    def Guide(self, Guide):
        self._Guide = Guide


    def _deserialize(self, params):
        self._ScriptName = params.get("ScriptName")
        self._ScriptDownloadUrl = params.get("ScriptDownloadUrl")
        self._Guide = params.get("Guide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodeLabel(AbstractModel):
    """边缘节点标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Protected: 是否受保护
        :type Protected: bool
        """
        self._Key = None
        self._Value = None
        self._Protected = None

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
    def Protected(self):
        return self._Protected

    @Protected.setter
    def Protected(self, Protected):
        self._Protected = Protected


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Protected = params.get("Protected")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodePodContainerInfo(AbstractModel):
    """边缘节点Pod容器信息

    """

    def __init__(self):
        r"""
        :param _Name: Pod名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Id: 容器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Image: 镜像（含版本号）
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param _CpuRequest: CPU Request
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuRequest: str
        :param _CpuLimit: CPU Limit
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuLimit: str
        :param _MemoryRequest: Memory Request
注意：此字段可能返回 null，表示取不到有效值。
        :type MemoryRequest: str
        :param _MemoryLimit: Memory Limit
注意：此字段可能返回 null，表示取不到有效值。
        :type MemoryLimit: str
        :param _RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param _Status: 容器状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._Name = None
        self._Id = None
        self._Image = None
        self._CpuRequest = None
        self._CpuLimit = None
        self._MemoryRequest = None
        self._MemoryLimit = None
        self._RestartCount = None
        self._Status = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def CpuRequest(self):
        return self._CpuRequest

    @CpuRequest.setter
    def CpuRequest(self, CpuRequest):
        self._CpuRequest = CpuRequest

    @property
    def CpuLimit(self):
        return self._CpuLimit

    @CpuLimit.setter
    def CpuLimit(self, CpuLimit):
        self._CpuLimit = CpuLimit

    @property
    def MemoryRequest(self):
        return self._MemoryRequest

    @MemoryRequest.setter
    def MemoryRequest(self, MemoryRequest):
        self._MemoryRequest = MemoryRequest

    @property
    def MemoryLimit(self):
        return self._MemoryLimit

    @MemoryLimit.setter
    def MemoryLimit(self, MemoryLimit):
        self._MemoryLimit = MemoryLimit

    @property
    def RestartCount(self):
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Image = params.get("Image")
        self._CpuRequest = params.get("CpuRequest")
        self._CpuLimit = params.get("CpuLimit")
        self._MemoryRequest = params.get("MemoryRequest")
        self._MemoryLimit = params.get("MemoryLimit")
        self._RestartCount = params.get("RestartCount")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodePodInfo(AbstractModel):
    """边缘节点Pod信息

    """

    def __init__(self):
        r"""
        :param _Name: Pod名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Status: Pod状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _NodeIp: 所在节点IP
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeIp: str
        :param _Ip: 实例IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _CpuRequest: CPU Request
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuRequest: str
        :param _MemoryRequest: Memory Request
注意：此字段可能返回 null，表示取不到有效值。
        :type MemoryRequest: str
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _WorkloadType: 工作负载类型
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadType: str
        :param _WorkloadName: 工作负载名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadName: str
        :param _StartTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param _ClusterID: 集群ID
        :type ClusterID: str
        """
        self._Name = None
        self._Status = None
        self._NodeIp = None
        self._Ip = None
        self._CpuRequest = None
        self._MemoryRequest = None
        self._Namespace = None
        self._WorkloadType = None
        self._WorkloadName = None
        self._StartTime = None
        self._RestartCount = None
        self._ClusterID = None

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
    def NodeIp(self):
        return self._NodeIp

    @NodeIp.setter
    def NodeIp(self, NodeIp):
        self._NodeIp = NodeIp

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def CpuRequest(self):
        return self._CpuRequest

    @CpuRequest.setter
    def CpuRequest(self, CpuRequest):
        self._CpuRequest = CpuRequest

    @property
    def MemoryRequest(self):
        return self._MemoryRequest

    @MemoryRequest.setter
    def MemoryRequest(self, MemoryRequest):
        self._MemoryRequest = MemoryRequest

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def WorkloadType(self):
        return self._WorkloadType

    @WorkloadType.setter
    def WorkloadType(self, WorkloadType):
        self._WorkloadType = WorkloadType

    @property
    def WorkloadName(self):
        return self._WorkloadName

    @WorkloadName.setter
    def WorkloadName(self, WorkloadName):
        self._WorkloadName = WorkloadName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def RestartCount(self):
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._NodeIp = params.get("NodeIp")
        self._Ip = params.get("Ip")
        self._CpuRequest = params.get("CpuRequest")
        self._MemoryRequest = params.get("MemoryRequest")
        self._Namespace = params.get("Namespace")
        self._WorkloadType = params.get("WorkloadType")
        self._WorkloadName = params.get("WorkloadName")
        self._StartTime = params.get("StartTime")
        self._RestartCount = params.get("RestartCount")
        self._ClusterID = params.get("ClusterID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodeResourceInfo(AbstractModel):
    """边缘节点资源信息

    """

    def __init__(self):
        r"""
        :param _AllocatedCPU: 可使用的CPU 单位: m核
注意：此字段可能返回 null，表示取不到有效值。
        :type AllocatedCPU: str
        :param _TotalCPU: CPU总量 单位:m核
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCPU: str
        :param _AllocatedMemory: 已分配的内存 单位G
注意：此字段可能返回 null，表示取不到有效值。
        :type AllocatedMemory: str
        :param _TotalMemory: 内存总量 单位G
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalMemory: str
        :param _AllocatedGPU: 已分配的GPU资源
注意：此字段可能返回 null，表示取不到有效值。
        :type AllocatedGPU: str
        :param _TotalGPU: GPU总量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalGPU: str
        :param _AvailableCPU: 可使用的CPU 单位: m核
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableCPU: str
        :param _AvailableMemory: 可使用的内存 单位: G
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableMemory: str
        :param _AvailableGPU: 可使用的GPU资源
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableGPU: str
        """
        self._AllocatedCPU = None
        self._TotalCPU = None
        self._AllocatedMemory = None
        self._TotalMemory = None
        self._AllocatedGPU = None
        self._TotalGPU = None
        self._AvailableCPU = None
        self._AvailableMemory = None
        self._AvailableGPU = None

    @property
    def AllocatedCPU(self):
        return self._AllocatedCPU

    @AllocatedCPU.setter
    def AllocatedCPU(self, AllocatedCPU):
        self._AllocatedCPU = AllocatedCPU

    @property
    def TotalCPU(self):
        return self._TotalCPU

    @TotalCPU.setter
    def TotalCPU(self, TotalCPU):
        self._TotalCPU = TotalCPU

    @property
    def AllocatedMemory(self):
        return self._AllocatedMemory

    @AllocatedMemory.setter
    def AllocatedMemory(self, AllocatedMemory):
        self._AllocatedMemory = AllocatedMemory

    @property
    def TotalMemory(self):
        return self._TotalMemory

    @TotalMemory.setter
    def TotalMemory(self, TotalMemory):
        self._TotalMemory = TotalMemory

    @property
    def AllocatedGPU(self):
        return self._AllocatedGPU

    @AllocatedGPU.setter
    def AllocatedGPU(self, AllocatedGPU):
        self._AllocatedGPU = AllocatedGPU

    @property
    def TotalGPU(self):
        return self._TotalGPU

    @TotalGPU.setter
    def TotalGPU(self, TotalGPU):
        self._TotalGPU = TotalGPU

    @property
    def AvailableCPU(self):
        return self._AvailableCPU

    @AvailableCPU.setter
    def AvailableCPU(self, AvailableCPU):
        self._AvailableCPU = AvailableCPU

    @property
    def AvailableMemory(self):
        return self._AvailableMemory

    @AvailableMemory.setter
    def AvailableMemory(self, AvailableMemory):
        self._AvailableMemory = AvailableMemory

    @property
    def AvailableGPU(self):
        return self._AvailableGPU

    @AvailableGPU.setter
    def AvailableGPU(self, AvailableGPU):
        self._AvailableGPU = AvailableGPU


    def _deserialize(self, params):
        self._AllocatedCPU = params.get("AllocatedCPU")
        self._TotalCPU = params.get("TotalCPU")
        self._AllocatedMemory = params.get("AllocatedMemory")
        self._TotalMemory = params.get("TotalMemory")
        self._AllocatedGPU = params.get("AllocatedGPU")
        self._TotalGPU = params.get("TotalGPU")
        self._AvailableCPU = params.get("AvailableCPU")
        self._AvailableMemory = params.get("AvailableMemory")
        self._AvailableGPU = params.get("AvailableGPU")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeUnitStatisticItem(AbstractModel):
    """单元内的统计信息

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Online: 在线数
注意：此字段可能返回 null，表示取不到有效值。
        :type Online: int
        :param _Abnormal: 异常数
注意：此字段可能返回 null，表示取不到有效值。
        :type Abnormal: int
        :param _Offline: 离线数
注意：此字段可能返回 null，表示取不到有效值。
        :type Offline: int
        :param _NotActive: 未激活
注意：此字段可能返回 null，表示取不到有效值。
        :type NotActive: int
        """
        self._Total = None
        self._Online = None
        self._Abnormal = None
        self._Offline = None
        self._NotActive = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def Abnormal(self):
        return self._Abnormal

    @Abnormal.setter
    def Abnormal(self, Abnormal):
        self._Abnormal = Abnormal

    @property
    def Offline(self):
        return self._Offline

    @Offline.setter
    def Offline(self, Offline):
        self._Offline = Offline

    @property
    def NotActive(self):
        return self._NotActive

    @NotActive.setter
    def NotActive(self, NotActive):
        self._NotActive = NotActive


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Online = params.get("Online")
        self._Abnormal = params.get("Abnormal")
        self._Offline = params.get("Offline")
        self._NotActive = params.get("NotActive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Env(AbstractModel):
    """环境变量

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Value: 值
        :type Value: str
        :param _ValueFrom: 值引用
        :type ValueFrom: :class:`tencentcloud.iecp.v20210914.models.EnvValueSelector`
        """
        self._Name = None
        self._Value = None
        self._ValueFrom = None

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

    @property
    def ValueFrom(self):
        return self._ValueFrom

    @ValueFrom.setter
    def ValueFrom(self, ValueFrom):
        self._ValueFrom = ValueFrom


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("ValueFrom") is not None:
            self._ValueFrom = EnvValueSelector()
            self._ValueFrom._deserialize(params.get("ValueFrom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvValueSelector(AbstractModel):
    """环境变量选择

    """

    def __init__(self):
        r"""
        :param _Key: 健名
        :type Key: str
        :param _ObjectName: 对象名
        :type ObjectName: str
        :param _ObjectType: 对象值
        :type ObjectType: str
        """
        self._Key = None
        self._ObjectName = None
        self._ObjectType = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def ObjectName(self):
        return self._ObjectName

    @ObjectName.setter
    def ObjectName(self, ObjectName):
        self._ObjectName = ObjectName

    @property
    def ObjectType(self):
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._ObjectName = params.get("ObjectName")
        self._ObjectType = params.get("ObjectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Event(AbstractModel):
    """事件信息

    """

    def __init__(self):
        r"""
        :param _FirstTime: 第一次出现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstTime: str
        :param _LastTime: 最后一次出现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTime: str
        :param _InvolvedObjectKind: 事件关联对象类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InvolvedObjectKind: str
        :param _InvolvedObjectName: 事件关联对象名
注意：此字段可能返回 null，表示取不到有效值。
        :type InvolvedObjectName: str
        :param _Type: 事件类型(Normal|Warning)
        :type Type: str
        :param _Reason: 原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param _Message: 内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Count: 出现次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self._FirstTime = None
        self._LastTime = None
        self._InvolvedObjectKind = None
        self._InvolvedObjectName = None
        self._Type = None
        self._Reason = None
        self._Message = None
        self._Count = None

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def LastTime(self):
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def InvolvedObjectKind(self):
        return self._InvolvedObjectKind

    @InvolvedObjectKind.setter
    def InvolvedObjectKind(self, InvolvedObjectKind):
        self._InvolvedObjectKind = InvolvedObjectKind

    @property
    def InvolvedObjectName(self):
        return self._InvolvedObjectName

    @InvolvedObjectName.setter
    def InvolvedObjectName(self, InvolvedObjectName):
        self._InvolvedObjectName = InvolvedObjectName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._FirstTime = params.get("FirstTime")
        self._LastTime = params.get("LastTime")
        self._InvolvedObjectKind = params.get("InvolvedObjectKind")
        self._InvolvedObjectName = params.get("InvolvedObjectName")
        self._Type = params.get("Type")
        self._Reason = params.get("Reason")
        self._Message = params.get("Message")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FieldSort(AbstractModel):
    """字段排序

    """

    def __init__(self):
        r"""
        :param _Field: 字段名
        :type Field: str
        :param _Order: 排序(ASC:升序 DESC:降序
        :type Order: str
        """
        self._Field = None
        self._Order = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMarketComponentListRequest(AbstractModel):
    """GetMarketComponentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页偏移，从0开始
        :type Offset: int
        :param _Limit: 每页条数
        :type Limit: int
        :param _Filter: 名称模糊筛选
        :type Filter: str
        :param _Order: 以名称排序，ASC、DESC
        :type Order: str
        """
        self._Offset = None
        self._Limit = None
        self._Filter = None
        self._Order = None

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
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Filter = params.get("Filter")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMarketComponentListResponse(AbstractModel):
    """GetMarketComponentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ComponentList: 组件列表
        :type ComponentList: list of MarketComponentInfo
        :param _TotalCount: 组件总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ComponentList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ComponentList(self):
        return self._ComponentList

    @ComponentList.setter
    def ComponentList(self, ComponentList):
        self._ComponentList = ComponentList

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


    def _deserialize(self, params):
        if params.get("ComponentList") is not None:
            self._ComponentList = []
            for item in params.get("ComponentList"):
                obj = MarketComponentInfo()
                obj._deserialize(item)
                self._ComponentList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GetMarketComponentRequest(AbstractModel):
    """GetMarketComponent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 组件ID
        :type ID: int
        """
        self._ID = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMarketComponentResponse(AbstractModel):
    """GetMarketComponent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 组件ID
        :type ID: int
        :param _AppName: 组件名称
        :type AppName: str
        :param _Author: 发行组织
        :type Author: str
        :param _ReleaseTime: 发布时间
        :type ReleaseTime: str
        :param _Outline: 组件简介
        :type Outline: str
        :param _Detail: 详细介绍链接
        :type Detail: str
        :param _Icon: 图标连接
        :type Icon: str
        :param _Version: 组件版本
        :type Version: str
        :param _WorkloadVisualConfig: 组件可视化配置
        :type WorkloadVisualConfig: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ID = None
        self._AppName = None
        self._Author = None
        self._ReleaseTime = None
        self._Outline = None
        self._Detail = None
        self._Icon = None
        self._Version = None
        self._WorkloadVisualConfig = None
        self._RequestId = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def Author(self):
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def ReleaseTime(self):
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def Outline(self):
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Icon(self):
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def WorkloadVisualConfig(self):
        return self._WorkloadVisualConfig

    @WorkloadVisualConfig.setter
    def WorkloadVisualConfig(self, WorkloadVisualConfig):
        self._WorkloadVisualConfig = WorkloadVisualConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._AppName = params.get("AppName")
        self._Author = params.get("Author")
        self._ReleaseTime = params.get("ReleaseTime")
        self._Outline = params.get("Outline")
        self._Detail = params.get("Detail")
        self._Icon = params.get("Icon")
        self._Version = params.get("Version")
        self._WorkloadVisualConfig = params.get("WorkloadVisualConfig")
        self._RequestId = params.get("RequestId")


class GridDetail(AbstractModel):
    """ServiceGroup中Grid信息

    """

    def __init__(self):
        r"""
        :param _Name: Grid名称
        :type Name: str
        :param _Id: GridID
        :type Id: int
        """
        self._Name = None
        self._Id = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GridEventInfo(AbstractModel):
    """Grid事件信息

    """

    def __init__(self):
        r"""
        :param _FirstTime: 首次出现时间
        :type FirstTime: str
        :param _LastTime: 最后出现时间
        :type LastTime: str
        :param _InvolvedObjectKind: 对象类型
        :type InvolvedObjectKind: str
        :param _InvolvedObjectName: 对象名称
        :type InvolvedObjectName: str
        :param _Type: 事件类型(Normal,Warning)
        :type Type: str
        :param _Reason: 事件原因
        :type Reason: str
        :param _Message: 事件内容
        :type Message: str
        :param _Count: 次数
        :type Count: int
        :param _NodeName: 节点名（Pod事件类型时有值）
        :type NodeName: str
        :param _IP: 节点内部IP（Pod事件类型时有值）
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        """
        self._FirstTime = None
        self._LastTime = None
        self._InvolvedObjectKind = None
        self._InvolvedObjectName = None
        self._Type = None
        self._Reason = None
        self._Message = None
        self._Count = None
        self._NodeName = None
        self._IP = None

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def LastTime(self):
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def InvolvedObjectKind(self):
        return self._InvolvedObjectKind

    @InvolvedObjectKind.setter
    def InvolvedObjectKind(self, InvolvedObjectKind):
        self._InvolvedObjectKind = InvolvedObjectKind

    @property
    def InvolvedObjectName(self):
        return self._InvolvedObjectName

    @InvolvedObjectName.setter
    def InvolvedObjectName(self, InvolvedObjectName):
        self._InvolvedObjectName = InvolvedObjectName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP


    def _deserialize(self, params):
        self._FirstTime = params.get("FirstTime")
        self._LastTime = params.get("LastTime")
        self._InvolvedObjectKind = params.get("InvolvedObjectKind")
        self._InvolvedObjectName = params.get("InvolvedObjectName")
        self._Type = params.get("Type")
        self._Reason = params.get("Reason")
        self._Message = params.get("Message")
        self._Count = params.get("Count")
        self._NodeName = params.get("NodeName")
        self._IP = params.get("IP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GridInfo(AbstractModel):
    """Grid信息

    """

    def __init__(self):
        r"""
        :param _Id: DeployGridId
        :type Id: int
        :param _Name: 名称
        :type Name: str
        :param _GridUniqKey: Key
        :type GridUniqKey: str
        :param _Description: 描述
        :type Description: str
        :param _WorkloadKind: 工作负载类型
        :type WorkloadKind: str
        :param _StartTime: 启动时间
        :type StartTime: str
        :param _Replicas: 副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param _Publisher: 创建人
        :type Publisher: str
        :param _Version: 版本信息
        :type Version: str
        """
        self._Id = None
        self._Name = None
        self._GridUniqKey = None
        self._Description = None
        self._WorkloadKind = None
        self._StartTime = None
        self._Replicas = None
        self._Publisher = None
        self._Version = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def GridUniqKey(self):
        return self._GridUniqKey

    @GridUniqKey.setter
    def GridUniqKey(self, GridUniqKey):
        self._GridUniqKey = GridUniqKey

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WorkloadKind(self):
        return self._WorkloadKind

    @WorkloadKind.setter
    def WorkloadKind(self, WorkloadKind):
        self._WorkloadKind = WorkloadKind

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def Publisher(self):
        return self._Publisher

    @Publisher.setter
    def Publisher(self, Publisher):
        self._Publisher = Publisher

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._GridUniqKey = params.get("GridUniqKey")
        self._Description = params.get("Description")
        self._WorkloadKind = params.get("WorkloadKind")
        self._StartTime = params.get("StartTime")
        self._Replicas = params.get("Replicas")
        self._Publisher = params.get("Publisher")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GridItemInfo(AbstractModel):
    """Grid部署应用信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Replicas: 期望副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param _AvailableReplicas: 可用副本数
        :type AvailableReplicas: int
        :param _StartTime: 启动时间
        :type StartTime: str
        :param _WorkloadKind: 工作负载类型
        :type WorkloadKind: str
        """
        self._Name = None
        self._Replicas = None
        self._AvailableReplicas = None
        self._StartTime = None
        self._WorkloadKind = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def AvailableReplicas(self):
        return self._AvailableReplicas

    @AvailableReplicas.setter
    def AvailableReplicas(self, AvailableReplicas):
        self._AvailableReplicas = AvailableReplicas

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def WorkloadKind(self):
        return self._WorkloadKind

    @WorkloadKind.setter
    def WorkloadKind(self, WorkloadKind):
        self._WorkloadKind = WorkloadKind


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Replicas = params.get("Replicas")
        self._AvailableReplicas = params.get("AvailableReplicas")
        self._StartTime = params.get("StartTime")
        self._WorkloadKind = params.get("WorkloadKind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GridPodInfo(AbstractModel):
    """GridPod信息

    """

    def __init__(self):
        r"""
        :param _Name: Pod名称
        :type Name: str
        :param _NameSpace: 命名空间
        :type NameSpace: str
        :param _Status: 状态(Pending｜Running｜Succeeded｜Failed｜Unknown)
        :type Status: str
        :param _NodeName: 节点名
        :type NodeName: str
        :param _NodeIP: 节点IP
        :type NodeIP: str
        :param _PodIP: Pod的IP
        :type PodIP: str
        :param _StartTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _RunSec: 运行时长（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type RunSec: int
        :param _RestartCount: 重启次数
        :type RestartCount: int
        :param _ClusterID: 集群名称ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterID: str
        """
        self._Name = None
        self._NameSpace = None
        self._Status = None
        self._NodeName = None
        self._NodeIP = None
        self._PodIP = None
        self._StartTime = None
        self._RunSec = None
        self._RestartCount = None
        self._ClusterID = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NameSpace(self):
        return self._NameSpace

    @NameSpace.setter
    def NameSpace(self, NameSpace):
        self._NameSpace = NameSpace

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def NodeIP(self):
        return self._NodeIP

    @NodeIP.setter
    def NodeIP(self, NodeIP):
        self._NodeIP = NodeIP

    @property
    def PodIP(self):
        return self._PodIP

    @PodIP.setter
    def PodIP(self, PodIP):
        self._PodIP = PodIP

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def RunSec(self):
        return self._RunSec

    @RunSec.setter
    def RunSec(self, RunSec):
        self._RunSec = RunSec

    @property
    def RestartCount(self):
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._NameSpace = params.get("NameSpace")
        self._Status = params.get("Status")
        self._NodeName = params.get("NodeName")
        self._NodeIP = params.get("NodeIP")
        self._PodIP = params.get("PodIP")
        self._StartTime = params.get("StartTime")
        self._RunSec = params.get("RunSec")
        self._RestartCount = params.get("RestartCount")
        self._ClusterID = params.get("ClusterID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HorizontalPodAutoscaler(AbstractModel):
    """pod水平伸缩配置

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _MinReplicas: 最小实例数
        :type MinReplicas: int
        :param _MaxReplicas: 最大实例数
        :type MaxReplicas: int
        :param _ResourceMetricTarget: 资源目标指标
        :type ResourceMetricTarget: list of ResourceMetricTarget
        """
        self._Name = None
        self._Namespace = None
        self._MinReplicas = None
        self._MaxReplicas = None
        self._ResourceMetricTarget = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

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
    def ResourceMetricTarget(self):
        return self._ResourceMetricTarget

    @ResourceMetricTarget.setter
    def ResourceMetricTarget(self, ResourceMetricTarget):
        self._ResourceMetricTarget = ResourceMetricTarget


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("ResourceMetricTarget") is not None:
            self._ResourceMetricTarget = []
            for item in params.get("ResourceMetricTarget"):
                obj = ResourceMetricTarget()
                obj._deserialize(item)
                self._ResourceMetricTarget.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeader(AbstractModel):
    """Http探测头

    """

    def __init__(self):
        r"""
        :param _Name: HTTP头的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: HTTP头的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
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
        


class HttpProbe(AbstractModel):
    """HTTP探测配置

    """

    def __init__(self):
        r"""
        :param _Path: 请求路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Port: 请求端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Host: 请求地址，默认Pod的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param _Scheme: 请求模式  HTTP|HTTPS，默认HTTP
注意：此字段可能返回 null，表示取不到有效值。
        :type Scheme: str
        :param _Headers: HTTP的请求头
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of HttpHeader
        """
        self._Path = None
        self._Port = None
        self._Host = None
        self._Scheme = None
        self._Headers = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Port = params.get("Port")
        self._Host = params.get("Host")
        self._Scheme = params.get("Scheme")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = HttpHeader()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IotDevicesInfo(AbstractModel):
    """子设备列表信息

    """

    def __init__(self):
        r"""
        :param _Id: 设备id
        :type Id: int
        :param _Name: 设备名称
        :type Name: str
        :param _Status: 设备状态
        :type Status: int
        :param _Disabled: 设备打开状态
        :type Disabled: bool
        :param _Description: 描述
        :type Description: str
        :param _CreateTime: 设备创建时间
        :type CreateTime: str
        :param _LastOnlineTime: 最后在线时间
        :type LastOnlineTime: str
        :param _IsBound: 设备是否绑定到节点
        :type IsBound: bool
        :param _Version: 设备版本
        :type Version: str
        :param _Region: 无
        :type Region: str
        :param _UnitID: 无
        :type UnitID: int
        :param _UnitName: 无
        :type UnitName: str
        """
        self._Id = None
        self._Name = None
        self._Status = None
        self._Disabled = None
        self._Description = None
        self._CreateTime = None
        self._LastOnlineTime = None
        self._IsBound = None
        self._Version = None
        self._Region = None
        self._UnitID = None
        self._UnitName = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastOnlineTime(self):
        return self._LastOnlineTime

    @LastOnlineTime.setter
    def LastOnlineTime(self, LastOnlineTime):
        self._LastOnlineTime = LastOnlineTime

    @property
    def IsBound(self):
        return self._IsBound

    @IsBound.setter
    def IsBound(self, IsBound):
        self._IsBound = IsBound

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def UnitID(self):
        return self._UnitID

    @UnitID.setter
    def UnitID(self, UnitID):
        self._UnitID = UnitID

    @property
    def UnitName(self):
        return self._UnitName

    @UnitName.setter
    def UnitName(self, UnitName):
        self._UnitName = UnitName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Disabled = params.get("Disabled")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._LastOnlineTime = params.get("LastOnlineTime")
        self._IsBound = params.get("IsBound")
        self._Version = params.get("Version")
        self._Region = params.get("Region")
        self._UnitID = params.get("UnitID")
        self._UnitName = params.get("UnitName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    """Job配置

    """

    def __init__(self):
        r"""
        :param _Parallelism: 并发数
        :type Parallelism: int
        :param _Completion: 完成数
        :type Completion: int
        :param _ActiveDeadlineSeconds: 最大运行时间
        :type ActiveDeadlineSeconds: int
        :param _BackOffLimit: 失败前重试次数
        :type BackOffLimit: int
        """
        self._Parallelism = None
        self._Completion = None
        self._ActiveDeadlineSeconds = None
        self._BackOffLimit = None

    @property
    def Parallelism(self):
        return self._Parallelism

    @Parallelism.setter
    def Parallelism(self, Parallelism):
        self._Parallelism = Parallelism

    @property
    def Completion(self):
        return self._Completion

    @Completion.setter
    def Completion(self, Completion):
        self._Completion = Completion

    @property
    def ActiveDeadlineSeconds(self):
        return self._ActiveDeadlineSeconds

    @ActiveDeadlineSeconds.setter
    def ActiveDeadlineSeconds(self, ActiveDeadlineSeconds):
        self._ActiveDeadlineSeconds = ActiveDeadlineSeconds

    @property
    def BackOffLimit(self):
        return self._BackOffLimit

    @BackOffLimit.setter
    def BackOffLimit(self, BackOffLimit):
        self._BackOffLimit = BackOffLimit


    def _deserialize(self, params):
        self._Parallelism = params.get("Parallelism")
        self._Completion = params.get("Completion")
        self._ActiveDeadlineSeconds = params.get("ActiveDeadlineSeconds")
        self._BackOffLimit = params.get("BackOffLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValueObj(AbstractModel):
    """KeyValue对象

    """

    def __init__(self):
        r"""
        :param _Key: Key值
        :type Key: str
        :param _Value: Value值
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
        


class Label(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param _Key: 健名
        :type Key: str
        :param _Value: 健值
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
        


class MarketComponentInfo(AbstractModel):
    """组件市场的组件描述

    """

    def __init__(self):
        r"""
        :param _ID: 组件ID
        :type ID: int
        :param _AppName: 组件名称
        :type AppName: str
        :param _Author: 发布者
        :type Author: str
        :param _ReleaseTime: 发布时间
        :type ReleaseTime: str
        :param _Outline: 组件简介
        :type Outline: str
        :param _Detail: 指向详细描述的url
        :type Detail: str
        :param _Icon: 图标链接
        :type Icon: str
        :param _Version: 组件版本
        :type Version: str
        :param _WorkloadVisualConfig: 组件可视化信息
        :type WorkloadVisualConfig: str
        :param _DetailUrl: 无
        :type DetailUrl: str
        :param _Installed: 无
        :type Installed: bool
        """
        self._ID = None
        self._AppName = None
        self._Author = None
        self._ReleaseTime = None
        self._Outline = None
        self._Detail = None
        self._Icon = None
        self._Version = None
        self._WorkloadVisualConfig = None
        self._DetailUrl = None
        self._Installed = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def Author(self):
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def ReleaseTime(self):
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def Outline(self):
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Icon(self):
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def WorkloadVisualConfig(self):
        return self._WorkloadVisualConfig

    @WorkloadVisualConfig.setter
    def WorkloadVisualConfig(self, WorkloadVisualConfig):
        self._WorkloadVisualConfig = WorkloadVisualConfig

    @property
    def DetailUrl(self):
        return self._DetailUrl

    @DetailUrl.setter
    def DetailUrl(self, DetailUrl):
        self._DetailUrl = DetailUrl

    @property
    def Installed(self):
        return self._Installed

    @Installed.setter
    def Installed(self, Installed):
        self._Installed = Installed


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._AppName = params.get("AppName")
        self._Author = params.get("Author")
        self._ReleaseTime = params.get("ReleaseTime")
        self._Outline = params.get("Outline")
        self._Detail = params.get("Detail")
        self._Icon = params.get("Icon")
        self._Version = params.get("Version")
        self._WorkloadVisualConfig = params.get("WorkloadVisualConfig")
        self._DetailUrl = params.get("DetailUrl")
        self._Installed = params.get("Installed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationBasicInfoRequest(AbstractModel):
    """ModifyApplicationBasicInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用模板ID
        :type ApplicationId: int
        :param _BasicInfo: 应用模板基本信息
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        """
        self._ApplicationId = None
        self._BasicInfo = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def BasicInfo(self):
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        if params.get("BasicInfo") is not None:
            self._BasicInfo = ApplicationBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationBasicInfoResponse(AbstractModel):
    """ModifyApplicationBasicInfo返回参数结构体

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


class ModifyApplicationVisualizationRequest(AbstractModel):
    """ModifyApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        :param _BasicConfig: 应用配置
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param _Volumes: 卷配置
        :type Volumes: list of Volume
        :param _InitContainers: 初始容器
        :type InitContainers: list of Container
        :param _Containers: 容器配置
        :type Containers: list of Container
        :param _Service: 服务配置
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param _Job: Job配置
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param _CronJob: CronJob配置
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param _RestartPolicy: 重启策略
        :type RestartPolicy: str
        :param _ImagePullSecrets: 镜像拉取密钥
        :type ImagePullSecrets: list of str
        :param _HorizontalPodAutoscaler: HPA配置
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        :param _InitContainer: 单个初始化容器
        :type InitContainer: :class:`tencentcloud.iecp.v20210914.models.Container`
        """
        self._ApplicationId = None
        self._BasicConfig = None
        self._Volumes = None
        self._InitContainers = None
        self._Containers = None
        self._Service = None
        self._Job = None
        self._CronJob = None
        self._RestartPolicy = None
        self._ImagePullSecrets = None
        self._HorizontalPodAutoscaler = None
        self._InitContainer = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def BasicConfig(self):
        return self._BasicConfig

    @BasicConfig.setter
    def BasicConfig(self, BasicConfig):
        self._BasicConfig = BasicConfig

    @property
    def Volumes(self):
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def InitContainers(self):
        return self._InitContainers

    @InitContainers.setter
    def InitContainers(self, InitContainers):
        self._InitContainers = InitContainers

    @property
    def Containers(self):
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def CronJob(self):
        return self._CronJob

    @CronJob.setter
    def CronJob(self, CronJob):
        self._CronJob = CronJob

    @property
    def RestartPolicy(self):
        return self._RestartPolicy

    @RestartPolicy.setter
    def RestartPolicy(self, RestartPolicy):
        self._RestartPolicy = RestartPolicy

    @property
    def ImagePullSecrets(self):
        return self._ImagePullSecrets

    @ImagePullSecrets.setter
    def ImagePullSecrets(self, ImagePullSecrets):
        self._ImagePullSecrets = ImagePullSecrets

    @property
    def HorizontalPodAutoscaler(self):
        return self._HorizontalPodAutoscaler

    @HorizontalPodAutoscaler.setter
    def HorizontalPodAutoscaler(self, HorizontalPodAutoscaler):
        self._HorizontalPodAutoscaler = HorizontalPodAutoscaler

    @property
    def InitContainer(self):
        return self._InitContainer

    @InitContainer.setter
    def InitContainer(self, InitContainer):
        self._InitContainer = InitContainer


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        if params.get("BasicConfig") is not None:
            self._BasicConfig = ApplicationBasicConfig()
            self._BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self._Volumes.append(obj)
        if params.get("InitContainers") is not None:
            self._InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self._InitContainers.append(obj)
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self._Containers.append(obj)
        if params.get("Service") is not None:
            self._Service = Service()
            self._Service._deserialize(params.get("Service"))
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self._CronJob = CronJob()
            self._CronJob._deserialize(params.get("CronJob"))
        self._RestartPolicy = params.get("RestartPolicy")
        self._ImagePullSecrets = params.get("ImagePullSecrets")
        if params.get("HorizontalPodAutoscaler") is not None:
            self._HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self._HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        if params.get("InitContainer") is not None:
            self._InitContainer = Container()
            self._InitContainer._deserialize(params.get("InitContainer"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationVisualizationResponse(AbstractModel):
    """ModifyApplicationVisualization返回参数结构体

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


class ModifyConfigMapRequest(AbstractModel):
    """ModifyConfigMap请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param _ConfigMapName: ConfigMap名称
        :type ConfigMapName: str
        :param _Yaml: Yaml配置, base64之后的串
        :type Yaml: str
        :param _ConfigMapNamespace: ConfigMap命名空间
        :type ConfigMapNamespace: str
        """
        self._EdgeUnitID = None
        self._ConfigMapName = None
        self._Yaml = None
        self._ConfigMapNamespace = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def ConfigMapName(self):
        return self._ConfigMapName

    @ConfigMapName.setter
    def ConfigMapName(self, ConfigMapName):
        self._ConfigMapName = ConfigMapName

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def ConfigMapNamespace(self):
        return self._ConfigMapNamespace

    @ConfigMapNamespace.setter
    def ConfigMapNamespace(self, ConfigMapNamespace):
        self._ConfigMapNamespace = ConfigMapNamespace


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._ConfigMapName = params.get("ConfigMapName")
        self._Yaml = params.get("Yaml")
        self._ConfigMapNamespace = params.get("ConfigMapNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigMapResponse(AbstractModel):
    """ModifyConfigMap返回参数结构体

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


class ModifyEdgeDracoNodeRequest(AbstractModel):
    """ModifyEdgeDracoNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 边缘单元ID
        :type EdgeUnitId: int
        :param _NodeId: 边缘节点ID
        :type NodeId: int
        :param _NodeInfo: 节点信息
        :type NodeInfo: :class:`tencentcloud.iecp.v20210914.models.DracoNodeInfo`
        :param _IsReset: 是否重置draco设备
        :type IsReset: bool
        """
        self._EdgeUnitId = None
        self._NodeId = None
        self._NodeInfo = None
        self._IsReset = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeInfo(self):
        return self._NodeInfo

    @NodeInfo.setter
    def NodeInfo(self, NodeInfo):
        self._NodeInfo = NodeInfo

    @property
    def IsReset(self):
        return self._IsReset

    @IsReset.setter
    def IsReset(self, IsReset):
        self._IsReset = IsReset


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeId = params.get("NodeId")
        if params.get("NodeInfo") is not None:
            self._NodeInfo = DracoNodeInfo()
            self._NodeInfo._deserialize(params.get("NodeInfo"))
        self._IsReset = params.get("IsReset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeDracoNodeResponse(AbstractModel):
    """ModifyEdgeDracoNode返回参数结构体

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


class ModifyEdgeNodeLabelsRequest(AbstractModel):
    """ModifyEdgeNodeLabels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NodeId: IECP边缘节点ID
        :type NodeId: int
        :param _Labels: 标签列表
        :type Labels: list of KeyValueObj
        """
        self._EdgeUnitId = None
        self._NodeId = None
        self._Labels = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeId = params.get("NodeId")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = KeyValueObj()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeNodeLabelsResponse(AbstractModel):
    """ModifyEdgeNodeLabels返回参数结构体

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


class ModifyEdgeUnitApplicationBasicInfoRequest(AbstractModel):
    """ModifyEdgeUnitApplicationBasicInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BasicInfo: 应用基本信息
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self._BasicInfo = None
        self._EdgeUnitId = None
        self._ApplicationId = None

    @property
    def BasicInfo(self):
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self._BasicInfo = ApplicationBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeUnitApplicationBasicInfoResponse(AbstractModel):
    """ModifyEdgeUnitApplicationBasicInfo返回参数结构体

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


class ModifyEdgeUnitApplicationVisualizationRequest(AbstractModel):
    """ModifyEdgeUnitApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        :param _BasicConfig: 应用配置
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param _Volumes: 卷配置
        :type Volumes: list of Volume
        :param _InitContainers: 初始容器列表
        :type InitContainers: list of Container
        :param _Containers: 容器配置
        :type Containers: list of Container
        :param _Service: 服务配置
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param _Job: Job配置
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param _CronJob: CronJob配置
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param _RestartPolicy: 重启策略
        :type RestartPolicy: str
        :param _ImagePullSecrets: 镜像拉取密钥
        :type ImagePullSecrets: list of str
        :param _HorizontalPodAutoscaler: HPA配置
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        """
        self._EdgeUnitId = None
        self._ApplicationId = None
        self._BasicConfig = None
        self._Volumes = None
        self._InitContainers = None
        self._Containers = None
        self._Service = None
        self._Job = None
        self._CronJob = None
        self._RestartPolicy = None
        self._ImagePullSecrets = None
        self._HorizontalPodAutoscaler = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def BasicConfig(self):
        return self._BasicConfig

    @BasicConfig.setter
    def BasicConfig(self, BasicConfig):
        self._BasicConfig = BasicConfig

    @property
    def Volumes(self):
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def InitContainers(self):
        return self._InitContainers

    @InitContainers.setter
    def InitContainers(self, InitContainers):
        self._InitContainers = InitContainers

    @property
    def Containers(self):
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def CronJob(self):
        return self._CronJob

    @CronJob.setter
    def CronJob(self, CronJob):
        self._CronJob = CronJob

    @property
    def RestartPolicy(self):
        return self._RestartPolicy

    @RestartPolicy.setter
    def RestartPolicy(self, RestartPolicy):
        self._RestartPolicy = RestartPolicy

    @property
    def ImagePullSecrets(self):
        return self._ImagePullSecrets

    @ImagePullSecrets.setter
    def ImagePullSecrets(self, ImagePullSecrets):
        self._ImagePullSecrets = ImagePullSecrets

    @property
    def HorizontalPodAutoscaler(self):
        return self._HorizontalPodAutoscaler

    @HorizontalPodAutoscaler.setter
    def HorizontalPodAutoscaler(self, HorizontalPodAutoscaler):
        self._HorizontalPodAutoscaler = HorizontalPodAutoscaler


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._ApplicationId = params.get("ApplicationId")
        if params.get("BasicConfig") is not None:
            self._BasicConfig = ApplicationBasicConfig()
            self._BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self._Volumes.append(obj)
        if params.get("InitContainers") is not None:
            self._InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self._InitContainers.append(obj)
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self._Containers.append(obj)
        if params.get("Service") is not None:
            self._Service = Service()
            self._Service._deserialize(params.get("Service"))
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self._CronJob = CronJob()
            self._CronJob._deserialize(params.get("CronJob"))
        self._RestartPolicy = params.get("RestartPolicy")
        self._ImagePullSecrets = params.get("ImagePullSecrets")
        if params.get("HorizontalPodAutoscaler") is not None:
            self._HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self._HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeUnitApplicationVisualizationResponse(AbstractModel):
    """ModifyEdgeUnitApplicationVisualization返回参数结构体

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


class ModifyEdgeUnitApplicationYamlRequest(AbstractModel):
    """ModifyEdgeUnitApplicationYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        :param _Yaml: Yaml配置
        :type Yaml: str
        """
        self._EdgeUnitId = None
        self._ApplicationId = None
        self._Yaml = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._ApplicationId = params.get("ApplicationId")
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeUnitApplicationYamlResponse(AbstractModel):
    """ModifyEdgeUnitApplicationYaml返回参数结构体

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


class ModifyEdgeUnitCloudApiRequest(AbstractModel):
    """ModifyEdgeUnitCloudApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 边缘单元ID
        :type EdgeUnitId: int
        :param _Name: 边缘单元名称，64字符内
        :type Name: str
        :param _Description: 描述，200字符内
        :type Description: str
        :param _OpenCloudMonitor: 是否开启监控
        :type OpenCloudMonitor: bool
        """
        self._EdgeUnitId = None
        self._Name = None
        self._Description = None
        self._OpenCloudMonitor = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OpenCloudMonitor(self):
        return self._OpenCloudMonitor

    @OpenCloudMonitor.setter
    def OpenCloudMonitor(self, OpenCloudMonitor):
        self._OpenCloudMonitor = OpenCloudMonitor


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._OpenCloudMonitor = params.get("OpenCloudMonitor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeUnitCloudApiResponse(AbstractModel):
    """ModifyEdgeUnitCloudApi返回参数结构体

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


class ModifyEdgeUnitDeployGridItemRequest(AbstractModel):
    """ModifyEdgeUnitDeployGridItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _GridItemName: Grid名称
        :type GridItemName: str
        :param _WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param _Replicas: 副本数
        :type Replicas: int
        :param _Namespace: 命名空间，默认default
        :type Namespace: str
        """
        self._EdgeUnitId = None
        self._GridItemName = None
        self._WorkloadKind = None
        self._Replicas = None
        self._Namespace = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def GridItemName(self):
        return self._GridItemName

    @GridItemName.setter
    def GridItemName(self, GridItemName):
        self._GridItemName = GridItemName

    @property
    def WorkloadKind(self):
        return self._WorkloadKind

    @WorkloadKind.setter
    def WorkloadKind(self, WorkloadKind):
        self._WorkloadKind = WorkloadKind

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._GridItemName = params.get("GridItemName")
        self._WorkloadKind = params.get("WorkloadKind")
        self._Replicas = params.get("Replicas")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeUnitDeployGridItemResponse(AbstractModel):
    """ModifyEdgeUnitDeployGridItem返回参数结构体

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


class ModifyEdgeUnitRequest(AbstractModel):
    """ModifyEdgeUnit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 边缘集群ID
        :type EdgeUnitId: int
        :param _Name: 边缘集群名称，64字符以内
        :type Name: str
        :param _Description: 集群描述，200字符以内
        :type Description: str
        """
        self._EdgeUnitId = None
        self._Name = None
        self._Description = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeUnitResponse(AbstractModel):
    """ModifyEdgeUnit返回参数结构体

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


class ModifyIotDeviceRequest(AbstractModel):
    """ModifyIotDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备id
        :type DeviceId: int
        :param _Description: 描述
        :type Description: str
        :param _Disabled: 设备是否开启
        :type Disabled: bool
        :param _LogSetting: 日志设置
        :type LogSetting: int
        :param _LogLevel: 日志级别
        :type LogLevel: int
        """
        self._DeviceId = None
        self._Description = None
        self._Disabled = None
        self._LogSetting = None
        self._LogLevel = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def LogSetting(self):
        return self._LogSetting

    @LogSetting.setter
    def LogSetting(self, LogSetting):
        self._LogSetting = LogSetting

    @property
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Description = params.get("Description")
        self._Disabled = params.get("Disabled")
        self._LogSetting = params.get("LogSetting")
        self._LogLevel = params.get("LogLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIotDeviceResponse(AbstractModel):
    """ModifyIotDevice返回参数结构体

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


class ModifyNodeUnitTemplateRequest(AbstractModel):
    """ModifyNodeUnitTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param _NodeUnitTemplateID: NodeUnit模板ID
        :type NodeUnitTemplateID: int
        :param _Nodes: 包含的节点列表
        :type Nodes: list of str
        """
        self._EdgeUnitId = None
        self._NodeUnitTemplateID = None
        self._Nodes = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def NodeUnitTemplateID(self):
        return self._NodeUnitTemplateID

    @NodeUnitTemplateID.setter
    def NodeUnitTemplateID(self, NodeUnitTemplateID):
        self._NodeUnitTemplateID = NodeUnitTemplateID

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._NodeUnitTemplateID = params.get("NodeUnitTemplateID")
        self._Nodes = params.get("Nodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNodeUnitTemplateResponse(AbstractModel):
    """ModifyNodeUnitTemplate返回参数结构体

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


class ModifySecretRequest(AbstractModel):
    """ModifySecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitID: 边缘单元ID
        :type EdgeUnitID: int
        :param _SecretName: Secret名
        :type SecretName: str
        :param _Yaml: Secret的Yaml格式
        :type Yaml: str
        :param _SecretNamespace: Secret命名空间（默认:default）
        :type SecretNamespace: str
        """
        self._EdgeUnitID = None
        self._SecretName = None
        self._Yaml = None
        self._SecretNamespace = None

    @property
    def EdgeUnitID(self):
        return self._EdgeUnitID

    @EdgeUnitID.setter
    def EdgeUnitID(self, EdgeUnitID):
        self._EdgeUnitID = EdgeUnitID

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def SecretNamespace(self):
        return self._SecretNamespace

    @SecretNamespace.setter
    def SecretNamespace(self, SecretNamespace):
        self._SecretNamespace = SecretNamespace


    def _deserialize(self, params):
        self._EdgeUnitID = params.get("EdgeUnitID")
        self._SecretName = params.get("SecretName")
        self._Yaml = params.get("Yaml")
        self._SecretNamespace = params.get("SecretNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecretResponse(AbstractModel):
    """ModifySecret返回参数结构体

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


class MonitorMetricsColumn(AbstractModel):
    """监控数据列

    """

    def __init__(self):
        r"""
        :param _ColumnName: 数据名称
        :type ColumnName: str
        :param _ColumnData: 数据内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ColumnData: list of str
        :param _ColumnBelong: 数据所属，查询Workload类型时有值
        :type ColumnBelong: str
        :param _MaxValue: 最大值
        :type MaxValue: float
        :param _MinValue: 最小值
        :type MinValue: float
        :param _AvgValue: 平均值
        :type AvgValue: float
        :param _ColumnTime: 时间戳数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ColumnTime: int
        """
        self._ColumnName = None
        self._ColumnData = None
        self._ColumnBelong = None
        self._MaxValue = None
        self._MinValue = None
        self._AvgValue = None
        self._ColumnTime = None

    @property
    def ColumnName(self):
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName

    @property
    def ColumnData(self):
        return self._ColumnData

    @ColumnData.setter
    def ColumnData(self, ColumnData):
        self._ColumnData = ColumnData

    @property
    def ColumnBelong(self):
        return self._ColumnBelong

    @ColumnBelong.setter
    def ColumnBelong(self, ColumnBelong):
        self._ColumnBelong = ColumnBelong

    @property
    def MaxValue(self):
        return self._MaxValue

    @MaxValue.setter
    def MaxValue(self, MaxValue):
        self._MaxValue = MaxValue

    @property
    def MinValue(self):
        return self._MinValue

    @MinValue.setter
    def MinValue(self, MinValue):
        self._MinValue = MinValue

    @property
    def AvgValue(self):
        return self._AvgValue

    @AvgValue.setter
    def AvgValue(self, AvgValue):
        self._AvgValue = AvgValue

    @property
    def ColumnTime(self):
        return self._ColumnTime

    @ColumnTime.setter
    def ColumnTime(self, ColumnTime):
        self._ColumnTime = ColumnTime


    def _deserialize(self, params):
        self._ColumnName = params.get("ColumnName")
        self._ColumnData = params.get("ColumnData")
        self._ColumnBelong = params.get("ColumnBelong")
        self._MaxValue = params.get("MaxValue")
        self._MinValue = params.get("MinValue")
        self._AvgValue = params.get("AvgValue")
        self._ColumnTime = params.get("ColumnTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceInfo(AbstractModel):
    """命名空间信息

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间名
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _Status: 状态(Active|Terminating)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Protected: 是否保护(不允许删除)
注意：此字段可能返回 null，表示取不到有效值。
        :type Protected: bool
        :param _Yaml: 对应的Yaml配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        """
        self._Namespace = None
        self._Status = None
        self._Description = None
        self._CreateTime = None
        self._Protected = None
        self._Yaml = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Protected(self):
        return self._Protected

    @Protected.setter
    def Protected(self, Protected):
        self._Protected = Protected

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._Protected = params.get("Protected")
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceResource(AbstractModel):
    """命名空间下资源描述

    """

    def __init__(self):
        r"""
        :param _Type: 类型(workload|grid|configmap|secret)
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Count: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Names: 名称(最多返回5个）
注意：此字段可能返回 null，表示取不到有效值。
        :type Names: list of str
        """
        self._Type = None
        self._Count = None
        self._Names = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Count = params.get("Count")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeGroupInfo(AbstractModel):
    """NodeGroup信息

    """

    def __init__(self):
        r"""
        :param _Description: 描述
        :type Description: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _NodeGroupName: NodeGroup名称
        :type NodeGroupName: str
        :param _DeploymentGridList: DeploymentGrid数组
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploymentGridList: list of GridDetail
        :param _StatefulSetGridList: StatefulSetGrid数组
注意：此字段可能返回 null，表示取不到有效值。
        :type StatefulSetGridList: list of GridDetail
        :param _Protect: 是否平台保护
注意：此字段可能返回 null，表示取不到有效值。
        :type Protect: bool
        """
        self._Description = None
        self._CreateTime = None
        self._NodeGroupName = None
        self._DeploymentGridList = None
        self._StatefulSetGridList = None
        self._Protect = None

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def NodeGroupName(self):
        return self._NodeGroupName

    @NodeGroupName.setter
    def NodeGroupName(self, NodeGroupName):
        self._NodeGroupName = NodeGroupName

    @property
    def DeploymentGridList(self):
        return self._DeploymentGridList

    @DeploymentGridList.setter
    def DeploymentGridList(self, DeploymentGridList):
        self._DeploymentGridList = DeploymentGridList

    @property
    def StatefulSetGridList(self):
        return self._StatefulSetGridList

    @StatefulSetGridList.setter
    def StatefulSetGridList(self, StatefulSetGridList):
        self._StatefulSetGridList = StatefulSetGridList

    @property
    def Protect(self):
        return self._Protect

    @Protect.setter
    def Protect(self, Protect):
        self._Protect = Protect


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._NodeGroupName = params.get("NodeGroupName")
        if params.get("DeploymentGridList") is not None:
            self._DeploymentGridList = []
            for item in params.get("DeploymentGridList"):
                obj = GridDetail()
                obj._deserialize(item)
                self._DeploymentGridList.append(obj)
        if params.get("StatefulSetGridList") is not None:
            self._StatefulSetGridList = []
            for item in params.get("StatefulSetGridList"):
                obj = GridDetail()
                obj._deserialize(item)
                self._StatefulSetGridList.append(obj)
        self._Protect = params.get("Protect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeGroupNodeUnitTemplateInfo(AbstractModel):
    """指定NodeGroup中查询NodeUnit模版

    """

    def __init__(self):
        r"""
        :param _ID: 模版ID
        :type ID: int
        :param _Name: 名称
        :type Name: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Description: 描述
        :type Description: str
        :param _NodeList: 包含节点列表
        :type NodeList: list of NodeSimpleInfo
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Relation: 是否关联
        :type Relation: bool
        """
        self._ID = None
        self._Name = None
        self._Namespace = None
        self._Description = None
        self._NodeList = None
        self._UpdateTime = None
        self._CreateTime = None
        self._Relation = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NodeList(self):
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Relation(self):
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Description = params.get("Description")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = NodeSimpleInfo()
                obj._deserialize(item)
                self._NodeList.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeSimpleInfo(AbstractModel):
    """节点基础信息

    """

    def __init__(self):
        r"""
        :param _ID: 节点ID
        :type ID: int
        :param _NodeName: 节点名称
        :type NodeName: str
        """
        self._ID = None
        self._NodeName = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._NodeName = params.get("NodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeUnitInfo(AbstractModel):
    """NodeUnit信息

    """

    def __init__(self):
        r"""
        :param _Id: NodeUnitId
        :type Id: int
        :param _NodeUnitName: NodeUnit名称
        :type NodeUnitName: str
        :param _NodeList: 包含节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeList: list of NodeUnitNodeInfo
        """
        self._Id = None
        self._NodeUnitName = None
        self._NodeList = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def NodeUnitName(self):
        return self._NodeUnitName

    @NodeUnitName.setter
    def NodeUnitName(self, NodeUnitName):
        self._NodeUnitName = NodeUnitName

    @property
    def NodeList(self):
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._NodeUnitName = params.get("NodeUnitName")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = NodeUnitNodeInfo()
                obj._deserialize(item)
                self._NodeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeUnitNodeInfo(AbstractModel):
    """NodeUnit中边缘节点信息

    """

    def __init__(self):
        r"""
        :param _Id: 节点ID
        :type Id: int
        :param _Status: 节点状态  NodeStatusHealthy (健康)/NodeStatusAbnormal (异常)/NodeStatusOffline (下线)/NodeStatusNotActivated (未激活
        :type Status: str
        :param _NodeName: 节点名称
        :type NodeName: str
        :param _InternalIP: 内网节点IP
        :type InternalIP: str
        """
        self._Id = None
        self._Status = None
        self._NodeName = None
        self._InternalIP = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def InternalIP(self):
        return self._InternalIP

    @InternalIP.setter
    def InternalIP(self, InternalIP):
        self._InternalIP = InternalIP


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._NodeName = params.get("NodeName")
        self._InternalIP = params.get("InternalIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeUnitTemplate(AbstractModel):
    """NodeUnit模版信息

    """

    def __init__(self):
        r"""
        :param _ID: NodeUnit模版ID
        :type ID: int
        :param _Name: NodeUnit模版名称
        :type Name: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Description: 描述
        :type Description: str
        :param _NodeList: 包含节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeList: list of NodeSimpleInfo
        :param _NodeGroups: NodeGroup列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeGroups: list of str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._ID = None
        self._Name = None
        self._Namespace = None
        self._Description = None
        self._NodeList = None
        self._NodeGroups = None
        self._UpdateTime = None
        self._CreateTime = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NodeList(self):
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

    @property
    def NodeGroups(self):
        return self._NodeGroups

    @NodeGroups.setter
    def NodeGroups(self, NodeGroups):
        self._NodeGroups = NodeGroups

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Description = params.get("Description")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = NodeSimpleInfo()
                obj._deserialize(item)
                self._NodeList.append(obj)
        self._NodeGroups = params.get("NodeGroups")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationLog(AbstractModel):
    """操作日志

    """

    def __init__(self):
        r"""
        :param _OperateTime: 操作时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateTime: str
        :param _Module: 模块名
注意：此字段可能返回 null，表示取不到有效值。
        :type Module: str
        :param _Description: 操作信息
        :type Description: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _Status: 状态: 1:成功 2:失败
        :type Status: int
        :param _OperatorUserID: 操作用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorUserID: str
        :param _Action: 操作动作
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        """
        self._OperateTime = None
        self._Module = None
        self._Description = None
        self._UserId = None
        self._Status = None
        self._OperatorUserID = None
        self._Action = None

    @property
    def OperateTime(self):
        return self._OperateTime

    @OperateTime.setter
    def OperateTime(self, OperateTime):
        self._OperateTime = OperateTime

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OperatorUserID(self):
        return self._OperatorUserID

    @OperatorUserID.setter
    def OperatorUserID(self, OperatorUserID):
        self._OperatorUserID = OperatorUserID

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._OperateTime = params.get("OperateTime")
        self._Module = params.get("Module")
        self._Description = params.get("Description")
        self._UserId = params.get("UserId")
        self._Status = params.get("Status")
        self._OperatorUserID = params.get("OperatorUserID")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationLogsCondition(AbstractModel):
    """操作日志状态查询条件

    """

    def __init__(self):
        r"""
        :param _Status: 状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: list of int
        """
        self._Status = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodStatus(AbstractModel):
    """Pod状态信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _NameSpace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type NameSpace: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _IP: IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param _StartTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _RunSec: 运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RunSec: int
        :param _RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        """
        self._Name = None
        self._NameSpace = None
        self._Status = None
        self._IP = None
        self._StartTime = None
        self._RunSec = None
        self._RestartCount = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NameSpace(self):
        return self._NameSpace

    @NameSpace.setter
    def NameSpace(self, NameSpace):
        self._NameSpace = NameSpace

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def RunSec(self):
        return self._RunSec

    @RunSec.setter
    def RunSec(self, RunSec):
        self._RunSec = RunSec

    @property
    def RestartCount(self):
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._NameSpace = params.get("NameSpace")
        self._Status = params.get("Status")
        self._IP = params.get("IP")
        self._StartTime = params.get("StartTime")
        self._RunSec = params.get("RunSec")
        self._RestartCount = params.get("RestartCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortConfig(AbstractModel):
    """端口配置

    """

    def __init__(self):
        r"""
        :param _Protocol: 协议类型(tcp|udp)
        :type Protocol: str
        :param _Port: 源端口
        :type Port: int
        :param _TargetPort: 目标端口
        :type TargetPort: int
        :param _NodePort: 节点端口
        :type NodePort: int
        """
        self._Protocol = None
        self._Port = None
        self._TargetPort = None
        self._NodePort = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

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
    def NodePort(self):
        return self._NodePort

    @NodePort.setter
    def NodePort(self, NodePort):
        self._NodePort = NodePort


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._TargetPort = params.get("TargetPort")
        self._NodePort = params.get("NodePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Probe(AbstractModel):
    """探针配置

    """

    def __init__(self):
        r"""
        :param _InitialDelaySeconds: 启动后，延迟探测时间 单位:秒
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param _PeriodSeconds: 探测间隔，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodSeconds: int
        :param _TimeoutSeconds: 探测超时时间 单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutSeconds: int
        :param _SuccessThreshold: 失败后检查成功的最小连续成功次数。默认为1.活跃度必须为1。最小值为1
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessThreshold: int
        :param _FailureThreshold: 当Pod成功启动且检查失败时，放弃之前尝试次数。默认为3.最小值为1
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureThreshold: int
        :param _HttpProbe: HTTP探测配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpProbe: :class:`tencentcloud.iecp.v20210914.models.HttpProbe`
        :param _TcpProbe: TCP探测配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TcpProbe: :class:`tencentcloud.iecp.v20210914.models.TcpProbe`
        """
        self._InitialDelaySeconds = None
        self._PeriodSeconds = None
        self._TimeoutSeconds = None
        self._SuccessThreshold = None
        self._FailureThreshold = None
        self._HttpProbe = None
        self._TcpProbe = None

    @property
    def InitialDelaySeconds(self):
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def PeriodSeconds(self):
        return self._PeriodSeconds

    @PeriodSeconds.setter
    def PeriodSeconds(self, PeriodSeconds):
        self._PeriodSeconds = PeriodSeconds

    @property
    def TimeoutSeconds(self):
        return self._TimeoutSeconds

    @TimeoutSeconds.setter
    def TimeoutSeconds(self, TimeoutSeconds):
        self._TimeoutSeconds = TimeoutSeconds

    @property
    def SuccessThreshold(self):
        return self._SuccessThreshold

    @SuccessThreshold.setter
    def SuccessThreshold(self, SuccessThreshold):
        self._SuccessThreshold = SuccessThreshold

    @property
    def FailureThreshold(self):
        return self._FailureThreshold

    @FailureThreshold.setter
    def FailureThreshold(self, FailureThreshold):
        self._FailureThreshold = FailureThreshold

    @property
    def HttpProbe(self):
        return self._HttpProbe

    @HttpProbe.setter
    def HttpProbe(self, HttpProbe):
        self._HttpProbe = HttpProbe

    @property
    def TcpProbe(self):
        return self._TcpProbe

    @TcpProbe.setter
    def TcpProbe(self, TcpProbe):
        self._TcpProbe = TcpProbe


    def _deserialize(self, params):
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        self._PeriodSeconds = params.get("PeriodSeconds")
        self._TimeoutSeconds = params.get("TimeoutSeconds")
        self._SuccessThreshold = params.get("SuccessThreshold")
        self._FailureThreshold = params.get("FailureThreshold")
        if params.get("HttpProbe") is not None:
            self._HttpProbe = HttpProbe()
            self._HttpProbe._deserialize(params.get("HttpProbe"))
        if params.get("TcpProbe") is not None:
            self._TcpProbe = TcpProbe()
            self._TcpProbe._deserialize(params.get("TcpProbe"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedeployEdgeUnitApplicationRequest(AbstractModel):
    """RedeployEdgeUnitApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param _ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self._EdgeUnitId = None
        self._ApplicationId = None

    @property
    def EdgeUnitId(self):
        return self._EdgeUnitId

    @EdgeUnitId.setter
    def EdgeUnitId(self, EdgeUnitId):
        self._EdgeUnitId = EdgeUnitId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EdgeUnitId = params.get("EdgeUnitId")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedeployEdgeUnitApplicationResponse(AbstractModel):
    """RedeployEdgeUnitApplication返回参数结构体

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


class ResourceMetricTarget(AbstractModel):
    """资源目标指标

    """

    def __init__(self):
        r"""
        :param _Type: 类型(cpu|memory)
        :type Type: str
        :param _AverageValue: 平均值
        :type AverageValue: int
        :param _Scale: 单位
        :type Scale: str
        :param _AverageUtilization: 平均值
        :type AverageUtilization: int
        """
        self._Type = None
        self._AverageValue = None
        self._Scale = None
        self._AverageUtilization = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AverageValue(self):
        return self._AverageValue

    @AverageValue.setter
    def AverageValue(self, AverageValue):
        self._AverageValue = AverageValue

    @property
    def Scale(self):
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def AverageUtilization(self):
        return self._AverageUtilization

    @AverageUtilization.setter
    def AverageUtilization(self, AverageUtilization):
        self._AverageUtilization = AverageUtilization


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._AverageValue = params.get("AverageValue")
        self._Scale = params.get("Scale")
        self._AverageUtilization = params.get("AverageUtilization")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteInfo(AbstractModel):
    """消息路由

    """

    def __init__(self):
        r"""
        :param _RouteID: 无
        :type RouteID: int
        :param _RouteName: 无
        :type RouteName: str
        :param _SourceProductID: 无
        :type SourceProductID: str
        :param _TopicFilter: 无
        :type TopicFilter: str
        :param _Mode: 无
        :type Mode: str
        :param _TargetOptions: 无
        :type TargetOptions: str
        :param _CreateTime: 无
        :type CreateTime: str
        :param _Descript: 无
        :type Descript: str
        :param _Healthy: 无
        :type Healthy: str
        :param _Status: 无
        :type Status: str
        :param _MessageCount: 无
        :type MessageCount: int
        :param _MessageLastTime: 无
        :type MessageLastTime: str
        :param _SourceProductName: 无
        :type SourceProductName: str
        :param _SourceUnitIDList: 无
        :type SourceUnitIDList: list of str
        :param _SourceUnitNameList: 无
        :type SourceUnitNameList: list of str
        :param _SourceDeviceNameList: 无
        :type SourceDeviceNameList: list of str
        """
        self._RouteID = None
        self._RouteName = None
        self._SourceProductID = None
        self._TopicFilter = None
        self._Mode = None
        self._TargetOptions = None
        self._CreateTime = None
        self._Descript = None
        self._Healthy = None
        self._Status = None
        self._MessageCount = None
        self._MessageLastTime = None
        self._SourceProductName = None
        self._SourceUnitIDList = None
        self._SourceUnitNameList = None
        self._SourceDeviceNameList = None

    @property
    def RouteID(self):
        return self._RouteID

    @RouteID.setter
    def RouteID(self, RouteID):
        self._RouteID = RouteID

    @property
    def RouteName(self):
        return self._RouteName

    @RouteName.setter
    def RouteName(self, RouteName):
        self._RouteName = RouteName

    @property
    def SourceProductID(self):
        return self._SourceProductID

    @SourceProductID.setter
    def SourceProductID(self, SourceProductID):
        self._SourceProductID = SourceProductID

    @property
    def TopicFilter(self):
        return self._TopicFilter

    @TopicFilter.setter
    def TopicFilter(self, TopicFilter):
        self._TopicFilter = TopicFilter

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def TargetOptions(self):
        return self._TargetOptions

    @TargetOptions.setter
    def TargetOptions(self, TargetOptions):
        self._TargetOptions = TargetOptions

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Descript(self):
        return self._Descript

    @Descript.setter
    def Descript(self, Descript):
        self._Descript = Descript

    @property
    def Healthy(self):
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MessageCount(self):
        return self._MessageCount

    @MessageCount.setter
    def MessageCount(self, MessageCount):
        self._MessageCount = MessageCount

    @property
    def MessageLastTime(self):
        return self._MessageLastTime

    @MessageLastTime.setter
    def MessageLastTime(self, MessageLastTime):
        self._MessageLastTime = MessageLastTime

    @property
    def SourceProductName(self):
        return self._SourceProductName

    @SourceProductName.setter
    def SourceProductName(self, SourceProductName):
        self._SourceProductName = SourceProductName

    @property
    def SourceUnitIDList(self):
        return self._SourceUnitIDList

    @SourceUnitIDList.setter
    def SourceUnitIDList(self, SourceUnitIDList):
        self._SourceUnitIDList = SourceUnitIDList

    @property
    def SourceUnitNameList(self):
        return self._SourceUnitNameList

    @SourceUnitNameList.setter
    def SourceUnitNameList(self, SourceUnitNameList):
        self._SourceUnitNameList = SourceUnitNameList

    @property
    def SourceDeviceNameList(self):
        return self._SourceDeviceNameList

    @SourceDeviceNameList.setter
    def SourceDeviceNameList(self, SourceDeviceNameList):
        self._SourceDeviceNameList = SourceDeviceNameList


    def _deserialize(self, params):
        self._RouteID = params.get("RouteID")
        self._RouteName = params.get("RouteName")
        self._SourceProductID = params.get("SourceProductID")
        self._TopicFilter = params.get("TopicFilter")
        self._Mode = params.get("Mode")
        self._TargetOptions = params.get("TargetOptions")
        self._CreateTime = params.get("CreateTime")
        self._Descript = params.get("Descript")
        self._Healthy = params.get("Healthy")
        self._Status = params.get("Status")
        self._MessageCount = params.get("MessageCount")
        self._MessageLastTime = params.get("MessageLastTime")
        self._SourceProductName = params.get("SourceProductName")
        self._SourceUnitIDList = params.get("SourceUnitIDList")
        self._SourceUnitNameList = params.get("SourceUnitNameList")
        self._SourceDeviceNameList = params.get("SourceDeviceNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecretItem(AbstractModel):
    """Secret信息

    """

    def __init__(self):
        r"""
        :param _Name: Secret名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _SecretType: Secret类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretType: str
        """
        self._Name = None
        self._Namespace = None
        self._CreateTime = None
        self._SecretType = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecretType(self):
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._CreateTime = params.get("CreateTime")
        self._SecretType = params.get("SecretType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityCapabilities(AbstractModel):
    """安全能力

    """

    def __init__(self):
        r"""
        :param _Add: 允许操作列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Add: list of str
        :param _Drop: 禁止操作列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Drop: list of str
        """
        self._Add = None
        self._Drop = None

    @property
    def Add(self):
        return self._Add

    @Add.setter
    def Add(self, Add):
        self._Add = Add

    @property
    def Drop(self):
        return self._Drop

    @Drop.setter
    def Drop(self, Drop):
        self._Drop = Drop


    def _deserialize(self, params):
        self._Add = params.get("Add")
        self._Drop = params.get("Drop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityContext(AbstractModel):
    """安全上下文

    """

    def __init__(self):
        r"""
        :param _Privilege: 是否开启特权模式
        :type Privilege: bool
        :param _ProcMount: 目录/Proc挂载方式
        :type ProcMount: str
        :param _Capabilities: 安全配置
        :type Capabilities: :class:`tencentcloud.iecp.v20210914.models.SecurityCapabilities`
        """
        self._Privilege = None
        self._ProcMount = None
        self._Capabilities = None

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def ProcMount(self):
        return self._ProcMount

    @ProcMount.setter
    def ProcMount(self, ProcMount):
        self._ProcMount = ProcMount

    @property
    def Capabilities(self):
        return self._Capabilities

    @Capabilities.setter
    def Capabilities(self, Capabilities):
        self._Capabilities = Capabilities


    def _deserialize(self, params):
        self._Privilege = params.get("Privilege")
        self._ProcMount = params.get("ProcMount")
        if params.get("Capabilities") is not None:
            self._Capabilities = SecurityCapabilities()
            self._Capabilities._deserialize(params.get("Capabilities"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Service(AbstractModel):
    """服务配置

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Type: 类型 (ClusterIP|NodePort)
        :type Type: str
        :param _Ports: 端口配置
        :type Ports: list of PortConfig
        :param _Labels: 标签
        :type Labels: list of Label
        :param _Namespace: 命名空间默认default
        :type Namespace: str
        :param _ClusterIP: 服务IP
        :type ClusterIP: str
        """
        self._Name = None
        self._Type = None
        self._Ports = None
        self._Labels = None
        self._Namespace = None
        self._ClusterIP = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ClusterIP(self):
        return self._ClusterIP

    @ClusterIP.setter
    def ClusterIP(self, ClusterIP):
        self._ClusterIP = ClusterIP


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Ports") is not None:
            self._Ports = []
            for item in params.get("Ports"):
                obj = PortConfig()
                obj._deserialize(item)
                self._Ports.append(obj)
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._Namespace = params.get("Namespace")
        self._ClusterIP = params.get("ClusterIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRouteOnOffRequest(AbstractModel):
    """SetRouteOnOff请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteID: 无
        :type RouteID: int
        :param _Status: on 或 off
        :type Status: str
        """
        self._RouteID = None
        self._Status = None

    @property
    def RouteID(self):
        return self._RouteID

    @RouteID.setter
    def RouteID(self, RouteID):
        self._RouteID = RouteID

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RouteID = params.get("RouteID")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRouteOnOffResponse(AbstractModel):
    """SetRouteOnOff返回参数结构体

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


class Sort(AbstractModel):
    """查询结果排序条件

    """

    def __init__(self):
        r"""
        :param _Field: 排序字段
        :type Field: str
        :param _Order: 排序方式，升序ASC / 降序DESC
        :type Order: str
        """
        self._Field = None
        self._Order = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcpProbe(AbstractModel):
    """TCP探测配置

    """

    def __init__(self):
        r"""
        :param _Port: 连接端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        """
        self._Port = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Volume(AbstractModel):
    """卷

    """

    def __init__(self):
        r"""
        :param _Source: 来源(emptyDir|hostPath|configMap|secret|nfs)
        :type Source: str
        :param _Name: 名称
        :type Name: str
        :param _HostPath: Host挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HostPath: :class:`tencentcloud.iecp.v20210914.models.VolumeHostPath`
        :param _ConfigMap: ConfigMap挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigMap: :class:`tencentcloud.iecp.v20210914.models.VolumeConfigMap`
        :param _Secret: Secret挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Secret: :class:`tencentcloud.iecp.v20210914.models.VolumeConfigMap`
        :param _NFS: NFS挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NFS: :class:`tencentcloud.iecp.v20210914.models.VolumeNFS`
        """
        self._Source = None
        self._Name = None
        self._HostPath = None
        self._ConfigMap = None
        self._Secret = None
        self._NFS = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def HostPath(self):
        return self._HostPath

    @HostPath.setter
    def HostPath(self, HostPath):
        self._HostPath = HostPath

    @property
    def ConfigMap(self):
        return self._ConfigMap

    @ConfigMap.setter
    def ConfigMap(self, ConfigMap):
        self._ConfigMap = ConfigMap

    @property
    def Secret(self):
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret

    @property
    def NFS(self):
        return self._NFS

    @NFS.setter
    def NFS(self, NFS):
        self._NFS = NFS


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Name = params.get("Name")
        if params.get("HostPath") is not None:
            self._HostPath = VolumeHostPath()
            self._HostPath._deserialize(params.get("HostPath"))
        if params.get("ConfigMap") is not None:
            self._ConfigMap = VolumeConfigMap()
            self._ConfigMap._deserialize(params.get("ConfigMap"))
        if params.get("Secret") is not None:
            self._Secret = VolumeConfigMap()
            self._Secret._deserialize(params.get("Secret"))
        if params.get("NFS") is not None:
            self._NFS = VolumeNFS()
            self._NFS._deserialize(params.get("NFS"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeConfigMap(AbstractModel):
    """ConfigMap挂载卷

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Items: Key列表配置
        :type Items: list of VolumeConfigMapKeyToPath
        """
        self._Name = None
        self._Items = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = VolumeConfigMapKeyToPath()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeConfigMapKeyToPath(AbstractModel):
    """ConfigMap的key挂载到路径

    """

    def __init__(self):
        r"""
        :param _Key: 健名
        :type Key: str
        :param _Path: 对应本地路径
        :type Path: str
        :param _Mode: 对应权限模式
        :type Mode: str
        """
        self._Key = None
        self._Path = None
        self._Mode = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Path = params.get("Path")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeHostPath(AbstractModel):
    """数据卷主机路径，取值参考: https://kubernetes.io/docs/concepts/storage/volumes#hostpath

    """

    def __init__(self):
        r"""
        :param _Type: 类型
        :type Type: str
        :param _Path: 路径
        :type Path: str
        """
        self._Type = None
        self._Path = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeMount(AbstractModel):
    """数据挂载

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _MountPath: 挂载路径
        :type MountPath: str
        :param _SubPath: 子路径
注意：此字段可能返回 null，表示取不到有效值。
        :type SubPath: str
        :param _ReadOnly: 是否只读
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnly: bool
        """
        self._Name = None
        self._MountPath = None
        self._SubPath = None
        self._ReadOnly = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MountPath(self):
        return self._MountPath

    @MountPath.setter
    def MountPath(self, MountPath):
        self._MountPath = MountPath

    @property
    def SubPath(self):
        return self._SubPath

    @SubPath.setter
    def SubPath(self, SubPath):
        self._SubPath = SubPath

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._MountPath = params.get("MountPath")
        self._SubPath = params.get("SubPath")
        self._ReadOnly = params.get("ReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeNFS(AbstractModel):
    """NFS挂载卷

    """

    def __init__(self):
        r"""
        :param _Server: 服务地址
        :type Server: str
        :param _ServerPath: 对应服务器路径
        :type ServerPath: str
        :param _Path: 对应本地路径
        :type Path: str
        """
        self._Server = None
        self._ServerPath = None
        self._Path = None

    @property
    def Server(self):
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server

    @property
    def ServerPath(self):
        return self._ServerPath

    @ServerPath.setter
    def ServerPath(self, ServerPath):
        self._ServerPath = ServerPath

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Server = params.get("Server")
        self._ServerPath = params.get("ServerPath")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        