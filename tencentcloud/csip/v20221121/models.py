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


class AddNewBindRoleUserRequest(AbstractModel):
    """AddNewBindRoleUser请求参数结构体

    """


class AddNewBindRoleUserResponse(AbstractModel):
    """AddNewBindRoleUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0成功，其他失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class AssetBaseInfoResponse(AbstractModel):
    """主机资产详情

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc-id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcName: vpc-name
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _Os: 操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Os: str
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _PrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _AccountNum: 账号数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountNum: int
        :param _PortNum: 端口数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PortNum: int
        :param _ProcessNum: 进程数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessNum: int
        :param _SoftApplicationNum: 软件应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftApplicationNum: int
        :param _DatabaseNum: 数据库数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseNum: int
        :param _WebApplicationNum: Web应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type WebApplicationNum: int
        :param _ServiceNum: 服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceNum: int
        :param _WebFrameworkNum: web框架数量
注意：此字段可能返回 null，表示取不到有效值。
        :type WebFrameworkNum: int
        :param _WebSiteNum: Web站点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type WebSiteNum: int
        :param _JarPackageNum: Jar包数量
注意：此字段可能返回 null，表示取不到有效值。
        :type JarPackageNum: int
        :param _StartServiceNum: 启动服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StartServiceNum: int
        :param _ScheduledTaskNum: 计划任务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduledTaskNum: int
        :param _EnvironmentVariableNum: 环境变量数量
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentVariableNum: int
        :param _KernelModuleNum: 内核模块数量
注意：此字段可能返回 null，表示取不到有效值。
        :type KernelModuleNum: int
        :param _SystemInstallationPackageNum: 系统安装包数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemInstallationPackageNum: int
        :param _SurplusProtectDay: 剩余防护时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SurplusProtectDay: int
        :param _CWPStatus: 客户端是否安装  1 已安装 0 未安装
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPStatus: int
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _ProtectLevel: 防护等级
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectLevel: str
        :param _ProtectedDay: 防护时长
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectedDay: int
        """
        self._VpcId = None
        self._VpcName = None
        self._AssetName = None
        self._Os = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Region = None
        self._AssetType = None
        self._AssetId = None
        self._AccountNum = None
        self._PortNum = None
        self._ProcessNum = None
        self._SoftApplicationNum = None
        self._DatabaseNum = None
        self._WebApplicationNum = None
        self._ServiceNum = None
        self._WebFrameworkNum = None
        self._WebSiteNum = None
        self._JarPackageNum = None
        self._StartServiceNum = None
        self._ScheduledTaskNum = None
        self._EnvironmentVariableNum = None
        self._KernelModuleNum = None
        self._SystemInstallationPackageNum = None
        self._SurplusProtectDay = None
        self._CWPStatus = None
        self._Tag = None
        self._ProtectLevel = None
        self._ProtectedDay = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AccountNum(self):
        return self._AccountNum

    @AccountNum.setter
    def AccountNum(self, AccountNum):
        self._AccountNum = AccountNum

    @property
    def PortNum(self):
        return self._PortNum

    @PortNum.setter
    def PortNum(self, PortNum):
        self._PortNum = PortNum

    @property
    def ProcessNum(self):
        return self._ProcessNum

    @ProcessNum.setter
    def ProcessNum(self, ProcessNum):
        self._ProcessNum = ProcessNum

    @property
    def SoftApplicationNum(self):
        return self._SoftApplicationNum

    @SoftApplicationNum.setter
    def SoftApplicationNum(self, SoftApplicationNum):
        self._SoftApplicationNum = SoftApplicationNum

    @property
    def DatabaseNum(self):
        return self._DatabaseNum

    @DatabaseNum.setter
    def DatabaseNum(self, DatabaseNum):
        self._DatabaseNum = DatabaseNum

    @property
    def WebApplicationNum(self):
        return self._WebApplicationNum

    @WebApplicationNum.setter
    def WebApplicationNum(self, WebApplicationNum):
        self._WebApplicationNum = WebApplicationNum

    @property
    def ServiceNum(self):
        return self._ServiceNum

    @ServiceNum.setter
    def ServiceNum(self, ServiceNum):
        self._ServiceNum = ServiceNum

    @property
    def WebFrameworkNum(self):
        return self._WebFrameworkNum

    @WebFrameworkNum.setter
    def WebFrameworkNum(self, WebFrameworkNum):
        self._WebFrameworkNum = WebFrameworkNum

    @property
    def WebSiteNum(self):
        return self._WebSiteNum

    @WebSiteNum.setter
    def WebSiteNum(self, WebSiteNum):
        self._WebSiteNum = WebSiteNum

    @property
    def JarPackageNum(self):
        return self._JarPackageNum

    @JarPackageNum.setter
    def JarPackageNum(self, JarPackageNum):
        self._JarPackageNum = JarPackageNum

    @property
    def StartServiceNum(self):
        return self._StartServiceNum

    @StartServiceNum.setter
    def StartServiceNum(self, StartServiceNum):
        self._StartServiceNum = StartServiceNum

    @property
    def ScheduledTaskNum(self):
        return self._ScheduledTaskNum

    @ScheduledTaskNum.setter
    def ScheduledTaskNum(self, ScheduledTaskNum):
        self._ScheduledTaskNum = ScheduledTaskNum

    @property
    def EnvironmentVariableNum(self):
        return self._EnvironmentVariableNum

    @EnvironmentVariableNum.setter
    def EnvironmentVariableNum(self, EnvironmentVariableNum):
        self._EnvironmentVariableNum = EnvironmentVariableNum

    @property
    def KernelModuleNum(self):
        return self._KernelModuleNum

    @KernelModuleNum.setter
    def KernelModuleNum(self, KernelModuleNum):
        self._KernelModuleNum = KernelModuleNum

    @property
    def SystemInstallationPackageNum(self):
        return self._SystemInstallationPackageNum

    @SystemInstallationPackageNum.setter
    def SystemInstallationPackageNum(self, SystemInstallationPackageNum):
        self._SystemInstallationPackageNum = SystemInstallationPackageNum

    @property
    def SurplusProtectDay(self):
        return self._SurplusProtectDay

    @SurplusProtectDay.setter
    def SurplusProtectDay(self, SurplusProtectDay):
        self._SurplusProtectDay = SurplusProtectDay

    @property
    def CWPStatus(self):
        return self._CWPStatus

    @CWPStatus.setter
    def CWPStatus(self, CWPStatus):
        self._CWPStatus = CWPStatus

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ProtectLevel(self):
        return self._ProtectLevel

    @ProtectLevel.setter
    def ProtectLevel(self, ProtectLevel):
        self._ProtectLevel = ProtectLevel

    @property
    def ProtectedDay(self):
        return self._ProtectedDay

    @ProtectedDay.setter
    def ProtectedDay(self, ProtectedDay):
        self._ProtectedDay = ProtectedDay


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AssetName = params.get("AssetName")
        self._Os = params.get("Os")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Region = params.get("Region")
        self._AssetType = params.get("AssetType")
        self._AssetId = params.get("AssetId")
        self._AccountNum = params.get("AccountNum")
        self._PortNum = params.get("PortNum")
        self._ProcessNum = params.get("ProcessNum")
        self._SoftApplicationNum = params.get("SoftApplicationNum")
        self._DatabaseNum = params.get("DatabaseNum")
        self._WebApplicationNum = params.get("WebApplicationNum")
        self._ServiceNum = params.get("ServiceNum")
        self._WebFrameworkNum = params.get("WebFrameworkNum")
        self._WebSiteNum = params.get("WebSiteNum")
        self._JarPackageNum = params.get("JarPackageNum")
        self._StartServiceNum = params.get("StartServiceNum")
        self._ScheduledTaskNum = params.get("ScheduledTaskNum")
        self._EnvironmentVariableNum = params.get("EnvironmentVariableNum")
        self._KernelModuleNum = params.get("KernelModuleNum")
        self._SystemInstallationPackageNum = params.get("SystemInstallationPackageNum")
        self._SurplusProtectDay = params.get("SurplusProtectDay")
        self._CWPStatus = params.get("CWPStatus")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._ProtectLevel = params.get("ProtectLevel")
        self._ProtectedDay = params.get("ProtectedDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetClusterPod(AbstractModel):
    """集群pod列表

    """

    def __init__(self):
        r"""
        :param _AppId: 租户id
        :type AppId: int
        :param _Uin: 租户uin
        :type Uin: str
        :param _Nick: 租户昵称
        :type Nick: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _AssetId: pod id
        :type AssetId: str
        :param _AssetName: pod名称
        :type AssetName: str
        :param _InstanceCreateTime: pod创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCreateTime: str
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ClusterId: 集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _MachineId: 主机id
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineId: str
        :param _MachineName: 主机名
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineName: str
        :param _PodIp: pod ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PodIp: str
        :param _ServiceCount: 关联service数
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCount: int
        :param _ContainerCount: 关联容器数
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerCount: int
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _PrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _IsCore: 是否核心：1:核心，2:非核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        """
        self._AppId = None
        self._Uin = None
        self._Nick = None
        self._Region = None
        self._AssetId = None
        self._AssetName = None
        self._InstanceCreateTime = None
        self._Namespace = None
        self._Status = None
        self._ClusterId = None
        self._ClusterName = None
        self._MachineId = None
        self._MachineName = None
        self._PodIp = None
        self._ServiceCount = None
        self._ContainerCount = None
        self._PublicIp = None
        self._PrivateIp = None
        self._IsCore = None

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
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def InstanceCreateTime(self):
        return self._InstanceCreateTime

    @InstanceCreateTime.setter
    def InstanceCreateTime(self, InstanceCreateTime):
        self._InstanceCreateTime = InstanceCreateTime

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
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def MachineId(self):
        return self._MachineId

    @MachineId.setter
    def MachineId(self, MachineId):
        self._MachineId = MachineId

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def PodIp(self):
        return self._PodIp

    @PodIp.setter
    def PodIp(self, PodIp):
        self._PodIp = PodIp

    @property
    def ServiceCount(self):
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def ContainerCount(self):
        return self._ContainerCount

    @ContainerCount.setter
    def ContainerCount(self, ContainerCount):
        self._ContainerCount = ContainerCount

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nick = params.get("Nick")
        self._Region = params.get("Region")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._InstanceCreateTime = params.get("InstanceCreateTime")
        self._Namespace = params.get("Namespace")
        self._Status = params.get("Status")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._MachineId = params.get("MachineId")
        self._MachineName = params.get("MachineName")
        self._PodIp = params.get("PodIp")
        self._ServiceCount = params.get("ServiceCount")
        self._ContainerCount = params.get("ContainerCount")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._IsCore = params.get("IsCore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewPortRisk(AbstractModel):
    """资产视角的端口风险对象

    """

    def __init__(self):
        r"""
        :param _Port: 端口
        :type Port: int
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级
        :type Level: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Component: 组件
        :type Component: str
        :param _Service: 服务
        :type Service: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Suggestion: 处置建议,0保持现状、1限制访问、2封禁端口
        :type Suggestion: int
        :param _Status: 状态，0未处理、1已处置、2已忽略
        :type Status: int
        :param _Id: 资产唯一id
        :type Id: str
        :param _Index: 前端索引
        :type Index: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _From: 来源
        :type From: str
        """
        self._Port = None
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Protocol = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._Suggestion = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._From = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def AffectAsset(self):
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Component(self):
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Protocol = params.get("Protocol")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Suggestion = params.get("Suggestion")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._From = params.get("From")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewVULRisk(AbstractModel):
    """资产视角的漏洞风险对象

    """

    def __init__(self):
        r"""
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级
        :type Level: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Component: 组件
        :type Component: str
        :param _Service: 服务
        :type Service: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Status: 状态，0未处理、1已处置、2已忽略
        :type Status: int
        :param _Id: 资产唯一id
        :type Id: str
        :param _Index: 前端索引
        :type Index: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _Port: 端口
        :type Port: str
        :param _Describe: 描述
        :type Describe: str
        :param _AppName: 版本名
        :type AppName: str
        :param _References: 相关信息
        :type References: str
        :param _AppVersion: 版本
        :type AppVersion: str
        :param _VULURL: 漏洞url
        :type VULURL: str
        :param _VULName: 漏洞名称
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _Fix: 修复建议
        :type Fix: str
        :param _POCId: pocid
        :type POCId: str
        :param _From: 来源
        :type From: str
        :param _CWPVersion: 主机版本
        :type CWPVersion: int
        :param _IsSupportRepair: 是否支持修复
        :type IsSupportRepair: bool
        :param _IsSupportDetect: 是否支持扫描
        :type IsSupportDetect: bool
        :param _InstanceUUID: 实例uuid
        :type InstanceUUID: str
        :param _Payload: 负载
        :type Payload: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :type EMGCVulType: int
        """
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._VULType = None
        self._Port = None
        self._Describe = None
        self._AppName = None
        self._References = None
        self._AppVersion = None
        self._VULURL = None
        self._VULName = None
        self._CVE = None
        self._Fix = None
        self._POCId = None
        self._From = None
        self._CWPVersion = None
        self._IsSupportRepair = None
        self._IsSupportDetect = None
        self._InstanceUUID = None
        self._Payload = None
        self._EMGCVulType = None

    @property
    def AffectAsset(self):
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Component(self):
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VULType(self):
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def References(self):
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def VULName(self):
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Fix(self):
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def POCId(self):
        return self._POCId

    @POCId.setter
    def POCId(self, POCId):
        self._POCId = POCId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CWPVersion(self):
        return self._CWPVersion

    @CWPVersion.setter
    def CWPVersion(self, CWPVersion):
        self._CWPVersion = CWPVersion

    @property
    def IsSupportRepair(self):
        return self._IsSupportRepair

    @IsSupportRepair.setter
    def IsSupportRepair(self, IsSupportRepair):
        self._IsSupportRepair = IsSupportRepair

    @property
    def IsSupportDetect(self):
        return self._IsSupportDetect

    @IsSupportDetect.setter
    def IsSupportDetect(self, IsSupportDetect):
        self._IsSupportDetect = IsSupportDetect

    @property
    def InstanceUUID(self):
        return self._InstanceUUID

    @InstanceUUID.setter
    def InstanceUUID(self, InstanceUUID):
        self._InstanceUUID = InstanceUUID

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def EMGCVulType(self):
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._VULType = params.get("VULType")
        self._Port = params.get("Port")
        self._Describe = params.get("Describe")
        self._AppName = params.get("AppName")
        self._References = params.get("References")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Fix = params.get("Fix")
        self._POCId = params.get("POCId")
        self._From = params.get("From")
        self._CWPVersion = params.get("CWPVersion")
        self._IsSupportRepair = params.get("IsSupportRepair")
        self._IsSupportDetect = params.get("IsSupportDetect")
        self._InstanceUUID = params.get("InstanceUUID")
        self._Payload = params.get("Payload")
        self._EMGCVulType = params.get("EMGCVulType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CVMAssetVO(AbstractModel):
    """主机资产信息

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _CWPStatus: 防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPStatus: int
        :param _AssetCreateTime: 资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _PrivateIp: 私网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcName: vpc 名
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _AppId: appid信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _NickName: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _AvailableArea: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableArea: str
        :param _IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param _SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _SubnetName: 子网名
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param _InstanceUuid: uuid
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceUuid: str
        :param _InstanceQUuid: qquid
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceQUuid: str
        :param _OsName: os名
注意：此字段可能返回 null，表示取不到有效值。
        :type OsName: str
        :param _PartitionCount: 分区
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionCount: int
        :param _CPUInfo: cpu信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CPUInfo: str
        :param _CPUSize: cpu大小
注意：此字段可能返回 null，表示取不到有效值。
        :type CPUSize: int
        :param _CPULoad: cpu负载
注意：此字段可能返回 null，表示取不到有效值。
        :type CPULoad: str
        :param _MemorySize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemorySize: str
        :param _MemoryLoad: 内存负载
注意：此字段可能返回 null，表示取不到有效值。
        :type MemoryLoad: str
        :param _DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: str
        :param _DiskLoad: 硬盘负载
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskLoad: str
        :param _AccountCount: 账号数
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountCount: str
        :param _ProcessCount: 进程数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessCount: str
        :param _AppCount: 软件应用
注意：此字段可能返回 null，表示取不到有效值。
        :type AppCount: str
        :param _PortCount: 监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type PortCount: int
        :param _Attack: 网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type Attack: int
        :param _Access: 网络访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Access: int
        :param _Intercept: 网络拦截
注意：此字段可能返回 null，表示取不到有效值。
        :type Intercept: int
        :param _InBandwidth: 入向峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InBandwidth: str
        :param _OutBandwidth: 出向峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type OutBandwidth: str
        :param _InFlow: 入向累计流量
注意：此字段可能返回 null，表示取不到有效值。
        :type InFlow: str
        :param _OutFlow: 出向累计流量
注意：此字段可能返回 null，表示取不到有效值。
        :type OutFlow: str
        :param _LastScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param _NetWorkOut: 恶意主动外联
注意：此字段可能返回 null，表示取不到有效值。
        :type NetWorkOut: int
        :param _PortRisk: 端口风险
注意：此字段可能返回 null，表示取不到有效值。
        :type PortRisk: int
        :param _VulnerabilityRisk: 漏洞风险
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: 配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigurationRisk: int
        :param _ScanTask: 扫描任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTask: int
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _MemberId: memberId
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberId: str
        :param _Os: os全称
注意：此字段可能返回 null，表示取不到有效值。
        :type Os: str
        :param _RiskExposure: 风险服务暴露
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskExposure: int
        :param _BASAgentStatus: 模拟攻击工具状态。0代表未安装，1代表已安装，2代表已离线
注意：此字段可能返回 null，表示取不到有效值。
        :type BASAgentStatus: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._CWPStatus = None
        self._AssetCreateTime = None
        self._PublicIp = None
        self._PrivateIp = None
        self._VpcId = None
        self._VpcName = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._AvailableArea = None
        self._IsCore = None
        self._SubnetId = None
        self._SubnetName = None
        self._InstanceUuid = None
        self._InstanceQUuid = None
        self._OsName = None
        self._PartitionCount = None
        self._CPUInfo = None
        self._CPUSize = None
        self._CPULoad = None
        self._MemorySize = None
        self._MemoryLoad = None
        self._DiskSize = None
        self._DiskLoad = None
        self._AccountCount = None
        self._ProcessCount = None
        self._AppCount = None
        self._PortCount = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._NetWorkOut = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._Tag = None
        self._MemberId = None
        self._Os = None
        self._RiskExposure = None
        self._BASAgentStatus = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CWPStatus(self):
        return self._CWPStatus

    @CWPStatus.setter
    def CWPStatus(self, CWPStatus):
        self._CWPStatus = CWPStatus

    @property
    def AssetCreateTime(self):
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

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
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def AvailableArea(self):
        return self._AvailableArea

    @AvailableArea.setter
    def AvailableArea(self, AvailableArea):
        self._AvailableArea = AvailableArea

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def InstanceUuid(self):
        return self._InstanceUuid

    @InstanceUuid.setter
    def InstanceUuid(self, InstanceUuid):
        self._InstanceUuid = InstanceUuid

    @property
    def InstanceQUuid(self):
        return self._InstanceQUuid

    @InstanceQUuid.setter
    def InstanceQUuid(self, InstanceQUuid):
        self._InstanceQUuid = InstanceQUuid

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def PartitionCount(self):
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def CPUInfo(self):
        return self._CPUInfo

    @CPUInfo.setter
    def CPUInfo(self, CPUInfo):
        self._CPUInfo = CPUInfo

    @property
    def CPUSize(self):
        return self._CPUSize

    @CPUSize.setter
    def CPUSize(self, CPUSize):
        self._CPUSize = CPUSize

    @property
    def CPULoad(self):
        return self._CPULoad

    @CPULoad.setter
    def CPULoad(self, CPULoad):
        self._CPULoad = CPULoad

    @property
    def MemorySize(self):
        return self._MemorySize

    @MemorySize.setter
    def MemorySize(self, MemorySize):
        self._MemorySize = MemorySize

    @property
    def MemoryLoad(self):
        return self._MemoryLoad

    @MemoryLoad.setter
    def MemoryLoad(self, MemoryLoad):
        self._MemoryLoad = MemoryLoad

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskLoad(self):
        return self._DiskLoad

    @DiskLoad.setter
    def DiskLoad(self, DiskLoad):
        self._DiskLoad = DiskLoad

    @property
    def AccountCount(self):
        return self._AccountCount

    @AccountCount.setter
    def AccountCount(self, AccountCount):
        self._AccountCount = AccountCount

    @property
    def ProcessCount(self):
        return self._ProcessCount

    @ProcessCount.setter
    def ProcessCount(self, ProcessCount):
        self._ProcessCount = ProcessCount

    @property
    def AppCount(self):
        return self._AppCount

    @AppCount.setter
    def AppCount(self, AppCount):
        self._AppCount = AppCount

    @property
    def PortCount(self):
        return self._PortCount

    @PortCount.setter
    def PortCount(self, PortCount):
        self._PortCount = PortCount

    @property
    def Attack(self):
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def NetWorkOut(self):
        return self._NetWorkOut

    @NetWorkOut.setter
    def NetWorkOut(self, NetWorkOut):
        self._NetWorkOut = NetWorkOut

    @property
    def PortRisk(self):
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def RiskExposure(self):
        return self._RiskExposure

    @RiskExposure.setter
    def RiskExposure(self, RiskExposure):
        self._RiskExposure = RiskExposure

    @property
    def BASAgentStatus(self):
        return self._BASAgentStatus

    @BASAgentStatus.setter
    def BASAgentStatus(self, BASAgentStatus):
        self._BASAgentStatus = BASAgentStatus


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._CWPStatus = params.get("CWPStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._AvailableArea = params.get("AvailableArea")
        self._IsCore = params.get("IsCore")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._InstanceUuid = params.get("InstanceUuid")
        self._InstanceQUuid = params.get("InstanceQUuid")
        self._OsName = params.get("OsName")
        self._PartitionCount = params.get("PartitionCount")
        self._CPUInfo = params.get("CPUInfo")
        self._CPUSize = params.get("CPUSize")
        self._CPULoad = params.get("CPULoad")
        self._MemorySize = params.get("MemorySize")
        self._MemoryLoad = params.get("MemoryLoad")
        self._DiskSize = params.get("DiskSize")
        self._DiskLoad = params.get("DiskLoad")
        self._AccountCount = params.get("AccountCount")
        self._ProcessCount = params.get("ProcessCount")
        self._AppCount = params.get("AppCount")
        self._PortCount = params.get("PortCount")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._NetWorkOut = params.get("NetWorkOut")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._MemberId = params.get("MemberId")
        self._Os = params.get("Os")
        self._RiskExposure = params.get("RiskExposure")
        self._BASAgentStatus = params.get("BASAgentStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAndIpRequest(AbstractModel):
    """CreateDomainAndIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: -
        :type Content: list of str
        """
        self._Content = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAndIpResponse(AbstractModel):
    """CreateDomainAndIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回创建成功的数量
        :type Data: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class CreateRiskCenterScanTaskRequest(AbstractModel):
    """CreateRiskCenterScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _ScanAssetType: 0-全扫，1-指定资产扫，2-排除资产扫，3-手动填写扫；1和2则Assets字段必填，3则SelfDefiningAssets必填
        :type ScanAssetType: int
        :param _ScanItem: 扫描项目；port/poc/weakpass/webcontent/configrisk
        :type ScanItem: list of str
        :param _ScanPlanType: 0-周期任务,1-立即扫描,2-定时扫描,3-自定义；0,2,3则ScanPlanContent必填
        :type ScanPlanType: int
        :param _Assets: 扫描资产信息列表
        :type Assets: list of TaskAssetObject
        :param _ScanPlanContent: 扫描计划详情
        :type ScanPlanContent: str
        :param _SelfDefiningAssets: ip/域名/url数组
        :type SelfDefiningAssets: list of str
        :param _TaskAdvanceCFG: 高级配置
        :type TaskAdvanceCFG: :class:`tencentcloud.csip.v20221121.models.TaskAdvanceCFG`
        :param _TaskMode: 体检模式，0-标准模式，1-快速模式，2-高级模式，默认标准模式
        :type TaskMode: int
        """
        self._TaskName = None
        self._ScanAssetType = None
        self._ScanItem = None
        self._ScanPlanType = None
        self._Assets = None
        self._ScanPlanContent = None
        self._SelfDefiningAssets = None
        self._TaskAdvanceCFG = None
        self._TaskMode = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ScanAssetType(self):
        return self._ScanAssetType

    @ScanAssetType.setter
    def ScanAssetType(self, ScanAssetType):
        self._ScanAssetType = ScanAssetType

    @property
    def ScanItem(self):
        return self._ScanItem

    @ScanItem.setter
    def ScanItem(self, ScanItem):
        self._ScanItem = ScanItem

    @property
    def ScanPlanType(self):
        return self._ScanPlanType

    @ScanPlanType.setter
    def ScanPlanType(self, ScanPlanType):
        self._ScanPlanType = ScanPlanType

    @property
    def Assets(self):
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

    @property
    def ScanPlanContent(self):
        return self._ScanPlanContent

    @ScanPlanContent.setter
    def ScanPlanContent(self, ScanPlanContent):
        self._ScanPlanContent = ScanPlanContent

    @property
    def SelfDefiningAssets(self):
        return self._SelfDefiningAssets

    @SelfDefiningAssets.setter
    def SelfDefiningAssets(self, SelfDefiningAssets):
        self._SelfDefiningAssets = SelfDefiningAssets

    @property
    def TaskAdvanceCFG(self):
        return self._TaskAdvanceCFG

    @TaskAdvanceCFG.setter
    def TaskAdvanceCFG(self, TaskAdvanceCFG):
        self._TaskAdvanceCFG = TaskAdvanceCFG

    @property
    def TaskMode(self):
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._ScanAssetType = params.get("ScanAssetType")
        self._ScanItem = params.get("ScanItem")
        self._ScanPlanType = params.get("ScanPlanType")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = TaskAssetObject()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._ScanPlanContent = params.get("ScanPlanContent")
        self._SelfDefiningAssets = params.get("SelfDefiningAssets")
        if params.get("TaskAdvanceCFG") is not None:
            self._TaskAdvanceCFG = TaskAdvanceCFG()
            self._TaskAdvanceCFG._deserialize(params.get("TaskAdvanceCFG"))
        self._TaskMode = params.get("TaskMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRiskCenterScanTaskResponse(AbstractModel):
    """CreateRiskCenterScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
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


class DBAssetVO(AbstractModel):
    """db资产输出字段

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _VpcId: vpcid
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcName: vpc标签
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _AssetCreateTime: 资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param _LastScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param _ConfigurationRisk: 配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigurationRisk: int
        :param _Attack: 网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type Attack: int
        :param _Access: 网络访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Access: int
        :param _ScanTask: 扫描任务
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTask: int
        :param _AppId: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _NickName: 昵称别名
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _PrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._VpcId = None
        self._VpcName = None
        self._Region = None
        self._Domain = None
        self._AssetCreateTime = None
        self._LastScanTime = None
        self._ConfigurationRisk = None
        self._Attack = None
        self._Access = None
        self._ScanTask = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._Port = None
        self._Tag = None
        self._PrivateIp = None
        self._PublicIp = None
        self._Status = None
        self._IsCore = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AssetCreateTime(self):
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def ConfigurationRisk(self):
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def Attack(self):
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

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
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._Region = params.get("Region")
        self._Domain = params.get("Domain")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._LastScanTime = params.get("LastScanTime")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._ScanTask = params.get("ScanTask")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._Port = params.get("Port")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._Status = params.get("Status")
        self._IsCore = params.get("IsCore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbAssetInfo(AbstractModel):
    """db资产详情

    """

    def __init__(self):
        r"""
        :param _CFWStatus: 云防状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CFWStatus: int
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _VpcName: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _PrivateIp: 私网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _VpcId: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _CFWProtectLevel: 云防保护版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CFWProtectLevel: int
        :param _Tag: tag信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        """
        self._CFWStatus = None
        self._AssetId = None
        self._VpcName = None
        self._AssetType = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Region = None
        self._VpcId = None
        self._AssetName = None
        self._CFWProtectLevel = None
        self._Tag = None

    @property
    def CFWStatus(self):
        return self._CFWStatus

    @CFWStatus.setter
    def CFWStatus(self, CFWStatus):
        self._CFWStatus = CFWStatus

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

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
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def CFWProtectLevel(self):
        return self._CFWProtectLevel

    @CFWProtectLevel.setter
    def CFWProtectLevel(self, CFWProtectLevel):
        self._CFWProtectLevel = CFWProtectLevel

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._CFWStatus = params.get("CFWStatus")
        self._AssetId = params.get("AssetId")
        self._VpcName = params.get("VpcName")
        self._AssetType = params.get("AssetType")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._AssetName = params.get("AssetName")
        self._CFWProtectLevel = params.get("CFWProtectLevel")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetInfoRequest(AbstractModel):
    """DescribeCVMAssetInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: -
        :type AssetId: str
        """
        self._AssetId = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetInfoResponse(AbstractModel):
    """DescribeCVMAssetInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.csip.v20221121.models.AssetBaseInfoResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AssetBaseInfoResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCVMAssetsRequest(AbstractModel):
    """DescribeCVMAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: -
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetsResponse(AbstractModel):
    """DescribeCVMAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Data: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CVMAssetVO
        :param _RegionList: 地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionList: list of FilterDataObject
        :param _DefenseStatusList: 防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseStatusList: list of FilterDataObject
        :param _VpcList: vpc枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcList: list of FilterDataObject
        :param _AssetTypeList: 资产类型枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTypeList: list of FilterDataObject
        :param _SystemTypeList: 操作系统枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemTypeList: list of FilterDataObject
        :param _IpTypeList: ip列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IpTypeList: list of FilterDataObject
        :param _AppIdList: appid列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AppIdList: list of FilterDataObject
        :param _ZoneList: 可用区列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneList: list of FilterDataObject
        :param _OsList: os列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OsList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RegionList = None
        self._DefenseStatusList = None
        self._VpcList = None
        self._AssetTypeList = None
        self._SystemTypeList = None
        self._IpTypeList = None
        self._AppIdList = None
        self._ZoneList = None
        self._OsList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def DefenseStatusList(self):
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AssetTypeList(self):
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def SystemTypeList(self):
        return self._SystemTypeList

    @SystemTypeList.setter
    def SystemTypeList(self, SystemTypeList):
        self._SystemTypeList = SystemTypeList

    @property
    def IpTypeList(self):
        return self._IpTypeList

    @IpTypeList.setter
    def IpTypeList(self, IpTypeList):
        self._IpTypeList = IpTypeList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def ZoneList(self):
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def OsList(self):
        return self._OsList

    @OsList.setter
    def OsList(self, OsList):
        self._OsList = OsList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CVMAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("SystemTypeList") is not None:
            self._SystemTypeList = []
            for item in params.get("SystemTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SystemTypeList.append(obj)
        if params.get("IpTypeList") is not None:
            self._IpTypeList = []
            for item in params.get("IpTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._IpTypeList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        if params.get("OsList") is not None:
            self._OsList = []
            for item in params.get("OsList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._OsList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterPodAssetsRequest(AbstractModel):
    """DescribeClusterPodAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterPodAssetsResponse(AbstractModel):
    """DescribeClusterPodAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of AssetClusterPod
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _PodStatusList: 集群pod状态枚举
        :type PodStatusList: list of FilterDataObject
        :param _NamespaceList: 命名空间枚举
        :type NamespaceList: list of FilterDataObject
        :param _RegionList: 地域枚举
        :type RegionList: list of FilterDataObject
        :param _AppIdList: 租户枚举
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._PodStatusList = None
        self._NamespaceList = None
        self._RegionList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PodStatusList(self):
        return self._PodStatusList

    @PodStatusList.setter
    def PodStatusList(self, PodStatusList):
        self._PodStatusList = PodStatusList

    @property
    def NamespaceList(self):
        return self._NamespaceList

    @NamespaceList.setter
    def NamespaceList(self, NamespaceList):
        self._NamespaceList = NamespaceList

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetClusterPod()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("PodStatusList") is not None:
            self._PodStatusList = []
            for item in params.get("PodStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._PodStatusList.append(obj)
        if params.get("NamespaceList") is not None:
            self._NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._NamespaceList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDbAssetInfoRequest(AbstractModel):
    """DescribeDbAssetInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
        :type AssetId: str
        """
        self._AssetId = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbAssetInfoResponse(AbstractModel):
    """DescribeDbAssetInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: db资产详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.csip.v20221121.models.DbAssetInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DbAssetInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDbAssetsRequest(AbstractModel):
    """DescribeDbAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: -
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbAssetsResponse(AbstractModel):
    """DescribeDbAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Data: 资产总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DBAssetVO
        :param _RegionList: 地域枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: 资产类型枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: Vpc枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcList: list of FilterDataObject
        :param _AppIdList: Appid枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DBAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainAssetsRequest(AbstractModel):
    """DescribeDomainAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: -
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainAssetsResponse(AbstractModel):
    """DescribeDomainAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Data: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DomainAssetVO
        :param _DefenseStatusList: 防护状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseStatusList: list of FilterDataObject
        :param _AssetLocationList: 资产归属地列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetLocationList: list of FilterDataObject
        :param _SourceTypeList: 资产类型列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceTypeList: list of FilterDataObject
        :param _RegionList: 地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._DefenseStatusList = None
        self._AssetLocationList = None
        self._SourceTypeList = None
        self._RegionList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DefenseStatusList(self):
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def AssetLocationList(self):
        return self._AssetLocationList

    @AssetLocationList.setter
    def AssetLocationList(self, AssetLocationList):
        self._AssetLocationList = AssetLocationList

    @property
    def SourceTypeList(self):
        return self._SourceTypeList

    @SourceTypeList.setter
    def SourceTypeList(self, SourceTypeList):
        self._SourceTypeList = SourceTypeList

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DomainAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("AssetLocationList") is not None:
            self._AssetLocationList = []
            for item in params.get("AssetLocationList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetLocationList.append(obj)
        if params.get("SourceTypeList") is not None:
            self._SourceTypeList = []
            for item in params.get("SourceTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SourceTypeList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePublicIpAssetsRequest(AbstractModel):
    """DescribePublicIpAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: filte过滤条件
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicIpAssetsResponse(AbstractModel):
    """DescribePublicIpAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of IpAssetListVO
        :param _Total: 总数
        :type Total: int
        :param _AssetLocationList: 资产归属地
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetLocationList: list of FilterDataObject
        :param _IpTypeList: ip列表枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type IpTypeList: list of FilterDataObject
        :param _RegionList: 地域列表枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionList: list of FilterDataObject
        :param _DefenseStatusList: 防护枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseStatusList: list of FilterDataObject
        :param _AssetTypeList: 资产类型枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTypeList: list of FilterDataObject
        :param _AppIdList: AppId枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._AssetLocationList = None
        self._IpTypeList = None
        self._RegionList = None
        self._DefenseStatusList = None
        self._AssetTypeList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AssetLocationList(self):
        return self._AssetLocationList

    @AssetLocationList.setter
    def AssetLocationList(self, AssetLocationList):
        self._AssetLocationList = AssetLocationList

    @property
    def IpTypeList(self):
        return self._IpTypeList

    @IpTypeList.setter
    def IpTypeList(self, IpTypeList):
        self._IpTypeList = IpTypeList

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def DefenseStatusList(self):
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def AssetTypeList(self):
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = IpAssetListVO()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        if params.get("AssetLocationList") is not None:
            self._AssetLocationList = []
            for item in params.get("AssetLocationList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetLocationList.append(obj)
        if params.get("IpTypeList") is not None:
            self._IpTypeList = []
            for item in params.get("IpTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._IpTypeList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewPortRiskListRequest(AbstractModel):
    """DescribeRiskCenterAssetViewPortRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewPortRiskListResponse(AbstractModel):
    """DescribeRiskCenterAssetViewPortRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 资产视角的配置风险列表
        :type Data: list of AssetViewPortRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _SuggestionLists: 建议列表
        :type SuggestionLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._SuggestionLists = None
        self._InstanceTypeLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def SuggestionLists(self):
        return self._SuggestionLists

    @SuggestionLists.setter
    def SuggestionLists(self, SuggestionLists):
        self._SuggestionLists = SuggestionLists

    @property
    def InstanceTypeLists(self):
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def FromLists(self):
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewPortRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("SuggestionLists") is not None:
            self._SuggestionLists = []
            for item in params.get("SuggestionLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SuggestionLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewVULRiskListRequest(AbstractModel):
    """DescribeRiskCenterAssetViewVULRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewVULRiskListResponse(AbstractModel):
    """DescribeRiskCenterAssetViewVULRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 资产视角的漏洞风险列表
        :type Data: list of AssetViewVULRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: 漏洞类型列表
        :type VULTypeLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._InstanceTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def InstanceTypeLists(self):
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewVULRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScanReportListRequest(AbstractModel):
    """DescribeScanReportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 列表过滤条件
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanReportListResponse(AbstractModel):
    """DescribeScanReportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 任务日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ScanTaskInfo
        :param _UINList: 主账户ID列表
        :type UINList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._UINList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def UINList(self):
        return self._UINList

    @UINList.setter
    def UINList(self, UINList):
        self._UINList = UINList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ScanTaskInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._UINList = params.get("UINList")
        self._RequestId = params.get("RequestId")


class DescribeSubnetAssetsRequest(AbstractModel):
    """DescribeSubnetAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetAssetsResponse(AbstractModel):
    """DescribeSubnetAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of SubnetAsset
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param _AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param _ZoneList: 可用区列表
        :type ZoneList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RegionList = None
        self._VpcList = None
        self._AppIdList = None
        self._ZoneList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def ZoneList(self):
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubnetAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVpcAssetsRequest(AbstractModel):
    """DescribeVpcAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcAssetsResponse(AbstractModel):
    """DescribeVpcAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of Vpc
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._VpcList = None
        self._RegionList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Vpc()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DomainAssetVO(AbstractModel):
    """域名资产

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: list of str
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: list of str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: list of str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: list of str
        :param _WAFStatus: Waf状态
注意：此字段可能返回 null，表示取不到有效值。
        :type WAFStatus: int
        :param _AssetCreateTime: 资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param _AppId: Appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 账号id
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _NickName: 账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param _IsCloud: 是否云上资产
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCloud: int
        :param _Attack: 网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type Attack: int
        :param _Access: 网络访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Access: int
        :param _Intercept: 网络拦截
注意：此字段可能返回 null，表示取不到有效值。
        :type Intercept: int
        :param _InBandwidth: 入站峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InBandwidth: str
        :param _OutBandwidth: 出站峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type OutBandwidth: str
        :param _InFlow: 入站累计流量
注意：此字段可能返回 null，表示取不到有效值。
        :type InFlow: str
        :param _OutFlow: 出站累计流量
注意：此字段可能返回 null，表示取不到有效值。
        :type OutFlow: str
        :param _LastScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param _PortRisk: 端口风险
注意：此字段可能返回 null，表示取不到有效值。
        :type PortRisk: int
        :param _VulnerabilityRisk: 漏洞风险
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: 配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigurationRisk: int
        :param _ScanTask: 扫描任务
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTask: int
        :param _SubDomain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type SubDomain: str
        :param _SeverIp: 解析ip
注意：此字段可能返回 null，表示取不到有效值。
        :type SeverIp: list of str
        :param _BotCount: boi访问数量
注意：此字段可能返回 null，表示取不到有效值。
        :type BotCount: int
        :param _WeakPassword: 弱口令风险
注意：此字段可能返回 null，表示取不到有效值。
        :type WeakPassword: int
        :param _WebContentRisk: 内容风险
注意：此字段可能返回 null，表示取不到有效值。
        :type WebContentRisk: int
        :param _Tag: tag标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _SourceType: 关联实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: str
        :param _MemberId: memberiD
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberId: str
        :param _CCAttack: cc攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type CCAttack: int
        :param _WebAttack: web攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type WebAttack: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._WAFStatus = None
        self._AssetCreateTime = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._IsCore = None
        self._IsCloud = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._SubDomain = None
        self._SeverIp = None
        self._BotCount = None
        self._WeakPassword = None
        self._WebContentRisk = None
        self._Tag = None
        self._SourceType = None
        self._MemberId = None
        self._CCAttack = None
        self._WebAttack = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def WAFStatus(self):
        return self._WAFStatus

    @WAFStatus.setter
    def WAFStatus(self, WAFStatus):
        self._WAFStatus = WAFStatus

    @property
    def AssetCreateTime(self):
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

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
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsCloud(self):
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def Attack(self):
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def PortRisk(self):
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def SeverIp(self):
        return self._SeverIp

    @SeverIp.setter
    def SeverIp(self, SeverIp):
        self._SeverIp = SeverIp

    @property
    def BotCount(self):
        return self._BotCount

    @BotCount.setter
    def BotCount(self, BotCount):
        self._BotCount = BotCount

    @property
    def WeakPassword(self):
        return self._WeakPassword

    @WeakPassword.setter
    def WeakPassword(self, WeakPassword):
        self._WeakPassword = WeakPassword

    @property
    def WebContentRisk(self):
        return self._WebContentRisk

    @WebContentRisk.setter
    def WebContentRisk(self, WebContentRisk):
        self._WebContentRisk = WebContentRisk

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def CCAttack(self):
        return self._CCAttack

    @CCAttack.setter
    def CCAttack(self, CCAttack):
        self._CCAttack = CCAttack

    @property
    def WebAttack(self):
        return self._WebAttack

    @WebAttack.setter
    def WebAttack(self, WebAttack):
        self._WebAttack = WebAttack


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._WAFStatus = params.get("WAFStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._IsCore = params.get("IsCore")
        self._IsCloud = params.get("IsCloud")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        self._SubDomain = params.get("SubDomain")
        self._SeverIp = params.get("SeverIp")
        self._BotCount = params.get("BotCount")
        self._WeakPassword = params.get("WeakPassword")
        self._WebContentRisk = params.get("WebContentRisk")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._SourceType = params.get("SourceType")
        self._MemberId = params.get("MemberId")
        self._CCAttack = params.get("CCAttack")
        self._WebAttack = params.get("WebAttack")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """列表查询接口采用新filter 接口，直接传给后台供后台查询过滤

    """

    def __init__(self):
        r"""
        :param _Limit: 查询数量限制
        :type Limit: int
        :param _Offset: 查询偏移位置
        :type Offset: int
        :param _Order: 排序采用升序还是降序 升:asc 降 desc
        :type Order: str
        :param _By: 需排序的字段
        :type By: str
        :param _Filters: 过滤的列及内容
        :type Filters: list of WhereFilter
        :param _StartTime: 可填无， 日志使用查询时间
        :type StartTime: str
        :param _EndTime: 可填无， 日志使用查询时间
        :type EndTime: str
        """
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = WhereFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterDataObject(AbstractModel):
    """过滤数据对象

    """

    def __init__(self):
        r"""
        :param _Value: 英文翻译
        :type Value: str
        :param _Text: 中文翻译
        :type Text: str
        """
        self._Value = None
        self._Text = None

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Value = params.get("Value")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpAssetListVO(AbstractModel):
    """ip列表

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _AssetName: 资产name
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _CFWStatus: 云防状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CFWStatus: int
        :param _AssetCreateTime: 资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _PublicIpType: 公网ip类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpType: int
        :param _VpcId: vpc
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcName: vpc名
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _AppId: appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _NickName: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _IsCore: 核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param _IsCloud: 云上
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCloud: int
        :param _Attack: 网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type Attack: int
        :param _Access: 网络访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Access: int
        :param _Intercept: 网络拦截
注意：此字段可能返回 null，表示取不到有效值。
        :type Intercept: int
        :param _InBandwidth: 入向带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InBandwidth: str
        :param _OutBandwidth: 出向带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type OutBandwidth: str
        :param _InFlow: 入向流量
注意：此字段可能返回 null，表示取不到有效值。
        :type InFlow: str
        :param _OutFlow: 出向流量
注意：此字段可能返回 null，表示取不到有效值。
        :type OutFlow: str
        :param _LastScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param _PortRisk: 端口风险
注意：此字段可能返回 null，表示取不到有效值。
        :type PortRisk: int
        :param _VulnerabilityRisk: 漏洞风险
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: 配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigurationRisk: int
        :param _ScanTask: 扫描任务
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTask: int
        :param _WeakPassword: 弱口令
注意：此字段可能返回 null，表示取不到有效值。
        :type WeakPassword: int
        :param _WebContentRisk: 内容风险
注意：此字段可能返回 null，表示取不到有效值。
        :type WebContentRisk: int
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _AddressId: eip主键
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressId: str
        :param _MemberId: memberid信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberId: str
        :param _RiskExposure: 风险服务暴露
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskExposure: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._CFWStatus = None
        self._AssetCreateTime = None
        self._PublicIp = None
        self._PublicIpType = None
        self._VpcId = None
        self._VpcName = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._IsCore = None
        self._IsCloud = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._WeakPassword = None
        self._WebContentRisk = None
        self._Tag = None
        self._AddressId = None
        self._MemberId = None
        self._RiskExposure = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CFWStatus(self):
        return self._CFWStatus

    @CFWStatus.setter
    def CFWStatus(self, CFWStatus):
        self._CFWStatus = CFWStatus

    @property
    def AssetCreateTime(self):
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PublicIpType(self):
        return self._PublicIpType

    @PublicIpType.setter
    def PublicIpType(self, PublicIpType):
        self._PublicIpType = PublicIpType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

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
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsCloud(self):
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def Attack(self):
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def PortRisk(self):
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def WeakPassword(self):
        return self._WeakPassword

    @WeakPassword.setter
    def WeakPassword(self, WeakPassword):
        self._WeakPassword = WeakPassword

    @property
    def WebContentRisk(self):
        return self._WebContentRisk

    @WebContentRisk.setter
    def WebContentRisk(self, WebContentRisk):
        self._WebContentRisk = WebContentRisk

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def AddressId(self):
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def RiskExposure(self):
        return self._RiskExposure

    @RiskExposure.setter
    def RiskExposure(self, RiskExposure):
        self._RiskExposure = RiskExposure


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._CFWStatus = params.get("CFWStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._PublicIp = params.get("PublicIp")
        self._PublicIpType = params.get("PublicIpType")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._IsCore = params.get("IsCore")
        self._IsCloud = params.get("IsCloud")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        self._WeakPassword = params.get("WeakPassword")
        self._WebContentRisk = params.get("WebContentRisk")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._AddressId = params.get("AddressId")
        self._MemberId = params.get("MemberId")
        self._RiskExposure = params.get("RiskExposure")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskInfo(AbstractModel):
    """扫描任务详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务日志Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: 任务日志名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _Status: 任务状态码：1等待开始  2正在扫描  3扫描出错 4扫描完成
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Progress: 任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param _TaskTime: 对应的展示时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTime: str
        :param _ReportId: 报表id
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportId: str
        :param _ReportName: 报表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportName: str
        :param _ScanPlan: 扫描计划，0-周期任务,1-立即扫描,2-定时扫描,3-自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanPlan: int
        :param _AssetCount: 关联的资产数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCount: int
        :param _AppId: APP ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _UIN: 用户主账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UIN: str
        :param _UserName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        """
        self._TaskId = None
        self._TaskName = None
        self._Status = None
        self._Progress = None
        self._TaskTime = None
        self._ReportId = None
        self._ReportName = None
        self._ScanPlan = None
        self._AssetCount = None
        self._AppId = None
        self._UIN = None
        self._UserName = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskTime(self):
        return self._TaskTime

    @TaskTime.setter
    def TaskTime(self, TaskTime):
        self._TaskTime = TaskTime

    @property
    def ReportId(self):
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def ReportName(self):
        return self._ReportName

    @ReportName.setter
    def ReportName(self, ReportName):
        self._ReportName = ReportName

    @property
    def ScanPlan(self):
        return self._ScanPlan

    @ScanPlan.setter
    def ScanPlan(self, ScanPlan):
        self._ScanPlan = ScanPlan

    @property
    def AssetCount(self):
        return self._AssetCount

    @AssetCount.setter
    def AssetCount(self, AssetCount):
        self._AssetCount = AssetCount

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UIN(self):
        return self._UIN

    @UIN.setter
    def UIN(self, UIN):
        self._UIN = UIN

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._TaskTime = params.get("TaskTime")
        self._ReportId = params.get("ReportId")
        self._ReportName = params.get("ReportName")
        self._ScanPlan = params.get("ScanPlan")
        self._AssetCount = params.get("AssetCount")
        self._AppId = params.get("AppId")
        self._UIN = params.get("UIN")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetAsset(AbstractModel):
    """子网资产

    """

    def __init__(self):
        r"""
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _AssetId: 资产ID
        :type AssetId: str
        :param _AssetName: 资产名
        :type AssetName: str
        :param _Region: 区域
        :type Region: str
        :param _VpcId: 私有网络id
        :type VpcId: str
        :param _VpcName: 私有网络名
        :type VpcName: str
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _Nick: 昵称
        :type Nick: str
        :param _CIDR: cidr
        :type CIDR: str
        :param _Zone: 可用区
        :type Zone: str
        :param _CVM: cvm数
        :type CVM: int
        :param _AvailableIp: 可用ip数
        :type AvailableIp: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ConfigureRisk: 配置风险
        :type ConfigureRisk: int
        :param _ScanTask: 任务数
        :type ScanTask: int
        :param _LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param _IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        """
        self._AppId = None
        self._Uin = None
        self._AssetId = None
        self._AssetName = None
        self._Region = None
        self._VpcId = None
        self._VpcName = None
        self._Tag = None
        self._Nick = None
        self._CIDR = None
        self._Zone = None
        self._CVM = None
        self._AvailableIp = None
        self._CreateTime = None
        self._ConfigureRisk = None
        self._ScanTask = None
        self._LastScanTime = None
        self._IsCore = None

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
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

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
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def CIDR(self):
        return self._CIDR

    @CIDR.setter
    def CIDR(self, CIDR):
        self._CIDR = CIDR

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CVM(self):
        return self._CVM

    @CVM.setter
    def CVM(self, CVM):
        self._CVM = CVM

    @property
    def AvailableIp(self):
        return self._AvailableIp

    @AvailableIp.setter
    def AvailableIp(self, AvailableIp):
        self._AvailableIp = AvailableIp

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ConfigureRisk(self):
        return self._ConfigureRisk

    @ConfigureRisk.setter
    def ConfigureRisk(self, ConfigureRisk):
        self._ConfigureRisk = ConfigureRisk

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._Nick = params.get("Nick")
        self._CIDR = params.get("CIDR")
        self._Zone = params.get("Zone")
        self._CVM = params.get("CVM")
        self._AvailableIp = params.get("AvailableIp")
        self._CreateTime = params.get("CreateTime")
        self._ConfigureRisk = params.get("ConfigureRisk")
        self._ScanTask = params.get("ScanTask")
        self._LastScanTime = params.get("LastScanTime")
        self._IsCore = params.get("IsCore")
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
        :param _Name: 标签名称
        :type Name: str
        :param _Value: 标签内容
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
        


class TaskAdvanceCFG(AbstractModel):
    """任务高级配置

    """

    def __init__(self):
        r"""
        :param _VulRisk: 漏洞风险高级配置
        :type VulRisk: list of TaskCenterVulRiskInputParam
        :param _WeakPwdRisk: 弱口令风险高级配置
        :type WeakPwdRisk: list of TaskCenterWeakPwdRiskInputParam
        :param _CFGRisk: 配置风险高级配置
        :type CFGRisk: list of TaskCenterCFGRiskInputParam
        """
        self._VulRisk = None
        self._WeakPwdRisk = None
        self._CFGRisk = None

    @property
    def VulRisk(self):
        return self._VulRisk

    @VulRisk.setter
    def VulRisk(self, VulRisk):
        self._VulRisk = VulRisk

    @property
    def WeakPwdRisk(self):
        return self._WeakPwdRisk

    @WeakPwdRisk.setter
    def WeakPwdRisk(self, WeakPwdRisk):
        self._WeakPwdRisk = WeakPwdRisk

    @property
    def CFGRisk(self):
        return self._CFGRisk

    @CFGRisk.setter
    def CFGRisk(self, CFGRisk):
        self._CFGRisk = CFGRisk


    def _deserialize(self, params):
        if params.get("VulRisk") is not None:
            self._VulRisk = []
            for item in params.get("VulRisk"):
                obj = TaskCenterVulRiskInputParam()
                obj._deserialize(item)
                self._VulRisk.append(obj)
        if params.get("WeakPwdRisk") is not None:
            self._WeakPwdRisk = []
            for item in params.get("WeakPwdRisk"):
                obj = TaskCenterWeakPwdRiskInputParam()
                obj._deserialize(item)
                self._WeakPwdRisk.append(obj)
        if params.get("CFGRisk") is not None:
            self._CFGRisk = []
            for item in params.get("CFGRisk"):
                obj = TaskCenterCFGRiskInputParam()
                obj._deserialize(item)
                self._CFGRisk.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskAssetObject(AbstractModel):
    """任务资产项

    """

    def __init__(self):
        r"""
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _InstanceType: 	资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _AssetType: 资产分类
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _Asset: ip/域名/资产id，数据库id等
        :type Asset: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._AssetName = None
        self._InstanceType = None
        self._AssetType = None
        self._Asset = None
        self._Region = None

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Asset(self):
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._AssetName = params.get("AssetName")
        self._InstanceType = params.get("InstanceType")
        self._AssetType = params.get("AssetType")
        self._Asset = params.get("Asset")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterCFGRiskInputParam(AbstractModel):
    """配置风险高级配置

    """

    def __init__(self):
        r"""
        :param _ItemId: 检测项ID
        :type ItemId: str
        :param _Enable: 是否开启，0-不开启，1-开启
        :type Enable: int
        :param _ResourceType: 资源类型
        :type ResourceType: str
        """
        self._ItemId = None
        self._Enable = None
        self._ResourceType = None

    @property
    def ItemId(self):
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._Enable = params.get("Enable")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterVulRiskInputParam(AbstractModel):
    """漏洞风险高级配置

    """

    def __init__(self):
        r"""
        :param _RiskId: 风险ID
        :type RiskId: str
        :param _Enable: 是否开启，0-不开启，1-开启
        :type Enable: int
        """
        self._RiskId = None
        self._Enable = None

    @property
    def RiskId(self):
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._RiskId = params.get("RiskId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterWeakPwdRiskInputParam(AbstractModel):
    """弱口令风险高级配置

    """

    def __init__(self):
        r"""
        :param _CheckItemId: 检测项ID
        :type CheckItemId: int
        :param _Enable: 是否开启，0-不开启，1-开启
        :type Enable: int
        """
        self._CheckItemId = None
        self._Enable = None

    @property
    def CheckItemId(self):
        return self._CheckItemId

    @CheckItemId.setter
    def CheckItemId(self, CheckItemId):
        self._CheckItemId = CheckItemId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._CheckItemId = params.get("CheckItemId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Vpc(AbstractModel):
    """vpc列表数据

    """

    def __init__(self):
        r"""
        :param _Subnet: 子网(只支持32位)
        :type Subnet: int
        :param _ConnectedVpc: 互通vpc(只支持32位)
        :type ConnectedVpc: int
        :param _AssetId: 资产id
        :type AssetId: str
        :param _Region: region区域
        :type Region: str
        :param _CVM: 云服务器(只支持32位)
        :type CVM: int
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _DNS: dns域名
注意：此字段可能返回 null，表示取不到有效值。
        :type DNS: list of str
        :param _AssetName: 资产名称
        :type AssetName: str
        :param _CIDR: cidr网段
        :type CIDR: str
        :param _CreateTime: 资产创建时间
        :type CreateTime: str
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _Nick: 昵称
        :type Nick: str
        """
        self._Subnet = None
        self._ConnectedVpc = None
        self._AssetId = None
        self._Region = None
        self._CVM = None
        self._Tag = None
        self._DNS = None
        self._AssetName = None
        self._CIDR = None
        self._CreateTime = None
        self._AppId = None
        self._Uin = None
        self._Nick = None

    @property
    def Subnet(self):
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

    @property
    def ConnectedVpc(self):
        return self._ConnectedVpc

    @ConnectedVpc.setter
    def ConnectedVpc(self, ConnectedVpc):
        self._ConnectedVpc = ConnectedVpc

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CVM(self):
        return self._CVM

    @CVM.setter
    def CVM(self, CVM):
        self._CVM = CVM

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def DNS(self):
        return self._DNS

    @DNS.setter
    def DNS(self, DNS):
        self._DNS = DNS

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def CIDR(self):
        return self._CIDR

    @CIDR.setter
    def CIDR(self, CIDR):
        self._CIDR = CIDR

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick


    def _deserialize(self, params):
        self._Subnet = params.get("Subnet")
        self._ConnectedVpc = params.get("ConnectedVpc")
        self._AssetId = params.get("AssetId")
        self._Region = params.get("Region")
        self._CVM = params.get("CVM")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._DNS = params.get("DNS")
        self._AssetName = params.get("AssetName")
        self._CIDR = params.get("CIDR")
        self._CreateTime = params.get("CreateTime")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nick = params.get("Nick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhereFilter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤的项
        :type Name: str
        :param _Values: 过滤的值
        :type Values: list of str
        :param _OperatorType: 精确匹配填 7 模糊匹配填9 ， 兼容 中台定的结构
        :type OperatorType: int
        """
        self._Name = None
        self._Values = None
        self._OperatorType = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def OperatorType(self):
        return self._OperatorType

    @OperatorType.setter
    def OperatorType(self, OperatorType):
        self._OperatorType = OperatorType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._OperatorType = params.get("OperatorType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        