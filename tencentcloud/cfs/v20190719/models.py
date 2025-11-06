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


class ApplyPathLifecyclePolicyRequest(AbstractModel):
    r"""ApplyPathLifecyclePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecyclePolicyID: 生命周期管理策略ID
        :type LifecyclePolicyID: str
        :param _Paths: 生命周期管理策略关联目录的绝对路径列表
        :type Paths: list of PathInfo
        """
        self._LifecyclePolicyID = None
        self._Paths = None

    @property
    def LifecyclePolicyID(self):
        r"""生命周期管理策略ID
        :rtype: str
        """
        return self._LifecyclePolicyID

    @LifecyclePolicyID.setter
    def LifecyclePolicyID(self, LifecyclePolicyID):
        self._LifecyclePolicyID = LifecyclePolicyID

    @property
    def Paths(self):
        r"""生命周期管理策略关联目录的绝对路径列表
        :rtype: list of PathInfo
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths


    def _deserialize(self, params):
        self._LifecyclePolicyID = params.get("LifecyclePolicyID")
        if params.get("Paths") is not None:
            self._Paths = []
            for item in params.get("Paths"):
                obj = PathInfo()
                obj._deserialize(item)
                self._Paths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyPathLifecyclePolicyResponse(AbstractModel):
    r"""ApplyPathLifecyclePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckResults: 有规则冲突时返回的已有冲突规则信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckResults: list of CheckResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckResults = None
        self._RequestId = None

    @property
    def CheckResults(self):
        r"""有规则冲突时返回的已有冲突规则信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CheckResult
        """
        return self._CheckResults

    @CheckResults.setter
    def CheckResults(self, CheckResults):
        self._CheckResults = CheckResults

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
        if params.get("CheckResults") is not None:
            self._CheckResults = []
            for item in params.get("CheckResults"):
                obj = CheckResult()
                obj._deserialize(item)
                self._CheckResults.append(obj)
        self._RequestId = params.get("RequestId")


class AutoScaleUpRule(AbstractModel):
    r"""自动扩容规则

    """

    def __init__(self):
        r"""
        :param _Status: 自动扩容策略开启，关闭
        :type Status: str
        :param _ScaleThreshold: 集群用量占比，到达这个值后开始扩容,范围[10-90]
        :type ScaleThreshold: int
        :param _TargetThreshold: 扩容后使用量跟集群总量比例,范围[10-90]
        :type TargetThreshold: int
        """
        self._Status = None
        self._ScaleThreshold = None
        self._TargetThreshold = None

    @property
    def Status(self):
        r"""自动扩容策略开启，关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ScaleThreshold(self):
        r"""集群用量占比，到达这个值后开始扩容,范围[10-90]
        :rtype: int
        """
        return self._ScaleThreshold

    @ScaleThreshold.setter
    def ScaleThreshold(self, ScaleThreshold):
        self._ScaleThreshold = ScaleThreshold

    @property
    def TargetThreshold(self):
        r"""扩容后使用量跟集群总量比例,范围[10-90]
        :rtype: int
        """
        return self._TargetThreshold

    @TargetThreshold.setter
    def TargetThreshold(self, TargetThreshold):
        self._TargetThreshold = TargetThreshold


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ScaleThreshold = params.get("ScaleThreshold")
        self._TargetThreshold = params.get("TargetThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoSnapshotPolicyInfo(AbstractModel):
    r"""快照策略信息

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param _PolicyName: 快照策略名称
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
        :param _Status: 快照策略状态，available代表快照策略状态正常。这里只有一种状态
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
        r"""快照策略ID
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def PolicyName(self):
        r"""快照策略名称
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def CreationTime(self):
        r"""快照策略创建时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def FileSystemNums(self):
        r"""关联的文件系统个数
        :rtype: int
        """
        return self._FileSystemNums

    @FileSystemNums.setter
    def FileSystemNums(self, FileSystemNums):
        self._FileSystemNums = FileSystemNums

    @property
    def DayOfWeek(self):
        r"""快照定期备份在一星期哪一天，该参数与DayOfMonth,IntervalDays互斥
        :rtype: str
        """
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def Hour(self):
        r"""快照定期备份在一天的哪一小时
        :rtype: str
        """
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def IsActivated(self):
        r"""是否激活定期快照功能,1代表已激活，0代表未激活
        :rtype: int
        """
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def NextActiveTime(self):
        r"""下一次触发快照时间
        :rtype: str
        """
        return self._NextActiveTime

    @NextActiveTime.setter
    def NextActiveTime(self, NextActiveTime):
        self._NextActiveTime = NextActiveTime

    @property
    def Status(self):
        r"""快照策略状态，available代表快照策略状态正常。这里只有一种状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AppId(self):
        r"""账号ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AliveDays(self):
        r"""保留时间
        :rtype: int
        """
        return self._AliveDays

    @AliveDays.setter
    def AliveDays(self, AliveDays):
        self._AliveDays = AliveDays

    @property
    def RegionName(self):
        r"""地域
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def FileSystems(self):
        r"""文件系统信息
        :rtype: list of FileSystemByPolicy
        """
        return self._FileSystems

    @FileSystems.setter
    def FileSystems(self, FileSystems):
        self._FileSystems = FileSystems

    @property
    def DayOfMonth(self):
        r"""快照定期备份在一个月的某个时间；该参数与DayOfWeek,IntervalDays互斥
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        r"""快照定期间隔天数，1-365 天；该参数与DayOfMonth,DayOfWeek互斥
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IntervalDays

    @IntervalDays.setter
    def IntervalDays(self, IntervalDays):
        self._IntervalDays = IntervalDays

    @property
    def CrossRegionsAliveDays(self):
        r"""跨地域复制的快照保留时间，单位天
        :rtype: int
        """
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
    r"""版本控制-协议详情

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
        r"""售卖状态。可选值有 sale_out 售罄、saling可售、no_saling不可销售
        :rtype: str
        """
        return self._SaleStatus

    @SaleStatus.setter
    def SaleStatus(self, SaleStatus):
        self._SaleStatus = SaleStatus

    @property
    def Protocol(self):
        r"""协议类型。可选值有 NFS、CIFS、TURBO
        :rtype: str
        """
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
    r"""版本控制-区域数组

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
        r"""区域名称，如“ap-beijing”
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        r"""区域名称，如“bj”
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionStatus(self):
        r"""区域可用情况，当区域内至少有一个可用区处于可售状态时，取值为AVAILABLE，否则为UNAVAILABLE
        :rtype: str
        """
        return self._RegionStatus

    @RegionStatus.setter
    def RegionStatus(self, RegionStatus):
        self._RegionStatus = RegionStatus

    @property
    def Zones(self):
        r"""可用区数组
        :rtype: list of AvailableZone
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RegionCnName(self):
        r"""区域中文名称，如“广州”
        :rtype: str
        """
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
    r"""版本控制-类型数组

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
        r"""协议与售卖详情
        :rtype: list of AvailableProtoStatus
        """
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def Type(self):
        r"""存储类型。返回值中 SD 为通用标准型存储， HP为通用性能型存储， TB为Turbo标准型， TP 为Turbo性能型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Prepayment(self):
        r"""是否支持预付费。返回值中 true 为支持、false 为不支持
        :rtype: bool
        """
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
    r"""版本控制-可用区数组

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
        r"""可用区名称
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        r"""可用区ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneCnName(self):
        r"""可用区中文名称
        :rtype: str
        """
        return self._ZoneCnName

    @ZoneCnName.setter
    def ZoneCnName(self, ZoneCnName):
        self._ZoneCnName = ZoneCnName

    @property
    def Types(self):
        r"""Type数组
        :rtype: list of AvailableType
        """
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

    @property
    def ZoneName(self):
        r"""可用区中英文名称
        :rtype: str
        """
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
    r"""BindAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 需要解绑的文件系统ID列表，用"," 分割，文件系统ID，通过查询文件系统列表获取；[DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170)
        :type AutoSnapshotPolicyId: str
        :param _FileSystemIds: 解绑的快照策略ID，可以通过[DescribeAutoSnapshotPolicies](https://cloud.tencent.com/document/api/582/80208) 查询获取
        :type FileSystemIds: str
        """
        self._AutoSnapshotPolicyId = None
        self._FileSystemIds = None

    @property
    def AutoSnapshotPolicyId(self):
        r"""需要解绑的文件系统ID列表，用"," 分割，文件系统ID，通过查询文件系统列表获取；[DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170)
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def FileSystemIds(self):
        r"""解绑的快照策略ID，可以通过[DescribeAutoSnapshotPolicies](https://cloud.tencent.com/document/api/582/80208) 查询获取
        :rtype: str
        """
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
    r"""BindAutoSnapshotPolicy返回参数结构体

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
        r"""快照策略ID
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

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
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class BucketInfo(AbstractModel):
    r"""对象存储桶

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
        r"""桶名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Region(self):
        r"""桶所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class CheckResult(AbstractModel):
    r"""有规则冲突时返回的已有冲突规则信息列表

    """

    def __init__(self):
        r"""
        :param _LifecyclePolicyID: 生命周期管理策略ID
        :type LifecyclePolicyID: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _Path: 目录绝对路径
        :type Path: str
        :param _LifecycleRules: 生命周期管理策略关联的管理规则列表
        :type LifecycleRules: list of LifecycleRule
        :param _TargetPath: 目标路径
        :type TargetPath: str
        """
        self._LifecyclePolicyID = None
        self._FileSystemId = None
        self._Path = None
        self._LifecycleRules = None
        self._TargetPath = None

    @property
    def LifecyclePolicyID(self):
        r"""生命周期管理策略ID
        :rtype: str
        """
        return self._LifecyclePolicyID

    @LifecyclePolicyID.setter
    def LifecyclePolicyID(self, LifecyclePolicyID):
        self._LifecyclePolicyID = LifecyclePolicyID

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Path(self):
        r"""目录绝对路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def LifecycleRules(self):
        r"""生命周期管理策略关联的管理规则列表
        :rtype: list of LifecycleRule
        """
        return self._LifecycleRules

    @LifecycleRules.setter
    def LifecycleRules(self, LifecycleRules):
        self._LifecycleRules = LifecycleRules

    @property
    def TargetPath(self):
        r"""目标路径
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath


    def _deserialize(self, params):
        self._LifecyclePolicyID = params.get("LifecyclePolicyID")
        self._FileSystemId = params.get("FileSystemId")
        self._Path = params.get("Path")
        if params.get("LifecycleRules") is not None:
            self._LifecycleRules = []
            for item in params.get("LifecycleRules"):
                obj = LifecycleRule()
                obj._deserialize(item)
                self._LifecycleRules.append(obj)
        self._TargetPath = params.get("TargetPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessCertRequest(AbstractModel):
    r"""CreateAccessCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertDesc: 证书描述，不超过64字符
        :type CertDesc: str
        """
        self._CertDesc = None

    @property
    def CertDesc(self):
        r"""证书描述，不超过64字符
        :rtype: str
        """
        return self._CertDesc

    @CertDesc.setter
    def CertDesc(self, CertDesc):
        self._CertDesc = CertDesc


    def _deserialize(self, params):
        self._CertDesc = params.get("CertDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessCertResponse(AbstractModel):
    r"""CreateAccessCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertId: 凭证唯一标识
        :type CertId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertId = None
        self._RequestId = None

    @property
    def CertId(self):
        r"""凭证唯一标识
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

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
        self._CertId = params.get("CertId")
        self._RequestId = params.get("RequestId")


class CreateAutoSnapshotPolicyRequest(AbstractModel):
    r"""CreateAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Hour: 快照重复时间点,0-23，小时
        :type Hour: str
        :param _PolicyName: 策略名称,限制64个字符数量仅支持输入中文、字母、数字、_或-
        :type PolicyName: str
        :param _DayOfWeek: 快照重复日期，星期一到星期日。 1代表星期一、7代表星期天，与DayOfMonth，IntervalDays 三者选一
        :type DayOfWeek: str
        :param _AliveDays: 快照保留时长，单位天，默认永久0
        :type AliveDays: int
        :param _DayOfMonth: 快照按月重复，每月1-31号，选择一天，每月将在这一天自动创建快照；例如1 代表1号；与DayOfWeek，IntervalDays 三者选一
        :type DayOfMonth: str
        :param _IntervalDays: 间隔天数，与DayOfWeek，DayOfMonth 三者选一
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
        r"""快照重复时间点,0-23，小时
        :rtype: str
        """
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def PolicyName(self):
        r"""策略名称,限制64个字符数量仅支持输入中文、字母、数字、_或-
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def DayOfWeek(self):
        r"""快照重复日期，星期一到星期日。 1代表星期一、7代表星期天，与DayOfMonth，IntervalDays 三者选一
        :rtype: str
        """
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def AliveDays(self):
        r"""快照保留时长，单位天，默认永久0
        :rtype: int
        """
        return self._AliveDays

    @AliveDays.setter
    def AliveDays(self, AliveDays):
        self._AliveDays = AliveDays

    @property
    def DayOfMonth(self):
        r"""快照按月重复，每月1-31号，选择一天，每月将在这一天自动创建快照；例如1 代表1号；与DayOfWeek，IntervalDays 三者选一
        :rtype: str
        """
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        r"""间隔天数，与DayOfWeek，DayOfMonth 三者选一
        :rtype: int
        """
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
    r"""CreateAutoSnapshotPolicy返回参数结构体

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
        r"""快照策略ID
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

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
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class CreateCfsFileSystemRequest(AbstractModel):
    r"""CreateCfsFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区名称，例如ap-beijing-1，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的地域与可用区列表
        :type Zone: str
        :param _NetInterface: 网络类型，可选值为 VPC，CCN；其中 VPC 为私有网络， CCN 为云联网。通用标准型/性能型请选择VPC，Turbo标准型/性能型请选择CCN。
        :type NetInterface: str
        :param _PGroupId: 权限组 ID,pgroupbasic 是默认权限组，通过控制查询权限组列表接口获取[DescribeCfsPGroups](https://cloud.tencent.com/document/product/582/38157)
        :type PGroupId: str
        :param _Protocol: 文件系统协议类型， 值为 NFS、CIFS、TURBO ; 若留空则默认为 NFS协议，turbo系列必须选择TURBO，不支持NFS、CIFS
        :type Protocol: str
        :param _StorageType: 文件系统存储类型，默认值为 SD ；其中 SD 为通用标准型存储， HP为通用性能型存储， TB为Turbo标准型， TP 为Turbo性能型。
        :type StorageType: str
        :param _VpcId: 私有网络（VPC） ID，若网络类型选择的是VPC，该字段为必填.通过查询私有网络接口获取，
[DescribeVpcs](https://cloud.tencent.com/document/product/215/15778)
        :type VpcId: str
        :param _SubnetId: 子网 ID，若网络类型选择的是VPC，该字段为必填。通过查询子网接口获取，
[DescribeSubnets](https://cloud.tencent.com/document/product/215/15784)
        :type SubnetId: str
        :param _MountIP: 指定IP地址，仅VPC网络支持；若不填写、将在该子网下随机分配 IP，Turbo系列当前不支持指定
        :type MountIP: str
        :param _FsName: 用户自定义文件系统名称
        :type FsName: str
        :param _ResourceTags: 文件系统标签
        :type ResourceTags: list of TagInfo
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。用于保证请求幂等性的字符串失效时间为2小时。
        :type ClientToken: str
        :param _CcnId: 云联网ID， 若网络类型选择的是CCN，该字段为必填;通过查询云联网列表接口获取，通过接口
[DescribeCcns](https://cloud.tencent.com/document/product/215/19199)

        :type CcnId: str
        :param _CidrBlock: 云联网中CFS使用的网段， 若网络类型选择的是Ccn，该字段为必填，且不能和Ccn中已经绑定的网段冲突
        :type CidrBlock: str
        :param _Capacity: 文件系统容量，turbo系列必填，单位为GiB。 turbo标准型单位GB，起售20TiB，即20480 GiB；扩容步长10TiB，即10240 GiB。turbo性能型起售10TiB，即10240 GiB；扩容步长10TiB，10240 GiB。
        :type Capacity: int
        :param _SnapshotId: 文件系统快照ID，通过查询快照列表获取该参数，
[DescribeCfsSnapshots](https://cloud.tencent.com/document/product/582/80206)
        :type SnapshotId: str
        :param _AutoSnapshotPolicyId: 定期快照策略ID，通过查询快照策略信息获取,
[DescribeAutoSnapshotPolicies](https://cloud.tencent.com/document/product/582/38157)
        :type AutoSnapshotPolicyId: str
        :param _EnableAutoScaleUp: 是否开启默认扩容，仅turbo类型文件存储支持
        :type EnableAutoScaleUp: bool
        :param _CfsVersion: v1.5：创建普通版的通用文件系统；
v3.1：创建增强版的通用文件系统
说明：增强版的通用系统需要开通白名单才能使用，如有需要请提交工单与我们联系。
        :type CfsVersion: str
        :param _MetaType: turbo文件系统元数据属性
basic：创建标准型的元数据
enhanced：创建增强型的元数据
        :type MetaType: str
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
        self._CfsVersion = None
        self._MetaType = None

    @property
    def Zone(self):
        r"""可用区名称，例如ap-beijing-1，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的地域与可用区列表
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NetInterface(self):
        r"""网络类型，可选值为 VPC，CCN；其中 VPC 为私有网络， CCN 为云联网。通用标准型/性能型请选择VPC，Turbo标准型/性能型请选择CCN。
        :rtype: str
        """
        return self._NetInterface

    @NetInterface.setter
    def NetInterface(self, NetInterface):
        self._NetInterface = NetInterface

    @property
    def PGroupId(self):
        r"""权限组 ID,pgroupbasic 是默认权限组，通过控制查询权限组列表接口获取[DescribeCfsPGroups](https://cloud.tencent.com/document/product/582/38157)
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Protocol(self):
        r"""文件系统协议类型， 值为 NFS、CIFS、TURBO ; 若留空则默认为 NFS协议，turbo系列必须选择TURBO，不支持NFS、CIFS
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def StorageType(self):
        r"""文件系统存储类型，默认值为 SD ；其中 SD 为通用标准型存储， HP为通用性能型存储， TB为Turbo标准型， TP 为Turbo性能型。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def VpcId(self):
        r"""私有网络（VPC） ID，若网络类型选择的是VPC，该字段为必填.通过查询私有网络接口获取，
[DescribeVpcs](https://cloud.tencent.com/document/product/215/15778)
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网 ID，若网络类型选择的是VPC，该字段为必填。通过查询子网接口获取，
[DescribeSubnets](https://cloud.tencent.com/document/product/215/15784)
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def MountIP(self):
        r"""指定IP地址，仅VPC网络支持；若不填写、将在该子网下随机分配 IP，Turbo系列当前不支持指定
        :rtype: str
        """
        return self._MountIP

    @MountIP.setter
    def MountIP(self, MountIP):
        self._MountIP = MountIP

    @property
    def FsName(self):
        r"""用户自定义文件系统名称
        :rtype: str
        """
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def ResourceTags(self):
        r"""文件系统标签
        :rtype: list of TagInfo
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def ClientToken(self):
        r"""用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。用于保证请求幂等性的字符串失效时间为2小时。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def CcnId(self):
        r"""云联网ID， 若网络类型选择的是CCN，该字段为必填;通过查询云联网列表接口获取，通过接口
[DescribeCcns](https://cloud.tencent.com/document/product/215/19199)

        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def CidrBlock(self):
        r"""云联网中CFS使用的网段， 若网络类型选择的是Ccn，该字段为必填，且不能和Ccn中已经绑定的网段冲突
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Capacity(self):
        r"""文件系统容量，turbo系列必填，单位为GiB。 turbo标准型单位GB，起售20TiB，即20480 GiB；扩容步长10TiB，即10240 GiB。turbo性能型起售10TiB，即10240 GiB；扩容步长10TiB，10240 GiB。
        :rtype: int
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def SnapshotId(self):
        r"""文件系统快照ID，通过查询快照列表获取该参数，
[DescribeCfsSnapshots](https://cloud.tencent.com/document/product/582/80206)
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def AutoSnapshotPolicyId(self):
        r"""定期快照策略ID，通过查询快照策略信息获取,
[DescribeAutoSnapshotPolicies](https://cloud.tencent.com/document/product/582/38157)
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def EnableAutoScaleUp(self):
        r"""是否开启默认扩容，仅turbo类型文件存储支持
        :rtype: bool
        """
        return self._EnableAutoScaleUp

    @EnableAutoScaleUp.setter
    def EnableAutoScaleUp(self, EnableAutoScaleUp):
        self._EnableAutoScaleUp = EnableAutoScaleUp

    @property
    def CfsVersion(self):
        r"""v1.5：创建普通版的通用文件系统；
v3.1：创建增强版的通用文件系统
说明：增强版的通用系统需要开通白名单才能使用，如有需要请提交工单与我们联系。
        :rtype: str
        """
        return self._CfsVersion

    @CfsVersion.setter
    def CfsVersion(self, CfsVersion):
        self._CfsVersion = CfsVersion

    @property
    def MetaType(self):
        r"""turbo文件系统元数据属性
basic：创建标准型的元数据
enhanced：创建增强型的元数据
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType


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
        self._CfsVersion = params.get("CfsVersion")
        self._MetaType = params.get("MetaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsFileSystemResponse(AbstractModel):
    r"""CreateCfsFileSystem返回参数结构体

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
        r"""文件系统创建时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def CreationToken(self):
        r"""用户自定义文件系统名称
        :rtype: str
        """
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        r"""文件系统 ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def LifeCycleState(self):
        r"""文件系统状态，可能出现状态包括：“creating”  创建中, “create_failed” 创建失败, “available” 可用, “unserviced” 不可用, “upgrading” 升级中， “deleting” 删除中。
        :rtype: str
        """
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def SizeByte(self):
        r"""文件系统已使用容量大小，单位为 Byte
        :rtype: int
        """
        return self._SizeByte

    @SizeByte.setter
    def SizeByte(self, SizeByte):
        self._SizeByte = SizeByte

    @property
    def ZoneId(self):
        r"""可用区 ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def FsName(self):
        r"""用户自定义文件系统名称
        :rtype: str
        """
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def Encrypted(self):
        r"""文件系统是否加密
        :rtype: bool
        """
        return self._Encrypted

    @Encrypted.setter
    def Encrypted(self, Encrypted):
        self._Encrypted = Encrypted

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
    r"""CreateCfsPGroup请求参数结构体

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
        r"""权限组名称，1-64个字符且只能为中文，字母，数字，下划线或横线
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        r"""权限组描述信息，1-255个字符
        :rtype: str
        """
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
    r"""CreateCfsPGroup返回参数结构体

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
        r"""权限组 ID
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        r"""权限组名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        r"""权限组描述信息
        :rtype: str
        """
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo

    @property
    def BindCfsNum(self):
        r"""已经与该权限组绑定的文件系统个数
        :rtype: int
        """
        return self._BindCfsNum

    @BindCfsNum.setter
    def BindCfsNum(self, BindCfsNum):
        self._BindCfsNum = BindCfsNum

    @property
    def CDate(self):
        r"""权限组创建时间
        :rtype: str
        """
        return self._CDate

    @CDate.setter
    def CDate(self, CDate):
        self._CDate = CDate

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
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        self._BindCfsNum = params.get("BindCfsNum")
        self._CDate = params.get("CDate")
        self._RequestId = params.get("RequestId")


class CreateCfsRuleRequest(AbstractModel):
    r"""CreateCfsRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :type PGroupId: str
        :param _AuthClientIp: 可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。
        :type AuthClientIp: str
        :param _Priority: 规则优先级，参数范围1-100。 其中 1 为最高，100为最低
        :type Priority: int
        :param _RWPermission: 读写权限, 值为 RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读
        :type RWPermission: str
        :param _UserPermission: 用户权限，值为 all_squash、no_all_squash、root_squash、no_root_squash。默认值为root_squash
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
        r"""权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def AuthClientIp(self):
        r"""可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。
        :rtype: str
        """
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def Priority(self):
        r"""规则优先级，参数范围1-100。 其中 1 为最高，100为最低
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RWPermission(self):
        r"""读写权限, 值为 RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读
        :rtype: str
        """
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        r"""用户权限，值为 all_squash、no_all_squash、root_squash、no_root_squash。默认值为root_squash
all_squash：所有访问用户（含 root 用户）都会被映射为匿名用户或用户组。
no_all_squash：所有访问用户（含 root 用户）均保持原有的 UID/GID 信息。
root_squash：将来访的 root 用户映射为匿名用户或用户组，非 root 用户保持原有的 UID/GID 信息。
no_root_squash：与 no_all_squash 效果一致，所有访问用户（含 root 用户）均保持原有的 UID/GID 信息

        :rtype: str
        """
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
    r"""CreateCfsRule返回参数结构体

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
        r"""规则 ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def PGroupId(self):
        r"""权限组 ID
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def AuthClientIp(self):
        r"""客户端 IP
        :rtype: str
        """
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        r"""读写权限
        :rtype: str
        """
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        r"""用户权限
        :rtype: str
        """
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        r"""优先级
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

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
        self._RuleId = params.get("RuleId")
        self._PGroupId = params.get("PGroupId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        self._Priority = params.get("Priority")
        self._RequestId = params.get("RequestId")


class CreateCfsSnapshotRequest(AbstractModel):
    r"""CreateCfsSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID，通过查询文件系统列表获取；[DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170)
        :type FileSystemId: str
        :param _SnapshotName: 快照名称，支持不超过64字符长度，支持中文、数字、_、-
        :type SnapshotName: str
        :param _ResourceTags: 快照标签
        :type ResourceTags: list of TagInfo
        """
        self._FileSystemId = None
        self._SnapshotName = None
        self._ResourceTags = None

    @property
    def FileSystemId(self):
        r"""文件系统ID，通过查询文件系统列表获取；[DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170)
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SnapshotName(self):
        r"""快照名称，支持不超过64字符长度，支持中文、数字、_、-
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def ResourceTags(self):
        r"""快照标签
        :rtype: list of TagInfo
        """
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
    r"""CreateCfsSnapshot返回参数结构体

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
        r"""文件系统快照id
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

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
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class CreateDataFlowRequest(AbstractModel):
    r"""CreateDataFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID ，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :type FileSystemId: str
        :param _SourceStorageType: 源端数据类型；包含S3_COS，S3_L5 
        :type SourceStorageType: str
        :param _SourceStorageAddress: 源端存储地址
        :type SourceStorageAddress: str
        :param _SourcePath: 源端路径
        :type SourcePath: str
        :param _TargetPath: 文件系统内目标路径
        :type TargetPath: str
        :param _SecretId: 密钥 ID
        :type SecretId: str
        :param _SecretKey: 密钥 key
        :type SecretKey: str
        :param _DataFlowName: 数据流动名称；支持不超过64字符长度，支持中文、数字、_、-
        :type DataFlowName: str
        :param _AutoRefresh:  0：不开启自动更新  1：开启自动更新
        :type AutoRefresh: int
        :param _UserKafkaTopic: KafkaConsumer 消费时使用的Topic参数
        :type UserKafkaTopic: str
        :param _ServerAddr: 	服务地址 示例值：kafkaconsumer-ap-beijing.cls.tencentyun.com:9095
        :type ServerAddr: str
        :param _UserName: Kafka消费用户名.示例值：name
        :type UserName: str
        :param _Password: Kafka消费用户密码。默认${SecretId}#${SecretKey}。
        :type Password: str
        """
        self._FileSystemId = None
        self._SourceStorageType = None
        self._SourceStorageAddress = None
        self._SourcePath = None
        self._TargetPath = None
        self._SecretId = None
        self._SecretKey = None
        self._DataFlowName = None
        self._AutoRefresh = None
        self._UserKafkaTopic = None
        self._ServerAddr = None
        self._UserName = None
        self._Password = None

    @property
    def FileSystemId(self):
        r"""文件系统 ID ，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SourceStorageType(self):
        r"""源端数据类型；包含S3_COS，S3_L5 
        :rtype: str
        """
        return self._SourceStorageType

    @SourceStorageType.setter
    def SourceStorageType(self, SourceStorageType):
        self._SourceStorageType = SourceStorageType

    @property
    def SourceStorageAddress(self):
        r"""源端存储地址
        :rtype: str
        """
        return self._SourceStorageAddress

    @SourceStorageAddress.setter
    def SourceStorageAddress(self, SourceStorageAddress):
        self._SourceStorageAddress = SourceStorageAddress

    @property
    def SourcePath(self):
        r"""源端路径
        :rtype: str
        """
        return self._SourcePath

    @SourcePath.setter
    def SourcePath(self, SourcePath):
        self._SourcePath = SourcePath

    @property
    def TargetPath(self):
        r"""文件系统内目标路径
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath

    @property
    def SecretId(self):
        r"""密钥 ID
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        r"""密钥 key
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def DataFlowName(self):
        r"""数据流动名称；支持不超过64字符长度，支持中文、数字、_、-
        :rtype: str
        """
        return self._DataFlowName

    @DataFlowName.setter
    def DataFlowName(self, DataFlowName):
        self._DataFlowName = DataFlowName

    @property
    def AutoRefresh(self):
        r""" 0：不开启自动更新  1：开启自动更新
        :rtype: int
        """
        return self._AutoRefresh

    @AutoRefresh.setter
    def AutoRefresh(self, AutoRefresh):
        self._AutoRefresh = AutoRefresh

    @property
    def UserKafkaTopic(self):
        r"""KafkaConsumer 消费时使用的Topic参数
        :rtype: str
        """
        return self._UserKafkaTopic

    @UserKafkaTopic.setter
    def UserKafkaTopic(self, UserKafkaTopic):
        self._UserKafkaTopic = UserKafkaTopic

    @property
    def ServerAddr(self):
        r"""	服务地址 示例值：kafkaconsumer-ap-beijing.cls.tencentyun.com:9095
        :rtype: str
        """
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def UserName(self):
        r"""Kafka消费用户名.示例值：name
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""Kafka消费用户密码。默认${SecretId}#${SecretKey}。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._SourceStorageType = params.get("SourceStorageType")
        self._SourceStorageAddress = params.get("SourceStorageAddress")
        self._SourcePath = params.get("SourcePath")
        self._TargetPath = params.get("TargetPath")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._DataFlowName = params.get("DataFlowName")
        self._AutoRefresh = params.get("AutoRefresh")
        self._UserKafkaTopic = params.get("UserKafkaTopic")
        self._ServerAddr = params.get("ServerAddr")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataFlowResponse(AbstractModel):
    r"""CreateDataFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataFlowId: 数据流动管理 ID
        :type DataFlowId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataFlowId = None
        self._RequestId = None

    @property
    def DataFlowId(self):
        r"""数据流动管理 ID
        :rtype: str
        """
        return self._DataFlowId

    @DataFlowId.setter
    def DataFlowId(self, DataFlowId):
        self._DataFlowId = DataFlowId

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
        self._DataFlowId = params.get("DataFlowId")
        self._RequestId = params.get("RequestId")


class CreateLifecycleDataTaskRequest(AbstractModel):
    r"""CreateLifecycleDataTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统唯一 ID
        :type FileSystemId: str
        :param _Type: 生命周期任务类型；archive：沉降；restore：预热；release：数据释放；metaload：元数据加载
        :type Type: str
        :param _TaskPath: 需要沉降的路径或文件，仅支持传入1个路径，不允许为空。
        :type TaskPath: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _DataFlowId: 数据流动 ID ，该接口可以通过 DescribeDataFlow 查询
        :type DataFlowId: str
        """
        self._FileSystemId = None
        self._Type = None
        self._TaskPath = None
        self._TaskName = None
        self._DataFlowId = None

    @property
    def FileSystemId(self):
        r"""文件系统唯一 ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Type(self):
        r"""生命周期任务类型；archive：沉降；restore：预热；release：数据释放；metaload：元数据加载
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TaskPath(self):
        r"""需要沉降的路径或文件，仅支持传入1个路径，不允许为空。
        :rtype: str
        """
        return self._TaskPath

    @TaskPath.setter
    def TaskPath(self, TaskPath):
        self._TaskPath = TaskPath

    @property
    def TaskName(self):
        r"""任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def DataFlowId(self):
        r"""数据流动 ID ，该接口可以通过 DescribeDataFlow 查询
        :rtype: str
        """
        return self._DataFlowId

    @DataFlowId.setter
    def DataFlowId(self, DataFlowId):
        self._DataFlowId = DataFlowId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._Type = params.get("Type")
        self._TaskPath = params.get("TaskPath")
        self._TaskName = params.get("TaskName")
        self._DataFlowId = params.get("DataFlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLifecycleDataTaskResponse(AbstractModel):
    r"""CreateLifecycleDataTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务 ID
        :rtype: str
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


class CreateLifecyclePolicyDownloadTaskRequest(AbstractModel):
    r"""CreateLifecyclePolicyDownloadTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _Type: 下载文件的类型，包含 FileSuccessList，FileTotalList，FileFailedList
        :type Type: str
        """
        self._TaskId = None
        self._Type = None

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Type(self):
        r"""下载文件的类型，包含 FileSuccessList，FileTotalList，FileFailedList
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLifecyclePolicyDownloadTaskResponse(AbstractModel):
    r"""CreateLifecyclePolicyDownloadTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadAddress: 下载路径
        :type DownloadAddress: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadAddress = None
        self._RequestId = None

    @property
    def DownloadAddress(self):
        r"""下载路径
        :rtype: str
        """
        return self._DownloadAddress

    @DownloadAddress.setter
    def DownloadAddress(self, DownloadAddress):
        self._DownloadAddress = DownloadAddress

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
        self._DownloadAddress = params.get("DownloadAddress")
        self._RequestId = params.get("RequestId")


class CreateLifecyclePolicyRequest(AbstractModel):
    r"""CreateLifecyclePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecyclePolicyName: 生命周期管理策略名称，中文/英文/数字/下划线/中划线的组合，不超过64个字符
        :type LifecyclePolicyName: str
        :param _LifecycleRules: 生命周期管理策略关联的管理规则列表
        :type LifecycleRules: list of LifecycleRule
        """
        self._LifecyclePolicyName = None
        self._LifecycleRules = None

    @property
    def LifecyclePolicyName(self):
        r"""生命周期管理策略名称，中文/英文/数字/下划线/中划线的组合，不超过64个字符
        :rtype: str
        """
        return self._LifecyclePolicyName

    @LifecyclePolicyName.setter
    def LifecyclePolicyName(self, LifecyclePolicyName):
        self._LifecyclePolicyName = LifecyclePolicyName

    @property
    def LifecycleRules(self):
        r"""生命周期管理策略关联的管理规则列表
        :rtype: list of LifecycleRule
        """
        return self._LifecycleRules

    @LifecycleRules.setter
    def LifecycleRules(self, LifecycleRules):
        self._LifecycleRules = LifecycleRules


    def _deserialize(self, params):
        self._LifecyclePolicyName = params.get("LifecyclePolicyName")
        if params.get("LifecycleRules") is not None:
            self._LifecycleRules = []
            for item in params.get("LifecycleRules"):
                obj = LifecycleRule()
                obj._deserialize(item)
                self._LifecycleRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLifecyclePolicyResponse(AbstractModel):
    r"""CreateLifecyclePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecyclePolicyID: 生命周期管理策略ID
        :type LifecyclePolicyID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LifecyclePolicyID = None
        self._RequestId = None

    @property
    def LifecyclePolicyID(self):
        r"""生命周期管理策略ID
        :rtype: str
        """
        return self._LifecyclePolicyID

    @LifecyclePolicyID.setter
    def LifecyclePolicyID(self, LifecyclePolicyID):
        self._LifecyclePolicyID = LifecyclePolicyID

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
        self._LifecyclePolicyID = params.get("LifecyclePolicyID")
        self._RequestId = params.get("RequestId")


class CreateMigrationTaskRequest(AbstractModel):
    r"""CreateMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskName: 迁移任务名称
        :type TaskName: str
        :param _MigrationType: 迁移方式标志位，默认为0。0：桶迁移；1：清单迁移
        :type MigrationType: int
        :param _MigrationMode: 迁移模式，默认为0。0: 全量迁移
        :type MigrationMode: int
        :param _SrcSecretId: 数据源账号的 SecretId
        :type SrcSecretId: str
        :param _SrcSecretKey: 数据源账号的 SecretKey
        :type SrcSecretKey: str
        :param _FileSystemId: 文件系统实例 ID，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :type FileSystemId: str
        :param _FsPath: 文件系统路径
        :type FsPath: str
        :param _CoverType: 同名文件迁移时覆盖策略，默认为0。0: 最后修改时间优先；1: 全覆盖；2: 不覆盖
        :type CoverType: int
        :param _SrcService: 数据源服务商。COS：腾讯云COS，OSS：阿里云OSS，OBS：华为云OBS
        :type SrcService: str
        :param _BucketName: 数据源桶名称；桶迁移时，BucketName 和 BucketAddress 必填其一，清单迁移时无需填写此参数
        :type BucketName: str
        :param _BucketRegion: 数据源桶地域
        :type BucketRegion: str
        :param _BucketAddress: 数据源桶地址；桶迁移时，BucketName 和 BucketAddress 必填其一，清单迁移时无需填写此参数
        :type BucketAddress: str
        :param _ListAddress: 清单地址，迁移方式为清单迁移时必填
        :type ListAddress: str
        :param _FsName: 目标文件系统名称
        :type FsName: str
        :param _BucketPath: 源桶路径，默认为 /
        :type BucketPath: str
        :param _Direction: 迁移方向；0：对象存储迁移至文件系统，1：文件系统迁移至对象存储。默认为0
        :type Direction: int
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
        self._Direction = None

    @property
    def TaskName(self):
        r"""迁移任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def MigrationType(self):
        r"""迁移方式标志位，默认为0。0：桶迁移；1：清单迁移
        :rtype: int
        """
        return self._MigrationType

    @MigrationType.setter
    def MigrationType(self, MigrationType):
        self._MigrationType = MigrationType

    @property
    def MigrationMode(self):
        r"""迁移模式，默认为0。0: 全量迁移
        :rtype: int
        """
        return self._MigrationMode

    @MigrationMode.setter
    def MigrationMode(self, MigrationMode):
        self._MigrationMode = MigrationMode

    @property
    def SrcSecretId(self):
        r"""数据源账号的 SecretId
        :rtype: str
        """
        return self._SrcSecretId

    @SrcSecretId.setter
    def SrcSecretId(self, SrcSecretId):
        self._SrcSecretId = SrcSecretId

    @property
    def SrcSecretKey(self):
        r"""数据源账号的 SecretKey
        :rtype: str
        """
        return self._SrcSecretKey

    @SrcSecretKey.setter
    def SrcSecretKey(self, SrcSecretKey):
        self._SrcSecretKey = SrcSecretKey

    @property
    def FileSystemId(self):
        r"""文件系统实例 ID，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsPath(self):
        r"""文件系统路径
        :rtype: str
        """
        return self._FsPath

    @FsPath.setter
    def FsPath(self, FsPath):
        self._FsPath = FsPath

    @property
    def CoverType(self):
        r"""同名文件迁移时覆盖策略，默认为0。0: 最后修改时间优先；1: 全覆盖；2: 不覆盖
        :rtype: int
        """
        return self._CoverType

    @CoverType.setter
    def CoverType(self, CoverType):
        self._CoverType = CoverType

    @property
    def SrcService(self):
        r"""数据源服务商。COS：腾讯云COS，OSS：阿里云OSS，OBS：华为云OBS
        :rtype: str
        """
        return self._SrcService

    @SrcService.setter
    def SrcService(self, SrcService):
        self._SrcService = SrcService

    @property
    def BucketName(self):
        r"""数据源桶名称；桶迁移时，BucketName 和 BucketAddress 必填其一，清单迁移时无需填写此参数
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketRegion(self):
        r"""数据源桶地域
        :rtype: str
        """
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def BucketAddress(self):
        r"""数据源桶地址；桶迁移时，BucketName 和 BucketAddress 必填其一，清单迁移时无需填写此参数
        :rtype: str
        """
        return self._BucketAddress

    @BucketAddress.setter
    def BucketAddress(self, BucketAddress):
        self._BucketAddress = BucketAddress

    @property
    def ListAddress(self):
        r"""清单地址，迁移方式为清单迁移时必填
        :rtype: str
        """
        return self._ListAddress

    @ListAddress.setter
    def ListAddress(self, ListAddress):
        self._ListAddress = ListAddress

    @property
    def FsName(self):
        r"""目标文件系统名称
        :rtype: str
        """
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def BucketPath(self):
        r"""源桶路径，默认为 /
        :rtype: str
        """
        return self._BucketPath

    @BucketPath.setter
    def BucketPath(self, BucketPath):
        self._BucketPath = BucketPath

    @property
    def Direction(self):
        r"""迁移方向；0：对象存储迁移至文件系统，1：文件系统迁移至对象存储。默认为0
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


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
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrationTaskResponse(AbstractModel):
    r"""CreateMigrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 迁移任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""迁移任务 ID
        :rtype: str
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


class DataFlowInfo(AbstractModel):
    r"""数据流动信息

    """

    def __init__(self):
        r"""
        :param _DataFlowId: 数据流动管理 ID
        :type DataFlowId: str
        :param _DataFlowName: 数据流动名称
        :type DataFlowName: str
        :param _SourceStorageType: 源端数据类型
        :type SourceStorageType: str
        :param _SourceStorageAddress: 源端存储地址
        :type SourceStorageAddress: str
        :param _SourcePath: 源端路径
        :type SourcePath: str
        :param _TargetPath: 目录路径
        :type TargetPath: str
        :param _Status: available：已生效
pending：配置中
unavailable：失效
deleting：删除中
        :type Status: str
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _AutoRefresh: 0：不开启自动更新

1：开启自动更新
        :type AutoRefresh: int
        :param _UserKafkaTopic: KafkaConsumer 消费时使用的Topic参数
        :type UserKafkaTopic: str
        :param _ServerAddr: 服务地址
        :type ServerAddr: str
        :param _UserName: Kafka消费用户名
        :type UserName: str
        :param _AutoRefreshStatus: 自动刷新的状态，available：已生效
pending：配置中
unavailable：失效
        :type AutoRefreshStatus: str
        :param _AutoRefreshTime: 自动刷新开启时间
        :type AutoRefreshTime: str
        """
        self._DataFlowId = None
        self._DataFlowName = None
        self._SourceStorageType = None
        self._SourceStorageAddress = None
        self._SourcePath = None
        self._TargetPath = None
        self._Status = None
        self._CreationTime = None
        self._FileSystemId = None
        self._AutoRefresh = None
        self._UserKafkaTopic = None
        self._ServerAddr = None
        self._UserName = None
        self._AutoRefreshStatus = None
        self._AutoRefreshTime = None

    @property
    def DataFlowId(self):
        r"""数据流动管理 ID
        :rtype: str
        """
        return self._DataFlowId

    @DataFlowId.setter
    def DataFlowId(self, DataFlowId):
        self._DataFlowId = DataFlowId

    @property
    def DataFlowName(self):
        r"""数据流动名称
        :rtype: str
        """
        return self._DataFlowName

    @DataFlowName.setter
    def DataFlowName(self, DataFlowName):
        self._DataFlowName = DataFlowName

    @property
    def SourceStorageType(self):
        r"""源端数据类型
        :rtype: str
        """
        return self._SourceStorageType

    @SourceStorageType.setter
    def SourceStorageType(self, SourceStorageType):
        self._SourceStorageType = SourceStorageType

    @property
    def SourceStorageAddress(self):
        r"""源端存储地址
        :rtype: str
        """
        return self._SourceStorageAddress

    @SourceStorageAddress.setter
    def SourceStorageAddress(self, SourceStorageAddress):
        self._SourceStorageAddress = SourceStorageAddress

    @property
    def SourcePath(self):
        r"""源端路径
        :rtype: str
        """
        return self._SourcePath

    @SourcePath.setter
    def SourcePath(self, SourcePath):
        self._SourcePath = SourcePath

    @property
    def TargetPath(self):
        r"""目录路径
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath

    @property
    def Status(self):
        r"""available：已生效
pending：配置中
unavailable：失效
deleting：删除中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreationTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def FileSystemId(self):
        r"""文件系统 ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def AutoRefresh(self):
        r"""0：不开启自动更新

1：开启自动更新
        :rtype: int
        """
        return self._AutoRefresh

    @AutoRefresh.setter
    def AutoRefresh(self, AutoRefresh):
        self._AutoRefresh = AutoRefresh

    @property
    def UserKafkaTopic(self):
        r"""KafkaConsumer 消费时使用的Topic参数
        :rtype: str
        """
        return self._UserKafkaTopic

    @UserKafkaTopic.setter
    def UserKafkaTopic(self, UserKafkaTopic):
        self._UserKafkaTopic = UserKafkaTopic

    @property
    def ServerAddr(self):
        r"""服务地址
        :rtype: str
        """
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def UserName(self):
        r"""Kafka消费用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def AutoRefreshStatus(self):
        r"""自动刷新的状态，available：已生效
pending：配置中
unavailable：失效
        :rtype: str
        """
        return self._AutoRefreshStatus

    @AutoRefreshStatus.setter
    def AutoRefreshStatus(self, AutoRefreshStatus):
        self._AutoRefreshStatus = AutoRefreshStatus

    @property
    def AutoRefreshTime(self):
        r"""自动刷新开启时间
        :rtype: str
        """
        return self._AutoRefreshTime

    @AutoRefreshTime.setter
    def AutoRefreshTime(self, AutoRefreshTime):
        self._AutoRefreshTime = AutoRefreshTime


    def _deserialize(self, params):
        self._DataFlowId = params.get("DataFlowId")
        self._DataFlowName = params.get("DataFlowName")
        self._SourceStorageType = params.get("SourceStorageType")
        self._SourceStorageAddress = params.get("SourceStorageAddress")
        self._SourcePath = params.get("SourcePath")
        self._TargetPath = params.get("TargetPath")
        self._Status = params.get("Status")
        self._CreationTime = params.get("CreationTime")
        self._FileSystemId = params.get("FileSystemId")
        self._AutoRefresh = params.get("AutoRefresh")
        self._UserKafkaTopic = params.get("UserKafkaTopic")
        self._ServerAddr = params.get("ServerAddr")
        self._UserName = params.get("UserName")
        self._AutoRefreshStatus = params.get("AutoRefreshStatus")
        self._AutoRefreshTime = params.get("AutoRefreshTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoSnapshotPolicyRequest(AbstractModel):
    r"""DeleteAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 快照策略ID，查询快照策略接口获取,[DescribeAutoSnapshotPolicies](https://cloud.tencent.com/document/api/582/80208)
        :type AutoSnapshotPolicyId: str
        """
        self._AutoSnapshotPolicyId = None

    @property
    def AutoSnapshotPolicyId(self):
        r"""快照策略ID，查询快照策略接口获取,[DescribeAutoSnapshotPolicies](https://cloud.tencent.com/document/api/582/80208)
        :rtype: str
        """
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
    r"""DeleteAutoSnapshotPolicy返回参数结构体

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
        r"""快照策略ID
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

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
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class DeleteCfsFileSystemRequest(AbstractModel):
    r"""DeleteCfsFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID，通过[查询文件系统接口](https://cloud.tencent.com/document/api/582/38170)获取。说明，进行删除文件系统操作前需要先调用 DeleteMountTarget 接口删除该文件系统的挂载点，否则会删除失败。
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        r"""文件系统 ID，通过[查询文件系统接口](https://cloud.tencent.com/document/api/582/38170)获取。说明，进行删除文件系统操作前需要先调用 DeleteMountTarget 接口删除该文件系统的挂载点，否则会删除失败。
        :rtype: str
        """
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
    r"""DeleteCfsFileSystem返回参数结构体

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


class DeleteCfsPGroupRequest(AbstractModel):
    r"""DeleteCfsPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :type PGroupId: str
        """
        self._PGroupId = None

    @property
    def PGroupId(self):
        r"""权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :rtype: str
        """
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
    r"""DeleteCfsPGroup返回参数结构体

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
        r"""权限组 ID
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def AppId(self):
        r"""用户 ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
        self._PGroupId = params.get("PGroupId")
        self._AppId = params.get("AppId")
        self._RequestId = params.get("RequestId")


class DeleteCfsRuleRequest(AbstractModel):
    r"""DeleteCfsRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :type PGroupId: str
        :param _RuleId: 规则 ID，可通过[DescribeCfsRules](https://cloud.tencent.com/document/api/582/38156)接口获取
        :type RuleId: str
        """
        self._PGroupId = None
        self._RuleId = None

    @property
    def PGroupId(self):
        r"""权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def RuleId(self):
        r"""规则 ID，可通过[DescribeCfsRules](https://cloud.tencent.com/document/api/582/38156)接口获取
        :rtype: str
        """
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
    r"""DeleteCfsRule返回参数结构体

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
        r"""规则 ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def PGroupId(self):
        r"""权限组 ID
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

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
        self._RuleId = params.get("RuleId")
        self._PGroupId = params.get("PGroupId")
        self._RequestId = params.get("RequestId")


class DeleteCfsSnapshotRequest(AbstractModel):
    r"""DeleteCfsSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照ID，可以通过[DescribeCfsSnapshots](https://cloud.tencent.com/document/api/582/80206) 查询获取
        :type SnapshotId: str
        :param _SnapshotIds: 需要删除的文件系统快照ID 列表，快照ID，跟ID列表至少填一项
快照ID，可以通过[DescribeCfsSnapshots](https://cloud.tencent.com/document/api/582/80206) 查询获取
        :type SnapshotIds: list of str
        """
        self._SnapshotId = None
        self._SnapshotIds = None

    @property
    def SnapshotId(self):
        r"""快照ID，可以通过[DescribeCfsSnapshots](https://cloud.tencent.com/document/api/582/80206) 查询获取
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotIds(self):
        r"""需要删除的文件系统快照ID 列表，快照ID，跟ID列表至少填一项
快照ID，可以通过[DescribeCfsSnapshots](https://cloud.tencent.com/document/api/582/80206) 查询获取
        :rtype: list of str
        """
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
    r"""DeleteCfsSnapshot返回参数结构体

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
        r"""文件系统ID
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

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
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class DeleteDataFlowRequest(AbstractModel):
    r"""DeleteDataFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataFlowId: 数据流动管理 ID
        :type DataFlowId: str
        :param _FileSystemId: 文件系统 ID ，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :type FileSystemId: str
        """
        self._DataFlowId = None
        self._FileSystemId = None

    @property
    def DataFlowId(self):
        r"""数据流动管理 ID
        :rtype: str
        """
        return self._DataFlowId

    @DataFlowId.setter
    def DataFlowId(self, DataFlowId):
        self._DataFlowId = DataFlowId

    @property
    def FileSystemId(self):
        r"""文件系统 ID ，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._DataFlowId = params.get("DataFlowId")
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDataFlowResponse(AbstractModel):
    r"""DeleteDataFlow返回参数结构体

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


class DeleteLifecyclePolicyRequest(AbstractModel):
    r"""DeleteLifecyclePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecyclePolicyID: 生命周期管理策略ID
        :type LifecyclePolicyID: str
        """
        self._LifecyclePolicyID = None

    @property
    def LifecyclePolicyID(self):
        r"""生命周期管理策略ID
        :rtype: str
        """
        return self._LifecyclePolicyID

    @LifecyclePolicyID.setter
    def LifecyclePolicyID(self, LifecyclePolicyID):
        self._LifecyclePolicyID = LifecyclePolicyID


    def _deserialize(self, params):
        self._LifecyclePolicyID = params.get("LifecyclePolicyID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLifecyclePolicyResponse(AbstractModel):
    r"""DeleteLifecyclePolicy返回参数结构体

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


class DeleteMigrationTaskRequest(AbstractModel):
    r"""DeleteMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 迁移任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""迁移任务ID
        :rtype: str
        """
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
    r"""DeleteMigrationTask返回参数结构体

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


class DeleteUserQuotaRequest(AbstractModel):
    r"""DeleteUserQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID，通过查询文件系统列表获取；[DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170)
        :type FileSystemId: str
        :param _UserType: 指定配额类型，包括Uid（按用户ID限制）、Gid（按用户组ID限制）、Dir（按目录限制）
        :type UserType: str
        :param _UserId: UID/GID信息，和DirectoryPath参数，两者必须填写一个
        :type UserId: str
        :param _DirectoryPath: 设置目录配额的目录的绝对路径，和UserId参数，两者必须填写一个
        :type DirectoryPath: str
        """
        self._FileSystemId = None
        self._UserType = None
        self._UserId = None
        self._DirectoryPath = None

    @property
    def FileSystemId(self):
        r"""文件系统ID，通过查询文件系统列表获取；[DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170)
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def UserType(self):
        r"""指定配额类型，包括Uid（按用户ID限制）、Gid（按用户组ID限制）、Dir（按目录限制）
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserId(self):
        r"""UID/GID信息，和DirectoryPath参数，两者必须填写一个
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def DirectoryPath(self):
        r"""设置目录配额的目录的绝对路径，和UserId参数，两者必须填写一个
        :rtype: str
        """
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
    r"""DeleteUserQuota返回参数结构体

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


class DescribeAutoSnapshotPoliciesRequest(AbstractModel):
    r"""DescribeAutoSnapshotPolicies请求参数结构体

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
        r"""快照策略ID
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def Offset(self):
        r"""分页码
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""页面长
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Order(self):
        r"""升序，降序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""排序字段
        :rtype: str
        """
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
    r"""DescribeAutoSnapshotPolicies返回参数结构体

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
        r"""快照策略总个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoSnapshotPolicies(self):
        r"""快照策略信息
        :rtype: list of AutoSnapshotPolicyInfo
        """
        return self._AutoSnapshotPolicies

    @AutoSnapshotPolicies.setter
    def AutoSnapshotPolicies(self, AutoSnapshotPolicies):
        self._AutoSnapshotPolicies = AutoSnapshotPolicies

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
        self._TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicies") is not None:
            self._AutoSnapshotPolicies = []
            for item in params.get("AutoSnapshotPolicies"):
                obj = AutoSnapshotPolicyInfo()
                obj._deserialize(item)
                self._AutoSnapshotPolicies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAvailableZoneInfoRequest(AbstractModel):
    r"""DescribeAvailableZoneInfo请求参数结构体

    """


class DescribeAvailableZoneInfoResponse(AbstractModel):
    r"""DescribeAvailableZoneInfo返回参数结构体

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
        r"""各可用区的资源售卖情况以及支持的存储类型、存储协议等信息
        :rtype: list of AvailableRegion
        """
        return self._RegionZones

    @RegionZones.setter
    def RegionZones(self, RegionZones):
        self._RegionZones = RegionZones

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
        if params.get("RegionZones") is not None:
            self._RegionZones = []
            for item in params.get("RegionZones"):
                obj = AvailableRegion()
                obj._deserialize(item)
                self._RegionZones.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBucketListRequest(AbstractModel):
    r"""DescribeBucketList请求参数结构体

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
        r"""数据源服务商。COS: 腾讯云COS，OSS: 阿里云OSS，OBS:华为云OBS
        :rtype: str
        """
        return self._SrcService

    @SrcService.setter
    def SrcService(self, SrcService):
        self._SrcService = SrcService

    @property
    def SrcSecretId(self):
        r"""数据源账号的SecretId
        :rtype: str
        """
        return self._SrcSecretId

    @SrcSecretId.setter
    def SrcSecretId(self, SrcSecretId):
        self._SrcSecretId = SrcSecretId

    @property
    def SrcSecretKey(self):
        r"""数据源账号的SecretKey
        :rtype: str
        """
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
    r"""DescribeBucketList返回参数结构体

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
        r"""桶的数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BucketList(self):
        r"""桶列表
        :rtype: list of BucketInfo
        """
        return self._BucketList

    @BucketList.setter
    def BucketList(self, BucketList):
        self._BucketList = BucketList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("BucketList") is not None:
            self._BucketList = []
            for item in params.get("BucketList"):
                obj = BucketInfo()
                obj._deserialize(item)
                self._BucketList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsFileSystemClientsRequest(AbstractModel):
    r"""DescribeCfsFileSystemClients请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID，通过[查询文件系统接口](https://cloud.tencent.com/document/api/582/38170)获取
        :type FileSystemId: str
        :param _Offset: Offset 分页码，默认为0
        :type Offset: int
        :param _Limit: Limit 页面大小，默认为10，最大值为100
        :type Limit: int
        """
        self._FileSystemId = None
        self._Offset = None
        self._Limit = None

    @property
    def FileSystemId(self):
        r"""文件系统 ID，通过[查询文件系统接口](https://cloud.tencent.com/document/api/582/38170)获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Offset(self):
        r"""Offset 分页码，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Limit 页面大小，默认为10，最大值为100
        :rtype: int
        """
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
    r"""DescribeCfsFileSystemClients返回参数结构体

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
        r"""客户端列表
        :rtype: list of FileSystemClient
        """
        return self._ClientList

    @ClientList.setter
    def ClientList(self, ClientList):
        self._ClientList = ClientList

    @property
    def TotalCount(self):
        r"""文件系统总数
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
        if params.get("ClientList") is not None:
            self._ClientList = []
            for item in params.get("ClientList"):
                obj = FileSystemClient()
                obj._deserialize(item)
                self._ClientList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCfsFileSystemsRequest(AbstractModel):
    r"""DescribeCfsFileSystems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _VpcId: 私有网络（VPC） ID
        :type VpcId: str
        :param _SubnetId: 子网 ID
        :type SubnetId: str
        :param _Offset: Offset 分页码,默认0
        :type Offset: int
        :param _Limit: Limit 页面大小，默认10
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
        r"""文件系统 ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def VpcId(self):
        r"""私有网络（VPC） ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网 ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Offset(self):
        r"""Offset 分页码,默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Limit 页面大小，默认10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CreationToken(self):
        r"""用户自定义名称
        :rtype: str
        """
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
    r"""DescribeCfsFileSystems返回参数结构体

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
        r"""文件系统信息
        :rtype: list of FileSystemInfo
        """
        return self._FileSystems

    @FileSystems.setter
    def FileSystems(self, FileSystems):
        self._FileSystems = FileSystems

    @property
    def TotalCount(self):
        r"""文件系统总数
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
        if params.get("FileSystems") is not None:
            self._FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystemInfo()
                obj._deserialize(item)
                self._FileSystems.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCfsPGroupsRequest(AbstractModel):
    r"""DescribeCfsPGroups请求参数结构体

    """


class DescribeCfsPGroupsResponse(AbstractModel):
    r"""DescribeCfsPGroups返回参数结构体

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
        r"""权限组信息列表
        :rtype: list of PGroupInfo
        """
        return self._PGroupList

    @PGroupList.setter
    def PGroupList(self, PGroupList):
        self._PGroupList = PGroupList

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
        if params.get("PGroupList") is not None:
            self._PGroupList = []
            for item in params.get("PGroupList"):
                obj = PGroupInfo()
                obj._deserialize(item)
                self._PGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsRulesRequest(AbstractModel):
    r"""DescribeCfsRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :type PGroupId: str
        """
        self._PGroupId = None

    @property
    def PGroupId(self):
        r"""权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :rtype: str
        """
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
    r"""DescribeCfsRules返回参数结构体

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
        r"""权限组规则列表
        :rtype: list of PGroupRuleInfo
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

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
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = PGroupRuleInfo()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsServiceStatusRequest(AbstractModel):
    r"""DescribeCfsServiceStatus请求参数结构体

    """


class DescribeCfsServiceStatusResponse(AbstractModel):
    r"""DescribeCfsServiceStatus返回参数结构体

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
        r"""该用户当前 CFS 服务的状态，none 为未开通，creating 为开通中，created 为已开通
        :rtype: str
        """
        return self._CfsServiceStatus

    @CfsServiceStatus.setter
    def CfsServiceStatus(self, CfsServiceStatus):
        self._CfsServiceStatus = CfsServiceStatus

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
        self._CfsServiceStatus = params.get("CfsServiceStatus")
        self._RequestId = params.get("RequestId")


class DescribeCfsSnapshotOverviewRequest(AbstractModel):
    r"""DescribeCfsSnapshotOverview请求参数结构体

    """


class DescribeCfsSnapshotOverviewResponse(AbstractModel):
    r"""DescribeCfsSnapshotOverview返回参数结构体

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
        r"""统计信息
        :rtype: list of SnapshotStatistics
        """
        return self._StatisticsList

    @StatisticsList.setter
    def StatisticsList(self, StatisticsList):
        self._StatisticsList = StatisticsList

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
        if params.get("StatisticsList") is not None:
            self._StatisticsList = []
            for item in params.get("StatisticsList"):
                obj = SnapshotStatistics()
                obj._deserialize(item)
                self._StatisticsList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsSnapshotsRequest(AbstractModel):
    r"""DescribeCfsSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :type FileSystemId: str
        :param _SnapshotId: 快照 ID
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
<br>Status - Array of String - 是否必填：否 -（过滤条件）按照快照状态过滤。状态分类：creating：创建中 | available：运行中 | deleting：删除中 | rollbacking_new：由快照创建新文件系统中 | create-failed：创建失败。
<br>tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键进行过滤。
<br>tag:tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key 使用具体的标签键进行替换。
        :type Filters: list of Filter
        :param _OrderField: 按创建时间排序取值
        :type OrderField: str
        :param _Order: 排序；升序或者降序
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
        r"""文件系统 ID，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SnapshotId(self):
        r"""快照 ID
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Offset(self):
        r"""分页起始位置，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""页面长度，默认为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤条件。
<br>SnapshotId - Array of String - 是否必填：否 -（过滤条件）按快照ID过滤。
<br>SnapshotName - Array of String - 是否必填：否 -（过滤条件）按照快照名称过滤。
<br>FileSystemId - Array of String - 是否必填：否 -（过滤条件）按文件系统ID过滤。
<br>FsName - Array of String - 是否必填：否 -（过滤条件）按文件系统名过滤。
<br>Status - Array of String - 是否必填：否 -（过滤条件）按照快照状态过滤。状态分类：creating：创建中 | available：运行中 | deleting：删除中 | rollbacking_new：由快照创建新文件系统中 | create-failed：创建失败。
<br>tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键进行过滤。
<br>tag:tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key 使用具体的标签键进行替换。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderField(self):
        r"""按创建时间排序取值
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        r"""排序；升序或者降序
        :rtype: str
        """
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
    r"""DescribeCfsSnapshots返回参数结构体

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
        r"""总个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Snapshots(self):
        r"""快照信息描述
        :rtype: list of SnapshotInfo
        """
        return self._Snapshots

    @Snapshots.setter
    def Snapshots(self, Snapshots):
        self._Snapshots = Snapshots

    @property
    def TotalSize(self):
        r"""快照列表快照汇总
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Snapshots") is not None:
            self._Snapshots = []
            for item in params.get("Snapshots"):
                obj = SnapshotInfo()
                obj._deserialize(item)
                self._Snapshots.append(obj)
        self._TotalSize = params.get("TotalSize")
        self._RequestId = params.get("RequestId")


class DescribeDataFlowRequest(AbstractModel):
    r"""DescribeDataFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID ，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :type FileSystemId: str
        :param _DataFlowId: 数据流动 ID ，由创建数据流动返回
        :type DataFlowId: str
        :param _Limit: 每次查询返回值个数，默认20；最大100
        :type Limit: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _CfsVersion: 文件系统版本；版本号：v1.5，v3.0，v3.1，v4.0
        :type CfsVersion: str
        """
        self._FileSystemId = None
        self._DataFlowId = None
        self._Limit = None
        self._Offset = None
        self._CfsVersion = None

    @property
    def FileSystemId(self):
        r"""文件系统 ID ，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def DataFlowId(self):
        r"""数据流动 ID ，由创建数据流动返回
        :rtype: str
        """
        return self._DataFlowId

    @DataFlowId.setter
    def DataFlowId(self, DataFlowId):
        self._DataFlowId = DataFlowId

    @property
    def Limit(self):
        r"""每次查询返回值个数，默认20；最大100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CfsVersion(self):
        r"""文件系统版本；版本号：v1.5，v3.0，v3.1，v4.0
        :rtype: str
        """
        return self._CfsVersion

    @CfsVersion.setter
    def CfsVersion(self, CfsVersion):
        self._CfsVersion = CfsVersion


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._DataFlowId = params.get("DataFlowId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._CfsVersion = params.get("CfsVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFlowResponse(AbstractModel):
    r"""DescribeDataFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数量
        :type TotalCount: int
        :param _DataFlows: 无
        :type DataFlows: list of DataFlowInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DataFlows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataFlows(self):
        r"""无
        :rtype: list of DataFlowInfo
        """
        return self._DataFlows

    @DataFlows.setter
    def DataFlows(self, DataFlows):
        self._DataFlows = DataFlows

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
        self._TotalCount = params.get("TotalCount")
        if params.get("DataFlows") is not None:
            self._DataFlows = []
            for item in params.get("DataFlows"):
                obj = DataFlowInfo()
                obj._deserialize(item)
                self._DataFlows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLifecycleDataTaskRequest(AbstractModel):
    r"""DescribeLifecycleDataTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。须早于 EndTime ，仅支持查询最近3个月内的任务数据。
        :type StartTime: str
        :param _EndTime: 结束时间。须晚于 StartTime ，仅支持查询最近3个月内的任务数据。
        :type EndTime: str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Offset: Offset 分页码	
        :type Offset: int
        :param _Limit: Limit 页面大小	
        :type Limit: int
        :param _Filters: 过滤条件，TaskName，FileSystemId，Type
        :type Filters: list of Filter
        :param _CfsVersion: 文件系统版本；v3.1: pcfs/hifs v4.0:Turbo
        :type CfsVersion: str
        """
        self._StartTime = None
        self._EndTime = None
        self._TaskId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._CfsVersion = None

    @property
    def StartTime(self):
        r"""开始时间。须早于 EndTime ，仅支持查询最近3个月内的任务数据。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间。须晚于 StartTime ，仅支持查询最近3个月内的任务数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Offset(self):
        r"""Offset 分页码	
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Limit 页面大小	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤条件，TaskName，FileSystemId，Type
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def CfsVersion(self):
        r"""文件系统版本；v3.1: pcfs/hifs v4.0:Turbo
        :rtype: str
        """
        return self._CfsVersion

    @CfsVersion.setter
    def CfsVersion(self, CfsVersion):
        self._CfsVersion = CfsVersion


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskId = params.get("TaskId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._CfsVersion = params.get("CfsVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLifecycleDataTaskResponse(AbstractModel):
    r"""DescribeLifecycleDataTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecycleDataTask: 任务数组
        :type LifecycleDataTask: list of LifecycleDataTaskInfo
        :param _TotalCount: 查询结果总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LifecycleDataTask = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LifecycleDataTask(self):
        r"""任务数组
        :rtype: list of LifecycleDataTaskInfo
        """
        return self._LifecycleDataTask

    @LifecycleDataTask.setter
    def LifecycleDataTask(self, LifecycleDataTask):
        self._LifecycleDataTask = LifecycleDataTask

    @property
    def TotalCount(self):
        r"""查询结果总数
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
        if params.get("LifecycleDataTask") is not None:
            self._LifecycleDataTask = []
            for item in params.get("LifecycleDataTask"):
                obj = LifecycleDataTaskInfo()
                obj._deserialize(item)
                self._LifecycleDataTask.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLifecyclePoliciesRequest(AbstractModel):
    r"""DescribeLifecyclePolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecyclePolicyName: 生命周期管理策略名称
        :type LifecyclePolicyName: str
        :param _PageSize: 每个分页包含的生命周期管理策略个数
        :type PageSize: int
        :param _PageNumber: 列表的分页页码
        :type PageNumber: int
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _LifecyclePolicyID: 生命周期管理策略ID
        :type LifecyclePolicyID: str
        """
        self._LifecyclePolicyName = None
        self._PageSize = None
        self._PageNumber = None
        self._FileSystemId = None
        self._LifecyclePolicyID = None

    @property
    def LifecyclePolicyName(self):
        r"""生命周期管理策略名称
        :rtype: str
        """
        return self._LifecyclePolicyName

    @LifecyclePolicyName.setter
    def LifecyclePolicyName(self, LifecyclePolicyName):
        self._LifecyclePolicyName = LifecyclePolicyName

    @property
    def PageSize(self):
        r"""每个分页包含的生命周期管理策略个数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""列表的分页页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def LifecyclePolicyID(self):
        r"""生命周期管理策略ID
        :rtype: str
        """
        return self._LifecyclePolicyID

    @LifecyclePolicyID.setter
    def LifecyclePolicyID(self, LifecyclePolicyID):
        self._LifecyclePolicyID = LifecyclePolicyID


    def _deserialize(self, params):
        self._LifecyclePolicyName = params.get("LifecyclePolicyName")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._FileSystemId = params.get("FileSystemId")
        self._LifecyclePolicyID = params.get("LifecyclePolicyID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLifecyclePoliciesResponse(AbstractModel):
    r"""DescribeLifecyclePolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 列表的分页页码
        :type PageNumber: int
        :param _PageSize: 每个分页包含的生命周期管理策略个数
        :type PageSize: int
        :param _TotalCount: 生命周期管理策略总数
        :type TotalCount: int
        :param _LifecyclePolicies: 生命周期管理策略列表
        :type LifecyclePolicies: list of LifecyclePolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._LifecyclePolicies = None
        self._RequestId = None

    @property
    def PageNumber(self):
        r"""列表的分页页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每个分页包含的生命周期管理策略个数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""生命周期管理策略总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LifecyclePolicies(self):
        r"""生命周期管理策略列表
        :rtype: list of LifecyclePolicy
        """
        return self._LifecyclePolicies

    @LifecyclePolicies.setter
    def LifecyclePolicies(self, LifecyclePolicies):
        self._LifecyclePolicies = LifecyclePolicies

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
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        if params.get("LifecyclePolicies") is not None:
            self._LifecyclePolicies = []
            for item in params.get("LifecyclePolicies"):
                obj = LifecyclePolicy()
                obj._deserialize(item)
                self._LifecyclePolicies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigrationTasksRequest(AbstractModel):
    r"""DescribeMigrationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        :param _Filters: <br><li> taskId按照【迁移任务id】进行过滤。类型：String必选：否<br></li><br><li>  taskName按照【迁移任务名字】进行模糊搜索过滤。类型：String必选：否每次请求的Filters的上限为10，Filter.Values的上限为100。</li>
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页单页限制数目，默认值为20，最大值100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<br><li> taskId按照【迁移任务id】进行过滤。类型：String必选：否<br></li><br><li>  taskName按照【迁移任务名字】进行模糊搜索过滤。类型：String必选：否每次请求的Filters的上限为10，Filter.Values的上限为100。</li>
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
        


class DescribeMigrationTasksResponse(AbstractModel):
    r"""DescribeMigrationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 迁移任务的总数量
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
        r"""迁移任务的总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MigrationTasks(self):
        r"""迁移任务详情
        :rtype: list of MigrationTaskInfo
        """
        return self._MigrationTasks

    @MigrationTasks.setter
    def MigrationTasks(self, MigrationTasks):
        self._MigrationTasks = MigrationTasks

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
        self._TotalCount = params.get("TotalCount")
        if params.get("MigrationTasks") is not None:
            self._MigrationTasks = []
            for item in params.get("MigrationTasks"):
                obj = MigrationTaskInfo()
                obj._deserialize(item)
                self._MigrationTasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMountTargetsRequest(AbstractModel):
    r"""DescribeMountTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID，[查询文件系统列表](https://cloud.tencent.com/document/api/582/38170)可以获得id
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        r"""文件系统 ID，[查询文件系统列表](https://cloud.tencent.com/document/api/582/38170)可以获得id
        :rtype: str
        """
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
    r"""DescribeMountTargets返回参数结构体

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
        r"""挂载点详情
        :rtype: list of MountInfo
        """
        return self._MountTargets

    @MountTargets.setter
    def MountTargets(self, MountTargets):
        self._MountTargets = MountTargets

    @property
    def NumberOfMountTargets(self):
        r"""挂载点数量
        :rtype: int
        """
        return self._NumberOfMountTargets

    @NumberOfMountTargets.setter
    def NumberOfMountTargets(self, NumberOfMountTargets):
        self._NumberOfMountTargets = NumberOfMountTargets

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
        if params.get("MountTargets") is not None:
            self._MountTargets = []
            for item in params.get("MountTargets"):
                obj = MountInfo()
                obj._deserialize(item)
                self._MountTargets.append(obj)
        self._NumberOfMountTargets = params.get("NumberOfMountTargets")
        self._RequestId = params.get("RequestId")


class DescribeSnapshotOperationLogsRequest(AbstractModel):
    r"""DescribeSnapshotOperationLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照ID，可以通过[DescribeCfsSnapshots](https://cloud.tencent.com/document/api/582/80206) 查询获取
        :type SnapshotId: str
        :param _StartTime: 起始时间，格式“YYYY-MM-DD hh:mm:ss”
        :type StartTime: str
        :param _EndTime: 结束时间，格式“YYYY-MM-DD hh:mm:ss”
        :type EndTime: str
        """
        self._SnapshotId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SnapshotId(self):
        r"""快照ID，可以通过[DescribeCfsSnapshots](https://cloud.tencent.com/document/api/582/80206) 查询获取
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def StartTime(self):
        r"""起始时间，格式“YYYY-MM-DD hh:mm:ss”
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间，格式“YYYY-MM-DD hh:mm:ss”
        :rtype: str
        """
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
    r"""DescribeSnapshotOperationLogs返回参数结构体

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
        r"""快照ID
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotOperates(self):
        r"""操作日志
        :rtype: list of SnapshotOperateLog
        """
        return self._SnapshotOperates

    @SnapshotOperates.setter
    def SnapshotOperates(self, SnapshotOperates):
        self._SnapshotOperates = SnapshotOperates

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
        self._SnapshotId = params.get("SnapshotId")
        if params.get("SnapshotOperates") is not None:
            self._SnapshotOperates = []
            for item in params.get("SnapshotOperates"):
                obj = SnapshotOperateLog()
                obj._deserialize(item)
                self._SnapshotOperates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserQuotaRequest(AbstractModel):
    r"""DescribeUserQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID,通过[查询文件系统列表](https://cloud.tencent.com/document/api/582/38170)获取
        :type FileSystemId: str
        :param _Filters: 过滤条件。
UserType - Array of String - 是否必填：否 -（过滤条件）按配额类型过滤。(Uid|Gid|Dir，分别对应用户，用户组，目录 )
UserId- Array of String - 是否必填：否 -（过滤条件）按用户id过滤。
        :type Filters: list of Filter
        :param _Offset: Offset 分页码，默认值0
        :type Offset: int
        :param _Limit: Limit 页面大小，可填范围为大于0的整数，默认值是10
        :type Limit: int
        """
        self._FileSystemId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def FileSystemId(self):
        r"""文件系统 ID,通过[查询文件系统列表](https://cloud.tencent.com/document/api/582/38170)获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Filters(self):
        r"""过滤条件。
UserType - Array of String - 是否必填：否 -（过滤条件）按配额类型过滤。(Uid|Gid|Dir，分别对应用户，用户组，目录 )
UserId- Array of String - 是否必填：否 -（过滤条件）按用户id过滤。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""Offset 分页码，默认值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Limit 页面大小，可填范围为大于0的整数，默认值是10
        :rtype: int
        """
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
    r"""DescribeUserQuota返回参数结构体

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
        r"""UserQuota条目总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UserQuotaInfo(self):
        r"""UserQuota条目
        :rtype: list of UserQuota
        """
        return self._UserQuotaInfo

    @UserQuotaInfo.setter
    def UserQuotaInfo(self, UserQuotaInfo):
        self._UserQuotaInfo = UserQuotaInfo

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
        self._TotalCount = params.get("TotalCount")
        if params.get("UserQuotaInfo") is not None:
            self._UserQuotaInfo = []
            for item in params.get("UserQuotaInfo"):
                obj = UserQuota()
                obj._deserialize(item)
                self._UserQuotaInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DoDirectoryOperationRequest(AbstractModel):
    r"""DoDirectoryOperation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统Id
        :type FileSystemId: str
        :param _OpetationType: create：创建目录，等同于mkdir。
check：确认目录是否存在，等同于stat。
move：对文件/目录进行重命名，等同于mv。
        :type OpetationType: str
        :param _DirectoryPath: 目录的绝对路径  默认递归创建（即如果目录中有子目录不存在，则先创建出对应子目录）
        :type DirectoryPath: str
        :param _Mode: 创建目录的权限，若不传，默认为0755  若Operation Type为check，此值无实际意义
        :type Mode: str
        :param _DestPath: mv操作的目标目录名称；如果是turbo文件系统必须以/cfs/开头
        :type DestPath: str
        """
        self._FileSystemId = None
        self._OpetationType = None
        self._DirectoryPath = None
        self._Mode = None
        self._DestPath = None

    @property
    def FileSystemId(self):
        r"""文件系统Id
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def OpetationType(self):
        r"""create：创建目录，等同于mkdir。
check：确认目录是否存在，等同于stat。
move：对文件/目录进行重命名，等同于mv。
        :rtype: str
        """
        return self._OpetationType

    @OpetationType.setter
    def OpetationType(self, OpetationType):
        self._OpetationType = OpetationType

    @property
    def DirectoryPath(self):
        r"""目录的绝对路径  默认递归创建（即如果目录中有子目录不存在，则先创建出对应子目录）
        :rtype: str
        """
        return self._DirectoryPath

    @DirectoryPath.setter
    def DirectoryPath(self, DirectoryPath):
        self._DirectoryPath = DirectoryPath

    @property
    def Mode(self):
        r"""创建目录的权限，若不传，默认为0755  若Operation Type为check，此值无实际意义
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def DestPath(self):
        r"""mv操作的目标目录名称；如果是turbo文件系统必须以/cfs/开头
        :rtype: str
        """
        return self._DestPath

    @DestPath.setter
    def DestPath(self, DestPath):
        self._DestPath = DestPath


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._OpetationType = params.get("OpetationType")
        self._DirectoryPath = params.get("DirectoryPath")
        self._Mode = params.get("Mode")
        self._DestPath = params.get("DestPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DoDirectoryOperationResponse(AbstractModel):
    r"""DoDirectoryOperation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 1:成功  0:失败  创建目录的操作，1表示创建成功，0表示创建失败。  确认目录是否存在的操作，1表示目录存在，0表示目录不存在。  说明：创建目录操作若目录已存在，也会返回创建成功。
        :type Result: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""1:成功  0:失败  创建目录的操作，1表示创建成功，0表示创建失败。  确认目录是否存在的操作，1表示目录存在，0表示目录不存在。  说明：创建目录操作若目录已存在，也会返回创建成功。
        :rtype: int
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


class ExstraPerformanceInfo(AbstractModel):
    r"""购买完额外性能之后的值

    """

    def __init__(self):
        r"""
        :param _Type: fixed: 最终值固定
        :type Type: str
        :param _Performance: 额外购买的CFS性能值，单位MB/s。
        :type Performance: int
        """
        self._Type = None
        self._Performance = None

    @property
    def Type(self):
        r"""fixed: 最终值固定
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Performance(self):
        r"""额外购买的CFS性能值，单位MB/s。
        :rtype: int
        """
        return self._Performance

    @Performance.setter
    def Performance(self, Performance):
        self._Performance = Performance


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Performance = params.get("Performance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSystemByPolicy(AbstractModel):
    r"""绑定快照策略的文件系统信息

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
        r"""文件系统名称
        :rtype: str
        """
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SizeByte(self):
        r"""文件系统大小，单位Byte
        :rtype: int
        """
        return self._SizeByte

    @SizeByte.setter
    def SizeByte(self, SizeByte):
        self._SizeByte = SizeByte

    @property
    def StorageType(self):
        r"""存储类型，HP：通用性能型；SD：通用标准型；TP:turbo性能型；TB：turbo标准型；THP：吞吐型
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def TotalSnapshotSize(self):
        r"""快照总大小，单位GiB
        :rtype: int
        """
        return self._TotalSnapshotSize

    @TotalSnapshotSize.setter
    def TotalSnapshotSize(self, TotalSnapshotSize):
        self._TotalSnapshotSize = TotalSnapshotSize

    @property
    def CreationTime(self):
        r"""文件系统创建时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def ZoneId(self):
        r"""文件系统所在区ID
        :rtype: int
        """
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
    r"""文件系统客户端信息

    """

    def __init__(self):
        r"""
        :param _CfsVip: 文件系统IP地址
        :type CfsVip: str
        :param _ClientIp: 客户端IP地址
        :type ClientIp: str
        :param _VpcId: 文件系统所属VPCID
        :type VpcId: str
        :param _Zone: 可用区名称，例如ap-beijing-1，参考[简介](https://cloud.tencent.com/document/api/582/38144)文档中的地域与可用区列表
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
        r"""文件系统IP地址
        :rtype: str
        """
        return self._CfsVip

    @CfsVip.setter
    def CfsVip(self, CfsVip):
        self._CfsVip = CfsVip

    @property
    def ClientIp(self):
        r"""客户端IP地址
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def VpcId(self):
        r"""文件系统所属VPCID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Zone(self):
        r"""可用区名称，例如ap-beijing-1，参考[简介](https://cloud.tencent.com/document/api/582/38144)文档中的地域与可用区列表
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        r"""可用区中文名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def MountDirectory(self):
        r"""该文件系统被挂载到客户端上的路径信息
        :rtype: str
        """
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
    r"""文件系统基本信息

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
        :param _AutoSnapshotPolicyId: 文件系统关联的快照策略
        :type AutoSnapshotPolicyId: str
        :param _SnapStatus: 文件系统处理快照状态,snapping：快照中，normal：正常状态
        :type SnapStatus: str
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
        :type TieringDetail: :class:`tencentcloud.cfs.v20190719.models.TieringDetailInfo`
        :param _AutoScaleUpRule: 文件系统自动扩容策略
        :type AutoScaleUpRule: :class:`tencentcloud.cfs.v20190719.models.AutoScaleUpRule`
        :param _Version: 文件系统版本
        :type Version: str
        :param _ExstraPerformanceInfo: 额外性能信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExstraPerformanceInfo: list of ExstraPerformanceInfo
        :param _MetaType: basic：标准版元数据类型
enhanced：增项版元数据类型
        :type MetaType: str
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
        self._AutoSnapshotPolicyId = None
        self._SnapStatus = None
        self._Capacity = None
        self._Tags = None
        self._TieringState = None
        self._TieringDetail = None
        self._AutoScaleUpRule = None
        self._Version = None
        self._ExstraPerformanceInfo = None
        self._MetaType = None

    @property
    def CreationTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def CreationToken(self):
        r"""用户自定义名称
        :rtype: str
        """
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        r"""文件系统 ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def LifeCycleState(self):
        r"""文件系统状态。取值范围：
- creating:创建中
- mounting:挂载中
- create_failed:创建失败
- available:可使用
- unserviced:停服中
- upgrading:升级中
        :rtype: str
        """
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def SizeByte(self):
        r"""文件系统已使用容量。单位：Byte
        :rtype: int
        """
        return self._SizeByte

    @SizeByte.setter
    def SizeByte(self, SizeByte):
        self._SizeByte = SizeByte

    @property
    def SizeLimit(self):
        r"""文件系统空间限制。单位:GiB
        :rtype: int
        """
        return self._SizeLimit

    @SizeLimit.setter
    def SizeLimit(self, SizeLimit):
        self._SizeLimit = SizeLimit

    @property
    def ZoneId(self):
        r"""区域 ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        r"""区域名称
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Protocol(self):
        r"""文件系统协议类型, 支持 NFS,CIFS,TURBO
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def StorageType(self):
        r"""存储类型，HP：通用性能型；SD：通用标准型；TP:turbo性能型；TB：turbo标准型；THP：吞吐型
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def StorageResourcePkg(self):
        r"""文件系统绑定的预付费存储包
        :rtype: str
        """
        return self._StorageResourcePkg

    @StorageResourcePkg.setter
    def StorageResourcePkg(self, StorageResourcePkg):
        self._StorageResourcePkg = StorageResourcePkg

    @property
    def BandwidthResourcePkg(self):
        r"""文件系统绑定的预付费带宽包（暂未支持）
        :rtype: str
        """
        return self._BandwidthResourcePkg

    @BandwidthResourcePkg.setter
    def BandwidthResourcePkg(self, BandwidthResourcePkg):
        self._BandwidthResourcePkg = BandwidthResourcePkg

    @property
    def PGroup(self):
        r"""文件系统绑定权限组信息
        :rtype: :class:`tencentcloud.cfs.v20190719.models.PGroup`
        """
        return self._PGroup

    @PGroup.setter
    def PGroup(self, PGroup):
        self._PGroup = PGroup

    @property
    def FsName(self):
        r"""用户自定义名称
        :rtype: str
        """
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def Encrypted(self):
        r"""文件系统是否加密,true：代表加密，false：非加密
        :rtype: bool
        """
        return self._Encrypted

    @Encrypted.setter
    def Encrypted(self, Encrypted):
        self._Encrypted = Encrypted

    @property
    def KmsKeyId(self):
        r"""加密所使用的密钥，可以为密钥的 ID 或者 ARN
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def AppId(self):
        r"""应用ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def BandwidthLimit(self):
        r"""文件系统吞吐上限，吞吐上限是根据文件系统当前已使用存储量、绑定的存储资源包以及吞吐资源包一同确定. 单位MiB/s
        :rtype: float
        """
        return self._BandwidthLimit

    @BandwidthLimit.setter
    def BandwidthLimit(self, BandwidthLimit):
        self._BandwidthLimit = BandwidthLimit

    @property
    def AutoSnapshotPolicyId(self):
        r"""文件系统关联的快照策略
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def SnapStatus(self):
        r"""文件系统处理快照状态,snapping：快照中，normal：正常状态
        :rtype: str
        """
        return self._SnapStatus

    @SnapStatus.setter
    def SnapStatus(self, SnapStatus):
        self._SnapStatus = SnapStatus

    @property
    def Capacity(self):
        r"""文件系统容量规格上限
单位:GiB
        :rtype: int
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def Tags(self):
        r"""文件系统标签列表
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TieringState(self):
        r"""文件系统生命周期管理状态
NotAvailable：不可用
Available:可用
        :rtype: str
        """
        return self._TieringState

    @TieringState.setter
    def TieringState(self, TieringState):
        self._TieringState = TieringState

    @property
    def TieringDetail(self):
        r"""分层存储详情
        :rtype: :class:`tencentcloud.cfs.v20190719.models.TieringDetailInfo`
        """
        return self._TieringDetail

    @TieringDetail.setter
    def TieringDetail(self, TieringDetail):
        self._TieringDetail = TieringDetail

    @property
    def AutoScaleUpRule(self):
        r"""文件系统自动扩容策略
        :rtype: :class:`tencentcloud.cfs.v20190719.models.AutoScaleUpRule`
        """
        return self._AutoScaleUpRule

    @AutoScaleUpRule.setter
    def AutoScaleUpRule(self, AutoScaleUpRule):
        self._AutoScaleUpRule = AutoScaleUpRule

    @property
    def Version(self):
        r"""文件系统版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ExstraPerformanceInfo(self):
        r"""额外性能信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ExstraPerformanceInfo
        """
        return self._ExstraPerformanceInfo

    @ExstraPerformanceInfo.setter
    def ExstraPerformanceInfo(self, ExstraPerformanceInfo):
        self._ExstraPerformanceInfo = ExstraPerformanceInfo

    @property
    def MetaType(self):
        r"""basic：标准版元数据类型
enhanced：增项版元数据类型
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType


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
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._SnapStatus = params.get("SnapStatus")
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
        if params.get("AutoScaleUpRule") is not None:
            self._AutoScaleUpRule = AutoScaleUpRule()
            self._AutoScaleUpRule._deserialize(params.get("AutoScaleUpRule"))
        self._Version = params.get("Version")
        if params.get("ExstraPerformanceInfo") is not None:
            self._ExstraPerformanceInfo = []
            for item in params.get("ExstraPerformanceInfo"):
                obj = ExstraPerformanceInfo()
                obj._deserialize(item)
                self._ExstraPerformanceInfo.append(obj)
        self._MetaType = params.get("MetaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""条件过滤

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
        r"""值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
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
        


class LifecycleDataTaskInfo(AbstractModel):
    r"""生命周期任务

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _TaskStatus: 任务状态.
init：未执行
running：执行中，finished：已完成
,failed：失败
,stopping：停止中,stopped：已停止
        :type TaskStatus: str
        :param _CreationTime: 任务创建时间
        :type CreationTime: str
        :param _FinishTime: 任务结束时间
        :type FinishTime: str
        :param _FileTotalCount: 文件总数
        :type FileTotalCount: int
        :param _FileSuccessedCount: 处理成功文件数量
        :type FileSuccessedCount: int
        :param _FileFailedCount: 当前已经失败的文件数
        :type FileFailedCount: int
        :param _FileTotalSize: 文件容量，单位Byte


        :type FileTotalSize: int
        :param _FileSuccessedSize: 已处理完成的文件容量，单位Byte


        :type FileSuccessedSize: int
        :param _FileFailedSize: 已处理失败文件容量，单位Byte

        :type FileFailedSize: int
        :param _FileTotalList: 总文件列表
        :type FileTotalList: str
        :param _FileSuccessedList: 成功的文件列表
        :type FileSuccessedList: str
        :param _FileFailedList: 失败文件的列表
        :type FileFailedList: str
        :param _FileSystemId: FileSystemId
        :type FileSystemId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskPath: 任务路径
        :type TaskPath: str
        :param _Type: 任务类型,archive:表示沉降任务，restore：表示拉取任务
        :type Type: str
        :param _DataFlowId: 数据流动Id
        :type DataFlowId: str
        """
        self._TaskId = None
        self._TaskStatus = None
        self._CreationTime = None
        self._FinishTime = None
        self._FileTotalCount = None
        self._FileSuccessedCount = None
        self._FileFailedCount = None
        self._FileTotalSize = None
        self._FileSuccessedSize = None
        self._FileFailedSize = None
        self._FileTotalList = None
        self._FileSuccessedList = None
        self._FileFailedList = None
        self._FileSystemId = None
        self._TaskName = None
        self._TaskPath = None
        self._Type = None
        self._DataFlowId = None

    @property
    def TaskId(self):
        r"""任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskStatus(self):
        r"""任务状态.
init：未执行
running：执行中，finished：已完成
,failed：失败
,stopping：停止中,stopped：已停止
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def CreationTime(self):
        r"""任务创建时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def FinishTime(self):
        r"""任务结束时间
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def FileTotalCount(self):
        r"""文件总数
        :rtype: int
        """
        return self._FileTotalCount

    @FileTotalCount.setter
    def FileTotalCount(self, FileTotalCount):
        self._FileTotalCount = FileTotalCount

    @property
    def FileSuccessedCount(self):
        r"""处理成功文件数量
        :rtype: int
        """
        return self._FileSuccessedCount

    @FileSuccessedCount.setter
    def FileSuccessedCount(self, FileSuccessedCount):
        self._FileSuccessedCount = FileSuccessedCount

    @property
    def FileFailedCount(self):
        r"""当前已经失败的文件数
        :rtype: int
        """
        return self._FileFailedCount

    @FileFailedCount.setter
    def FileFailedCount(self, FileFailedCount):
        self._FileFailedCount = FileFailedCount

    @property
    def FileTotalSize(self):
        r"""文件容量，单位Byte


        :rtype: int
        """
        return self._FileTotalSize

    @FileTotalSize.setter
    def FileTotalSize(self, FileTotalSize):
        self._FileTotalSize = FileTotalSize

    @property
    def FileSuccessedSize(self):
        r"""已处理完成的文件容量，单位Byte


        :rtype: int
        """
        return self._FileSuccessedSize

    @FileSuccessedSize.setter
    def FileSuccessedSize(self, FileSuccessedSize):
        self._FileSuccessedSize = FileSuccessedSize

    @property
    def FileFailedSize(self):
        r"""已处理失败文件容量，单位Byte

        :rtype: int
        """
        return self._FileFailedSize

    @FileFailedSize.setter
    def FileFailedSize(self, FileFailedSize):
        self._FileFailedSize = FileFailedSize

    @property
    def FileTotalList(self):
        r"""总文件列表
        :rtype: str
        """
        return self._FileTotalList

    @FileTotalList.setter
    def FileTotalList(self, FileTotalList):
        self._FileTotalList = FileTotalList

    @property
    def FileSuccessedList(self):
        r"""成功的文件列表
        :rtype: str
        """
        return self._FileSuccessedList

    @FileSuccessedList.setter
    def FileSuccessedList(self, FileSuccessedList):
        self._FileSuccessedList = FileSuccessedList

    @property
    def FileFailedList(self):
        r"""失败文件的列表
        :rtype: str
        """
        return self._FileFailedList

    @FileFailedList.setter
    def FileFailedList(self, FileFailedList):
        self._FileFailedList = FileFailedList

    @property
    def FileSystemId(self):
        r"""FileSystemId
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def TaskName(self):
        r"""任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskPath(self):
        r"""任务路径
        :rtype: str
        """
        return self._TaskPath

    @TaskPath.setter
    def TaskPath(self, TaskPath):
        self._TaskPath = TaskPath

    @property
    def Type(self):
        r"""任务类型,archive:表示沉降任务，restore：表示拉取任务
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DataFlowId(self):
        r"""数据流动Id
        :rtype: str
        """
        return self._DataFlowId

    @DataFlowId.setter
    def DataFlowId(self, DataFlowId):
        self._DataFlowId = DataFlowId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskStatus = params.get("TaskStatus")
        self._CreationTime = params.get("CreationTime")
        self._FinishTime = params.get("FinishTime")
        self._FileTotalCount = params.get("FileTotalCount")
        self._FileSuccessedCount = params.get("FileSuccessedCount")
        self._FileFailedCount = params.get("FileFailedCount")
        self._FileTotalSize = params.get("FileTotalSize")
        self._FileSuccessedSize = params.get("FileSuccessedSize")
        self._FileFailedSize = params.get("FileFailedSize")
        self._FileTotalList = params.get("FileTotalList")
        self._FileSuccessedList = params.get("FileSuccessedList")
        self._FileFailedList = params.get("FileFailedList")
        self._FileSystemId = params.get("FileSystemId")
        self._TaskName = params.get("TaskName")
        self._TaskPath = params.get("TaskPath")
        self._Type = params.get("Type")
        self._DataFlowId = params.get("DataFlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifecyclePolicy(AbstractModel):
    r"""生命周期管理策略信息

    """

    def __init__(self):
        r"""
        :param _CreateTime: 生命周期管理策略创建的时间
        :type CreateTime: str
        :param _LifecyclePolicyID: 生命周期管理策略ID
        :type LifecyclePolicyID: str
        :param _LifecyclePolicyName: 生命周期管理策略名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LifecyclePolicyName: str
        :param _LifecycleRules: 生命周期管理策略关联的管理规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LifecycleRules: list of LifecycleRule
        :param _Paths: 生命周期管理策略关联目录的绝对路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Paths: list of PathInfo
        """
        self._CreateTime = None
        self._LifecyclePolicyID = None
        self._LifecyclePolicyName = None
        self._LifecycleRules = None
        self._Paths = None

    @property
    def CreateTime(self):
        r"""生命周期管理策略创建的时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LifecyclePolicyID(self):
        r"""生命周期管理策略ID
        :rtype: str
        """
        return self._LifecyclePolicyID

    @LifecyclePolicyID.setter
    def LifecyclePolicyID(self, LifecyclePolicyID):
        self._LifecyclePolicyID = LifecyclePolicyID

    @property
    def LifecyclePolicyName(self):
        r"""生命周期管理策略名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LifecyclePolicyName

    @LifecyclePolicyName.setter
    def LifecyclePolicyName(self, LifecyclePolicyName):
        self._LifecyclePolicyName = LifecyclePolicyName

    @property
    def LifecycleRules(self):
        r"""生命周期管理策略关联的管理规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LifecycleRule
        """
        return self._LifecycleRules

    @LifecycleRules.setter
    def LifecycleRules(self, LifecycleRules):
        self._LifecycleRules = LifecycleRules

    @property
    def Paths(self):
        r"""生命周期管理策略关联目录的绝对路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PathInfo
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._LifecyclePolicyID = params.get("LifecyclePolicyID")
        self._LifecyclePolicyName = params.get("LifecyclePolicyName")
        if params.get("LifecycleRules") is not None:
            self._LifecycleRules = []
            for item in params.get("LifecycleRules"):
                obj = LifecycleRule()
                obj._deserialize(item)
                self._LifecycleRules.append(obj)
        if params.get("Paths") is not None:
            self._Paths = []
            for item in params.get("Paths"):
                obj = PathInfo()
                obj._deserialize(item)
                self._Paths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifecycleRule(AbstractModel):
    r"""生命周期管理策略关联的管理规则

    """

    def __init__(self):
        r"""
        :param _StorageType: 数据转储后的存储类型。其中：InfrequentAccess：低频介质存储；ColdStorage：冷存储。
        :type StorageType: str
        :param _FileType: 数据转储文件类型。其中，BIG_FILE：超大文件；STD_FILE：普通文件；SMALL_FILE：小文件；ALL：所有文件。
        :type FileType: str
        :param _Action: 数据转储行为。其中，Archive：沉降；Noarchive：不沉降。
        :type Action: str
        :param _Interval: 数据转储触发时间。由“DEFAULT_ATIME_”与“数字”组成，单位为天。当 Action 为 Noarchive，请保持为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Interval: str
        :param _FileMaxSize: 数据转储文件最大规格。其数值需使用“数字+单位”格式进行表示，单位支持K（KiB）、M（MiB）、G（GiB）。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileMaxSize: str
        :param _FileMinSize: 数据转储文件最小规格。其数值需使用“数字+单位”格式进行表示，单位支持K（KiB）、M（MiB）、G（GiB）。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileMinSize: str
        """
        self._StorageType = None
        self._FileType = None
        self._Action = None
        self._Interval = None
        self._FileMaxSize = None
        self._FileMinSize = None

    @property
    def StorageType(self):
        r"""数据转储后的存储类型。其中：InfrequentAccess：低频介质存储；ColdStorage：冷存储。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def FileType(self):
        r"""数据转储文件类型。其中，BIG_FILE：超大文件；STD_FILE：普通文件；SMALL_FILE：小文件；ALL：所有文件。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Action(self):
        r"""数据转储行为。其中，Archive：沉降；Noarchive：不沉降。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Interval(self):
        r"""数据转储触发时间。由“DEFAULT_ATIME_”与“数字”组成，单位为天。当 Action 为 Noarchive，请保持为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def FileMaxSize(self):
        r"""数据转储文件最大规格。其数值需使用“数字+单位”格式进行表示，单位支持K（KiB）、M（MiB）、G（GiB）。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileMaxSize

    @FileMaxSize.setter
    def FileMaxSize(self, FileMaxSize):
        self._FileMaxSize = FileMaxSize

    @property
    def FileMinSize(self):
        r"""数据转储文件最小规格。其数值需使用“数字+单位”格式进行表示，单位支持K（KiB）、M（MiB）、G（GiB）。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileMinSize

    @FileMinSize.setter
    def FileMinSize(self, FileMinSize):
        self._FileMinSize = FileMinSize


    def _deserialize(self, params):
        self._StorageType = params.get("StorageType")
        self._FileType = params.get("FileType")
        self._Action = params.get("Action")
        self._Interval = params.get("Interval")
        self._FileMaxSize = params.get("FileMaxSize")
        self._FileMinSize = params.get("FileMinSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrationTaskInfo(AbstractModel):
    r"""CFS数据迁移任务信息

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
        :type BucketName: str
        :param _BucketRegion: 数据源桶地域
        :type BucketRegion: str
        :param _BucketAddress: 数据源桶地址
        :type BucketAddress: str
        :param _ListAddress: 清单地址
        :type ListAddress: str
        :param _FsName: 文件系统实例名称
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
        :type EndTime: int
        :param _Status: 迁移状态。0: 已完成；1: 创建中；2: 运行中；3: 终止中；4: 已终止；5: 创建失败；6: 运行失败；7: 结束中；8: 删除中；9: 等待中
        :type Status: int
        :param _FileTotalCount: 文件数量
        :type FileTotalCount: int
        :param _FileMigratedCount: 已迁移文件数量
        :type FileMigratedCount: int
        :param _FileFailedCount: 迁移失败文件数量
        :type FileFailedCount: int
        :param _FileTotalSize: 文件容量，单位Byte
        :type FileTotalSize: int
        :param _FileMigratedSize: 已迁移文件容量，单位Byte
        :type FileMigratedSize: int
        :param _FileFailedSize: 迁移失败文件容量，单位Byte
        :type FileFailedSize: int
        :param _FileTotalList: 全部清单
        :type FileTotalList: str
        :param _FileCompletedList: 已完成文件清单
        :type FileCompletedList: str
        :param _FileFailedList: 失败文件清单
        :type FileFailedList: str
        :param _BucketPath: 源桶路径
        :type BucketPath: str
        :param _Direction: 迁移方向。0: 对象存储迁移至文件系统，1: 文件系统迁移至对象存储。默认 0
        :type Direction: int
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
        self._Direction = None

    @property
    def TaskName(self):
        r"""迁移任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskId(self):
        r"""迁移任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MigrationType(self):
        r"""迁移方式标志位，默认为0。0: 桶迁移；1: 清单迁移
        :rtype: int
        """
        return self._MigrationType

    @MigrationType.setter
    def MigrationType(self, MigrationType):
        self._MigrationType = MigrationType

    @property
    def MigrationMode(self):
        r"""迁移模式，默认为0。0: 全量迁移
        :rtype: int
        """
        return self._MigrationMode

    @MigrationMode.setter
    def MigrationMode(self, MigrationMode):
        self._MigrationMode = MigrationMode

    @property
    def BucketName(self):
        r"""数据源桶名称
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketRegion(self):
        r"""数据源桶地域
        :rtype: str
        """
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def BucketAddress(self):
        r"""数据源桶地址
        :rtype: str
        """
        return self._BucketAddress

    @BucketAddress.setter
    def BucketAddress(self, BucketAddress):
        self._BucketAddress = BucketAddress

    @property
    def ListAddress(self):
        r"""清单地址
        :rtype: str
        """
        return self._ListAddress

    @ListAddress.setter
    def ListAddress(self, ListAddress):
        self._ListAddress = ListAddress

    @property
    def FsName(self):
        r"""文件系统实例名称
        :rtype: str
        """
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def FileSystemId(self):
        r"""文件系统实例Id
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsPath(self):
        r"""文件系统路径
        :rtype: str
        """
        return self._FsPath

    @FsPath.setter
    def FsPath(self, FsPath):
        self._FsPath = FsPath

    @property
    def CoverType(self):
        r"""同名文件迁移时覆盖策略，默认为0。0: 最后修改时间优先；1: 全覆盖；2: 不覆盖
        :rtype: int
        """
        return self._CoverType

    @CoverType.setter
    def CoverType(self, CoverType):
        self._CoverType = CoverType

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        r"""完成/终止时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""迁移状态。0: 已完成；1: 创建中；2: 运行中；3: 终止中；4: 已终止；5: 创建失败；6: 运行失败；7: 结束中；8: 删除中；9: 等待中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FileTotalCount(self):
        r"""文件数量
        :rtype: int
        """
        return self._FileTotalCount

    @FileTotalCount.setter
    def FileTotalCount(self, FileTotalCount):
        self._FileTotalCount = FileTotalCount

    @property
    def FileMigratedCount(self):
        r"""已迁移文件数量
        :rtype: int
        """
        return self._FileMigratedCount

    @FileMigratedCount.setter
    def FileMigratedCount(self, FileMigratedCount):
        self._FileMigratedCount = FileMigratedCount

    @property
    def FileFailedCount(self):
        r"""迁移失败文件数量
        :rtype: int
        """
        return self._FileFailedCount

    @FileFailedCount.setter
    def FileFailedCount(self, FileFailedCount):
        self._FileFailedCount = FileFailedCount

    @property
    def FileTotalSize(self):
        r"""文件容量，单位Byte
        :rtype: int
        """
        return self._FileTotalSize

    @FileTotalSize.setter
    def FileTotalSize(self, FileTotalSize):
        self._FileTotalSize = FileTotalSize

    @property
    def FileMigratedSize(self):
        r"""已迁移文件容量，单位Byte
        :rtype: int
        """
        return self._FileMigratedSize

    @FileMigratedSize.setter
    def FileMigratedSize(self, FileMigratedSize):
        self._FileMigratedSize = FileMigratedSize

    @property
    def FileFailedSize(self):
        r"""迁移失败文件容量，单位Byte
        :rtype: int
        """
        return self._FileFailedSize

    @FileFailedSize.setter
    def FileFailedSize(self, FileFailedSize):
        self._FileFailedSize = FileFailedSize

    @property
    def FileTotalList(self):
        r"""全部清单
        :rtype: str
        """
        return self._FileTotalList

    @FileTotalList.setter
    def FileTotalList(self, FileTotalList):
        self._FileTotalList = FileTotalList

    @property
    def FileCompletedList(self):
        r"""已完成文件清单
        :rtype: str
        """
        return self._FileCompletedList

    @FileCompletedList.setter
    def FileCompletedList(self, FileCompletedList):
        self._FileCompletedList = FileCompletedList

    @property
    def FileFailedList(self):
        r"""失败文件清单
        :rtype: str
        """
        return self._FileFailedList

    @FileFailedList.setter
    def FileFailedList(self, FileFailedList):
        self._FileFailedList = FileFailedList

    @property
    def BucketPath(self):
        r"""源桶路径
        :rtype: str
        """
        return self._BucketPath

    @BucketPath.setter
    def BucketPath(self, BucketPath):
        self._BucketPath = BucketPath

    @property
    def Direction(self):
        r"""迁移方向。0: 对象存储迁移至文件系统，1: 文件系统迁移至对象存储。默认 0
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


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
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataFlowRequest(AbstractModel):
    r"""ModifyDataFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataFlowId: 数据流动管理 ID ，通过查询数据流动接口获取
        :type DataFlowId: str
        :param _FileSystemId: 文件系统 ID ，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :type FileSystemId: str
        :param _DataFlowName: 数据流动名称；支持不超过64字符长度，支持中文、数字、_、-
        :type DataFlowName: str
        :param _SecretId: 密钥 ID
        :type SecretId: str
        :param _SecretKey: 密钥 key
        :type SecretKey: str
        :param _UserKafkaTopic: KafkaConsumer 消费时使用的Topic参数
        :type UserKafkaTopic: str
        :param _ServerAddr: 服务地址
        :type ServerAddr: str
        :param _UserName: name
        :type UserName: str
        :param _Password: Kafka消费用户密码
        :type Password: str
        :param _AutoRefresh: 元数据增量更新开关；1开启，0关闭
        :type AutoRefresh: int
        """
        self._DataFlowId = None
        self._FileSystemId = None
        self._DataFlowName = None
        self._SecretId = None
        self._SecretKey = None
        self._UserKafkaTopic = None
        self._ServerAddr = None
        self._UserName = None
        self._Password = None
        self._AutoRefresh = None

    @property
    def DataFlowId(self):
        r"""数据流动管理 ID ，通过查询数据流动接口获取
        :rtype: str
        """
        return self._DataFlowId

    @DataFlowId.setter
    def DataFlowId(self, DataFlowId):
        self._DataFlowId = DataFlowId

    @property
    def FileSystemId(self):
        r"""文件系统 ID ，通过查询文件系统 [DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170) 获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def DataFlowName(self):
        r"""数据流动名称；支持不超过64字符长度，支持中文、数字、_、-
        :rtype: str
        """
        return self._DataFlowName

    @DataFlowName.setter
    def DataFlowName(self, DataFlowName):
        self._DataFlowName = DataFlowName

    @property
    def SecretId(self):
        r"""密钥 ID
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        r"""密钥 key
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def UserKafkaTopic(self):
        r"""KafkaConsumer 消费时使用的Topic参数
        :rtype: str
        """
        return self._UserKafkaTopic

    @UserKafkaTopic.setter
    def UserKafkaTopic(self, UserKafkaTopic):
        self._UserKafkaTopic = UserKafkaTopic

    @property
    def ServerAddr(self):
        r"""服务地址
        :rtype: str
        """
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def UserName(self):
        r"""name
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""Kafka消费用户密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def AutoRefresh(self):
        r"""元数据增量更新开关；1开启，0关闭
        :rtype: int
        """
        return self._AutoRefresh

    @AutoRefresh.setter
    def AutoRefresh(self, AutoRefresh):
        self._AutoRefresh = AutoRefresh


    def _deserialize(self, params):
        self._DataFlowId = params.get("DataFlowId")
        self._FileSystemId = params.get("FileSystemId")
        self._DataFlowName = params.get("DataFlowName")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._UserKafkaTopic = params.get("UserKafkaTopic")
        self._ServerAddr = params.get("ServerAddr")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._AutoRefresh = params.get("AutoRefresh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataFlowResponse(AbstractModel):
    r"""ModifyDataFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataFlowId: 数据流动管理 ID
        :type DataFlowId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataFlowId = None
        self._RequestId = None

    @property
    def DataFlowId(self):
        r"""数据流动管理 ID
        :rtype: str
        """
        return self._DataFlowId

    @DataFlowId.setter
    def DataFlowId(self, DataFlowId):
        self._DataFlowId = DataFlowId

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
        self._DataFlowId = params.get("DataFlowId")
        self._RequestId = params.get("RequestId")


class ModifyFileSystemAutoScaleUpRuleRequest(AbstractModel):
    r"""ModifyFileSystemAutoScaleUpRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID，通过查询文件系统列表获取；[DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170)
        :type FileSystemId: str
        :param _ScaleUpThreshold: 扩容阈值，范围[10-90]
        :type ScaleUpThreshold: int
        :param _TargetThreshold: 扩容后目标阈值，范围[10-90]，该值要小于 ScaleUpThreshold
        :type TargetThreshold: int
        :param _Status: 规则状态 0：关闭，1：开启；不传保留原状态
        :type Status: int
        """
        self._FileSystemId = None
        self._ScaleUpThreshold = None
        self._TargetThreshold = None
        self._Status = None

    @property
    def FileSystemId(self):
        r"""文件系统 ID，通过查询文件系统列表获取；[DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170)
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def ScaleUpThreshold(self):
        r"""扩容阈值，范围[10-90]
        :rtype: int
        """
        return self._ScaleUpThreshold

    @ScaleUpThreshold.setter
    def ScaleUpThreshold(self, ScaleUpThreshold):
        self._ScaleUpThreshold = ScaleUpThreshold

    @property
    def TargetThreshold(self):
        r"""扩容后目标阈值，范围[10-90]，该值要小于 ScaleUpThreshold
        :rtype: int
        """
        return self._TargetThreshold

    @TargetThreshold.setter
    def TargetThreshold(self, TargetThreshold):
        self._TargetThreshold = TargetThreshold

    @property
    def Status(self):
        r"""规则状态 0：关闭，1：开启；不传保留原状态
        :rtype: int
        """
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
    r"""ModifyFileSystemAutoScaleUpRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param _Status: 规则状态 0：关闭，1：开启
        :type Status: int
        :param _ScaleUpThreshold: 扩容阈值，范围[10-90]
        :type ScaleUpThreshold: int
        :param _TargetThreshold: 扩容后达到阈值，范围[10-90]
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
        r"""文件系统 ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Status(self):
        r"""规则状态 0：关闭，1：开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ScaleUpThreshold(self):
        r"""扩容阈值，范围[10-90]
        :rtype: int
        """
        return self._ScaleUpThreshold

    @ScaleUpThreshold.setter
    def ScaleUpThreshold(self, ScaleUpThreshold):
        self._ScaleUpThreshold = ScaleUpThreshold

    @property
    def TargetThreshold(self):
        r"""扩容后达到阈值，范围[10-90]
        :rtype: int
        """
        return self._TargetThreshold

    @TargetThreshold.setter
    def TargetThreshold(self, TargetThreshold):
        self._TargetThreshold = TargetThreshold

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
        self._FileSystemId = params.get("FileSystemId")
        self._Status = params.get("Status")
        self._ScaleUpThreshold = params.get("ScaleUpThreshold")
        self._TargetThreshold = params.get("TargetThreshold")
        self._RequestId = params.get("RequestId")


class ModifyLifecyclePolicyRequest(AbstractModel):
    r"""ModifyLifecyclePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecyclePolicyName: 生命周期管理策略名称，中文/英文/数字/下划线/中划线的组合，不超过64个字符
        :type LifecyclePolicyName: str
        :param _LifecycleRules: 生命周期管理策略关联的管理规则列表
        :type LifecycleRules: list of LifecycleRule
        :param _LifecyclePolicyID: 生命周期管理策略ID
        :type LifecyclePolicyID: str
        """
        self._LifecyclePolicyName = None
        self._LifecycleRules = None
        self._LifecyclePolicyID = None

    @property
    def LifecyclePolicyName(self):
        r"""生命周期管理策略名称，中文/英文/数字/下划线/中划线的组合，不超过64个字符
        :rtype: str
        """
        return self._LifecyclePolicyName

    @LifecyclePolicyName.setter
    def LifecyclePolicyName(self, LifecyclePolicyName):
        self._LifecyclePolicyName = LifecyclePolicyName

    @property
    def LifecycleRules(self):
        r"""生命周期管理策略关联的管理规则列表
        :rtype: list of LifecycleRule
        """
        return self._LifecycleRules

    @LifecycleRules.setter
    def LifecycleRules(self, LifecycleRules):
        self._LifecycleRules = LifecycleRules

    @property
    def LifecyclePolicyID(self):
        r"""生命周期管理策略ID
        :rtype: str
        """
        return self._LifecyclePolicyID

    @LifecyclePolicyID.setter
    def LifecyclePolicyID(self, LifecyclePolicyID):
        self._LifecyclePolicyID = LifecyclePolicyID


    def _deserialize(self, params):
        self._LifecyclePolicyName = params.get("LifecyclePolicyName")
        if params.get("LifecycleRules") is not None:
            self._LifecycleRules = []
            for item in params.get("LifecycleRules"):
                obj = LifecycleRule()
                obj._deserialize(item)
                self._LifecycleRules.append(obj)
        self._LifecyclePolicyID = params.get("LifecyclePolicyID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLifecyclePolicyResponse(AbstractModel):
    r"""ModifyLifecyclePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecyclePolicyID: 生命周期管理策略ID
        :type LifecyclePolicyID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LifecyclePolicyID = None
        self._RequestId = None

    @property
    def LifecyclePolicyID(self):
        r"""生命周期管理策略ID
        :rtype: str
        """
        return self._LifecyclePolicyID

    @LifecyclePolicyID.setter
    def LifecyclePolicyID(self, LifecyclePolicyID):
        self._LifecyclePolicyID = LifecyclePolicyID

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
        self._LifecyclePolicyID = params.get("LifecyclePolicyID")
        self._RequestId = params.get("RequestId")


class MountInfo(AbstractModel):
    r"""挂载点信息

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
        :param _LifeCycleState: 挂载点状态，包括creating：创建中；available：运行中；
deleting：删除中；
create_failed： 创建失败
        :type LifeCycleState: str
        :param _NetworkInterface: 网络类型，包括VPC,CCN
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
        r"""文件系统 ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def MountTargetId(self):
        r"""挂载点 ID
        :rtype: str
        """
        return self._MountTargetId

    @MountTargetId.setter
    def MountTargetId(self, MountTargetId):
        self._MountTargetId = MountTargetId

    @property
    def IpAddress(self):
        r"""挂载点 IP
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def FSID(self):
        r"""挂载根目录
        :rtype: str
        """
        return self._FSID

    @FSID.setter
    def FSID(self, FSID):
        self._FSID = FSID

    @property
    def LifeCycleState(self):
        r"""挂载点状态，包括creating：创建中；available：运行中；
deleting：删除中；
create_failed： 创建失败
        :rtype: str
        """
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def NetworkInterface(self):
        r"""网络类型，包括VPC,CCN
        :rtype: str
        """
        return self._NetworkInterface

    @NetworkInterface.setter
    def NetworkInterface(self, NetworkInterface):
        self._NetworkInterface = NetworkInterface

    @property
    def VpcId(self):
        r"""私有网络 ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""私有网络名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetId(self):
        r"""子网 Id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        r"""子网名称
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CcnID(self):
        r"""CFS Turbo使用的云联网ID
        :rtype: str
        """
        return self._CcnID

    @CcnID.setter
    def CcnID(self, CcnID):
        self._CcnID = CcnID

    @property
    def CidrBlock(self):
        r"""云联网中CFS Turbo使用的网段
        :rtype: str
        """
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
    r"""文件系统绑定权限组信息

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
        r"""权限组ID
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        r"""权限组名称
        :rtype: str
        """
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
    r"""权限组数组

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
        r"""权限组ID
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        r"""权限组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        r"""描述信息
        :rtype: str
        """
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo

    @property
    def CDate(self):
        r"""创建时间
        :rtype: str
        """
        return self._CDate

    @CDate.setter
    def CDate(self, CDate):
        self._CDate = CDate

    @property
    def BindCfsNum(self):
        r"""关联文件系统个数
        :rtype: int
        """
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
    r"""权限组规则列表

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
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AuthClientIp(self):
        r"""允许访问的客户端IP
        :rtype: str
        """
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        r"""读写权限, ro为只读，rw为读写
        :rtype: str
        """
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        r"""all_squash：所有访问用户（含 root 用户）都会被映射为匿名用户或用户组。
no_all_squash：所有访问用户（含 root 用户）均保持原有的 UID/GID 信息。
root_squash：将来访的 root 用户映射为匿名用户或用户组，非 root 用户保持原有的 UID/GID 信息。
no_root_squash：与 no_all_squash 效果一致，所有访问用户（含 root 用户）均保持原有的 UID/GID 信息

        :rtype: str
        """
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        r"""规则优先级，1-100。 其中 1 为最高，100为最低
        :rtype: int
        """
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
        


class PathInfo(AbstractModel):
    r"""生命周期管理策略关联目录的绝对路径

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _Path: 目录绝对路径
        :type Path: str
        """
        self._FileSystemId = None
        self._Path = None

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Path(self):
        r"""目录绝对路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpFileSystemRequest(AbstractModel):
    r"""ScaleUpFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统Id,该参数通过查询文件系统列表接口获取
        :type FileSystemId: str
        :param _TargetCapacity: 扩容的目标容量（单位GiB）
        :type TargetCapacity: int
        """
        self._FileSystemId = None
        self._TargetCapacity = None

    @property
    def FileSystemId(self):
        r"""文件系统Id,该参数通过查询文件系统列表接口获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def TargetCapacity(self):
        r"""扩容的目标容量（单位GiB）
        :rtype: int
        """
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
    r"""ScaleUpFileSystem返回参数结构体

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
        r"""文件系统Id
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def TargetCapacity(self):
        r"""扩容的目标容量（单位GiB）
        :rtype: int
        """
        return self._TargetCapacity

    @TargetCapacity.setter
    def TargetCapacity(self, TargetCapacity):
        self._TargetCapacity = TargetCapacity

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
        self._FileSystemId = params.get("FileSystemId")
        self._TargetCapacity = params.get("TargetCapacity")
        self._RequestId = params.get("RequestId")


class SetUserQuotaRequest(AbstractModel):
    r"""SetUserQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID,通过[查询文件系统列表](https://cloud.tencent.com/document/api/582/38170)获取
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
        r"""文件系统 ID,通过[查询文件系统列表](https://cloud.tencent.com/document/api/582/38170)获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def UserType(self):
        r"""指定配额类型，包括Uid、Gid，Dir，分别代表用户配额，用户组配额，目录配额
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserId(self):
        r"""UID/GID信息
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def CapacityHardLimit(self):
        r"""容量硬限制，单位GiB。设置范围10-10000000。
        :rtype: int
        """
        return self._CapacityHardLimit

    @CapacityHardLimit.setter
    def CapacityHardLimit(self, CapacityHardLimit):
        self._CapacityHardLimit = CapacityHardLimit

    @property
    def FileHardLimit(self):
        r"""文件硬限制，单位个。设置范围1000-100000000
        :rtype: int
        """
        return self._FileHardLimit

    @FileHardLimit.setter
    def FileHardLimit(self, FileHardLimit):
        self._FileHardLimit = FileHardLimit

    @property
    def DirectoryPath(self):
        r"""需设置目录配额的目录绝对路径，不同目录不可存在包含关系
        :rtype: str
        """
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
    r"""SetUserQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: UID/GID信息
        :type UserId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._RequestId = None

    @property
    def UserId(self):
        r"""UID/GID信息
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

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
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")


class SignUpCfsServiceRequest(AbstractModel):
    r"""SignUpCfsService请求参数结构体

    """


class SignUpCfsServiceResponse(AbstractModel):
    r"""SignUpCfsService返回参数结构体

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
        r"""该用户当前 CFS 服务的状态，creating 是开通中，created 是已开通
        :rtype: str
        """
        return self._CfsServiceStatus

    @CfsServiceStatus.setter
    def CfsServiceStatus(self, CfsServiceStatus):
        self._CfsServiceStatus = CfsServiceStatus

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
        self._CfsServiceStatus = params.get("CfsServiceStatus")
        self._RequestId = params.get("RequestId")


class SnapshotInfo(AbstractModel):
    r"""快照信息

    """

    def __init__(self):
        r"""
        :param _CreationTime: 创建快照时间
        :type CreationTime: str
        :param _SnapshotName: 快照名称
        :type SnapshotName: str
        :param _SnapshotId: 快照ID
        :type SnapshotId: str
        :param _Status: 快照状态，creating-创建中；available-运行中；deleting-删除中；rollbacking-new 创建新文件系统中；create-failed 创建失败
        :type Status: str
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _Size: 快照大小
        :type Size: int
        :param _AliveDay: 保留时长天
        :type AliveDay: int
        :param _Percent: 快照进度百分比，1表示1% 范围1-100
        :type Percent: int
        :param _AppId: 账号ID
        :type AppId: int
        :param _DeleteTime: 快照删除时间
        :type DeleteTime: str
        :param _FsName: 文件系统名称
        :type FsName: str
        :param _Tags: 快照标签
        :type Tags: list of TagInfo
        :param _SnapshotType: 快照类型，general为通用系列快照，turbo为Turbo系列快照
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotType: str
        :param _SnapshotTime: 实际快照时间，反映快照对应文件系统某个时刻的数据。
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
        r"""创建快照时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def SnapshotName(self):
        r"""快照名称
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SnapshotId(self):
        r"""快照ID
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Status(self):
        r"""快照状态，creating-创建中；available-运行中；deleting-删除中；rollbacking-new 创建新文件系统中；create-failed 创建失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RegionName(self):
        r"""地域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Size(self):
        r"""快照大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def AliveDay(self):
        r"""保留时长天
        :rtype: int
        """
        return self._AliveDay

    @AliveDay.setter
    def AliveDay(self, AliveDay):
        self._AliveDay = AliveDay

    @property
    def Percent(self):
        r"""快照进度百分比，1表示1% 范围1-100
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def AppId(self):
        r"""账号ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def DeleteTime(self):
        r"""快照删除时间
        :rtype: str
        """
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime

    @property
    def FsName(self):
        r"""文件系统名称
        :rtype: str
        """
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def Tags(self):
        r"""快照标签
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SnapshotType(self):
        r"""快照类型，general为通用系列快照，turbo为Turbo系列快照
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SnapshotType

    @SnapshotType.setter
    def SnapshotType(self, SnapshotType):
        self._SnapshotType = SnapshotType

    @property
    def SnapshotTime(self):
        r"""实际快照时间，反映快照对应文件系统某个时刻的数据。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
    r"""快照操作日志

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
        r"""操作类型
CreateCfsSnapshot：创建快照
DeleteCfsSnapshot：删除快照
CreateCfsFileSystem：创建文件系统
UpdateCfsSnapshotAttribute：更新快照
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionTime(self):
        r"""操作时间
        :rtype: str
        """
        return self._ActionTime

    @ActionTime.setter
    def ActionTime(self, ActionTime):
        self._ActionTime = ActionTime

    @property
    def ActionName(self):
        r"""操作名称
CreateCfsSnapshot
DeleteCfsSnapshot
CreateCfsFileSystem
UpdateCfsSnapshotAttribute
        :rtype: str
        """
        return self._ActionName

    @ActionName.setter
    def ActionName(self, ActionName):
        self._ActionName = ActionName

    @property
    def Operator(self):
        r"""操作者uin
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Result(self):
        r"""1-任务进行中；2-任务成功；3-任务失败
        :rtype: int
        """
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
    r"""文件系统快照统计

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _SnapshotNumber: 快照总个数
        :type SnapshotNumber: int
        :param _SnapshotSize: 快照总容量，单位是MiB
        :type SnapshotSize: int
        """
        self._Region = None
        self._SnapshotNumber = None
        self._SnapshotSize = None

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SnapshotNumber(self):
        r"""快照总个数
        :rtype: int
        """
        return self._SnapshotNumber

    @SnapshotNumber.setter
    def SnapshotNumber(self, SnapshotNumber):
        self._SnapshotNumber = SnapshotNumber

    @property
    def SnapshotSize(self):
        r"""快照总容量，单位是MiB
        :rtype: int
        """
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
        


class StopLifecycleDataTaskRequest(AbstractModel):
    r"""StopLifecycleDataTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
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
        


class StopLifecycleDataTaskResponse(AbstractModel):
    r"""StopLifecycleDataTask返回参数结构体

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


class StopMigrationTaskRequest(AbstractModel):
    r"""StopMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 迁移任务Id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""迁移任务Id
        :rtype: str
        """
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
    r"""StopMigrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 迁移任务Id
        :type TaskId: str
        :param _Status: 迁移状态。0: 已完成；1: 创建中；2: 运行中；3: 终止中；4: 已终止；5: 创建失败；6: 运行失败；7: 结束中；8: 删除中；9: 等待中
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""迁移任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""迁移状态。0: 已完成；1: 创建中；2: 运行中；3: 终止中；4: 已终止；5: 创建失败；6: 运行失败；7: 结束中；8: 删除中；9: 等待中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    r"""Tag信息单元

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
        r"""标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
        :rtype: str
        """
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
    r"""分层存储详细信息

    """

    def __init__(self):
        r"""
        :param _TieringSizeInBytes: 低频存储容量
        :type TieringSizeInBytes: int
        :param _SecondaryTieringSizeInBytes: 冷存储容量
        :type SecondaryTieringSizeInBytes: int
        """
        self._TieringSizeInBytes = None
        self._SecondaryTieringSizeInBytes = None

    @property
    def TieringSizeInBytes(self):
        r"""低频存储容量
        :rtype: int
        """
        return self._TieringSizeInBytes

    @TieringSizeInBytes.setter
    def TieringSizeInBytes(self, TieringSizeInBytes):
        self._TieringSizeInBytes = TieringSizeInBytes

    @property
    def SecondaryTieringSizeInBytes(self):
        r"""冷存储容量
        :rtype: int
        """
        return self._SecondaryTieringSizeInBytes

    @SecondaryTieringSizeInBytes.setter
    def SecondaryTieringSizeInBytes(self, SecondaryTieringSizeInBytes):
        self._SecondaryTieringSizeInBytes = SecondaryTieringSizeInBytes


    def _deserialize(self, params):
        self._TieringSizeInBytes = params.get("TieringSizeInBytes")
        self._SecondaryTieringSizeInBytes = params.get("SecondaryTieringSizeInBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoSnapshotPolicyRequest(AbstractModel):
    r"""UnbindAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemIds: 需要解绑的文件系统ID列表，用"," 分割，文件系统ID，通过查询文件系统列表获取；[DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170)
        :type FileSystemIds: str
        :param _AutoSnapshotPolicyId: 解绑的快照策略ID，可以通过[DescribeAutoSnapshotPolicies](https://cloud.tencent.com/document/api/582/80208) 查询获取
        :type AutoSnapshotPolicyId: str
        """
        self._FileSystemIds = None
        self._AutoSnapshotPolicyId = None

    @property
    def FileSystemIds(self):
        r"""需要解绑的文件系统ID列表，用"," 分割，文件系统ID，通过查询文件系统列表获取；[DescribeCfsFileSystems](https://cloud.tencent.com/document/product/582/38170)
        :rtype: str
        """
        return self._FileSystemIds

    @FileSystemIds.setter
    def FileSystemIds(self, FileSystemIds):
        self._FileSystemIds = FileSystemIds

    @property
    def AutoSnapshotPolicyId(self):
        r"""解绑的快照策略ID，可以通过[DescribeAutoSnapshotPolicies](https://cloud.tencent.com/document/api/582/80208) 查询获取
        :rtype: str
        """
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
    r"""UnbindAutoSnapshotPolicy返回参数结构体

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
        r"""快照策略ID
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

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
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class UpdateAutoSnapshotPolicyRequest(AbstractModel):
    r"""UpdateAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: 解绑的快照策略ID，可以通过[DescribeAutoSnapshotPolicies](https://cloud.tencent.com/document/api/582/80208) 查询获取
        :type AutoSnapshotPolicyId: str
        :param _PolicyName: 快照策略名称，不超过64个字符
        :type PolicyName: str
        :param _DayOfWeek: 快照定期备份，按照星期一到星期日。 1代表星期一，7代表星期日，与DayOfMonth，IntervalDays 三者选一个
        :type DayOfWeek: str
        :param _Hour: 快照定期备份在一天的哪一小时
        :type Hour: str
        :param _AliveDays: 快照保留天数
        :type AliveDays: int
        :param _IsActivated: 是否激活定期快照功能；1代表激活，0代表未激活
        :type IsActivated: int
        :param _DayOfMonth: 定期快照在每月的第几天创建快照，该参数与DayOfWeek,IntervalDays 三者选一
        :type DayOfMonth: str
        :param _IntervalDays: 间隔天数定期执行快照，该参数与DayOfWeek,DayOfMonth 三者选一
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
        r"""解绑的快照策略ID，可以通过[DescribeAutoSnapshotPolicies](https://cloud.tencent.com/document/api/582/80208) 查询获取
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def PolicyName(self):
        r"""快照策略名称，不超过64个字符
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def DayOfWeek(self):
        r"""快照定期备份，按照星期一到星期日。 1代表星期一，7代表星期日，与DayOfMonth，IntervalDays 三者选一个
        :rtype: str
        """
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def Hour(self):
        r"""快照定期备份在一天的哪一小时
        :rtype: str
        """
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def AliveDays(self):
        r"""快照保留天数
        :rtype: int
        """
        return self._AliveDays

    @AliveDays.setter
    def AliveDays(self, AliveDays):
        self._AliveDays = AliveDays

    @property
    def IsActivated(self):
        r"""是否激活定期快照功能；1代表激活，0代表未激活
        :rtype: int
        """
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def DayOfMonth(self):
        r"""定期快照在每月的第几天创建快照，该参数与DayOfWeek,IntervalDays 三者选一
        :rtype: str
        """
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        r"""间隔天数定期执行快照，该参数与DayOfWeek,DayOfMonth 三者选一
        :rtype: int
        """
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
    r"""UpdateAutoSnapshotPolicy返回参数结构体

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
        r"""快照策略ID
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

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
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class UpdateCfsFileSystemNameRequest(AbstractModel):
    r"""UpdateCfsFileSystemName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID,通过[查询文件系统接口](https://cloud.tencent.com/document/api/582/38170)获取
        :type FileSystemId: str
        :param _FsName: 用户自定义文件系统名称，64字节内的中文字母数字或者 _,-,与CreationToken 至少填一个
        :type FsName: str
        """
        self._FileSystemId = None
        self._FsName = None

    @property
    def FileSystemId(self):
        r"""文件系统 ID,通过[查询文件系统接口](https://cloud.tencent.com/document/api/582/38170)获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsName(self):
        r"""用户自定义文件系统名称，64字节内的中文字母数字或者 _,-,与CreationToken 至少填一个
        :rtype: str
        """
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
    r"""UpdateCfsFileSystemName返回参数结构体

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
        r"""用户自定义文件系统名称
        :rtype: str
        """
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsName(self):
        r"""用户自定义文件系统名称
        :rtype: str
        """
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

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
        self._CreationToken = params.get("CreationToken")
        self._FileSystemId = params.get("FileSystemId")
        self._FsName = params.get("FsName")
        self._RequestId = params.get("RequestId")


class UpdateCfsFileSystemPGroupRequest(AbstractModel):
    r"""UpdateCfsFileSystemPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :type PGroupId: str
        :param _FileSystemId: 文件系统 ID，通过[查询文件系统接口](https://cloud.tencent.com/document/api/582/38170)获取
        :type FileSystemId: str
        """
        self._PGroupId = None
        self._FileSystemId = None

    @property
    def PGroupId(self):
        r"""权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def FileSystemId(self):
        r"""文件系统 ID，通过[查询文件系统接口](https://cloud.tencent.com/document/api/582/38170)获取
        :rtype: str
        """
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
    r"""UpdateCfsFileSystemPGroup返回参数结构体

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
        r"""权限组 ID
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def FileSystemId(self):
        r"""文件系统 ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

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
        self._PGroupId = params.get("PGroupId")
        self._FileSystemId = params.get("FileSystemId")
        self._RequestId = params.get("RequestId")


class UpdateCfsFileSystemSizeLimitRequest(AbstractModel):
    r"""UpdateCfsFileSystemSizeLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FsLimit: 文件系统容量限制大小，输入范围0-1073741824, 单位为GB；其中输入值为0时，表示不限制文件系统容量。
        :type FsLimit: int
        :param _FileSystemId: 文件系统ID，目前仅支持标准型文件系统。该参数通过查询文件系统列表获取
        :type FileSystemId: str
        """
        self._FsLimit = None
        self._FileSystemId = None

    @property
    def FsLimit(self):
        r"""文件系统容量限制大小，输入范围0-1073741824, 单位为GB；其中输入值为0时，表示不限制文件系统容量。
        :rtype: int
        """
        return self._FsLimit

    @FsLimit.setter
    def FsLimit(self, FsLimit):
        self._FsLimit = FsLimit

    @property
    def FileSystemId(self):
        r"""文件系统ID，目前仅支持标准型文件系统。该参数通过查询文件系统列表获取
        :rtype: str
        """
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
    r"""UpdateCfsFileSystemSizeLimit返回参数结构体

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


class UpdateCfsPGroupRequest(AbstractModel):
    r"""UpdateCfsPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
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
        r"""权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        r"""权限组名称，1-64个字符且只能为中文，字母，数字，下划线或横线
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        r"""权限组描述信息，1-255个字符。 Name和Descinfo不能同时为空
        :rtype: str
        """
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
    r"""UpdateCfsPGroup返回参数结构体

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
        r"""权限组ID
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        r"""权限组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        r"""描述信息
        :rtype: str
        """
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo

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
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        self._RequestId = params.get("RequestId")


class UpdateCfsRuleRequest(AbstractModel):
    r"""UpdateCfsRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PGroupId: 权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :type PGroupId: str
        :param _RuleId: 规则 ID，可通过[DescribeCfsRules](https://cloud.tencent.com/document/api/582/38156)接口获取
        :type RuleId: str
        :param _AuthClientIp: 可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。
        :type AuthClientIp: str
        :param _RWPermission: 读写权限, 值为RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读
        :type RWPermission: str
        :param _UserPermission: 用户权限，值为all_squash、no_all_squash、root_squash、no_root_squash，默认值为root_squash
all_squash：所有访问用户（含 root 用户）都会被映射为匿名用户或用户组。
no_all_squash：所有访问用户（含 root 用户）均保持原有的 UID/GID 信息。
root_squash：将来访的 root 用户映射为匿名用户或用户组，非 root 用户保持原有的 UID/GID 信息。
no_root_squash：与 no_all_squash 效果一致，所有访问用户（含 root 用户）均保持原有的 UID/GID 信息

        :type UserPermission: str
        :param _Priority: 规则优先级，参数范围1-100。 其中 1 为最高，100为最低，默认值为100
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
        r"""权限组 ID，可通过[DescribeCfsPGroups接口](https://cloud.tencent.com/document/api/582/38157)获取
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def RuleId(self):
        r"""规则 ID，可通过[DescribeCfsRules](https://cloud.tencent.com/document/api/582/38156)接口获取
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AuthClientIp(self):
        r"""可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。
        :rtype: str
        """
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        r"""读写权限, 值为RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读
        :rtype: str
        """
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        r"""用户权限，值为all_squash、no_all_squash、root_squash、no_root_squash，默认值为root_squash
all_squash：所有访问用户（含 root 用户）都会被映射为匿名用户或用户组。
no_all_squash：所有访问用户（含 root 用户）均保持原有的 UID/GID 信息。
root_squash：将来访的 root 用户映射为匿名用户或用户组，非 root 用户保持原有的 UID/GID 信息。
no_root_squash：与 no_all_squash 效果一致，所有访问用户（含 root 用户）均保持原有的 UID/GID 信息

        :rtype: str
        """
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        r"""规则优先级，参数范围1-100。 其中 1 为最高，100为最低，默认值为100
        :rtype: int
        """
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
    r"""UpdateCfsRule返回参数结构体

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
        r"""权限组 ID
        :rtype: str
        """
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def RuleId(self):
        r"""规则 ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AuthClientIp(self):
        r"""允许访问的客户端 IP 或者 IP 段
        :rtype: str
        """
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        r"""读写权限
        :rtype: str
        """
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        r"""用户权限
        :rtype: str
        """
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        r"""优先级
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

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
        self._PGroupId = params.get("PGroupId")
        self._RuleId = params.get("RuleId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        self._Priority = params.get("Priority")
        self._RequestId = params.get("RequestId")


class UpdateCfsSnapshotAttributeRequest(AbstractModel):
    r"""UpdateCfsSnapshotAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照ID，可以通过[DescribeCfsSnapshots](https://cloud.tencent.com/document/api/582/80206) 查询获取
        :type SnapshotId: str
        :param _SnapshotName: 文件系统快照名称，与AliveDays 必须填一个，快照名称，支持不超过64字符长度，支持中文、数字、_、-
        :type SnapshotName: str
        :param _AliveDays: 文件系统快照保留天数，与SnapshotName必须填一个，如果原来是永久保留时间，不允许修改成短期有效期
        :type AliveDays: int
        """
        self._SnapshotId = None
        self._SnapshotName = None
        self._AliveDays = None

    @property
    def SnapshotId(self):
        r"""快照ID，可以通过[DescribeCfsSnapshots](https://cloud.tencent.com/document/api/582/80206) 查询获取
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotName(self):
        r"""文件系统快照名称，与AliveDays 必须填一个，快照名称，支持不超过64字符长度，支持中文、数字、_、-
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def AliveDays(self):
        r"""文件系统快照保留天数，与SnapshotName必须填一个，如果原来是永久保留时间，不允许修改成短期有效期
        :rtype: int
        """
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
    r"""UpdateCfsSnapshotAttribute返回参数结构体

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
        r"""文件系统快照ID
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

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
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class UpdateFileSystemBandwidthLimitRequest(AbstractModel):
    r"""UpdateFileSystemBandwidthLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统 ID,可通过[DescribeCfsFileSystems](https://cloud.tencent.com/document/api/582/38170)接口获取
        :type FileSystemId: str
        :param _BandwidthLimit: 文件系统带宽，仅吞吐型可填。单位MiB/s，最小为1GiB/s，最大200GiB/s。
        :type BandwidthLimit: int
        """
        self._FileSystemId = None
        self._BandwidthLimit = None

    @property
    def FileSystemId(self):
        r"""文件系统 ID,可通过[DescribeCfsFileSystems](https://cloud.tencent.com/document/api/582/38170)接口获取
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def BandwidthLimit(self):
        r"""文件系统带宽，仅吞吐型可填。单位MiB/s，最小为1GiB/s，最大200GiB/s。
        :rtype: int
        """
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
    r"""UpdateFileSystemBandwidthLimit返回参数结构体

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


class UserQuota(AbstractModel):
    r"""文件系统配额信息

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
        :type CapacityUsed: int
        :param _FileUsed: 文件使用个数，单位个
        :type FileUsed: int
        :param _DirectoryPath: 目录配额的目录绝对路径
注意：此字段可能返回 null，表示取不到有效值。
        :type DirectoryPath: str
        :param _Status: 配置规则状态，inavailable---配置中，available --已生效，deleting--删除中，deleted 已删除，failed--配置失败
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
        r"""指定配额类型，包括Uid、Gid、Dir
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserId(self):
        r"""UID/GID信息
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def CapacityHardLimit(self):
        r"""容量硬限制，单位GiB
        :rtype: int
        """
        return self._CapacityHardLimit

    @CapacityHardLimit.setter
    def CapacityHardLimit(self, CapacityHardLimit):
        self._CapacityHardLimit = CapacityHardLimit

    @property
    def FileHardLimit(self):
        r"""文件硬限制，单位个
        :rtype: int
        """
        return self._FileHardLimit

    @FileHardLimit.setter
    def FileHardLimit(self, FileHardLimit):
        self._FileHardLimit = FileHardLimit

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def CapacityUsed(self):
        r"""容量使用，单位GiB
        :rtype: int
        """
        return self._CapacityUsed

    @CapacityUsed.setter
    def CapacityUsed(self, CapacityUsed):
        self._CapacityUsed = CapacityUsed

    @property
    def FileUsed(self):
        r"""文件使用个数，单位个
        :rtype: int
        """
        return self._FileUsed

    @FileUsed.setter
    def FileUsed(self, FileUsed):
        self._FileUsed = FileUsed

    @property
    def DirectoryPath(self):
        r"""目录配额的目录绝对路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DirectoryPath

    @DirectoryPath.setter
    def DirectoryPath(self, DirectoryPath):
        self._DirectoryPath = DirectoryPath

    @property
    def Status(self):
        r"""配置规则状态，inavailable---配置中，available --已生效，deleting--删除中，deleted 已删除，failed--配置失败
        :rtype: str
        """
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
        