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


class DBInstanceDetail(AbstractModel):
    """DB实例详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: DB实例Id
        :type InstanceId: str
        :param _InstanceName: DB实例名称
        :type InstanceName: str
        :param _Status: DB实例状态,-1:已隔离, 0:创建中, 1:流程中, 2:运行中, 3:未初始化
        :type Status: int
        :param _StatusDesc: DB实例状态描述,-1:已隔离, 0:创建中, 1:流程中, 2:运行中, 3:未初始化
        :type StatusDesc: str
        :param _DbVersion: DB实例版本
        :type DbVersion: str
        :param _Vip: Vip信息
        :type Vip: str
        :param _Vport: Vip使用的端口号
        :type Vport: int
        :param _UniqueVpcId: 字符串型的私有网络ID
        :type UniqueVpcId: str
        :param _UniqueSubnetId: 字符串型的私有网络子网ID
        :type UniqueSubnetId: str
        :param _Shard: 是否为分布式版本,0:否,1:是
        :type Shard: int
        :param _NodeNum: DB实例节点数
        :type NodeNum: int
        :param _Cpu: CPU规格(单位:核数)
        :type Cpu: int
        :param _Memory: 内存规格(单位:GB)
        :type Memory: int
        :param _Disk: 磁盘规格(单位:GB)
        :type Disk: int
        :param _ShardNum: 分布式类型的实例的分片数
        :type ShardNum: int
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _DbHosts: Db所在主机列表, 格式: m1,s1|m2,s2
        :type DbHosts: str
        :param _HostRole: 主机角色, 1:主, 2:从, 3:主+从
        :type HostRole: int
        :param _DbEngine: DB引擎，MySQL,Percona,MariaDB
        :type DbEngine: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._StatusDesc = None
        self._DbVersion = None
        self._Vip = None
        self._Vport = None
        self._UniqueVpcId = None
        self._UniqueSubnetId = None
        self._Shard = None
        self._NodeNum = None
        self._Cpu = None
        self._Memory = None
        self._Disk = None
        self._ShardNum = None
        self._Region = None
        self._Zone = None
        self._DbHosts = None
        self._HostRole = None
        self._DbEngine = None
        self._CreateTime = None

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def UniqueVpcId(self):
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def Shard(self):
        return self._Shard

    @Shard.setter
    def Shard(self, Shard):
        self._Shard = Shard

    @property
    def NodeNum(self):
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Disk(self):
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def ShardNum(self):
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DbHosts(self):
        return self._DbHosts

    @DbHosts.setter
    def DbHosts(self, DbHosts):
        self._DbHosts = DbHosts

    @property
    def HostRole(self):
        return self._HostRole

    @HostRole.setter
    def HostRole(self, HostRole):
        self._HostRole = HostRole

    @property
    def DbEngine(self):
        return self._DbEngine

    @DbEngine.setter
    def DbEngine(self, DbEngine):
        self._DbEngine = DbEngine

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._DbVersion = params.get("DbVersion")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._UniqueVpcId = params.get("UniqueVpcId")
        self._UniqueSubnetId = params.get("UniqueSubnetId")
        self._Shard = params.get("Shard")
        self._NodeNum = params.get("NodeNum")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Disk = params.get("Disk")
        self._ShardNum = params.get("ShardNum")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._DbHosts = params.get("DbHosts")
        self._HostRole = params.get("HostRole")
        self._DbEngine = params.get("DbEngine")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param _HostId: 独享集群主机Id
        :type HostId: str
        :param _Limit: 分页返回数量
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _ShardType: 实例类型,0:mariadb, 1:tdsql
        :type ShardType: list of int
        """
        self._InstanceId = None
        self._HostId = None
        self._Limit = None
        self._Offset = None
        self._ShardType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def HostId(self):
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

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
    def ShardType(self):
        return self._ShardType

    @ShardType.setter
    def ShardType(self, ShardType):
        self._ShardType = ShardType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._HostId = params.get("HostId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ShardType = params.get("ShardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 独享集群内的DB实例列表
        :type Instances: list of DBInstanceDetail
        :param _TotalCount: 独享集群内的DB实例总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = DBInstanceDetail()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostListRequest(AbstractModel):
    """DescribeHostList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param _Limit: 分页返回数量
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _AssignStatus: 分配状态过滤，0-可分配，1-禁止分配
        :type AssignStatus: list of int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._AssignStatus = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def AssignStatus(self):
        return self._AssignStatus

    @AssignStatus.setter
    def AssignStatus(self, AssignStatus):
        self._AssignStatus = AssignStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AssignStatus = params.get("AssignStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostListResponse(AbstractModel):
    """DescribeHostList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 主机总数
        :type TotalCount: int
        :param _Hosts: 主机详情
        :type Hosts: list of HostDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Hosts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Hosts") is not None:
            self._Hosts = []
            for item in params.get("Hosts"):
                obj = HostDetail()
                obj._deserialize(item)
                self._Hosts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceDetail(AbstractModel):
    """独享集群详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param _InstanceName: 独享集群实例名称
        :type InstanceName: str
        :param _Region: 地域
        :type Region: str
        :param _ProductId: 产品ID, 0:CDB, 1:TDSQL
        :type ProductId: int
        :param _Type: 集群类型, 0:公有云, 1:金融围笼, 2:CDC集群
        :type Type: int
        :param _HostType: 主机类型, 0:物理机, 1:CVM机型, 2:CDC机型
        :type HostType: int
        :param _AutoRenewFlag: 自动续费标志, 0:未设置, 1:自动续费, 2:到期不续费
        :type AutoRenewFlag: int
        :param _Status: 集群状态
        :type Status: int
        :param _StatusDesc: 集群状态描述
        :type StatusDesc: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param _HostNum: 主机数
        :type HostNum: int
        :param _DbNum: DB实例数
        :type DbNum: int
        :param _AssignStrategy: 分配策略, 0:紧凑, 1:均匀
        :type AssignStrategy: int
        :param _CpuSpec: 总主机CPU(单位:核数)
        :type CpuSpec: int
        :param _CpuAssigned: 总已分配CPU(单位:核数)
        :type CpuAssigned: int
        :param _CpuAssignable: 总可分配CPU(单位:核数)
        :type CpuAssignable: int
        :param _MemorySpec: 总主机内存(单位:GB)
        :type MemorySpec: int
        :param _MemoryAssigned: 总已分配内存(单位:GB)
        :type MemoryAssigned: int
        :param _MemoryAssignable: 总可分配内存(单位:GB)
        :type MemoryAssignable: int
        :param _DiskSpec: 总机器磁盘(单位:GB)
        :type DiskSpec: int
        :param _DiskAssigned: 总已分配磁盘(单位:GB)
        :type DiskAssigned: int
        :param _DiskAssignable: 总可分配磁盘(单位:GB)
        :type DiskAssignable: int
        :param _Zone: 可用区
        :type Zone: str
        :param _FenceId: 金融围笼ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FenceId: str
        :param _ClusterId: 所属集群ID(默认集群为空)
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._ProductId = None
        self._Type = None
        self._HostType = None
        self._AutoRenewFlag = None
        self._Status = None
        self._StatusDesc = None
        self._CreateTime = None
        self._PeriodEndTime = None
        self._HostNum = None
        self._DbNum = None
        self._AssignStrategy = None
        self._CpuSpec = None
        self._CpuAssigned = None
        self._CpuAssignable = None
        self._MemorySpec = None
        self._MemoryAssigned = None
        self._MemoryAssignable = None
        self._DiskSpec = None
        self._DiskAssigned = None
        self._DiskAssignable = None
        self._Zone = None
        self._FenceId = None
        self._ClusterId = None

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
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def HostType(self):
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def HostNum(self):
        return self._HostNum

    @HostNum.setter
    def HostNum(self, HostNum):
        self._HostNum = HostNum

    @property
    def DbNum(self):
        return self._DbNum

    @DbNum.setter
    def DbNum(self, DbNum):
        self._DbNum = DbNum

    @property
    def AssignStrategy(self):
        return self._AssignStrategy

    @AssignStrategy.setter
    def AssignStrategy(self, AssignStrategy):
        self._AssignStrategy = AssignStrategy

    @property
    def CpuSpec(self):
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def CpuAssigned(self):
        return self._CpuAssigned

    @CpuAssigned.setter
    def CpuAssigned(self, CpuAssigned):
        self._CpuAssigned = CpuAssigned

    @property
    def CpuAssignable(self):
        return self._CpuAssignable

    @CpuAssignable.setter
    def CpuAssignable(self, CpuAssignable):
        self._CpuAssignable = CpuAssignable

    @property
    def MemorySpec(self):
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def MemoryAssigned(self):
        return self._MemoryAssigned

    @MemoryAssigned.setter
    def MemoryAssigned(self, MemoryAssigned):
        self._MemoryAssigned = MemoryAssigned

    @property
    def MemoryAssignable(self):
        return self._MemoryAssignable

    @MemoryAssignable.setter
    def MemoryAssignable(self, MemoryAssignable):
        self._MemoryAssignable = MemoryAssignable

    @property
    def DiskSpec(self):
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def DiskAssigned(self):
        return self._DiskAssigned

    @DiskAssigned.setter
    def DiskAssigned(self, DiskAssigned):
        self._DiskAssigned = DiskAssigned

    @property
    def DiskAssignable(self):
        return self._DiskAssignable

    @DiskAssignable.setter
    def DiskAssignable(self, DiskAssignable):
        self._DiskAssignable = DiskAssignable

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def FenceId(self):
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._ProductId = params.get("ProductId")
        self._Type = params.get("Type")
        self._HostType = params.get("HostType")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._HostNum = params.get("HostNum")
        self._DbNum = params.get("DbNum")
        self._AssignStrategy = params.get("AssignStrategy")
        self._CpuSpec = params.get("CpuSpec")
        self._CpuAssigned = params.get("CpuAssigned")
        self._CpuAssignable = params.get("CpuAssignable")
        self._MemorySpec = params.get("MemorySpec")
        self._MemoryAssigned = params.get("MemoryAssigned")
        self._MemoryAssignable = params.get("MemoryAssignable")
        self._DiskSpec = params.get("DiskSpec")
        self._DiskAssigned = params.get("DiskAssigned")
        self._DiskAssignable = params.get("DiskAssignable")
        self._Zone = params.get("Zone")
        self._FenceId = params.get("FenceId")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDetailRequest(AbstractModel):
    """DescribeInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDetailResponse(AbstractModel):
    """DescribeInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param _InstanceName: 独享集群实例名称
        :type InstanceName: str
        :param _Region: 地域
        :type Region: str
        :param _ProductId: 产品ID, 0:CDB, 1:TDSQL
        :type ProductId: int
        :param _Type: 集群类型, 0:公有云, 1:金融围笼
        :type Type: int
        :param _HostType: 主机类型, 0:物理机, 1:cvm本地盘, 2:cvm云盘
        :type HostType: int
        :param _AutoRenewFlag: 自动续费标志, 0:未设置, 1:自动续费, 2:到期不续费
        :type AutoRenewFlag: int
        :param _Status: 集群状态
        :type Status: int
        :param _StatusDesc: 集群状态描述
        :type StatusDesc: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param _HostNum: 主机数
        :type HostNum: int
        :param _DbNum: Db实例数
        :type DbNum: int
        :param _AssignStrategy: 分配策略, 0:紧凑, 1:均匀
        :type AssignStrategy: int
        :param _CpuSpec: 总主机CPU(单位:核)
        :type CpuSpec: int
        :param _CpuAssigned: 总已分配CPU(单位:核)
        :type CpuAssigned: int
        :param _CpuAssignable: 总可分配CPU(单位:核)
        :type CpuAssignable: int
        :param _MemorySpec: 总主机内存(单位:GB)
        :type MemorySpec: int
        :param _MemoryAssigned: 总已分配内存(单位:GB)
        :type MemoryAssigned: int
        :param _MemoryAssignable: 总可分配内存(单位:GB)
        :type MemoryAssignable: int
        :param _DiskSpec: 总机器磁盘(单位:GB)
        :type DiskSpec: int
        :param _DiskAssigned: 总已分配磁盘(单位:GB)
        :type DiskAssigned: int
        :param _DiskAssignable: 总可分配磁盘(单位:GB)
        :type DiskAssignable: int
        :param _Zone: 可用区
        :type Zone: str
        :param _FenceId: 金融围笼ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FenceId: str
        :param _ClusterId: 所属集群ID(默认集群为空)
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._ProductId = None
        self._Type = None
        self._HostType = None
        self._AutoRenewFlag = None
        self._Status = None
        self._StatusDesc = None
        self._CreateTime = None
        self._PeriodEndTime = None
        self._HostNum = None
        self._DbNum = None
        self._AssignStrategy = None
        self._CpuSpec = None
        self._CpuAssigned = None
        self._CpuAssignable = None
        self._MemorySpec = None
        self._MemoryAssigned = None
        self._MemoryAssignable = None
        self._DiskSpec = None
        self._DiskAssigned = None
        self._DiskAssignable = None
        self._Zone = None
        self._FenceId = None
        self._ClusterId = None
        self._RequestId = None

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
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def HostType(self):
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def HostNum(self):
        return self._HostNum

    @HostNum.setter
    def HostNum(self, HostNum):
        self._HostNum = HostNum

    @property
    def DbNum(self):
        return self._DbNum

    @DbNum.setter
    def DbNum(self, DbNum):
        self._DbNum = DbNum

    @property
    def AssignStrategy(self):
        return self._AssignStrategy

    @AssignStrategy.setter
    def AssignStrategy(self, AssignStrategy):
        self._AssignStrategy = AssignStrategy

    @property
    def CpuSpec(self):
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def CpuAssigned(self):
        return self._CpuAssigned

    @CpuAssigned.setter
    def CpuAssigned(self, CpuAssigned):
        self._CpuAssigned = CpuAssigned

    @property
    def CpuAssignable(self):
        return self._CpuAssignable

    @CpuAssignable.setter
    def CpuAssignable(self, CpuAssignable):
        self._CpuAssignable = CpuAssignable

    @property
    def MemorySpec(self):
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def MemoryAssigned(self):
        return self._MemoryAssigned

    @MemoryAssigned.setter
    def MemoryAssigned(self, MemoryAssigned):
        self._MemoryAssigned = MemoryAssigned

    @property
    def MemoryAssignable(self):
        return self._MemoryAssignable

    @MemoryAssignable.setter
    def MemoryAssignable(self, MemoryAssignable):
        self._MemoryAssignable = MemoryAssignable

    @property
    def DiskSpec(self):
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def DiskAssigned(self):
        return self._DiskAssigned

    @DiskAssigned.setter
    def DiskAssigned(self, DiskAssigned):
        self._DiskAssigned = DiskAssigned

    @property
    def DiskAssignable(self):
        return self._DiskAssignable

    @DiskAssignable.setter
    def DiskAssignable(self, DiskAssignable):
        self._DiskAssignable = DiskAssignable

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def FenceId(self):
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._ProductId = params.get("ProductId")
        self._Type = params.get("Type")
        self._HostType = params.get("HostType")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._HostNum = params.get("HostNum")
        self._DbNum = params.get("DbNum")
        self._AssignStrategy = params.get("AssignStrategy")
        self._CpuSpec = params.get("CpuSpec")
        self._CpuAssigned = params.get("CpuAssigned")
        self._CpuAssignable = params.get("CpuAssignable")
        self._MemorySpec = params.get("MemorySpec")
        self._MemoryAssigned = params.get("MemoryAssigned")
        self._MemoryAssignable = params.get("MemoryAssignable")
        self._DiskSpec = params.get("DiskSpec")
        self._DiskAssigned = params.get("DiskAssigned")
        self._DiskAssignable = params.get("DiskAssignable")
        self._Zone = params.get("Zone")
        self._FenceId = params.get("FenceId")
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class DescribeInstanceListRequest(AbstractModel):
    """DescribeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页返回数量
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _OrderBy: 排序字段，createTime,instancename两者之一
        :type OrderBy: str
        :param _SortBy: 排序规则，desc,asc两者之一
        :type SortBy: str
        :param _ProductId: 按产品过滤，0:CDB, 1:TDSQL
        :type ProductId: list of int
        :param _InstanceId: 按实例ID过滤
        :type InstanceId: list of str
        :param _InstanceName: 按实例名称过滤
        :type InstanceName: list of str
        :param _FenceId: 按金融围笼ID过滤
        :type FenceId: list of str
        :param _Status: 按实例状态过滤, -1:已隔离, 0:创建中, 1:运行中, 2:扩容中, 3:删除中
        :type Status: list of int
        :param _ClusterId: 按所属集群ID过滤
        :type ClusterId: list of str
        """
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._SortBy = None
        self._ProductId = None
        self._InstanceId = None
        self._InstanceName = None
        self._FenceId = None
        self._Status = None
        self._ClusterId = None

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def FenceId(self):
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

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


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._SortBy = params.get("SortBy")
        self._ProductId = params.get("ProductId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._FenceId = params.get("FenceId")
        self._Status = params.get("Status")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceListResponse(AbstractModel):
    """DescribeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 独享集群列表
        :type Instances: list of DescribeInstanceDetail
        :param _TotalCount: 独享集群实例总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = DescribeInstanceDetail()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceTypes: 集群类型: 0 一主一备, 1 一主两备...N-1 一主N备
        :type InstanceTypes: list of int
        :param _ProductIds: 产品ID:  0 MYSQL，1 TDSQL
        :type ProductIds: list of int
        :param _InstanceIds: 集群uuid: 如 dbdc-q810131s
        :type InstanceIds: list of str
        :param _FenceFlag: 是否按金融围笼标志搜索
        :type FenceFlag: bool
        :param _InstanceName: 按实例名字模糊匹配
        :type InstanceName: str
        :param _PageSize: 每页数目, 整型
        :type PageSize: int
        :param _PageNumber: 页码, 整型
        :type PageNumber: int
        :param _OrderBy: 排序字段，枚举：createtime,groupname
        :type OrderBy: str
        :param _OrderByType: 排序方式: asc升序, desc降序
        :type OrderByType: str
        :param _InstanceStatus: 集群状态: -2 已删除, -1 已隔离, 0 创建中, 1 运行中, 2 扩容中, 3 删除中
        :type InstanceStatus: int
        """
        self._InstanceTypes = None
        self._ProductIds = None
        self._InstanceIds = None
        self._FenceFlag = None
        self._InstanceName = None
        self._PageSize = None
        self._PageNumber = None
        self._OrderBy = None
        self._OrderByType = None
        self._InstanceStatus = None

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def ProductIds(self):
        return self._ProductIds

    @ProductIds.setter
    def ProductIds(self, ProductIds):
        self._ProductIds = ProductIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def FenceFlag(self):
        return self._FenceFlag

    @FenceFlag.setter
    def FenceFlag(self, FenceFlag):
        self._FenceFlag = FenceFlag

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus


    def _deserialize(self, params):
        self._InstanceTypes = params.get("InstanceTypes")
        self._ProductIds = params.get("ProductIds")
        self._InstanceIds = params.get("InstanceIds")
        self._FenceFlag = params.get("FenceFlag")
        self._InstanceName = params.get("InstanceName")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._InstanceStatus = params.get("InstanceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 集群数量
        :type TotalCount: int
        :param _Instances: 集群扩展信息
        :type Instances: list of InstanceExpand
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = InstanceExpand()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    """设备信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: int
        :param _DeviceNo: 设备No
        :type DeviceNo: str
        :param _DevClass: 设备类型
        :type DevClass: str
        :param _MaxMemory: 设备总内存，单位GB
        :type MaxMemory: float
        :param _MaxDisk: 设备总磁盘，单位GB
        :type MaxDisk: float
        :param _RestMemory: 设备剩余内存，单位GB
        :type RestMemory: float
        :param _RestDisk: 设备剩余磁盘，单位GB
        :type RestDisk: float
        :param _RawDeviceNum: 设备机器个数
        :type RawDeviceNum: int
        :param _InstanceNum: 数据库实例个数
        :type InstanceNum: int
        """
        self._DeviceId = None
        self._DeviceNo = None
        self._DevClass = None
        self._MaxMemory = None
        self._MaxDisk = None
        self._RestMemory = None
        self._RestDisk = None
        self._RawDeviceNum = None
        self._InstanceNum = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceNo(self):
        return self._DeviceNo

    @DeviceNo.setter
    def DeviceNo(self, DeviceNo):
        self._DeviceNo = DeviceNo

    @property
    def DevClass(self):
        return self._DevClass

    @DevClass.setter
    def DevClass(self, DevClass):
        self._DevClass = DevClass

    @property
    def MaxMemory(self):
        return self._MaxMemory

    @MaxMemory.setter
    def MaxMemory(self, MaxMemory):
        self._MaxMemory = MaxMemory

    @property
    def MaxDisk(self):
        return self._MaxDisk

    @MaxDisk.setter
    def MaxDisk(self, MaxDisk):
        self._MaxDisk = MaxDisk

    @property
    def RestMemory(self):
        return self._RestMemory

    @RestMemory.setter
    def RestMemory(self, RestMemory):
        self._RestMemory = RestMemory

    @property
    def RestDisk(self):
        return self._RestDisk

    @RestDisk.setter
    def RestDisk(self, RestDisk):
        self._RestDisk = RestDisk

    @property
    def RawDeviceNum(self):
        return self._RawDeviceNum

    @RawDeviceNum.setter
    def RawDeviceNum(self, RawDeviceNum):
        self._RawDeviceNum = RawDeviceNum

    @property
    def InstanceNum(self):
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceNo = params.get("DeviceNo")
        self._DevClass = params.get("DevClass")
        self._MaxMemory = params.get("MaxMemory")
        self._MaxDisk = params.get("MaxDisk")
        self._RestMemory = params.get("RestMemory")
        self._RestDisk = params.get("RestDisk")
        self._RawDeviceNum = params.get("RawDeviceNum")
        self._InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostDetail(AbstractModel):
    """主机详情

    """

    def __init__(self):
        r"""
        :param _HostId: 主机Id
        :type HostId: str
        :param _HostName: 主机名称
        :type HostName: str
        :param _Zone: 可用区
        :type Zone: str
        :param _Status: 主机状态
        :type Status: int
        :param _AssignStatus: 分配DB实例状态,0:可分配,1:不可分配
        :type AssignStatus: int
        :param _HostType: 主机类型, 0:物理机, 1:cvm本地盘, 2:cvm云盘
        :type HostType: int
        :param _DbNum: DB实例数
        :type DbNum: int
        :param _CpuSpec: 主机CPU(单位:核数)
        :type CpuSpec: int
        :param _CpuAssigned: 已分配CPU(单位:核数)
        :type CpuAssigned: int
        :param _CpuAssignable: 可分配CPU(单位:核数)
        :type CpuAssignable: int
        :param _MemorySpec: 主机内存(单位:GB)
        :type MemorySpec: int
        :param _MemoryAssigned: 已分配内存(单位:GB)
        :type MemoryAssigned: int
        :param _MemoryAssignable: 可分配内存(单位:GB)
        :type MemoryAssignable: int
        :param _DiskSpec: 主机磁盘(单位:GB)
        :type DiskSpec: int
        :param _DiskAssigned: 已分配磁盘(单位:GB)
        :type DiskAssigned: int
        :param _DiskAssignable: 可分配磁盘(GB)
        :type DiskAssignable: int
        :param _CpuRatio: CPU分配比
        :type CpuRatio: float
        :param _MemoryRatio: 内存分配比
        :type MemoryRatio: float
        :param _DiskRatio: 磁盘分配比
        :type DiskRatio: float
        :param _MachineName: 机型名称
        :type MachineName: str
        :param _MachineType: 机型类别
        :type MachineType: str
        :param _PidTag: 计费标签
        :type PidTag: str
        :param _Pid: 计费ID
        :type Pid: int
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        """
        self._HostId = None
        self._HostName = None
        self._Zone = None
        self._Status = None
        self._AssignStatus = None
        self._HostType = None
        self._DbNum = None
        self._CpuSpec = None
        self._CpuAssigned = None
        self._CpuAssignable = None
        self._MemorySpec = None
        self._MemoryAssigned = None
        self._MemoryAssignable = None
        self._DiskSpec = None
        self._DiskAssigned = None
        self._DiskAssignable = None
        self._CpuRatio = None
        self._MemoryRatio = None
        self._DiskRatio = None
        self._MachineName = None
        self._MachineType = None
        self._PidTag = None
        self._Pid = None
        self._InstanceId = None

    @property
    def HostId(self):
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AssignStatus(self):
        return self._AssignStatus

    @AssignStatus.setter
    def AssignStatus(self, AssignStatus):
        self._AssignStatus = AssignStatus

    @property
    def HostType(self):
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def DbNum(self):
        return self._DbNum

    @DbNum.setter
    def DbNum(self, DbNum):
        self._DbNum = DbNum

    @property
    def CpuSpec(self):
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def CpuAssigned(self):
        return self._CpuAssigned

    @CpuAssigned.setter
    def CpuAssigned(self, CpuAssigned):
        self._CpuAssigned = CpuAssigned

    @property
    def CpuAssignable(self):
        return self._CpuAssignable

    @CpuAssignable.setter
    def CpuAssignable(self, CpuAssignable):
        self._CpuAssignable = CpuAssignable

    @property
    def MemorySpec(self):
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def MemoryAssigned(self):
        return self._MemoryAssigned

    @MemoryAssigned.setter
    def MemoryAssigned(self, MemoryAssigned):
        self._MemoryAssigned = MemoryAssigned

    @property
    def MemoryAssignable(self):
        return self._MemoryAssignable

    @MemoryAssignable.setter
    def MemoryAssignable(self, MemoryAssignable):
        self._MemoryAssignable = MemoryAssignable

    @property
    def DiskSpec(self):
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def DiskAssigned(self):
        return self._DiskAssigned

    @DiskAssigned.setter
    def DiskAssigned(self, DiskAssigned):
        self._DiskAssigned = DiskAssigned

    @property
    def DiskAssignable(self):
        return self._DiskAssignable

    @DiskAssignable.setter
    def DiskAssignable(self, DiskAssignable):
        self._DiskAssignable = DiskAssignable

    @property
    def CpuRatio(self):
        return self._CpuRatio

    @CpuRatio.setter
    def CpuRatio(self, CpuRatio):
        self._CpuRatio = CpuRatio

    @property
    def MemoryRatio(self):
        return self._MemoryRatio

    @MemoryRatio.setter
    def MemoryRatio(self, MemoryRatio):
        self._MemoryRatio = MemoryRatio

    @property
    def DiskRatio(self):
        return self._DiskRatio

    @DiskRatio.setter
    def DiskRatio(self, DiskRatio):
        self._DiskRatio = DiskRatio

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def PidTag(self):
        return self._PidTag

    @PidTag.setter
    def PidTag(self, PidTag):
        self._PidTag = PidTag

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._HostId = params.get("HostId")
        self._HostName = params.get("HostName")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        self._AssignStatus = params.get("AssignStatus")
        self._HostType = params.get("HostType")
        self._DbNum = params.get("DbNum")
        self._CpuSpec = params.get("CpuSpec")
        self._CpuAssigned = params.get("CpuAssigned")
        self._CpuAssignable = params.get("CpuAssignable")
        self._MemorySpec = params.get("MemorySpec")
        self._MemoryAssigned = params.get("MemoryAssigned")
        self._MemoryAssignable = params.get("MemoryAssignable")
        self._DiskSpec = params.get("DiskSpec")
        self._DiskAssigned = params.get("DiskAssigned")
        self._DiskAssignable = params.get("DiskAssignable")
        self._CpuRatio = params.get("CpuRatio")
        self._MemoryRatio = params.get("MemoryRatio")
        self._DiskRatio = params.get("DiskRatio")
        self._MachineName = params.get("MachineName")
        self._MachineType = params.get("MachineType")
        self._PidTag = params.get("PidTag")
        self._Pid = params.get("Pid")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """集群容量信息。

    """

    def __init__(self):
        r"""
        :param _Status: 集群状态，0：运行中，1：不在运行
        :type Status: int
        :param _ReadWriteTotalLeaveMemory: 读写集群剩余内存容量，单位GB
        :type ReadWriteTotalLeaveMemory: float
        :param _ReadWriteTotalLeaveDisk: 读写集群剩余磁盘容量，单位GB
        :type ReadWriteTotalLeaveDisk: float
        :param _ReadWriteTotalMemory: 读写集群总内存容量，单位GB
        :type ReadWriteTotalMemory: float
        :param _ReadWriteTotalDisk: 读写集群总磁盘容量，单位GB
        :type ReadWriteTotalDisk: float
        :param _ReadOnlyTotalLeaveMemory: 只读集群剩余内存容量，单位GB
        :type ReadOnlyTotalLeaveMemory: float
        :param _ReadOnlyTotalLeaveDisk: 只读集群剩余磁盘容量，单位GB
        :type ReadOnlyTotalLeaveDisk: float
        :param _ReadOnlyTotalMemory: 只读集群总内存容量，单位GB
        :type ReadOnlyTotalMemory: float
        :param _ReadOnlyTotalDisk: 只读集群总磁盘容量，单位GB
        :type ReadOnlyTotalDisk: float
        :param _InstanceDeviceInfos: 集群设备详情
        :type InstanceDeviceInfos: list of InstanceDeviceInfo
        """
        self._Status = None
        self._ReadWriteTotalLeaveMemory = None
        self._ReadWriteTotalLeaveDisk = None
        self._ReadWriteTotalMemory = None
        self._ReadWriteTotalDisk = None
        self._ReadOnlyTotalLeaveMemory = None
        self._ReadOnlyTotalLeaveDisk = None
        self._ReadOnlyTotalMemory = None
        self._ReadOnlyTotalDisk = None
        self._InstanceDeviceInfos = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ReadWriteTotalLeaveMemory(self):
        return self._ReadWriteTotalLeaveMemory

    @ReadWriteTotalLeaveMemory.setter
    def ReadWriteTotalLeaveMemory(self, ReadWriteTotalLeaveMemory):
        self._ReadWriteTotalLeaveMemory = ReadWriteTotalLeaveMemory

    @property
    def ReadWriteTotalLeaveDisk(self):
        return self._ReadWriteTotalLeaveDisk

    @ReadWriteTotalLeaveDisk.setter
    def ReadWriteTotalLeaveDisk(self, ReadWriteTotalLeaveDisk):
        self._ReadWriteTotalLeaveDisk = ReadWriteTotalLeaveDisk

    @property
    def ReadWriteTotalMemory(self):
        return self._ReadWriteTotalMemory

    @ReadWriteTotalMemory.setter
    def ReadWriteTotalMemory(self, ReadWriteTotalMemory):
        self._ReadWriteTotalMemory = ReadWriteTotalMemory

    @property
    def ReadWriteTotalDisk(self):
        return self._ReadWriteTotalDisk

    @ReadWriteTotalDisk.setter
    def ReadWriteTotalDisk(self, ReadWriteTotalDisk):
        self._ReadWriteTotalDisk = ReadWriteTotalDisk

    @property
    def ReadOnlyTotalLeaveMemory(self):
        return self._ReadOnlyTotalLeaveMemory

    @ReadOnlyTotalLeaveMemory.setter
    def ReadOnlyTotalLeaveMemory(self, ReadOnlyTotalLeaveMemory):
        self._ReadOnlyTotalLeaveMemory = ReadOnlyTotalLeaveMemory

    @property
    def ReadOnlyTotalLeaveDisk(self):
        return self._ReadOnlyTotalLeaveDisk

    @ReadOnlyTotalLeaveDisk.setter
    def ReadOnlyTotalLeaveDisk(self, ReadOnlyTotalLeaveDisk):
        self._ReadOnlyTotalLeaveDisk = ReadOnlyTotalLeaveDisk

    @property
    def ReadOnlyTotalMemory(self):
        return self._ReadOnlyTotalMemory

    @ReadOnlyTotalMemory.setter
    def ReadOnlyTotalMemory(self, ReadOnlyTotalMemory):
        self._ReadOnlyTotalMemory = ReadOnlyTotalMemory

    @property
    def ReadOnlyTotalDisk(self):
        return self._ReadOnlyTotalDisk

    @ReadOnlyTotalDisk.setter
    def ReadOnlyTotalDisk(self, ReadOnlyTotalDisk):
        self._ReadOnlyTotalDisk = ReadOnlyTotalDisk

    @property
    def InstanceDeviceInfos(self):
        return self._InstanceDeviceInfos

    @InstanceDeviceInfos.setter
    def InstanceDeviceInfos(self, InstanceDeviceInfos):
        self._InstanceDeviceInfos = InstanceDeviceInfos


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ReadWriteTotalLeaveMemory = params.get("ReadWriteTotalLeaveMemory")
        self._ReadWriteTotalLeaveDisk = params.get("ReadWriteTotalLeaveDisk")
        self._ReadWriteTotalMemory = params.get("ReadWriteTotalMemory")
        self._ReadWriteTotalDisk = params.get("ReadWriteTotalDisk")
        self._ReadOnlyTotalLeaveMemory = params.get("ReadOnlyTotalLeaveMemory")
        self._ReadOnlyTotalLeaveDisk = params.get("ReadOnlyTotalLeaveDisk")
        self._ReadOnlyTotalMemory = params.get("ReadOnlyTotalMemory")
        self._ReadOnlyTotalDisk = params.get("ReadOnlyTotalDisk")
        if params.get("InstanceDeviceInfos") is not None:
            self._InstanceDeviceInfos = []
            for item in params.get("InstanceDeviceInfos"):
                obj = InstanceDeviceInfo()
                obj._deserialize(item)
                self._InstanceDeviceInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDeviceInfo(AbstractModel):
    """集群设备组信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _ReadWriteDevice: 读写设备组
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadWriteDevice: list of DeviceInfo
        :param _ReadOnlyDevice: 只读设备组
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnlyDevice: list of DeviceInfo
        :param _FreeDevice: 空闲设备组
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeDevice: list of DeviceInfo
        """
        self._InstanceId = None
        self._ReadWriteDevice = None
        self._ReadOnlyDevice = None
        self._FreeDevice = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadWriteDevice(self):
        return self._ReadWriteDevice

    @ReadWriteDevice.setter
    def ReadWriteDevice(self, ReadWriteDevice):
        self._ReadWriteDevice = ReadWriteDevice

    @property
    def ReadOnlyDevice(self):
        return self._ReadOnlyDevice

    @ReadOnlyDevice.setter
    def ReadOnlyDevice(self, ReadOnlyDevice):
        self._ReadOnlyDevice = ReadOnlyDevice

    @property
    def FreeDevice(self):
        return self._FreeDevice

    @FreeDevice.setter
    def FreeDevice(self, FreeDevice):
        self._FreeDevice = FreeDevice


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ReadWriteDevice") is not None:
            self._ReadWriteDevice = []
            for item in params.get("ReadWriteDevice"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._ReadWriteDevice.append(obj)
        if params.get("ReadOnlyDevice") is not None:
            self._ReadOnlyDevice = []
            for item in params.get("ReadOnlyDevice"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._ReadOnlyDevice.append(obj)
        if params.get("FreeDevice") is not None:
            self._FreeDevice = []
            for item in params.get("FreeDevice"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._FreeDevice.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExpand(AbstractModel):
    """集群扩展信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _InstanceName: 集群名称
        :type InstanceName: str
        :param _AppId: 用户ID
        :type AppId: int
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _InstanceType: 集群类型： 0：一主一备，1：一主两备
        :type InstanceType: int
        :param _InstanceStatus: 集群状态: 0 集群创建中, 1 集群有效, 2 集群扩容中, 3 集群删除中, 4 集群缩容中 -1 集群已隔离 -2 集群已删除
        :type InstanceStatus: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AutoRenewFlag: 实例自动续费标识： 0正常续费 1自动续费 2到期不续费
        :type AutoRenewFlag: int
        :param _Machine: 机型
        :type Machine: str
        :param _PeriodEndTime: 过期时间
        :type PeriodEndTime: str
        :param _InstanceDetail: 集群信息
        :type InstanceDetail: :class:`tencentcloud.dbdc.v20201029.models.InstanceDetail`
        :param _Pid: 计费侧的产品ID
        :type Pid: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Region = None
        self._Zone = None
        self._InstanceType = None
        self._InstanceStatus = None
        self._CreateTime = None
        self._AutoRenewFlag = None
        self._Machine = None
        self._PeriodEndTime = None
        self._InstanceDetail = None
        self._Pid = None

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
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Machine(self):
        return self._Machine

    @Machine.setter
    def Machine(self, Machine):
        self._Machine = Machine

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def InstanceDetail(self):
        return self._InstanceDetail

    @InstanceDetail.setter
    def InstanceDetail(self, InstanceDetail):
        self._InstanceDetail = InstanceDetail

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatus = params.get("InstanceStatus")
        self._CreateTime = params.get("CreateTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Machine = params.get("Machine")
        self._PeriodEndTime = params.get("PeriodEndTime")
        if params.get("InstanceDetail") is not None:
            self._InstanceDetail = InstanceDetail()
            self._InstanceDetail._deserialize(params.get("InstanceDetail"))
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNameRequest(AbstractModel):
    """ModifyInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param _InstanceName: 独享集群实例名称
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNameResponse(AbstractModel):
    """ModifyInstanceName返回参数结构体

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