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
        :param InstanceId: DB实例Id
        :type InstanceId: str
        :param InstanceName: DB实例名称
        :type InstanceName: str
        :param Status: DB实例状态,-1:已隔离, 0:创建中, 1:流程中, 2:运行中, 3:未初始化
        :type Status: int
        :param StatusDesc: DB实例状态描述,-1:已隔离, 0:创建中, 1:流程中, 2:运行中, 3:未初始化
        :type StatusDesc: str
        :param DbVersion: DB实例版本
        :type DbVersion: str
        :param Vip: Vip信息
        :type Vip: str
        :param Vport: Vip使用的端口号
        :type Vport: int
        :param UniqueVpcId: 字符串型的私有网络ID
        :type UniqueVpcId: str
        :param UniqueSubnetId: 字符串型的私有网络子网ID
        :type UniqueSubnetId: str
        :param Shard: 是否为分布式版本,0:否,1:是
        :type Shard: int
        :param NodeNum: DB实例节点数
        :type NodeNum: int
        :param Cpu: CPU规格(单位:核数)
        :type Cpu: int
        :param Memory: 内存规格(单位:GB)
        :type Memory: int
        :param Disk: 磁盘规格(单位:GB)
        :type Disk: int
        :param ShardNum: 分布式类型的实例的分片数
        :type ShardNum: int
        :param Zone: 可用区
        :type Zone: str
        :param DbHosts: Db所在主机列表, 格式: m1,s1|m2,s2
        :type DbHosts: str
        :param HostRole: 主机角色, 1:主, 2:从, 3:主+从
        :type HostRole: int
        :param DbEngine: DB引擎，MySQL,Percona,MariaDB
        :type DbEngine: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Status = None
        self.StatusDesc = None
        self.DbVersion = None
        self.Vip = None
        self.Vport = None
        self.UniqueVpcId = None
        self.UniqueSubnetId = None
        self.Shard = None
        self.NodeNum = None
        self.Cpu = None
        self.Memory = None
        self.Disk = None
        self.ShardNum = None
        self.Zone = None
        self.DbHosts = None
        self.HostRole = None
        self.DbEngine = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.DbVersion = params.get("DbVersion")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.UniqueVpcId = params.get("UniqueVpcId")
        self.UniqueSubnetId = params.get("UniqueSubnetId")
        self.Shard = params.get("Shard")
        self.NodeNum = params.get("NodeNum")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Disk = params.get("Disk")
        self.ShardNum = params.get("ShardNum")
        self.Zone = params.get("Zone")
        self.DbHosts = params.get("DbHosts")
        self.HostRole = params.get("HostRole")
        self.DbEngine = params.get("DbEngine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param HostId: 独享集群主机Id
        :type HostId: str
        :param Limit: 分页返回数量
        :type Limit: int
        :param Offset: 分页偏移量
        :type Offset: int
        :param ShardType: 实例类型,0:mariadb, 1:tdsql
        :type ShardType: list of int
        """
        self.InstanceId = None
        self.HostId = None
        self.Limit = None
        self.Offset = None
        self.ShardType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.HostId = params.get("HostId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ShardType = params.get("ShardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Instances: 独享集群内的DB实例列表
        :type Instances: list of DBInstanceDetail
        :param TotalCount: 独享集群内的DB实例总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Instances = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = DBInstanceDetail()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstanceDetail(AbstractModel):
    """独享集群详情

    """

    def __init__(self):
        r"""
        :param InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param InstanceName: 独享集群实例名称
        :type InstanceName: str
        :param Region: 地域
        :type Region: str
        :param ProductId: 产品ID, 0:CDB, 1:TDSQL
        :type ProductId: int
        :param Type: 集群类型, 0:公有云, 1:金融围笼
        :type Type: int
        :param HostType: 主机类型, 0:物理机, 1:cvm本地盘, 2:cvm云盘
        :type HostType: int
        :param AutoRenewFlag: 自动续费标志, 0:未设置, 1:自动续费, 2:到期不续费
        :type AutoRenewFlag: int
        :param Status: 集群状态
        :type Status: int
        :param StatusDesc: 集群状态描述
        :type StatusDesc: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param HostNum: 主机数
        :type HostNum: int
        :param DbNum: DB实例数
        :type DbNum: int
        :param AssignStrategy: 分配策略, 0:紧凑, 1:均匀
        :type AssignStrategy: int
        :param CpuSpec: 总主机CPU(单位:核数)
        :type CpuSpec: int
        :param CpuAssigned: 总已分配CPU(单位:核数)
        :type CpuAssigned: int
        :param CpuAssignable: 总可分配CPU(单位:核数)
        :type CpuAssignable: int
        :param MemorySpec: 总主机内存(单位:GB)
        :type MemorySpec: int
        :param MemoryAssigned: 总已分配内存(单位:GB)
        :type MemoryAssigned: int
        :param MemoryAssignable: 总可分配内存(单位:GB)
        :type MemoryAssignable: int
        :param DiskSpec: 总机器磁盘(单位:GB)
        :type DiskSpec: int
        :param DiskAssigned: 总已分配磁盘(单位:GB)
        :type DiskAssigned: int
        :param DiskAssignable: 总可分配磁盘(单位:GB)
        :type DiskAssignable: int
        :param Zone: 可用区
        :type Zone: str
        :param FenceId: 围笼ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FenceId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.ProductId = None
        self.Type = None
        self.HostType = None
        self.AutoRenewFlag = None
        self.Status = None
        self.StatusDesc = None
        self.CreateTime = None
        self.PeriodEndTime = None
        self.HostNum = None
        self.DbNum = None
        self.AssignStrategy = None
        self.CpuSpec = None
        self.CpuAssigned = None
        self.CpuAssignable = None
        self.MemorySpec = None
        self.MemoryAssigned = None
        self.MemoryAssignable = None
        self.DiskSpec = None
        self.DiskAssigned = None
        self.DiskAssignable = None
        self.Zone = None
        self.FenceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.ProductId = params.get("ProductId")
        self.Type = params.get("Type")
        self.HostType = params.get("HostType")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.CreateTime = params.get("CreateTime")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.HostNum = params.get("HostNum")
        self.DbNum = params.get("DbNum")
        self.AssignStrategy = params.get("AssignStrategy")
        self.CpuSpec = params.get("CpuSpec")
        self.CpuAssigned = params.get("CpuAssigned")
        self.CpuAssignable = params.get("CpuAssignable")
        self.MemorySpec = params.get("MemorySpec")
        self.MemoryAssigned = params.get("MemoryAssigned")
        self.MemoryAssignable = params.get("MemoryAssignable")
        self.DiskSpec = params.get("DiskSpec")
        self.DiskAssigned = params.get("DiskAssigned")
        self.DiskAssignable = params.get("DiskAssignable")
        self.Zone = params.get("Zone")
        self.FenceId = params.get("FenceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDetailRequest(AbstractModel):
    """DescribeInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 独享集群实例Id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDetailResponse(AbstractModel):
    """DescribeInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param InstanceName: 独享集群实例名称
        :type InstanceName: str
        :param Region: 地域
        :type Region: str
        :param ProductId: 产品ID, 0:CDB, 1:TDSQL
        :type ProductId: int
        :param Type: 集群类型, 0:公有云, 1:金融围笼
        :type Type: int
        :param HostType: 主机类型, 0:物理机, 1:cvm本地盘, 2:cvm云盘
        :type HostType: int
        :param AutoRenewFlag: 自动续费标志, 0:未设置, 1:自动续费, 2:到期不续费
        :type AutoRenewFlag: int
        :param Status: 集群状态
        :type Status: int
        :param StatusDesc: 集群状态描述
        :type StatusDesc: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param HostNum: 主机数
        :type HostNum: int
        :param DbNum: Db实例数
        :type DbNum: int
        :param AssignStrategy: 分配策略, 0:紧凑, 1:均匀
        :type AssignStrategy: int
        :param CpuSpec: 总主机CPU(单位:核)
        :type CpuSpec: int
        :param CpuAssigned: 总已分配CPU(单位:核)
        :type CpuAssigned: int
        :param CpuAssignable: 总可分配CPU(单位:核)
        :type CpuAssignable: int
        :param MemorySpec: 总主机内存(单位:GB)
        :type MemorySpec: int
        :param MemoryAssigned: 总已分配内存(单位:GB)
        :type MemoryAssigned: int
        :param MemoryAssignable: 总可分配内存(单位:GB)
        :type MemoryAssignable: int
        :param DiskSpec: 总机器磁盘(单位:GB)
        :type DiskSpec: int
        :param DiskAssigned: 总已分配磁盘(单位:GB)
        :type DiskAssigned: int
        :param DiskAssignable: 总可分配磁盘(单位:GB)
        :type DiskAssignable: int
        :param Zone: 可用区
        :type Zone: str
        :param FenceId: 围笼ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FenceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.ProductId = None
        self.Type = None
        self.HostType = None
        self.AutoRenewFlag = None
        self.Status = None
        self.StatusDesc = None
        self.CreateTime = None
        self.PeriodEndTime = None
        self.HostNum = None
        self.DbNum = None
        self.AssignStrategy = None
        self.CpuSpec = None
        self.CpuAssigned = None
        self.CpuAssignable = None
        self.MemorySpec = None
        self.MemoryAssigned = None
        self.MemoryAssignable = None
        self.DiskSpec = None
        self.DiskAssigned = None
        self.DiskAssignable = None
        self.Zone = None
        self.FenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.ProductId = params.get("ProductId")
        self.Type = params.get("Type")
        self.HostType = params.get("HostType")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.CreateTime = params.get("CreateTime")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.HostNum = params.get("HostNum")
        self.DbNum = params.get("DbNum")
        self.AssignStrategy = params.get("AssignStrategy")
        self.CpuSpec = params.get("CpuSpec")
        self.CpuAssigned = params.get("CpuAssigned")
        self.CpuAssignable = params.get("CpuAssignable")
        self.MemorySpec = params.get("MemorySpec")
        self.MemoryAssigned = params.get("MemoryAssigned")
        self.MemoryAssignable = params.get("MemoryAssignable")
        self.DiskSpec = params.get("DiskSpec")
        self.DiskAssigned = params.get("DiskAssigned")
        self.DiskAssignable = params.get("DiskAssignable")
        self.Zone = params.get("Zone")
        self.FenceId = params.get("FenceId")
        self.RequestId = params.get("RequestId")


class DescribeInstanceListRequest(AbstractModel):
    """DescribeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页返回数量
        :type Limit: int
        :param Offset: 分页偏移量
        :type Offset: int
        :param OrderBy: 排序字段，createTime,instancename两者之一
        :type OrderBy: str
        :param SortBy: 排序规则，desc,asc两者之一
        :type SortBy: str
        :param ProductId: 按产品过滤，0:CDB, 1:TDSQL
        :type ProductId: list of int
        :param InstanceId: 按实例ID过滤
        :type InstanceId: list of str
        :param InstanceName: 按实例名称过滤
        :type InstanceName: list of str
        :param FenceId: 按金融围笼ID过滤
        :type FenceId: list of str
        :param Status: 按实例状态过滤, -1:已隔离, 0:创建中, 1:运行中, 2:扩容中, 3:删除中
        :type Status: list of int
        """
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.SortBy = None
        self.ProductId = None
        self.InstanceId = None
        self.InstanceName = None
        self.FenceId = None
        self.Status = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.SortBy = params.get("SortBy")
        self.ProductId = params.get("ProductId")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.FenceId = params.get("FenceId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceListResponse(AbstractModel):
    """DescribeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Instances: 独享集群列表
        :type Instances: list of DescribeInstanceDetail
        :param TotalCount: 独享集群实例总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Instances = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = DescribeInstanceDetail()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceTypes: 集群类型: 0 一主一备, 1 一主两备...N-1 一主N备
        :type InstanceTypes: list of int
        :param ProductIds: 产品ID:  0 MYSQL，1 TDSQL
        :type ProductIds: list of int
        :param InstanceIds: 集群uuid: 如 dbdc-q810131s
        :type InstanceIds: list of str
        :param FenceFlag: 是否按金融围笼标志搜索
        :type FenceFlag: bool
        :param InstanceName: 按实例名字模糊匹配
        :type InstanceName: str
        :param PageSize: 每页数目, 整型
        :type PageSize: int
        :param PageNumber: 页码, 整型
        :type PageNumber: int
        :param OrderBy: 排序字段，枚举：createtime,groupname
        :type OrderBy: str
        :param OrderByType: 排序方式: asc升序, desc降序
        :type OrderByType: str
        :param InstanceStatus: 集群状态: -2 已删除, -1 已隔离, 0 创建中, 1 运行中, 2 扩容中, 3 删除中
        :type InstanceStatus: int
        """
        self.InstanceTypes = None
        self.ProductIds = None
        self.InstanceIds = None
        self.FenceFlag = None
        self.InstanceName = None
        self.PageSize = None
        self.PageNumber = None
        self.OrderBy = None
        self.OrderByType = None
        self.InstanceStatus = None


    def _deserialize(self, params):
        self.InstanceTypes = params.get("InstanceTypes")
        self.ProductIds = params.get("ProductIds")
        self.InstanceIds = params.get("InstanceIds")
        self.FenceFlag = params.get("FenceFlag")
        self.InstanceName = params.get("InstanceName")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.InstanceStatus = params.get("InstanceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 集群数量
        :type TotalCount: int
        :param Instances: 集群扩展信息
        :type Instances: list of InstanceExpand
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = InstanceExpand()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    """设备信息

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备ID
        :type DeviceId: int
        :param DeviceNo: 设备No
        :type DeviceNo: str
        :param DevClass: 设备类型
        :type DevClass: str
        :param MaxMemory: 设备总内存，单位GB
        :type MaxMemory: float
        :param MaxDisk: 设备总磁盘，单位GB
        :type MaxDisk: float
        :param RestMemory: 设备剩余内存，单位GB
        :type RestMemory: float
        :param RestDisk: 设备剩余磁盘，单位GB
        :type RestDisk: float
        :param RawDeviceNum: 设备机器个数
        :type RawDeviceNum: int
        :param InstanceNum: 数据库实例个数
        :type InstanceNum: int
        """
        self.DeviceId = None
        self.DeviceNo = None
        self.DevClass = None
        self.MaxMemory = None
        self.MaxDisk = None
        self.RestMemory = None
        self.RestDisk = None
        self.RawDeviceNum = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.DeviceNo = params.get("DeviceNo")
        self.DevClass = params.get("DevClass")
        self.MaxMemory = params.get("MaxMemory")
        self.MaxDisk = params.get("MaxDisk")
        self.RestMemory = params.get("RestMemory")
        self.RestDisk = params.get("RestDisk")
        self.RawDeviceNum = params.get("RawDeviceNum")
        self.InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """集群容量信息。

    """

    def __init__(self):
        r"""
        :param Status: 集群状态，0：运行中，1：不在运行
        :type Status: int
        :param ReadWriteTotalLeaveMemory: 读写集群剩余内存容量，单位GB
        :type ReadWriteTotalLeaveMemory: float
        :param ReadWriteTotalLeaveDisk: 读写集群剩余磁盘容量，单位GB
        :type ReadWriteTotalLeaveDisk: float
        :param ReadWriteTotalMemory: 读写集群总内存容量，单位GB
        :type ReadWriteTotalMemory: float
        :param ReadWriteTotalDisk: 读写集群总磁盘容量，单位GB
        :type ReadWriteTotalDisk: float
        :param ReadOnlyTotalLeaveMemory: 只读集群剩余内存容量，单位GB
        :type ReadOnlyTotalLeaveMemory: float
        :param ReadOnlyTotalLeaveDisk: 只读集群剩余磁盘容量，单位GB
        :type ReadOnlyTotalLeaveDisk: float
        :param ReadOnlyTotalMemory: 只读集群总内存容量，单位GB
        :type ReadOnlyTotalMemory: float
        :param ReadOnlyTotalDisk: 只读集群总磁盘容量，单位GB
        :type ReadOnlyTotalDisk: float
        :param InstanceDeviceInfos: 集群设备详情
        :type InstanceDeviceInfos: list of InstanceDeviceInfo
        """
        self.Status = None
        self.ReadWriteTotalLeaveMemory = None
        self.ReadWriteTotalLeaveDisk = None
        self.ReadWriteTotalMemory = None
        self.ReadWriteTotalDisk = None
        self.ReadOnlyTotalLeaveMemory = None
        self.ReadOnlyTotalLeaveDisk = None
        self.ReadOnlyTotalMemory = None
        self.ReadOnlyTotalDisk = None
        self.InstanceDeviceInfos = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ReadWriteTotalLeaveMemory = params.get("ReadWriteTotalLeaveMemory")
        self.ReadWriteTotalLeaveDisk = params.get("ReadWriteTotalLeaveDisk")
        self.ReadWriteTotalMemory = params.get("ReadWriteTotalMemory")
        self.ReadWriteTotalDisk = params.get("ReadWriteTotalDisk")
        self.ReadOnlyTotalLeaveMemory = params.get("ReadOnlyTotalLeaveMemory")
        self.ReadOnlyTotalLeaveDisk = params.get("ReadOnlyTotalLeaveDisk")
        self.ReadOnlyTotalMemory = params.get("ReadOnlyTotalMemory")
        self.ReadOnlyTotalDisk = params.get("ReadOnlyTotalDisk")
        if params.get("InstanceDeviceInfos") is not None:
            self.InstanceDeviceInfos = []
            for item in params.get("InstanceDeviceInfos"):
                obj = InstanceDeviceInfo()
                obj._deserialize(item)
                self.InstanceDeviceInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDeviceInfo(AbstractModel):
    """集群设备组信息。

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param ReadWriteDevice: 读写设备组
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadWriteDevice: list of DeviceInfo
        :param ReadOnlyDevice: 只读设备组
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnlyDevice: list of DeviceInfo
        :param FreeDevice: 空闲设备组
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeDevice: list of DeviceInfo
        """
        self.InstanceId = None
        self.ReadWriteDevice = None
        self.ReadOnlyDevice = None
        self.FreeDevice = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("ReadWriteDevice") is not None:
            self.ReadWriteDevice = []
            for item in params.get("ReadWriteDevice"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.ReadWriteDevice.append(obj)
        if params.get("ReadOnlyDevice") is not None:
            self.ReadOnlyDevice = []
            for item in params.get("ReadOnlyDevice"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.ReadOnlyDevice.append(obj)
        if params.get("FreeDevice") is not None:
            self.FreeDevice = []
            for item in params.get("FreeDevice"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.FreeDevice.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExpand(AbstractModel):
    """集群扩展信息。

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群ID
        :type InstanceId: str
        :param InstanceName: 集群名称
        :type InstanceName: str
        :param AppId: 用户ID
        :type AppId: int
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param InstanceType: 集群类型： 0：一主一备，1：一主两备
        :type InstanceType: int
        :param InstanceStatus: 集群状态: 0 集群创建中, 1 集群有效, 2 集群扩容中, 3 集群删除中, 4 集群缩容中 -1 集群已隔离 -2 集群已删除
        :type InstanceStatus: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param AutoRenewFlag: 实例自动续费标识： 0正常续费 1自动续费 2到期不续费
        :type AutoRenewFlag: int
        :param Machine: 机型
        :type Machine: str
        :param PeriodEndTime: 过期时间
        :type PeriodEndTime: str
        :param InstanceDetail: 集群信息
        :type InstanceDetail: :class:`tencentcloud.dbdc.v20201029.models.InstanceDetail`
        :param Pid: 计费侧的产品ID
        :type Pid: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.AppId = None
        self.Region = None
        self.Zone = None
        self.InstanceType = None
        self.InstanceStatus = None
        self.CreateTime = None
        self.AutoRenewFlag = None
        self.Machine = None
        self.PeriodEndTime = None
        self.InstanceDetail = None
        self.Pid = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.AppId = params.get("AppId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceStatus = params.get("InstanceStatus")
        self.CreateTime = params.get("CreateTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.Machine = params.get("Machine")
        self.PeriodEndTime = params.get("PeriodEndTime")
        if params.get("InstanceDetail") is not None:
            self.InstanceDetail = InstanceDetail()
            self.InstanceDetail._deserialize(params.get("InstanceDetail"))
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNameRequest(AbstractModel):
    """ModifyInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param InstanceName: 独享集群实例名称
        :type InstanceName: str
        """
        self.InstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNameResponse(AbstractModel):
    """ModifyInstanceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")