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


class AutoSnapshotPolicyInfo(AbstractModel):
    """快照策略信息

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param _PolicyName: 快照策略ID
        :type PolicyName: str
        :param _CreationTime: 快照策略创建时间
        :type CreationTime: str
        :param _FileSystemNums: 关联的文件系统个数
        :type FileSystemNums: int
        :param _DayOfWeek: 快照定期备份在一星期哪一天，该参数与DayOfMonth,IntervalDays互斥
        :type DayOfWeek: str
        :param _Hour: 快照定期备份在一天的哪一小时
        :type Hour: str
        :param _IsActivated: 是否激活定期快照功能,1代表已激活，0代表未激活
        :type IsActivated: int
        :param _NextActiveTime: 下一次触发快照时间
        :type NextActiveTime: str
        :param _Status: 快照策略状态，1代表快照策略状态正常。这里只有一种状态
        :type Status: str
        :param _AppId: 账号ID
        :type AppId: int
        :param _AliveDays: 保留时间
        :type AliveDays: int
        :param _RegionName: 地域
        :type RegionName: str
        :param _FileSystems: 文件系统信息
        :type FileSystems: list of FileSystemByPolicy
        :param _DayOfMonth: 快照定期备份在一个月的某个时间；该参数与DayOfWeek,IntervalDays互斥
注意：此字段可能返回 null，表示取不到有效值。
        :type DayOfMonth: str
        :param _IntervalDays: 快照定期间隔天数，1-365 天；该参数与DayOfMonth,DayOfWeek互斥
注意：此字段可能返回 null，表示取不到有效值。
        :type IntervalDays: int
        :param _CrossRegionsAliveDays: 跨地域复制的快照保留时间，单位天
        :type CrossRegionsAliveDays: int
        """
        self._AutoSnapshotPolicyId = None
        self._PolicyName = None
        self._CreationTime = None
        self._FileSystemNums = None
        self._DayOfWeek = None
        self._Hour = None
        self._IsActivated = None
        self._NextActiveTime = None
        self._Status = None
        self._AppId = None
        self._AliveDays = None
        self._RegionName = None
        self._FileSystems = None
        self._DayOfMonth = None
        self._IntervalDays = None
        self._CrossRegionsAliveDays = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def FileSystemNums(self):
        return self._FileSystemNums

    @FileSystemNums.setter
    def FileSystemNums(self, FileSystemNums):
        self._FileSystemNums = FileSystemNums

    @property
    def DayOfWeek(self):
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def IsActivated(self):
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def NextActiveTime(self):
        return self._NextActiveTime

    @NextActiveTime.setter
    def NextActiveTime(self, NextActiveTime):
        self._NextActiveTime = NextActiveTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AliveDays(self):
        return self._AliveDays

    @AliveDays.setter
    def AliveDays(self, AliveDays):
        self._AliveDays = AliveDays

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def FileSystems(self):
        return self._FileSystems

    @FileSystems.setter
    def FileSystems(self, FileSystems):
        self._FileSystems = FileSystems

    @property
    def DayOfMonth(self):
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        return self._IntervalDays

    @IntervalDays.setter
    def IntervalDays(self, IntervalDays):
        self._IntervalDays = IntervalDays

    @property
    def CrossRegionsAliveDays(self):
        return self._CrossRegionsAliveDays

    @CrossRegionsAliveDays.setter
    def CrossRegionsAliveDays(self, CrossRegionsAliveDays):
        self._CrossRegionsAliveDays = CrossRegionsAliveDays


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._PolicyName = params.get("PolicyName")
        self._CreationTime = params.get("CreationTime")
        self._FileSystemNums = params.get("FileSystemNums")
        self._DayOfWeek = params.get("DayOfWeek")
        self._Hour = params.get("Hour")
        self._IsActivated = params.get("IsActivated")
        self._NextActiveTime = params.get("NextActiveTime")
        self._Status = params.get("Status")
        self._AppId = params.get("AppId")
        self._AliveDays = params.get("AliveDays")
        self._RegionName = params.get("RegionName")
        if params.get("FileSystems") is not None:
            self._FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystemByPolicy()
                obj._deserialize(item)
                self._FileSystems.append(obj)
        self._DayOfMonth = params.get("DayOfMonth")
        self._IntervalDays = params.get("IntervalDays")
        self._CrossRegionsAliveDays = params.get("CrossRegionsAliveDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableProtoStatus(AbstractModel):
    """版本控制-协议详情

    """

    def __init__(self):
        r"""
        :param _SaleStatus: 售卖状态。可选值有 sale_out 售罄、saling可售、no_saling不可销售
        :type SaleStatus: str
        :param _Protocol: 协议类型。可选值有 NFS、CIFS、TURBO
        :type Protocol: str
        """
        self._SaleStatus = None
        self._Protocol = None

    @property
    def SaleStatus(self):
        return self._SaleStatus

    @SaleStatus.setter
    def SaleStatus(self, SaleStatus):
        self._SaleStatus = SaleStatus

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._SaleStatus = params.get("SaleStatus")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableRegion(AbstractModel):
    """版本控制-区域数组

    """

    def __init__(self):
        r"""
        :param _Region: 区域名称，如“ap-beijing”
        :type Region: str
        :param _RegionName: 区域名称，如“bj”
        :type RegionName: str
        :param _RegionStatus: 区域可用情况，当区域内至少有一个可用区处于可售状态时，取值为AVAILABLE，否则为UNAVAILABLE
        :type RegionStatus: str
        :param _Zones: 可用区数组
        :type Zones: list of AvailableZone
        :param _RegionCnName: 区域中文名称，如“广州”
        :type RegionCnName: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionStatus = None
        self._Zones = None
        self._RegionCnName = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionStatus(self):
        return self._RegionStatus

    @RegionStatus.setter
    def RegionStatus(self, RegionStatus):
        self._RegionStatus = RegionStatus

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RegionCnName(self):
        return self._RegionCnName

    @RegionCnName.setter
    def RegionCnName(self, RegionCnName):
        self._RegionCnName = RegionCnName


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionStatus = params.get("RegionStatus")
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = AvailableZone()
                obj._deserialize(item)
                self._Zones.append(obj)
        self._RegionCnName = params.get("RegionCnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableType(AbstractModel):
    """版本控制-类型数组

    """

    def __init__(self):
        r"""
        :param _Protocols: 协议与售卖详情
        :type Protocols: list of AvailableProtoStatus
        :param _Type: 存储类型。返回值中 SD 为通用标准型存储， HP为通用性能型存储， TB为Turbo标准型， TP 为Turbo性能型。
        :type Type: str
        :param _Prepayment: 是否支持预付费。返回值中 true 为支持、false 为不支持
        :type Prepayment: bool
        """
        self._Protocols = None
        self._Type = None
        self._Prepayment = None

    @property
    def Protocols(self):
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Prepayment(self):
        return self._Prepayment

    @Prepayment.setter
    def Prepayment(self, Prepayment):
        self._Prepayment = Prepayment


    def _deserialize(self, params):
        if params.get("Protocols") is not None:
            self._Protocols = []
            for item in params.get("Protocols"):
                obj = AvailableProtoStatus()
                obj._deserialize(item)
                self._Protocols.append(obj)
        self._Type = params.get("Type")
        self._Prepayment = params.get("Prepayment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableZone(AbstractModel):
    """版本控制-可用区数组

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区名称
        :type Zone: str
        :param _ZoneId: 可用区ID
        :type ZoneId: int
        :param _ZoneCnName: 可用区中文名称
        :type ZoneCnName: str
        :param _Types: Type数组
        :type Types: list of AvailableType
        :param _ZoneName: 可用区中英文名称
        :type ZoneName: str
        """
        self._Zone = None
        self._ZoneId = None
        self._ZoneCnName = None
        self._Types = None
        self._ZoneName = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneCnName(self):
        return self._ZoneCnName

    @ZoneCnName.setter
    def ZoneCnName(self, ZoneCnName):
        self._ZoneCnName = ZoneCnName

    @property
    def Types(self):
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneCnName = params.get("ZoneCnName")
        if params.get("Types") is not None:
            self._Types = []
            for item in params.get("Types"):
                obj = AvailableType()
                obj._deserialize(item)
                self._Types.append(obj)
        self._ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoSnapshotPolicyRequest(AbstractModel):
    """BindAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param _FileSystemIds: 文件系统列表
        :type FileSystemIds: str
        """
        self._AutoSnapshotPolicyId = None
        self._FileSystemIds = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def FileSystemIds(self):
        return self._FileSystemIds

    @FileSystemIds.setter
    def FileSystemIds(self, FileSystemIds):
        self._FileSystemIds = FileSystemIds


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._FileSystemIds = params.get("FileSystemIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoSnapshotPolicyResponse(AbstractModel):
    """BindAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class BucketInfo(AbstractModel):
    """对象存储桶

    """

    def __init__(self):
        r"""
        :param _Name: 桶名称
        :type Name: str
        :param _Region: 桶所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._Name = None
        self._Region = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoSnapshotPolicyRequest(AbstractModel):
    """CreateAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Hour: 快照重复时间点,0-23
        :type Hour: str
        :param _PolicyName: 策略名称
        :type PolicyName: str
        :param _DayOfWeek: 快照重复日期，星期一到星期日。 1代表星期一、7代表星期天
        :type DayOfWeek: str
        :param _AliveDays: 快照保留时长，单位天
        :type AliveDays: int
        :param _DayOfMonth: 快照按月重复，每月1-31号，选择一天，每月将在这一天自动创建快照。
        :type DayOfMonth: str
        :param _IntervalDays: 间隔天数
        :type IntervalDays: int
        """
        self._Hour = None
        self._PolicyName = None
        self._DayOfWeek = None
        self._AliveDays = None
        self._DayOfMonth = None
        self._IntervalDays = None

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def DayOfWeek(self):
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def AliveDays(self):
        return self._AliveDays

    @AliveDays.setter
    def AliveDays(self, AliveDays):
        self._AliveDays = AliveDays

    @property
    def DayOfMonth(self):
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        return self._IntervalDays

    @IntervalDays.setter
    def IntervalDays(self, IntervalDays):
        self._IntervalDays = IntervalDays


    def _deserialize(self, params):
        self._Hour = params.get("Hour")
        self._PolicyName = params.get("PolicyName")
        self._DayOfWeek = params.get("DayOfWeek")
        self._AliveDays = params.get("AliveDays")
        self._DayOfMonth = params.get("DayOfMonth")
        self._IntervalDays = params.get("IntervalDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoSnapshotPolicyResponse(AbstractModel):
    """CreateAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class CreateCfsFileSystemRequest(AbstractModel):
    """CreateCfsFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区名称，例如ap-beijing-1，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的地域与可用区列表
        :type Zone: str
        :param _NetInterface: 网络类型，可选值为 VPC，CCN；其中 VPC 为私有网络， CCN 为云联网。通用标准型/性能型请选择VPC，Turbo标准型/性能型请选择CCN。
        :type NetInterface: str
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _Protocol: 文件系统协议类型， 值为 NFS、CIFS、TURBO ; 若留空则默认为 NFS协议，turbo系列必须选择turbo，不支持NFS、CIFS
        :type Protocol: str
        :param _StorageType: 文件系统存储类型，默认值为 SD ；其中 SD 为通用标准型存储， HP为通用性能型存储， TB为Turbo标准型， TP 为Turbo性能型。
        :type StorageType: str
        :param _VpcId: 私有网络（VPC） ID，若网络类型选择的是VPC，该字段为必填。
        :type VpcId: str
        :param _SubnetId: 子网 ID，若网络类型选择的是VPC，该字段为必填。
        :type SubnetId: str
        :param _MountIP: 指定IP地址，仅VPC网络支持；若不填写、将在该子网下随机分配 IP，Turbo系列当前不支持指定
        :type MountIP: str
        :param _FsName: 用户自定义文件系统名称
        :type FsName: str
        :param _ResourceTags: 文件系统标签
        :type ResourceTags: list of TagInfo
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。用于保证请求幂等性的字符串失效时间为2小时。
        :type ClientToken: str
        :param _CcnId: 云联网ID， 若网络类型选择的是CCN，该字段为必填
        :type CcnId: str
        :param _CidrBlock: 云联网中CFS使用的网段， 若网络类型选择的是Ccn，该字段为必填，且不能和Ccn中已经绑定的网段冲突
        :type CidrBlock: str
        :param _Capacity: 文件系统容量，turbo系列必填，单位为GiB。 turbo标准型单位GB，起售20TiB，即20480 GiB；扩容步长20TiB，即20480 GiB。turbo性能型起售10TiB，即10240 GiB；扩容步长10TiB，10240 GiB。
        :type Capacity: int
        :param _SnapshotId: 文件系统快照ID
        :type SnapshotId: str
        :param _AutoSnapshotPolicyId: 定期快照策略ID
        :type AutoSnapshotPolicyId: str
        :param _EnableAutoScaleUp: 是否开启默认扩容，仅Turbo类型文件存储支持
        :type EnableAutoScaleUp: bool
        """
        self._Zone = None
        self._NetInterface = None
        self._PGroupId = None
        self._Protocol = None
        self._StorageType = None
        self._VpcId = None
        self._SubnetId = None
        self._MountIP = None
        self._FsName = None
        self._ResourceTags = None
        self._ClientToken = None
        self._CcnId = None
        self._CidrBlock = None
        self._Capacity = None
        self._SnapshotId = None
        self._AutoSnapshotPolicyId = None
        self._EnableAutoScaleUp = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NetInterface(self):
        return self._NetInterface

    @NetInterface.setter
    def NetInterface(self, NetInterface):
        self._NetInterface = NetInterface

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def MountIP(self):
        return self._MountIP

    @MountIP.setter
    def MountIP(self, MountIP):
        self._MountIP = MountIP

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def CcnId(self):
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Capacity(self):
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def EnableAutoScaleUp(self):
        return self._EnableAutoScaleUp

    @EnableAutoScaleUp.setter
    def EnableAutoScaleUp(self, EnableAutoScaleUp):
        self._EnableAutoScaleUp = EnableAutoScaleUp


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._NetInterface = params.get("NetInterface")
        self._PGroupId = params.get("PGroupId")
        self._Protocol = params.get("Protocol")
        self._StorageType = params.get("StorageType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._MountIP = params.get("MountIP")
        self._FsName = params.get("FsName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._ClientToken = params.get("ClientToken")
        self._CcnId = params.get("CcnId")
        self._CidrBlock = params.get("CidrBlock")
        self._Capacity = params.get("Capacity")
        self._SnapshotId = params.get("SnapshotId")
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._EnableAutoScaleUp = params.get("EnableAutoScaleUp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsFileSystemResponse(AbstractModel):
    """CreateCfsFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CreationTime: 文件系统创建时间
        :type CreationTime: str
        :param _CreationToken: 用户自定义文件系统名称
        :type CreationToken: str
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _LifeCycleState: 文件系统状态，可能出现状态包括：“creating”  创建中, “create_failed” 创建失败, “available” 可用, “unserviced” 不可用, “upgrading” 升级中， “deleting” 删除中。
        :type LifeCycleState: str
        :param _SizeByte: 文件系统已使用容量大小，单位为 Byte
        :type SizeByte: int
        :param _ZoneId: 可用区 ID
        :type ZoneId: int
        :param _FsName: 用户自定义文件系统名称
        :type FsName: str
        :param _Encrypted: 文件系统是否加密
        :type Encrypted: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CreationTime = None
        self._CreationToken = None
        self._FileSystemId = None
        self._LifeCycleState = None
        self._SizeByte = None
        self._ZoneId = None
        self._FsName = None
        self._Encrypted = None
        self._RequestId = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def CreationToken(self):
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def LifeCycleState(self):
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def SizeByte(self):
        return self._SizeByte

    @SizeByte.setter
    def SizeByte(self, SizeByte):
        self._SizeByte = SizeByte

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def Encrypted(self):
        return self._Encrypted

    @Encrypted.setter
    def Encrypted(self, Encrypted):
        self._Encrypted = Encrypted

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._CreationToken = params.get("CreationToken")
        self._FileSystemId = params.get("FileSystemId")
        self._LifeCycleState = params.get("LifeCycleState")
        self._SizeByte = params.get("SizeByte")
        self._ZoneId = params.get("ZoneId")
        self._FsName = params.get("FsName")
        self._Encrypted = params.get("Encrypted")
        self._RequestId = params.get("RequestId")


class CreateCfsPGroupRequest(AbstractModel):
    """CreateCfsPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 权限组名称，1-64个字符且只能为中文，字母，数字，下划线或横线
        :type Name: str
        :param _DescInfo: 权限组描述信息，1-255个字符
        :type DescInfo: str
        """
        self._Name = None
        self._DescInfo = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsPGroupResponse(AbstractModel):
    """CreateCfsPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _Name: 权限组名字
        :type Name: str
        :param _DescInfo: 权限组描述信息
        :type DescInfo: str
        :param _BindCfsNum: 已经与该权限组绑定的文件系统个数
        :type BindCfsNum: int
        :param _CDate: 权限组创建时间
        :type CDate: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PGroupId = None
        self._Name = None
        self._DescInfo = None
        self._BindCfsNum = None
        self._CDate = None
        self._RequestId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo

    @property
    def BindCfsNum(self):
        return self._BindCfsNum

    @BindCfsNum.setter
    def BindCfsNum(self, BindCfsNum):
        self._BindCfsNum = BindCfsNum

    @property
    def CDate(self):
        return self._CDate

    @CDate.setter
    def CDate(self, CDate):
        self._CDate = CDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        self._BindCfsNum = params.get("BindCfsNum")
        self._CDate = params.get("CDate")
        self._RequestId = params.get("RequestId")


class CreateCfsRuleRequest(AbstractModel):
    """CreateCfsRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _AuthClientIp: 可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。
        :type AuthClientIp: str
        :param _Priority: 规则优先级，参数范围1-100。 其中 1 为最高，100为最低
        :type Priority: int
        :param _RWPermission: 读写权限, 值为 RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读
        :type RWPermission: str
        :param _UserPermission: 用户权限，值为 all_squash、no_all_squash、root_squash、no_root_squash。
all_squash：所有访问用户（含 root 用户）都会被映射为匿名用户或用户组。
no_all_squash：所有访问用户（含 root 用户）均保持原有的 UID/GID 信息。
root_squash：将来访的 root 用户映射为匿名用户或用户组，非 root 用户保持原有的 UID/GID 信息。
no_root_squash：与 no_all_squash 效果一致，所有访问用户（含 root 用户）均保持原有的 UID/GID 信息

        :type UserPermission: str
        """
        self._PGroupId = None
        self._AuthClientIp = None
        self._Priority = None
        self._RWPermission = None
        self._UserPermission = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def AuthClientIp(self):
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RWPermission(self):
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._Priority = params.get("Priority")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsRuleResponse(AbstractModel):
    """CreateCfsRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则 ID
        :type RuleId: str
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _AuthClientIp: 客户端 IP
        :type AuthClientIp: str
        :param _RWPermission: 读写权限
        :type RWPermission: str
        :param _UserPermission: 用户权限
        :type UserPermission: str
        :param _Priority: 优先级
        :type Priority: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._PGroupId = None
        self._AuthClientIp = None
        self._RWPermission = None
        self._UserPermission = None
        self._Priority = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def AuthClientIp(self):
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._PGroupId = params.get("PGroupId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        self._Priority = params.get("Priority")
        self._RequestId = params.get("RequestId")


class CreateCfsSnapshotRequest(AbstractModel):
    """CreateCfsSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统id
        :type FileSystemId: str
        :param _SnapshotName: 快照名称
        :type SnapshotName: str
        :param _ResourceTags: 快照标签
        :type ResourceTags: list of TagInfo
        """
        self._FileSystemId = None
        self._SnapshotName = None
        self._ResourceTags = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._SnapshotName = params.get("SnapshotName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsSnapshotResponse(AbstractModel):
    """CreateCfsSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 文件系统快照id
        :type SnapshotId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SnapshotId = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class CreateMigrationTaskRequest(AbstractModel):
    """CreateMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskName: 迁移任务名称
        :type TaskName: str
        :param _MigrationType: 迁移方式标志位，默认为0。0: 桶迁移；1: 清单迁移
        :type MigrationType: int
        :param _MigrationMode: 迁移模式，默认为0。0: 全量迁移
        :type MigrationMode: int
        :param _SrcSecretId: 数据源账号的SecretId
        :type SrcSecretId: str
        :param _SrcSecretKey: 数据源账号的SecretKey
        :type SrcSecretKey: str
        :param _FileSystemId: 文件系统实例Id
        :type FileSystemId: str
        :param _FsPath: 文件系统路径
        :type FsPath: str
        :param _CoverType: 同名文件迁移时覆盖策略，默认为0。0: 最后修改时间优先；1: 全覆盖；2: 不覆盖
        :type CoverType: int
        :param _SrcService: 数据源服务商。COS: 腾讯云COS，OSS: 阿里云OSS，OBS:华为云OBS
        :type SrcService: str
        :param _BucketName: 数据源桶名称，名称和地址至少有一个
        :type BucketName: str
        :param _BucketRegion: 数据源桶地域
        :type BucketRegion: str
        :param _BucketAddress: 数据源桶地址，名称和地址至少有一个
        :type BucketAddress: str
        :param _ListAddress: 清单地址，迁移方式为清单迁移时必填
        :type ListAddress: str
        :param _FsName: 目标文件系统名称
        :type FsName: str
        :param _BucketPath: 源桶路径，默认为/
        :type BucketPath: str
        """
        self._TaskName = None
        self._MigrationType = None
        self._MigrationMode = None
        self._SrcSecretId = None
        self._SrcSecretKey = None
        self._FileSystemId = None
        self._FsPath = None
        self._CoverType = None
        self._SrcService = None
        self._BucketName = None
        self._BucketRegion = None
        self._BucketAddress = None
        self._ListAddress = None
        self._FsName = None
        self._BucketPath = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def MigrationType(self):
        return self._MigrationType

    @MigrationType.setter
    def MigrationType(self, MigrationType):
        self._MigrationType = MigrationType

    @property
    def MigrationMode(self):
        return self._MigrationMode

    @MigrationMode.setter
    def MigrationMode(self, MigrationMode):
        self._MigrationMode = MigrationMode

    @property
    def SrcSecretId(self):
        return self._SrcSecretId

    @SrcSecretId.setter
    def SrcSecretId(self, SrcSecretId):
        self._SrcSecretId = SrcSecretId

    @property
    def SrcSecretKey(self):
        return self._SrcSecretKey

    @SrcSecretKey.setter
    def SrcSecretKey(self, SrcSecretKey):
        self._SrcSecretKey = SrcSecretKey

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsPath(self):
        return self._FsPath

    @FsPath.setter
    def FsPath(self, FsPath):
        self._FsPath = FsPath

    @property
    def CoverType(self):
        return self._CoverType

    @CoverType.setter
    def CoverType(self, CoverType):
        self._CoverType = CoverType

    @property
    def SrcService(self):
        return self._SrcService

    @SrcService.setter
    def SrcService(self, SrcService):
        self._SrcService = SrcService

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketRegion(self):
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def BucketAddress(self):
        return self._BucketAddress

    @BucketAddress.setter
    def BucketAddress(self, BucketAddress):
        self._BucketAddress = BucketAddress

    @property
    def ListAddress(self):
        return self._ListAddress

    @ListAddress.setter
    def ListAddress(self, ListAddress):
        self._ListAddress = ListAddress

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def BucketPath(self):
        return self._BucketPath

    @BucketPath.setter
    def BucketPath(self, BucketPath):
        self._BucketPath = BucketPath


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._MigrationType = params.get("MigrationType")
        self._MigrationMode = params.get("MigrationMode")
        self._SrcSecretId = params.get("SrcSecretId")
        self._SrcSecretKey = params.get("SrcSecretKey")
        self._FileSystemId = params.get("FileSystemId")
        self._FsPath = params.get("FsPath")
        self._CoverType = params.get("CoverType")
        self._SrcService = params.get("SrcService")
        self._BucketName = params.get("BucketName")
        self._BucketRegion = params.get("BucketRegion")
        self._BucketAddress = params.get("BucketAddress")
        self._ListAddress = params.get("ListAddress")
        self._FsName = params.get("FsName")
        self._BucketPath = params.get("BucketPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrationTaskResponse(AbstractModel):
    """CreateMigrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 迁移任务Id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteAutoSnapshotPolicyRequest(AbstractModel):
    """DeleteAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        """
        self._AutoSnapshotPolicyId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoSnapshotPolicyResponse(AbstractModel):
    """DeleteAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class DeleteCfsFileSystemRequest(AbstractModel):
    """DeleteCfsFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID。说明，进行删除文件系统操作前需要先调用 DeleteMountTarget 接口删除该文件系统的挂载点，否则会删除失败。
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsFileSystemResponse(AbstractModel):
    """DeleteCfsFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteCfsPGroupRequest(AbstractModel):
    """DeleteCfsPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        """
        self._PGroupId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsPGroupResponse(AbstractModel):
    """DeleteCfsPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _AppId: 用户 ID
        :type AppId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PGroupId = None
        self._AppId = None
        self._RequestId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._AppId = params.get("AppId")
        self._RequestId = params.get("RequestId")


class DeleteCfsRuleRequest(AbstractModel):
    """DeleteCfsRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _RuleId: 规则 ID
        :type RuleId: str
        """
        self._PGroupId = None
        self._RuleId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsRuleResponse(AbstractModel):
    """DeleteCfsRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则 ID
        :type RuleId: str
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._PGroupId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._PGroupId = params.get("PGroupId")
        self._RequestId = params.get("RequestId")


class DeleteCfsSnapshotRequest(AbstractModel):
    """DeleteCfsSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 文件系统快照id
        :type SnapshotId: str
        :param _SnapshotIds: 需要删除的文件文件系统快照ID 列表，快照ID，跟ID列表至少填一项
        :type SnapshotIds: list of str
        """
        self._SnapshotId = None
        self._SnapshotIds = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._SnapshotIds = params.get("SnapshotIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsSnapshotResponse(AbstractModel):
    """DeleteCfsSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 文件系统ID
        :type SnapshotId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SnapshotId = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class DeleteMigrationTaskRequest(AbstractModel):
    """DeleteMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 迁移任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMigrationTaskResponse(AbstractModel):
    """DeleteMigrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteMountTargetRequest(AbstractModel):
    """DeleteMountTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _MountTargetId: 挂载点 ID
        :type MountTargetId: str
        """
        self._FileSystemId = None
        self._MountTargetId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def MountTargetId(self):
        return self._MountTargetId

    @MountTargetId.setter
    def MountTargetId(self, MountTargetId):
        self._MountTargetId = MountTargetId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._MountTargetId = params.get("MountTargetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMountTargetResponse(AbstractModel):
    """DeleteMountTarget返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteUserQuotaRequest(AbstractModel):
    """DeleteUserQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _UserType: 指定配额类型，包括Uid、Gid、Dir
        :type UserType: str
        :param _UserId: UID/GID信息
        :type UserId: str
        :param _DirectoryPath: 设置目录配额的目录的绝对路径
        :type DirectoryPath: str
        """
        self._FileSystemId = None
        self._UserType = None
        self._UserId = None
        self._DirectoryPath = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def DirectoryPath(self):
        return self._DirectoryPath

    @DirectoryPath.setter
    def DirectoryPath(self, DirectoryPath):
        self._DirectoryPath = DirectoryPath


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._UserType = params.get("UserType")
        self._UserId = params.get("UserId")
        self._DirectoryPath = params.get("DirectoryPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserQuotaResponse(AbstractModel):
    """DeleteUserQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeAutoSnapshotPoliciesRequest(AbstractModel):
    """DescribeAutoSnapshotPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param _Offset: 分页码
        :type Offset: int
        :param _Limit: 页面长
        :type Limit: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _Order: 升序，降序
        :type Order: str
        :param _OrderField: 排序字段
        :type OrderField: str
        """
        self._AutoSnapshotPolicyId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Order = None
        self._OrderField = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoSnapshotPoliciesResponse(AbstractModel):
    """DescribeAutoSnapshotPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 快照策略总个数
        :type TotalCount: int
        :param _AutoSnapshotPolicies: 快照策略信息
        :type AutoSnapshotPolicies: list of AutoSnapshotPolicyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoSnapshotPolicies = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoSnapshotPolicies(self):
        return self._AutoSnapshotPolicies

    @AutoSnapshotPolicies.setter
    def AutoSnapshotPolicies(self, AutoSnapshotPolicies):
        self._AutoSnapshotPolicies = AutoSnapshotPolicies

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicies") is not None:
            self._AutoSnapshotPolicies = []
            for item in params.get("AutoSnapshotPolicies"):
                obj = AutoSnapshotPolicyInfo()
                obj._deserialize(item)
                self._AutoSnapshotPolicies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAvailableZoneInfoRequest(AbstractModel):
    """DescribeAvailableZoneInfo请求参数结构体

    """


class DescribeAvailableZoneInfoResponse(AbstractModel):
    """DescribeAvailableZoneInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionZones: 各可用区的资源售卖情况以及支持的存储类型、存储协议等信息
        :type RegionZones: list of AvailableRegion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionZones = None
        self._RequestId = None

    @property
    def RegionZones(self):
        return self._RegionZones

    @RegionZones.setter
    def RegionZones(self, RegionZones):
        self._RegionZones = RegionZones

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionZones") is not None:
            self._RegionZones = []
            for item in params.get("RegionZones"):
                obj = AvailableRegion()
                obj._deserialize(item)
                self._RegionZones.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBucketListRequest(AbstractModel):
    """DescribeBucketList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcService: 数据源服务商。COS: 腾讯云COS，OSS: 阿里云OSS，OBS:华为云OBS
        :type SrcService: str
        :param _SrcSecretId: 数据源账号的SecretId

        :type SrcSecretId: str
        :param _SrcSecretKey: 数据源账号的SecretKey
        :type SrcSecretKey: str
        """
        self._SrcService = None
        self._SrcSecretId = None
        self._SrcSecretKey = None

    @property
    def SrcService(self):
        return self._SrcService

    @SrcService.setter
    def SrcService(self, SrcService):
        self._SrcService = SrcService

    @property
    def SrcSecretId(self):
        return self._SrcSecretId

    @SrcSecretId.setter
    def SrcSecretId(self, SrcSecretId):
        self._SrcSecretId = SrcSecretId

    @property
    def SrcSecretKey(self):
        return self._SrcSecretKey

    @SrcSecretKey.setter
    def SrcSecretKey(self, SrcSecretKey):
        self._SrcSecretKey = SrcSecretKey


    def _deserialize(self, params):
        self._SrcService = params.get("SrcService")
        self._SrcSecretId = params.get("SrcSecretId")
        self._SrcSecretKey = params.get("SrcSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBucketListResponse(AbstractModel):
    """DescribeBucketList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 桶的数量
        :type TotalCount: int
        :param _BucketList: 桶列表
        :type BucketList: list of BucketInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BucketList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BucketList(self):
        return self._BucketList

    @BucketList.setter
    def BucketList(self, BucketList):
        self._BucketList = BucketList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BucketList") is not None:
            self._BucketList = []
            for item in params.get("BucketList"):
                obj = BucketInfo()
                obj._deserialize(item)
                self._BucketList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsFileSystemClientsRequest(AbstractModel):
    """DescribeCfsFileSystemClients请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID。
        :type FileSystemId: str
        :param _Offset: Offset 分页码
        :type Offset: int
        :param _Limit: Limit 页面大小
        :type Limit: int
        """
        self._FileSystemId = None
        self._Offset = None
        self._Limit = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

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
        self._FileSystemId = params.get("FileSystemId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsFileSystemClientsResponse(AbstractModel):
    """DescribeCfsFileSystemClients返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientList: 客户端列表
        :type ClientList: list of FileSystemClient
        :param _TotalCount: 文件系统总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClientList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ClientList(self):
        return self._ClientList

    @ClientList.setter
    def ClientList(self, ClientList):
        self._ClientList = ClientList

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
        if params.get("ClientList") is not None:
            self._ClientList = []
            for item in params.get("ClientList"):
                obj = FileSystemClient()
                obj._deserialize(item)
                self._ClientList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCfsFileSystemsRequest(AbstractModel):
    """DescribeCfsFileSystems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _VpcId: 私有网络（VPC） ID
        :type VpcId: str
        :param _SubnetId: 子网 ID
        :type SubnetId: str
        :param _Offset: Offset 分页码
        :type Offset: int
        :param _Limit: Limit 页面大小
        :type Limit: int
        :param _CreationToken: 用户自定义名称
        :type CreationToken: str
        """
        self._FileSystemId = None
        self._VpcId = None
        self._SubnetId = None
        self._Offset = None
        self._Limit = None
        self._CreationToken = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

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
    def CreationToken(self):
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CreationToken = params.get("CreationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsFileSystemsResponse(AbstractModel):
    """DescribeCfsFileSystems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystems: 文件系统信息
        :type FileSystems: list of FileSystemInfo
        :param _TotalCount: 文件系统总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileSystems = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FileSystems(self):
        return self._FileSystems

    @FileSystems.setter
    def FileSystems(self, FileSystems):
        self._FileSystems = FileSystems

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
        if params.get("FileSystems") is not None:
            self._FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystemInfo()
                obj._deserialize(item)
                self._FileSystems.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCfsPGroupsRequest(AbstractModel):
    """DescribeCfsPGroups请求参数结构体

    """


class DescribeCfsPGroupsResponse(AbstractModel):
    """DescribeCfsPGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupList: 权限组信息列表
        :type PGroupList: list of PGroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PGroupList = None
        self._RequestId = None

    @property
    def PGroupList(self):
        return self._PGroupList

    @PGroupList.setter
    def PGroupList(self, PGroupList):
        self._PGroupList = PGroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PGroupList") is not None:
            self._PGroupList = []
            for item in params.get("PGroupList"):
                obj = PGroupInfo()
                obj._deserialize(item)
                self._PGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsRulesRequest(AbstractModel):
    """DescribeCfsRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        """
        self._PGroupId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsRulesResponse(AbstractModel):
    """DescribeCfsRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleList: 权限组规则列表
        :type RuleList: list of PGroupRuleInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleList = None
        self._RequestId = None

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = PGroupRuleInfo()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsServiceStatusRequest(AbstractModel):
    """DescribeCfsServiceStatus请求参数结构体

    """


class DescribeCfsServiceStatusResponse(AbstractModel):
    """DescribeCfsServiceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CfsServiceStatus: 该用户当前 CFS 服务的状态，none 为未开通，creating 为开通中，created 为已开通
        :type CfsServiceStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CfsServiceStatus = None
        self._RequestId = None

    @property
    def CfsServiceStatus(self):
        return self._CfsServiceStatus

    @CfsServiceStatus.setter
    def CfsServiceStatus(self, CfsServiceStatus):
        self._CfsServiceStatus = CfsServiceStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CfsServiceStatus = params.get("CfsServiceStatus")
        self._RequestId = params.get("RequestId")


class DescribeCfsSnapshotOverviewRequest(AbstractModel):
    """DescribeCfsSnapshotOverview请求参数结构体

    """


class DescribeCfsSnapshotOverviewResponse(AbstractModel):
    """DescribeCfsSnapshotOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StatisticsList: 统计信息
        :type StatisticsList: list of SnapshotStatistics
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StatisticsList = None
        self._RequestId = None

    @property
    def StatisticsList(self):
        return self._StatisticsList

    @StatisticsList.setter
    def StatisticsList(self, StatisticsList):
        self._StatisticsList = StatisticsList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StatisticsList") is not None:
            self._StatisticsList = []
            for item in params.get("StatisticsList"):
                obj = SnapshotStatistics()
                obj._deserialize(item)
                self._StatisticsList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsSnapshotsRequest(AbstractModel):
    """DescribeCfsSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _SnapshotId: 快照ID
        :type SnapshotId: str
        :param _Offset: 分页起始位置，默认为0
        :type Offset: int
        :param _Limit: 页面长度，默认为20
        :type Limit: int
        :param _Filters: 过滤条件。
<br>SnapshotId - Array of String - 是否必填：否 -（过滤条件）按快照ID过滤。
<br>SnapshotName - Array of String - 是否必填：否 -（过滤条件）按照快照名称过滤。
<br>FileSystemId - Array of String - 是否必填：否 -（过滤条件）按文件系统ID过滤。
<br>FsName - Array of String - 是否必填：否 -（过滤条件）按文件系统名过滤。
<br>Status - Array of String - 是否必填：否 -（过滤条件）按照快照状态过滤
(creating：表示创建中 | available：表示可用。| rollbacking：表示回滚。| rollbacking_new：表示由快照创建新文件系统中）
<br>tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键进行过滤。
<br>tag:tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
        :type Filters: list of Filter
        :param _OrderField: 排序取值
        :type OrderField: str
        :param _Order: 排序 升序或者降序
        :type Order: str
        """
        self._FileSystemId = None
        self._SnapshotId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._OrderField = None
        self._Order = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._SnapshotId = params.get("SnapshotId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsSnapshotsResponse(AbstractModel):
    """DescribeCfsSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总个数
        :type TotalCount: int
        :param _Snapshots: 快照信息描述
        :type Snapshots: list of SnapshotInfo
        :param _TotalSize: 快照列表快照汇总
        :type TotalSize: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Snapshots = None
        self._TotalSize = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Snapshots(self):
        return self._Snapshots

    @Snapshots.setter
    def Snapshots(self, Snapshots):
        self._Snapshots = Snapshots

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Snapshots") is not None:
            self._Snapshots = []
            for item in params.get("Snapshots"):
                obj = SnapshotInfo()
                obj._deserialize(item)
                self._Snapshots.append(obj)
        self._TotalSize = params.get("TotalSize")
        self._RequestId = params.get("RequestId")


class DescribeMigrationTasksRequest(AbstractModel):
    """DescribeMigrationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        :param _Filters: <br><li> taskId

按照【迁移任务id】进行过滤。
类型：String

必选：否

<br><li> taskName

按照【迁移任务名字】进行模糊搜索过滤。
类型：String

必选：否

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

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
    def Filters(self):
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
        


class DescribeMigrationTasksResponse(AbstractModel):
    """DescribeMigrationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 迁移任务的数量
        :type TotalCount: int
        :param _MigrationTasks: 迁移任务详情
        :type MigrationTasks: list of MigrationTaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MigrationTasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MigrationTasks(self):
        return self._MigrationTasks

    @MigrationTasks.setter
    def MigrationTasks(self, MigrationTasks):
        self._MigrationTasks = MigrationTasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("MigrationTasks") is not None:
            self._MigrationTasks = []
            for item in params.get("MigrationTasks"):
                obj = MigrationTaskInfo()
                obj._deserialize(item)
                self._MigrationTasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMountTargetsRequest(AbstractModel):
    """DescribeMountTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountTargetsResponse(AbstractModel):
    """DescribeMountTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MountTargets: 挂载点详情
        :type MountTargets: list of MountInfo
        :param _NumberOfMountTargets: 挂载点数量
        :type NumberOfMountTargets: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MountTargets = None
        self._NumberOfMountTargets = None
        self._RequestId = None

    @property
    def MountTargets(self):
        return self._MountTargets

    @MountTargets.setter
    def MountTargets(self, MountTargets):
        self._MountTargets = MountTargets

    @property
    def NumberOfMountTargets(self):
        return self._NumberOfMountTargets

    @NumberOfMountTargets.setter
    def NumberOfMountTargets(self, NumberOfMountTargets):
        self._NumberOfMountTargets = NumberOfMountTargets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MountTargets") is not None:
            self._MountTargets = []
            for item in params.get("MountTargets"):
                obj = MountInfo()
                obj._deserialize(item)
                self._MountTargets.append(obj)
        self._NumberOfMountTargets = params.get("NumberOfMountTargets")
        self._RequestId = params.get("RequestId")


class DescribeSnapshotOperationLogsRequest(AbstractModel):
    """DescribeSnapshotOperationLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 文件系统快照ID
        :type SnapshotId: str
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._SnapshotId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

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
        self._SnapshotId = params.get("SnapshotId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotOperationLogsResponse(AbstractModel):
    """DescribeSnapshotOperationLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照ID
        :type SnapshotId: str
        :param _SnapshotOperates: 操作日志
        :type SnapshotOperates: list of SnapshotOperateLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SnapshotId = None
        self._SnapshotOperates = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotOperates(self):
        return self._SnapshotOperates

    @SnapshotOperates.setter
    def SnapshotOperates(self, SnapshotOperates):
        self._SnapshotOperates = SnapshotOperates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        if params.get("SnapshotOperates") is not None:
            self._SnapshotOperates = []
            for item in params.get("SnapshotOperates"):
                obj = SnapshotOperateLog()
                obj._deserialize(item)
                self._SnapshotOperates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserQuotaRequest(AbstractModel):
    """DescribeUserQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _Filters: 过滤条件。
<br><li>UserType - Array of String - 是否必填：否 -（过滤条件）按配额类型过滤。(Uid| Gid )
<br><li>UserId - Array of String - 是否必填：否 -（过滤条件）按UID/GID过滤。
        :type Filters: list of Filter
        :param _Offset: Offset 分页码
        :type Offset: int
        :param _Limit: Limit 页面大小，可填范围为大于0的整数
        :type Limit: int
        """
        self._FileSystemId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._FileSystemId = params.get("FileSystemId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserQuotaResponse(AbstractModel):
    """DescribeUserQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: UserQuota条目总数
        :type TotalCount: int
        :param _UserQuotaInfo: UserQuota条目
        :type UserQuotaInfo: list of UserQuota
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UserQuotaInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UserQuotaInfo(self):
        return self._UserQuotaInfo

    @UserQuotaInfo.setter
    def UserQuotaInfo(self, UserQuotaInfo):
        self._UserQuotaInfo = UserQuotaInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("UserQuotaInfo") is not None:
            self._UserQuotaInfo = []
            for item in params.get("UserQuotaInfo"):
                obj = UserQuota()
                obj._deserialize(item)
                self._UserQuotaInfo.append(obj)
        self._RequestId = params.get("RequestId")


class FileSystemByPolicy(AbstractModel):
    """绑定快照策略的文件系统信息

    """

    def __init__(self):
        r"""
        :param _CreationToken: 文件系统名称
        :type CreationToken: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _SizeByte: 文件系统大小，单位Byte
        :type SizeByte: int
        :param _StorageType: 存储类型，HP：通用性能型；SD：通用标准型；TP:turbo性能型；TB：turbo标准型；THP：吞吐型
        :type StorageType: str
        :param _TotalSnapshotSize: 快照总大小，单位GiB
        :type TotalSnapshotSize: int
        :param _CreationTime: 文件系统创建时间
        :type CreationTime: str
        :param _ZoneId: 文件系统所在区ID
        :type ZoneId: int
        """
        self._CreationToken = None
        self._FileSystemId = None
        self._SizeByte = None
        self._StorageType = None
        self._TotalSnapshotSize = None
        self._CreationTime = None
        self._ZoneId = None

    @property
    def CreationToken(self):
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SizeByte(self):
        return self._SizeByte

    @SizeByte.setter
    def SizeByte(self, SizeByte):
        self._SizeByte = SizeByte

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def TotalSnapshotSize(self):
        return self._TotalSnapshotSize

    @TotalSnapshotSize.setter
    def TotalSnapshotSize(self, TotalSnapshotSize):
        self._TotalSnapshotSize = TotalSnapshotSize

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._CreationToken = params.get("CreationToken")
        self._FileSystemId = params.get("FileSystemId")
        self._SizeByte = params.get("SizeByte")
        self._StorageType = params.get("StorageType")
        self._TotalSnapshotSize = params.get("TotalSnapshotSize")
        self._CreationTime = params.get("CreationTime")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSystemClient(AbstractModel):
    """文件系统客户端信息

    """

    def __init__(self):
        r"""
        :param _CfsVip: 文件系统IP地址
        :type CfsVip: str
        :param _ClientIp: 客户端IP地址
        :type ClientIp: str
        :param _VpcId: 文件系统所属VPCID
        :type VpcId: str
        :param _Zone: 可用区名称，例如ap-beijing-1，请参考 概览文档中的地域与可用区列表
        :type Zone: str
        :param _ZoneName: 可用区中文名称
        :type ZoneName: str
        :param _MountDirectory: 该文件系统被挂载到客户端上的路径信息
        :type MountDirectory: str
        """
        self._CfsVip = None
        self._ClientIp = None
        self._VpcId = None
        self._Zone = None
        self._ZoneName = None
        self._MountDirectory = None

    @property
    def CfsVip(self):
        return self._CfsVip

    @CfsVip.setter
    def CfsVip(self, CfsVip):
        self._CfsVip = CfsVip

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def MountDirectory(self):
        return self._MountDirectory

    @MountDirectory.setter
    def MountDirectory(self, MountDirectory):
        self._MountDirectory = MountDirectory


    def _deserialize(self, params):
        self._CfsVip = params.get("CfsVip")
        self._ClientIp = params.get("ClientIp")
        self._VpcId = params.get("VpcId")
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._MountDirectory = params.get("MountDirectory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSystemInfo(AbstractModel):
    """文件系统基本信息

    """

    def __init__(self):
        r"""
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _CreationToken: 用户自定义名称
        :type CreationToken: str
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _LifeCycleState: 文件系统状态。取值范围：
- creating:创建中
- mounting:挂载中
- create_failed:创建失败
- available:可使用
- unserviced:停服中
- upgrading:升级中
        :type LifeCycleState: str
        :param _SizeByte: 文件系统已使用容量。单位：Byte
        :type SizeByte: int
        :param _SizeLimit: 文件系统空间限制。单位:GiB
        :type SizeLimit: int
        :param _ZoneId: 区域 ID
        :type ZoneId: int
        :param _Zone: 区域名称
        :type Zone: str
        :param _Protocol: 文件系统协议类型, 支持 NFS,CIFS,TURBO
        :type Protocol: str
        :param _StorageType: 存储类型，HP：通用性能型；SD：通用标准型；TP:turbo性能型；TB：turbo标准型；THP：吞吐型
        :type StorageType: str
        :param _StorageResourcePkg: 文件系统绑定的预付费存储包
        :type StorageResourcePkg: str
        :param _BandwidthResourcePkg: 文件系统绑定的预付费带宽包（暂未支持）
        :type BandwidthResourcePkg: str
        :param _PGroup: 文件系统绑定权限组信息
        :type PGroup: :class:`tencentcloud.cfs.v20190719.models.PGroup`
        :param _FsName: 用户自定义名称
        :type FsName: str
        :param _Encrypted: 文件系统是否加密,true：代表加密，false：非加密
        :type Encrypted: bool
        :param _KmsKeyId: 加密所使用的密钥，可以为密钥的 ID 或者 ARN
        :type KmsKeyId: str
        :param _AppId: 应用ID
        :type AppId: int
        :param _BandwidthLimit: 文件系统吞吐上限，吞吐上限是根据文件系统当前已使用存储量、绑定的存储资源包以及吞吐资源包一同确定. 单位MiB/s
        :type BandwidthLimit: float
        :param _Capacity: 文件系统容量规格上限
单位:GiB
        :type Capacity: int
        :param _Tags: 文件系统标签列表
        :type Tags: list of TagInfo
        :param _TieringState: 文件系统生命周期管理状态
NotAvailable：不可用
Available:可用
        :type TieringState: str
        :param _TieringDetail: 分层存储详情
注意：此字段可能返回 null，表示取不到有效值。
        :type TieringDetail: :class:`tencentcloud.cfs.v20190719.models.TieringDetailInfo`
        """
        self._CreationTime = None
        self._CreationToken = None
        self._FileSystemId = None
        self._LifeCycleState = None
        self._SizeByte = None
        self._SizeLimit = None
        self._ZoneId = None
        self._Zone = None
        self._Protocol = None
        self._StorageType = None
        self._StorageResourcePkg = None
        self._BandwidthResourcePkg = None
        self._PGroup = None
        self._FsName = None
        self._Encrypted = None
        self._KmsKeyId = None
        self._AppId = None
        self._BandwidthLimit = None
        self._Capacity = None
        self._Tags = None
        self._TieringState = None
        self._TieringDetail = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def CreationToken(self):
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def LifeCycleState(self):
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def SizeByte(self):
        return self._SizeByte

    @SizeByte.setter
    def SizeByte(self, SizeByte):
        self._SizeByte = SizeByte

    @property
    def SizeLimit(self):
        return self._SizeLimit

    @SizeLimit.setter
    def SizeLimit(self, SizeLimit):
        self._SizeLimit = SizeLimit

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def StorageResourcePkg(self):
        return self._StorageResourcePkg

    @StorageResourcePkg.setter
    def StorageResourcePkg(self, StorageResourcePkg):
        self._StorageResourcePkg = StorageResourcePkg

    @property
    def BandwidthResourcePkg(self):
        return self._BandwidthResourcePkg

    @BandwidthResourcePkg.setter
    def BandwidthResourcePkg(self, BandwidthResourcePkg):
        self._BandwidthResourcePkg = BandwidthResourcePkg

    @property
    def PGroup(self):
        return self._PGroup

    @PGroup.setter
    def PGroup(self, PGroup):
        self._PGroup = PGroup

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def Encrypted(self):
        return self._Encrypted

    @Encrypted.setter
    def Encrypted(self, Encrypted):
        self._Encrypted = Encrypted

    @property
    def KmsKeyId(self):
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def BandwidthLimit(self):
        return self._BandwidthLimit

    @BandwidthLimit.setter
    def BandwidthLimit(self, BandwidthLimit):
        self._BandwidthLimit = BandwidthLimit

    @property
    def Capacity(self):
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TieringState(self):
        return self._TieringState

    @TieringState.setter
    def TieringState(self, TieringState):
        self._TieringState = TieringState

    @property
    def TieringDetail(self):
        return self._TieringDetail

    @TieringDetail.setter
    def TieringDetail(self, TieringDetail):
        self._TieringDetail = TieringDetail


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._CreationToken = params.get("CreationToken")
        self._FileSystemId = params.get("FileSystemId")
        self._LifeCycleState = params.get("LifeCycleState")
        self._SizeByte = params.get("SizeByte")
        self._SizeLimit = params.get("SizeLimit")
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._Protocol = params.get("Protocol")
        self._StorageType = params.get("StorageType")
        self._StorageResourcePkg = params.get("StorageResourcePkg")
        self._BandwidthResourcePkg = params.get("BandwidthResourcePkg")
        if params.get("PGroup") is not None:
            self._PGroup = PGroup()
            self._PGroup._deserialize(params.get("PGroup"))
        self._FsName = params.get("FsName")
        self._Encrypted = params.get("Encrypted")
        self._KmsKeyId = params.get("KmsKeyId")
        self._AppId = params.get("AppId")
        self._BandwidthLimit = params.get("BandwidthLimit")
        self._Capacity = params.get("Capacity")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TieringState = params.get("TieringState")
        if params.get("TieringDetail") is not None:
            self._TieringDetail = TieringDetailInfo()
            self._TieringDetail._deserialize(params.get("TieringDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """条件过滤

    """

    def __init__(self):
        r"""
        :param _Values: 值
        :type Values: list of str
        :param _Name: 名称
        :type Name: str
        """
        self._Values = None
        self._Name = None

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Values = params.get("Values")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrationTaskInfo(AbstractModel):
    """CFS数据迁移任务信息

    """

    def __init__(self):
        r"""
        :param _TaskName: 迁移任务名称
        :type TaskName: str
        :param _TaskId: 迁移任务id
        :type TaskId: str
        :param _MigrationType: 迁移方式标志位，默认为0。0: 桶迁移；1: 清单迁移
        :type MigrationType: int
        :param _MigrationMode: 迁移模式，默认为0。0: 全量迁移
        :type MigrationMode: int
        :param _BucketName: 数据源桶名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketName: str
        :param _BucketRegion: 数据源桶地域
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketRegion: str
        :param _BucketAddress: 数据源桶地址
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketAddress: str
        :param _ListAddress: 清单地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ListAddress: str
        :param _FsName: 文件系统实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FsName: str
        :param _FileSystemId: 文件系统实例Id
        :type FileSystemId: str
        :param _FsPath: 文件系统路径
        :type FsPath: str
        :param _CoverType: 同名文件迁移时覆盖策略，默认为0。0: 最后修改时间优先；1: 全覆盖；2: 不覆盖
        :type CoverType: int
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _EndTime: 完成/终止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _Status: 迁移状态。0: 已完成；1: 进行中；2: 已终止
        :type Status: int
        :param _FileTotalCount: 文件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FileTotalCount: int
        :param _FileMigratedCount: 已迁移文件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FileMigratedCount: int
        :param _FileFailedCount: 迁移失败文件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FileFailedCount: int
        :param _FileTotalSize: 文件容量，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileTotalSize: int
        :param _FileMigratedSize: 已迁移文件容量，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileMigratedSize: int
        :param _FileFailedSize: 迁移失败文件容量，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileFailedSize: int
        :param _FileTotalList: 全部清单
注意：此字段可能返回 null，表示取不到有效值。
        :type FileTotalList: str
        :param _FileCompletedList: 已完成文件清单
注意：此字段可能返回 null，表示取不到有效值。
        :type FileCompletedList: str
        :param _FileFailedList: 失败文件清单
注意：此字段可能返回 null，表示取不到有效值。
        :type FileFailedList: str
        :param _BucketPath: 源桶路径
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketPath: str
        """
        self._TaskName = None
        self._TaskId = None
        self._MigrationType = None
        self._MigrationMode = None
        self._BucketName = None
        self._BucketRegion = None
        self._BucketAddress = None
        self._ListAddress = None
        self._FsName = None
        self._FileSystemId = None
        self._FsPath = None
        self._CoverType = None
        self._CreateTime = None
        self._EndTime = None
        self._Status = None
        self._FileTotalCount = None
        self._FileMigratedCount = None
        self._FileFailedCount = None
        self._FileTotalSize = None
        self._FileMigratedSize = None
        self._FileFailedSize = None
        self._FileTotalList = None
        self._FileCompletedList = None
        self._FileFailedList = None
        self._BucketPath = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MigrationType(self):
        return self._MigrationType

    @MigrationType.setter
    def MigrationType(self, MigrationType):
        self._MigrationType = MigrationType

    @property
    def MigrationMode(self):
        return self._MigrationMode

    @MigrationMode.setter
    def MigrationMode(self, MigrationMode):
        self._MigrationMode = MigrationMode

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketRegion(self):
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def BucketAddress(self):
        return self._BucketAddress

    @BucketAddress.setter
    def BucketAddress(self, BucketAddress):
        self._BucketAddress = BucketAddress

    @property
    def ListAddress(self):
        return self._ListAddress

    @ListAddress.setter
    def ListAddress(self, ListAddress):
        self._ListAddress = ListAddress

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsPath(self):
        return self._FsPath

    @FsPath.setter
    def FsPath(self, FsPath):
        self._FsPath = FsPath

    @property
    def CoverType(self):
        return self._CoverType

    @CoverType.setter
    def CoverType(self, CoverType):
        self._CoverType = CoverType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def FileTotalCount(self):
        return self._FileTotalCount

    @FileTotalCount.setter
    def FileTotalCount(self, FileTotalCount):
        self._FileTotalCount = FileTotalCount

    @property
    def FileMigratedCount(self):
        return self._FileMigratedCount

    @FileMigratedCount.setter
    def FileMigratedCount(self, FileMigratedCount):
        self._FileMigratedCount = FileMigratedCount

    @property
    def FileFailedCount(self):
        return self._FileFailedCount

    @FileFailedCount.setter
    def FileFailedCount(self, FileFailedCount):
        self._FileFailedCount = FileFailedCount

    @property
    def FileTotalSize(self):
        return self._FileTotalSize

    @FileTotalSize.setter
    def FileTotalSize(self, FileTotalSize):
        self._FileTotalSize = FileTotalSize

    @property
    def FileMigratedSize(self):
        return self._FileMigratedSize

    @FileMigratedSize.setter
    def FileMigratedSize(self, FileMigratedSize):
        self._FileMigratedSize = FileMigratedSize

    @property
    def FileFailedSize(self):
        return self._FileFailedSize

    @FileFailedSize.setter
    def FileFailedSize(self, FileFailedSize):
        self._FileFailedSize = FileFailedSize

    @property
    def FileTotalList(self):
        return self._FileTotalList

    @FileTotalList.setter
    def FileTotalList(self, FileTotalList):
        self._FileTotalList = FileTotalList

    @property
    def FileCompletedList(self):
        return self._FileCompletedList

    @FileCompletedList.setter
    def FileCompletedList(self, FileCompletedList):
        self._FileCompletedList = FileCompletedList

    @property
    def FileFailedList(self):
        return self._FileFailedList

    @FileFailedList.setter
    def FileFailedList(self, FileFailedList):
        self._FileFailedList = FileFailedList

    @property
    def BucketPath(self):
        return self._BucketPath

    @BucketPath.setter
    def BucketPath(self, BucketPath):
        self._BucketPath = BucketPath


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._TaskId = params.get("TaskId")
        self._MigrationType = params.get("MigrationType")
        self._MigrationMode = params.get("MigrationMode")
        self._BucketName = params.get("BucketName")
        self._BucketRegion = params.get("BucketRegion")
        self._BucketAddress = params.get("BucketAddress")
        self._ListAddress = params.get("ListAddress")
        self._FsName = params.get("FsName")
        self._FileSystemId = params.get("FileSystemId")
        self._FsPath = params.get("FsPath")
        self._CoverType = params.get("CoverType")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._FileTotalCount = params.get("FileTotalCount")
        self._FileMigratedCount = params.get("FileMigratedCount")
        self._FileFailedCount = params.get("FileFailedCount")
        self._FileTotalSize = params.get("FileTotalSize")
        self._FileMigratedSize = params.get("FileMigratedSize")
        self._FileFailedSize = params.get("FileFailedSize")
        self._FileTotalList = params.get("FileTotalList")
        self._FileCompletedList = params.get("FileCompletedList")
        self._FileFailedList = params.get("FileFailedList")
        self._BucketPath = params.get("BucketPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFileSystemAutoScaleUpRuleRequest(AbstractModel):
    """ModifyFileSystemAutoScaleUpRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统id
        :type FileSystemId: str
        :param _ScaleUpThreshold: 扩容阈值，范围[10-90]
        :type ScaleUpThreshold: int
        :param _TargetThreshold: 扩容后目标阈值,范围[10-90],该值要小于ScaleUpThreshold
        :type TargetThreshold: int
        :param _Status: 规则状态0:关闭，1 开启

        :type Status: int
        """
        self._FileSystemId = None
        self._ScaleUpThreshold = None
        self._TargetThreshold = None
        self._Status = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def ScaleUpThreshold(self):
        return self._ScaleUpThreshold

    @ScaleUpThreshold.setter
    def ScaleUpThreshold(self, ScaleUpThreshold):
        self._ScaleUpThreshold = ScaleUpThreshold

    @property
    def TargetThreshold(self):
        return self._TargetThreshold

    @TargetThreshold.setter
    def TargetThreshold(self, TargetThreshold):
        self._TargetThreshold = TargetThreshold

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._ScaleUpThreshold = params.get("ScaleUpThreshold")
        self._TargetThreshold = params.get("TargetThreshold")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFileSystemAutoScaleUpRuleResponse(AbstractModel):
    """ModifyFileSystemAutoScaleUpRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统id
        :type FileSystemId: str
        :param _Status: 规则状态0:关闭，1 开启
        :type Status: int
        :param _ScaleUpThreshold: 扩容阈值,范围[10-90]
        :type ScaleUpThreshold: int
        :param _TargetThreshold: 扩容后达到阈值,范围[10-90]
        :type TargetThreshold: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileSystemId = None
        self._Status = None
        self._ScaleUpThreshold = None
        self._TargetThreshold = None
        self._RequestId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ScaleUpThreshold(self):
        return self._ScaleUpThreshold

    @ScaleUpThreshold.setter
    def ScaleUpThreshold(self, ScaleUpThreshold):
        self._ScaleUpThreshold = ScaleUpThreshold

    @property
    def TargetThreshold(self):
        return self._TargetThreshold

    @TargetThreshold.setter
    def TargetThreshold(self, TargetThreshold):
        self._TargetThreshold = TargetThreshold

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._Status = params.get("Status")
        self._ScaleUpThreshold = params.get("ScaleUpThreshold")
        self._TargetThreshold = params.get("TargetThreshold")
        self._RequestId = params.get("RequestId")


class MountInfo(AbstractModel):
    """挂载点信息

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _MountTargetId: 挂载点 ID
        :type MountTargetId: str
        :param _IpAddress: 挂载点 IP
        :type IpAddress: str
        :param _FSID: 挂载根目录
        :type FSID: str
        :param _LifeCycleState: 挂载点状态
        :type LifeCycleState: str
        :param _NetworkInterface: 网络类型
        :type NetworkInterface: str
        :param _VpcId: 私有网络 ID
        :type VpcId: str
        :param _VpcName: 私有网络名称
        :type VpcName: str
        :param _SubnetId: 子网 Id
        :type SubnetId: str
        :param _SubnetName: 子网名称
        :type SubnetName: str
        :param _CcnID: CFS Turbo使用的云联网ID
        :type CcnID: str
        :param _CidrBlock: 云联网中CFS Turbo使用的网段
        :type CidrBlock: str
        """
        self._FileSystemId = None
        self._MountTargetId = None
        self._IpAddress = None
        self._FSID = None
        self._LifeCycleState = None
        self._NetworkInterface = None
        self._VpcId = None
        self._VpcName = None
        self._SubnetId = None
        self._SubnetName = None
        self._CcnID = None
        self._CidrBlock = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def MountTargetId(self):
        return self._MountTargetId

    @MountTargetId.setter
    def MountTargetId(self, MountTargetId):
        self._MountTargetId = MountTargetId

    @property
    def IpAddress(self):
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def FSID(self):
        return self._FSID

    @FSID.setter
    def FSID(self, FSID):
        self._FSID = FSID

    @property
    def LifeCycleState(self):
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def NetworkInterface(self):
        return self._NetworkInterface

    @NetworkInterface.setter
    def NetworkInterface(self, NetworkInterface):
        self._NetworkInterface = NetworkInterface

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
    def CcnID(self):
        return self._CcnID

    @CcnID.setter
    def CcnID(self, CcnID):
        self._CcnID = CcnID

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._MountTargetId = params.get("MountTargetId")
        self._IpAddress = params.get("IpAddress")
        self._FSID = params.get("FSID")
        self._LifeCycleState = params.get("LifeCycleState")
        self._NetworkInterface = params.get("NetworkInterface")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._CcnID = params.get("CcnID")
        self._CidrBlock = params.get("CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroup(AbstractModel):
    """文件系统绑定权限组信息

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组ID
        :type PGroupId: str
        :param _Name: 权限组名称
        :type Name: str
        """
        self._PGroupId = None
        self._Name = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroupInfo(AbstractModel):
    """权限组数组

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组ID
        :type PGroupId: str
        :param _Name: 权限组名称
        :type Name: str
        :param _DescInfo: 描述信息
        :type DescInfo: str
        :param _CDate: 创建时间
        :type CDate: str
        :param _BindCfsNum: 关联文件系统个数
        :type BindCfsNum: int
        """
        self._PGroupId = None
        self._Name = None
        self._DescInfo = None
        self._CDate = None
        self._BindCfsNum = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo

    @property
    def CDate(self):
        return self._CDate

    @CDate.setter
    def CDate(self, CDate):
        self._CDate = CDate

    @property
    def BindCfsNum(self):
        return self._BindCfsNum

    @BindCfsNum.setter
    def BindCfsNum(self, BindCfsNum):
        self._BindCfsNum = BindCfsNum


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        self._CDate = params.get("CDate")
        self._BindCfsNum = params.get("BindCfsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroupRuleInfo(AbstractModel):
    """权限组规则列表

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _AuthClientIp: 允许访问的客户端IP
        :type AuthClientIp: str
        :param _RWPermission: 读写权限, ro为只读，rw为读写
        :type RWPermission: str
        :param _UserPermission: all_squash：所有访问用户（含 root 用户）都会被映射为匿名用户或用户组。
no_all_squash：所有访问用户（含 root 用户）均保持原有的 UID/GID 信息。
root_squash：将来访的 root 用户映射为匿名用户或用户组，非 root 用户保持原有的 UID/GID 信息。
no_root_squash：与 no_all_squash 效果一致，所有访问用户（含 root 用户）均保持原有的 UID/GID 信息

        :type UserPermission: str
        :param _Priority: 规则优先级，1-100。 其中 1 为最高，100为最低
        :type Priority: int
        """
        self._RuleId = None
        self._AuthClientIp = None
        self._RWPermission = None
        self._UserPermission = None
        self._Priority = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AuthClientIp(self):
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpFileSystemRequest(AbstractModel):
    """ScaleUpFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统Id
        :type FileSystemId: str
        :param _TargetCapacity: 扩容的目标容量（单位GiB）
        :type TargetCapacity: int
        """
        self._FileSystemId = None
        self._TargetCapacity = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def TargetCapacity(self):
        return self._TargetCapacity

    @TargetCapacity.setter
    def TargetCapacity(self, TargetCapacity):
        self._TargetCapacity = TargetCapacity


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._TargetCapacity = params.get("TargetCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpFileSystemResponse(AbstractModel):
    """ScaleUpFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统Id
        :type FileSystemId: str
        :param _TargetCapacity: 扩容的目标容量（单位GiB）
        :type TargetCapacity: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileSystemId = None
        self._TargetCapacity = None
        self._RequestId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def TargetCapacity(self):
        return self._TargetCapacity

    @TargetCapacity.setter
    def TargetCapacity(self, TargetCapacity):
        self._TargetCapacity = TargetCapacity

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._TargetCapacity = params.get("TargetCapacity")
        self._RequestId = params.get("RequestId")


class SetUserQuotaRequest(AbstractModel):
    """SetUserQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _UserType: 指定配额类型，包括Uid、Gid，Dir，分别代表用户配额，用户组配额，目录配额
        :type UserType: str
        :param _UserId: UID/GID信息
        :type UserId: str
        :param _CapacityHardLimit: 容量硬限制，单位GiB。设置范围10-10000000。
        :type CapacityHardLimit: int
        :param _FileHardLimit: 文件硬限制，单位个。设置范围1000-100000000
        :type FileHardLimit: int
        :param _DirectoryPath: 需设置目录配额的目录绝对路径，不同目录不可存在包含关系
        :type DirectoryPath: str
        """
        self._FileSystemId = None
        self._UserType = None
        self._UserId = None
        self._CapacityHardLimit = None
        self._FileHardLimit = None
        self._DirectoryPath = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def CapacityHardLimit(self):
        return self._CapacityHardLimit

    @CapacityHardLimit.setter
    def CapacityHardLimit(self, CapacityHardLimit):
        self._CapacityHardLimit = CapacityHardLimit

    @property
    def FileHardLimit(self):
        return self._FileHardLimit

    @FileHardLimit.setter
    def FileHardLimit(self, FileHardLimit):
        self._FileHardLimit = FileHardLimit

    @property
    def DirectoryPath(self):
        return self._DirectoryPath

    @DirectoryPath.setter
    def DirectoryPath(self, DirectoryPath):
        self._DirectoryPath = DirectoryPath


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._UserType = params.get("UserType")
        self._UserId = params.get("UserId")
        self._CapacityHardLimit = params.get("CapacityHardLimit")
        self._FileHardLimit = params.get("FileHardLimit")
        self._DirectoryPath = params.get("DirectoryPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetUserQuotaResponse(AbstractModel):
    """SetUserQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class SignUpCfsServiceRequest(AbstractModel):
    """SignUpCfsService请求参数结构体

    """


class SignUpCfsServiceResponse(AbstractModel):
    """SignUpCfsService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CfsServiceStatus: 该用户当前 CFS 服务的状态，creating 是开通中，created 是已开通
        :type CfsServiceStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CfsServiceStatus = None
        self._RequestId = None

    @property
    def CfsServiceStatus(self):
        return self._CfsServiceStatus

    @CfsServiceStatus.setter
    def CfsServiceStatus(self, CfsServiceStatus):
        self._CfsServiceStatus = CfsServiceStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CfsServiceStatus = params.get("CfsServiceStatus")
        self._RequestId = params.get("RequestId")


class SnapshotInfo(AbstractModel):
    """快照信息

    """

    def __init__(self):
        r"""
        :param _CreationTime: 创建快照时间
        :type CreationTime: str
        :param _SnapshotName: 快照名称
        :type SnapshotName: str
        :param _SnapshotId: 快照ID
        :type SnapshotId: str
        :param _Status: 快照状态，createing-创建中；available-运行中；deleting-删除中；rollbacking-new 创建新文件系统中；create-failed 创建失败
        :type Status: str
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _Size: 快照大小
        :type Size: int
        :param _AliveDay: 保留时长天
        :type AliveDay: int
        :param _Percent: 快照进度百分比，1表示1%
        :type Percent: int
        :param _AppId: 账号ID
        :type AppId: int
        :param _DeleteTime: 快照删除时间
        :type DeleteTime: str
        :param _FsName: 文件系统名称
        :type FsName: str
        :param _Tags: 快照标签
        :type Tags: list of TagInfo
        :param _SnapshotType: 快照类型, general为通用系列快照，turbo为Turbo系列快照
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotType: str
        :param _SnapshotTime: 实际快照时间，反应快照对应文件系统某个时刻的数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotTime: str
        """
        self._CreationTime = None
        self._SnapshotName = None
        self._SnapshotId = None
        self._Status = None
        self._RegionName = None
        self._FileSystemId = None
        self._Size = None
        self._AliveDay = None
        self._Percent = None
        self._AppId = None
        self._DeleteTime = None
        self._FsName = None
        self._Tags = None
        self._SnapshotType = None
        self._SnapshotTime = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def AliveDay(self):
        return self._AliveDay

    @AliveDay.setter
    def AliveDay(self, AliveDay):
        self._AliveDay = AliveDay

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def DeleteTime(self):
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SnapshotType(self):
        return self._SnapshotType

    @SnapshotType.setter
    def SnapshotType(self, SnapshotType):
        self._SnapshotType = SnapshotType

    @property
    def SnapshotTime(self):
        return self._SnapshotTime

    @SnapshotTime.setter
    def SnapshotTime(self, SnapshotTime):
        self._SnapshotTime = SnapshotTime


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._SnapshotName = params.get("SnapshotName")
        self._SnapshotId = params.get("SnapshotId")
        self._Status = params.get("Status")
        self._RegionName = params.get("RegionName")
        self._FileSystemId = params.get("FileSystemId")
        self._Size = params.get("Size")
        self._AliveDay = params.get("AliveDay")
        self._Percent = params.get("Percent")
        self._AppId = params.get("AppId")
        self._DeleteTime = params.get("DeleteTime")
        self._FsName = params.get("FsName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SnapshotType = params.get("SnapshotType")
        self._SnapshotTime = params.get("SnapshotTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotOperateLog(AbstractModel):
    """快照操作日志

    """

    def __init__(self):
        r"""
        :param _Action: 操作类型
CreateCfsSnapshot：创建快照
DeleteCfsSnapshot：删除快照
CreateCfsFileSystem：创建文件系统
UpdateCfsSnapshotAttribute：更新快照
        :type Action: str
        :param _ActionTime: 操作时间
        :type ActionTime: str
        :param _ActionName: 操作名称
CreateCfsSnapshot
DeleteCfsSnapshot
CreateCfsFileSystem
UpdateCfsSnapshotAttribute
        :type ActionName: str
        :param _Operator: 操作者uin
        :type Operator: str
        :param _Result: 1-任务进行中；2-任务成功；3-任务失败
        :type Result: int
        """
        self._Action = None
        self._ActionTime = None
        self._ActionName = None
        self._Operator = None
        self._Result = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionTime(self):
        return self._ActionTime

    @ActionTime.setter
    def ActionTime(self, ActionTime):
        self._ActionTime = ActionTime

    @property
    def ActionName(self):
        return self._ActionName

    @ActionName.setter
    def ActionName(self, ActionName):
        self._ActionName = ActionName

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._ActionTime = params.get("ActionTime")
        self._ActionName = params.get("ActionName")
        self._Operator = params.get("Operator")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotStatistics(AbstractModel):
    """文件系统快照统计

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _SnapshotNumber: 快照总个数
        :type SnapshotNumber: int
        :param _SnapshotSize: 快照总容量
        :type SnapshotSize: int
        """
        self._Region = None
        self._SnapshotNumber = None
        self._SnapshotSize = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SnapshotNumber(self):
        return self._SnapshotNumber

    @SnapshotNumber.setter
    def SnapshotNumber(self, SnapshotNumber):
        self._SnapshotNumber = SnapshotNumber

    @property
    def SnapshotSize(self):
        return self._SnapshotSize

    @SnapshotSize.setter
    def SnapshotSize(self, SnapshotSize):
        self._SnapshotSize = SnapshotSize


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._SnapshotNumber = params.get("SnapshotNumber")
        self._SnapshotSize = params.get("SnapshotSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrationTaskRequest(AbstractModel):
    """StopMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 迁移任务名称
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrationTaskResponse(AbstractModel):
    """StopMigrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 迁移任务Id
        :type TaskId: str
        :param _Status: 迁移状态。0: 已完成；1: 进行中；2: 已终止
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """Tag信息单元

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
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
        


class TieringDetailInfo(AbstractModel):
    """分层存储详细信息

    """

    def __init__(self):
        r"""
        :param _TieringSizeInBytes: 低频存储容量
注意：此字段可能返回 null，表示取不到有效值。
        :type TieringSizeInBytes: int
        """
        self._TieringSizeInBytes = None

    @property
    def TieringSizeInBytes(self):
        return self._TieringSizeInBytes

    @TieringSizeInBytes.setter
    def TieringSizeInBytes(self, TieringSizeInBytes):
        self._TieringSizeInBytes = TieringSizeInBytes


    def _deserialize(self, params):
        self._TieringSizeInBytes = params.get("TieringSizeInBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoSnapshotPolicyRequest(AbstractModel):
    """UnbindAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemIds: 需要解绑的文件系统ID列表，用"," 分割
        :type FileSystemIds: str
        :param _AutoSnapshotPolicyId: 解绑的快照ID
        :type AutoSnapshotPolicyId: str
        """
        self._FileSystemIds = None
        self._AutoSnapshotPolicyId = None

    @property
    def FileSystemIds(self):
        return self._FileSystemIds

    @FileSystemIds.setter
    def FileSystemIds(self, FileSystemIds):
        self._FileSystemIds = FileSystemIds

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId


    def _deserialize(self, params):
        self._FileSystemIds = params.get("FileSystemIds")
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoSnapshotPolicyResponse(AbstractModel):
    """UnbindAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class UpdateAutoSnapshotPolicyRequest(AbstractModel):
    """UpdateAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param _PolicyName: 快照策略名称
        :type PolicyName: str
        :param _DayOfWeek: 快照定期备份，按照星期一到星期日。 1代表星期一，7代表星期日
        :type DayOfWeek: str
        :param _Hour: 快照定期备份在一天的哪一小时
        :type Hour: str
        :param _AliveDays: 快照保留日期
        :type AliveDays: int
        :param _IsActivated: 是否激活定期快照功能；1代表激活，0代表未激活
        :type IsActivated: int
        :param _DayOfMonth: 定期快照在每月的第几天创建快照，该参数与DayOfWeek互斥
        :type DayOfMonth: str
        :param _IntervalDays: 间隔天数定期执行快照，该参数与DayOfWeek,DayOfMonth 互斥
        :type IntervalDays: int
        """
        self._AutoSnapshotPolicyId = None
        self._PolicyName = None
        self._DayOfWeek = None
        self._Hour = None
        self._AliveDays = None
        self._IsActivated = None
        self._DayOfMonth = None
        self._IntervalDays = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def DayOfWeek(self):
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def AliveDays(self):
        return self._AliveDays

    @AliveDays.setter
    def AliveDays(self, AliveDays):
        self._AliveDays = AliveDays

    @property
    def IsActivated(self):
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def DayOfMonth(self):
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        return self._IntervalDays

    @IntervalDays.setter
    def IntervalDays(self, IntervalDays):
        self._IntervalDays = IntervalDays


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._PolicyName = params.get("PolicyName")
        self._DayOfWeek = params.get("DayOfWeek")
        self._Hour = params.get("Hour")
        self._AliveDays = params.get("AliveDays")
        self._IsActivated = params.get("IsActivated")
        self._DayOfMonth = params.get("DayOfMonth")
        self._IntervalDays = params.get("IntervalDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAutoSnapshotPolicyResponse(AbstractModel):
    """UpdateAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class UpdateCfsFileSystemNameRequest(AbstractModel):
    """UpdateCfsFileSystemName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _FsName: 用户自定义文件系统名称
        :type FsName: str
        """
        self._FileSystemId = None
        self._FsName = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._FsName = params.get("FsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemNameResponse(AbstractModel):
    """UpdateCfsFileSystemName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CreationToken: 用户自定义文件系统名称
        :type CreationToken: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _FsName: 用户自定义文件系统名称
        :type FsName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CreationToken = None
        self._FileSystemId = None
        self._FsName = None
        self._RequestId = None

    @property
    def CreationToken(self):
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CreationToken = params.get("CreationToken")
        self._FileSystemId = params.get("FileSystemId")
        self._FsName = params.get("FsName")
        self._RequestId = params.get("RequestId")


class UpdateCfsFileSystemPGroupRequest(AbstractModel):
    """UpdateCfsFileSystemPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        """
        self._PGroupId = None
        self._FileSystemId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemPGroupResponse(AbstractModel):
    """UpdateCfsFileSystemPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PGroupId = None
        self._FileSystemId = None
        self._RequestId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._FileSystemId = params.get("FileSystemId")
        self._RequestId = params.get("RequestId")


class UpdateCfsFileSystemSizeLimitRequest(AbstractModel):
    """UpdateCfsFileSystemSizeLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FsLimit: 文件系统容量限制大小，输入范围0-1073741824, 单位为GB；其中输入值为0时，表示不限制文件系统容量。
        :type FsLimit: int
        :param _FileSystemId: 文件系统ID，目前仅支持标准型文件系统。
        :type FileSystemId: str
        """
        self._FsLimit = None
        self._FileSystemId = None

    @property
    def FsLimit(self):
        return self._FsLimit

    @FsLimit.setter
    def FsLimit(self, FsLimit):
        self._FsLimit = FsLimit

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FsLimit = params.get("FsLimit")
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemSizeLimitResponse(AbstractModel):
    """UpdateCfsFileSystemSizeLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UpdateCfsPGroupRequest(AbstractModel):
    """UpdateCfsPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _Name: 权限组名称，1-64个字符且只能为中文，字母，数字，下划线或横线
        :type Name: str
        :param _DescInfo: 权限组描述信息，1-255个字符。 Name和Descinfo不能同时为空
        :type DescInfo: str
        """
        self._PGroupId = None
        self._Name = None
        self._DescInfo = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsPGroupResponse(AbstractModel):
    """UpdateCfsPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组ID
        :type PGroupId: str
        :param _Name: 权限组名称
        :type Name: str
        :param _DescInfo: 描述信息
        :type DescInfo: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PGroupId = None
        self._Name = None
        self._DescInfo = None
        self._RequestId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        self._RequestId = params.get("RequestId")


class UpdateCfsRuleRequest(AbstractModel):
    """UpdateCfsRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _RuleId: 规则 ID
        :type RuleId: str
        :param _AuthClientIp: 可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。
        :type AuthClientIp: str
        :param _RWPermission: 读写权限, 值为RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读
        :type RWPermission: str
        :param _UserPermission: 用户权限，值为all_squash、no_all_squash、root_squash、no_root_squash。
all_squash：所有访问用户（含 root 用户）都会被映射为匿名用户或用户组。
no_all_squash：所有访问用户（含 root 用户）均保持原有的 UID/GID 信息。
root_squash：将来访的 root 用户映射为匿名用户或用户组，非 root 用户保持原有的 UID/GID 信息。
no_root_squash：与 no_all_squash 效果一致，所有访问用户（含 root 用户）均保持原有的 UID/GID 信息

        :type UserPermission: str
        :param _Priority: 规则优先级，参数范围1-100。 其中 1 为最高，100为最低
        :type Priority: int
        """
        self._PGroupId = None
        self._RuleId = None
        self._AuthClientIp = None
        self._RWPermission = None
        self._UserPermission = None
        self._Priority = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AuthClientIp(self):
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._RuleId = params.get("RuleId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsRuleResponse(AbstractModel):
    """UpdateCfsRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _RuleId: 规则 ID
        :type RuleId: str
        :param _AuthClientIp: 允许访问的客户端 IP 或者 IP 段
        :type AuthClientIp: str
        :param _RWPermission: 读写权限
        :type RWPermission: str
        :param _UserPermission: 用户权限
        :type UserPermission: str
        :param _Priority: 优先级
        :type Priority: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PGroupId = None
        self._RuleId = None
        self._AuthClientIp = None
        self._RWPermission = None
        self._UserPermission = None
        self._Priority = None
        self._RequestId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AuthClientIp(self):
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._RuleId = params.get("RuleId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        self._Priority = params.get("Priority")
        self._RequestId = params.get("RequestId")


class UpdateCfsSnapshotAttributeRequest(AbstractModel):
    """UpdateCfsSnapshotAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 文件系统快照ID
        :type SnapshotId: str
        :param _SnapshotName: 文件系统快照名称
        :type SnapshotName: str
        :param _AliveDays: 文件系统快照保留天数
        :type AliveDays: int
        """
        self._SnapshotId = None
        self._SnapshotName = None
        self._AliveDays = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def AliveDays(self):
        return self._AliveDays

    @AliveDays.setter
    def AliveDays(self, AliveDays):
        self._AliveDays = AliveDays


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._SnapshotName = params.get("SnapshotName")
        self._AliveDays = params.get("AliveDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsSnapshotAttributeResponse(AbstractModel):
    """UpdateCfsSnapshotAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 文件系统快照ID
        :type SnapshotId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SnapshotId = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class UpdateFileSystemBandwidthLimitRequest(AbstractModel):
    """UpdateFileSystemBandwidthLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _BandwidthLimit: 文件系统带宽，仅吞吐型可填。单位MiB/s，最小为1GiB/s，最大200GiB/s。
        :type BandwidthLimit: int
        """
        self._FileSystemId = None
        self._BandwidthLimit = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def BandwidthLimit(self):
        return self._BandwidthLimit

    @BandwidthLimit.setter
    def BandwidthLimit(self, BandwidthLimit):
        self._BandwidthLimit = BandwidthLimit


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._BandwidthLimit = params.get("BandwidthLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFileSystemBandwidthLimitResponse(AbstractModel):
    """UpdateFileSystemBandwidthLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UserQuota(AbstractModel):
    """文件系统配额信息

    """

    def __init__(self):
        r"""
        :param _UserType: 指定配额类型，包括Uid、Gid、Dir
        :type UserType: str
        :param _UserId: UID/GID信息
        :type UserId: str
        :param _CapacityHardLimit: 容量硬限制，单位GiB
        :type CapacityHardLimit: int
        :param _FileHardLimit: 文件硬限制，单位个
        :type FileHardLimit: int
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _CapacityUsed: 容量使用，单位GiB
注意：此字段可能返回 null，表示取不到有效值。
        :type CapacityUsed: int
        :param _FileUsed: 文件使用个数，单位个
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUsed: int
        :param _DirectoryPath: 目录配额的目录绝对路径
注意：此字段可能返回 null，表示取不到有效值。
        :type DirectoryPath: str
        :param _Status: 配置规则状态，inavailable---配置中，available --已生效，deleting--删除中，deleted 已删除，failed--配置失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._UserType = None
        self._UserId = None
        self._CapacityHardLimit = None
        self._FileHardLimit = None
        self._FileSystemId = None
        self._CapacityUsed = None
        self._FileUsed = None
        self._DirectoryPath = None
        self._Status = None

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def CapacityHardLimit(self):
        return self._CapacityHardLimit

    @CapacityHardLimit.setter
    def CapacityHardLimit(self, CapacityHardLimit):
        self._CapacityHardLimit = CapacityHardLimit

    @property
    def FileHardLimit(self):
        return self._FileHardLimit

    @FileHardLimit.setter
    def FileHardLimit(self, FileHardLimit):
        self._FileHardLimit = FileHardLimit

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def CapacityUsed(self):
        return self._CapacityUsed

    @CapacityUsed.setter
    def CapacityUsed(self, CapacityUsed):
        self._CapacityUsed = CapacityUsed

    @property
    def FileUsed(self):
        return self._FileUsed

    @FileUsed.setter
    def FileUsed(self, FileUsed):
        self._FileUsed = FileUsed

    @property
    def DirectoryPath(self):
        return self._DirectoryPath

    @DirectoryPath.setter
    def DirectoryPath(self, DirectoryPath):
        self._DirectoryPath = DirectoryPath

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._UserType = params.get("UserType")
        self._UserId = params.get("UserId")
        self._CapacityHardLimit = params.get("CapacityHardLimit")
        self._FileHardLimit = params.get("FileHardLimit")
        self._FileSystemId = params.get("FileSystemId")
        self._CapacityUsed = params.get("CapacityUsed")
        self._FileUsed = params.get("FileUsed")
        self._DirectoryPath = params.get("DirectoryPath")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        