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


class AggrCategorySoftDetailRow(AbstractModel):
    r"""按版本聚合后的软件列表

    """

    def __init__(self):
        r"""
        :param _ID: ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param _Name: 软件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _PiracyRisk: 盗版风险
注意：此字段可能返回 null，表示取不到有效值。
        :type PiracyRisk: int
        :param _OsType: 系统平台
注意：此字段可能返回 null，表示取不到有效值。
        :type OsType: int
        :param _CorpName: 企业名
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpName: str
        :param _InstalledDeviceNum: 安装设备数量(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type InstalledDeviceNum: int
        :param _PiracyInstalledDeviceNum: 盗版安装设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type PiracyInstalledDeviceNum: int
        :param _InstalledUserNum: 已安装用户数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstalledUserNum: int
        :param _PiracyInstalledUserNum: 盗版软件用户数
注意：此字段可能返回 null，表示取不到有效值。
        :type PiracyInstalledUserNum: int
        :param _AuthNum: 授权总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthNum: int
        :param _GenuineRate: 正版率
注意：此字段可能返回 null，表示取不到有效值。
        :type GenuineRate: float
        :param _UpgradableDeviceNum: 有新版本可升级的设备数量
        :type UpgradableDeviceNum: int
        """
        self._ID = None
        self._Name = None
        self._PiracyRisk = None
        self._OsType = None
        self._CorpName = None
        self._InstalledDeviceNum = None
        self._PiracyInstalledDeviceNum = None
        self._InstalledUserNum = None
        self._PiracyInstalledUserNum = None
        self._AuthNum = None
        self._GenuineRate = None
        self._UpgradableDeviceNum = None

    @property
    def ID(self):
        r"""ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""软件名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PiracyRisk(self):
        r"""盗版风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PiracyRisk

    @PiracyRisk.setter
    def PiracyRisk(self, PiracyRisk):
        self._PiracyRisk = PiracyRisk

    @property
    def OsType(self):
        r"""系统平台
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def CorpName(self):
        r"""企业名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CorpName

    @CorpName.setter
    def CorpName(self, CorpName):
        self._CorpName = CorpName

    @property
    def InstalledDeviceNum(self):
        r"""安装设备数量(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InstalledDeviceNum

    @InstalledDeviceNum.setter
    def InstalledDeviceNum(self, InstalledDeviceNum):
        self._InstalledDeviceNum = InstalledDeviceNum

    @property
    def PiracyInstalledDeviceNum(self):
        r"""盗版安装设备数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PiracyInstalledDeviceNum

    @PiracyInstalledDeviceNum.setter
    def PiracyInstalledDeviceNum(self, PiracyInstalledDeviceNum):
        self._PiracyInstalledDeviceNum = PiracyInstalledDeviceNum

    @property
    def InstalledUserNum(self):
        r"""已安装用户数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InstalledUserNum

    @InstalledUserNum.setter
    def InstalledUserNum(self, InstalledUserNum):
        self._InstalledUserNum = InstalledUserNum

    @property
    def PiracyInstalledUserNum(self):
        r"""盗版软件用户数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PiracyInstalledUserNum

    @PiracyInstalledUserNum.setter
    def PiracyInstalledUserNum(self, PiracyInstalledUserNum):
        self._PiracyInstalledUserNum = PiracyInstalledUserNum

    @property
    def AuthNum(self):
        r"""授权总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AuthNum

    @AuthNum.setter
    def AuthNum(self, AuthNum):
        self._AuthNum = AuthNum

    @property
    def GenuineRate(self):
        r"""正版率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._GenuineRate

    @GenuineRate.setter
    def GenuineRate(self, GenuineRate):
        self._GenuineRate = GenuineRate

    @property
    def UpgradableDeviceNum(self):
        r"""有新版本可升级的设备数量
        :rtype: int
        """
        return self._UpgradableDeviceNum

    @UpgradableDeviceNum.setter
    def UpgradableDeviceNum(self, UpgradableDeviceNum):
        self._UpgradableDeviceNum = UpgradableDeviceNum


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._PiracyRisk = params.get("PiracyRisk")
        self._OsType = params.get("OsType")
        self._CorpName = params.get("CorpName")
        self._InstalledDeviceNum = params.get("InstalledDeviceNum")
        self._PiracyInstalledDeviceNum = params.get("PiracyInstalledDeviceNum")
        self._InstalledUserNum = params.get("InstalledUserNum")
        self._PiracyInstalledUserNum = params.get("PiracyInstalledUserNum")
        self._AuthNum = params.get("AuthNum")
        self._GenuineRate = params.get("GenuineRate")
        self._UpgradableDeviceNum = params.get("UpgradableDeviceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AggrSoftDeviceRow(AbstractModel):
    r"""聚合软件的已安装终端列表中的一行数据

    """

    def __init__(self):
        r"""
        :param _DeviceName: 终端名
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _LastLoginAccount: 最近登录账号
注意：此字段可能返回 null，表示取不到有效值。
        :type LastLoginAccount: str
        :param _DeviceUserName: 终端用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceUserName: str
        :param _Version: 软件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _PiracyRisk: 是否盗版
注意：此字段可能返回 null，表示取不到有效值。
        :type PiracyRisk: int
        :param _PiracyReason: 盗版原因
注意：此字段可能返回 null，表示取不到有效值。
        :type PiracyReason: str
        :param _InstallTime: 安装时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InstallTime: str
        :param _UserPath: 用户目录
注意：此字段可能返回 null，表示取不到有效值。
        :type UserPath: str
        :param _UserGroup: 所在分组
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroup: str
        :param _IP: IP
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param _MAC: MAC
注意：此字段可能返回 null，表示取不到有效值。
        :type MAC: str
        :param _UseTime: 使用时长
注意：此字段可能返回 null，表示取不到有效值。
        :type UseTime: int
        :param _DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: int
        :param _FullSoftName: 软件全名
注意：此字段可能返回 null，表示取不到有效值。
        :type FullSoftName: str
        :param _Id: 数据ID（唯一）
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _NewVersion: 该终端此款软件可升级到的目标版本号
        :type NewVersion: str
        :param _UpgradeSoftId: 该软件对应运营配置的可升级id
        :type UpgradeSoftId: int
        :param _RemarkName: 终端备注名
        :type RemarkName: str
        """
        self._DeviceName = None
        self._LastLoginAccount = None
        self._DeviceUserName = None
        self._Version = None
        self._PiracyRisk = None
        self._PiracyReason = None
        self._InstallTime = None
        self._UserPath = None
        self._UserGroup = None
        self._IP = None
        self._MAC = None
        self._UseTime = None
        self._DeviceId = None
        self._FullSoftName = None
        self._Id = None
        self._NewVersion = None
        self._UpgradeSoftId = None
        self._RemarkName = None

    @property
    def DeviceName(self):
        r"""终端名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def LastLoginAccount(self):
        r"""最近登录账号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastLoginAccount

    @LastLoginAccount.setter
    def LastLoginAccount(self, LastLoginAccount):
        self._LastLoginAccount = LastLoginAccount

    @property
    def DeviceUserName(self):
        r"""终端用户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeviceUserName

    @DeviceUserName.setter
    def DeviceUserName(self, DeviceUserName):
        self._DeviceUserName = DeviceUserName

    @property
    def Version(self):
        r"""软件版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def PiracyRisk(self):
        r"""是否盗版
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PiracyRisk

    @PiracyRisk.setter
    def PiracyRisk(self, PiracyRisk):
        self._PiracyRisk = PiracyRisk

    @property
    def PiracyReason(self):
        r"""盗版原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PiracyReason

    @PiracyReason.setter
    def PiracyReason(self, PiracyReason):
        self._PiracyReason = PiracyReason

    @property
    def InstallTime(self):
        r"""安装时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstallTime

    @InstallTime.setter
    def InstallTime(self, InstallTime):
        self._InstallTime = InstallTime

    @property
    def UserPath(self):
        r"""用户目录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserPath

    @UserPath.setter
    def UserPath(self, UserPath):
        self._UserPath = UserPath

    @property
    def UserGroup(self):
        r"""所在分组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def IP(self):
        r"""IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def MAC(self):
        r"""MAC
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MAC

    @MAC.setter
    def MAC(self, MAC):
        self._MAC = MAC

    @property
    def UseTime(self):
        r"""使用时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UseTime

    @UseTime.setter
    def UseTime(self, UseTime):
        self._UseTime = UseTime

    @property
    def DeviceId(self):
        r"""设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def FullSoftName(self):
        r"""软件全名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FullSoftName

    @FullSoftName.setter
    def FullSoftName(self, FullSoftName):
        self._FullSoftName = FullSoftName

    @property
    def Id(self):
        r"""数据ID（唯一）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def NewVersion(self):
        r"""该终端此款软件可升级到的目标版本号
        :rtype: str
        """
        return self._NewVersion

    @NewVersion.setter
    def NewVersion(self, NewVersion):
        self._NewVersion = NewVersion

    @property
    def UpgradeSoftId(self):
        r"""该软件对应运营配置的可升级id
        :rtype: int
        """
        return self._UpgradeSoftId

    @UpgradeSoftId.setter
    def UpgradeSoftId(self, UpgradeSoftId):
        self._UpgradeSoftId = UpgradeSoftId

    @property
    def RemarkName(self):
        r"""终端备注名
        :rtype: str
        """
        return self._RemarkName

    @RemarkName.setter
    def RemarkName(self, RemarkName):
        self._RemarkName = RemarkName


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._LastLoginAccount = params.get("LastLoginAccount")
        self._DeviceUserName = params.get("DeviceUserName")
        self._Version = params.get("Version")
        self._PiracyRisk = params.get("PiracyRisk")
        self._PiracyReason = params.get("PiracyReason")
        self._InstallTime = params.get("InstallTime")
        self._UserPath = params.get("UserPath")
        self._UserGroup = params.get("UserGroup")
        self._IP = params.get("IP")
        self._MAC = params.get("MAC")
        self._UseTime = params.get("UseTime")
        self._DeviceId = params.get("DeviceId")
        self._FullSoftName = params.get("FullSoftName")
        self._Id = params.get("Id")
        self._NewVersion = params.get("NewVersion")
        self._UpgradeSoftId = params.get("UpgradeSoftId")
        self._RemarkName = params.get("RemarkName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplexRule(AbstractModel):
    r"""自动划分规则数据

    """

    def __init__(self):
        r"""
        :param _SimpleRules: 简单规则表达式
        :type SimpleRules: list of SimpleRule
        :param _Relation: 表达式间逻辑关系
        :type Relation: str
        """
        self._SimpleRules = None
        self._Relation = None

    @property
    def SimpleRules(self):
        r"""简单规则表达式
        :rtype: list of SimpleRule
        """
        return self._SimpleRules

    @SimpleRules.setter
    def SimpleRules(self, SimpleRules):
        self._SimpleRules = SimpleRules

    @property
    def Relation(self):
        r"""表达式间逻辑关系
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        if params.get("SimpleRules") is not None:
            self._SimpleRules = []
            for item in params.get("SimpleRules"):
                obj = SimpleRule()
                obj._deserialize(item)
                self._SimpleRules.append(obj)
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Condition(AbstractModel):
    r"""这是一个多接口的公共数据结构，用于接口根据条件进行过滤和分页。具体支持哪些过滤条件，参考具体使用该结构的接口字段描述

    """

    def __init__(self):
        r"""
        :param _Filters: Filters 条件过滤
        :type Filters: list of Filter
        :param _FilterGroups: FilterGroups 条件过滤组
        :type FilterGroups: list of FilterGroup
        :param _Sort: Sort 排序字段
        :type Sort: :class:`tencentcloud.ioa.v20220601.models.Sort`
        :param _PageSize: PageSize 每页获取数(只支持32位)
        :type PageSize: int
        :param _PageNum: PageNum 获取第几页(只支持32位)
        :type PageNum: int
        """
        self._Filters = None
        self._FilterGroups = None
        self._Sort = None
        self._PageSize = None
        self._PageNum = None

    @property
    def Filters(self):
        r"""Filters 条件过滤
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def FilterGroups(self):
        r"""FilterGroups 条件过滤组
        :rtype: list of FilterGroup
        """
        return self._FilterGroups

    @FilterGroups.setter
    def FilterGroups(self, FilterGroups):
        self._FilterGroups = FilterGroups

    @property
    def Sort(self):
        r"""Sort 排序字段
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Sort`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def PageSize(self):
        r"""PageSize 每页获取数(只支持32位)
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        r"""PageNum 获取第几页(只支持32位)
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("FilterGroups") is not None:
            self._FilterGroups = []
            for item in params.get("FilterGroups"):
                obj = FilterGroup()
                obj._deserialize(item)
                self._FilterGroups.append(obj)
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDLPFileDetectTaskData(AbstractModel):
    r"""文件鉴定任务分页数据

    """

    def __init__(self):
        r"""
        :param _TaskRequestId: 任务请求唯一Id
        :type TaskRequestId: list of str
        """
        self._TaskRequestId = None

    @property
    def TaskRequestId(self):
        r"""任务请求唯一Id
        :rtype: list of str
        """
        return self._TaskRequestId

    @TaskRequestId.setter
    def TaskRequestId(self, TaskRequestId):
        self._TaskRequestId = TaskRequestId


    def _deserialize(self, params):
        self._TaskRequestId = params.get("TaskRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDLPFileDetectTaskRequest(AbstractModel):
    r"""CreateDLPFileDetectTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 文件下载Url
        :type DownloadUrl: str
        :param _FileName: 文件名
        :type FileName: str
        :param _FileMd5: 文件Md5
        :type FileMd5: str
        :param _BalanceType: 负载类型  1 从GroupId中选一节点 鉴定  2使用所有SelectNodeIds节点鉴定
        :type BalanceType: int
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _SelectNodeIds: 选中节点唯一Id列表,BalanceType=2时必填
        :type SelectNodeIds: list of str
        :param _GroupId: 节点组唯一Id,BalanceType=1时必填
        :type GroupId: str
        """
        self._DownloadUrl = None
        self._FileName = None
        self._FileMd5 = None
        self._BalanceType = None
        self._DomainInstanceId = None
        self._SelectNodeIds = None
        self._GroupId = None

    @property
    def DownloadUrl(self):
        r"""文件下载Url
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def FileName(self):
        r"""文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileMd5(self):
        r"""文件Md5
        :rtype: str
        """
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def BalanceType(self):
        r"""负载类型  1 从GroupId中选一节点 鉴定  2使用所有SelectNodeIds节点鉴定
        :rtype: int
        """
        return self._BalanceType

    @BalanceType.setter
    def BalanceType(self, BalanceType):
        self._BalanceType = BalanceType

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def SelectNodeIds(self):
        r"""选中节点唯一Id列表,BalanceType=2时必填
        :rtype: list of str
        """
        return self._SelectNodeIds

    @SelectNodeIds.setter
    def SelectNodeIds(self, SelectNodeIds):
        self._SelectNodeIds = SelectNodeIds

    @property
    def GroupId(self):
        r"""节点组唯一Id,BalanceType=1时必填
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._FileName = params.get("FileName")
        self._FileMd5 = params.get("FileMd5")
        self._BalanceType = params.get("BalanceType")
        self._DomainInstanceId = params.get("DomainInstanceId")
        self._SelectNodeIds = params.get("SelectNodeIds")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDLPFileDetectTaskResponse(AbstractModel):
    r"""CreateDLPFileDetectTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建文件鉴定任务数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.CreateDLPFileDetectTaskData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""创建文件鉴定任务数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.CreateDLPFileDetectTaskData`
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
            self._Data = CreateDLPFileDetectTaskData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateDLPFileDetectionTaskData(AbstractModel):
    r"""提交送检任务相应数据

    """

    def __init__(self):
        r"""
        :param _DLPFileDetectionTaskID: 提交任务生成的id，也即requestID。用于后续查询
        :type DLPFileDetectionTaskID: str
        """
        self._DLPFileDetectionTaskID = None

    @property
    def DLPFileDetectionTaskID(self):
        r"""提交任务生成的id，也即requestID。用于后续查询
        :rtype: str
        """
        return self._DLPFileDetectionTaskID

    @DLPFileDetectionTaskID.setter
    def DLPFileDetectionTaskID(self, DLPFileDetectionTaskID):
        self._DLPFileDetectionTaskID = DLPFileDetectionTaskID


    def _deserialize(self, params):
        self._DLPFileDetectionTaskID = params.get("DLPFileDetectionTaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDLPFileDetectionTaskRequest(AbstractModel):
    r"""CreateDLPFileDetectionTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 文件下载链接，要求公网可访问，GET方式访问后为文件
        :type Url: str
        :param _FileName: 文件名，带后缀
        :type FileName: str
        :param _FileMd5:  文件md5，传入相同md5会直接使用之前缓存的结果。

> 请注意：不同文件使用相同md5送检，会命中缓存得到旧的检测结果
        :type FileMd5: str
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配
        :type DomainInstanceId: str
        :param _CallBackUrl: 回调地址，暂时未使用
        :type CallBackUrl: str
        """
        self._Url = None
        self._FileName = None
        self._FileMd5 = None
        self._DomainInstanceId = None
        self._CallBackUrl = None

    @property
    def Url(self):
        r"""文件下载链接，要求公网可访问，GET方式访问后为文件
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def FileName(self):
        r"""文件名，带后缀
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileMd5(self):
        r""" 文件md5，传入相同md5会直接使用之前缓存的结果。

> 请注意：不同文件使用相同md5送检，会命中缓存得到旧的检测结果
        :rtype: str
        """
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def CallBackUrl(self):
        r"""回调地址，暂时未使用
        :rtype: str
        """
        return self._CallBackUrl

    @CallBackUrl.setter
    def CallBackUrl(self, CallBackUrl):
        self._CallBackUrl = CallBackUrl


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._FileName = params.get("FileName")
        self._FileMd5 = params.get("FileMd5")
        self._DomainInstanceId = params.get("DomainInstanceId")
        self._CallBackUrl = params.get("CallBackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDLPFileDetectionTaskResponse(AbstractModel):
    r"""CreateDLPFileDetectionTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建送检任务响应数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.CreateDLPFileDetectionTaskData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""创建送检任务响应数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.CreateDLPFileDetectionTaskData`
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
            self._Data = CreateDLPFileDetectionTaskData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateDeviceTaskRequest(AbstractModel):
    r"""CreateDeviceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _Mid: 终端id
        :type Mid: str
        """
        self._DomainInstanceId = None
        self._Mid = None

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def Mid(self):
        r"""终端id
        :rtype: str
        """
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid


    def _deserialize(self, params):
        self._DomainInstanceId = params.get("DomainInstanceId")
        self._Mid = params.get("Mid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceTaskResponse(AbstractModel):
    r"""CreateDeviceTask返回参数结构体

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


class CreateDeviceVirtualGroupRequest(AbstractModel):
    r"""CreateDeviceVirtualGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceVirtualGroupName: 必填，终端自定义分组名
        :type DeviceVirtualGroupName: str
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _Description: 详情
        :type Description: str
        :param _OsType: 系统类型（0: win，1：linux，2: mac，4：android，5：ios ； 默认值0）(只支持32位)
        :type OsType: int
        :param _TimeType: 分组类型（0:手动分组；非0为自动划分分组；具体枚举值为：1:自动每小时划分分组、2:自动每天划分分组、3:自定义时间划分分组； 默认值0）(只支持32位)
        :type TimeType: int
        :param _AutoMinute: 选填，TimeType=3时的自动划分时间，其他情况为0（单位min）(只支持32位)
        :type AutoMinute: int
        :param _AutoRules: 选填，手动分组不填，自动划分分组的划分规则数据
        :type AutoRules: :class:`tencentcloud.ioa.v20220601.models.ComplexRule`
        """
        self._DeviceVirtualGroupName = None
        self._DomainInstanceId = None
        self._Description = None
        self._OsType = None
        self._TimeType = None
        self._AutoMinute = None
        self._AutoRules = None

    @property
    def DeviceVirtualGroupName(self):
        r"""必填，终端自定义分组名
        :rtype: str
        """
        return self._DeviceVirtualGroupName

    @DeviceVirtualGroupName.setter
    def DeviceVirtualGroupName(self, DeviceVirtualGroupName):
        self._DeviceVirtualGroupName = DeviceVirtualGroupName

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def Description(self):
        r"""详情
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OsType(self):
        r"""系统类型（0: win，1：linux，2: mac，4：android，5：ios ； 默认值0）(只支持32位)
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def TimeType(self):
        r"""分组类型（0:手动分组；非0为自动划分分组；具体枚举值为：1:自动每小时划分分组、2:自动每天划分分组、3:自定义时间划分分组； 默认值0）(只支持32位)
        :rtype: int
        """
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType

    @property
    def AutoMinute(self):
        r"""选填，TimeType=3时的自动划分时间，其他情况为0（单位min）(只支持32位)
        :rtype: int
        """
        return self._AutoMinute

    @AutoMinute.setter
    def AutoMinute(self, AutoMinute):
        self._AutoMinute = AutoMinute

    @property
    def AutoRules(self):
        r"""选填，手动分组不填，自动划分分组的划分规则数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.ComplexRule`
        """
        return self._AutoRules

    @AutoRules.setter
    def AutoRules(self, AutoRules):
        self._AutoRules = AutoRules


    def _deserialize(self, params):
        self._DeviceVirtualGroupName = params.get("DeviceVirtualGroupName")
        self._DomainInstanceId = params.get("DomainInstanceId")
        self._Description = params.get("Description")
        self._OsType = params.get("OsType")
        self._TimeType = params.get("TimeType")
        self._AutoMinute = params.get("AutoMinute")
        if params.get("AutoRules") is not None:
            self._AutoRules = ComplexRule()
            self._AutoRules._deserialize(params.get("AutoRules"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceVirtualGroupResponse(AbstractModel):
    r"""CreateDeviceVirtualGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 响应返回的data
        :type Data: :class:`tencentcloud.ioa.v20220601.models.CreateDeviceVirtualGroupRspData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""响应返回的data
        :rtype: :class:`tencentcloud.ioa.v20220601.models.CreateDeviceVirtualGroupRspData`
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
            self._Data = CreateDeviceVirtualGroupRspData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateDeviceVirtualGroupRspData(AbstractModel):
    r"""响应返回的data

    """

    def __init__(self):
        r"""
        :param _Id: 返回的自定义分组id
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        r"""返回的自定义分组id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivilegeCodeRequest(AbstractModel):
    r"""CreatePrivilegeCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mid: 必填；设备唯一标识符;
        :type Mid: str
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _OsType: 系统类型（0: win，1：linux，2: mac，4：android，5：ios ）；默认值0
        :type OsType: int
        """
        self._Mid = None
        self._DomainInstanceId = None
        self._OsType = None

    @property
    def Mid(self):
        r"""必填；设备唯一标识符;
        :rtype: str
        """
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def OsType(self):
        r"""系统类型（0: win，1：linux，2: mac，4：android，5：ios ）；默认值0
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType


    def _deserialize(self, params):
        self._Mid = params.get("Mid")
        self._DomainInstanceId = params.get("DomainInstanceId")
        self._OsType = params.get("OsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivilegeCodeResponse(AbstractModel):
    r"""CreatePrivilegeCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务响应数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.CreatePrivilegeCodeRspData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务响应数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.CreatePrivilegeCodeRspData`
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
            self._Data = CreatePrivilegeCodeRspData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreatePrivilegeCodeRspData(AbstractModel):
    r"""业务响应数据

    """

    def __init__(self):
        r"""
        :param _Code: 特权码数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        """
        self._Code = None

    @property
    def Code(self):
        r"""特权码数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupsData(AbstractModel):
    r"""账号分组信息

    """

    def __init__(self):
        r"""
        :param _NamePath: 账号分组名全路径，点分格式
        :type NamePath: str
        :param _IdPathArr: 账号分组ID全路径，数组格式
        :type IdPathArr: list of int
        :param _ExtraInfo: 扩展信息
        :type ExtraInfo: str
        :param _Utime: 最后更新时间
        :type Utime: str
        :param _ParentId: 父分组ID
        :type ParentId: int
        :param _OrgId: 源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :type OrgId: str
        :param _Name: 分组名称
        :type Name: str
        :param _Id: 分组ID
        :type Id: int
        :param _Description: 分组描述
        :type Description: str
        :param _Source: 同步数据源
        :type Source: int
        :param _IdPath: 账号分组ID全路径，点分格式
        :type IdPath: str
        :param _Itime: 创建时间
        :type Itime: str
        :param _ParentOrgId: 父源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :type ParentOrgId: str
        :param _ImportType: 导入类型
        :type ImportType: str
        :param _MiniIamId: miniIAM id
        :type MiniIamId: str
        :param _UserTotal: 该分组下含子组的所有用户总数
        :type UserTotal: int
        :param _IsLeaf: 是否叶子节点
        :type IsLeaf: bool
        :param _ReadOnly: 是否该账户的直接权限
        :type ReadOnly: bool
        :param _LatestSyncResult: 最新一次同步任务的结果
        :type LatestSyncResult: str
        :param _LatestSyncTime: 最新一次同步任务的结束时间
        :type LatestSyncTime: str
        :param _NamePathArr: 分组名称数组
        :type NamePathArr: list of str
        """
        self._NamePath = None
        self._IdPathArr = None
        self._ExtraInfo = None
        self._Utime = None
        self._ParentId = None
        self._OrgId = None
        self._Name = None
        self._Id = None
        self._Description = None
        self._Source = None
        self._IdPath = None
        self._Itime = None
        self._ParentOrgId = None
        self._ImportType = None
        self._MiniIamId = None
        self._UserTotal = None
        self._IsLeaf = None
        self._ReadOnly = None
        self._LatestSyncResult = None
        self._LatestSyncTime = None
        self._NamePathArr = None

    @property
    def NamePath(self):
        r"""账号分组名全路径，点分格式
        :rtype: str
        """
        return self._NamePath

    @NamePath.setter
    def NamePath(self, NamePath):
        self._NamePath = NamePath

    @property
    def IdPathArr(self):
        r"""账号分组ID全路径，数组格式
        :rtype: list of int
        """
        return self._IdPathArr

    @IdPathArr.setter
    def IdPathArr(self, IdPathArr):
        self._IdPathArr = IdPathArr

    @property
    def ExtraInfo(self):
        r"""扩展信息
        :rtype: str
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def Utime(self):
        r"""最后更新时间
        :rtype: str
        """
        return self._Utime

    @Utime.setter
    def Utime(self, Utime):
        self._Utime = Utime

    @property
    def ParentId(self):
        r"""父分组ID
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def OrgId(self):
        r"""源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :rtype: str
        """
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def Name(self):
        r"""分组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        r"""分组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Description(self):
        r"""分组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Source(self):
        r"""同步数据源
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def IdPath(self):
        r"""账号分组ID全路径，点分格式
        :rtype: str
        """
        return self._IdPath

    @IdPath.setter
    def IdPath(self, IdPath):
        self._IdPath = IdPath

    @property
    def Itime(self):
        r"""创建时间
        :rtype: str
        """
        return self._Itime

    @Itime.setter
    def Itime(self, Itime):
        self._Itime = Itime

    @property
    def ParentOrgId(self):
        r"""父源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :rtype: str
        """
        return self._ParentOrgId

    @ParentOrgId.setter
    def ParentOrgId(self, ParentOrgId):
        self._ParentOrgId = ParentOrgId

    @property
    def ImportType(self):
        r"""导入类型
        :rtype: str
        """
        return self._ImportType

    @ImportType.setter
    def ImportType(self, ImportType):
        self._ImportType = ImportType

    @property
    def MiniIamId(self):
        r"""miniIAM id
        :rtype: str
        """
        return self._MiniIamId

    @MiniIamId.setter
    def MiniIamId(self, MiniIamId):
        self._MiniIamId = MiniIamId

    @property
    def UserTotal(self):
        r"""该分组下含子组的所有用户总数
        :rtype: int
        """
        return self._UserTotal

    @UserTotal.setter
    def UserTotal(self, UserTotal):
        self._UserTotal = UserTotal

    @property
    def IsLeaf(self):
        r"""是否叶子节点
        :rtype: bool
        """
        return self._IsLeaf

    @IsLeaf.setter
    def IsLeaf(self, IsLeaf):
        self._IsLeaf = IsLeaf

    @property
    def ReadOnly(self):
        r"""是否该账户的直接权限
        :rtype: bool
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def LatestSyncResult(self):
        r"""最新一次同步任务的结果
        :rtype: str
        """
        return self._LatestSyncResult

    @LatestSyncResult.setter
    def LatestSyncResult(self, LatestSyncResult):
        self._LatestSyncResult = LatestSyncResult

    @property
    def LatestSyncTime(self):
        r"""最新一次同步任务的结束时间
        :rtype: str
        """
        return self._LatestSyncTime

    @LatestSyncTime.setter
    def LatestSyncTime(self, LatestSyncTime):
        self._LatestSyncTime = LatestSyncTime

    @property
    def NamePathArr(self):
        r"""分组名称数组
        :rtype: list of str
        """
        return self._NamePathArr

    @NamePathArr.setter
    def NamePathArr(self, NamePathArr):
        self._NamePathArr = NamePathArr


    def _deserialize(self, params):
        self._NamePath = params.get("NamePath")
        self._IdPathArr = params.get("IdPathArr")
        self._ExtraInfo = params.get("ExtraInfo")
        self._Utime = params.get("Utime")
        self._ParentId = params.get("ParentId")
        self._OrgId = params.get("OrgId")
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Description = params.get("Description")
        self._Source = params.get("Source")
        self._IdPath = params.get("IdPath")
        self._Itime = params.get("Itime")
        self._ParentOrgId = params.get("ParentOrgId")
        self._ImportType = params.get("ImportType")
        self._MiniIamId = params.get("MiniIamId")
        self._UserTotal = params.get("UserTotal")
        self._IsLeaf = params.get("IsLeaf")
        self._ReadOnly = params.get("ReadOnly")
        self._LatestSyncResult = params.get("LatestSyncResult")
        self._LatestSyncTime = params.get("LatestSyncTime")
        self._NamePathArr = params.get("NamePathArr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupsPageResp(AbstractModel):
    r"""账户分组详情响应数据

    """

    def __init__(self):
        r"""
        :param _Items: 账户分响应对象集合
        :type Items: list of DescribeAccountGroupsData
        :param _Page: 分页公共对象
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        self._Items = None
        self._Page = None

    @property
    def Items(self):
        r"""账户分响应对象集合
        :rtype: list of DescribeAccountGroupsData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Page(self):
        r"""分页公共对象
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeAccountGroupsData()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupsRequest(AbstractModel):
    r"""DescribeAccountGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Deepin: 搜索范围：0-仅当前分组的直接子组，1-当前分组的所有子组。默认为0。
        :type Deepin: int
        :param _Condition: 查询条件

过滤参数
1、Name，string类型，按分组名过滤
是否必填：否
操作符: like

排序条件
1、Itime，string类型，按分组创建时间排序
是否必填：否
2、Utime，string类型，按分组更新时间排序
是否必填：否
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _ParentId: 父分组ID，获取该分组下的子组信息。默认查询全网根分组下子组信息。
        :type ParentId: int
        """
        self._Deepin = None
        self._Condition = None
        self._ParentId = None

    @property
    def Deepin(self):
        r"""搜索范围：0-仅当前分组的直接子组，1-当前分组的所有子组。默认为0。
        :rtype: int
        """
        return self._Deepin

    @Deepin.setter
    def Deepin(self, Deepin):
        self._Deepin = Deepin

    @property
    def Condition(self):
        r"""查询条件

过滤参数
1、Name，string类型，按分组名过滤
是否必填：否
操作符: like

排序条件
1、Itime，string类型，按分组创建时间排序
是否必填：否
2、Utime，string类型，按分组更新时间排序
是否必填：否
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def ParentId(self):
        r"""父分组ID，获取该分组下的子组信息。默认查询全网根分组下子组信息。
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId


    def _deserialize(self, params):
        self._Deepin = params.get("Deepin")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._ParentId = params.get("ParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupsResponse(AbstractModel):
    r"""DescribeAccountGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 账号分组详情响应数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeAccountGroupsPageResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""账号分组详情响应数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeAccountGroupsPageResp`
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
            self._Data = DescribeAccountGroupsPageResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAggrSoftCategorySoftListData(AbstractModel):
    r"""业务响应数据

    """

    def __init__(self):
        r"""
        :param _Page: 分页公共对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        :param _Total: 总数(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _AggrSoftCategorySoftList: 行数据
注意：此字段可能返回 null，表示取不到有效值。
        :type AggrSoftCategorySoftList: list of AggrCategorySoftDetailRow
        """
        self._Page = None
        self._Total = None
        self._AggrSoftCategorySoftList = None

    @property
    def Page(self):
        r"""分页公共对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Total(self):
        r"""总数(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AggrSoftCategorySoftList(self):
        r"""行数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AggrCategorySoftDetailRow
        """
        return self._AggrSoftCategorySoftList

    @AggrSoftCategorySoftList.setter
    def AggrSoftCategorySoftList(self, AggrSoftCategorySoftList):
        self._AggrSoftCategorySoftList = AggrSoftCategorySoftList


    def _deserialize(self, params):
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        self._Total = params.get("Total")
        if params.get("AggrSoftCategorySoftList") is not None:
            self._AggrSoftCategorySoftList = []
            for item in params.get("AggrSoftCategorySoftList"):
                obj = AggrCategorySoftDetailRow()
                obj._deserialize(item)
                self._AggrSoftCategorySoftList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggrSoftCategorySoftListRequest(AbstractModel):
    r"""DescribeAggrSoftCategorySoftList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Condition: 过滤条件、分页参数<li>Name - String - 过滤支持：是 - 操作符:eq,neq,like,ilike,nlike - 排序支持：是 - 按类别名称过滤或排序。</li><li>CorpName - String - 过滤支持：是 - 操作符:eq,neq,like,ilike,nlike - 排序支持：是 - 按CorpName过滤或排序。</li><li>Version - String - 过滤支持：否 - 操作符:eq,like - 排序支持：是 - 按版本排序。</li><li>InstalledDeviceCount - int - 过滤支持：否 - 操作符:eq,like - 排序支持：是 - 按安装设备数量排序。</li><li>GenuineRate - float - 过滤支持：否 - 操作符:eq,like - 排序支持：是 - 按正版率排序。</li><li>AuthNum - int - 过滤支持：否 - 操作符:eq,like - 排序支持：是 - 按授权数量排序。</li><li>CategoryNamePath - String - 过滤支持：否 - 操作符:eq,like - 排序支持：是 - 按类别路径名排序。</li>
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _OsType: 操作系统类型（0: win，1：linux，2: mac，4：android，5：ios 默认值0）
        :type OsType: int
        """
        self._Condition = None
        self._OsType = None

    @property
    def Condition(self):
        r"""过滤条件、分页参数<li>Name - String - 过滤支持：是 - 操作符:eq,neq,like,ilike,nlike - 排序支持：是 - 按类别名称过滤或排序。</li><li>CorpName - String - 过滤支持：是 - 操作符:eq,neq,like,ilike,nlike - 排序支持：是 - 按CorpName过滤或排序。</li><li>Version - String - 过滤支持：否 - 操作符:eq,like - 排序支持：是 - 按版本排序。</li><li>InstalledDeviceCount - int - 过滤支持：否 - 操作符:eq,like - 排序支持：是 - 按安装设备数量排序。</li><li>GenuineRate - float - 过滤支持：否 - 操作符:eq,like - 排序支持：是 - 按正版率排序。</li><li>AuthNum - int - 过滤支持：否 - 操作符:eq,like - 排序支持：是 - 按授权数量排序。</li><li>CategoryNamePath - String - 过滤支持：否 - 操作符:eq,like - 排序支持：是 - 按类别路径名排序。</li>
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def OsType(self):
        r"""操作系统类型（0: win，1：linux，2: mac，4：android，5：ios 默认值0）
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType


    def _deserialize(self, params):
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._OsType = params.get("OsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggrSoftCategorySoftListResponse(AbstractModel):
    r"""DescribeAggrSoftCategorySoftList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftCategorySoftListData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftCategorySoftListData`
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
            self._Data = DescribeAggrSoftCategorySoftListData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAggrSoftDetailData(AbstractModel):
    r"""聚合软件详情数据

    """

    def __init__(self):
        r"""
        :param _Name: 软件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _OsType: 平台
注意：此字段可能返回 null，表示取不到有效值。
        :type OsType: int
        :param _PiracyRisk: 盗版风险
注意：此字段可能返回 null，表示取不到有效值。
        :type PiracyRisk: int
        :param _Corp: 厂商
注意：此字段可能返回 null，表示取不到有效值。
        :type Corp: str
        :param _SoftVersionDist: 已安装版本分布
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftVersionDist: list of SoftVersionAndNum
        :param _PiracyVersionDist: 盗版版本安装
注意：此字段可能返回 null，表示取不到有效值。
        :type PiracyVersionDist: list of SoftVersionAndNum
        :param _InstalledDeviceNum: 安装设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstalledDeviceNum: int
        :param _PiracyInstalledDeviceNum: 盗版安装设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type PiracyInstalledDeviceNum: int
        :param _InstalledUserNum: 安装用户数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstalledUserNum: int
        :param _PiracyInstalledUserNum: 盗版安装用户数
注意：此字段可能返回 null，表示取不到有效值。
        :type PiracyInstalledUserNum: int
        :param _AuthNum: 授权数
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthNum: int
        :param _GenuineRate: 正版率
注意：此字段可能返回 null，表示取不到有效值。
        :type GenuineRate: float
        :param _UpgradableDeviceNum: 有新版本可升级的设备数量
        :type UpgradableDeviceNum: int
        :param _UpgradableVersions: 当前可升级的最新版本信息, 每一项均为json字符串
        :type UpgradableVersions: list of str
        """
        self._Name = None
        self._OsType = None
        self._PiracyRisk = None
        self._Corp = None
        self._SoftVersionDist = None
        self._PiracyVersionDist = None
        self._InstalledDeviceNum = None
        self._PiracyInstalledDeviceNum = None
        self._InstalledUserNum = None
        self._PiracyInstalledUserNum = None
        self._AuthNum = None
        self._GenuineRate = None
        self._UpgradableDeviceNum = None
        self._UpgradableVersions = None

    @property
    def Name(self):
        r"""软件名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OsType(self):
        r"""平台
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def PiracyRisk(self):
        r"""盗版风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PiracyRisk

    @PiracyRisk.setter
    def PiracyRisk(self, PiracyRisk):
        self._PiracyRisk = PiracyRisk

    @property
    def Corp(self):
        r"""厂商
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Corp

    @Corp.setter
    def Corp(self, Corp):
        self._Corp = Corp

    @property
    def SoftVersionDist(self):
        r"""已安装版本分布
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SoftVersionAndNum
        """
        return self._SoftVersionDist

    @SoftVersionDist.setter
    def SoftVersionDist(self, SoftVersionDist):
        self._SoftVersionDist = SoftVersionDist

    @property
    def PiracyVersionDist(self):
        r"""盗版版本安装
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SoftVersionAndNum
        """
        return self._PiracyVersionDist

    @PiracyVersionDist.setter
    def PiracyVersionDist(self, PiracyVersionDist):
        self._PiracyVersionDist = PiracyVersionDist

    @property
    def InstalledDeviceNum(self):
        r"""安装设备数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InstalledDeviceNum

    @InstalledDeviceNum.setter
    def InstalledDeviceNum(self, InstalledDeviceNum):
        self._InstalledDeviceNum = InstalledDeviceNum

    @property
    def PiracyInstalledDeviceNum(self):
        r"""盗版安装设备数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PiracyInstalledDeviceNum

    @PiracyInstalledDeviceNum.setter
    def PiracyInstalledDeviceNum(self, PiracyInstalledDeviceNum):
        self._PiracyInstalledDeviceNum = PiracyInstalledDeviceNum

    @property
    def InstalledUserNum(self):
        r"""安装用户数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InstalledUserNum

    @InstalledUserNum.setter
    def InstalledUserNum(self, InstalledUserNum):
        self._InstalledUserNum = InstalledUserNum

    @property
    def PiracyInstalledUserNum(self):
        r"""盗版安装用户数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PiracyInstalledUserNum

    @PiracyInstalledUserNum.setter
    def PiracyInstalledUserNum(self, PiracyInstalledUserNum):
        self._PiracyInstalledUserNum = PiracyInstalledUserNum

    @property
    def AuthNum(self):
        r"""授权数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AuthNum

    @AuthNum.setter
    def AuthNum(self, AuthNum):
        self._AuthNum = AuthNum

    @property
    def GenuineRate(self):
        r"""正版率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._GenuineRate

    @GenuineRate.setter
    def GenuineRate(self, GenuineRate):
        self._GenuineRate = GenuineRate

    @property
    def UpgradableDeviceNum(self):
        r"""有新版本可升级的设备数量
        :rtype: int
        """
        return self._UpgradableDeviceNum

    @UpgradableDeviceNum.setter
    def UpgradableDeviceNum(self, UpgradableDeviceNum):
        self._UpgradableDeviceNum = UpgradableDeviceNum

    @property
    def UpgradableVersions(self):
        r"""当前可升级的最新版本信息, 每一项均为json字符串
        :rtype: list of str
        """
        return self._UpgradableVersions

    @UpgradableVersions.setter
    def UpgradableVersions(self, UpgradableVersions):
        self._UpgradableVersions = UpgradableVersions


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._OsType = params.get("OsType")
        self._PiracyRisk = params.get("PiracyRisk")
        self._Corp = params.get("Corp")
        if params.get("SoftVersionDist") is not None:
            self._SoftVersionDist = []
            for item in params.get("SoftVersionDist"):
                obj = SoftVersionAndNum()
                obj._deserialize(item)
                self._SoftVersionDist.append(obj)
        if params.get("PiracyVersionDist") is not None:
            self._PiracyVersionDist = []
            for item in params.get("PiracyVersionDist"):
                obj = SoftVersionAndNum()
                obj._deserialize(item)
                self._PiracyVersionDist.append(obj)
        self._InstalledDeviceNum = params.get("InstalledDeviceNum")
        self._PiracyInstalledDeviceNum = params.get("PiracyInstalledDeviceNum")
        self._InstalledUserNum = params.get("InstalledUserNum")
        self._PiracyInstalledUserNum = params.get("PiracyInstalledUserNum")
        self._AuthNum = params.get("AuthNum")
        self._GenuineRate = params.get("GenuineRate")
        self._UpgradableDeviceNum = params.get("UpgradableDeviceNum")
        self._UpgradableVersions = params.get("UpgradableVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggrSoftDetailRequest(AbstractModel):
    r"""DescribeAggrSoftDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 软件名称
        :type Name: str
        :param _OsType: 操作系统
        :type OsType: int
        """
        self._Name = None
        self._OsType = None

    @property
    def Name(self):
        r"""软件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OsType(self):
        r"""操作系统
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._OsType = params.get("OsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggrSoftDetailResponse(AbstractModel):
    r"""DescribeAggrSoftDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftDetailData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftDetailData`
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
            self._Data = DescribeAggrSoftDetailData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAggrSoftDeviceListData(AbstractModel):
    r"""聚合软件-已安装终端列表

    """

    def __init__(self):
        r"""
        :param _Page: 分页公共对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _AggrSoftDeviceList: 详情
注意：此字段可能返回 null，表示取不到有效值。
        :type AggrSoftDeviceList: list of AggrSoftDeviceRow
        """
        self._Page = None
        self._Total = None
        self._AggrSoftDeviceList = None

    @property
    def Page(self):
        r"""分页公共对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Total(self):
        r"""总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AggrSoftDeviceList(self):
        r"""详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AggrSoftDeviceRow
        """
        return self._AggrSoftDeviceList

    @AggrSoftDeviceList.setter
    def AggrSoftDeviceList(self, AggrSoftDeviceList):
        self._AggrSoftDeviceList = AggrSoftDeviceList


    def _deserialize(self, params):
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        self._Total = params.get("Total")
        if params.get("AggrSoftDeviceList") is not None:
            self._AggrSoftDeviceList = []
            for item in params.get("AggrSoftDeviceList"):
                obj = AggrSoftDeviceRow()
                obj._deserialize(item)
                self._AggrSoftDeviceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggrSoftDeviceListRequest(AbstractModel):
    r"""DescribeAggrSoftDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Condition: 过滤条件
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _Name: 软件名
        :type Name: str
        :param _OsType: 0:win 2:mac
        :type OsType: int
        """
        self._Condition = None
        self._Name = None
        self._OsType = None

    @property
    def Condition(self):
        r"""过滤条件
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def Name(self):
        r"""软件名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OsType(self):
        r"""0:win 2:mac
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType


    def _deserialize(self, params):
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._Name = params.get("Name")
        self._OsType = params.get("OsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggrSoftDeviceListResponse(AbstractModel):
    r"""DescribeAggrSoftDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 已安装终端列表
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftDeviceListData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""已安装终端列表
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeAggrSoftDeviceListData`
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
            self._Data = DescribeAggrSoftDeviceListData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDLPEdgeNodeGroupsRequest(AbstractModel):
    r"""DescribeDLPEdgeNodeGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _Condition: 过滤条件
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        self._DomainInstanceId = None
        self._Condition = None

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def Condition(self):
        r"""过滤条件
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition


    def _deserialize(self, params):
        self._DomainInstanceId = params.get("DomainInstanceId")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDLPEdgeNodeGroupsResponse(AbstractModel):
    r"""DescribeDLPEdgeNodeGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务响应数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPEdgeNodeGroupsRspData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务响应数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPEdgeNodeGroupsRspData`
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
            self._Data = DescribeDLPEdgeNodeGroupsRspData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDLPEdgeNodeGroupsRspData(AbstractModel):
    r"""业务响应数据

    """

    def __init__(self):
        r"""
        :param _Items: 分组信息
        :type Items: list of DescribeDLPEdgeNodeGroupsRspItem
        :param _Page: 分页信息
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        self._Items = None
        self._Page = None

    @property
    def Items(self):
        r"""分组信息
        :rtype: list of DescribeDLPEdgeNodeGroupsRspItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Page(self):
        r"""分页信息
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeDLPEdgeNodeGroupsRspItem()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDLPEdgeNodeGroupsRspItem(AbstractModel):
    r"""节点分组信息

    """

    def __init__(self):
        r"""
        :param _Id: 自增id，数据库中唯一
        :type Id: int
        :param _GroupName: 节点分组名称
        :type GroupName: str
        :param _GroupId: 节点分组id
        :type GroupId: str
        :param _EdgeCount: 包含边缘节点数量
        :type EdgeCount: int
        """
        self._Id = None
        self._GroupName = None
        self._GroupId = None
        self._EdgeCount = None

    @property
    def Id(self):
        r"""自增id，数据库中唯一
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def GroupName(self):
        r"""节点分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        r"""节点分组id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EdgeCount(self):
        r"""包含边缘节点数量
        :rtype: int
        """
        return self._EdgeCount

    @EdgeCount.setter
    def EdgeCount(self, EdgeCount):
        self._EdgeCount = EdgeCount


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._EdgeCount = params.get("EdgeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDLPEdgeNodesPageData(AbstractModel):
    r"""业务响应数据

    """

    def __init__(self):
        r"""
        :param _Page: 分页信息
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        :param _Items: 节点列表
        :type Items: list of DescribeDLPEdgeNodesRspItem
        """
        self._Page = None
        self._Items = None

    @property
    def Page(self):
        r"""分页信息
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Items(self):
        r"""节点列表
        :rtype: list of DescribeDLPEdgeNodesRspItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeDLPEdgeNodesRspItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDLPEdgeNodesRequest(AbstractModel):
    r"""DescribeDLPEdgeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _Condition: 过滤条件、分页参数<li>EdgeNodeName - string - 是否必填：否 - 操作符: ilike  - 排序支持：否- 按节点名称过滤。</li>
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        self._DomainInstanceId = None
        self._Condition = None

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def Condition(self):
        r"""过滤条件、分页参数<li>EdgeNodeName - string - 是否必填：否 - 操作符: ilike  - 排序支持：否- 按节点名称过滤。</li>
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition


    def _deserialize(self, params):
        self._DomainInstanceId = params.get("DomainInstanceId")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDLPEdgeNodesResponse(AbstractModel):
    r"""DescribeDLPEdgeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务响应数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPEdgeNodesPageData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务响应数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPEdgeNodesPageData`
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
            self._Data = DescribeDLPEdgeNodesPageData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDLPEdgeNodesRspItem(AbstractModel):
    r"""边缘节点信息

    """

    def __init__(self):
        r"""
        :param _Id: 自增id，数据库中唯一
        :type Id: int
        :param _GroupId: 节点分组唯一id
        :type GroupId: str
        :param _EdgeNodeId: 节点id
        :type EdgeNodeId: str
        :param _EdgeNodeName: 节点名称
        :type EdgeNodeName: str
        :param _IsActive: 是否活跃/连通
        :type IsActive: bool
        :param _GroupName: 节点分组名称
        :type GroupName: str
        :param _Ip: 节点IP
        :type Ip: str
        :param _Version: 节点版本
        :type Version: str
        :param _IsUpgradeEnable: 是否支持升级连接器
        :type IsUpgradeEnable: bool
        :param _UpgradeStatus: 升级状态: 0(升级中) , 1(升级失败) 或 2(升级成功)
        :type UpgradeStatus: int
        :param _UpgradeDescription: 升级状态描述
        :type UpgradeDescription: str
        :param _RuleVersion: 规则版本
        :type RuleVersion: str
        """
        self._Id = None
        self._GroupId = None
        self._EdgeNodeId = None
        self._EdgeNodeName = None
        self._IsActive = None
        self._GroupName = None
        self._Ip = None
        self._Version = None
        self._IsUpgradeEnable = None
        self._UpgradeStatus = None
        self._UpgradeDescription = None
        self._RuleVersion = None

    @property
    def Id(self):
        r"""自增id，数据库中唯一
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def GroupId(self):
        r"""节点分组唯一id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EdgeNodeId(self):
        r"""节点id
        :rtype: str
        """
        return self._EdgeNodeId

    @EdgeNodeId.setter
    def EdgeNodeId(self, EdgeNodeId):
        self._EdgeNodeId = EdgeNodeId

    @property
    def EdgeNodeName(self):
        r"""节点名称
        :rtype: str
        """
        return self._EdgeNodeName

    @EdgeNodeName.setter
    def EdgeNodeName(self, EdgeNodeName):
        self._EdgeNodeName = EdgeNodeName

    @property
    def IsActive(self):
        r"""是否活跃/连通
        :rtype: bool
        """
        return self._IsActive

    @IsActive.setter
    def IsActive(self, IsActive):
        self._IsActive = IsActive

    @property
    def GroupName(self):
        r"""节点分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Ip(self):
        r"""节点IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Version(self):
        r"""节点版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def IsUpgradeEnable(self):
        r"""是否支持升级连接器
        :rtype: bool
        """
        return self._IsUpgradeEnable

    @IsUpgradeEnable.setter
    def IsUpgradeEnable(self, IsUpgradeEnable):
        self._IsUpgradeEnable = IsUpgradeEnable

    @property
    def UpgradeStatus(self):
        r"""升级状态: 0(升级中) , 1(升级失败) 或 2(升级成功)
        :rtype: int
        """
        return self._UpgradeStatus

    @UpgradeStatus.setter
    def UpgradeStatus(self, UpgradeStatus):
        self._UpgradeStatus = UpgradeStatus

    @property
    def UpgradeDescription(self):
        r"""升级状态描述
        :rtype: str
        """
        return self._UpgradeDescription

    @UpgradeDescription.setter
    def UpgradeDescription(self, UpgradeDescription):
        self._UpgradeDescription = UpgradeDescription

    @property
    def RuleVersion(self):
        r"""规则版本
        :rtype: str
        """
        return self._RuleVersion

    @RuleVersion.setter
    def RuleVersion(self, RuleVersion):
        self._RuleVersion = RuleVersion


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._GroupId = params.get("GroupId")
        self._EdgeNodeId = params.get("EdgeNodeId")
        self._EdgeNodeName = params.get("EdgeNodeName")
        self._IsActive = params.get("IsActive")
        self._GroupName = params.get("GroupName")
        self._Ip = params.get("Ip")
        self._Version = params.get("Version")
        self._IsUpgradeEnable = params.get("IsUpgradeEnable")
        self._UpgradeStatus = params.get("UpgradeStatus")
        self._UpgradeDescription = params.get("UpgradeDescription")
        self._RuleVersion = params.get("RuleVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDLPFileDetectResultData(AbstractModel):
    r"""查询文件检测结果响应数据

    """

    def __init__(self):
        r"""
        :param _FileMd5: 提交任务时的文件md5
        :type FileMd5: str
        :param _FileName: 提交任务时的文件名
        :type FileName: str
        :param _Status: 状态：等待检测->正在检测->检测失败/检测成功。或任务不存在
        :type Status: str
        :param _DetectResult: 文件检测结果，json字符串。包含文件基本信息如type，path，md5以及命中的信息。其中State为检测状态，0为待解析文件，1为检测中，2为检测完成；FileAbstract为命中的上下文摘要信息，HitRuleid是命中的规则唯一ID，HitRuleCategoryId是规则分类唯一id，HitLevel是文件的等级，HitRuleDesc是规则的名称，HitContent是具体命中的规则以及词库信息，以及命中的内容。EngineConfigVersion是当前词库版本号
        :type DetectResult: str
        """
        self._FileMd5 = None
        self._FileName = None
        self._Status = None
        self._DetectResult = None

    @property
    def FileMd5(self):
        r"""提交任务时的文件md5
        :rtype: str
        """
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def FileName(self):
        r"""提交任务时的文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Status(self):
        r"""状态：等待检测->正在检测->检测失败/检测成功。或任务不存在
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DetectResult(self):
        r"""文件检测结果，json字符串。包含文件基本信息如type，path，md5以及命中的信息。其中State为检测状态，0为待解析文件，1为检测中，2为检测完成；FileAbstract为命中的上下文摘要信息，HitRuleid是命中的规则唯一ID，HitRuleCategoryId是规则分类唯一id，HitLevel是文件的等级，HitRuleDesc是规则的名称，HitContent是具体命中的规则以及词库信息，以及命中的内容。EngineConfigVersion是当前词库版本号
        :rtype: str
        """
        return self._DetectResult

    @DetectResult.setter
    def DetectResult(self, DetectResult):
        self._DetectResult = DetectResult


    def _deserialize(self, params):
        self._FileMd5 = params.get("FileMd5")
        self._FileName = params.get("FileName")
        self._Status = params.get("Status")
        self._DetectResult = params.get("DetectResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDLPFileDetectResultRequest(AbstractModel):
    r"""DescribeDLPFileDetectResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _QueryID: 查询ID，即提交送检任务接口（CreateDLPFileDetectionTask）返回的任务ID（DLPFileDetectionTaskID）
        :type QueryID: str
        """
        self._DomainInstanceId = None
        self._QueryID = None

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def QueryID(self):
        r"""查询ID，即提交送检任务接口（CreateDLPFileDetectionTask）返回的任务ID（DLPFileDetectionTaskID）
        :rtype: str
        """
        return self._QueryID

    @QueryID.setter
    def QueryID(self, QueryID):
        self._QueryID = QueryID


    def _deserialize(self, params):
        self._DomainInstanceId = params.get("DomainInstanceId")
        self._QueryID = params.get("QueryID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDLPFileDetectResultResponse(AbstractModel):
    r"""DescribeDLPFileDetectResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 文件鉴定任务结果数据。详情查看具体数据结构
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPFileDetectResultData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""文件鉴定任务结果数据。详情查看具体数据结构
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPFileDetectResultData`
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
            self._Data = DescribeDLPFileDetectResultData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDLPFileDetectTaskResult(AbstractModel):
    r"""查询文件检测结果响应数据

    """

    def __init__(self):
        r"""
        :param _FileMd5: 提交任务时的文件md5
        :type FileMd5: str
        :param _FileName: 提交任务时的文件名
        :type FileName: str
        :param _Status: 检测执行状态：0未执行 1等待执行 2执行中 3执行失败 4执行完成 
        :type Status: int
        :param _DetectResult:     FileAbstract:文件摘要
    FileAttr:文件属性
    FileCategory:命中分级分类 array
    FileContent:命中信息json(array)
	            RuleId:规则Id
				RuleName:规则名称
				RuleLevel:规则等级
				Hits：命中词库内容
				    LibraryId：词库Id
					LibraryType:词库类型
					LibraryName:词库名称
					Attribute: 命中属性 doc.Content文件内容|doc.FileSize文件大小|doc.Name文件名|doc.Type文件类型
					String  待匹配内容
					Content 命中内容
                HitsTotal 规则命中次数
    FileMd5 文件ND5
    FileName 文件名
    FileSize 文件大小
    FileType 文件后缀
    FileTypeName 文件类型名称
    FinalDataLevel 命中最高等级
    NodeId 节点唯一Id
    NodeIp 节点IP
    NodeName 节点名称
    OperateTime 文件操作时间
    Url 文件下载Url
        :type DetectResult: str
        :param _Message: 检测执行状态描述
        :type Message: str
        """
        self._FileMd5 = None
        self._FileName = None
        self._Status = None
        self._DetectResult = None
        self._Message = None

    @property
    def FileMd5(self):
        r"""提交任务时的文件md5
        :rtype: str
        """
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def FileName(self):
        r"""提交任务时的文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Status(self):
        r"""检测执行状态：0未执行 1等待执行 2执行中 3执行失败 4执行完成 
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DetectResult(self):
        r"""    FileAbstract:文件摘要
    FileAttr:文件属性
    FileCategory:命中分级分类 array
    FileContent:命中信息json(array)
	            RuleId:规则Id
				RuleName:规则名称
				RuleLevel:规则等级
				Hits：命中词库内容
				    LibraryId：词库Id
					LibraryType:词库类型
					LibraryName:词库名称
					Attribute: 命中属性 doc.Content文件内容|doc.FileSize文件大小|doc.Name文件名|doc.Type文件类型
					String  待匹配内容
					Content 命中内容
                HitsTotal 规则命中次数
    FileMd5 文件ND5
    FileName 文件名
    FileSize 文件大小
    FileType 文件后缀
    FileTypeName 文件类型名称
    FinalDataLevel 命中最高等级
    NodeId 节点唯一Id
    NodeIp 节点IP
    NodeName 节点名称
    OperateTime 文件操作时间
    Url 文件下载Url
        :rtype: str
        """
        return self._DetectResult

    @DetectResult.setter
    def DetectResult(self, DetectResult):
        self._DetectResult = DetectResult

    @property
    def Message(self):
        r"""检测执行状态描述
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._FileMd5 = params.get("FileMd5")
        self._FileName = params.get("FileName")
        self._Status = params.get("Status")
        self._DetectResult = params.get("DetectResult")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDLPFileDetectTaskResultRequest(AbstractModel):
    r"""DescribeDLPFileDetectTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _TaskRequestId: 任务请求Id
        :type TaskRequestId: str
        """
        self._DomainInstanceId = None
        self._TaskRequestId = None

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def TaskRequestId(self):
        r"""任务请求Id
        :rtype: str
        """
        return self._TaskRequestId

    @TaskRequestId.setter
    def TaskRequestId(self, TaskRequestId):
        self._TaskRequestId = TaskRequestId


    def _deserialize(self, params):
        self._DomainInstanceId = params.get("DomainInstanceId")
        self._TaskRequestId = params.get("TaskRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDLPFileDetectTaskResultResponse(AbstractModel):
    r"""DescribeDLPFileDetectTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 文件鉴定任务结果数据。详情查看具体数据结构
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPFileDetectTaskResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""文件鉴定任务结果数据。详情查看具体数据结构
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDLPFileDetectTaskResult`
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
            self._Data = DescribeDLPFileDetectTaskResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceChildGroupsRequest(AbstractModel):
    r"""DescribeDeviceChildGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _Condition: 过滤条件参数（字段含义请参考接口返回值）
- Name, 类型String，支持操作：【like，ilike】，支持排序




分页参数
- PageNum 从1开始，小于等于0时使用默认参数
- PageSize 最大值5000，最好不超过100
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _ParentId: 父分组id，默认0：表示获取全网终端分组
        :type ParentId: int
        :param _OsType: 操作系统类型（0：win，1：linux，2：mac，4：android，5：ios；默认0：系统win）
        :type OsType: int
        """
        self._DomainInstanceId = None
        self._Condition = None
        self._ParentId = None
        self._OsType = None

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def Condition(self):
        r"""过滤条件参数（字段含义请参考接口返回值）
- Name, 类型String，支持操作：【like，ilike】，支持排序




分页参数
- PageNum 从1开始，小于等于0时使用默认参数
- PageSize 最大值5000，最好不超过100
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def ParentId(self):
        r"""父分组id，默认0：表示获取全网终端分组
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def OsType(self):
        r"""操作系统类型（0：win，1：linux，2：mac，4：android，5：ios；默认0：系统win）
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType


    def _deserialize(self, params):
        self._DomainInstanceId = params.get("DomainInstanceId")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._ParentId = params.get("ParentId")
        self._OsType = params.get("OsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceChildGroupsResponse(AbstractModel):
    r"""DescribeDeviceChildGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询设备组子分组详情响应结构
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceChildGroupsRspData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""查询设备组子分组详情响应结构
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceChildGroupsRspData`
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
            self._Data = DescribeDeviceChildGroupsRspData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceChildGroupsRspData(AbstractModel):
    r"""查询设备组子分组详情响应结构

    """

    def __init__(self):
        r"""
        :param _Items: 返回的数组列表
        :type Items: list of DeviceGroupDetail
        """
        self._Items = None

    @property
    def Items(self):
        r"""返回的数组列表
        :rtype: list of DeviceGroupDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DeviceGroupDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDetailListData(AbstractModel):
    r"""终端详情响应对象集合

    """

    def __init__(self):
        r"""
        :param _UserName: 账号名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _ComputerName: 计算机名
注意：此字段可能返回 null，表示取不到有效值。
        :type ComputerName: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _AccountGroupIdPath: 用户组IdPath
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroupIdPath: str
        :param _AccountGroupId: 用户组id(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroupId: int
        :param _GroupNamePath: 终端组名path
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupNamePath: str
        :param _Ip: Ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _AccountGroupName: 用户组名
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroupName: str
        :param _GroupIdPath: 终端组IdPath
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupIdPath: str
        :param _Mid: 唯一标识Mid
注意：此字段可能返回 null，表示取不到有效值。
        :type Mid: str
        :param _IoaUserName: IOA账号名
注意：此字段可能返回 null，表示取不到有效值。
        :type IoaUserName: str
        :param _GroupId: 所在分组Id(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: int
        :param _GroupName: 所在分组Name
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _Mac: Mac地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Mac: str
        :param _Version: 软件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _AccountGroupNamePath: 用户组名Path
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroupNamePath: str
        :param _Id: 列表Id(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        """
        self._UserName = None
        self._ComputerName = None
        self._Name = None
        self._AccountGroupIdPath = None
        self._AccountGroupId = None
        self._GroupNamePath = None
        self._Ip = None
        self._AccountGroupName = None
        self._GroupIdPath = None
        self._Mid = None
        self._IoaUserName = None
        self._GroupId = None
        self._GroupName = None
        self._Mac = None
        self._Version = None
        self._AccountGroupNamePath = None
        self._Id = None

    @property
    def UserName(self):
        r"""账号名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ComputerName(self):
        r"""计算机名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ComputerName

    @ComputerName.setter
    def ComputerName(self, ComputerName):
        self._ComputerName = ComputerName

    @property
    def Name(self):
        r"""名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AccountGroupIdPath(self):
        r"""用户组IdPath
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountGroupIdPath

    @AccountGroupIdPath.setter
    def AccountGroupIdPath(self, AccountGroupIdPath):
        self._AccountGroupIdPath = AccountGroupIdPath

    @property
    def AccountGroupId(self):
        r"""用户组id(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def GroupNamePath(self):
        r"""终端组名path
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupNamePath

    @GroupNamePath.setter
    def GroupNamePath(self, GroupNamePath):
        self._GroupNamePath = GroupNamePath

    @property
    def Ip(self):
        r"""Ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def AccountGroupName(self):
        r"""用户组名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountGroupName

    @AccountGroupName.setter
    def AccountGroupName(self, AccountGroupName):
        self._AccountGroupName = AccountGroupName

    @property
    def GroupIdPath(self):
        r"""终端组IdPath
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupIdPath

    @GroupIdPath.setter
    def GroupIdPath(self, GroupIdPath):
        self._GroupIdPath = GroupIdPath

    @property
    def Mid(self):
        r"""唯一标识Mid
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid

    @property
    def IoaUserName(self):
        r"""IOA账号名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IoaUserName

    @IoaUserName.setter
    def IoaUserName(self, IoaUserName):
        self._IoaUserName = IoaUserName

    @property
    def GroupId(self):
        r"""所在分组Id(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""所在分组Name
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Mac(self):
        r"""Mac地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def Version(self):
        r"""软件版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def AccountGroupNamePath(self):
        r"""用户组名Path
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountGroupNamePath

    @AccountGroupNamePath.setter
    def AccountGroupNamePath(self, AccountGroupNamePath):
        self._AccountGroupNamePath = AccountGroupNamePath

    @property
    def Id(self):
        r"""列表Id(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._ComputerName = params.get("ComputerName")
        self._Name = params.get("Name")
        self._AccountGroupIdPath = params.get("AccountGroupIdPath")
        self._AccountGroupId = params.get("AccountGroupId")
        self._GroupNamePath = params.get("GroupNamePath")
        self._Ip = params.get("Ip")
        self._AccountGroupName = params.get("AccountGroupName")
        self._GroupIdPath = params.get("GroupIdPath")
        self._Mid = params.get("Mid")
        self._IoaUserName = params.get("IoaUserName")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Mac = params.get("Mac")
        self._Version = params.get("Version")
        self._AccountGroupNamePath = params.get("AccountGroupNamePath")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDetailListPageData(AbstractModel):
    r"""业务响应数据

    """

    def __init__(self):
        r"""
        :param _Items: 终端详情响应对象集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of DescribeDeviceDetailListData
        :param _Page: 分页公共对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        self._Items = None
        self._Page = None

    @property
    def Items(self):
        r"""终端详情响应对象集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DescribeDeviceDetailListData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Page(self):
        r"""分页公共对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeDeviceDetailListData()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDetailListRequest(AbstractModel):
    r"""DescribeDeviceDetailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OsType: 系统类型(只支持32位)
        :type OsType: int
        :param _GroupId: 终端分组id(只支持32位)
        :type GroupId: int
        :param _Condition: 过滤条件、分页参数
<li>Name - String - 过滤支持：是 - 操作符:eq,like - 排序支持：是 。</li>
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        self._OsType = None
        self._GroupId = None
        self._Condition = None

    @property
    def OsType(self):
        r"""系统类型(只支持32位)
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def GroupId(self):
        r"""终端分组id(只支持32位)
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Condition(self):
        r"""过滤条件、分页参数
<li>Name - String - 过滤支持：是 - 操作符:eq,like - 排序支持：是 。</li>
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition


    def _deserialize(self, params):
        self._OsType = params.get("OsType")
        self._GroupId = params.get("GroupId")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDetailListResponse(AbstractModel):
    r"""DescribeDeviceDetailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceDetailListPageData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceDetailListPageData`
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
            self._Data = DescribeDeviceDetailListPageData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceHardwareInfoItem(AbstractModel):
    r"""终端硬件信息列表Item数据

    """

    def __init__(self):
        r"""
        :param _Id: 设备ID
        :type Id: int
        :param _Mid: 设备唯一标识符
        :type Mid: str
        :param _OsType: OS平台 0 Windows 1 Linux 2 macOS 4 Android 5 iOS
        :type OsType: int
        :param _Name: 终端名
        :type Name: str
        :param _UserName: 终端用户名
        :type UserName: str
        :param _Status: 授权状态（ 4未授权 5已授权）
        :type Status: int
        :param _GroupId: 设备所属分组ID
        :type GroupId: int
        :param _GroupName: 设备所属分组名
        :type GroupName: str
        :param _GroupNamePath: 设备所属分组路径
        :type GroupNamePath: str
        :param _AccountName: 最近登录账户的姓名
        :type AccountName: str
        :param _Ip: 出口IP
        :type Ip: str
        :param _MacAddr: MAC地址
        :type MacAddr: str
        :param _Cpu: CPU品牌型号
        :type Cpu: str
        :param _Memory: 内存信息
        :type Memory: str
        :param _HardDiskSize: 硬盘信息
        :type HardDiskSize: str
        :param _Monitor: 显示器品牌型号
        :type Monitor: str
        :param _RemarkName: 终端备注名
        :type RemarkName: str
        """
        self._Id = None
        self._Mid = None
        self._OsType = None
        self._Name = None
        self._UserName = None
        self._Status = None
        self._GroupId = None
        self._GroupName = None
        self._GroupNamePath = None
        self._AccountName = None
        self._Ip = None
        self._MacAddr = None
        self._Cpu = None
        self._Memory = None
        self._HardDiskSize = None
        self._Monitor = None
        self._RemarkName = None

    @property
    def Id(self):
        r"""设备ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Mid(self):
        r"""设备唯一标识符
        :rtype: str
        """
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid

    @property
    def OsType(self):
        r"""OS平台 0 Windows 1 Linux 2 macOS 4 Android 5 iOS
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def Name(self):
        r"""终端名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UserName(self):
        r"""终端用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Status(self):
        r"""授权状态（ 4未授权 5已授权）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GroupId(self):
        r"""设备所属分组ID
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""设备所属分组名
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupNamePath(self):
        r"""设备所属分组路径
        :rtype: str
        """
        return self._GroupNamePath

    @GroupNamePath.setter
    def GroupNamePath(self, GroupNamePath):
        self._GroupNamePath = GroupNamePath

    @property
    def AccountName(self):
        r"""最近登录账户的姓名
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Ip(self):
        r"""出口IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def MacAddr(self):
        r"""MAC地址
        :rtype: str
        """
        return self._MacAddr

    @MacAddr.setter
    def MacAddr(self, MacAddr):
        self._MacAddr = MacAddr

    @property
    def Cpu(self):
        r"""CPU品牌型号
        :rtype: str
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""内存信息
        :rtype: str
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def HardDiskSize(self):
        r"""硬盘信息
        :rtype: str
        """
        return self._HardDiskSize

    @HardDiskSize.setter
    def HardDiskSize(self, HardDiskSize):
        self._HardDiskSize = HardDiskSize

    @property
    def Monitor(self):
        r"""显示器品牌型号
        :rtype: str
        """
        return self._Monitor

    @Monitor.setter
    def Monitor(self, Monitor):
        self._Monitor = Monitor

    @property
    def RemarkName(self):
        r"""终端备注名
        :rtype: str
        """
        return self._RemarkName

    @RemarkName.setter
    def RemarkName(self, RemarkName):
        self._RemarkName = RemarkName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Mid = params.get("Mid")
        self._OsType = params.get("OsType")
        self._Name = params.get("Name")
        self._UserName = params.get("UserName")
        self._Status = params.get("Status")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._GroupNamePath = params.get("GroupNamePath")
        self._AccountName = params.get("AccountName")
        self._Ip = params.get("Ip")
        self._MacAddr = params.get("MacAddr")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._HardDiskSize = params.get("HardDiskSize")
        self._Monitor = params.get("Monitor")
        self._RemarkName = params.get("RemarkName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceHardwareInfoListRequest(AbstractModel):
    r"""DescribeDeviceHardwareInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 【必填】设备分组id（需要和OsType匹配），下面是私有化场景下默认id：id-名称-操作系统1	全网终端	Win2	未分组终端	Win30000000	服务器	Win40000101	全网终端	Linux40000102	未分组终端	Linux40000103	服务器	Linux40000201	全网终端	macOS40000202	未分组终端	macOS40000203	服务器	macOS40000401	全网终端	Android40000402	未分组终端	Android40000501	全网终端	iOS40000502	未分组终端	iOSSaaS需要调用分组接口DescribeDeviceChildGroups获取对应分组id
        :type GroupId: int
        :param _OsType: 【必填】操作系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0），需要和GroupId或者GroupIds匹配
        :type OsType: int
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _Condition: 过滤条件参数（字段含义请参考接口返回值）  - Name, 类型String，支持操作：【eq，like，ilike】，支持排序  - UserName, 类型String，支持操作：【eq，like，ilike】，支持排序  - IoaUserName，类型String，支持操作：【eq，like，ilike】，支持排序  - MacAddr, 类型String，支持操作：【eq，like，ilike】，支持排序  - Ip, 类型String，支持操作：【eq，like，ilike】，支持排序  - Mid, 类型String，支持操作：【eq，like，ilike】，支持排序  ，支持排序分页参数  - PageNum 从1开始，小于等于0时使用默认参数 - PageSize 最大值5000，最好不超过100
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        self._GroupId = None
        self._OsType = None
        self._DomainInstanceId = None
        self._Condition = None

    @property
    def GroupId(self):
        r"""【必填】设备分组id（需要和OsType匹配），下面是私有化场景下默认id：id-名称-操作系统1	全网终端	Win2	未分组终端	Win30000000	服务器	Win40000101	全网终端	Linux40000102	未分组终端	Linux40000103	服务器	Linux40000201	全网终端	macOS40000202	未分组终端	macOS40000203	服务器	macOS40000401	全网终端	Android40000402	未分组终端	Android40000501	全网终端	iOS40000502	未分组终端	iOSSaaS需要调用分组接口DescribeDeviceChildGroups获取对应分组id
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def OsType(self):
        r"""【必填】操作系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0），需要和GroupId或者GroupIds匹配
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def Condition(self):
        r"""过滤条件参数（字段含义请参考接口返回值）  - Name, 类型String，支持操作：【eq，like，ilike】，支持排序  - UserName, 类型String，支持操作：【eq，like，ilike】，支持排序  - IoaUserName，类型String，支持操作：【eq，like，ilike】，支持排序  - MacAddr, 类型String，支持操作：【eq，like，ilike】，支持排序  - Ip, 类型String，支持操作：【eq，like，ilike】，支持排序  - Mid, 类型String，支持操作：【eq，like，ilike】，支持排序  ，支持排序分页参数  - PageNum 从1开始，小于等于0时使用默认参数 - PageSize 最大值5000，最好不超过100
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._OsType = params.get("OsType")
        self._DomainInstanceId = params.get("DomainInstanceId")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceHardwareInfoListResponse(AbstractModel):
    r"""DescribeDeviceHardwareInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 分页的data数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceHardwareInfoListRspData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""分页的data数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceHardwareInfoListRspData`
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
            self._Data = DescribeDeviceHardwareInfoListRspData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceHardwareInfoListRspData(AbstractModel):
    r"""终端硬件信息列表响应详情

    """

    def __init__(self):
        r"""
        :param _Page: 分页数据
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        :param _Items: 终端硬件信息数据数组
        :type Items: list of DescribeDeviceHardwareInfoItem
        """
        self._Page = None
        self._Items = None

    @property
    def Page(self):
        r"""分页数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Items(self):
        r"""终端硬件信息数据数组
        :rtype: list of DescribeDeviceHardwareInfoItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeDeviceHardwareInfoItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceInfoRequest(AbstractModel):
    r"""DescribeDeviceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _Mid: 终端id
        :type Mid: str
        :param _Type: 查询类型  process_list network_list service_list
        :type Type: str
        """
        self._DomainInstanceId = None
        self._Mid = None
        self._Type = None

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def Mid(self):
        r"""终端id
        :rtype: str
        """
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid

    @property
    def Type(self):
        r"""查询类型  process_list network_list service_list
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._DomainInstanceId = params.get("DomainInstanceId")
        self._Mid = params.get("Mid")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceInfoResponse(AbstractModel):
    r"""DescribeDeviceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceInfoRspData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceInfoRspData`
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
            self._Data = DescribeDeviceInfoRspData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceInfoRspData(AbstractModel):
    r"""业务响应数据

    """

    def __init__(self):
        r"""
        :param _ProcessList: 分页的具体数据对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessList: list of DeviceProcessInfo
        :param _NetworkList: 分页的具体数据对象
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkList: list of DeviceNetworkInfo
        :param _ServiceList: 分页的具体数据对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceList: list of DeviceServiceInfo
        """
        self._ProcessList = None
        self._NetworkList = None
        self._ServiceList = None

    @property
    def ProcessList(self):
        r"""分页的具体数据对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DeviceProcessInfo
        """
        return self._ProcessList

    @ProcessList.setter
    def ProcessList(self, ProcessList):
        self._ProcessList = ProcessList

    @property
    def NetworkList(self):
        r"""分页的具体数据对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DeviceNetworkInfo
        """
        return self._NetworkList

    @NetworkList.setter
    def NetworkList(self, NetworkList):
        self._NetworkList = NetworkList

    @property
    def ServiceList(self):
        r"""分页的具体数据对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DeviceServiceInfo
        """
        return self._ServiceList

    @ServiceList.setter
    def ServiceList(self, ServiceList):
        self._ServiceList = ServiceList


    def _deserialize(self, params):
        if params.get("ProcessList") is not None:
            self._ProcessList = []
            for item in params.get("ProcessList"):
                obj = DeviceProcessInfo()
                obj._deserialize(item)
                self._ProcessList.append(obj)
        if params.get("NetworkList") is not None:
            self._NetworkList = []
            for item in params.get("NetworkList"):
                obj = DeviceNetworkInfo()
                obj._deserialize(item)
                self._NetworkList.append(obj)
        if params.get("ServiceList") is not None:
            self._ServiceList = []
            for item in params.get("ServiceList"):
                obj = DeviceServiceInfo()
                obj._deserialize(item)
                self._ServiceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceVirtualGroupsPageRsp(AbstractModel):
    r"""查询返回终端自定义分组的Data数据

    """

    def __init__(self):
        r"""
        :param _Page: 分页公共对象
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        :param _Items: 终端自定义分组列表数据
        :type Items: list of DeviceVirtualDeviceGroupsDetail
        """
        self._Page = None
        self._Items = None

    @property
    def Page(self):
        r"""分页公共对象
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Items(self):
        r"""终端自定义分组列表数据
        :rtype: list of DeviceVirtualDeviceGroupsDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DeviceVirtualDeviceGroupsDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceVirtualGroupsRequest(AbstractModel):
    r"""DescribeDeviceVirtualGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _Condition: 滤条件、分页参数 <li>Name - String - 是否必填：否 - 操作符: like  - 排序支持：否- 按终端自定义分组过滤。</li> <li>DeviceVirtualGroupName - String - 是否必填：否 - 操作符: like  - 排序支持：否- 按终端自定义分组过滤。</li>
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _OsType: 系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0）
        :type OsType: int
        :param _VirtualGroupIds: 非必填，自定义分组ids
        :type VirtualGroupIds: list of int
        """
        self._DomainInstanceId = None
        self._Condition = None
        self._OsType = None
        self._VirtualGroupIds = None

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def Condition(self):
        r"""滤条件、分页参数 <li>Name - String - 是否必填：否 - 操作符: like  - 排序支持：否- 按终端自定义分组过滤。</li> <li>DeviceVirtualGroupName - String - 是否必填：否 - 操作符: like  - 排序支持：否- 按终端自定义分组过滤。</li>
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def OsType(self):
        r"""系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0）
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def VirtualGroupIds(self):
        r"""非必填，自定义分组ids
        :rtype: list of int
        """
        return self._VirtualGroupIds

    @VirtualGroupIds.setter
    def VirtualGroupIds(self, VirtualGroupIds):
        self._VirtualGroupIds = VirtualGroupIds


    def _deserialize(self, params):
        self._DomainInstanceId = params.get("DomainInstanceId")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._OsType = params.get("OsType")
        self._VirtualGroupIds = params.get("VirtualGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceVirtualGroupsResponse(AbstractModel):
    r"""DescribeDeviceVirtualGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询终端自定义分组的Data数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceVirtualGroupsPageRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""查询终端自定义分组的Data数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDeviceVirtualGroupsPageRsp`
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
            self._Data = DescribeDeviceVirtualGroupsPageRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDevicesPageRsp(AbstractModel):
    r"""分页的data数据

    """

    def __init__(self):
        r"""
        :param _Paging: 数据分页信息
        :type Paging: :class:`tencentcloud.ioa.v20220601.models.Paging`
        :param _Items: 业务响应数据
        :type Items: list of DeviceDetail
        """
        self._Paging = None
        self._Items = None

    @property
    def Paging(self):
        r"""数据分页信息
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Paging

    @Paging.setter
    def Paging(self, Paging):
        self._Paging = Paging

    @property
    def Items(self):
        r"""业务响应数据
        :rtype: list of DeviceDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Paging") is not None:
            self._Paging = Paging()
            self._Paging._deserialize(params.get("Paging"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DeviceDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesRequest(AbstractModel):
    r"""DescribeDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _Condition: 过滤条件参数（字段含义请参考接口返回值）

- Mid, 类型String，支持操作：【eq，like，ilike】，支持排序
- Name, 类型String，支持操作：【eq，like，ilike】，支持排序
- Itime, 类型String，支持操作：【eq，like，ilike】，支持排序
- UserName, 类型String，支持操作：【eq，like，ilike】，支持排序
- MacAddr, 类型String，支持操作：【eq，like，ilike】，支持排序
- UserId, 类型String，支持操作：【eq，like，ilike】，支持排序
- Ip, 类型String，支持操作：【eq，like，ilike】，支持排序
- Tags，类型String，支持操作：【eq，like，ilike】，支持排序
- LocalIpList，类型String，支持操作：【eq，like，ilike】，支持排序
- SerialNum，类型String，支持操作：【eq，like，ilike】，支持排序
- Version，类型String，支持操作：【eq，like，ilike】，支持排序
- StrVersion，类型String，支持操作：【eq，like，ilike】，支持排序
- RtpStatus，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- HostName，类型String，支持操作：【eq，like，ilike】，支持排序
- IoaUserName，类型String，支持操作：【eq，like，ilike】，支持排序
- GroupName，类型String，支持操作：【eq，like，ilike】，支持排序
- CriticalVulListCount，**类型Int**，支持操作：【eq】，**不支持排序**
- RiskCount，**类型Int**，支持操作：【eq】，**不支持排序**
- VulVersion，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- Virusver，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- SysRepver，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- BaseBoardSn，类型String，支持操作：【eq，like，ilike】，支持排序
- Os，类型String，支持操作：【eq，like，ilike】，支持排序
- ConnActiveTime，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- FirewallStatus，**类型Int**，支持操作：【eq】，**不支持排序**
- ProfileName，类型String，支持操作：【eq，like，ilike】，支持排序
- DomainName，类型String，支持操作：【eq，like，ilike】，支持排序
- SysRepVersion，类型String，支持操作：【eq，like，ilike】，支持排序
- VirusVer，类型String，支持操作：【eq，like，ilike】，支持排序
- Cpu，类型String，支持操作：【eq，like，ilike】，支持排序
- Memory，类型String，支持操作：【eq，like，ilike】，支持排序
- HardDiskSize，类型String，支持操作：【eq，like，ilike】，支持排序
- HardwareChangeCount，**类型Int**，支持操作：【eq】，支持排序
- AccountName，类型String，支持操作：【like.ilike】，支持排序
- AccountGroupName，类型String，支持操作：【like.ilike】，支持排序
- ScreenRecordingPermission，**类型Int**，支持操作：【eq】，支持排序
- DiskAccessPermission，**类型Int**，支持操作：【eq】，支持排序





分页参数
- PageNum 从1开始，小于等于0时使用默认参数
- PageSize 最大值5000，最好不超过100
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _GroupId: 【和GroupIds必须有一个填写】设备分组id（需要和OsType匹配），下面是私有化场景下默认id：
id-名称-操作系统
1	全网终端	Win
2	未分组终端	Win
30000000	服务器	Win
40000101	全网终端	Linux
40000102	未分组终端	Linux
40000103	服务器	Linux
40000201	全网终端	macOS
40000202	未分组终端	macOS
40000203	服务器	macOS
40000401	全网终端	Android
40000402	未分组终端	Android
40000501	全网终端	iOS
40000502	未分组终端	iOS


SaaS需要调用分组接口DescribeDeviceChildGroups获取对应分组id
        :type GroupId: int
        :param _OsType: 操作系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0），需要和GroupId或者GroupIds匹配
        :type OsType: int
        :param _OnlineStatus: 在线状态 （2表示在线，0或者1表示离线）
        :type OnlineStatus: int
        :param _Filters: 过滤条件--兼容旧接口,参数同Condition
        :type Filters: list of Filter
        :param _Sort: 排序字段--兼容旧接口,参数同Condition
        :type Sort: :class:`tencentcloud.ioa.v20220601.models.Sort`
        :param _PageNum: 获取第几页--兼容旧接口,参数同Condition
        :type PageNum: int
        :param _PageSize: 每页获取数--兼容旧接口,参数同Condition
        :type PageSize: int
        :param _Status: 授权状态： 4基础授权 5高级授权
        :type Status: int
        :param _GroupIds: 【和GroupId必须有一个填写】设备分组id列表（需要和OsType匹配）

        :type GroupIds: list of int
        """
        self._DomainInstanceId = None
        self._Condition = None
        self._GroupId = None
        self._OsType = None
        self._OnlineStatus = None
        self._Filters = None
        self._Sort = None
        self._PageNum = None
        self._PageSize = None
        self._Status = None
        self._GroupIds = None

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def Condition(self):
        r"""过滤条件参数（字段含义请参考接口返回值）

- Mid, 类型String，支持操作：【eq，like，ilike】，支持排序
- Name, 类型String，支持操作：【eq，like，ilike】，支持排序
- Itime, 类型String，支持操作：【eq，like，ilike】，支持排序
- UserName, 类型String，支持操作：【eq，like，ilike】，支持排序
- MacAddr, 类型String，支持操作：【eq，like，ilike】，支持排序
- UserId, 类型String，支持操作：【eq，like，ilike】，支持排序
- Ip, 类型String，支持操作：【eq，like，ilike】，支持排序
- Tags，类型String，支持操作：【eq，like，ilike】，支持排序
- LocalIpList，类型String，支持操作：【eq，like，ilike】，支持排序
- SerialNum，类型String，支持操作：【eq，like，ilike】，支持排序
- Version，类型String，支持操作：【eq，like，ilike】，支持排序
- StrVersion，类型String，支持操作：【eq，like，ilike】，支持排序
- RtpStatus，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- HostName，类型String，支持操作：【eq，like，ilike】，支持排序
- IoaUserName，类型String，支持操作：【eq，like，ilike】，支持排序
- GroupName，类型String，支持操作：【eq，like，ilike】，支持排序
- CriticalVulListCount，**类型Int**，支持操作：【eq】，**不支持排序**
- RiskCount，**类型Int**，支持操作：【eq】，**不支持排序**
- VulVersion，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- Virusver，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- SysRepver，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- BaseBoardSn，类型String，支持操作：【eq，like，ilike】，支持排序
- Os，类型String，支持操作：【eq，like，ilike】，支持排序
- ConnActiveTime，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- FirewallStatus，**类型Int**，支持操作：【eq】，**不支持排序**
- ProfileName，类型String，支持操作：【eq，like，ilike】，支持排序
- DomainName，类型String，支持操作：【eq，like，ilike】，支持排序
- SysRepVersion，类型String，支持操作：【eq，like，ilike】，支持排序
- VirusVer，类型String，支持操作：【eq，like，ilike】，支持排序
- Cpu，类型String，支持操作：【eq，like，ilike】，支持排序
- Memory，类型String，支持操作：【eq，like，ilike】，支持排序
- HardDiskSize，类型String，支持操作：【eq，like，ilike】，支持排序
- HardwareChangeCount，**类型Int**，支持操作：【eq】，支持排序
- AccountName，类型String，支持操作：【like.ilike】，支持排序
- AccountGroupName，类型String，支持操作：【like.ilike】，支持排序
- ScreenRecordingPermission，**类型Int**，支持操作：【eq】，支持排序
- DiskAccessPermission，**类型Int**，支持操作：【eq】，支持排序





分页参数
- PageNum 从1开始，小于等于0时使用默认参数
- PageSize 最大值5000，最好不超过100
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def GroupId(self):
        r"""【和GroupIds必须有一个填写】设备分组id（需要和OsType匹配），下面是私有化场景下默认id：
id-名称-操作系统
1	全网终端	Win
2	未分组终端	Win
30000000	服务器	Win
40000101	全网终端	Linux
40000102	未分组终端	Linux
40000103	服务器	Linux
40000201	全网终端	macOS
40000202	未分组终端	macOS
40000203	服务器	macOS
40000401	全网终端	Android
40000402	未分组终端	Android
40000501	全网终端	iOS
40000502	未分组终端	iOS


SaaS需要调用分组接口DescribeDeviceChildGroups获取对应分组id
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def OsType(self):
        r"""操作系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0），需要和GroupId或者GroupIds匹配
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OnlineStatus(self):
        r"""在线状态 （2表示在线，0或者1表示离线）
        :rtype: int
        """
        return self._OnlineStatus

    @OnlineStatus.setter
    def OnlineStatus(self, OnlineStatus):
        self._OnlineStatus = OnlineStatus

    @property
    def Filters(self):
        r"""过滤条件--兼容旧接口,参数同Condition
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sort(self):
        r"""排序字段--兼容旧接口,参数同Condition
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Sort`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def PageNum(self):
        r"""获取第几页--兼容旧接口,参数同Condition
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        r"""每页获取数--兼容旧接口,参数同Condition
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Status(self):
        r"""授权状态： 4基础授权 5高级授权
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GroupIds(self):
        r"""【和GroupId必须有一个填写】设备分组id列表（需要和OsType匹配）

        :rtype: list of int
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._DomainInstanceId = params.get("DomainInstanceId")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._GroupId = params.get("GroupId")
        self._OsType = params.get("OsType")
        self._OnlineStatus = params.get("OnlineStatus")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._Status = params.get("Status")
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    r"""DescribeDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 分页的data数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDevicesPageRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""分页的data数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDevicesPageRsp`
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
            self._Data = DescribeDevicesPageRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeLocalAccountAccountGroupsData(AbstractModel):
    r"""所属组

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: 组Id(只支持32位)
        :type AccountGroupId: int
        """
        self._AccountGroupId = None

    @property
    def AccountGroupId(self):
        r"""组Id(只支持32位)
        :rtype: int
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalAccountsData(AbstractModel):
    r"""获取账号列表响应的单个对象

    """

    def __init__(self):
        r"""
        :param _Id: uid，数据库中唯一
        :type Id: int
        :param _UserId: 账号，登录账号
        :type UserId: str
        :param _UserName: 用户名
        :type UserName: str
        :param _AccountId: 账号id，同Id字段
        :type AccountId: int
        :param _GroupId: 账号所在的分组id
        :type GroupId: int
        :param _GroupName: 账号所在的分组名称
        :type GroupName: str
        :param _NamePath: 账号所在的分组名称路径，用英文.分割
        :type NamePath: str
        :param _Source: 账号来源,0表示本地账号(只支持32位)
        :type Source: int
        :param _Status: 账号状态,0禁用，1启用(只支持32位)
        :type Status: int
        :param _Itime: 账号的创建时间
        :type Itime: str
        :param _Utime: 账号的最后更新时间
        :type Utime: str
        :param _ExtraInfo: 账号的扩展信息，包含邮箱、手机号、身份证、职位等信息
        :type ExtraInfo: str
        :param _RiskLevel: 用户风险等级，枚举：none, low, middle, high
        :type RiskLevel: str
        :param _AccountGroups: 所属组
        :type AccountGroups: list of DescribeLocalAccountAccountGroupsData
        :param _MobileBindNum: 绑定手机端设备数
        :type MobileBindNum: int
        :param _PcBindNum: 绑定Pc端设备数
        :type PcBindNum: int
        :param _OnlineStatus: 账号在线状态 1：在线 2：离线
        :type OnlineStatus: int
        :param _ActiveStatus: 账号活跃状态 1：活跃 2：非活跃
        :type ActiveStatus: int
        :param _LoginTime: 账号登录时间
        :type LoginTime: str
        :param _LogoutTime: 账号登出时间
        :type LogoutTime: str
        """
        self._Id = None
        self._UserId = None
        self._UserName = None
        self._AccountId = None
        self._GroupId = None
        self._GroupName = None
        self._NamePath = None
        self._Source = None
        self._Status = None
        self._Itime = None
        self._Utime = None
        self._ExtraInfo = None
        self._RiskLevel = None
        self._AccountGroups = None
        self._MobileBindNum = None
        self._PcBindNum = None
        self._OnlineStatus = None
        self._ActiveStatus = None
        self._LoginTime = None
        self._LogoutTime = None

    @property
    def Id(self):
        r"""uid，数据库中唯一
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def UserId(self):
        r"""账号，登录账号
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        r"""用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def AccountId(self):
        r"""账号id，同Id字段
        :rtype: int
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def GroupId(self):
        r"""账号所在的分组id
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""账号所在的分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def NamePath(self):
        r"""账号所在的分组名称路径，用英文.分割
        :rtype: str
        """
        return self._NamePath

    @NamePath.setter
    def NamePath(self, NamePath):
        self._NamePath = NamePath

    @property
    def Source(self):
        r"""账号来源,0表示本地账号(只支持32位)
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Status(self):
        r"""账号状态,0禁用，1启用(只支持32位)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Itime(self):
        r"""账号的创建时间
        :rtype: str
        """
        return self._Itime

    @Itime.setter
    def Itime(self, Itime):
        self._Itime = Itime

    @property
    def Utime(self):
        r"""账号的最后更新时间
        :rtype: str
        """
        return self._Utime

    @Utime.setter
    def Utime(self, Utime):
        self._Utime = Utime

    @property
    def ExtraInfo(self):
        r"""账号的扩展信息，包含邮箱、手机号、身份证、职位等信息
        :rtype: str
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def RiskLevel(self):
        r"""用户风险等级，枚举：none, low, middle, high
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def AccountGroups(self):
        r"""所属组
        :rtype: list of DescribeLocalAccountAccountGroupsData
        """
        return self._AccountGroups

    @AccountGroups.setter
    def AccountGroups(self, AccountGroups):
        self._AccountGroups = AccountGroups

    @property
    def MobileBindNum(self):
        r"""绑定手机端设备数
        :rtype: int
        """
        return self._MobileBindNum

    @MobileBindNum.setter
    def MobileBindNum(self, MobileBindNum):
        self._MobileBindNum = MobileBindNum

    @property
    def PcBindNum(self):
        r"""绑定Pc端设备数
        :rtype: int
        """
        return self._PcBindNum

    @PcBindNum.setter
    def PcBindNum(self, PcBindNum):
        self._PcBindNum = PcBindNum

    @property
    def OnlineStatus(self):
        r"""账号在线状态 1：在线 2：离线
        :rtype: int
        """
        return self._OnlineStatus

    @OnlineStatus.setter
    def OnlineStatus(self, OnlineStatus):
        self._OnlineStatus = OnlineStatus

    @property
    def ActiveStatus(self):
        r"""账号活跃状态 1：活跃 2：非活跃
        :rtype: int
        """
        return self._ActiveStatus

    @ActiveStatus.setter
    def ActiveStatus(self, ActiveStatus):
        self._ActiveStatus = ActiveStatus

    @property
    def LoginTime(self):
        r"""账号登录时间
        :rtype: str
        """
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def LogoutTime(self):
        r"""账号登出时间
        :rtype: str
        """
        return self._LogoutTime

    @LogoutTime.setter
    def LogoutTime(self, LogoutTime):
        self._LogoutTime = LogoutTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._AccountId = params.get("AccountId")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._NamePath = params.get("NamePath")
        self._Source = params.get("Source")
        self._Status = params.get("Status")
        self._Itime = params.get("Itime")
        self._Utime = params.get("Utime")
        self._ExtraInfo = params.get("ExtraInfo")
        self._RiskLevel = params.get("RiskLevel")
        if params.get("AccountGroups") is not None:
            self._AccountGroups = []
            for item in params.get("AccountGroups"):
                obj = DescribeLocalAccountAccountGroupsData()
                obj._deserialize(item)
                self._AccountGroups.append(obj)
        self._MobileBindNum = params.get("MobileBindNum")
        self._PcBindNum = params.get("PcBindNum")
        self._OnlineStatus = params.get("OnlineStatus")
        self._ActiveStatus = params.get("ActiveStatus")
        self._LoginTime = params.get("LoginTime")
        self._LogoutTime = params.get("LogoutTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalAccountsPage(AbstractModel):
    r"""获取账号列表响应的分页对象

    """

    def __init__(self):
        r"""
        :param _Page: 公共分页对象
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        :param _Items: 获取账号列表响应的单个对象
        :type Items: list of DescribeLocalAccountsData
        """
        self._Page = None
        self._Items = None

    @property
    def Page(self):
        r"""公共分页对象
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Items(self):
        r"""获取账号列表响应的单个对象
        :rtype: list of DescribeLocalAccountsData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeLocalAccountsData()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalAccountsRequest(AbstractModel):
    r"""DescribeLocalAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Condition: 查询条件：过滤或排序
1、UserName，string类型，姓名
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
2、UserId，string类型，账户
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
3、Phone，string类型，手机号
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _AccountGroupId: 获取账号的分组ID，不传默认获取全网根账号组
        :type AccountGroupId: int
        :param _ShowFlag: 是否仅展示当前目录下用户 1： 递归显示 2：仅显示当前目录下用户
        :type ShowFlag: int
        """
        self._Condition = None
        self._AccountGroupId = None
        self._ShowFlag = None

    @property
    def Condition(self):
        r"""查询条件：过滤或排序
1、UserName，string类型，姓名
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
2、UserId，string类型，账户
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
3、Phone，string类型，手机号
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def AccountGroupId(self):
        r"""获取账号的分组ID，不传默认获取全网根账号组
        :rtype: int
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def ShowFlag(self):
        r"""是否仅展示当前目录下用户 1： 递归显示 2：仅显示当前目录下用户
        :rtype: int
        """
        return self._ShowFlag

    @ShowFlag.setter
    def ShowFlag(self, ShowFlag):
        self._ShowFlag = ShowFlag


    def _deserialize(self, params):
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._AccountGroupId = params.get("AccountGroupId")
        self._ShowFlag = params.get("ShowFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalAccountsResponse(AbstractModel):
    r"""DescribeLocalAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 获取账号列表响应的分页对象
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeLocalAccountsPage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""获取账号列表响应的分页对象
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeLocalAccountsPage`
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
            self._Data = DescribeLocalAccountsPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRootAccountGroupRequest(AbstractModel):
    r"""DescribeRootAccountGroup请求参数结构体

    """


class DescribeRootAccountGroupResponse(AbstractModel):
    r"""DescribeRootAccountGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 账号根分组响应详情
        :type Data: :class:`tencentcloud.ioa.v20220601.models.GetAccountGroupData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""账号根分组响应详情
        :rtype: :class:`tencentcloud.ioa.v20220601.models.GetAccountGroupData`
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
            self._Data = GetAccountGroupData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSoftCensusListByDeviceData(AbstractModel):
    r"""软件统计响应对象集合

    """

    def __init__(self):
        r"""
        :param _UserName: 终端用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _MacAddr: mac地址
注意：此字段可能返回 null，表示取不到有效值。
        :type MacAddr: str
        :param _Name: 终端计算机名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _GroupNamePath: 终端组路径名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupNamePath: str
        :param _Ip: IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Mid: 唯一标识Mid
注意：此字段可能返回 null，表示取不到有效值。
        :type Mid: str
        :param _IoaUserName: 企业账户名
注意：此字段可能返回 null，表示取不到有效值。
        :type IoaUserName: str
        :param _GroupId: 终端分组Id(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: int
        :param _GroupName: 终端组名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _Id: 终端列表Id(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _SoftNum: 软件数量(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftNum: int
        :param _PiracyRisk: 盗版风险（1=风险;2=未知）
注意：此字段可能返回 null，表示取不到有效值。
        :type PiracyRisk: int
        :param _RemarkName: 终端备注名
        :type RemarkName: str
        """
        self._UserName = None
        self._MacAddr = None
        self._Name = None
        self._GroupNamePath = None
        self._Ip = None
        self._Mid = None
        self._IoaUserName = None
        self._GroupId = None
        self._GroupName = None
        self._Id = None
        self._SoftNum = None
        self._PiracyRisk = None
        self._RemarkName = None

    @property
    def UserName(self):
        r"""终端用户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def MacAddr(self):
        r"""mac地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MacAddr

    @MacAddr.setter
    def MacAddr(self, MacAddr):
        self._MacAddr = MacAddr

    @property
    def Name(self):
        r"""终端计算机名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def GroupNamePath(self):
        r"""终端组路径名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupNamePath

    @GroupNamePath.setter
    def GroupNamePath(self, GroupNamePath):
        self._GroupNamePath = GroupNamePath

    @property
    def Ip(self):
        r"""IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Mid(self):
        r"""唯一标识Mid
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid

    @property
    def IoaUserName(self):
        r"""企业账户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IoaUserName

    @IoaUserName.setter
    def IoaUserName(self, IoaUserName):
        self._IoaUserName = IoaUserName

    @property
    def GroupId(self):
        r"""终端分组Id(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""终端组名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Id(self):
        r"""终端列表Id(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SoftNum(self):
        r"""软件数量(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SoftNum

    @SoftNum.setter
    def SoftNum(self, SoftNum):
        self._SoftNum = SoftNum

    @property
    def PiracyRisk(self):
        r"""盗版风险（1=风险;2=未知）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PiracyRisk

    @PiracyRisk.setter
    def PiracyRisk(self, PiracyRisk):
        self._PiracyRisk = PiracyRisk

    @property
    def RemarkName(self):
        r"""终端备注名
        :rtype: str
        """
        return self._RemarkName

    @RemarkName.setter
    def RemarkName(self, RemarkName):
        self._RemarkName = RemarkName


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._MacAddr = params.get("MacAddr")
        self._Name = params.get("Name")
        self._GroupNamePath = params.get("GroupNamePath")
        self._Ip = params.get("Ip")
        self._Mid = params.get("Mid")
        self._IoaUserName = params.get("IoaUserName")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Id = params.get("Id")
        self._SoftNum = params.get("SoftNum")
        self._PiracyRisk = params.get("PiracyRisk")
        self._RemarkName = params.get("RemarkName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSoftCensusListByDevicePageData(AbstractModel):
    r"""业务响应数据

    """

    def __init__(self):
        r"""
        :param _Items: 软件统计响应对象集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of DescribeSoftCensusListByDeviceData
        :param _Page: 分页公共对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        self._Items = None
        self._Page = None

    @property
    def Items(self):
        r"""软件统计响应对象集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DescribeSoftCensusListByDeviceData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Page(self):
        r"""分页公共对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeSoftCensusListByDeviceData()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSoftCensusListByDeviceRequest(AbstractModel):
    r"""DescribeSoftCensusListByDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 必填，终端分组ID
        :type GroupId: int
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _OsType: 系统类型（0: win，1：linux，2: mac，4：android，5：ios  ）；默认值0
        :type OsType: int
        :param _Condition: 过滤条件、分页参数   <li>Name - String - 是否必填：否 - 操作符: eq,like,ilike  - 排序支持：否 - 备注：字段含义，终端名。</li> 	<li>UserName - String - 是否必填：否 - 操作符: eq,like,ilike  - 排序支持：否 - 备注：字段含义，终端用户名。</li> 	<li>IoaUserName - String - 是否必填：否 - 操作符: eq,like,ilike  - 排序支持：否 - 备注：字段含义，最近登录账号。</li> 	<li>Ip - String - 是否必填：否 - 操作符: eq,like,ilike  - 排序支持：否 - 备注：字段含义，IP地址。</li> 	<li>MacAddr - String - 是否必填：否 - 操作符: eq,like,ilike  - 排序支持：否 - 备注：字段含义，MAC地址。</li>
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        self._GroupId = None
        self._DomainInstanceId = None
        self._OsType = None
        self._Condition = None

    @property
    def GroupId(self):
        r"""必填，终端分组ID
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def OsType(self):
        r"""系统类型（0: win，1：linux，2: mac，4：android，5：ios  ）；默认值0
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def Condition(self):
        r"""过滤条件、分页参数   <li>Name - String - 是否必填：否 - 操作符: eq,like,ilike  - 排序支持：否 - 备注：字段含义，终端名。</li> 	<li>UserName - String - 是否必填：否 - 操作符: eq,like,ilike  - 排序支持：否 - 备注：字段含义，终端用户名。</li> 	<li>IoaUserName - String - 是否必填：否 - 操作符: eq,like,ilike  - 排序支持：否 - 备注：字段含义，最近登录账号。</li> 	<li>Ip - String - 是否必填：否 - 操作符: eq,like,ilike  - 排序支持：否 - 备注：字段含义，IP地址。</li> 	<li>MacAddr - String - 是否必填：否 - 操作符: eq,like,ilike  - 排序支持：否 - 备注：字段含义，MAC地址。</li>
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._DomainInstanceId = params.get("DomainInstanceId")
        self._OsType = params.get("OsType")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSoftCensusListByDeviceResponse(AbstractModel):
    r"""DescribeSoftCensusListByDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务响应数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeSoftCensusListByDevicePageData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务响应数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeSoftCensusListByDevicePageData`
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
            self._Data = DescribeSoftCensusListByDevicePageData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSoftwareInformationPageData(AbstractModel):
    r"""业务响应数据

    """

    def __init__(self):
        r"""
        :param _Items: 软件详情响应对象集合
        :type Items: list of SoftwareInformationData
        :param _Page: 分页公共对象
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        self._Items = None
        self._Page = None

    @property
    def Items(self):
        r"""软件详情响应对象集合
        :rtype: list of SoftwareInformationData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Page(self):
        r"""分页公共对象
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SoftwareInformationData()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSoftwareInformationRequest(AbstractModel):
    r"""DescribeSoftwareInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mid: 终端唯一标识Mid
        :type Mid: str
        :param _Condition: 过滤条件、分页参数
<li>Name - String - 过滤支持：是 - 操作符:eq,like - 排序支持：是 。</li>
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _OsType: 0:win 2:mac
        :type OsType: int
        """
        self._Mid = None
        self._Condition = None
        self._OsType = None

    @property
    def Mid(self):
        r"""终端唯一标识Mid
        :rtype: str
        """
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid

    @property
    def Condition(self):
        r"""过滤条件、分页参数
<li>Name - String - 过滤支持：是 - 操作符:eq,like - 排序支持：是 。</li>
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def OsType(self):
        r"""0:win 2:mac
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType


    def _deserialize(self, params):
        self._Mid = params.get("Mid")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._OsType = params.get("OsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSoftwareInformationResponse(AbstractModel):
    r"""DescribeSoftwareInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务响应数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeSoftwareInformationPageData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务响应数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeSoftwareInformationPageData`
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
            self._Data = DescribeSoftwareInformationPageData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVirtualDevicesPageRsp(AbstractModel):
    r"""返回的具体Data数据

    """

    def __init__(self):
        r"""
        :param _Paging: 数据分页信息
        :type Paging: :class:`tencentcloud.ioa.v20220601.models.Paging`
        :param _Items: 设备列表
        :type Items: list of DeviceDetail
        """
        self._Paging = None
        self._Items = None

    @property
    def Paging(self):
        r"""数据分页信息
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Paging

    @Paging.setter
    def Paging(self, Paging):
        self._Paging = Paging

    @property
    def Items(self):
        r"""设备列表
        :rtype: list of DeviceDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Paging") is not None:
            self._Paging = Paging()
            self._Paging._deserialize(params.get("Paging"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DeviceDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirtualDevicesRequest(AbstractModel):
    r"""DescribeVirtualDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _Condition: 过滤条件参数（字段含义请参考接口返回值）- Mid, 类型String，支持操作：【eq，like，ilike】，支持排序- Name, 类型String，支持操作：【eq，like，ilike】，支持排序- Itime, 类型String，支持操作：【eq，like，ilike】，支持排序- UserName, 类型String，支持操作：【eq，like，ilike】，支持排序- MacAddr, 类型String，支持操作：【eq，like，ilike】，支持排序- UserId, 类型String，支持操作：【eq，like，ilike】，支持排序- Ip, 类型String，支持操作：【eq，like，ilike】，支持排序- Tags，类型String，支持操作：【eq，like，ilike】，支持排序- LocalIpList，类型String，支持操作：【eq，like，ilike】，支持排序- SerialNum，类型String，支持操作：【eq，like，ilike】，支持排序- Version，类型String，支持操作：【eq，like，ilike】，支持排序- StrVersion，类型String，支持操作：【eq，like，ilike】，支持排序- RtpStatus，类型String，支持操作：【eq，like，ilike】，**不支持排序**- HostName，类型String，支持操作：【eq，like，ilike】，支持排序- IoaUserName，类型String，支持操作：【eq，like，ilike】，支持排序- GroupName，类型String，支持操作：【eq，like，ilike】，支持排序- CriticalVulListCount，**类型Int**，支持操作：【eq】，**不支持排序**- RiskCount，**类型Int**，支持操作：【eq】，**不支持排序**- VulVersion，类型String，支持操作：【eq，like，ilike】，**不支持排序**- Virusver，类型String，支持操作：【eq，like，ilike】，**不支持排序**- SysRepver，类型String，支持操作：【eq，like，ilike】，**不支持排序**- BaseBoardSn，类型String，支持操作：【eq，like，ilike】，支持排序- Os，类型String，支持操作：【eq，like，ilike】，支持排序- ConnActiveTime，类型String，支持操作：【eq，like，ilike】，**不支持排序**- FirewallStatus，**类型Int**，支持操作：【eq】，**不支持排序**- ProfileName，类型String，支持操作：【eq，like，ilike】，支持排序- DomainName，类型String，支持操作：【eq，like，ilike】，支持排序- SysRepVersion，类型String，支持操作：【eq，like，ilike】，支持排序- VirusVer，类型String，支持操作：【eq，like，ilike】，支持排序- Cpu，类型String，支持操作：【eq，like，ilike】，支持排序- Memory，类型String，支持操作：【eq，like，ilike】，支持排序- HardDiskSize，类型String，支持操作：【eq，like，ilike】，支持排序- HardwareChangeCount，**类型Int**，支持操作：【eq】，支持排序- AccountName，类型String，支持操作：【like.ilike】，支持排序- AccountGroupName，类型String，支持操作：【like.ilike】，支持排序- ScreenRecordingPermission，**类型Int**，支持操作：【eq】，支持排序- DiskAccessPermission，**类型Int**，支持操作：【eq】，支持排序分页参数- PageNum 从1开始，小于等于0时使用默认参数- PageSize 最大值5000，最好不超过100
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _DeviceVirtualGroupId: 终端自定义分组ID（0：获取租户全部自定义分组下的终端数据；其他值：获取具体ID分组下的终端数据）
        :type DeviceVirtualGroupId: int
        :param _OsType: 系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0）
        :type OsType: int
        :param _OnlineStatus: 选填，在线状态 （2表示在线，0或者1表示离线）
        :type OnlineStatus: int
        """
        self._DomainInstanceId = None
        self._Condition = None
        self._DeviceVirtualGroupId = None
        self._OsType = None
        self._OnlineStatus = None

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def Condition(self):
        r"""过滤条件参数（字段含义请参考接口返回值）- Mid, 类型String，支持操作：【eq，like，ilike】，支持排序- Name, 类型String，支持操作：【eq，like，ilike】，支持排序- Itime, 类型String，支持操作：【eq，like，ilike】，支持排序- UserName, 类型String，支持操作：【eq，like，ilike】，支持排序- MacAddr, 类型String，支持操作：【eq，like，ilike】，支持排序- UserId, 类型String，支持操作：【eq，like，ilike】，支持排序- Ip, 类型String，支持操作：【eq，like，ilike】，支持排序- Tags，类型String，支持操作：【eq，like，ilike】，支持排序- LocalIpList，类型String，支持操作：【eq，like，ilike】，支持排序- SerialNum，类型String，支持操作：【eq，like，ilike】，支持排序- Version，类型String，支持操作：【eq，like，ilike】，支持排序- StrVersion，类型String，支持操作：【eq，like，ilike】，支持排序- RtpStatus，类型String，支持操作：【eq，like，ilike】，**不支持排序**- HostName，类型String，支持操作：【eq，like，ilike】，支持排序- IoaUserName，类型String，支持操作：【eq，like，ilike】，支持排序- GroupName，类型String，支持操作：【eq，like，ilike】，支持排序- CriticalVulListCount，**类型Int**，支持操作：【eq】，**不支持排序**- RiskCount，**类型Int**，支持操作：【eq】，**不支持排序**- VulVersion，类型String，支持操作：【eq，like，ilike】，**不支持排序**- Virusver，类型String，支持操作：【eq，like，ilike】，**不支持排序**- SysRepver，类型String，支持操作：【eq，like，ilike】，**不支持排序**- BaseBoardSn，类型String，支持操作：【eq，like，ilike】，支持排序- Os，类型String，支持操作：【eq，like，ilike】，支持排序- ConnActiveTime，类型String，支持操作：【eq，like，ilike】，**不支持排序**- FirewallStatus，**类型Int**，支持操作：【eq】，**不支持排序**- ProfileName，类型String，支持操作：【eq，like，ilike】，支持排序- DomainName，类型String，支持操作：【eq，like，ilike】，支持排序- SysRepVersion，类型String，支持操作：【eq，like，ilike】，支持排序- VirusVer，类型String，支持操作：【eq，like，ilike】，支持排序- Cpu，类型String，支持操作：【eq，like，ilike】，支持排序- Memory，类型String，支持操作：【eq，like，ilike】，支持排序- HardDiskSize，类型String，支持操作：【eq，like，ilike】，支持排序- HardwareChangeCount，**类型Int**，支持操作：【eq】，支持排序- AccountName，类型String，支持操作：【like.ilike】，支持排序- AccountGroupName，类型String，支持操作：【like.ilike】，支持排序- ScreenRecordingPermission，**类型Int**，支持操作：【eq】，支持排序- DiskAccessPermission，**类型Int**，支持操作：【eq】，支持排序分页参数- PageNum 从1开始，小于等于0时使用默认参数- PageSize 最大值5000，最好不超过100
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def DeviceVirtualGroupId(self):
        r"""终端自定义分组ID（0：获取租户全部自定义分组下的终端数据；其他值：获取具体ID分组下的终端数据）
        :rtype: int
        """
        return self._DeviceVirtualGroupId

    @DeviceVirtualGroupId.setter
    def DeviceVirtualGroupId(self, DeviceVirtualGroupId):
        self._DeviceVirtualGroupId = DeviceVirtualGroupId

    @property
    def OsType(self):
        r"""系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0）
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OnlineStatus(self):
        r"""选填，在线状态 （2表示在线，0或者1表示离线）
        :rtype: int
        """
        return self._OnlineStatus

    @OnlineStatus.setter
    def OnlineStatus(self, OnlineStatus):
        self._OnlineStatus = OnlineStatus


    def _deserialize(self, params):
        self._DomainInstanceId = params.get("DomainInstanceId")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._DeviceVirtualGroupId = params.get("DeviceVirtualGroupId")
        self._OsType = params.get("OsType")
        self._OnlineStatus = params.get("OnlineStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirtualDevicesResponse(AbstractModel):
    r"""DescribeVirtualDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回的具体Data数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeVirtualDevicesPageRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""返回的具体Data数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeVirtualDevicesPageRsp`
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
            self._Data = DescribeVirtualDevicesPageRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeviceDetail(AbstractModel):
    r"""业务响应数据

    """

    def __init__(self):
        r"""
        :param _Id: 设备ID
        :type Id: int
        :param _Mid: 设备唯一标识码，在ioa中每个设备有唯一标识码
        :type Mid: str
        :param _Name: 终端名（设备名）
        :type Name: str
        :param _GroupId: 设备所在分组ID
        :type GroupId: int
        :param _OsType: OS平台，0：Windows 、1： Linux、 2：macOS 、4： Android、 5: iOS。默认是0
        :type OsType: int
        :param _Ip: 设备IP地址（出口IP）
        :type Ip: str
        :param _OnlineStatus: 在线状态，2：在线、0或者1:离线
        :type OnlineStatus: int
        :param _Version: 客户端版本号-大整数
        :type Version: str
        :param _StrVersion: 客户端版本号-点分字符串
        :type StrVersion: str
        :param _Itime: 首次在线时间
        :type Itime: str
        :param _ConnActiveTime: 最后一次在线时间
        :type ConnActiveTime: str
        :param _Locked: 设备是否加锁 ，1：锁定 0或者2：未锁定。
        :type Locked: int
        :param _LocalIpList: 设备本地IP列表, 包括IP
        :type LocalIpList: str
        :param _HostId: 宿主机id（需要宿主机也安装iOA才能显示）
        :type HostId: int
        :param _GroupName: 设备所属分组名
        :type GroupName: str
        :param _GroupNamePath: 设备所属分组路径
        :type GroupNamePath: str
        :param _CriticalVulListCount: 未修复高危漏洞数(只支持32位)
        :type CriticalVulListCount: int
        :param _Os: 操作系统名称
        :type Os: str
        :param _OsBits: 操作系统位数
        :type OsBits: int
        :param _OsVersion: 操作系统版本
        :type OsVersion: str
        :param _OsLanguage: 操作系统语言
        :type OsLanguage: str
        :param _OsInstallDate: 操作系统安装时间
        :type OsInstallDate: str
        :param _ComputerName: 设备名，和Name相同
        :type ComputerName: str
        :param _DomainName: 登录域名
        :type DomainName: str
        :param _MacAddr: MAC地址
        :type MacAddr: str
        :param _VulCount: 漏洞数
        :type VulCount: int
        :param _RiskCount: 病毒风险数
        :type RiskCount: int
        :param _VirusVer: 病毒库版本
        :type VirusVer: str
        :param _VulVersion: 漏洞库版本
        :type VulVersion: str
        :param _SysRepVersion: 系统修复引擎版本
        :type SysRepVersion: str
        :param _VulCriticalList: 高危补丁列表
        :type VulCriticalList: list of str
        :param _Tags: 标签
        :type Tags: str
        :param _UserName: 终端用户名
        :type UserName: str
        :param _FirewallStatus: 防火墙状态，不等于0表示开启
        :type FirewallStatus: int
        :param _SerialNum: SN序列号
        :type SerialNum: str
        :param _DeviceStrategyVer: 设备管控策略版本
        :type DeviceStrategyVer: str
        :param _NGNStrategyVer: NGN策略版本
        :type NGNStrategyVer: str
        :param _IOAUserName: 最近登录账户的账号(账号系统用户账号)
        :type IOAUserName: str
        :param _DeviceNewStrategyVer: 设备管控新策略
        :type DeviceNewStrategyVer: str
        :param _NGNNewStrategyVer: NGN策略新版本
        :type NGNNewStrategyVer: str
        :param _HostName: 宿主机名称（需要宿主机也安装iOA才能显示）
        :type HostName: str
        :param _BaseBoardSn: 主板序列号
        :type BaseBoardSn: str
        :param _AccountUsers: 绑定账户名称
        :type AccountUsers: str
        :param _IdentityStrategyVer: 身份策略版本
        :type IdentityStrategyVer: str
        :param _IdentityNewStrategyVer: 身份策略新版本
        :type IdentityNewStrategyVer: str
        :param _AccountGroupName: 最近登录账号部门
        :type AccountGroupName: str
        :param _AccountName: 最近登录账户的姓名(账号系统用户姓名)
        :type AccountName: str
        :param _AccountGroupId: 账号组id
        :type AccountGroupId: int
        :param _ScreenRecordingPermission: 是否开启录屏权限，仅macOS， 0： 未开启 、1： 开启
        :type ScreenRecordingPermission: int
        :param _DiskAccessPermission: 是否开启磁盘访问权限，仅macOS， 0： 未开启、 1： 开启
        :type DiskAccessPermission: int
        :param _RemarkName: 终端备注名
        :type RemarkName: str
        """
        self._Id = None
        self._Mid = None
        self._Name = None
        self._GroupId = None
        self._OsType = None
        self._Ip = None
        self._OnlineStatus = None
        self._Version = None
        self._StrVersion = None
        self._Itime = None
        self._ConnActiveTime = None
        self._Locked = None
        self._LocalIpList = None
        self._HostId = None
        self._GroupName = None
        self._GroupNamePath = None
        self._CriticalVulListCount = None
        self._Os = None
        self._OsBits = None
        self._OsVersion = None
        self._OsLanguage = None
        self._OsInstallDate = None
        self._ComputerName = None
        self._DomainName = None
        self._MacAddr = None
        self._VulCount = None
        self._RiskCount = None
        self._VirusVer = None
        self._VulVersion = None
        self._SysRepVersion = None
        self._VulCriticalList = None
        self._Tags = None
        self._UserName = None
        self._FirewallStatus = None
        self._SerialNum = None
        self._DeviceStrategyVer = None
        self._NGNStrategyVer = None
        self._IOAUserName = None
        self._DeviceNewStrategyVer = None
        self._NGNNewStrategyVer = None
        self._HostName = None
        self._BaseBoardSn = None
        self._AccountUsers = None
        self._IdentityStrategyVer = None
        self._IdentityNewStrategyVer = None
        self._AccountGroupName = None
        self._AccountName = None
        self._AccountGroupId = None
        self._ScreenRecordingPermission = None
        self._DiskAccessPermission = None
        self._RemarkName = None

    @property
    def Id(self):
        r"""设备ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Mid(self):
        r"""设备唯一标识码，在ioa中每个设备有唯一标识码
        :rtype: str
        """
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid

    @property
    def Name(self):
        r"""终端名（设备名）
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def GroupId(self):
        r"""设备所在分组ID
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def OsType(self):
        r"""OS平台，0：Windows 、1： Linux、 2：macOS 、4： Android、 5: iOS。默认是0
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def Ip(self):
        r"""设备IP地址（出口IP）
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def OnlineStatus(self):
        r"""在线状态，2：在线、0或者1:离线
        :rtype: int
        """
        return self._OnlineStatus

    @OnlineStatus.setter
    def OnlineStatus(self, OnlineStatus):
        self._OnlineStatus = OnlineStatus

    @property
    def Version(self):
        r"""客户端版本号-大整数
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def StrVersion(self):
        r"""客户端版本号-点分字符串
        :rtype: str
        """
        return self._StrVersion

    @StrVersion.setter
    def StrVersion(self, StrVersion):
        self._StrVersion = StrVersion

    @property
    def Itime(self):
        r"""首次在线时间
        :rtype: str
        """
        return self._Itime

    @Itime.setter
    def Itime(self, Itime):
        self._Itime = Itime

    @property
    def ConnActiveTime(self):
        r"""最后一次在线时间
        :rtype: str
        """
        return self._ConnActiveTime

    @ConnActiveTime.setter
    def ConnActiveTime(self, ConnActiveTime):
        self._ConnActiveTime = ConnActiveTime

    @property
    def Locked(self):
        r"""设备是否加锁 ，1：锁定 0或者2：未锁定。
        :rtype: int
        """
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def LocalIpList(self):
        r"""设备本地IP列表, 包括IP
        :rtype: str
        """
        return self._LocalIpList

    @LocalIpList.setter
    def LocalIpList(self, LocalIpList):
        self._LocalIpList = LocalIpList

    @property
    def HostId(self):
        r"""宿主机id（需要宿主机也安装iOA才能显示）
        :rtype: int
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def GroupName(self):
        r"""设备所属分组名
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupNamePath(self):
        r"""设备所属分组路径
        :rtype: str
        """
        return self._GroupNamePath

    @GroupNamePath.setter
    def GroupNamePath(self, GroupNamePath):
        self._GroupNamePath = GroupNamePath

    @property
    def CriticalVulListCount(self):
        r"""未修复高危漏洞数(只支持32位)
        :rtype: int
        """
        return self._CriticalVulListCount

    @CriticalVulListCount.setter
    def CriticalVulListCount(self, CriticalVulListCount):
        self._CriticalVulListCount = CriticalVulListCount

    @property
    def Os(self):
        r"""操作系统名称
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def OsBits(self):
        r"""操作系统位数
        :rtype: int
        """
        return self._OsBits

    @OsBits.setter
    def OsBits(self, OsBits):
        self._OsBits = OsBits

    @property
    def OsVersion(self):
        r"""操作系统版本
        :rtype: str
        """
        return self._OsVersion

    @OsVersion.setter
    def OsVersion(self, OsVersion):
        self._OsVersion = OsVersion

    @property
    def OsLanguage(self):
        r"""操作系统语言
        :rtype: str
        """
        return self._OsLanguage

    @OsLanguage.setter
    def OsLanguage(self, OsLanguage):
        self._OsLanguage = OsLanguage

    @property
    def OsInstallDate(self):
        r"""操作系统安装时间
        :rtype: str
        """
        return self._OsInstallDate

    @OsInstallDate.setter
    def OsInstallDate(self, OsInstallDate):
        self._OsInstallDate = OsInstallDate

    @property
    def ComputerName(self):
        r"""设备名，和Name相同
        :rtype: str
        """
        return self._ComputerName

    @ComputerName.setter
    def ComputerName(self, ComputerName):
        self._ComputerName = ComputerName

    @property
    def DomainName(self):
        r"""登录域名
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def MacAddr(self):
        r"""MAC地址
        :rtype: str
        """
        return self._MacAddr

    @MacAddr.setter
    def MacAddr(self, MacAddr):
        self._MacAddr = MacAddr

    @property
    def VulCount(self):
        r"""漏洞数
        :rtype: int
        """
        return self._VulCount

    @VulCount.setter
    def VulCount(self, VulCount):
        self._VulCount = VulCount

    @property
    def RiskCount(self):
        r"""病毒风险数
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def VirusVer(self):
        r"""病毒库版本
        :rtype: str
        """
        return self._VirusVer

    @VirusVer.setter
    def VirusVer(self, VirusVer):
        self._VirusVer = VirusVer

    @property
    def VulVersion(self):
        r"""漏洞库版本
        :rtype: str
        """
        return self._VulVersion

    @VulVersion.setter
    def VulVersion(self, VulVersion):
        self._VulVersion = VulVersion

    @property
    def SysRepVersion(self):
        r"""系统修复引擎版本
        :rtype: str
        """
        return self._SysRepVersion

    @SysRepVersion.setter
    def SysRepVersion(self, SysRepVersion):
        self._SysRepVersion = SysRepVersion

    @property
    def VulCriticalList(self):
        r"""高危补丁列表
        :rtype: list of str
        """
        return self._VulCriticalList

    @VulCriticalList.setter
    def VulCriticalList(self, VulCriticalList):
        self._VulCriticalList = VulCriticalList

    @property
    def Tags(self):
        r"""标签
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UserName(self):
        r"""终端用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def FirewallStatus(self):
        r"""防火墙状态，不等于0表示开启
        :rtype: int
        """
        return self._FirewallStatus

    @FirewallStatus.setter
    def FirewallStatus(self, FirewallStatus):
        self._FirewallStatus = FirewallStatus

    @property
    def SerialNum(self):
        r"""SN序列号
        :rtype: str
        """
        return self._SerialNum

    @SerialNum.setter
    def SerialNum(self, SerialNum):
        self._SerialNum = SerialNum

    @property
    def DeviceStrategyVer(self):
        r"""设备管控策略版本
        :rtype: str
        """
        return self._DeviceStrategyVer

    @DeviceStrategyVer.setter
    def DeviceStrategyVer(self, DeviceStrategyVer):
        self._DeviceStrategyVer = DeviceStrategyVer

    @property
    def NGNStrategyVer(self):
        r"""NGN策略版本
        :rtype: str
        """
        return self._NGNStrategyVer

    @NGNStrategyVer.setter
    def NGNStrategyVer(self, NGNStrategyVer):
        self._NGNStrategyVer = NGNStrategyVer

    @property
    def IOAUserName(self):
        r"""最近登录账户的账号(账号系统用户账号)
        :rtype: str
        """
        return self._IOAUserName

    @IOAUserName.setter
    def IOAUserName(self, IOAUserName):
        self._IOAUserName = IOAUserName

    @property
    def DeviceNewStrategyVer(self):
        r"""设备管控新策略
        :rtype: str
        """
        return self._DeviceNewStrategyVer

    @DeviceNewStrategyVer.setter
    def DeviceNewStrategyVer(self, DeviceNewStrategyVer):
        self._DeviceNewStrategyVer = DeviceNewStrategyVer

    @property
    def NGNNewStrategyVer(self):
        r"""NGN策略新版本
        :rtype: str
        """
        return self._NGNNewStrategyVer

    @NGNNewStrategyVer.setter
    def NGNNewStrategyVer(self, NGNNewStrategyVer):
        self._NGNNewStrategyVer = NGNNewStrategyVer

    @property
    def HostName(self):
        r"""宿主机名称（需要宿主机也安装iOA才能显示）
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def BaseBoardSn(self):
        r"""主板序列号
        :rtype: str
        """
        return self._BaseBoardSn

    @BaseBoardSn.setter
    def BaseBoardSn(self, BaseBoardSn):
        self._BaseBoardSn = BaseBoardSn

    @property
    def AccountUsers(self):
        r"""绑定账户名称
        :rtype: str
        """
        return self._AccountUsers

    @AccountUsers.setter
    def AccountUsers(self, AccountUsers):
        self._AccountUsers = AccountUsers

    @property
    def IdentityStrategyVer(self):
        r"""身份策略版本
        :rtype: str
        """
        return self._IdentityStrategyVer

    @IdentityStrategyVer.setter
    def IdentityStrategyVer(self, IdentityStrategyVer):
        self._IdentityStrategyVer = IdentityStrategyVer

    @property
    def IdentityNewStrategyVer(self):
        r"""身份策略新版本
        :rtype: str
        """
        return self._IdentityNewStrategyVer

    @IdentityNewStrategyVer.setter
    def IdentityNewStrategyVer(self, IdentityNewStrategyVer):
        self._IdentityNewStrategyVer = IdentityNewStrategyVer

    @property
    def AccountGroupName(self):
        r"""最近登录账号部门
        :rtype: str
        """
        return self._AccountGroupName

    @AccountGroupName.setter
    def AccountGroupName(self, AccountGroupName):
        self._AccountGroupName = AccountGroupName

    @property
    def AccountName(self):
        r"""最近登录账户的姓名(账号系统用户姓名)
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountGroupId(self):
        r"""账号组id
        :rtype: int
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def ScreenRecordingPermission(self):
        r"""是否开启录屏权限，仅macOS， 0： 未开启 、1： 开启
        :rtype: int
        """
        return self._ScreenRecordingPermission

    @ScreenRecordingPermission.setter
    def ScreenRecordingPermission(self, ScreenRecordingPermission):
        self._ScreenRecordingPermission = ScreenRecordingPermission

    @property
    def DiskAccessPermission(self):
        r"""是否开启磁盘访问权限，仅macOS， 0： 未开启、 1： 开启
        :rtype: int
        """
        return self._DiskAccessPermission

    @DiskAccessPermission.setter
    def DiskAccessPermission(self, DiskAccessPermission):
        self._DiskAccessPermission = DiskAccessPermission

    @property
    def RemarkName(self):
        r"""终端备注名
        :rtype: str
        """
        return self._RemarkName

    @RemarkName.setter
    def RemarkName(self, RemarkName):
        self._RemarkName = RemarkName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Mid = params.get("Mid")
        self._Name = params.get("Name")
        self._GroupId = params.get("GroupId")
        self._OsType = params.get("OsType")
        self._Ip = params.get("Ip")
        self._OnlineStatus = params.get("OnlineStatus")
        self._Version = params.get("Version")
        self._StrVersion = params.get("StrVersion")
        self._Itime = params.get("Itime")
        self._ConnActiveTime = params.get("ConnActiveTime")
        self._Locked = params.get("Locked")
        self._LocalIpList = params.get("LocalIpList")
        self._HostId = params.get("HostId")
        self._GroupName = params.get("GroupName")
        self._GroupNamePath = params.get("GroupNamePath")
        self._CriticalVulListCount = params.get("CriticalVulListCount")
        self._Os = params.get("Os")
        self._OsBits = params.get("OsBits")
        self._OsVersion = params.get("OsVersion")
        self._OsLanguage = params.get("OsLanguage")
        self._OsInstallDate = params.get("OsInstallDate")
        self._ComputerName = params.get("ComputerName")
        self._DomainName = params.get("DomainName")
        self._MacAddr = params.get("MacAddr")
        self._VulCount = params.get("VulCount")
        self._RiskCount = params.get("RiskCount")
        self._VirusVer = params.get("VirusVer")
        self._VulVersion = params.get("VulVersion")
        self._SysRepVersion = params.get("SysRepVersion")
        self._VulCriticalList = params.get("VulCriticalList")
        self._Tags = params.get("Tags")
        self._UserName = params.get("UserName")
        self._FirewallStatus = params.get("FirewallStatus")
        self._SerialNum = params.get("SerialNum")
        self._DeviceStrategyVer = params.get("DeviceStrategyVer")
        self._NGNStrategyVer = params.get("NGNStrategyVer")
        self._IOAUserName = params.get("IOAUserName")
        self._DeviceNewStrategyVer = params.get("DeviceNewStrategyVer")
        self._NGNNewStrategyVer = params.get("NGNNewStrategyVer")
        self._HostName = params.get("HostName")
        self._BaseBoardSn = params.get("BaseBoardSn")
        self._AccountUsers = params.get("AccountUsers")
        self._IdentityStrategyVer = params.get("IdentityStrategyVer")
        self._IdentityNewStrategyVer = params.get("IdentityNewStrategyVer")
        self._AccountGroupName = params.get("AccountGroupName")
        self._AccountName = params.get("AccountName")
        self._AccountGroupId = params.get("AccountGroupId")
        self._ScreenRecordingPermission = params.get("ScreenRecordingPermission")
        self._DiskAccessPermission = params.get("DiskAccessPermission")
        self._RemarkName = params.get("RemarkName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDownloadTask(AbstractModel):
    r"""业务响应数据

    """

    def __init__(self):
        r"""
        :param _DownloadURL: 同步数据下载的url
        :type DownloadURL: str
        :param _TaskId: 异步任务id，需要根据id去任务中心下载
        :type TaskId: int
        """
        self._DownloadURL = None
        self._TaskId = None

    @property
    def DownloadURL(self):
        r"""同步数据下载的url
        :rtype: str
        """
        return self._DownloadURL

    @DownloadURL.setter
    def DownloadURL(self, DownloadURL):
        self._DownloadURL = DownloadURL

    @property
    def TaskId(self):
        r"""异步任务id，需要根据id去任务中心下载
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DownloadURL = params.get("DownloadURL")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceGroupDetail(AbstractModel):
    r"""返回的数组列表

    """

    def __init__(self):
        r"""
        :param _Id: 设备组id
        :type Id: int
        :param _Name: 设备组名称
        :type Name: str
        :param _Description: 设备组描述
        :type Description: str
        :param _ParentId: 父节点id
        :type ParentId: int
        :param _IdPath: 基于id的节点路径
        :type IdPath: str
        :param _NamePath: 基于名称的节点路径
        :type NamePath: str
        :param _Locked: 分组锁定状态
        :type Locked: int
        :param _OsType: 系统类型（0: win，1：linux，2: mac，4：android，5：ios   ）
        :type OsType: int
        :param _Sort: 排序
        :type Sort: int
        :param _FromAuto: 是否自动调整
        :type FromAuto: int
        :param _Count: 子节点数量
        :type Count: int
        :param _Icon: 图标
        :type Icon: str
        :param _WithIp: 是否有ip
        :type WithIp: int
        :param _HasIp: 是否有组ip
        :type HasIp: bool
        :param _IsLeaf: 是否是叶子节点
        :type IsLeaf: bool
        :param _ReadOnly: 是否只读
        :type ReadOnly: bool
        :param _BindAccount: 对应绑定的账号id
        :type BindAccount: int
        :param _BindAccountName: 绑定账号的用户名
        :type BindAccountName: str
        """
        self._Id = None
        self._Name = None
        self._Description = None
        self._ParentId = None
        self._IdPath = None
        self._NamePath = None
        self._Locked = None
        self._OsType = None
        self._Sort = None
        self._FromAuto = None
        self._Count = None
        self._Icon = None
        self._WithIp = None
        self._HasIp = None
        self._IsLeaf = None
        self._ReadOnly = None
        self._BindAccount = None
        self._BindAccountName = None

    @property
    def Id(self):
        r"""设备组id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""设备组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""设备组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParentId(self):
        r"""父节点id
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def IdPath(self):
        r"""基于id的节点路径
        :rtype: str
        """
        return self._IdPath

    @IdPath.setter
    def IdPath(self, IdPath):
        self._IdPath = IdPath

    @property
    def NamePath(self):
        r"""基于名称的节点路径
        :rtype: str
        """
        return self._NamePath

    @NamePath.setter
    def NamePath(self, NamePath):
        self._NamePath = NamePath

    @property
    def Locked(self):
        r"""分组锁定状态
        :rtype: int
        """
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def OsType(self):
        r"""系统类型（0: win，1：linux，2: mac，4：android，5：ios   ）
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def Sort(self):
        r"""排序
        :rtype: int
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def FromAuto(self):
        r"""是否自动调整
        :rtype: int
        """
        return self._FromAuto

    @FromAuto.setter
    def FromAuto(self, FromAuto):
        self._FromAuto = FromAuto

    @property
    def Count(self):
        r"""子节点数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Icon(self):
        r"""图标
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def WithIp(self):
        r"""是否有ip
        :rtype: int
        """
        return self._WithIp

    @WithIp.setter
    def WithIp(self, WithIp):
        self._WithIp = WithIp

    @property
    def HasIp(self):
        r"""是否有组ip
        :rtype: bool
        """
        return self._HasIp

    @HasIp.setter
    def HasIp(self, HasIp):
        self._HasIp = HasIp

    @property
    def IsLeaf(self):
        r"""是否是叶子节点
        :rtype: bool
        """
        return self._IsLeaf

    @IsLeaf.setter
    def IsLeaf(self, IsLeaf):
        self._IsLeaf = IsLeaf

    @property
    def ReadOnly(self):
        r"""是否只读
        :rtype: bool
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def BindAccount(self):
        r"""对应绑定的账号id
        :rtype: int
        """
        return self._BindAccount

    @BindAccount.setter
    def BindAccount(self, BindAccount):
        self._BindAccount = BindAccount

    @property
    def BindAccountName(self):
        r"""绑定账号的用户名
        :rtype: str
        """
        return self._BindAccountName

    @BindAccountName.setter
    def BindAccountName(self, BindAccountName):
        self._BindAccountName = BindAccountName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ParentId = params.get("ParentId")
        self._IdPath = params.get("IdPath")
        self._NamePath = params.get("NamePath")
        self._Locked = params.get("Locked")
        self._OsType = params.get("OsType")
        self._Sort = params.get("Sort")
        self._FromAuto = params.get("FromAuto")
        self._Count = params.get("Count")
        self._Icon = params.get("Icon")
        self._WithIp = params.get("WithIp")
        self._HasIp = params.get("HasIp")
        self._IsLeaf = params.get("IsLeaf")
        self._ReadOnly = params.get("ReadOnly")
        self._BindAccount = params.get("BindAccount")
        self._BindAccountName = params.get("BindAccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceNetworkInfo(AbstractModel):
    r"""分页的具体数据对象

    """

    def __init__(self):
        r"""
        :param _LocalAddr: 本地地址
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalAddr: str
        :param _LocalPort: 本地端口
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalPort: int
        :param _ProcessId: 进程id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessId: int
        :param _ProcessName: 进程名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessName: str
        :param _Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _RemoteAddr: 远程地址
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoteAddr: str
        :param _RemotePort: 远程端口
注意：此字段可能返回 null，表示取不到有效值。
        :type RemotePort: int
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        """
        self._LocalAddr = None
        self._LocalPort = None
        self._ProcessId = None
        self._ProcessName = None
        self._Protocol = None
        self._RemoteAddr = None
        self._RemotePort = None
        self._State = None

    @property
    def LocalAddr(self):
        r"""本地地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LocalAddr

    @LocalAddr.setter
    def LocalAddr(self, LocalAddr):
        self._LocalAddr = LocalAddr

    @property
    def LocalPort(self):
        r"""本地端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LocalPort

    @LocalPort.setter
    def LocalPort(self, LocalPort):
        self._LocalPort = LocalPort

    @property
    def ProcessId(self):
        r"""进程id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProcessId

    @ProcessId.setter
    def ProcessId(self, ProcessId):
        self._ProcessId = ProcessId

    @property
    def ProcessName(self):
        r"""进程名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def Protocol(self):
        r"""协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RemoteAddr(self):
        r"""远程地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RemoteAddr

    @RemoteAddr.setter
    def RemoteAddr(self, RemoteAddr):
        self._RemoteAddr = RemoteAddr

    @property
    def RemotePort(self):
        r"""远程端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RemotePort

    @RemotePort.setter
    def RemotePort(self, RemotePort):
        self._RemotePort = RemotePort

    @property
    def State(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._LocalAddr = params.get("LocalAddr")
        self._LocalPort = params.get("LocalPort")
        self._ProcessId = params.get("ProcessId")
        self._ProcessName = params.get("ProcessName")
        self._Protocol = params.get("Protocol")
        self._RemoteAddr = params.get("RemoteAddr")
        self._RemotePort = params.get("RemotePort")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceProcessInfo(AbstractModel):
    r"""分页的具体数据对象

    """

    def __init__(self):
        r"""
        :param _CmdLine: 命令行
注意：此字段可能返回 null，表示取不到有效值。
        :type CmdLine: str
        :param _Memory: 内存
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Path: 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _ProcessId: 进程id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessId: int
        :param _User: 启动用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        """
        self._CmdLine = None
        self._Memory = None
        self._Name = None
        self._Path = None
        self._ProcessId = None
        self._User = None

    @property
    def CmdLine(self):
        r"""命令行
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CmdLine

    @CmdLine.setter
    def CmdLine(self, CmdLine):
        self._CmdLine = CmdLine

    @property
    def Memory(self):
        r"""内存
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Name(self):
        r"""名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Path(self):
        r"""路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def ProcessId(self):
        r"""进程id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProcessId

    @ProcessId.setter
    def ProcessId(self, ProcessId):
        self._ProcessId = ProcessId

    @property
    def User(self):
        r"""启动用户
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._CmdLine = params.get("CmdLine")
        self._Memory = params.get("Memory")
        self._Name = params.get("Name")
        self._Path = params.get("Path")
        self._ProcessId = params.get("ProcessId")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceServiceInfo(AbstractModel):
    r"""分页的具体数据对象

    """

    def __init__(self):
        r"""
        :param _CmdLine: 命令行
注意：此字段可能返回 null，表示取不到有效值。
        :type CmdLine: str
        :param _Description: 内存
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ProcessId: 进程id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessId: int
        :param _StartType: 启动类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StartType: int
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        :param _User: 启动用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        """
        self._CmdLine = None
        self._Description = None
        self._Name = None
        self._ProcessId = None
        self._StartType = None
        self._State = None
        self._User = None

    @property
    def CmdLine(self):
        r"""命令行
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CmdLine

    @CmdLine.setter
    def CmdLine(self, CmdLine):
        self._CmdLine = CmdLine

    @property
    def Description(self):
        r"""内存
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        r"""名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProcessId(self):
        r"""进程id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProcessId

    @ProcessId.setter
    def ProcessId(self, ProcessId):
        self._ProcessId = ProcessId

    @property
    def StartType(self):
        r"""启动类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StartType

    @StartType.setter
    def StartType(self, StartType):
        self._StartType = StartType

    @property
    def State(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def User(self):
        r"""启动用户
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._CmdLine = params.get("CmdLine")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._ProcessId = params.get("ProcessId")
        self._StartType = params.get("StartType")
        self._State = params.get("State")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceVirtualDeviceGroupsDetail(AbstractModel):
    r"""终端自定义分组列表数据

    """

    def __init__(self):
        r"""
        :param _Id: 终端自定义分组id
        :type Id: int
        :param _DeviceVirtualGroupName: 自定义分组名称
        :type DeviceVirtualGroupName: str
        :param _DeviceCount: 设备数
        :type DeviceCount: int
        :param _OsType: 系统类型（0: win，1：linux，2: mac，4：android，5：ios  ）
        :type OsType: int
        :param _Itime: 创建时间
        :type Itime: str
        :param _Utime: 更新时间
        :type Utime: str
        """
        self._Id = None
        self._DeviceVirtualGroupName = None
        self._DeviceCount = None
        self._OsType = None
        self._Itime = None
        self._Utime = None

    @property
    def Id(self):
        r"""终端自定义分组id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DeviceVirtualGroupName(self):
        r"""自定义分组名称
        :rtype: str
        """
        return self._DeviceVirtualGroupName

    @DeviceVirtualGroupName.setter
    def DeviceVirtualGroupName(self, DeviceVirtualGroupName):
        self._DeviceVirtualGroupName = DeviceVirtualGroupName

    @property
    def DeviceCount(self):
        r"""设备数
        :rtype: int
        """
        return self._DeviceCount

    @DeviceCount.setter
    def DeviceCount(self, DeviceCount):
        self._DeviceCount = DeviceCount

    @property
    def OsType(self):
        r"""系统类型（0: win，1：linux，2: mac，4：android，5：ios  ）
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def Itime(self):
        r"""创建时间
        :rtype: str
        """
        return self._Itime

    @Itime.setter
    def Itime(self, Itime):
        self._Itime = Itime

    @property
    def Utime(self):
        r"""更新时间
        :rtype: str
        """
        return self._Utime

    @Utime.setter
    def Utime(self, Utime):
        self._Utime = Utime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DeviceVirtualGroupName = params.get("DeviceVirtualGroupName")
        self._DeviceCount = params.get("DeviceCount")
        self._OsType = params.get("OsType")
        self._Itime = params.get("Itime")
        self._Utime = params.get("Utime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportDeviceDownloadTaskRequest(AbstractModel):
    r"""ExportDeviceDownloadTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OsType: 系统类型（0: win，1：linux，2: mac，4：android，5：ios；默认值0）
        :type OsType: int
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _GroupId: 分组id
        :type GroupId: int
        :param _OnlineStatus:  在线状态 2 在线 0，1 离线
        :type OnlineStatus: int
        :param _ExportOrder: 导出顺序，接口返回的数据字段
        :type ExportOrder: str
        :param _ExportType:  导出类型， 0：终端树；7:硬件信息列表导出；
        :type ExportType: int
        :param _Condition: 过滤条件。同DescribeDevices接口
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        self._OsType = None
        self._DomainInstanceId = None
        self._GroupId = None
        self._OnlineStatus = None
        self._ExportOrder = None
        self._ExportType = None
        self._Condition = None

    @property
    def OsType(self):
        r"""系统类型（0: win，1：linux，2: mac，4：android，5：ios；默认值0）
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def GroupId(self):
        r"""分组id
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def OnlineStatus(self):
        r""" 在线状态 2 在线 0，1 离线
        :rtype: int
        """
        return self._OnlineStatus

    @OnlineStatus.setter
    def OnlineStatus(self, OnlineStatus):
        self._OnlineStatus = OnlineStatus

    @property
    def ExportOrder(self):
        r"""导出顺序，接口返回的数据字段
        :rtype: str
        """
        return self._ExportOrder

    @ExportOrder.setter
    def ExportOrder(self, ExportOrder):
        self._ExportOrder = ExportOrder

    @property
    def ExportType(self):
        r""" 导出类型， 0：终端树；7:硬件信息列表导出；
        :rtype: int
        """
        return self._ExportType

    @ExportType.setter
    def ExportType(self, ExportType):
        self._ExportType = ExportType

    @property
    def Condition(self):
        r"""过滤条件。同DescribeDevices接口
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition


    def _deserialize(self, params):
        self._OsType = params.get("OsType")
        self._DomainInstanceId = params.get("DomainInstanceId")
        self._GroupId = params.get("GroupId")
        self._OnlineStatus = params.get("OnlineStatus")
        self._ExportOrder = params.get("ExportOrder")
        self._ExportType = params.get("ExportType")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportDeviceDownloadTaskResponse(AbstractModel):
    r"""ExportDeviceDownloadTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务响应数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DeviceDownloadTask`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务响应数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DeviceDownloadTask`
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
            self._Data = DeviceDownloadTask()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ExportSoftwareDownloadUrlRspData(AbstractModel):
    r"""业务响应数据

    """

    def __init__(self):
        r"""
        :param _DownloadURL: 下载的url
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadURL: str
        :param _TaskId: 超过一定时间走异步任务
        :type TaskId: int
        """
        self._DownloadURL = None
        self._TaskId = None

    @property
    def DownloadURL(self):
        r"""下载的url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DownloadURL

    @DownloadURL.setter
    def DownloadURL(self, DownloadURL):
        self._DownloadURL = DownloadURL

    @property
    def TaskId(self):
        r"""超过一定时间走异步任务
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DownloadURL = params.get("DownloadURL")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportSoftwareInformationListRequest(AbstractModel):
    r"""ExportSoftwareInformationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mid: 终端唯一标识Mid
        :type Mid: str
        :param _Condition: 过滤条件、分页参数
<li>Name - String - 过滤支持：是 - 操作符:eq,like - 排序支持：是 。</li>
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _OsType: 系统类型0:win 2:mac
        :type OsType: int
        """
        self._Mid = None
        self._Condition = None
        self._OsType = None

    @property
    def Mid(self):
        r"""终端唯一标识Mid
        :rtype: str
        """
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid

    @property
    def Condition(self):
        r"""过滤条件、分页参数
<li>Name - String - 过滤支持：是 - 操作符:eq,like - 排序支持：是 。</li>
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def OsType(self):
        r"""系统类型0:win 2:mac
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType


    def _deserialize(self, params):
        self._Mid = params.get("Mid")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._OsType = params.get("OsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportSoftwareInformationListResponse(AbstractModel):
    r"""ExportSoftwareInformationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务响应数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.ExportSoftwareDownloadUrlRspData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务响应数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.ExportSoftwareDownloadUrlRspData`
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
            self._Data = ExportSoftwareDownloadUrlRspData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""Filters 条件过滤

    """

    def __init__(self):
        r"""
        :param _Field: 过滤字段
        :type Field: str
        :param _Operator: 过滤方式： eq:等于,net:不等于,like,nlike,gt:大于,lt:小于,egt:大于等于,elt:小于等于。具体支持哪些过滤方式，结合具体接口字段描述来定
        :type Operator: str
        :param _Values: 过滤条件
        :type Values: list of str
        """
        self._Field = None
        self._Operator = None
        self._Values = None

    @property
    def Field(self):
        r"""过滤字段
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Operator(self):
        r"""过滤方式： eq:等于,net:不等于,like,nlike,gt:大于,lt:小于,egt:大于等于,elt:小于等于。具体支持哪些过滤方式，结合具体接口字段描述来定
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Values(self):
        r"""过滤条件
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Operator = params.get("Operator")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterGroup(AbstractModel):
    r"""FilterGroups 条件过滤组

    """

    def __init__(self):
        r"""
        :param _Filters: Filters 条件过滤
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        r"""Filters 条件过滤
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class GetAccountGroupData(AbstractModel):
    r"""账号分组详情响应数据

    """

    def __init__(self):
        r"""
        :param _NamePath: 分组名称全路径，点分格式
        :type NamePath: str
        :param _IdPathArr: 分组ID全路径，数组格式
        :type IdPathArr: list of int
        :param _ExtraInfo: 分组扩展信息
        :type ExtraInfo: str
        :param _Utime: 最后更新时间
        :type Utime: str
        :param _ParentId: 当前分组的父分组ID
        :type ParentId: int
        :param _OrgId: 源账号组ID，该字段仅适用于第三方同步的组织架构，通过OrgId-Id构成源组织架构分组ID-现组织架构分组ID映射关系
        :type OrgId: str
        :param _Name: 分组名称
        :type Name: str
        :param _Id: 分组ID
        :type Id: int
        :param _Description: 分组描述
        :type Description: str
        :param _Source: 分组导入源(只支持32位)
        :type Source: int
        :param _IdPath: 分组ID全路径，点分格式
        :type IdPath: str
        :param _Itime: 创建时间
        :type Itime: str
        :param _ParentOrgId: 父源账号组ID，该字段仅适用于第三方同步的组织架构
        :type ParentOrgId: str
        :param _Import: 导入信息,json格式
        :type Import: str
        :param _ImportEnable: 是否开启导入架构
        :type ImportEnable: bool
        :param _ImportType: 导入类型
        :type ImportType: str
        :param _MiniIamId: miniIAMId，MiniIAM源才有
        :type MiniIamId: str
        """
        self._NamePath = None
        self._IdPathArr = None
        self._ExtraInfo = None
        self._Utime = None
        self._ParentId = None
        self._OrgId = None
        self._Name = None
        self._Id = None
        self._Description = None
        self._Source = None
        self._IdPath = None
        self._Itime = None
        self._ParentOrgId = None
        self._Import = None
        self._ImportEnable = None
        self._ImportType = None
        self._MiniIamId = None

    @property
    def NamePath(self):
        r"""分组名称全路径，点分格式
        :rtype: str
        """
        return self._NamePath

    @NamePath.setter
    def NamePath(self, NamePath):
        self._NamePath = NamePath

    @property
    def IdPathArr(self):
        r"""分组ID全路径，数组格式
        :rtype: list of int
        """
        return self._IdPathArr

    @IdPathArr.setter
    def IdPathArr(self, IdPathArr):
        self._IdPathArr = IdPathArr

    @property
    def ExtraInfo(self):
        r"""分组扩展信息
        :rtype: str
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def Utime(self):
        r"""最后更新时间
        :rtype: str
        """
        return self._Utime

    @Utime.setter
    def Utime(self, Utime):
        self._Utime = Utime

    @property
    def ParentId(self):
        r"""当前分组的父分组ID
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def OrgId(self):
        r"""源账号组ID，该字段仅适用于第三方同步的组织架构，通过OrgId-Id构成源组织架构分组ID-现组织架构分组ID映射关系
        :rtype: str
        """
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def Name(self):
        r"""分组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        r"""分组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Description(self):
        r"""分组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Source(self):
        r"""分组导入源(只支持32位)
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def IdPath(self):
        r"""分组ID全路径，点分格式
        :rtype: str
        """
        return self._IdPath

    @IdPath.setter
    def IdPath(self, IdPath):
        self._IdPath = IdPath

    @property
    def Itime(self):
        r"""创建时间
        :rtype: str
        """
        return self._Itime

    @Itime.setter
    def Itime(self, Itime):
        self._Itime = Itime

    @property
    def ParentOrgId(self):
        r"""父源账号组ID，该字段仅适用于第三方同步的组织架构
        :rtype: str
        """
        return self._ParentOrgId

    @ParentOrgId.setter
    def ParentOrgId(self, ParentOrgId):
        self._ParentOrgId = ParentOrgId

    @property
    def Import(self):
        r"""导入信息,json格式
        :rtype: str
        """
        return self._Import

    @Import.setter
    def Import(self, Import):
        self._Import = Import

    @property
    def ImportEnable(self):
        r"""是否开启导入架构
        :rtype: bool
        """
        return self._ImportEnable

    @ImportEnable.setter
    def ImportEnable(self, ImportEnable):
        self._ImportEnable = ImportEnable

    @property
    def ImportType(self):
        r"""导入类型
        :rtype: str
        """
        return self._ImportType

    @ImportType.setter
    def ImportType(self, ImportType):
        self._ImportType = ImportType

    @property
    def MiniIamId(self):
        r"""miniIAMId，MiniIAM源才有
        :rtype: str
        """
        return self._MiniIamId

    @MiniIamId.setter
    def MiniIamId(self, MiniIamId):
        self._MiniIamId = MiniIamId


    def _deserialize(self, params):
        self._NamePath = params.get("NamePath")
        self._IdPathArr = params.get("IdPathArr")
        self._ExtraInfo = params.get("ExtraInfo")
        self._Utime = params.get("Utime")
        self._ParentId = params.get("ParentId")
        self._OrgId = params.get("OrgId")
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Description = params.get("Description")
        self._Source = params.get("Source")
        self._IdPath = params.get("IdPath")
        self._Itime = params.get("Itime")
        self._ParentOrgId = params.get("ParentOrgId")
        self._Import = params.get("Import")
        self._ImportEnable = params.get("ImportEnable")
        self._ImportType = params.get("ImportType")
        self._MiniIamId = params.get("MiniIamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVirtualDeviceGroupsReqItem(AbstractModel):
    r"""操作的设备列表

    """

    def __init__(self):
        r"""
        :param _DeviceMid: 设备mid
        :type DeviceMid: str
        :param _Operation: 操作标识  0:删除设备 1:添加设备
        :type Operation: int
        """
        self._DeviceMid = None
        self._Operation = None

    @property
    def DeviceMid(self):
        r"""设备mid
        :rtype: str
        """
        return self._DeviceMid

    @DeviceMid.setter
    def DeviceMid(self, DeviceMid):
        self._DeviceMid = DeviceMid

    @property
    def Operation(self):
        r"""操作标识  0:删除设备 1:添加设备
        :rtype: int
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._DeviceMid = params.get("DeviceMid")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVirtualDeviceGroupsRequest(AbstractModel):
    r"""ModifyVirtualDeviceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceList: 必填，操作的设备列表数据
        :type DeviceList: list of ModifyVirtualDeviceGroupsReqItem
        :param _DomainInstanceId: 管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :type DomainInstanceId: str
        :param _DeviceVirtualGroupId: 添加到的终端自定义分组id。和DeviceVirtualGroupIds互斥，必填其一，优先使用本参数
        :type DeviceVirtualGroupId: int
        :param _DeviceVirtualGroupIds: 要添加的终端自定义分组id列表
        :type DeviceVirtualGroupIds: list of int
        :param _OsType: 系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0）
        :type OsType: int
        """
        self._DeviceList = None
        self._DomainInstanceId = None
        self._DeviceVirtualGroupId = None
        self._DeviceVirtualGroupIds = None
        self._OsType = None

    @property
    def DeviceList(self):
        r"""必填，操作的设备列表数据
        :rtype: list of ModifyVirtualDeviceGroupsReqItem
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

    @property
    def DomainInstanceId(self):
        r"""管理域实例ID，用于CAM管理域权限分配。若企业未进行管理域的划分，可直接传入根域"1"，此时表示针对当前企业的全部设备和账号进行接口CRUD，具体CRUD的影响范围限制于相应接口的入参。
        :rtype: str
        """
        return self._DomainInstanceId

    @DomainInstanceId.setter
    def DomainInstanceId(self, DomainInstanceId):
        self._DomainInstanceId = DomainInstanceId

    @property
    def DeviceVirtualGroupId(self):
        r"""添加到的终端自定义分组id。和DeviceVirtualGroupIds互斥，必填其一，优先使用本参数
        :rtype: int
        """
        return self._DeviceVirtualGroupId

    @DeviceVirtualGroupId.setter
    def DeviceVirtualGroupId(self, DeviceVirtualGroupId):
        self._DeviceVirtualGroupId = DeviceVirtualGroupId

    @property
    def DeviceVirtualGroupIds(self):
        r"""要添加的终端自定义分组id列表
        :rtype: list of int
        """
        return self._DeviceVirtualGroupIds

    @DeviceVirtualGroupIds.setter
    def DeviceVirtualGroupIds(self, DeviceVirtualGroupIds):
        self._DeviceVirtualGroupIds = DeviceVirtualGroupIds

    @property
    def OsType(self):
        r"""系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0）
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType


    def _deserialize(self, params):
        if params.get("DeviceList") is not None:
            self._DeviceList = []
            for item in params.get("DeviceList"):
                obj = ModifyVirtualDeviceGroupsReqItem()
                obj._deserialize(item)
                self._DeviceList.append(obj)
        self._DomainInstanceId = params.get("DomainInstanceId")
        self._DeviceVirtualGroupId = params.get("DeviceVirtualGroupId")
        self._DeviceVirtualGroupIds = params.get("DeviceVirtualGroupIds")
        self._OsType = params.get("OsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVirtualDeviceGroupsResponse(AbstractModel):
    r"""ModifyVirtualDeviceGroups返回参数结构体

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


class Paging(AbstractModel):
    r"""页码

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _PageNum: 页码
        :type PageNum: int
        :param _PageCount: 总页数
        :type PageCount: int
        :param _Total: 记录总数
        :type Total: int
        """
        self._PageSize = None
        self._PageNum = None
        self._PageCount = None
        self._Total = None

    @property
    def PageSize(self):
        r"""每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        r"""页码
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageCount(self):
        r"""总页数
        :rtype: int
        """
        return self._PageCount

    @PageCount.setter
    def PageCount(self, PageCount):
        self._PageCount = PageCount

    @property
    def Total(self):
        r"""记录总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._PageCount = params.get("PageCount")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExpression(AbstractModel):
    r"""规则表达式

    """

    def __init__(self):
        r"""
        :param _Items: 规则元数据
        :type Items: list of RuleItem
        :param _Relation: 关系
        :type Relation: str
        """
        self._Items = None
        self._Relation = None

    @property
    def Items(self):
        r"""规则元数据
        :rtype: list of RuleItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Relation(self):
        r"""关系
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RuleItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleItem(AbstractModel):
    r"""规则元数据

    """

    def __init__(self):
        r"""
        :param _Key: 字段名称
        :type Key: str
        :param _Operate: 操作关系（等于、不等于、包含、不包含）
        :type Operate: str
        :param _Value: 内容
        :type Value: str
        :param _Values: 内容，v2多值版本使用
        :type Values: list of str
        """
        self._Key = None
        self._Operate = None
        self._Value = None
        self._Values = None

    @property
    def Key(self):
        r"""字段名称
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operate(self):
        r"""操作关系（等于、不等于、包含、不包含）
        :rtype: str
        """
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def Value(self):
        r"""内容
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Values(self):
        r"""内容，v2多值版本使用
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operate = params.get("Operate")
        self._Value = params.get("Value")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleRule(AbstractModel):
    r"""简单规则表达式

    """

    def __init__(self):
        r"""
        :param _Expressions: 规则表达式
        :type Expressions: list of RuleExpression
        :param _Relation: 表达式间逻辑关系
        :type Relation: str
        """
        self._Expressions = None
        self._Relation = None

    @property
    def Expressions(self):
        r"""规则表达式
        :rtype: list of RuleExpression
        """
        return self._Expressions

    @Expressions.setter
    def Expressions(self, Expressions):
        self._Expressions = Expressions

    @property
    def Relation(self):
        r"""表达式间逻辑关系
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        if params.get("Expressions") is not None:
            self._Expressions = []
            for item in params.get("Expressions"):
                obj = RuleExpression()
                obj._deserialize(item)
                self._Expressions.append(obj)
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SoftVersionAndNum(AbstractModel):
    r"""软件版本与安装数量

    """

    def __init__(self):
        r"""
        :param _Version: 软件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Num: 安装数
注意：此字段可能返回 null，表示取不到有效值。
        :type Num: int
        """
        self._Version = None
        self._Num = None

    @property
    def Version(self):
        r"""软件版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Num(self):
        r"""安装数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SoftwareInformationData(AbstractModel):
    r"""软件详情响应对象集合

    """

    def __init__(self):
        r"""
        :param _Name: 软件名称
        :type Name: str
        :param _InstallDate: 安装时间
        :type InstallDate: str
        :param _SoftwareId: 软件列表id(只支持32位)
        :type SoftwareId: int
        :param _Mid: 唯一标识Mid
        :type Mid: str
        :param _Version: 软件版本
        :type Version: str
        :param _CorpName: 公司名
        :type CorpName: str
        :param _Id: 列表Id(只支持32位)
        :type Id: int
        :param _PiracyRisk: 盗版风险（0:未支持，1:风险，2:未发现，3:未开启）
        :type PiracyRisk: int
        """
        self._Name = None
        self._InstallDate = None
        self._SoftwareId = None
        self._Mid = None
        self._Version = None
        self._CorpName = None
        self._Id = None
        self._PiracyRisk = None

    @property
    def Name(self):
        r"""软件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InstallDate(self):
        r"""安装时间
        :rtype: str
        """
        return self._InstallDate

    @InstallDate.setter
    def InstallDate(self, InstallDate):
        self._InstallDate = InstallDate

    @property
    def SoftwareId(self):
        r"""软件列表id(只支持32位)
        :rtype: int
        """
        return self._SoftwareId

    @SoftwareId.setter
    def SoftwareId(self, SoftwareId):
        self._SoftwareId = SoftwareId

    @property
    def Mid(self):
        r"""唯一标识Mid
        :rtype: str
        """
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid

    @property
    def Version(self):
        r"""软件版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def CorpName(self):
        r"""公司名
        :rtype: str
        """
        return self._CorpName

    @CorpName.setter
    def CorpName(self, CorpName):
        self._CorpName = CorpName

    @property
    def Id(self):
        r"""列表Id(只支持32位)
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PiracyRisk(self):
        r"""盗版风险（0:未支持，1:风险，2:未发现，3:未开启）
        :rtype: int
        """
        return self._PiracyRisk

    @PiracyRisk.setter
    def PiracyRisk(self, PiracyRisk):
        self._PiracyRisk = PiracyRisk


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._InstallDate = params.get("InstallDate")
        self._SoftwareId = params.get("SoftwareId")
        self._Mid = params.get("Mid")
        self._Version = params.get("Version")
        self._CorpName = params.get("CorpName")
        self._Id = params.get("Id")
        self._PiracyRisk = params.get("PiracyRisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    r"""Sort 排序字段

    """

    def __init__(self):
        r"""
        :param _Field: 排序字段
        :type Field: str
        :param _Order: 排序方式
        :type Order: str
        """
        self._Field = None
        self._Order = None

    @property
    def Field(self):
        r"""排序字段
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
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
        