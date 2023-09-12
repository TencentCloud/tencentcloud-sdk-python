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
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
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
        self._IsNewAsset = None

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

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


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
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetInfoDetail(AbstractModel):
    """资产扫描结构细节

    """

    def __init__(self):
        r"""
        :param _AppID: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppID: str
        :param _CVEId: CVE编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CVEId: str
        :param _IsScan: 是扫描，0默认未扫描，1正在扫描，2扫描完成，3扫描出错
注意：此字段可能返回 null，表示取不到有效值。
        :type IsScan: int
        :param _InfluenceAsset: 影响资产数目
注意：此字段可能返回 null，表示取不到有效值。
        :type InfluenceAsset: int
        :param _NotRepairAsset: 未修复资产数目
注意：此字段可能返回 null，表示取不到有效值。
        :type NotRepairAsset: int
        :param _NotProtectAsset: 未防护资产数目
注意：此字段可能返回 null，表示取不到有效值。
        :type NotProtectAsset: int
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskPercent: 任务百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskPercent: int
        :param _TaskTime: 任务时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTime: int
        :param _ScanTime: 扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTime: str
        """
        self._AppID = None
        self._CVEId = None
        self._IsScan = None
        self._InfluenceAsset = None
        self._NotRepairAsset = None
        self._NotProtectAsset = None
        self._TaskId = None
        self._TaskPercent = None
        self._TaskTime = None
        self._ScanTime = None

    @property
    def AppID(self):
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def CVEId(self):
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId

    @property
    def IsScan(self):
        return self._IsScan

    @IsScan.setter
    def IsScan(self, IsScan):
        self._IsScan = IsScan

    @property
    def InfluenceAsset(self):
        return self._InfluenceAsset

    @InfluenceAsset.setter
    def InfluenceAsset(self, InfluenceAsset):
        self._InfluenceAsset = InfluenceAsset

    @property
    def NotRepairAsset(self):
        return self._NotRepairAsset

    @NotRepairAsset.setter
    def NotRepairAsset(self, NotRepairAsset):
        self._NotRepairAsset = NotRepairAsset

    @property
    def NotProtectAsset(self):
        return self._NotProtectAsset

    @NotProtectAsset.setter
    def NotProtectAsset(self, NotProtectAsset):
        self._NotProtectAsset = NotProtectAsset

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskPercent(self):
        return self._TaskPercent

    @TaskPercent.setter
    def TaskPercent(self, TaskPercent):
        self._TaskPercent = TaskPercent

    @property
    def TaskTime(self):
        return self._TaskTime

    @TaskTime.setter
    def TaskTime(self, TaskTime):
        self._TaskTime = TaskTime

    @property
    def ScanTime(self):
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._CVEId = params.get("CVEId")
        self._IsScan = params.get("IsScan")
        self._InfluenceAsset = params.get("InfluenceAsset")
        self._NotRepairAsset = params.get("NotRepairAsset")
        self._NotProtectAsset = params.get("NotProtectAsset")
        self._TaskId = params.get("TaskId")
        self._TaskPercent = params.get("TaskPercent")
        self._TaskTime = params.get("TaskTime")
        self._ScanTime = params.get("ScanTime")
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
        


class BugInfoDetail(AbstractModel):
    """漏洞详细信息

    """

    def __init__(self):
        r"""
        :param _Id: 漏洞编号
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _PatchId: 漏洞对应pocId
注意：此字段可能返回 null，表示取不到有效值。
        :type PatchId: str
        :param _VULName: 漏洞名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VULName: str
        :param _Level: 漏洞严重性：high,middle，low，info
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        :param _CVSSScore: cvss评分
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSSScore: str
        :param _CVEId: cve编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CVEId: str
        :param _Tag: 漏洞标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        :param _VULCategory: 漏洞种类，1:web应用，2:系统组件漏洞，3:配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type VULCategory: int
        :param _ImpactOs: 漏洞影响系统
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactOs: str
        :param _ImpactCOMPENT: 漏洞影响组件
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactCOMPENT: str
        :param _ImpactVersion: 漏洞影响版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactVersion: str
        :param _Reference: 链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Reference: str
        :param _VULDescribe: 漏洞描述
注意：此字段可能返回 null，表示取不到有效值。
        :type VULDescribe: str
        :param _Fix: 修复建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Fix: str
        :param _ProSupport: 产品支持状态，实时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type ProSupport: int
        :param _IsPublish: 是否公开，0为未发布，1为发布
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublish: int
        :param _ReleaseTime: 释放时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _SubCategory: 漏洞子类别
注意：此字段可能返回 null，表示取不到有效值。
        :type SubCategory: str
        """
        self._Id = None
        self._PatchId = None
        self._VULName = None
        self._Level = None
        self._CVSSScore = None
        self._CVEId = None
        self._Tag = None
        self._VULCategory = None
        self._ImpactOs = None
        self._ImpactCOMPENT = None
        self._ImpactVersion = None
        self._Reference = None
        self._VULDescribe = None
        self._Fix = None
        self._ProSupport = None
        self._IsPublish = None
        self._ReleaseTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._SubCategory = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PatchId(self):
        return self._PatchId

    @PatchId.setter
    def PatchId(self, PatchId):
        self._PatchId = PatchId

    @property
    def VULName(self):
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def CVSSScore(self):
        return self._CVSSScore

    @CVSSScore.setter
    def CVSSScore(self, CVSSScore):
        self._CVSSScore = CVSSScore

    @property
    def CVEId(self):
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def VULCategory(self):
        return self._VULCategory

    @VULCategory.setter
    def VULCategory(self, VULCategory):
        self._VULCategory = VULCategory

    @property
    def ImpactOs(self):
        return self._ImpactOs

    @ImpactOs.setter
    def ImpactOs(self, ImpactOs):
        self._ImpactOs = ImpactOs

    @property
    def ImpactCOMPENT(self):
        return self._ImpactCOMPENT

    @ImpactCOMPENT.setter
    def ImpactCOMPENT(self, ImpactCOMPENT):
        self._ImpactCOMPENT = ImpactCOMPENT

    @property
    def ImpactVersion(self):
        return self._ImpactVersion

    @ImpactVersion.setter
    def ImpactVersion(self, ImpactVersion):
        self._ImpactVersion = ImpactVersion

    @property
    def Reference(self):
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference

    @property
    def VULDescribe(self):
        return self._VULDescribe

    @VULDescribe.setter
    def VULDescribe(self, VULDescribe):
        self._VULDescribe = VULDescribe

    @property
    def Fix(self):
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def ProSupport(self):
        return self._ProSupport

    @ProSupport.setter
    def ProSupport(self, ProSupport):
        self._ProSupport = ProSupport

    @property
    def IsPublish(self):
        return self._IsPublish

    @IsPublish.setter
    def IsPublish(self, IsPublish):
        self._IsPublish = IsPublish

    @property
    def ReleaseTime(self):
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

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
    def SubCategory(self):
        return self._SubCategory

    @SubCategory.setter
    def SubCategory(self, SubCategory):
        self._SubCategory = SubCategory


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PatchId = params.get("PatchId")
        self._VULName = params.get("VULName")
        self._Level = params.get("Level")
        self._CVSSScore = params.get("CVSSScore")
        self._CVEId = params.get("CVEId")
        self._Tag = params.get("Tag")
        self._VULCategory = params.get("VULCategory")
        self._ImpactOs = params.get("ImpactOs")
        self._ImpactCOMPENT = params.get("ImpactCOMPENT")
        self._ImpactVersion = params.get("ImpactVersion")
        self._Reference = params.get("Reference")
        self._VULDescribe = params.get("VULDescribe")
        self._Fix = params.get("Fix")
        self._ProSupport = params.get("ProSupport")
        self._IsPublish = params.get("IsPublish")
        self._ReleaseTime = params.get("ReleaseTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._SubCategory = params.get("SubCategory")
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
        :param _IsNewAsset: 1新资产；0 非新资产
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
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
        self._IsNewAsset = None

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

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


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
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListenerListInfo(AbstractModel):
    """clb实例和监听器信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器id
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param _ListenerName: 监听器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param _LoadBalancerId: 负载均衡Id
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerName: str
        :param _Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Vip: 负载均衡ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _VPort: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type VPort: int
        :param _Zone: 区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _NumericalVpcId: 私有网络id
注意：此字段可能返回 null，表示取不到有效值。
        :type NumericalVpcId: int
        :param _LoadBalancerType: 负载均衡类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param _Domain: 监听器域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _LoadBalancerDomain: 负载均衡域名
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerDomain: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Protocol = None
        self._Region = None
        self._Vip = None
        self._VPort = None
        self._Zone = None
        self._NumericalVpcId = None
        self._LoadBalancerType = None
        self._Domain = None
        self._LoadBalancerDomain = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NumericalVpcId(self):
        return self._NumericalVpcId

    @NumericalVpcId.setter
    def NumericalVpcId(self, NumericalVpcId):
        self._NumericalVpcId = NumericalVpcId

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerDomain(self):
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Protocol = params.get("Protocol")
        self._Region = params.get("Region")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._Zone = params.get("Zone")
        self._NumericalVpcId = params.get("NumericalVpcId")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Domain = params.get("Domain")
        self._LoadBalancerDomain = params.get("LoadBalancerDomain")
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
        :param _ScanItem: 扫描项目；port/poc/weakpass/webcontent/configrisk/exposedserver
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
        :param _Status: 0,任务创建成功；小于0失败；-1为存在资产未认证
        :type Status: int
        :param _UnAuthAsset: 未认证资产列表
        :type UnAuthAsset: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._UnAuthAsset = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnAuthAsset(self):
        return self._UnAuthAsset

    @UnAuthAsset.setter
    def UnAuthAsset(self, UnAuthAsset):
        self._UnAuthAsset = UnAuthAsset

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._UnAuthAsset = params.get("UnAuthAsset")
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
        :param _IsNewAsset: 是否新资产: 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
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
        self._IsNewAsset = None

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

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


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
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSearchBug(AbstractModel):
    """漏洞和资产信息

    """

    def __init__(self):
        r"""
        :param _StateCode: 返回查询状态
        :type StateCode: str
        :param _DataBug: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type DataBug: list of BugInfoDetail
        :param _DataAsset: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type DataAsset: list of AssetInfoDetail
        :param _VSSScan: true支持扫描。false不支持扫描
注意：此字段可能返回 null，表示取不到有效值。
        :type VSSScan: bool
        :param _CWPScan: 0不支持，1支持
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPScan: str
        :param _CFWPatch: 1支持虚拟补丁，0或空不支持
注意：此字段可能返回 null，表示取不到有效值。
        :type CFWPatch: str
        :param _WafPatch: 0不支持，1支持
注意：此字段可能返回 null，表示取不到有效值。
        :type WafPatch: int
        :param _CWPFix: 0不支持，1支持
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPFix: int
        """
        self._StateCode = None
        self._DataBug = None
        self._DataAsset = None
        self._VSSScan = None
        self._CWPScan = None
        self._CFWPatch = None
        self._WafPatch = None
        self._CWPFix = None

    @property
    def StateCode(self):
        return self._StateCode

    @StateCode.setter
    def StateCode(self, StateCode):
        self._StateCode = StateCode

    @property
    def DataBug(self):
        return self._DataBug

    @DataBug.setter
    def DataBug(self, DataBug):
        self._DataBug = DataBug

    @property
    def DataAsset(self):
        return self._DataAsset

    @DataAsset.setter
    def DataAsset(self, DataAsset):
        self._DataAsset = DataAsset

    @property
    def VSSScan(self):
        return self._VSSScan

    @VSSScan.setter
    def VSSScan(self, VSSScan):
        self._VSSScan = VSSScan

    @property
    def CWPScan(self):
        return self._CWPScan

    @CWPScan.setter
    def CWPScan(self, CWPScan):
        self._CWPScan = CWPScan

    @property
    def CFWPatch(self):
        return self._CFWPatch

    @CFWPatch.setter
    def CFWPatch(self, CFWPatch):
        self._CFWPatch = CFWPatch

    @property
    def WafPatch(self):
        return self._WafPatch

    @WafPatch.setter
    def WafPatch(self, WafPatch):
        self._WafPatch = WafPatch

    @property
    def CWPFix(self):
        return self._CWPFix

    @CWPFix.setter
    def CWPFix(self, CWPFix):
        self._CWPFix = CWPFix


    def _deserialize(self, params):
        self._StateCode = params.get("StateCode")
        if params.get("DataBug") is not None:
            self._DataBug = []
            for item in params.get("DataBug"):
                obj = BugInfoDetail()
                obj._deserialize(item)
                self._DataBug.append(obj)
        if params.get("DataAsset") is not None:
            self._DataAsset = []
            for item in params.get("DataAsset"):
                obj = AssetInfoDetail()
                obj._deserialize(item)
                self._DataAsset.append(obj)
        self._VSSScan = params.get("VSSScan")
        self._CWPScan = params.get("CWPScan")
        self._CFWPatch = params.get("CFWPatch")
        self._WafPatch = params.get("WafPatch")
        self._CWPFix = params.get("CWPFix")
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


class DescribeListenerListRequest(AbstractModel):
    """DescribeListenerList请求参数结构体

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
        


class DescribeListenerListResponse(AbstractModel):
    """DescribeListenerList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Data: 监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ClbListenerListInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
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
                obj = ClbListenerListInfo()
                obj._deserialize(item)
                self._Data.append(obj)
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


class DescribeScanTaskListRequest(AbstractModel):
    """DescribeScanTaskList请求参数结构体

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
        


class DescribeScanTaskListResponse(AbstractModel):
    """DescribeScanTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 任务日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ScanTaskInfoList
        :param _UINList: 主账户ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UINList: list of str
        :param _TaskModeList: 体检模式过滤列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskModeList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._UINList = None
        self._TaskModeList = None
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
    def TaskModeList(self):
        return self._TaskModeList

    @TaskModeList.setter
    def TaskModeList(self, TaskModeList):
        self._TaskModeList = TaskModeList

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
                obj = ScanTaskInfoList()
                obj._deserialize(item)
                self._Data.append(obj)
        self._UINList = params.get("UINList")
        if params.get("TaskModeList") is not None:
            self._TaskModeList = []
            for item in params.get("TaskModeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._TaskModeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSearchBugInfoRequest(AbstractModel):
    """DescribeSearchBugInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 无
        :type Id: str
        :param _CVEId: id=3时传入该参数
        :type CVEId: str
        """
        self._Id = None
        self._CVEId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CVEId(self):
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CVEId = params.get("CVEId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchBugInfoResponse(AbstractModel):
    """DescribeSearchBugInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 漏洞信息和资产信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.csip.v20221121.models.DataSearchBug`
        :param _ReturnCode: 状态值，0：查询成功，非0：查询失败
        :type ReturnCode: int
        :param _ReturnMsg: 状态信息，success：查询成功，fail：查询失败
        :type ReturnMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DataSearchBug()
            self._Data._deserialize(params.get("Data"))
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
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


class DescribeTaskLogListRequest(AbstractModel):
    """DescribeTaskLogList请求参数结构体

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
        


class DescribeTaskLogListResponse(AbstractModel):
    """DescribeTaskLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 报告列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TaskLogInfo
        :param _NotViewNumber: 待查看数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NotViewNumber: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._NotViewNumber = None
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
    def NotViewNumber(self):
        return self._NotViewNumber

    @NotViewNumber.setter
    def NotViewNumber(self, NotViewNumber):
        self._NotViewNumber = NotViewNumber

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
                obj = TaskLogInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._NotViewNumber = params.get("NotViewNumber")
        self._RequestId = params.get("RequestId")


class DescribeTaskLogURLRequest(AbstractModel):
    """DescribeTaskLogURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportItemKeyList: 任务报告Id 列表
        :type ReportItemKeyList: list of ReportItemKey
        :param _Type: 0: 预览， 1: 下载
        :type Type: int
        """
        self._ReportItemKeyList = None
        self._Type = None

    @property
    def ReportItemKeyList(self):
        return self._ReportItemKeyList

    @ReportItemKeyList.setter
    def ReportItemKeyList(self, ReportItemKeyList):
        self._ReportItemKeyList = ReportItemKeyList

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        if params.get("ReportItemKeyList") is not None:
            self._ReportItemKeyList = []
            for item in params.get("ReportItemKeyList"):
                obj = ReportItemKey()
                obj._deserialize(item)
                self._ReportItemKeyList.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLogURLResponse(AbstractModel):
    """DescribeTaskLogURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回报告临时下载url
        :type Data: list of TaskLogURL
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
            self._Data = []
            for item in params.get("Data"):
                obj = TaskLogURL()
                obj._deserialize(item)
                self._Data.append(obj)
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
        :param _ServiceRisk: 风险服务暴露数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceRisk: int
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        :param _VerifyDomain: 待确认资产的随机三级域名
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyDomain: str
        :param _VerifyTXTRecord: 待确认资产的TXT记录内容
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyTXTRecord: str
        :param _VerifyStatus: 待确认资产的认证状态，0-待认证，1-认证成功，2-认证中，3-txt认证失败，4-人工认证失败
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyStatus: int
        :param _BotAccessCount: bot访问数据
注意：此字段可能返回 null，表示取不到有效值。
        :type BotAccessCount: int
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
        self._ServiceRisk = None
        self._IsNewAsset = None
        self._VerifyDomain = None
        self._VerifyTXTRecord = None
        self._VerifyStatus = None
        self._BotAccessCount = None

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

    @property
    def ServiceRisk(self):
        return self._ServiceRisk

    @ServiceRisk.setter
    def ServiceRisk(self, ServiceRisk):
        self._ServiceRisk = ServiceRisk

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def VerifyDomain(self):
        return self._VerifyDomain

    @VerifyDomain.setter
    def VerifyDomain(self, VerifyDomain):
        self._VerifyDomain = VerifyDomain

    @property
    def VerifyTXTRecord(self):
        return self._VerifyTXTRecord

    @VerifyTXTRecord.setter
    def VerifyTXTRecord(self, VerifyTXTRecord):
        self._VerifyTXTRecord = VerifyTXTRecord

    @property
    def VerifyStatus(self):
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus

    @property
    def BotAccessCount(self):
        return self._BotAccessCount

    @BotAccessCount.setter
    def BotAccessCount(self, BotAccessCount):
        self._BotAccessCount = BotAccessCount


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
        self._ServiceRisk = params.get("ServiceRisk")
        self._IsNewAsset = params.get("IsNewAsset")
        self._VerifyDomain = params.get("VerifyDomain")
        self._VerifyTXTRecord = params.get("VerifyTXTRecord")
        self._VerifyStatus = params.get("VerifyStatus")
        self._BotAccessCount = params.get("BotAccessCount")
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
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        :param _VerifyStatus: 资产认证状态，0-待认证，1-认证成功，2-认证中，3+-认证失败
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyStatus: int
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
        self._IsNewAsset = None
        self._VerifyStatus = None

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

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def VerifyStatus(self):
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus


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
        self._IsNewAsset = params.get("IsNewAsset")
        self._VerifyStatus = params.get("VerifyStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportItemKey(AbstractModel):
    """报告项key

    """

    def __init__(self):
        r"""
        :param _TaskLogList: 日志Id列表
        :type TaskLogList: list of str
        """
        self._TaskLogList = None

    @property
    def TaskLogList(self):
        return self._TaskLogList

    @TaskLogList.setter
    def TaskLogList(self, TaskLogList):
        self._TaskLogList = TaskLogList


    def _deserialize(self, params):
        self._TaskLogList = params.get("TaskLogList")
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
        


class ScanTaskInfoList(AbstractModel):
    """扫描任务列表展示信息

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _StartTime: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _ScanPlanContent: corn
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanPlanContent: str
        :param _TaskType: 0-周期任务,1-立即扫描,2-定时扫描,3-自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: int
        :param _InsertTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _SelfDefiningAssets: 排除扫描资产信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfDefiningAssets: list of str
        :param _PredictTime: 预估时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PredictTime: int
        :param _PredictEndTime: 预估完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PredictEndTime: str
        :param _ReportNumber: 报告数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportNumber: int
        :param _AssetNumber: 资产数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetNumber: int
        :param _ScanStatus: 扫描状态 0 初始值  1正在扫描  2扫描完成  3扫描出错
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanStatus: int
        :param _Percent: 任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: float
        :param _ScanItem: port/poc/weakpass/webcontent/configrisk
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanItem: str
        :param _ScanAssetType: 0-全扫，1-指定资产扫，2-排除资产扫
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanAssetType: int
        :param _VSSTaskId: vss子任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type VSSTaskId: str
        :param _CSPMTaskId: cspm子任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type CSPMTaskId: str
        :param _CWPPOCId: 主机漏扫子任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPPOCId: str
        :param _CWPBlId: 主机基线子任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPBlId: str
        :param _VSSTaskProcess: vss子任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type VSSTaskProcess: int
        :param _CSPMTaskProcess: cspm子任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type CSPMTaskProcess: int
        :param _CWPPOCProcess: 主机漏扫子任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPPOCProcess: int
        :param _CWPBlProcess: 主机基线子任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPBlProcess: int
        :param _ErrorCode: 异常状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: int
        :param _ErrorInfo: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: str
        :param _StartDay: 周期任务开始的天数
注意：此字段可能返回 null，表示取不到有效值。
        :type StartDay: int
        :param _Frequency: 扫描频率,单位天,1-每天,7-每周,30-月,0-扫描一次
注意：此字段可能返回 null，表示取不到有效值。
        :type Frequency: int
        :param _CompleteNumber: 完成次数
注意：此字段可能返回 null，表示取不到有效值。
        :type CompleteNumber: int
        :param _CompleteAssetNumber: 已完成资产个数
注意：此字段可能返回 null，表示取不到有效值。
        :type CompleteAssetNumber: int
        :param _RiskCount: 风险数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCount: int
        :param _Assets: 资产
注意：此字段可能返回 null，表示取不到有效值。
        :type Assets: list of TaskAssetObject
        :param _AppId: 用户Appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _UIN: 用户主账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UIN: str
        :param _UserName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _TaskMode: 体检模式，0-标准模式，1-快速模式，2-高级模式
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskMode: int
        :param _ScanFrom: 扫描来源
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanFrom: str
        :param _IsFree: 是否限免体检0不是，1是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFree: int
        :param _IsDelete: 是否可以删除，1-可以，0-不可以，对应多账户管理使用
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDelete: int
        """
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._ScanPlanContent = None
        self._TaskType = None
        self._InsertTime = None
        self._TaskId = None
        self._SelfDefiningAssets = None
        self._PredictTime = None
        self._PredictEndTime = None
        self._ReportNumber = None
        self._AssetNumber = None
        self._ScanStatus = None
        self._Percent = None
        self._ScanItem = None
        self._ScanAssetType = None
        self._VSSTaskId = None
        self._CSPMTaskId = None
        self._CWPPOCId = None
        self._CWPBlId = None
        self._VSSTaskProcess = None
        self._CSPMTaskProcess = None
        self._CWPPOCProcess = None
        self._CWPBlProcess = None
        self._ErrorCode = None
        self._ErrorInfo = None
        self._StartDay = None
        self._Frequency = None
        self._CompleteNumber = None
        self._CompleteAssetNumber = None
        self._RiskCount = None
        self._Assets = None
        self._AppId = None
        self._UIN = None
        self._UserName = None
        self._TaskMode = None
        self._ScanFrom = None
        self._IsFree = None
        self._IsDelete = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

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
    def ScanPlanContent(self):
        return self._ScanPlanContent

    @ScanPlanContent.setter
    def ScanPlanContent(self, ScanPlanContent):
        self._ScanPlanContent = ScanPlanContent

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SelfDefiningAssets(self):
        return self._SelfDefiningAssets

    @SelfDefiningAssets.setter
    def SelfDefiningAssets(self, SelfDefiningAssets):
        self._SelfDefiningAssets = SelfDefiningAssets

    @property
    def PredictTime(self):
        return self._PredictTime

    @PredictTime.setter
    def PredictTime(self, PredictTime):
        self._PredictTime = PredictTime

    @property
    def PredictEndTime(self):
        return self._PredictEndTime

    @PredictEndTime.setter
    def PredictEndTime(self, PredictEndTime):
        self._PredictEndTime = PredictEndTime

    @property
    def ReportNumber(self):
        return self._ReportNumber

    @ReportNumber.setter
    def ReportNumber(self, ReportNumber):
        self._ReportNumber = ReportNumber

    @property
    def AssetNumber(self):
        return self._AssetNumber

    @AssetNumber.setter
    def AssetNumber(self, AssetNumber):
        self._AssetNumber = AssetNumber

    @property
    def ScanStatus(self):
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def ScanItem(self):
        return self._ScanItem

    @ScanItem.setter
    def ScanItem(self, ScanItem):
        self._ScanItem = ScanItem

    @property
    def ScanAssetType(self):
        return self._ScanAssetType

    @ScanAssetType.setter
    def ScanAssetType(self, ScanAssetType):
        self._ScanAssetType = ScanAssetType

    @property
    def VSSTaskId(self):
        return self._VSSTaskId

    @VSSTaskId.setter
    def VSSTaskId(self, VSSTaskId):
        self._VSSTaskId = VSSTaskId

    @property
    def CSPMTaskId(self):
        return self._CSPMTaskId

    @CSPMTaskId.setter
    def CSPMTaskId(self, CSPMTaskId):
        self._CSPMTaskId = CSPMTaskId

    @property
    def CWPPOCId(self):
        return self._CWPPOCId

    @CWPPOCId.setter
    def CWPPOCId(self, CWPPOCId):
        self._CWPPOCId = CWPPOCId

    @property
    def CWPBlId(self):
        return self._CWPBlId

    @CWPBlId.setter
    def CWPBlId(self, CWPBlId):
        self._CWPBlId = CWPBlId

    @property
    def VSSTaskProcess(self):
        return self._VSSTaskProcess

    @VSSTaskProcess.setter
    def VSSTaskProcess(self, VSSTaskProcess):
        self._VSSTaskProcess = VSSTaskProcess

    @property
    def CSPMTaskProcess(self):
        return self._CSPMTaskProcess

    @CSPMTaskProcess.setter
    def CSPMTaskProcess(self, CSPMTaskProcess):
        self._CSPMTaskProcess = CSPMTaskProcess

    @property
    def CWPPOCProcess(self):
        return self._CWPPOCProcess

    @CWPPOCProcess.setter
    def CWPPOCProcess(self, CWPPOCProcess):
        self._CWPPOCProcess = CWPPOCProcess

    @property
    def CWPBlProcess(self):
        return self._CWPBlProcess

    @CWPBlProcess.setter
    def CWPBlProcess(self, CWPBlProcess):
        self._CWPBlProcess = CWPBlProcess

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def StartDay(self):
        return self._StartDay

    @StartDay.setter
    def StartDay(self, StartDay):
        self._StartDay = StartDay

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def CompleteNumber(self):
        return self._CompleteNumber

    @CompleteNumber.setter
    def CompleteNumber(self, CompleteNumber):
        self._CompleteNumber = CompleteNumber

    @property
    def CompleteAssetNumber(self):
        return self._CompleteAssetNumber

    @CompleteAssetNumber.setter
    def CompleteAssetNumber(self, CompleteAssetNumber):
        self._CompleteAssetNumber = CompleteAssetNumber

    @property
    def RiskCount(self):
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def Assets(self):
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

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

    @property
    def TaskMode(self):
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def ScanFrom(self):
        return self._ScanFrom

    @ScanFrom.setter
    def ScanFrom(self, ScanFrom):
        self._ScanFrom = ScanFrom

    @property
    def IsFree(self):
        return self._IsFree

    @IsFree.setter
    def IsFree(self, IsFree):
        self._IsFree = IsFree

    @property
    def IsDelete(self):
        return self._IsDelete

    @IsDelete.setter
    def IsDelete(self, IsDelete):
        self._IsDelete = IsDelete


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ScanPlanContent = params.get("ScanPlanContent")
        self._TaskType = params.get("TaskType")
        self._InsertTime = params.get("InsertTime")
        self._TaskId = params.get("TaskId")
        self._SelfDefiningAssets = params.get("SelfDefiningAssets")
        self._PredictTime = params.get("PredictTime")
        self._PredictEndTime = params.get("PredictEndTime")
        self._ReportNumber = params.get("ReportNumber")
        self._AssetNumber = params.get("AssetNumber")
        self._ScanStatus = params.get("ScanStatus")
        self._Percent = params.get("Percent")
        self._ScanItem = params.get("ScanItem")
        self._ScanAssetType = params.get("ScanAssetType")
        self._VSSTaskId = params.get("VSSTaskId")
        self._CSPMTaskId = params.get("CSPMTaskId")
        self._CWPPOCId = params.get("CWPPOCId")
        self._CWPBlId = params.get("CWPBlId")
        self._VSSTaskProcess = params.get("VSSTaskProcess")
        self._CSPMTaskProcess = params.get("CSPMTaskProcess")
        self._CWPPOCProcess = params.get("CWPPOCProcess")
        self._CWPBlProcess = params.get("CWPBlProcess")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorInfo = params.get("ErrorInfo")
        self._StartDay = params.get("StartDay")
        self._Frequency = params.get("Frequency")
        self._CompleteNumber = params.get("CompleteNumber")
        self._CompleteAssetNumber = params.get("CompleteAssetNumber")
        self._RiskCount = params.get("RiskCount")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = TaskAssetObject()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._AppId = params.get("AppId")
        self._UIN = params.get("UIN")
        self._UserName = params.get("UserName")
        self._TaskMode = params.get("TaskMode")
        self._ScanFrom = params.get("ScanFrom")
        self._IsFree = params.get("IsFree")
        self._IsDelete = params.get("IsDelete")
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
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
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
        self._IsNewAsset = None

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

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


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
        self._IsNewAsset = params.get("IsNewAsset")
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
        


class TaskLogInfo(AbstractModel):
    """任务报告信息

    """

    def __init__(self):
        r"""
        :param _TaskLogName: 报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskLogName: str
        :param _TaskLogId: 报告ID
        :type TaskLogId: str
        :param _AssetsNumber: 关联资产个数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetsNumber: int
        :param _RiskNumber: 安全风险数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskNumber: int
        :param _Time: 报告生成时间,任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param _Status: 任务状态码：0 初始值  1正在扫描  2扫描完成  3扫描出错，4停止，5暂停，6该任务已被重启过
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _TaskName: 关联任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _StartTime: 扫描开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _TaskCenterTaskId: 任务中心扫描任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskCenterTaskId: str
        :param _AppId: 租户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _UIN: 主账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UIN: str
        :param _UserName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        """
        self._TaskLogName = None
        self._TaskLogId = None
        self._AssetsNumber = None
        self._RiskNumber = None
        self._Time = None
        self._Status = None
        self._TaskName = None
        self._StartTime = None
        self._TaskCenterTaskId = None
        self._AppId = None
        self._UIN = None
        self._UserName = None

    @property
    def TaskLogName(self):
        return self._TaskLogName

    @TaskLogName.setter
    def TaskLogName(self, TaskLogName):
        self._TaskLogName = TaskLogName

    @property
    def TaskLogId(self):
        return self._TaskLogId

    @TaskLogId.setter
    def TaskLogId(self, TaskLogId):
        self._TaskLogId = TaskLogId

    @property
    def AssetsNumber(self):
        return self._AssetsNumber

    @AssetsNumber.setter
    def AssetsNumber(self, AssetsNumber):
        self._AssetsNumber = AssetsNumber

    @property
    def RiskNumber(self):
        return self._RiskNumber

    @RiskNumber.setter
    def RiskNumber(self, RiskNumber):
        self._RiskNumber = RiskNumber

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskCenterTaskId(self):
        return self._TaskCenterTaskId

    @TaskCenterTaskId.setter
    def TaskCenterTaskId(self, TaskCenterTaskId):
        self._TaskCenterTaskId = TaskCenterTaskId

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
        self._TaskLogName = params.get("TaskLogName")
        self._TaskLogId = params.get("TaskLogId")
        self._AssetsNumber = params.get("AssetsNumber")
        self._RiskNumber = params.get("RiskNumber")
        self._Time = params.get("Time")
        self._Status = params.get("Status")
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._TaskCenterTaskId = params.get("TaskCenterTaskId")
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
        


class TaskLogURL(AbstractModel):
    """报告pdf下载的临时链接

    """

    def __init__(self):
        r"""
        :param _URL: 报告下载临时链接
注意：此字段可能返回 null，表示取不到有效值。
        :type URL: str
        :param _LogId: 任务报告id
注意：此字段可能返回 null，表示取不到有效值。
        :type LogId: str
        :param _TaskLogName: 任务报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskLogName: str
        :param _AppId: APP ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        """
        self._URL = None
        self._LogId = None
        self._TaskLogName = None
        self._AppId = None

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def LogId(self):
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def TaskLogName(self):
        return self._TaskLogName

    @TaskLogName.setter
    def TaskLogName(self, TaskLogName):
        self._TaskLogName = TaskLogName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._URL = params.get("URL")
        self._LogId = params.get("LogId")
        self._TaskLogName = params.get("TaskLogName")
        self._AppId = params.get("AppId")
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
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        :param _IsCore: 是否核心资产1是 2不是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
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
        self._IsNewAsset = None
        self._IsCore = None

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

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore


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
        self._IsNewAsset = params.get("IsNewAsset")
        self._IsCore = params.get("IsCore")
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
        :param _OperatorType: 中台定义：
1等于 2大于 3小于 4大于等于 5小于等于 6不等于 9模糊匹配 13非模糊匹配 14按位与
精确匹配填 7 模糊匹配填9 兼容 中台定的结构

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
        