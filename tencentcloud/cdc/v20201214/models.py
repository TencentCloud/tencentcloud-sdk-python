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


class CbsInfo(AbstractModel):
    """购买的cbs信息

    """

    def __init__(self):
        r"""
        :param Size: cbs存储大小，单位TB
        :type Size: int
        :param Type: cbs存储类型，默认为SSD
        :type Type: str
        """
        self.Size = None
        self.Type = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosCapacity(AbstractModel):
    """CDC集群内cos的容量信息

    """

    def __init__(self):
        r"""
        :param TotalCapacity: 已购cos的总容量大小，单位GB
        :type TotalCapacity: float
        :param TotalFreeCapacity: 剩余可用cos的容量大小，单位GB
        :type TotalFreeCapacity: float
        :param TotalUsedCapacity: 已用cos的容量大小，单位GB
        :type TotalUsedCapacity: float
        """
        self.TotalCapacity = None
        self.TotalFreeCapacity = None
        self.TotalUsedCapacity = None


    def _deserialize(self, params):
        self.TotalCapacity = params.get("TotalCapacity")
        self.TotalFreeCapacity = params.get("TotalFreeCapacity")
        self.TotalUsedCapacity = params.get("TotalUsedCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosInfo(AbstractModel):
    """用于购买页面添加cos信息

    """

    def __init__(self):
        r"""
        :param Size: COS存储大小，单位TB
        :type Size: int
        :param Type: COS存储类型，默认为cos
        :type Type: str
        """
        self.Size = None
        self.Type = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterOrderRequest(AbstractModel):
    """CreateDedicatedClusterOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterId: 专用集群id
        :type DedicatedClusterId: str
        :param DedicatedClusterTypes: order关联的专用集群类型数组
        :type DedicatedClusterTypes: list of DedicatedClusterTypeInfo
        :param CosInfo: order关联的cos存储信息
        :type CosInfo: :class:`tencentcloud.cdc.v20201214.models.CosInfo`
        :param CbsInfo: order关联的cbs存储信息
        :type CbsInfo: :class:`tencentcloud.cdc.v20201214.models.CbsInfo`
        :param PurchaseSource: 购买来源，默认为cloudApi
        :type PurchaseSource: str
        :param DedicatedClusterOrderId: 当调用API接口提交订单时，需要提交DedicatedClusterOrderId
        :type DedicatedClusterOrderId: str
        """
        self.DedicatedClusterId = None
        self.DedicatedClusterTypes = None
        self.CosInfo = None
        self.CbsInfo = None
        self.PurchaseSource = None
        self.DedicatedClusterOrderId = None


    def _deserialize(self, params):
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        if params.get("DedicatedClusterTypes") is not None:
            self.DedicatedClusterTypes = []
            for item in params.get("DedicatedClusterTypes"):
                obj = DedicatedClusterTypeInfo()
                obj._deserialize(item)
                self.DedicatedClusterTypes.append(obj)
        if params.get("CosInfo") is not None:
            self.CosInfo = CosInfo()
            self.CosInfo._deserialize(params.get("CosInfo"))
        if params.get("CbsInfo") is not None:
            self.CbsInfo = CbsInfo()
            self.CbsInfo._deserialize(params.get("CbsInfo"))
        self.PurchaseSource = params.get("PurchaseSource")
        self.DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterOrderResponse(AbstractModel):
    """CreateDedicatedClusterOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterOrderId: 专用集群订单id
注意：此字段可能返回 null，表示取不到有效值。
        :type DedicatedClusterOrderId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DedicatedClusterOrderId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        self.RequestId = params.get("RequestId")


class CreateDedicatedClusterRequest(AbstractModel):
    """CreateDedicatedCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param SiteId: 专用集群所属的SiteId
        :type SiteId: str
        :param Name: 专用集群的名称
        :type Name: str
        :param Zone: 专用集群所属的可用区
        :type Zone: str
        :param Description: 专用集群的描述
        :type Description: str
        """
        self.SiteId = None
        self.Name = None
        self.Zone = None
        self.Description = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.Name = params.get("Name")
        self.Zone = params.get("Zone")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterResponse(AbstractModel):
    """CreateDedicatedCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterId: 创建的专用集群id
        :type DedicatedClusterId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DedicatedClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        self.RequestId = params.get("RequestId")


class CreateSiteRequest(AbstractModel):
    """CreateSite请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
        :type Name: str
        :param Country: 站点所在国家
        :type Country: str
        :param Province: 站点所在省份
        :type Province: str
        :param City: 站点所在城市
        :type City: str
        :param AddressLine: 站点所在地区的详细地址信息
        :type AddressLine: str
        :param Description: 站点描述
        :type Description: str
        :param Note: 注意事项
        :type Note: str
        :param FiberType: 您将使用光纤类型将CDC设备连接到网络。有单模和多模两种选项。
        :type FiberType: str
        :param OpticalStandard: 您将CDC连接到网络时采用的光学标准。此字段取决于上行链路速度、光纤类型和到上游设备的距离。
        :type OpticalStandard: str
        :param PowerConnectors: 电源连接器类型
        :type PowerConnectors: str
        :param PowerFeedDrop: 从机架上方还是下方供电。
        :type PowerFeedDrop: str
        :param MaxWeight: 最大承重(KG)
        :type MaxWeight: int
        :param PowerDrawKva: 功耗(KW)
        :type PowerDrawKva: int
        :param UplinkSpeedGbps: 网络到腾讯云Region区域的上行链路速度
        :type UplinkSpeedGbps: int
        :param UplinkCount: 将CDC连接到网络时，每台CDC网络设备(每个机架 2 台设备)使用的上行链路数量。
        :type UplinkCount: int
        :param ConditionRequirement: 是否满足下面环境条件：
1、场地没有材料要求或验收标准会影响 CDC 设备配送和安装。
2、确定的机架位置包含:
温度范围为 41 到 104°F (5 到 40°C)。
湿度范围为 10°F (-12°C)和 8% RH (相对湿度)到 70°F(21°C)和 80% RH。
机架位置的气流方向为从前向后，且应具有足够的 CFM (每分钟立方英尺)。CFM 必须是 CDC 配置的 kVA 功耗值的 145.8 倍。
        :type ConditionRequirement: bool
        :param DimensionRequirement: 是否满足下面的尺寸条件：
您的装货站台可以容纳一个机架箱(高 x 宽 x 深 = 94" x 54" x 48")。
您可以提供从机架(高 x 宽 x 深 = 80" x 24" x 48")交货地点到机架最终安置位置的明确通道。测量深度时，应包括站台、走廊通道、门、转弯、坡道、货梯，并将其他通道限制考虑在内。
在最终的 CDC安置位置，前部间隙可以为 48" 或更大，后部间隙可以为 24" 或更大。
        :type DimensionRequirement: bool
        :param RedundantNetworking: 是否提供冗余的上游设备(交换机或路由器)，以便两台  网络设备都能连接到网络设备。
        :type RedundantNetworking: bool
        :param PostalCode: 站点所在地区的邮编
        :type PostalCode: int
        :param OptionalAddressLine: 站点所在地区的详细地址信息（补充）
        :type OptionalAddressLine: str
        :param NeedHelp: 是否需要腾讯云团队协助完成机架支撑工作
        :type NeedHelp: bool
        :param RedundantPower: 是否电源冗余
        :type RedundantPower: bool
        :param BreakerRequirement: 上游断路器是否具备
        :type BreakerRequirement: bool
        """
        self.Name = None
        self.Country = None
        self.Province = None
        self.City = None
        self.AddressLine = None
        self.Description = None
        self.Note = None
        self.FiberType = None
        self.OpticalStandard = None
        self.PowerConnectors = None
        self.PowerFeedDrop = None
        self.MaxWeight = None
        self.PowerDrawKva = None
        self.UplinkSpeedGbps = None
        self.UplinkCount = None
        self.ConditionRequirement = None
        self.DimensionRequirement = None
        self.RedundantNetworking = None
        self.PostalCode = None
        self.OptionalAddressLine = None
        self.NeedHelp = None
        self.RedundantPower = None
        self.BreakerRequirement = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.AddressLine = params.get("AddressLine")
        self.Description = params.get("Description")
        self.Note = params.get("Note")
        self.FiberType = params.get("FiberType")
        self.OpticalStandard = params.get("OpticalStandard")
        self.PowerConnectors = params.get("PowerConnectors")
        self.PowerFeedDrop = params.get("PowerFeedDrop")
        self.MaxWeight = params.get("MaxWeight")
        self.PowerDrawKva = params.get("PowerDrawKva")
        self.UplinkSpeedGbps = params.get("UplinkSpeedGbps")
        self.UplinkCount = params.get("UplinkCount")
        self.ConditionRequirement = params.get("ConditionRequirement")
        self.DimensionRequirement = params.get("DimensionRequirement")
        self.RedundantNetworking = params.get("RedundantNetworking")
        self.PostalCode = params.get("PostalCode")
        self.OptionalAddressLine = params.get("OptionalAddressLine")
        self.NeedHelp = params.get("NeedHelp")
        self.RedundantPower = params.get("RedundantPower")
        self.BreakerRequirement = params.get("BreakerRequirement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSiteResponse(AbstractModel):
    """CreateSite返回参数结构体

    """

    def __init__(self):
        r"""
        :param SiteId: 创建Site生成的id
        :type SiteId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SiteId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.RequestId = params.get("RequestId")


class DedicatedCluster(AbstractModel):
    """专用集群列表

    """

    def __init__(self):
        r"""
        :param DedicatedClusterId: 专用集群id。如"cluster-xxxxx"。
        :type DedicatedClusterId: str
        :param Zone: 专用集群所属可用区名称。
        :type Zone: str
        :param Description: 专用集群的描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Name: 专用集群的名称。
        :type Name: str
        :param LifecycleStatus: 专用集群的生命周期。如"PENDING"。
        :type LifecycleStatus: str
        :param CreateTime: 专用集群的创建时间。
        :type CreateTime: str
        :param SiteId: 专用集群所属的站点id。
        :type SiteId: str
        """
        self.DedicatedClusterId = None
        self.Zone = None
        self.Description = None
        self.Name = None
        self.LifecycleStatus = None
        self.CreateTime = None
        self.SiteId = None


    def _deserialize(self, params):
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        self.Zone = params.get("Zone")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.LifecycleStatus = params.get("LifecycleStatus")
        self.CreateTime = params.get("CreateTime")
        self.SiteId = params.get("SiteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterInstanceType(AbstractModel):
    """专用宿主机支持的实例规格列表

    """

    def __init__(self):
        r"""
        :param Zone: 可用区
        :type Zone: str
        :param InstanceType: 规格名称
        :type InstanceType: str
        :param NetworkCard: 网卡类型，例如：25代表25G网卡
        :type NetworkCard: int
        :param Cpu: 实例的CPU核数，单位：核。
        :type Cpu: int
        :param Memory: 实例内存容量，单位：`GB`。
        :type Memory: int
        :param InstanceFamily: 实例机型系列。
        :type InstanceFamily: str
        :param TypeName: 机型名称。
        :type TypeName: str
        :param StorageBlockAmount: 本地存储块数量。
        :type StorageBlockAmount: int
        :param InstanceBandwidth: 内网带宽，单位Gbps。
        :type InstanceBandwidth: float
        :param InstancePps: 网络收发包能力，单位万PPS。
        :type InstancePps: int
        :param CpuType: 处理器型号。
        :type CpuType: str
        :param Gpu: 实例的GPU数量。
        :type Gpu: int
        :param Fpga: 实例的FPGA数量。
        :type Fpga: int
        :param Remark: 机型描述
        :type Remark: str
        :param Status: 实例是否售卖。取值范围： <br><li>SELL：表示实例可购买<br><li>SOLD_OUT：表示实例已售罄。
        :type Status: str
        """
        self.Zone = None
        self.InstanceType = None
        self.NetworkCard = None
        self.Cpu = None
        self.Memory = None
        self.InstanceFamily = None
        self.TypeName = None
        self.StorageBlockAmount = None
        self.InstanceBandwidth = None
        self.InstancePps = None
        self.CpuType = None
        self.Gpu = None
        self.Fpga = None
        self.Remark = None
        self.Status = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.NetworkCard = params.get("NetworkCard")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.InstanceFamily = params.get("InstanceFamily")
        self.TypeName = params.get("TypeName")
        self.StorageBlockAmount = params.get("StorageBlockAmount")
        self.InstanceBandwidth = params.get("InstanceBandwidth")
        self.InstancePps = params.get("InstancePps")
        self.CpuType = params.get("CpuType")
        self.Gpu = params.get("Gpu")
        self.Fpga = params.get("Fpga")
        self.Remark = params.get("Remark")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterOrder(AbstractModel):
    """专用集群订单

    """

    def __init__(self):
        r"""
        :param DedicatedClusterId: 专用集群id
        :type DedicatedClusterId: str
        :param DedicatedClusterTypeId: 专用集群类型id（移到下一层级，已经废弃，后续将删除）
        :type DedicatedClusterTypeId: str
        :param SupportedStorageType: 支持的存储类型列表（移到下一层级，已经废弃，后续将删除）
        :type SupportedStorageType: list of str
        :param SupportedUplinkSpeed: 支持的上连交换机的链路传输速率(GiB)（移到下一层级，已经废弃，后续将删除）
        :type SupportedUplinkSpeed: list of int
        :param SupportedInstanceFamily: 支持的实例族列表（移到下一层级，已经废弃，后续将删除）
        :type SupportedInstanceFamily: list of str
        :param Weight: 地板承重要求(KG)
        :type Weight: int
        :param PowerDraw: 功率要求(KW)
        :type PowerDraw: float
        :param OrderStatus: 订单状态
        :type OrderStatus: str
        :param CreateTime: 订单创建的时间
        :type CreateTime: str
        :param DedicatedClusterOrderId: 大订单ID
        :type DedicatedClusterOrderId: str
        :param Action: 订单类型，创建CREATE或扩容EXTEND
        :type Action: str
        :param DedicatedClusterOrderItems: 子订单详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DedicatedClusterOrderItems: list of DedicatedClusterOrderItem
        :param Cpu: cpu值
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param Mem: mem值
注意：此字段可能返回 null，表示取不到有效值。
        :type Mem: int
        :param Gpu: gpu值
注意：此字段可能返回 null，表示取不到有效值。
        :type Gpu: int
        :param PayStatus: 0代表未支付，1代表已支付
注意：此字段可能返回 null，表示取不到有效值。
        :type PayStatus: int
        """
        self.DedicatedClusterId = None
        self.DedicatedClusterTypeId = None
        self.SupportedStorageType = None
        self.SupportedUplinkSpeed = None
        self.SupportedInstanceFamily = None
        self.Weight = None
        self.PowerDraw = None
        self.OrderStatus = None
        self.CreateTime = None
        self.DedicatedClusterOrderId = None
        self.Action = None
        self.DedicatedClusterOrderItems = None
        self.Cpu = None
        self.Mem = None
        self.Gpu = None
        self.PayStatus = None


    def _deserialize(self, params):
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        self.DedicatedClusterTypeId = params.get("DedicatedClusterTypeId")
        self.SupportedStorageType = params.get("SupportedStorageType")
        self.SupportedUplinkSpeed = params.get("SupportedUplinkSpeed")
        self.SupportedInstanceFamily = params.get("SupportedInstanceFamily")
        self.Weight = params.get("Weight")
        self.PowerDraw = params.get("PowerDraw")
        self.OrderStatus = params.get("OrderStatus")
        self.CreateTime = params.get("CreateTime")
        self.DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        self.Action = params.get("Action")
        if params.get("DedicatedClusterOrderItems") is not None:
            self.DedicatedClusterOrderItems = []
            for item in params.get("DedicatedClusterOrderItems"):
                obj = DedicatedClusterOrderItem()
                obj._deserialize(item)
                self.DedicatedClusterOrderItems.append(obj)
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.Gpu = params.get("Gpu")
        self.PayStatus = params.get("PayStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterOrderItem(AbstractModel):
    """专用集群子订单

    """

    def __init__(self):
        r"""
        :param DedicatedClusterTypeId: 专用集群类型id
        :type DedicatedClusterTypeId: str
        :param SupportedStorageType: 支持的存储类型列表
        :type SupportedStorageType: list of str
        :param SupportedUplinkSpeed: 支持的上连交换机的链路传输速率(GiB)
        :type SupportedUplinkSpeed: list of int
        :param SupportedInstanceFamily: 支持的实例族列表
        :type SupportedInstanceFamily: list of str
        :param Weight: 地板承重要求(KG)
        :type Weight: int
        :param PowerDraw: 功率要求(KW)
        :type PowerDraw: float
        :param SubOrderStatus: 订单状态
        :type SubOrderStatus: str
        :param CreateTime: 订单创建的时间
        :type CreateTime: str
        :param SubOrderId: 子订单ID
        :type SubOrderId: str
        :param Count: 关联的集群规格数量
        :type Count: int
        :param Name: 规格简单描述
        :type Name: str
        :param Description: 规格详细描述
        :type Description: str
        :param TotalCpu: CPU数
        :type TotalCpu: int
        :param TotalMem: 内存数
        :type TotalMem: int
        :param TotalGpu: GPU数
        :type TotalGpu: int
        :param TypeName: 规格英文名
        :type TypeName: str
        :param ComputeFormat: 规格展示
注意：此字段可能返回 null，表示取不到有效值。
        :type ComputeFormat: str
        """
        self.DedicatedClusterTypeId = None
        self.SupportedStorageType = None
        self.SupportedUplinkSpeed = None
        self.SupportedInstanceFamily = None
        self.Weight = None
        self.PowerDraw = None
        self.SubOrderStatus = None
        self.CreateTime = None
        self.SubOrderId = None
        self.Count = None
        self.Name = None
        self.Description = None
        self.TotalCpu = None
        self.TotalMem = None
        self.TotalGpu = None
        self.TypeName = None
        self.ComputeFormat = None


    def _deserialize(self, params):
        self.DedicatedClusterTypeId = params.get("DedicatedClusterTypeId")
        self.SupportedStorageType = params.get("SupportedStorageType")
        self.SupportedUplinkSpeed = params.get("SupportedUplinkSpeed")
        self.SupportedInstanceFamily = params.get("SupportedInstanceFamily")
        self.Weight = params.get("Weight")
        self.PowerDraw = params.get("PowerDraw")
        self.SubOrderStatus = params.get("SubOrderStatus")
        self.CreateTime = params.get("CreateTime")
        self.SubOrderId = params.get("SubOrderId")
        self.Count = params.get("Count")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.TotalCpu = params.get("TotalCpu")
        self.TotalMem = params.get("TotalMem")
        self.TotalGpu = params.get("TotalGpu")
        self.TypeName = params.get("TypeName")
        self.ComputeFormat = params.get("ComputeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterType(AbstractModel):
    """专用集群配置

    """

    def __init__(self):
        r"""
        :param DedicatedClusterTypeId: 配置id
        :type DedicatedClusterTypeId: str
        :param Description: 配置描述，对应描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Name: 配置名称，对应计算资源类型
        :type Name: str
        :param CreateTime: 创建配置的时间
        :type CreateTime: str
        :param SupportedStorageType: 支持的存储类型列表
        :type SupportedStorageType: list of str
        :param SupportedUplinkGiB: 支持的上连交换机的链路传输速率
        :type SupportedUplinkGiB: list of int
        :param SupportedInstanceFamily: 支持的实例族列表
        :type SupportedInstanceFamily: list of str
        :param Weight: 地板承重要求(KG)
        :type Weight: int
        :param PowerDrawKva: 功率要求(KW)
        :type PowerDrawKva: float
        :param ComputeFormatDesc: 显示计算资源规格详情，存储等资源不显示；对应规格
        :type ComputeFormatDesc: str
        """
        self.DedicatedClusterTypeId = None
        self.Description = None
        self.Name = None
        self.CreateTime = None
        self.SupportedStorageType = None
        self.SupportedUplinkGiB = None
        self.SupportedInstanceFamily = None
        self.Weight = None
        self.PowerDrawKva = None
        self.ComputeFormatDesc = None


    def _deserialize(self, params):
        self.DedicatedClusterTypeId = params.get("DedicatedClusterTypeId")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.SupportedStorageType = params.get("SupportedStorageType")
        self.SupportedUplinkGiB = params.get("SupportedUplinkGiB")
        self.SupportedInstanceFamily = params.get("SupportedInstanceFamily")
        self.Weight = params.get("Weight")
        self.PowerDrawKva = params.get("PowerDrawKva")
        self.ComputeFormatDesc = params.get("ComputeFormatDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterTypeInfo(AbstractModel):
    """DedicatedClusterType => (Id, Count)

    """

    def __init__(self):
        r"""
        :param Id: 集群类型Id
        :type Id: str
        :param Count: 集群类型个数
        :type Count: int
        """
        self.Id = None
        self.Count = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDedicatedClustersRequest(AbstractModel):
    """DeleteDedicatedClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterIds: 要删除的专用集群id
        :type DedicatedClusterIds: list of str
        """
        self.DedicatedClusterIds = None


    def _deserialize(self, params):
        self.DedicatedClusterIds = params.get("DedicatedClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDedicatedClustersResponse(AbstractModel):
    """DeleteDedicatedClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSitesRequest(AbstractModel):
    """DeleteSites请求参数结构体

    """

    def __init__(self):
        r"""
        :param SiteIds: 要删除的站点id列表
        :type SiteIds: list of str
        """
        self.SiteIds = None


    def _deserialize(self, params):
        self.SiteIds = params.get("SiteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSitesResponse(AbstractModel):
    """DeleteSites返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDedicatedClusterCosCapacityRequest(AbstractModel):
    """DescribeDedicatedClusterCosCapacity请求参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterId: 查询的专用集群id
        :type DedicatedClusterId: str
        """
        self.DedicatedClusterId = None


    def _deserialize(self, params):
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterCosCapacityResponse(AbstractModel):
    """DescribeDedicatedClusterCosCapacity返回参数结构体

    """

    def __init__(self):
        r"""
        :param CosCapacity: 本集群内cos容量信息，单位：‘GB’
        :type CosCapacity: :class:`tencentcloud.cdc.v20201214.models.CosCapacity`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CosCapacity = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CosCapacity") is not None:
            self.CosCapacity = CosCapacity()
            self.CosCapacity._deserialize(params.get("CosCapacity"))
        self.RequestId = params.get("RequestId")


class DescribeDedicatedClusterHostStatisticsRequest(AbstractModel):
    """DescribeDedicatedClusterHostStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterId: 查询的专用集群id
        :type DedicatedClusterId: str
        """
        self.DedicatedClusterId = None


    def _deserialize(self, params):
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterHostStatisticsResponse(AbstractModel):
    """DescribeDedicatedClusterHostStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param HostStatisticSet: 该集群内宿主机的统计信息列表
        :type HostStatisticSet: list of HostStatistic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HostStatisticSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HostStatisticSet") is not None:
            self.HostStatisticSet = []
            for item in params.get("HostStatisticSet"):
                obj = HostStatistic()
                obj._deserialize(item)
                self.HostStatisticSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDedicatedClusterHostsRequest(AbstractModel):
    """DescribeDedicatedClusterHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterId: 集群id
        :type DedicatedClusterId: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20
        :type Limit: int
        """
        self.DedicatedClusterId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterHostsResponse(AbstractModel):
    """DescribeDedicatedClusterHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param HostInfoSet: 宿主机信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HostInfoSet: list of HostInfo
        :param TotalCount: 宿主机总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HostInfoSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HostInfoSet") is not None:
            self.HostInfoSet = []
            for item in params.get("HostInfoSet"):
                obj = HostInfo()
                obj._deserialize(item)
                self.HostInfoSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDedicatedClusterInstanceTypesRequest(AbstractModel):
    """DescribeDedicatedClusterInstanceTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterId: 查询的专用集群id
        :type DedicatedClusterId: str
        """
        self.DedicatedClusterId = None


    def _deserialize(self, params):
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterInstanceTypesResponse(AbstractModel):
    """DescribeDedicatedClusterInstanceTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterInstanceTypeSet: 支持的实例规格列表
        :type DedicatedClusterInstanceTypeSet: list of DedicatedClusterInstanceType
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DedicatedClusterInstanceTypeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DedicatedClusterInstanceTypeSet") is not None:
            self.DedicatedClusterInstanceTypeSet = []
            for item in params.get("DedicatedClusterInstanceTypeSet"):
                obj = DedicatedClusterInstanceType()
                obj._deserialize(item)
                self.DedicatedClusterInstanceTypeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDedicatedClusterOrdersRequest(AbstractModel):
    """DescribeDedicatedClusterOrders请求参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterIds: 按照专用集群id过滤
        :type DedicatedClusterIds: list of str
        :param DedicatedClusterOrderIds: 按照专用集群订单id过滤
        :type DedicatedClusterOrderIds: str
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param Status: 订单状态为过滤条件：PENDING INCONSTRUCTION DELIVERING DELIVERED EXPIRED CANCELLED  OFFLINE
        :type Status: str
        :param ActionType: 订单类型为过滤条件：CREATE  EXTEND
        :type ActionType: str
        """
        self.DedicatedClusterIds = None
        self.DedicatedClusterOrderIds = None
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.ActionType = None


    def _deserialize(self, params):
        self.DedicatedClusterIds = params.get("DedicatedClusterIds")
        self.DedicatedClusterOrderIds = params.get("DedicatedClusterOrderIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterOrdersResponse(AbstractModel):
    """DescribeDedicatedClusterOrders返回参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterOrderSet: 专用集群订单列表
        :type DedicatedClusterOrderSet: list of DedicatedClusterOrder
        :param TotalCount: 符合条件的专用集群订单总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DedicatedClusterOrderSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DedicatedClusterOrderSet") is not None:
            self.DedicatedClusterOrderSet = []
            for item in params.get("DedicatedClusterOrderSet"):
                obj = DedicatedClusterOrder()
                obj._deserialize(item)
                self.DedicatedClusterOrderSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDedicatedClusterOverviewRequest(AbstractModel):
    """DescribeDedicatedClusterOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterId: 集群id
        :type DedicatedClusterId: str
        """
        self.DedicatedClusterId = None


    def _deserialize(self, params):
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterOverviewResponse(AbstractModel):
    """DescribeDedicatedClusterOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param CvmCount: 云服务器数量
        :type CvmCount: int
        :param HostCount: 宿主机数量
        :type HostCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CvmCount = None
        self.HostCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CvmCount = params.get("CvmCount")
        self.HostCount = params.get("HostCount")
        self.RequestId = params.get("RequestId")


class DescribeDedicatedClusterTypesRequest(AbstractModel):
    """DescribeDedicatedClusterTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 模糊匹配专用集群配置名称
        :type Name: str
        :param DedicatedClusterTypeIds: 待查询的专用集群配置id列表
        :type DedicatedClusterTypeIds: list of str
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param IsCompute: 是否只查询计算规格类型
        :type IsCompute: bool
        """
        self.Name = None
        self.DedicatedClusterTypeIds = None
        self.Offset = None
        self.Limit = None
        self.IsCompute = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DedicatedClusterTypeIds = params.get("DedicatedClusterTypeIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.IsCompute = params.get("IsCompute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterTypesResponse(AbstractModel):
    """DescribeDedicatedClusterTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterTypeSet: 专用集群配置列表
        :type DedicatedClusterTypeSet: list of DedicatedClusterType
        :param TotalCount: 符合条件的个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DedicatedClusterTypeSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DedicatedClusterTypeSet") is not None:
            self.DedicatedClusterTypeSet = []
            for item in params.get("DedicatedClusterTypeSet"):
                obj = DedicatedClusterType()
                obj._deserialize(item)
                self.DedicatedClusterTypeSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDedicatedClustersRequest(AbstractModel):
    """DescribeDedicatedClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterIds: 按照一个或者多个实例ID查询。实例ID形如：`cluster-xxxxxxxx`
        :type DedicatedClusterIds: list of str
        :param Zones: 按照可用区名称过滤
        :type Zones: list of str
        :param SiteIds: 按照站点id过滤
        :type SiteIds: list of str
        :param LifecycleStatuses: 按照专用集群生命周期过滤
        :type LifecycleStatuses: list of str
        :param Name: 模糊匹配专用集群名称
        :type Name: str
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.DedicatedClusterIds = None
        self.Zones = None
        self.SiteIds = None
        self.LifecycleStatuses = None
        self.Name = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DedicatedClusterIds = params.get("DedicatedClusterIds")
        self.Zones = params.get("Zones")
        self.SiteIds = params.get("SiteIds")
        self.LifecycleStatuses = params.get("LifecycleStatuses")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClustersResponse(AbstractModel):
    """DescribeDedicatedClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterSet: 符合查询条件的专用集群列表
        :type DedicatedClusterSet: list of DedicatedCluster
        :param TotalCount: 符合条件的专用集群数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DedicatedClusterSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DedicatedClusterSet") is not None:
            self.DedicatedClusterSet = []
            for item in params.get("DedicatedClusterSet"):
                obj = DedicatedCluster()
                obj._deserialize(item)
                self.DedicatedClusterSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDedicatedSupportedZonesRequest(AbstractModel):
    """DescribeDedicatedSupportedZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param Regions: 传入region列表
        :type Regions: list of int
        """
        self.Regions = None


    def _deserialize(self, params):
        self.Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedSupportedZonesResponse(AbstractModel):
    """DescribeDedicatedSupportedZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneSet: 支持的可用区列表
        :type ZoneSet: list of RegionZoneInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = RegionZoneInfo()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSitesDetailRequest(AbstractModel):
    """DescribeSitesDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param SiteIds: 按照站点id过滤
        :type SiteIds: list of str
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param Name: 按照站定名称模糊匹配
        :type Name: str
        """
        self.SiteIds = None
        self.Offset = None
        self.Limit = None
        self.Name = None


    def _deserialize(self, params):
        self.SiteIds = params.get("SiteIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSitesDetailResponse(AbstractModel):
    """DescribeSitesDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param SiteDetailSet: 站点详情
        :type SiteDetailSet: list of SiteDetail
        :param TotalCount: 符合条件的站点总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SiteDetailSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SiteDetailSet") is not None:
            self.SiteDetailSet = []
            for item in params.get("SiteDetailSet"):
                obj = SiteDetail()
                obj._deserialize(item)
                self.SiteDetailSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSitesRequest(AbstractModel):
    """DescribeSites请求参数结构体

    """

    def __init__(self):
        r"""
        :param SiteIds: 按照站点id过滤
        :type SiteIds: list of str
        :param Name: 模糊匹配站点名称
        :type Name: str
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.SiteIds = None
        self.Name = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SiteIds = params.get("SiteIds")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSitesResponse(AbstractModel):
    """DescribeSites返回参数结构体

    """

    def __init__(self):
        r"""
        :param SiteSet: 符合查询条件的站点列表
        :type SiteSet: list of Site
        :param TotalCount: 符合条件的站点数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SiteSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SiteSet") is not None:
            self.SiteSet = []
            for item in params.get("SiteSet"):
                obj = Site()
                obj._deserialize(item)
                self.SiteSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class HostInfo(AbstractModel):
    """CDC宿主机的详细信息

    """

    def __init__(self):
        r"""
        :param HostIp: 宿主机IP
        :type HostIp: str
        :param ServiceType: 云服务类型
        :type ServiceType: str
        :param HostStatus: 宿主机运行状态
        :type HostStatus: str
        :param HostType: 宿主机类型
        :type HostType: str
        :param CpuAvailable: cpu可用数
        :type CpuAvailable: int
        :param CpuTotal: cpu总数
        :type CpuTotal: int
        :param MemAvailable: 内存可用数
        :type MemAvailable: int
        :param MemTotal: 内存总数
        :type MemTotal: int
        :param RunTime: 运行时间
        :type RunTime: str
        :param ExpireTime: 到期时间
        :type ExpireTime: str
        """
        self.HostIp = None
        self.ServiceType = None
        self.HostStatus = None
        self.HostType = None
        self.CpuAvailable = None
        self.CpuTotal = None
        self.MemAvailable = None
        self.MemTotal = None
        self.RunTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.HostIp = params.get("HostIp")
        self.ServiceType = params.get("ServiceType")
        self.HostStatus = params.get("HostStatus")
        self.HostType = params.get("HostType")
        self.CpuAvailable = params.get("CpuAvailable")
        self.CpuTotal = params.get("CpuTotal")
        self.MemAvailable = params.get("MemAvailable")
        self.MemTotal = params.get("MemTotal")
        self.RunTime = params.get("RunTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostStatistic(AbstractModel):
    """CDC集群内宿主机的统计信息

    """

    def __init__(self):
        r"""
        :param HostType: 宿主机规格
        :type HostType: str
        :param HostFamily: 宿主机机型系列
        :type HostFamily: str
        :param Cpu: 宿主机的CPU核数，单位：核
        :type Cpu: int
        :param Memory: 宿主机内存大小，单位：GB
        :type Memory: int
        :param Count: 该规格宿主机的数量
        :type Count: int
        """
        self.HostType = None
        self.HostFamily = None
        self.Cpu = None
        self.Memory = None
        self.Count = None


    def _deserialize(self, params):
        self.HostType = params.get("HostType")
        self.HostFamily = params.get("HostFamily")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDedicatedClusterInfoRequest(AbstractModel):
    """ModifyDedicatedClusterInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param DedicatedClusterId: 本地专用集群ID
        :type DedicatedClusterId: str
        :param Name: 集群的新名称
        :type Name: str
        :param Zone: 集群的新可用区
        :type Zone: str
        :param Description: 集群的新描述信息
        :type Description: str
        :param SiteId: 集群所在站点
        :type SiteId: str
        """
        self.DedicatedClusterId = None
        self.Name = None
        self.Zone = None
        self.Description = None
        self.SiteId = None


    def _deserialize(self, params):
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        self.Name = params.get("Name")
        self.Zone = params.get("Zone")
        self.Description = params.get("Description")
        self.SiteId = params.get("SiteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDedicatedClusterInfoResponse(AbstractModel):
    """ModifyDedicatedClusterInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyOrderStatusRequest(AbstractModel):
    """ModifyOrderStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 要更新成的状态
        :type Status: str
        :param DedicatedClusterOrderId: 大订单ID
        :type DedicatedClusterOrderId: str
        :param SubOrderIds: 小订单ID
        :type SubOrderIds: list of str
        """
        self.Status = None
        self.DedicatedClusterOrderId = None
        self.SubOrderIds = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        self.SubOrderIds = params.get("SubOrderIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOrderStatusResponse(AbstractModel):
    """ModifyOrderStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySiteDeviceInfoRequest(AbstractModel):
    """ModifySiteDeviceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param SiteId: 机房ID
        :type SiteId: str
        :param FiberType: 您将使用光纤类型将CDC设备连接到网络。有单模和多模两种选项。
        :type FiberType: str
        :param OpticalStandard: 您将CDC连接到网络时采用的光学标准。此字段取决于上行链路速度、光纤类型和到上游设备的距离。
        :type OpticalStandard: str
        :param PowerConnectors: 电源连接器类型
        :type PowerConnectors: str
        :param PowerFeedDrop: 从机架上方还是下方供电。
        :type PowerFeedDrop: str
        :param MaxWeight: 最大承重(KG)
        :type MaxWeight: int
        :param PowerDrawKva: 功耗(KW)
        :type PowerDrawKva: int
        :param UplinkSpeedGbps: 网络到腾讯云Region区域的上行链路速度
        :type UplinkSpeedGbps: int
        :param UplinkCount: 将CDC连接到网络时，每台CDC网络设备(每个机架 2 台设备)使用的上行链路数量。
        :type UplinkCount: int
        :param ConditionRequirement: 是否满足下面环境条件：
1、场地没有材料要求或验收标准会影响 CDC 设备配送和安装。
2、确定的机架位置包含:
温度范围为 41 到 104°F (5 到 40°C)。
湿度范围为 10°F (-12°C)和 8% RH (相对湿度)到 70°F(21°C)和 80% RH。
机架位置的气流方向为从前向后，且应具有足够的 CFM (每分钟立方英尺)。CFM 必须是 CDC 配置的 kVA 功耗值的 145.8 倍。
        :type ConditionRequirement: bool
        :param DimensionRequirement: 是否满足下面的尺寸条件：
您的装货站台可以容纳一个机架箱(高 x 宽 x 深 = 94" x 54" x 48")。
您可以提供从机架(高 x 宽 x 深 = 80" x 24" x 48")交货地点到机架最终安置位置的明确通道。测量深度时，应包括站台、走廊通道、门、转弯、坡道、货梯，并将其他通道限制考虑在内。
在最终的 CDC安置位置，前部间隙可以为 48" 或更大，后部间隙可以为 24" 或更大。
        :type DimensionRequirement: bool
        :param RedundantNetworking: 是否提供冗余的上游设备(交换机或路由器)，以便两台  网络设备都能连接到网络设备。
        :type RedundantNetworking: bool
        :param NeedHelp: 是否需要腾讯云团队协助完成机架支撑工作
        :type NeedHelp: bool
        :param RedundantPower: 是否电源冗余
        :type RedundantPower: bool
        :param BreakerRequirement: 上游断路器是否具备
        :type BreakerRequirement: bool
        """
        self.SiteId = None
        self.FiberType = None
        self.OpticalStandard = None
        self.PowerConnectors = None
        self.PowerFeedDrop = None
        self.MaxWeight = None
        self.PowerDrawKva = None
        self.UplinkSpeedGbps = None
        self.UplinkCount = None
        self.ConditionRequirement = None
        self.DimensionRequirement = None
        self.RedundantNetworking = None
        self.NeedHelp = None
        self.RedundantPower = None
        self.BreakerRequirement = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.FiberType = params.get("FiberType")
        self.OpticalStandard = params.get("OpticalStandard")
        self.PowerConnectors = params.get("PowerConnectors")
        self.PowerFeedDrop = params.get("PowerFeedDrop")
        self.MaxWeight = params.get("MaxWeight")
        self.PowerDrawKva = params.get("PowerDrawKva")
        self.UplinkSpeedGbps = params.get("UplinkSpeedGbps")
        self.UplinkCount = params.get("UplinkCount")
        self.ConditionRequirement = params.get("ConditionRequirement")
        self.DimensionRequirement = params.get("DimensionRequirement")
        self.RedundantNetworking = params.get("RedundantNetworking")
        self.NeedHelp = params.get("NeedHelp")
        self.RedundantPower = params.get("RedundantPower")
        self.BreakerRequirement = params.get("BreakerRequirement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySiteDeviceInfoResponse(AbstractModel):
    """ModifySiteDeviceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySiteInfoRequest(AbstractModel):
    """ModifySiteInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param SiteId: 机房ID
        :type SiteId: str
        :param Name: 站点名称
        :type Name: str
        :param Description: 站点描述
        :type Description: str
        :param Note: 注意事项
        :type Note: str
        :param Country: 站点所在国家
        :type Country: str
        :param Province: 站点所在省份
        :type Province: str
        :param City: 站点所在城市
        :type City: str
        :param PostalCode: 站点所在地区的邮编
        :type PostalCode: str
        :param AddressLine: 站点所在地区的详细地址信息
        :type AddressLine: str
        """
        self.SiteId = None
        self.Name = None
        self.Description = None
        self.Note = None
        self.Country = None
        self.Province = None
        self.City = None
        self.PostalCode = None
        self.AddressLine = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Note = params.get("Note")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.PostalCode = params.get("PostalCode")
        self.AddressLine = params.get("AddressLine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySiteInfoResponse(AbstractModel):
    """ModifySiteInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionZoneInfo(AbstractModel):
    """RegionZoneInfo信息

    """

    def __init__(self):
        r"""
        :param RegionId: Region id
        :type RegionId: int
        :param Zones: ZoneInfo数组
        :type Zones: list of ZoneInfo
        """
        self.RegionId = None
        self.Zones = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.Zones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Site(AbstractModel):
    """客户站点信息

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
        :type Name: str
        :param SiteId: 站点id
        :type SiteId: str
        :param Description: 站点描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateTime: 站点创建时间
        :type CreateTime: str
        """
        self.Name = None
        self.SiteId = None
        self.Description = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.SiteId = params.get("SiteId")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SiteDetail(AbstractModel):
    """站点详情

    """

    def __init__(self):
        r"""
        :param SiteId: 站点id
        :type SiteId: str
        :param Name: 站点名称
        :type Name: str
        :param Description: 站点描述
        :type Description: str
        :param CreateTime: 站点创建时间
        :type CreateTime: str
        :param FiberType: 光纤类型
        :type FiberType: str
        :param UplinkSpeedGbps: 网络到腾讯云Region区域的上行链路速度
        :type UplinkSpeedGbps: int
        :param UplinkCount: 将CDC连接到网络时，每台CDC网络设备(每个机架 2 台设备)使用的上行链路数量。
        :type UplinkCount: int
        :param OpticalStandard: 将CDC连接到网络时采用的光学标准
        :type OpticalStandard: str
        :param RedundantNetworking: 是否提供冗余的上游设备(交换机或路由器)，以便两台  网络设备都能连接到网络设备。
        :type RedundantNetworking: bool
        :param PowerConnectors: 电源连接器类型
        :type PowerConnectors: str
        :param PowerFeedDrop: 从机架上方还是下方供电。
        :type PowerFeedDrop: str
        :param PowerDrawKva: 功耗(KW)
        :type PowerDrawKva: float
        :param ConditionRequirement: 是否满足下面环境条件：
1、场地没有材料要求或验收标准会影响 CDC 设备配送和安装。
2、确定的机架位置包含:
温度范围为 41 到 104°F (5 到 40°C)。
湿度范围为 10°F (-12°C)和 8% RH (相对湿度)到 70°F(21°C)和 80% RH。
机架位置的气流方向为从前向后，且应具有足够的 CFM (每分钟立方英尺)。CFM 必须是 CDC 配置的 kVA 功耗值的 145.8 倍。
        :type ConditionRequirement: bool
        :param DimensionRequirement: 是否满足下面的尺寸条件：
您的装货站台可以容纳一个机架箱(高 x 宽 x 深 = 94" x 54" x 48")。
您可以提供从机架(高 x 宽 x 深 = 80" x 24" x 48")交货地点到机架最终安置位置的明确通道。测量深度时，应包括站台、走廊通道、门、转弯、坡道、货梯，并将其他通道限制考虑在内。
在最终的 CDC安置位置，前部间隙可以为 48" 或更大，后部间隙可以为 24" 或更大。
        :type DimensionRequirement: bool
        :param MaxWeight: 最大承重(KG)
        :type MaxWeight: int
        :param AddressLine: 站点地址
        :type AddressLine: str
        :param OptionalAddressLine: 站点所在地区的详细地址信息（补充）
        :type OptionalAddressLine: str
        :param NeedHelp: 是否需要腾讯云团队协助完成机架支撑工作
        :type NeedHelp: bool
        :param BreakerRequirement: 上游断路器是否具备
        :type BreakerRequirement: bool
        :param RedundantPower: 是否电源冗余
        :type RedundantPower: bool
        :param Country: 站点所在国家
        :type Country: str
        :param Province: 站点所在省份
        :type Province: str
        :param City: 站点所在城市
        :type City: str
        :param PostalCode: 站点所在地区的邮编
        :type PostalCode: int
        """
        self.SiteId = None
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.FiberType = None
        self.UplinkSpeedGbps = None
        self.UplinkCount = None
        self.OpticalStandard = None
        self.RedundantNetworking = None
        self.PowerConnectors = None
        self.PowerFeedDrop = None
        self.PowerDrawKva = None
        self.ConditionRequirement = None
        self.DimensionRequirement = None
        self.MaxWeight = None
        self.AddressLine = None
        self.OptionalAddressLine = None
        self.NeedHelp = None
        self.BreakerRequirement = None
        self.RedundantPower = None
        self.Country = None
        self.Province = None
        self.City = None
        self.PostalCode = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.FiberType = params.get("FiberType")
        self.UplinkSpeedGbps = params.get("UplinkSpeedGbps")
        self.UplinkCount = params.get("UplinkCount")
        self.OpticalStandard = params.get("OpticalStandard")
        self.RedundantNetworking = params.get("RedundantNetworking")
        self.PowerConnectors = params.get("PowerConnectors")
        self.PowerFeedDrop = params.get("PowerFeedDrop")
        self.PowerDrawKva = params.get("PowerDrawKva")
        self.ConditionRequirement = params.get("ConditionRequirement")
        self.DimensionRequirement = params.get("DimensionRequirement")
        self.MaxWeight = params.get("MaxWeight")
        self.AddressLine = params.get("AddressLine")
        self.OptionalAddressLine = params.get("OptionalAddressLine")
        self.NeedHelp = params.get("NeedHelp")
        self.BreakerRequirement = params.get("BreakerRequirement")
        self.RedundantPower = params.get("RedundantPower")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.PostalCode = params.get("PostalCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        r"""
        :param Zone: 可用区名称
        :type Zone: str
        :param ZoneName: 可用区描述
        :type ZoneName: str
        :param ZoneId: 可用区ID
        :type ZoneId: int
        :param ZoneState: 可用区状态，包含AVAILABLE和UNAVAILABLE。AVAILABLE代表可用，UNAVAILABLE代表不可用。
        :type ZoneState: str
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.ZoneState = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.ZoneState = params.get("ZoneState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        