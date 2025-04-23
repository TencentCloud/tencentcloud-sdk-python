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
        :param _Size: cbs存储大小，单位TB
        :type Size: int
        :param _Type: cbs存储类型，默认为SSD
        :type Type: str
        """
        self._Size = None
        self._Type = None

    @property
    def Size(self):
        """cbs存储大小，单位TB
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Type(self):
        """cbs存储类型，默认为SSD
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Size = params.get("Size")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosCapacity(AbstractModel):
    """CDC集群内cos的容量信息

    """

    def __init__(self):
        r"""
        :param _TotalCapacity: 已购cos的总容量大小，单位GB
        :type TotalCapacity: float
        :param _TotalFreeCapacity: 剩余可用cos的容量大小，单位GB
        :type TotalFreeCapacity: float
        :param _TotalUsedCapacity: 已用cos的容量大小，单位GB
        :type TotalUsedCapacity: float
        """
        self._TotalCapacity = None
        self._TotalFreeCapacity = None
        self._TotalUsedCapacity = None

    @property
    def TotalCapacity(self):
        """已购cos的总容量大小，单位GB
        :rtype: float
        """
        return self._TotalCapacity

    @TotalCapacity.setter
    def TotalCapacity(self, TotalCapacity):
        self._TotalCapacity = TotalCapacity

    @property
    def TotalFreeCapacity(self):
        """剩余可用cos的容量大小，单位GB
        :rtype: float
        """
        return self._TotalFreeCapacity

    @TotalFreeCapacity.setter
    def TotalFreeCapacity(self, TotalFreeCapacity):
        self._TotalFreeCapacity = TotalFreeCapacity

    @property
    def TotalUsedCapacity(self):
        """已用cos的容量大小，单位GB
        :rtype: float
        """
        return self._TotalUsedCapacity

    @TotalUsedCapacity.setter
    def TotalUsedCapacity(self, TotalUsedCapacity):
        self._TotalUsedCapacity = TotalUsedCapacity


    def _deserialize(self, params):
        self._TotalCapacity = params.get("TotalCapacity")
        self._TotalFreeCapacity = params.get("TotalFreeCapacity")
        self._TotalUsedCapacity = params.get("TotalUsedCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosInfo(AbstractModel):
    """用于购买页面添加cos信息

    """

    def __init__(self):
        r"""
        :param _Size: COS存储大小，单位TB
        :type Size: int
        :param _Type: COS存储类型，默认为cos
        :type Type: str
        """
        self._Size = None
        self._Type = None

    @property
    def Size(self):
        """COS存储大小，单位TB
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Type(self):
        """COS存储类型，默认为cos
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Size = params.get("Size")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterImageCacheRequest(AbstractModel):
    """CreateDedicatedClusterImageCache请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 集群ID
        :type DedicatedClusterId: str
        :param _ImageId: 镜像ID
        :type ImageId: str
        """
        self._DedicatedClusterId = None
        self._ImageId = None

    @property
    def DedicatedClusterId(self):
        """集群ID
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def ImageId(self):
        """镜像ID
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterImageCacheResponse(AbstractModel):
    """CreateDedicatedClusterImageCache返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateDedicatedClusterOrderRequest(AbstractModel):
    """CreateDedicatedClusterOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 专用集群id
        :type DedicatedClusterId: str
        :param _DedicatedClusterTypes: order关联的专用集群类型数组
        :type DedicatedClusterTypes: list of DedicatedClusterTypeInfo
        :param _CosInfo: order关联的cos存储信息
        :type CosInfo: :class:`tencentcloud.cdc.v20201214.models.CosInfo`
        :param _CbsInfo: order关联的cbs存储信息
        :type CbsInfo: :class:`tencentcloud.cdc.v20201214.models.CbsInfo`
        :param _PurchaseSource: 购买来源，默认为cloudApi
        :type PurchaseSource: str
        :param _DedicatedClusterOrderId: 当调用API接口提交订单时，需要提交DedicatedClusterOrderId，此处DedicatedClusterOrderId是之前创建的订单，可通过DescribeDedicatedClusterOrders接口查询，这里传入DedicatedClusterOrderId用于调整订单和支付。
        :type DedicatedClusterOrderId: str
        """
        self._DedicatedClusterId = None
        self._DedicatedClusterTypes = None
        self._CosInfo = None
        self._CbsInfo = None
        self._PurchaseSource = None
        self._DedicatedClusterOrderId = None

    @property
    def DedicatedClusterId(self):
        """专用集群id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def DedicatedClusterTypes(self):
        """order关联的专用集群类型数组
        :rtype: list of DedicatedClusterTypeInfo
        """
        return self._DedicatedClusterTypes

    @DedicatedClusterTypes.setter
    def DedicatedClusterTypes(self, DedicatedClusterTypes):
        self._DedicatedClusterTypes = DedicatedClusterTypes

    @property
    def CosInfo(self):
        """order关联的cos存储信息
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CosInfo`
        """
        return self._CosInfo

    @CosInfo.setter
    def CosInfo(self, CosInfo):
        self._CosInfo = CosInfo

    @property
    def CbsInfo(self):
        """order关联的cbs存储信息
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CbsInfo`
        """
        return self._CbsInfo

    @CbsInfo.setter
    def CbsInfo(self, CbsInfo):
        self._CbsInfo = CbsInfo

    @property
    def PurchaseSource(self):
        """购买来源，默认为cloudApi
        :rtype: str
        """
        return self._PurchaseSource

    @PurchaseSource.setter
    def PurchaseSource(self, PurchaseSource):
        self._PurchaseSource = PurchaseSource

    @property
    def DedicatedClusterOrderId(self):
        """当调用API接口提交订单时，需要提交DedicatedClusterOrderId，此处DedicatedClusterOrderId是之前创建的订单，可通过DescribeDedicatedClusterOrders接口查询，这里传入DedicatedClusterOrderId用于调整订单和支付。
        :rtype: str
        """
        return self._DedicatedClusterOrderId

    @DedicatedClusterOrderId.setter
    def DedicatedClusterOrderId(self, DedicatedClusterOrderId):
        self._DedicatedClusterOrderId = DedicatedClusterOrderId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        if params.get("DedicatedClusterTypes") is not None:
            self._DedicatedClusterTypes = []
            for item in params.get("DedicatedClusterTypes"):
                obj = DedicatedClusterTypeInfo()
                obj._deserialize(item)
                self._DedicatedClusterTypes.append(obj)
        if params.get("CosInfo") is not None:
            self._CosInfo = CosInfo()
            self._CosInfo._deserialize(params.get("CosInfo"))
        if params.get("CbsInfo") is not None:
            self._CbsInfo = CbsInfo()
            self._CbsInfo._deserialize(params.get("CbsInfo"))
        self._PurchaseSource = params.get("PurchaseSource")
        self._DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterOrderResponse(AbstractModel):
    """CreateDedicatedClusterOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterOrderId: 专用集群订单id
        :type DedicatedClusterOrderId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DedicatedClusterOrderId = None
        self._RequestId = None

    @property
    def DedicatedClusterOrderId(self):
        """专用集群订单id
        :rtype: str
        """
        return self._DedicatedClusterOrderId

    @DedicatedClusterOrderId.setter
    def DedicatedClusterOrderId(self, DedicatedClusterOrderId):
        self._DedicatedClusterOrderId = DedicatedClusterOrderId

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
        self._DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        self._RequestId = params.get("RequestId")


class CreateDedicatedClusterRequest(AbstractModel):
    """CreateDedicatedCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteId: 专用集群所属的SiteId
        :type SiteId: str
        :param _Name: 专用集群的名称
        :type Name: str
        :param _Zone: 专用集群所属的可用区
        :type Zone: str
        :param _Description: 专用集群的描述
        :type Description: str
        """
        self._SiteId = None
        self._Name = None
        self._Zone = None
        self._Description = None

    @property
    def SiteId(self):
        """专用集群所属的SiteId
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def Name(self):
        """专用集群的名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Zone(self):
        """专用集群所属的可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Description(self):
        """专用集群的描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._Name = params.get("Name")
        self._Zone = params.get("Zone")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterResponse(AbstractModel):
    """CreateDedicatedCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 创建的专用集群id
        :type DedicatedClusterId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DedicatedClusterId = None
        self._RequestId = None

    @property
    def DedicatedClusterId(self):
        """创建的专用集群id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

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
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._RequestId = params.get("RequestId")


class CreateSiteRequest(AbstractModel):
    """CreateSite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 站点名称
        :type Name: str
        :param _Country: 站点所在国家
        :type Country: str
        :param _Province: 站点所在省份
        :type Province: str
        :param _City: 站点所在城市
        :type City: str
        :param _AddressLine: 站点所在地区的详细地址信息
        :type AddressLine: str
        :param _Description: 站点描述
        :type Description: str
        :param _Note: 注意事项
        :type Note: str
        :param _FiberType: 您将使用光纤类型将CDC设备连接到网络。有单模和多模两种选项。取值范围："MM","SM"
        :type FiberType: str
        :param _OpticalStandard: 您将CDC连接到网络时采用的光学标准。此字段取决于上行链路速度、光纤类型和到上游设备的距离。
        :type OpticalStandard: str
        :param _PowerConnectors: 电源连接器类型
        :type PowerConnectors: str
        :param _PowerFeedDrop: 从机架上方还是下方供电。取值范围：["UP","DOWN"]
        :type PowerFeedDrop: str
        :param _MaxWeight: 最大承重(KG)
        :type MaxWeight: int
        :param _PowerDrawKva: 功耗(KW)
        :type PowerDrawKva: int
        :param _UplinkSpeedGbps: 网络到腾讯云Region区域的上行链路速度(Gbps)
        :type UplinkSpeedGbps: int
        :param _UplinkCount: 将CDC连接到网络时，每台CDC网络设备(每个机架 2 台设备)使用的上行链路数量。
        :type UplinkCount: int
        :param _ConditionRequirement: 是否满足下面环境条件：
1、场地没有材料要求或验收标准会影响 CDC 设备配送和安装。
2、确定的机架位置包含:
温度范围为 41 到 104°F (5 到 40°C)。
湿度范围为 10°F (-12°C)和 8% RH (相对湿度)到 70°F(21°C)和 80% RH。
机架位置的气流方向为从前向后，且应具有足够的 CFM (每分钟立方英尺)。CFM 必须是 CDC 配置的 kVA 功耗值的 145.8 倍。
        :type ConditionRequirement: bool
        :param _DimensionRequirement: 是否满足下面的尺寸条件：
您的装货站台可以容纳一个机架箱(高 x 宽 x 深 = 94" x 54" x 48")。
您可以提供从机架(高 x 宽 x 深 = 80" x 24" x 48")交货地点到机架最终安置位置的明确通道。测量深度时，应包括站台、走廊通道、门、转弯、坡道、货梯，并将其他通道限制考虑在内。
在最终的 CDC安置位置，前部间隙可以为 48" 或更大，后部间隙可以为 24" 或更大。
        :type DimensionRequirement: bool
        :param _RedundantNetworking: 是否提供冗余的上游设备(交换机或路由器)，以便两台  网络设备都能连接到网络设备。
        :type RedundantNetworking: bool
        :param _PostalCode: 站点所在地区的邮编
        :type PostalCode: int
        :param _OptionalAddressLine: 站点所在地区的详细地址信息（补充）
        :type OptionalAddressLine: str
        :param _NeedHelp: 是否需要腾讯云团队协助完成机架支撑工作
        :type NeedHelp: bool
        :param _RedundantPower: 是否电源冗余
        :type RedundantPower: bool
        :param _BreakerRequirement: 上游断路器是否具备
        :type BreakerRequirement: bool
        """
        self._Name = None
        self._Country = None
        self._Province = None
        self._City = None
        self._AddressLine = None
        self._Description = None
        self._Note = None
        self._FiberType = None
        self._OpticalStandard = None
        self._PowerConnectors = None
        self._PowerFeedDrop = None
        self._MaxWeight = None
        self._PowerDrawKva = None
        self._UplinkSpeedGbps = None
        self._UplinkCount = None
        self._ConditionRequirement = None
        self._DimensionRequirement = None
        self._RedundantNetworking = None
        self._PostalCode = None
        self._OptionalAddressLine = None
        self._NeedHelp = None
        self._RedundantPower = None
        self._BreakerRequirement = None

    @property
    def Name(self):
        """站点名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Country(self):
        """站点所在国家
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """站点所在省份
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """站点所在城市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def AddressLine(self):
        """站点所在地区的详细地址信息
        :rtype: str
        """
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, AddressLine):
        self._AddressLine = AddressLine

    @property
    def Description(self):
        """站点描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Note(self):
        """注意事项
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def FiberType(self):
        """您将使用光纤类型将CDC设备连接到网络。有单模和多模两种选项。取值范围："MM","SM"
        :rtype: str
        """
        return self._FiberType

    @FiberType.setter
    def FiberType(self, FiberType):
        self._FiberType = FiberType

    @property
    def OpticalStandard(self):
        """您将CDC连接到网络时采用的光学标准。此字段取决于上行链路速度、光纤类型和到上游设备的距离。
        :rtype: str
        """
        return self._OpticalStandard

    @OpticalStandard.setter
    def OpticalStandard(self, OpticalStandard):
        self._OpticalStandard = OpticalStandard

    @property
    def PowerConnectors(self):
        """电源连接器类型
        :rtype: str
        """
        return self._PowerConnectors

    @PowerConnectors.setter
    def PowerConnectors(self, PowerConnectors):
        self._PowerConnectors = PowerConnectors

    @property
    def PowerFeedDrop(self):
        """从机架上方还是下方供电。取值范围：["UP","DOWN"]
        :rtype: str
        """
        return self._PowerFeedDrop

    @PowerFeedDrop.setter
    def PowerFeedDrop(self, PowerFeedDrop):
        self._PowerFeedDrop = PowerFeedDrop

    @property
    def MaxWeight(self):
        """最大承重(KG)
        :rtype: int
        """
        return self._MaxWeight

    @MaxWeight.setter
    def MaxWeight(self, MaxWeight):
        self._MaxWeight = MaxWeight

    @property
    def PowerDrawKva(self):
        """功耗(KW)
        :rtype: int
        """
        return self._PowerDrawKva

    @PowerDrawKva.setter
    def PowerDrawKva(self, PowerDrawKva):
        self._PowerDrawKva = PowerDrawKva

    @property
    def UplinkSpeedGbps(self):
        """网络到腾讯云Region区域的上行链路速度(Gbps)
        :rtype: int
        """
        return self._UplinkSpeedGbps

    @UplinkSpeedGbps.setter
    def UplinkSpeedGbps(self, UplinkSpeedGbps):
        self._UplinkSpeedGbps = UplinkSpeedGbps

    @property
    def UplinkCount(self):
        """将CDC连接到网络时，每台CDC网络设备(每个机架 2 台设备)使用的上行链路数量。
        :rtype: int
        """
        return self._UplinkCount

    @UplinkCount.setter
    def UplinkCount(self, UplinkCount):
        self._UplinkCount = UplinkCount

    @property
    def ConditionRequirement(self):
        """是否满足下面环境条件：
1、场地没有材料要求或验收标准会影响 CDC 设备配送和安装。
2、确定的机架位置包含:
温度范围为 41 到 104°F (5 到 40°C)。
湿度范围为 10°F (-12°C)和 8% RH (相对湿度)到 70°F(21°C)和 80% RH。
机架位置的气流方向为从前向后，且应具有足够的 CFM (每分钟立方英尺)。CFM 必须是 CDC 配置的 kVA 功耗值的 145.8 倍。
        :rtype: bool
        """
        return self._ConditionRequirement

    @ConditionRequirement.setter
    def ConditionRequirement(self, ConditionRequirement):
        self._ConditionRequirement = ConditionRequirement

    @property
    def DimensionRequirement(self):
        """是否满足下面的尺寸条件：
您的装货站台可以容纳一个机架箱(高 x 宽 x 深 = 94" x 54" x 48")。
您可以提供从机架(高 x 宽 x 深 = 80" x 24" x 48")交货地点到机架最终安置位置的明确通道。测量深度时，应包括站台、走廊通道、门、转弯、坡道、货梯，并将其他通道限制考虑在内。
在最终的 CDC安置位置，前部间隙可以为 48" 或更大，后部间隙可以为 24" 或更大。
        :rtype: bool
        """
        return self._DimensionRequirement

    @DimensionRequirement.setter
    def DimensionRequirement(self, DimensionRequirement):
        self._DimensionRequirement = DimensionRequirement

    @property
    def RedundantNetworking(self):
        """是否提供冗余的上游设备(交换机或路由器)，以便两台  网络设备都能连接到网络设备。
        :rtype: bool
        """
        return self._RedundantNetworking

    @RedundantNetworking.setter
    def RedundantNetworking(self, RedundantNetworking):
        self._RedundantNetworking = RedundantNetworking

    @property
    def PostalCode(self):
        """站点所在地区的邮编
        :rtype: int
        """
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def OptionalAddressLine(self):
        """站点所在地区的详细地址信息（补充）
        :rtype: str
        """
        return self._OptionalAddressLine

    @OptionalAddressLine.setter
    def OptionalAddressLine(self, OptionalAddressLine):
        self._OptionalAddressLine = OptionalAddressLine

    @property
    def NeedHelp(self):
        """是否需要腾讯云团队协助完成机架支撑工作
        :rtype: bool
        """
        return self._NeedHelp

    @NeedHelp.setter
    def NeedHelp(self, NeedHelp):
        self._NeedHelp = NeedHelp

    @property
    def RedundantPower(self):
        """是否电源冗余
        :rtype: bool
        """
        return self._RedundantPower

    @RedundantPower.setter
    def RedundantPower(self, RedundantPower):
        self._RedundantPower = RedundantPower

    @property
    def BreakerRequirement(self):
        """上游断路器是否具备
        :rtype: bool
        """
        return self._BreakerRequirement

    @BreakerRequirement.setter
    def BreakerRequirement(self, BreakerRequirement):
        self._BreakerRequirement = BreakerRequirement


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._AddressLine = params.get("AddressLine")
        self._Description = params.get("Description")
        self._Note = params.get("Note")
        self._FiberType = params.get("FiberType")
        self._OpticalStandard = params.get("OpticalStandard")
        self._PowerConnectors = params.get("PowerConnectors")
        self._PowerFeedDrop = params.get("PowerFeedDrop")
        self._MaxWeight = params.get("MaxWeight")
        self._PowerDrawKva = params.get("PowerDrawKva")
        self._UplinkSpeedGbps = params.get("UplinkSpeedGbps")
        self._UplinkCount = params.get("UplinkCount")
        self._ConditionRequirement = params.get("ConditionRequirement")
        self._DimensionRequirement = params.get("DimensionRequirement")
        self._RedundantNetworking = params.get("RedundantNetworking")
        self._PostalCode = params.get("PostalCode")
        self._OptionalAddressLine = params.get("OptionalAddressLine")
        self._NeedHelp = params.get("NeedHelp")
        self._RedundantPower = params.get("RedundantPower")
        self._BreakerRequirement = params.get("BreakerRequirement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSiteResponse(AbstractModel):
    """CreateSite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteId: 创建Site生成的id
        :type SiteId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SiteId = None
        self._RequestId = None

    @property
    def SiteId(self):
        """创建Site生成的id
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

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
        self._SiteId = params.get("SiteId")
        self._RequestId = params.get("RequestId")


class DedicatedCluster(AbstractModel):
    """专用集群列表

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 专用集群id。如"cluster-xxxxx"。
        :type DedicatedClusterId: str
        :param _Zone: 专用集群所属可用区名称。
        :type Zone: str
        :param _Description: 专用集群的描述。
        :type Description: str
        :param _Name: 专用集群的名称。
        :type Name: str
        :param _LifecycleStatus: 专用集群的生命周期。如"PENDING"。
        :type LifecycleStatus: str
        :param _CreateTime: 专用集群的创建时间。
        :type CreateTime: str
        :param _SiteId: 专用集群所属的站点id。
        :type SiteId: str
        :param _RunningStatus: 专用集群的运营状态
        :type RunningStatus: str
        """
        self._DedicatedClusterId = None
        self._Zone = None
        self._Description = None
        self._Name = None
        self._LifecycleStatus = None
        self._CreateTime = None
        self._SiteId = None
        self._RunningStatus = None

    @property
    def DedicatedClusterId(self):
        """专用集群id。如"cluster-xxxxx"。
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def Zone(self):
        """专用集群所属可用区名称。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Description(self):
        """专用集群的描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        """专用集群的名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LifecycleStatus(self):
        """专用集群的生命周期。如"PENDING"。
        :rtype: str
        """
        return self._LifecycleStatus

    @LifecycleStatus.setter
    def LifecycleStatus(self, LifecycleStatus):
        self._LifecycleStatus = LifecycleStatus

    @property
    def CreateTime(self):
        """专用集群的创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SiteId(self):
        """专用集群所属的站点id。
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def RunningStatus(self):
        """专用集群的运营状态
        :rtype: str
        """
        return self._RunningStatus

    @RunningStatus.setter
    def RunningStatus(self, RunningStatus):
        self._RunningStatus = RunningStatus


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._Zone = params.get("Zone")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._LifecycleStatus = params.get("LifecycleStatus")
        self._CreateTime = params.get("CreateTime")
        self._SiteId = params.get("SiteId")
        self._RunningStatus = params.get("RunningStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterInstanceType(AbstractModel):
    """专用宿主机支持的实例规格列表

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _InstanceType: 规格名称
        :type InstanceType: str
        :param _NetworkCard: 网卡类型，例如：25代表25G网卡
        :type NetworkCard: int
        :param _Cpu: 实例的CPU核数，单位：核。
        :type Cpu: int
        :param _Memory: 实例内存容量，单位：`GB`。
        :type Memory: int
        :param _InstanceFamily: 实例机型系列。
        :type InstanceFamily: str
        :param _TypeName: 机型名称。
        :type TypeName: str
        :param _StorageBlockAmount: 本地存储块数量。
        :type StorageBlockAmount: int
        :param _InstanceBandwidth: 内网带宽，单位Gbps。
        :type InstanceBandwidth: float
        :param _InstancePps: 网络收发包能力，单位万PPS。
        :type InstancePps: int
        :param _CpuType: 处理器型号。
        :type CpuType: str
        :param _Gpu: 实例的GPU数量。
        :type Gpu: int
        :param _Fpga: 实例的FPGA数量。
        :type Fpga: int
        :param _Remark: 机型描述
        :type Remark: str
        :param _Status: 实例是否售卖。取值范围： <br><li>SELL：表示实例可购买<br></li><li>SOLD_OUT：表示实例已售罄。</li>
        :type Status: str
        """
        self._Zone = None
        self._InstanceType = None
        self._NetworkCard = None
        self._Cpu = None
        self._Memory = None
        self._InstanceFamily = None
        self._TypeName = None
        self._StorageBlockAmount = None
        self._InstanceBandwidth = None
        self._InstancePps = None
        self._CpuType = None
        self._Gpu = None
        self._Fpga = None
        self._Remark = None
        self._Status = None

    @property
    def Zone(self):
        """可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        """规格名称
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def NetworkCard(self):
        """网卡类型，例如：25代表25G网卡
        :rtype: int
        """
        return self._NetworkCard

    @NetworkCard.setter
    def NetworkCard(self, NetworkCard):
        self._NetworkCard = NetworkCard

    @property
    def Cpu(self):
        """实例的CPU核数，单位：核。
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """实例内存容量，单位：`GB`。
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceFamily(self):
        """实例机型系列。
        :rtype: str
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def TypeName(self):
        """机型名称。
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def StorageBlockAmount(self):
        """本地存储块数量。
        :rtype: int
        """
        return self._StorageBlockAmount

    @StorageBlockAmount.setter
    def StorageBlockAmount(self, StorageBlockAmount):
        self._StorageBlockAmount = StorageBlockAmount

    @property
    def InstanceBandwidth(self):
        """内网带宽，单位Gbps。
        :rtype: float
        """
        return self._InstanceBandwidth

    @InstanceBandwidth.setter
    def InstanceBandwidth(self, InstanceBandwidth):
        self._InstanceBandwidth = InstanceBandwidth

    @property
    def InstancePps(self):
        """网络收发包能力，单位万PPS。
        :rtype: int
        """
        return self._InstancePps

    @InstancePps.setter
    def InstancePps(self, InstancePps):
        self._InstancePps = InstancePps

    @property
    def CpuType(self):
        """处理器型号。
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def Gpu(self):
        """实例的GPU数量。
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def Fpga(self):
        """实例的FPGA数量。
        :rtype: int
        """
        return self._Fpga

    @Fpga.setter
    def Fpga(self, Fpga):
        self._Fpga = Fpga

    @property
    def Remark(self):
        """机型描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Status(self):
        """实例是否售卖。取值范围： <br><li>SELL：表示实例可购买<br></li><li>SOLD_OUT：表示实例已售罄。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        self._NetworkCard = params.get("NetworkCard")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._InstanceFamily = params.get("InstanceFamily")
        self._TypeName = params.get("TypeName")
        self._StorageBlockAmount = params.get("StorageBlockAmount")
        self._InstanceBandwidth = params.get("InstanceBandwidth")
        self._InstancePps = params.get("InstancePps")
        self._CpuType = params.get("CpuType")
        self._Gpu = params.get("Gpu")
        self._Fpga = params.get("Fpga")
        self._Remark = params.get("Remark")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterOrder(AbstractModel):
    """专用集群订单

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 专用集群id
        :type DedicatedClusterId: str
        :param _DedicatedClusterTypeId: 专用集群类型id（移到下一层级，已经废弃，后续将删除）
        :type DedicatedClusterTypeId: str
        :param _SupportedStorageType: 支持的存储类型列表（移到下一层级，已经废弃，后续将删除）
        :type SupportedStorageType: list of str
        :param _SupportedUplinkSpeed: 支持的上连交换机的链路传输速率(GiB)（移到下一层级，已经废弃，后续将删除）
        :type SupportedUplinkSpeed: list of int
        :param _SupportedInstanceFamily: 支持的实例族列表（移到下一层级，已经废弃，后续将删除）
        :type SupportedInstanceFamily: list of str
        :param _Weight: 地板承重要求(KG)
        :type Weight: int
        :param _PowerDraw: 功率要求(KW)
        :type PowerDraw: float
        :param _OrderStatus: 订单状态
        :type OrderStatus: str
        :param _CreateTime: 订单创建的时间
        :type CreateTime: str
        :param _DedicatedClusterOrderId: 大订单ID
        :type DedicatedClusterOrderId: str
        :param _Action: 订单类型，创建CREATE或扩容EXTEND
        :type Action: str
        :param _DedicatedClusterOrderItems: 子订单详情列表
        :type DedicatedClusterOrderItems: list of DedicatedClusterOrderItem
        :param _Cpu: cpu值
        :type Cpu: int
        :param _Mem: mem值
        :type Mem: int
        :param _Gpu: gpu值
        :type Gpu: int
        :param _PayStatus: 0代表未支付，1代表已支付
        :type PayStatus: int
        :param _PayType: 支付方式，一次性、按月、按年
        :type PayType: str
        :param _TimeUnit: 购买时长的单位
        :type TimeUnit: str
        :param _TimeSpan: 购买时长
        :type TimeSpan: int
        :param _OrderType: 订单类型
        :type OrderType: str
        :param _CheckStatus: 验收状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckStatus: str
        :param _DeliverExpectTime: 交付预期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverExpectTime: str
        :param _DeliverFinishTime: 交付实际完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverFinishTime: str
        :param _CheckExpectTime: 验收预期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckExpectTime: str
        :param _CheckFinishTime: 验收实际完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckFinishTime: str
        :param _OrderSLA: 订单SLA
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderSLA: str
        :param _OrderPayPlan: 订单支付计划
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderPayPlan: str
        """
        self._DedicatedClusterId = None
        self._DedicatedClusterTypeId = None
        self._SupportedStorageType = None
        self._SupportedUplinkSpeed = None
        self._SupportedInstanceFamily = None
        self._Weight = None
        self._PowerDraw = None
        self._OrderStatus = None
        self._CreateTime = None
        self._DedicatedClusterOrderId = None
        self._Action = None
        self._DedicatedClusterOrderItems = None
        self._Cpu = None
        self._Mem = None
        self._Gpu = None
        self._PayStatus = None
        self._PayType = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._OrderType = None
        self._CheckStatus = None
        self._DeliverExpectTime = None
        self._DeliverFinishTime = None
        self._CheckExpectTime = None
        self._CheckFinishTime = None
        self._OrderSLA = None
        self._OrderPayPlan = None

    @property
    def DedicatedClusterId(self):
        """专用集群id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def DedicatedClusterTypeId(self):
        """专用集群类型id（移到下一层级，已经废弃，后续将删除）
        :rtype: str
        """
        return self._DedicatedClusterTypeId

    @DedicatedClusterTypeId.setter
    def DedicatedClusterTypeId(self, DedicatedClusterTypeId):
        self._DedicatedClusterTypeId = DedicatedClusterTypeId

    @property
    def SupportedStorageType(self):
        """支持的存储类型列表（移到下一层级，已经废弃，后续将删除）
        :rtype: list of str
        """
        return self._SupportedStorageType

    @SupportedStorageType.setter
    def SupportedStorageType(self, SupportedStorageType):
        self._SupportedStorageType = SupportedStorageType

    @property
    def SupportedUplinkSpeed(self):
        """支持的上连交换机的链路传输速率(GiB)（移到下一层级，已经废弃，后续将删除）
        :rtype: list of int
        """
        return self._SupportedUplinkSpeed

    @SupportedUplinkSpeed.setter
    def SupportedUplinkSpeed(self, SupportedUplinkSpeed):
        self._SupportedUplinkSpeed = SupportedUplinkSpeed

    @property
    def SupportedInstanceFamily(self):
        """支持的实例族列表（移到下一层级，已经废弃，后续将删除）
        :rtype: list of str
        """
        return self._SupportedInstanceFamily

    @SupportedInstanceFamily.setter
    def SupportedInstanceFamily(self, SupportedInstanceFamily):
        self._SupportedInstanceFamily = SupportedInstanceFamily

    @property
    def Weight(self):
        """地板承重要求(KG)
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PowerDraw(self):
        """功率要求(KW)
        :rtype: float
        """
        return self._PowerDraw

    @PowerDraw.setter
    def PowerDraw(self, PowerDraw):
        self._PowerDraw = PowerDraw

    @property
    def OrderStatus(self):
        """订单状态
        :rtype: str
        """
        return self._OrderStatus

    @OrderStatus.setter
    def OrderStatus(self, OrderStatus):
        self._OrderStatus = OrderStatus

    @property
    def CreateTime(self):
        """订单创建的时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DedicatedClusterOrderId(self):
        """大订单ID
        :rtype: str
        """
        return self._DedicatedClusterOrderId

    @DedicatedClusterOrderId.setter
    def DedicatedClusterOrderId(self, DedicatedClusterOrderId):
        self._DedicatedClusterOrderId = DedicatedClusterOrderId

    @property
    def Action(self):
        """订单类型，创建CREATE或扩容EXTEND
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def DedicatedClusterOrderItems(self):
        """子订单详情列表
        :rtype: list of DedicatedClusterOrderItem
        """
        return self._DedicatedClusterOrderItems

    @DedicatedClusterOrderItems.setter
    def DedicatedClusterOrderItems(self, DedicatedClusterOrderItems):
        self._DedicatedClusterOrderItems = DedicatedClusterOrderItems

    @property
    def Cpu(self):
        """cpu值
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        """mem值
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Gpu(self):
        """gpu值
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def PayStatus(self):
        """0代表未支付，1代表已支付
        :rtype: int
        """
        return self._PayStatus

    @PayStatus.setter
    def PayStatus(self, PayStatus):
        self._PayStatus = PayStatus

    @property
    def PayType(self):
        """支付方式，一次性、按月、按年
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def TimeUnit(self):
        """购买时长的单位
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        """购买时长
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def OrderType(self):
        """订单类型
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def CheckStatus(self):
        """验收状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus

    @property
    def DeliverExpectTime(self):
        """交付预期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeliverExpectTime

    @DeliverExpectTime.setter
    def DeliverExpectTime(self, DeliverExpectTime):
        self._DeliverExpectTime = DeliverExpectTime

    @property
    def DeliverFinishTime(self):
        """交付实际完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeliverFinishTime

    @DeliverFinishTime.setter
    def DeliverFinishTime(self, DeliverFinishTime):
        self._DeliverFinishTime = DeliverFinishTime

    @property
    def CheckExpectTime(self):
        """验收预期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CheckExpectTime

    @CheckExpectTime.setter
    def CheckExpectTime(self, CheckExpectTime):
        self._CheckExpectTime = CheckExpectTime

    @property
    def CheckFinishTime(self):
        """验收实际完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CheckFinishTime

    @CheckFinishTime.setter
    def CheckFinishTime(self, CheckFinishTime):
        self._CheckFinishTime = CheckFinishTime

    @property
    def OrderSLA(self):
        """订单SLA
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrderSLA

    @OrderSLA.setter
    def OrderSLA(self, OrderSLA):
        self._OrderSLA = OrderSLA

    @property
    def OrderPayPlan(self):
        """订单支付计划
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrderPayPlan

    @OrderPayPlan.setter
    def OrderPayPlan(self, OrderPayPlan):
        self._OrderPayPlan = OrderPayPlan


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._DedicatedClusterTypeId = params.get("DedicatedClusterTypeId")
        self._SupportedStorageType = params.get("SupportedStorageType")
        self._SupportedUplinkSpeed = params.get("SupportedUplinkSpeed")
        self._SupportedInstanceFamily = params.get("SupportedInstanceFamily")
        self._Weight = params.get("Weight")
        self._PowerDraw = params.get("PowerDraw")
        self._OrderStatus = params.get("OrderStatus")
        self._CreateTime = params.get("CreateTime")
        self._DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        self._Action = params.get("Action")
        if params.get("DedicatedClusterOrderItems") is not None:
            self._DedicatedClusterOrderItems = []
            for item in params.get("DedicatedClusterOrderItems"):
                obj = DedicatedClusterOrderItem()
                obj._deserialize(item)
                self._DedicatedClusterOrderItems.append(obj)
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Gpu = params.get("Gpu")
        self._PayStatus = params.get("PayStatus")
        self._PayType = params.get("PayType")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._OrderType = params.get("OrderType")
        self._CheckStatus = params.get("CheckStatus")
        self._DeliverExpectTime = params.get("DeliverExpectTime")
        self._DeliverFinishTime = params.get("DeliverFinishTime")
        self._CheckExpectTime = params.get("CheckExpectTime")
        self._CheckFinishTime = params.get("CheckFinishTime")
        self._OrderSLA = params.get("OrderSLA")
        self._OrderPayPlan = params.get("OrderPayPlan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterOrderItem(AbstractModel):
    """专用集群子订单

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterTypeId: 专用集群类型id
        :type DedicatedClusterTypeId: str
        :param _SupportedStorageType: 支持的存储类型列表
        :type SupportedStorageType: list of str
        :param _SupportedUplinkSpeed: 支持的上连交换机的链路传输速率(GiB)
        :type SupportedUplinkSpeed: list of int
        :param _SupportedInstanceFamily: 支持的实例族列表
        :type SupportedInstanceFamily: list of str
        :param _Weight: 地板承重要求(KG)
        :type Weight: int
        :param _PowerDraw: 功率要求(KW)
        :type PowerDraw: float
        :param _SubOrderStatus: 订单状态
        :type SubOrderStatus: str
        :param _CreateTime: 订单创建的时间
        :type CreateTime: str
        :param _SubOrderId: 子订单ID
        :type SubOrderId: str
        :param _Count: 关联的集群规格数量
        :type Count: int
        :param _Name: 规格简单描述
        :type Name: str
        :param _Description: 规格详细描述
        :type Description: str
        :param _TotalCpu: CPU数
        :type TotalCpu: int
        :param _TotalMem: 内存数
        :type TotalMem: int
        :param _TotalGpu: GPU数
        :type TotalGpu: int
        :param _TypeName: 规格英文名
        :type TypeName: str
        :param _ComputeFormat: 规格展示
        :type ComputeFormat: str
        :param _TypeFamily: 规格类型
        :type TypeFamily: str
        :param _SubOrderPayStatus: 0未支付，1已支付
        :type SubOrderPayStatus: int
        """
        self._DedicatedClusterTypeId = None
        self._SupportedStorageType = None
        self._SupportedUplinkSpeed = None
        self._SupportedInstanceFamily = None
        self._Weight = None
        self._PowerDraw = None
        self._SubOrderStatus = None
        self._CreateTime = None
        self._SubOrderId = None
        self._Count = None
        self._Name = None
        self._Description = None
        self._TotalCpu = None
        self._TotalMem = None
        self._TotalGpu = None
        self._TypeName = None
        self._ComputeFormat = None
        self._TypeFamily = None
        self._SubOrderPayStatus = None

    @property
    def DedicatedClusterTypeId(self):
        """专用集群类型id
        :rtype: str
        """
        return self._DedicatedClusterTypeId

    @DedicatedClusterTypeId.setter
    def DedicatedClusterTypeId(self, DedicatedClusterTypeId):
        self._DedicatedClusterTypeId = DedicatedClusterTypeId

    @property
    def SupportedStorageType(self):
        """支持的存储类型列表
        :rtype: list of str
        """
        return self._SupportedStorageType

    @SupportedStorageType.setter
    def SupportedStorageType(self, SupportedStorageType):
        self._SupportedStorageType = SupportedStorageType

    @property
    def SupportedUplinkSpeed(self):
        """支持的上连交换机的链路传输速率(GiB)
        :rtype: list of int
        """
        return self._SupportedUplinkSpeed

    @SupportedUplinkSpeed.setter
    def SupportedUplinkSpeed(self, SupportedUplinkSpeed):
        self._SupportedUplinkSpeed = SupportedUplinkSpeed

    @property
    def SupportedInstanceFamily(self):
        """支持的实例族列表
        :rtype: list of str
        """
        return self._SupportedInstanceFamily

    @SupportedInstanceFamily.setter
    def SupportedInstanceFamily(self, SupportedInstanceFamily):
        self._SupportedInstanceFamily = SupportedInstanceFamily

    @property
    def Weight(self):
        """地板承重要求(KG)
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PowerDraw(self):
        """功率要求(KW)
        :rtype: float
        """
        return self._PowerDraw

    @PowerDraw.setter
    def PowerDraw(self, PowerDraw):
        self._PowerDraw = PowerDraw

    @property
    def SubOrderStatus(self):
        """订单状态
        :rtype: str
        """
        return self._SubOrderStatus

    @SubOrderStatus.setter
    def SubOrderStatus(self, SubOrderStatus):
        self._SubOrderStatus = SubOrderStatus

    @property
    def CreateTime(self):
        """订单创建的时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SubOrderId(self):
        """子订单ID
        :rtype: str
        """
        return self._SubOrderId

    @SubOrderId.setter
    def SubOrderId(self, SubOrderId):
        self._SubOrderId = SubOrderId

    @property
    def Count(self):
        """关联的集群规格数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Name(self):
        """规格简单描述
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """规格详细描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TotalCpu(self):
        """CPU数
        :rtype: int
        """
        return self._TotalCpu

    @TotalCpu.setter
    def TotalCpu(self, TotalCpu):
        self._TotalCpu = TotalCpu

    @property
    def TotalMem(self):
        """内存数
        :rtype: int
        """
        return self._TotalMem

    @TotalMem.setter
    def TotalMem(self, TotalMem):
        self._TotalMem = TotalMem

    @property
    def TotalGpu(self):
        """GPU数
        :rtype: int
        """
        return self._TotalGpu

    @TotalGpu.setter
    def TotalGpu(self, TotalGpu):
        self._TotalGpu = TotalGpu

    @property
    def TypeName(self):
        """规格英文名
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def ComputeFormat(self):
        """规格展示
        :rtype: str
        """
        return self._ComputeFormat

    @ComputeFormat.setter
    def ComputeFormat(self, ComputeFormat):
        self._ComputeFormat = ComputeFormat

    @property
    def TypeFamily(self):
        """规格类型
        :rtype: str
        """
        return self._TypeFamily

    @TypeFamily.setter
    def TypeFamily(self, TypeFamily):
        self._TypeFamily = TypeFamily

    @property
    def SubOrderPayStatus(self):
        """0未支付，1已支付
        :rtype: int
        """
        return self._SubOrderPayStatus

    @SubOrderPayStatus.setter
    def SubOrderPayStatus(self, SubOrderPayStatus):
        self._SubOrderPayStatus = SubOrderPayStatus


    def _deserialize(self, params):
        self._DedicatedClusterTypeId = params.get("DedicatedClusterTypeId")
        self._SupportedStorageType = params.get("SupportedStorageType")
        self._SupportedUplinkSpeed = params.get("SupportedUplinkSpeed")
        self._SupportedInstanceFamily = params.get("SupportedInstanceFamily")
        self._Weight = params.get("Weight")
        self._PowerDraw = params.get("PowerDraw")
        self._SubOrderStatus = params.get("SubOrderStatus")
        self._CreateTime = params.get("CreateTime")
        self._SubOrderId = params.get("SubOrderId")
        self._Count = params.get("Count")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._TotalCpu = params.get("TotalCpu")
        self._TotalMem = params.get("TotalMem")
        self._TotalGpu = params.get("TotalGpu")
        self._TypeName = params.get("TypeName")
        self._ComputeFormat = params.get("ComputeFormat")
        self._TypeFamily = params.get("TypeFamily")
        self._SubOrderPayStatus = params.get("SubOrderPayStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterType(AbstractModel):
    """专用集群配置

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterTypeId: 配置id
        :type DedicatedClusterTypeId: str
        :param _Description: 配置描述，对应描述
        :type Description: str
        :param _Name: 配置名称，对应计算资源类型
        :type Name: str
        :param _CreateTime: 创建配置的时间
        :type CreateTime: str
        :param _SupportedStorageType: 支持的存储类型列表
        :type SupportedStorageType: list of str
        :param _SupportedUplinkGiB: 支持的上连交换机的链路传输速率
        :type SupportedUplinkGiB: list of int
        :param _SupportedInstanceFamily: 支持的实例族列表
        :type SupportedInstanceFamily: list of str
        :param _Weight: 地板承重要求(KG)
        :type Weight: int
        :param _PowerDrawKva: 功率要求(KW)
        :type PowerDrawKva: float
        :param _ComputeFormatDesc: 显示计算资源规格详情，存储等资源不显示
        :type ComputeFormatDesc: str
        """
        self._DedicatedClusterTypeId = None
        self._Description = None
        self._Name = None
        self._CreateTime = None
        self._SupportedStorageType = None
        self._SupportedUplinkGiB = None
        self._SupportedInstanceFamily = None
        self._Weight = None
        self._PowerDrawKva = None
        self._ComputeFormatDesc = None

    @property
    def DedicatedClusterTypeId(self):
        """配置id
        :rtype: str
        """
        return self._DedicatedClusterTypeId

    @DedicatedClusterTypeId.setter
    def DedicatedClusterTypeId(self, DedicatedClusterTypeId):
        self._DedicatedClusterTypeId = DedicatedClusterTypeId

    @property
    def Description(self):
        """配置描述，对应描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        """配置名称，对应计算资源类型
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        """创建配置的时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SupportedStorageType(self):
        """支持的存储类型列表
        :rtype: list of str
        """
        return self._SupportedStorageType

    @SupportedStorageType.setter
    def SupportedStorageType(self, SupportedStorageType):
        self._SupportedStorageType = SupportedStorageType

    @property
    def SupportedUplinkGiB(self):
        """支持的上连交换机的链路传输速率
        :rtype: list of int
        """
        return self._SupportedUplinkGiB

    @SupportedUplinkGiB.setter
    def SupportedUplinkGiB(self, SupportedUplinkGiB):
        self._SupportedUplinkGiB = SupportedUplinkGiB

    @property
    def SupportedInstanceFamily(self):
        """支持的实例族列表
        :rtype: list of str
        """
        return self._SupportedInstanceFamily

    @SupportedInstanceFamily.setter
    def SupportedInstanceFamily(self, SupportedInstanceFamily):
        self._SupportedInstanceFamily = SupportedInstanceFamily

    @property
    def Weight(self):
        """地板承重要求(KG)
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PowerDrawKva(self):
        """功率要求(KW)
        :rtype: float
        """
        return self._PowerDrawKva

    @PowerDrawKva.setter
    def PowerDrawKva(self, PowerDrawKva):
        self._PowerDrawKva = PowerDrawKva

    @property
    def ComputeFormatDesc(self):
        """显示计算资源规格详情，存储等资源不显示
        :rtype: str
        """
        return self._ComputeFormatDesc

    @ComputeFormatDesc.setter
    def ComputeFormatDesc(self, ComputeFormatDesc):
        self._ComputeFormatDesc = ComputeFormatDesc


    def _deserialize(self, params):
        self._DedicatedClusterTypeId = params.get("DedicatedClusterTypeId")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        self._SupportedStorageType = params.get("SupportedStorageType")
        self._SupportedUplinkGiB = params.get("SupportedUplinkGiB")
        self._SupportedInstanceFamily = params.get("SupportedInstanceFamily")
        self._Weight = params.get("Weight")
        self._PowerDrawKva = params.get("PowerDrawKva")
        self._ComputeFormatDesc = params.get("ComputeFormatDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterTypeInfo(AbstractModel):
    """DedicatedClusterType => (Id, Count)

    """

    def __init__(self):
        r"""
        :param _Id: 集群类型Id
        :type Id: str
        :param _Count: 集群类型个数
        :type Count: int
        """
        self._Id = None
        self._Count = None

    @property
    def Id(self):
        """集群类型Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Count(self):
        """集群类型个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDedicatedClusterImageCacheRequest(AbstractModel):
    """DeleteDedicatedClusterImageCache请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 集群id
        :type DedicatedClusterId: str
        :param _ImageId: 镜像id
        :type ImageId: str
        """
        self._DedicatedClusterId = None
        self._ImageId = None

    @property
    def DedicatedClusterId(self):
        """集群id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def ImageId(self):
        """镜像id
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDedicatedClusterImageCacheResponse(AbstractModel):
    """DeleteDedicatedClusterImageCache返回参数结构体

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


class DeleteDedicatedClustersRequest(AbstractModel):
    """DeleteDedicatedClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterIds: 要删除的专用集群id
        :type DedicatedClusterIds: list of str
        """
        self._DedicatedClusterIds = None

    @property
    def DedicatedClusterIds(self):
        """要删除的专用集群id
        :rtype: list of str
        """
        return self._DedicatedClusterIds

    @DedicatedClusterIds.setter
    def DedicatedClusterIds(self, DedicatedClusterIds):
        self._DedicatedClusterIds = DedicatedClusterIds


    def _deserialize(self, params):
        self._DedicatedClusterIds = params.get("DedicatedClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDedicatedClustersResponse(AbstractModel):
    """DeleteDedicatedClusters返回参数结构体

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


class DeleteSitesRequest(AbstractModel):
    """DeleteSites请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteIds: 要删除的站点id列表
        :type SiteIds: list of str
        """
        self._SiteIds = None

    @property
    def SiteIds(self):
        """要删除的站点id列表
        :rtype: list of str
        """
        return self._SiteIds

    @SiteIds.setter
    def SiteIds(self, SiteIds):
        self._SiteIds = SiteIds


    def _deserialize(self, params):
        self._SiteIds = params.get("SiteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSitesResponse(AbstractModel):
    """DeleteSites返回参数结构体

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


class DescribeDedicatedClusterCbsStatisticsRequest(AbstractModel):
    """DescribeDedicatedClusterCbsStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 查询的专用集群id
        :type DedicatedClusterId: str
        :param _SetId: 云硬盘仓库id
        :type SetId: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Period: 时间范围精度，1分钟(ONE_MINUTE)/5分钟(FIVE_MINUTE)
        :type Period: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20
        :type Limit: int
        """
        self._DedicatedClusterId = None
        self._SetId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None
        self._Offset = None
        self._Limit = None

    @property
    def DedicatedClusterId(self):
        """查询的专用集群id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def SetId(self):
        """云硬盘仓库id
        :rtype: str
        """
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

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
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        """时间范围精度，1分钟(ONE_MINUTE)/5分钟(FIVE_MINUTE)
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
        """返回数量，默认为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._SetId = params.get("SetId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterCbsStatisticsResponse(AbstractModel):
    """DescribeDedicatedClusterCbsStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SetList: 云硬盘仓库信息
        :type SetList: list of SetInfo
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SetList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SetList(self):
        """云硬盘仓库信息
        :rtype: list of SetInfo
        """
        return self._SetList

    @SetList.setter
    def SetList(self, SetList):
        self._SetList = SetList

    @property
    def TotalCount(self):
        """总数
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
        if params.get("SetList") is not None:
            self._SetList = []
            for item in params.get("SetList"):
                obj = SetInfo()
                obj._deserialize(item)
                self._SetList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterCosCapacityRequest(AbstractModel):
    """DescribeDedicatedClusterCosCapacity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 查询的专用集群id
        :type DedicatedClusterId: str
        """
        self._DedicatedClusterId = None

    @property
    def DedicatedClusterId(self):
        """查询的专用集群id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterCosCapacityResponse(AbstractModel):
    """DescribeDedicatedClusterCosCapacity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CosCapacity: 本集群内cos容量信息，单位：‘GB’
        :type CosCapacity: :class:`tencentcloud.cdc.v20201214.models.CosCapacity`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CosCapacity = None
        self._RequestId = None

    @property
    def CosCapacity(self):
        """本集群内cos容量信息，单位：‘GB’
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CosCapacity`
        """
        return self._CosCapacity

    @CosCapacity.setter
    def CosCapacity(self, CosCapacity):
        self._CosCapacity = CosCapacity

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
        if params.get("CosCapacity") is not None:
            self._CosCapacity = CosCapacity()
            self._CosCapacity._deserialize(params.get("CosCapacity"))
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterHostStatisticsRequest(AbstractModel):
    """DescribeDedicatedClusterHostStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 查询的专用集群id
        :type DedicatedClusterId: str
        :param _HostId: 宿主机id
        :type HostId: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Period: 时间范围精度，1分钟(ONE_MINUTE)/5分钟(FIVE_MINUTE)
        :type Period: str
        """
        self._DedicatedClusterId = None
        self._HostId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def DedicatedClusterId(self):
        """查询的专用集群id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def HostId(self):
        """宿主机id
        :rtype: str
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

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
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        """时间范围精度，1分钟(ONE_MINUTE)/5分钟(FIVE_MINUTE)
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._HostId = params.get("HostId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterHostStatisticsResponse(AbstractModel):
    """DescribeDedicatedClusterHostStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HostStatisticSet: 该集群内宿主机的统计信息列表
        :type HostStatisticSet: list of HostStatistic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HostStatisticSet = None
        self._RequestId = None

    @property
    def HostStatisticSet(self):
        """该集群内宿主机的统计信息列表
        :rtype: list of HostStatistic
        """
        return self._HostStatisticSet

    @HostStatisticSet.setter
    def HostStatisticSet(self, HostStatisticSet):
        self._HostStatisticSet = HostStatisticSet

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
        if params.get("HostStatisticSet") is not None:
            self._HostStatisticSet = []
            for item in params.get("HostStatisticSet"):
                obj = HostStatistic()
                obj._deserialize(item)
                self._HostStatisticSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterHostsRequest(AbstractModel):
    """DescribeDedicatedClusterHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 集群id
        :type DedicatedClusterId: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20
        :type Limit: int
        """
        self._DedicatedClusterId = None
        self._Offset = None
        self._Limit = None

    @property
    def DedicatedClusterId(self):
        """集群id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

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
        """返回数量，默认为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterHostsResponse(AbstractModel):
    """DescribeDedicatedClusterHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HostInfoSet: 宿主机信息
        :type HostInfoSet: list of HostInfo
        :param _TotalCount: 宿主机总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HostInfoSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def HostInfoSet(self):
        """宿主机信息
        :rtype: list of HostInfo
        """
        return self._HostInfoSet

    @HostInfoSet.setter
    def HostInfoSet(self, HostInfoSet):
        self._HostInfoSet = HostInfoSet

    @property
    def TotalCount(self):
        """宿主机总数
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
        if params.get("HostInfoSet") is not None:
            self._HostInfoSet = []
            for item in params.get("HostInfoSet"):
                obj = HostInfo()
                obj._deserialize(item)
                self._HostInfoSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterInstanceTypesRequest(AbstractModel):
    """DescribeDedicatedClusterInstanceTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 查询的专用集群id
        :type DedicatedClusterId: str
        """
        self._DedicatedClusterId = None

    @property
    def DedicatedClusterId(self):
        """查询的专用集群id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterInstanceTypesResponse(AbstractModel):
    """DescribeDedicatedClusterInstanceTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterInstanceTypeSet: 支持的实例规格列表
        :type DedicatedClusterInstanceTypeSet: list of DedicatedClusterInstanceType
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DedicatedClusterInstanceTypeSet = None
        self._RequestId = None

    @property
    def DedicatedClusterInstanceTypeSet(self):
        """支持的实例规格列表
        :rtype: list of DedicatedClusterInstanceType
        """
        return self._DedicatedClusterInstanceTypeSet

    @DedicatedClusterInstanceTypeSet.setter
    def DedicatedClusterInstanceTypeSet(self, DedicatedClusterInstanceTypeSet):
        self._DedicatedClusterInstanceTypeSet = DedicatedClusterInstanceTypeSet

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
        if params.get("DedicatedClusterInstanceTypeSet") is not None:
            self._DedicatedClusterInstanceTypeSet = []
            for item in params.get("DedicatedClusterInstanceTypeSet"):
                obj = DedicatedClusterInstanceType()
                obj._deserialize(item)
                self._DedicatedClusterInstanceTypeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterOrdersRequest(AbstractModel):
    """DescribeDedicatedClusterOrders请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterIds: 按照专用集群id过滤
        :type DedicatedClusterIds: list of str
        :param _DedicatedClusterOrderIds: 按照专用集群订单id过滤
        :type DedicatedClusterOrderIds: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Status: 订单状态为过滤条件：PENDING INCONSTRUCTION DELIVERING DELIVERED EXPIRED CANCELLED  OFFLINE
        :type Status: str
        :param _ActionType: 订单类型为过滤条件：CREATE  EXTEND
        :type ActionType: str
        :param _OrderTypes: 订单类型列表
        :type OrderTypes: list of str
        """
        self._DedicatedClusterIds = None
        self._DedicatedClusterOrderIds = None
        self._Offset = None
        self._Limit = None
        self._Status = None
        self._ActionType = None
        self._OrderTypes = None

    @property
    def DedicatedClusterIds(self):
        """按照专用集群id过滤
        :rtype: list of str
        """
        return self._DedicatedClusterIds

    @DedicatedClusterIds.setter
    def DedicatedClusterIds(self, DedicatedClusterIds):
        self._DedicatedClusterIds = DedicatedClusterIds

    @property
    def DedicatedClusterOrderIds(self):
        """按照专用集群订单id过滤
        :rtype: str
        """
        return self._DedicatedClusterOrderIds

    @DedicatedClusterOrderIds.setter
    def DedicatedClusterOrderIds(self, DedicatedClusterOrderIds):
        self._DedicatedClusterOrderIds = DedicatedClusterOrderIds

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """订单状态为过滤条件：PENDING INCONSTRUCTION DELIVERING DELIVERED EXPIRED CANCELLED  OFFLINE
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ActionType(self):
        """订单类型为过滤条件：CREATE  EXTEND
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def OrderTypes(self):
        """订单类型列表
        :rtype: list of str
        """
        return self._OrderTypes

    @OrderTypes.setter
    def OrderTypes(self, OrderTypes):
        self._OrderTypes = OrderTypes


    def _deserialize(self, params):
        self._DedicatedClusterIds = params.get("DedicatedClusterIds")
        self._DedicatedClusterOrderIds = params.get("DedicatedClusterOrderIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._ActionType = params.get("ActionType")
        self._OrderTypes = params.get("OrderTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterOrdersResponse(AbstractModel):
    """DescribeDedicatedClusterOrders返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterOrderSet: 专用集群订单列表
        :type DedicatedClusterOrderSet: list of DedicatedClusterOrder
        :param _TotalCount: 符合条件的专用集群订单总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DedicatedClusterOrderSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DedicatedClusterOrderSet(self):
        """专用集群订单列表
        :rtype: list of DedicatedClusterOrder
        """
        return self._DedicatedClusterOrderSet

    @DedicatedClusterOrderSet.setter
    def DedicatedClusterOrderSet(self, DedicatedClusterOrderSet):
        self._DedicatedClusterOrderSet = DedicatedClusterOrderSet

    @property
    def TotalCount(self):
        """符合条件的专用集群订单总数
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
        if params.get("DedicatedClusterOrderSet") is not None:
            self._DedicatedClusterOrderSet = []
            for item in params.get("DedicatedClusterOrderSet"):
                obj = DedicatedClusterOrder()
                obj._deserialize(item)
                self._DedicatedClusterOrderSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterOverviewRequest(AbstractModel):
    """DescribeDedicatedClusterOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 集群id
        :type DedicatedClusterId: str
        """
        self._DedicatedClusterId = None

    @property
    def DedicatedClusterId(self):
        """集群id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterOverviewResponse(AbstractModel):
    """DescribeDedicatedClusterOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CvmCount: 云服务器数量
        :type CvmCount: int
        :param _HostCount: 宿主机数量
        :type HostCount: int
        :param _VpnConnectionState: vpn通道状态
        :type VpnConnectionState: str
        :param _VpngwBandwidthData: vpn网关监控数据
        :type VpngwBandwidthData: :class:`tencentcloud.cdc.v20201214.models.VpngwBandwidthData`
        :param _LocalNetInfo: 本地网关信息
        :type LocalNetInfo: :class:`tencentcloud.cdc.v20201214.models.LocalNetInfo`
        :param _VpnConnectionBandwidthData: vpn网关通道监控数据
        :type VpnConnectionBandwidthData: list of VpngwBandwidthData
        :param _HostDetailInfo: 宿主机资源概览信息
        :type HostDetailInfo: list of HostDetailInfo
        :param _HostStandbyCount: 热备宿主机数量
        :type HostStandbyCount: int
        :param _HostNormalCount: 普通宿主机数量
        :type HostNormalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CvmCount = None
        self._HostCount = None
        self._VpnConnectionState = None
        self._VpngwBandwidthData = None
        self._LocalNetInfo = None
        self._VpnConnectionBandwidthData = None
        self._HostDetailInfo = None
        self._HostStandbyCount = None
        self._HostNormalCount = None
        self._RequestId = None

    @property
    def CvmCount(self):
        """云服务器数量
        :rtype: int
        """
        return self._CvmCount

    @CvmCount.setter
    def CvmCount(self, CvmCount):
        self._CvmCount = CvmCount

    @property
    def HostCount(self):
        """宿主机数量
        :rtype: int
        """
        return self._HostCount

    @HostCount.setter
    def HostCount(self, HostCount):
        self._HostCount = HostCount

    @property
    def VpnConnectionState(self):
        """vpn通道状态
        :rtype: str
        """
        return self._VpnConnectionState

    @VpnConnectionState.setter
    def VpnConnectionState(self, VpnConnectionState):
        self._VpnConnectionState = VpnConnectionState

    @property
    def VpngwBandwidthData(self):
        """vpn网关监控数据
        :rtype: :class:`tencentcloud.cdc.v20201214.models.VpngwBandwidthData`
        """
        return self._VpngwBandwidthData

    @VpngwBandwidthData.setter
    def VpngwBandwidthData(self, VpngwBandwidthData):
        self._VpngwBandwidthData = VpngwBandwidthData

    @property
    def LocalNetInfo(self):
        """本地网关信息
        :rtype: :class:`tencentcloud.cdc.v20201214.models.LocalNetInfo`
        """
        return self._LocalNetInfo

    @LocalNetInfo.setter
    def LocalNetInfo(self, LocalNetInfo):
        self._LocalNetInfo = LocalNetInfo

    @property
    def VpnConnectionBandwidthData(self):
        """vpn网关通道监控数据
        :rtype: list of VpngwBandwidthData
        """
        return self._VpnConnectionBandwidthData

    @VpnConnectionBandwidthData.setter
    def VpnConnectionBandwidthData(self, VpnConnectionBandwidthData):
        self._VpnConnectionBandwidthData = VpnConnectionBandwidthData

    @property
    def HostDetailInfo(self):
        """宿主机资源概览信息
        :rtype: list of HostDetailInfo
        """
        return self._HostDetailInfo

    @HostDetailInfo.setter
    def HostDetailInfo(self, HostDetailInfo):
        self._HostDetailInfo = HostDetailInfo

    @property
    def HostStandbyCount(self):
        """热备宿主机数量
        :rtype: int
        """
        return self._HostStandbyCount

    @HostStandbyCount.setter
    def HostStandbyCount(self, HostStandbyCount):
        self._HostStandbyCount = HostStandbyCount

    @property
    def HostNormalCount(self):
        """普通宿主机数量
        :rtype: int
        """
        return self._HostNormalCount

    @HostNormalCount.setter
    def HostNormalCount(self, HostNormalCount):
        self._HostNormalCount = HostNormalCount

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
        self._CvmCount = params.get("CvmCount")
        self._HostCount = params.get("HostCount")
        self._VpnConnectionState = params.get("VpnConnectionState")
        if params.get("VpngwBandwidthData") is not None:
            self._VpngwBandwidthData = VpngwBandwidthData()
            self._VpngwBandwidthData._deserialize(params.get("VpngwBandwidthData"))
        if params.get("LocalNetInfo") is not None:
            self._LocalNetInfo = LocalNetInfo()
            self._LocalNetInfo._deserialize(params.get("LocalNetInfo"))
        if params.get("VpnConnectionBandwidthData") is not None:
            self._VpnConnectionBandwidthData = []
            for item in params.get("VpnConnectionBandwidthData"):
                obj = VpngwBandwidthData()
                obj._deserialize(item)
                self._VpnConnectionBandwidthData.append(obj)
        if params.get("HostDetailInfo") is not None:
            self._HostDetailInfo = []
            for item in params.get("HostDetailInfo"):
                obj = HostDetailInfo()
                obj._deserialize(item)
                self._HostDetailInfo.append(obj)
        self._HostStandbyCount = params.get("HostStandbyCount")
        self._HostNormalCount = params.get("HostNormalCount")
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterTypesRequest(AbstractModel):
    """DescribeDedicatedClusterTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 模糊匹配专用集群配置名称
        :type Name: str
        :param _DedicatedClusterTypeIds: 待查询的专用集群配置id列表
        :type DedicatedClusterTypeIds: list of str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _IsCompute: 是否只查询计算规格类型
        :type IsCompute: bool
        """
        self._Name = None
        self._DedicatedClusterTypeIds = None
        self._Offset = None
        self._Limit = None
        self._IsCompute = None

    @property
    def Name(self):
        """模糊匹配专用集群配置名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DedicatedClusterTypeIds(self):
        """待查询的专用集群配置id列表
        :rtype: list of str
        """
        return self._DedicatedClusterTypeIds

    @DedicatedClusterTypeIds.setter
    def DedicatedClusterTypeIds(self, DedicatedClusterTypeIds):
        self._DedicatedClusterTypeIds = DedicatedClusterTypeIds

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def IsCompute(self):
        """是否只查询计算规格类型
        :rtype: bool
        """
        return self._IsCompute

    @IsCompute.setter
    def IsCompute(self, IsCompute):
        self._IsCompute = IsCompute


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DedicatedClusterTypeIds = params.get("DedicatedClusterTypeIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IsCompute = params.get("IsCompute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterTypesResponse(AbstractModel):
    """DescribeDedicatedClusterTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterTypeSet: 专用集群配置列表
        :type DedicatedClusterTypeSet: list of DedicatedClusterType
        :param _TotalCount: 符合条件的个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DedicatedClusterTypeSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DedicatedClusterTypeSet(self):
        """专用集群配置列表
        :rtype: list of DedicatedClusterType
        """
        return self._DedicatedClusterTypeSet

    @DedicatedClusterTypeSet.setter
    def DedicatedClusterTypeSet(self, DedicatedClusterTypeSet):
        self._DedicatedClusterTypeSet = DedicatedClusterTypeSet

    @property
    def TotalCount(self):
        """符合条件的个数
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
        if params.get("DedicatedClusterTypeSet") is not None:
            self._DedicatedClusterTypeSet = []
            for item in params.get("DedicatedClusterTypeSet"):
                obj = DedicatedClusterType()
                obj._deserialize(item)
                self._DedicatedClusterTypeSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClustersRequest(AbstractModel):
    """DescribeDedicatedClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterIds: 按照一个或者多个实例ID查询。实例ID形如：`cluster-xxxxxxxx`
        :type DedicatedClusterIds: list of str
        :param _Zones: 按照可用区名称过滤
        :type Zones: list of str
        :param _SiteIds: 按照站点id过滤
        :type SiteIds: list of str
        :param _LifecycleStatuses: 按照专用集群生命周期过滤
        :type LifecycleStatuses: list of str
        :param _Name: 模糊匹配专用集群名称
        :type Name: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._DedicatedClusterIds = None
        self._Zones = None
        self._SiteIds = None
        self._LifecycleStatuses = None
        self._Name = None
        self._Offset = None
        self._Limit = None

    @property
    def DedicatedClusterIds(self):
        """按照一个或者多个实例ID查询。实例ID形如：`cluster-xxxxxxxx`
        :rtype: list of str
        """
        return self._DedicatedClusterIds

    @DedicatedClusterIds.setter
    def DedicatedClusterIds(self, DedicatedClusterIds):
        self._DedicatedClusterIds = DedicatedClusterIds

    @property
    def Zones(self):
        """按照可用区名称过滤
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SiteIds(self):
        """按照站点id过滤
        :rtype: list of str
        """
        return self._SiteIds

    @SiteIds.setter
    def SiteIds(self, SiteIds):
        self._SiteIds = SiteIds

    @property
    def LifecycleStatuses(self):
        """按照专用集群生命周期过滤
        :rtype: list of str
        """
        return self._LifecycleStatuses

    @LifecycleStatuses.setter
    def LifecycleStatuses(self, LifecycleStatuses):
        self._LifecycleStatuses = LifecycleStatuses

    @property
    def Name(self):
        """模糊匹配专用集群名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DedicatedClusterIds = params.get("DedicatedClusterIds")
        self._Zones = params.get("Zones")
        self._SiteIds = params.get("SiteIds")
        self._LifecycleStatuses = params.get("LifecycleStatuses")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClustersResponse(AbstractModel):
    """DescribeDedicatedClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterSet: 符合查询条件的专用集群列表
        :type DedicatedClusterSet: list of DedicatedCluster
        :param _TotalCount: 符合条件的专用集群数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DedicatedClusterSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DedicatedClusterSet(self):
        """符合查询条件的专用集群列表
        :rtype: list of DedicatedCluster
        """
        return self._DedicatedClusterSet

    @DedicatedClusterSet.setter
    def DedicatedClusterSet(self, DedicatedClusterSet):
        self._DedicatedClusterSet = DedicatedClusterSet

    @property
    def TotalCount(self):
        """符合条件的专用集群数量。
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
        if params.get("DedicatedClusterSet") is not None:
            self._DedicatedClusterSet = []
            for item in params.get("DedicatedClusterSet"):
                obj = DedicatedCluster()
                obj._deserialize(item)
                self._DedicatedClusterSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDedicatedSupportedZonesRequest(AbstractModel):
    """DescribeDedicatedSupportedZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Regions: 传入region列表
        :type Regions: list of int
        """
        self._Regions = None

    @property
    def Regions(self):
        """传入region列表
        :rtype: list of int
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedSupportedZonesResponse(AbstractModel):
    """DescribeDedicatedSupportedZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneSet: 支持的可用区列表
        :type ZoneSet: list of RegionZoneInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneSet = None
        self._RequestId = None

    @property
    def ZoneSet(self):
        """支持的可用区列表
        :rtype: list of RegionZoneInfo
        """
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

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
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = RegionZoneInfo()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSitesDetailRequest(AbstractModel):
    """DescribeSitesDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteIds: 按照站点id过滤
        :type SiteIds: list of str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Name: 按照站定名称模糊匹配
        :type Name: str
        """
        self._SiteIds = None
        self._Offset = None
        self._Limit = None
        self._Name = None

    @property
    def SiteIds(self):
        """按照站点id过滤
        :rtype: list of str
        """
        return self._SiteIds

    @SiteIds.setter
    def SiteIds(self, SiteIds):
        self._SiteIds = SiteIds

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Name(self):
        """按照站定名称模糊匹配
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._SiteIds = params.get("SiteIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSitesDetailResponse(AbstractModel):
    """DescribeSitesDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteDetailSet: 站点详情
        :type SiteDetailSet: list of SiteDetail
        :param _TotalCount: 符合条件的站点总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SiteDetailSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SiteDetailSet(self):
        """站点详情
        :rtype: list of SiteDetail
        """
        return self._SiteDetailSet

    @SiteDetailSet.setter
    def SiteDetailSet(self, SiteDetailSet):
        self._SiteDetailSet = SiteDetailSet

    @property
    def TotalCount(self):
        """符合条件的站点总数
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
        if params.get("SiteDetailSet") is not None:
            self._SiteDetailSet = []
            for item in params.get("SiteDetailSet"):
                obj = SiteDetail()
                obj._deserialize(item)
                self._SiteDetailSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSitesRequest(AbstractModel):
    """DescribeSites请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteIds: 按照站点id过滤
        :type SiteIds: list of str
        :param _Name: 模糊匹配站点名称
        :type Name: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._SiteIds = None
        self._Name = None
        self._Offset = None
        self._Limit = None

    @property
    def SiteIds(self):
        """按照站点id过滤
        :rtype: list of str
        """
        return self._SiteIds

    @SiteIds.setter
    def SiteIds(self, SiteIds):
        self._SiteIds = SiteIds

    @property
    def Name(self):
        """模糊匹配站点名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SiteIds = params.get("SiteIds")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSitesResponse(AbstractModel):
    """DescribeSites返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteSet: 符合查询条件的站点列表
        :type SiteSet: list of Site
        :param _TotalCount: 符合条件的站点数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SiteSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SiteSet(self):
        """符合查询条件的站点列表
        :rtype: list of Site
        """
        return self._SiteSet

    @SiteSet.setter
    def SiteSet(self, SiteSet):
        self._SiteSet = SiteSet

    @property
    def TotalCount(self):
        """符合条件的站点数量。
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
        if params.get("SiteSet") is not None:
            self._SiteSet = []
            for item in params.get("SiteSet"):
                obj = Site()
                obj._deserialize(item)
                self._SiteSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DetailData(AbstractModel):
    """带有时间戳的详细数据。

    """

    def __init__(self):
        r"""
        :param _Timestamps: 时间戳
        :type Timestamps: list of float
        :param _Values: 对应的具体值
        :type Values: list of float
        """
        self._Timestamps = None
        self._Values = None

    @property
    def Timestamps(self):
        """时间戳
        :rtype: list of float
        """
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def Values(self):
        """对应的具体值
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Timestamps = params.get("Timestamps")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostDetailInfo(AbstractModel):
    """宿主机资源的概览详细信息。

    """

    def __init__(self):
        r"""
        :param _HostTypeFamily: 类型族
        :type HostTypeFamily: str
        :param _CpuTotal: 总CPU
        :type CpuTotal: float
        :param _CpuAvailable: 可用CPU
        :type CpuAvailable: float
        :param _MemTotal: 总内存
        :type MemTotal: float
        :param _MemAvailable: 可用内存
        :type MemAvailable: float
        """
        self._HostTypeFamily = None
        self._CpuTotal = None
        self._CpuAvailable = None
        self._MemTotal = None
        self._MemAvailable = None

    @property
    def HostTypeFamily(self):
        """类型族
        :rtype: str
        """
        return self._HostTypeFamily

    @HostTypeFamily.setter
    def HostTypeFamily(self, HostTypeFamily):
        self._HostTypeFamily = HostTypeFamily

    @property
    def CpuTotal(self):
        """总CPU
        :rtype: float
        """
        return self._CpuTotal

    @CpuTotal.setter
    def CpuTotal(self, CpuTotal):
        self._CpuTotal = CpuTotal

    @property
    def CpuAvailable(self):
        """可用CPU
        :rtype: float
        """
        return self._CpuAvailable

    @CpuAvailable.setter
    def CpuAvailable(self, CpuAvailable):
        self._CpuAvailable = CpuAvailable

    @property
    def MemTotal(self):
        """总内存
        :rtype: float
        """
        return self._MemTotal

    @MemTotal.setter
    def MemTotal(self, MemTotal):
        self._MemTotal = MemTotal

    @property
    def MemAvailable(self):
        """可用内存
        :rtype: float
        """
        return self._MemAvailable

    @MemAvailable.setter
    def MemAvailable(self, MemAvailable):
        self._MemAvailable = MemAvailable


    def _deserialize(self, params):
        self._HostTypeFamily = params.get("HostTypeFamily")
        self._CpuTotal = params.get("CpuTotal")
        self._CpuAvailable = params.get("CpuAvailable")
        self._MemTotal = params.get("MemTotal")
        self._MemAvailable = params.get("MemAvailable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostInfo(AbstractModel):
    """CDC宿主机的详细信息

    """

    def __init__(self):
        r"""
        :param _HostIp: 宿主机IP（废弃）
        :type HostIp: str
        :param _ServiceType: 云服务类型
        :type ServiceType: str
        :param _HostStatus: 宿主机运行状态
        :type HostStatus: str
        :param _HostType: 宿主机类型
        :type HostType: str
        :param _CpuAvailable: cpu可用数
        :type CpuAvailable: int
        :param _CpuTotal: cpu总数
        :type CpuTotal: int
        :param _MemAvailable: 内存可用数
        :type MemAvailable: int
        :param _MemTotal: 内存总数
        :type MemTotal: int
        :param _RunTime: 运行时间
        :type RunTime: str
        :param _ExpireTime: 到期时间
        :type ExpireTime: str
        :param _HostId: 宿主机id
        :type HostId: str
        """
        self._HostIp = None
        self._ServiceType = None
        self._HostStatus = None
        self._HostType = None
        self._CpuAvailable = None
        self._CpuTotal = None
        self._MemAvailable = None
        self._MemTotal = None
        self._RunTime = None
        self._ExpireTime = None
        self._HostId = None

    @property
    def HostIp(self):
        """宿主机IP（废弃）
        :rtype: str
        """
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp

    @property
    def ServiceType(self):
        """云服务类型
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def HostStatus(self):
        """宿主机运行状态
        :rtype: str
        """
        return self._HostStatus

    @HostStatus.setter
    def HostStatus(self, HostStatus):
        self._HostStatus = HostStatus

    @property
    def HostType(self):
        """宿主机类型
        :rtype: str
        """
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def CpuAvailable(self):
        """cpu可用数
        :rtype: int
        """
        return self._CpuAvailable

    @CpuAvailable.setter
    def CpuAvailable(self, CpuAvailable):
        self._CpuAvailable = CpuAvailable

    @property
    def CpuTotal(self):
        """cpu总数
        :rtype: int
        """
        return self._CpuTotal

    @CpuTotal.setter
    def CpuTotal(self, CpuTotal):
        self._CpuTotal = CpuTotal

    @property
    def MemAvailable(self):
        """内存可用数
        :rtype: int
        """
        return self._MemAvailable

    @MemAvailable.setter
    def MemAvailable(self, MemAvailable):
        self._MemAvailable = MemAvailable

    @property
    def MemTotal(self):
        """内存总数
        :rtype: int
        """
        return self._MemTotal

    @MemTotal.setter
    def MemTotal(self, MemTotal):
        self._MemTotal = MemTotal

    @property
    def RunTime(self):
        """运行时间
        :rtype: str
        """
        return self._RunTime

    @RunTime.setter
    def RunTime(self, RunTime):
        self._RunTime = RunTime

    @property
    def ExpireTime(self):
        """到期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def HostId(self):
        """宿主机id
        :rtype: str
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId


    def _deserialize(self, params):
        self._HostIp = params.get("HostIp")
        self._ServiceType = params.get("ServiceType")
        self._HostStatus = params.get("HostStatus")
        self._HostType = params.get("HostType")
        self._CpuAvailable = params.get("CpuAvailable")
        self._CpuTotal = params.get("CpuTotal")
        self._MemAvailable = params.get("MemAvailable")
        self._MemTotal = params.get("MemTotal")
        self._RunTime = params.get("RunTime")
        self._ExpireTime = params.get("ExpireTime")
        self._HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostStatistic(AbstractModel):
    """CDC集群内宿主机的统计信息

    """

    def __init__(self):
        r"""
        :param _HostType: 宿主机规格
        :type HostType: str
        :param _HostFamily: 宿主机机型系列
        :type HostFamily: str
        :param _Cpu: 宿主机的CPU核数，单位：核
        :type Cpu: int
        :param _Memory: 宿主机内存大小，单位：GB
        :type Memory: int
        :param _Count: 该规格宿主机的数量
        :type Count: int
        :param _CpuAverage: 平均cpu负载百分比
        :type CpuAverage: float
        :param _MemAverage: 平均内存使用率百分比
        :type MemAverage: float
        :param _NetAverage: 平均网络流量
        :type NetAverage: float
        :param _CpuDetailData: cpu详细监控数据
        :type CpuDetailData: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        :param _MemDetailData: 内存详细数据
        :type MemDetailData: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        :param _NetRateDetailData: 网络速率详细数据
        :type NetRateDetailData: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        :param _NetPacketDetailData: 网速包详细数据
        :type NetPacketDetailData: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        self._HostType = None
        self._HostFamily = None
        self._Cpu = None
        self._Memory = None
        self._Count = None
        self._CpuAverage = None
        self._MemAverage = None
        self._NetAverage = None
        self._CpuDetailData = None
        self._MemDetailData = None
        self._NetRateDetailData = None
        self._NetPacketDetailData = None

    @property
    def HostType(self):
        """宿主机规格
        :rtype: str
        """
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def HostFamily(self):
        """宿主机机型系列
        :rtype: str
        """
        return self._HostFamily

    @HostFamily.setter
    def HostFamily(self, HostFamily):
        self._HostFamily = HostFamily

    @property
    def Cpu(self):
        """宿主机的CPU核数，单位：核
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """宿主机内存大小，单位：GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Count(self):
        """该规格宿主机的数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def CpuAverage(self):
        """平均cpu负载百分比
        :rtype: float
        """
        return self._CpuAverage

    @CpuAverage.setter
    def CpuAverage(self, CpuAverage):
        self._CpuAverage = CpuAverage

    @property
    def MemAverage(self):
        """平均内存使用率百分比
        :rtype: float
        """
        return self._MemAverage

    @MemAverage.setter
    def MemAverage(self, MemAverage):
        self._MemAverage = MemAverage

    @property
    def NetAverage(self):
        """平均网络流量
        :rtype: float
        """
        return self._NetAverage

    @NetAverage.setter
    def NetAverage(self, NetAverage):
        self._NetAverage = NetAverage

    @property
    def CpuDetailData(self):
        """cpu详细监控数据
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._CpuDetailData

    @CpuDetailData.setter
    def CpuDetailData(self, CpuDetailData):
        self._CpuDetailData = CpuDetailData

    @property
    def MemDetailData(self):
        """内存详细数据
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._MemDetailData

    @MemDetailData.setter
    def MemDetailData(self, MemDetailData):
        self._MemDetailData = MemDetailData

    @property
    def NetRateDetailData(self):
        """网络速率详细数据
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._NetRateDetailData

    @NetRateDetailData.setter
    def NetRateDetailData(self, NetRateDetailData):
        self._NetRateDetailData = NetRateDetailData

    @property
    def NetPacketDetailData(self):
        """网速包详细数据
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._NetPacketDetailData

    @NetPacketDetailData.setter
    def NetPacketDetailData(self, NetPacketDetailData):
        self._NetPacketDetailData = NetPacketDetailData


    def _deserialize(self, params):
        self._HostType = params.get("HostType")
        self._HostFamily = params.get("HostFamily")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Count = params.get("Count")
        self._CpuAverage = params.get("CpuAverage")
        self._MemAverage = params.get("MemAverage")
        self._NetAverage = params.get("NetAverage")
        if params.get("CpuDetailData") is not None:
            self._CpuDetailData = DetailData()
            self._CpuDetailData._deserialize(params.get("CpuDetailData"))
        if params.get("MemDetailData") is not None:
            self._MemDetailData = DetailData()
            self._MemDetailData._deserialize(params.get("MemDetailData"))
        if params.get("NetRateDetailData") is not None:
            self._NetRateDetailData = DetailData()
            self._NetRateDetailData._deserialize(params.get("NetRateDetailData"))
        if params.get("NetPacketDetailData") is not None:
            self._NetPacketDetailData = DetailData()
            self._NetPacketDetailData._deserialize(params.get("NetPacketDetailData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InBandwidth(AbstractModel):
    """入带宽数据

    """

    def __init__(self):
        r"""
        :param _Timestamps: 时间戳
        :type Timestamps: list of float
        :param _Values: 时间对应的值
        :type Values: list of float
        """
        self._Timestamps = None
        self._Values = None

    @property
    def Timestamps(self):
        """时间戳
        :rtype: list of float
        """
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def Values(self):
        """时间对应的值
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Timestamps = params.get("Timestamps")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalNetInfo(AbstractModel):
    """本地网络信息

    """

    def __init__(self):
        r"""
        :param _Protocol: 协议
        :type Protocol: str
        :param _VpcId: 网络id
        :type VpcId: str
        :param _BGPRoute: 路由信息
        :type BGPRoute: str
        :param _LocalIp: 本地IP
        :type LocalIp: str
        """
        self._Protocol = None
        self._VpcId = None
        self._BGPRoute = None
        self._LocalIp = None

    @property
    def Protocol(self):
        """协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def VpcId(self):
        """网络id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def BGPRoute(self):
        """路由信息
        :rtype: str
        """
        return self._BGPRoute

    @BGPRoute.setter
    def BGPRoute(self, BGPRoute):
        self._BGPRoute = BGPRoute

    @property
    def LocalIp(self):
        """本地IP
        :rtype: str
        """
        return self._LocalIp

    @LocalIp.setter
    def LocalIp(self, LocalIp):
        self._LocalIp = LocalIp


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._VpcId = params.get("VpcId")
        self._BGPRoute = params.get("BGPRoute")
        self._LocalIp = params.get("LocalIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDedicatedClusterInfoRequest(AbstractModel):
    """ModifyDedicatedClusterInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: 本地专用集群ID
        :type DedicatedClusterId: str
        :param _Name: 集群的新名称
        :type Name: str
        :param _Zone: 集群的新可用区
        :type Zone: str
        :param _Description: 集群的新描述信息
        :type Description: str
        :param _SiteId: 集群所在站点
        :type SiteId: str
        """
        self._DedicatedClusterId = None
        self._Name = None
        self._Zone = None
        self._Description = None
        self._SiteId = None

    @property
    def DedicatedClusterId(self):
        """本地专用集群ID
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def Name(self):
        """集群的新名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Zone(self):
        """集群的新可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Description(self):
        """集群的新描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SiteId(self):
        """集群所在站点
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._Name = params.get("Name")
        self._Zone = params.get("Zone")
        self._Description = params.get("Description")
        self._SiteId = params.get("SiteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDedicatedClusterInfoResponse(AbstractModel):
    """ModifyDedicatedClusterInfo返回参数结构体

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


class ModifyOrderStatusRequest(AbstractModel):
    """ModifyOrderStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 要更新成的状态
        :type Status: str
        :param _DedicatedClusterOrderId: 大订单ID，可以在本地专用集群的基础信息页获取大订单ID
        :type DedicatedClusterOrderId: str
        :param _SubOrderIds: 小订单ID，进入大订单的详情页，可以看到小订单ID
        :type SubOrderIds: list of str
        """
        self._Status = None
        self._DedicatedClusterOrderId = None
        self._SubOrderIds = None

    @property
    def Status(self):
        """要更新成的状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DedicatedClusterOrderId(self):
        """大订单ID，可以在本地专用集群的基础信息页获取大订单ID
        :rtype: str
        """
        return self._DedicatedClusterOrderId

    @DedicatedClusterOrderId.setter
    def DedicatedClusterOrderId(self, DedicatedClusterOrderId):
        self._DedicatedClusterOrderId = DedicatedClusterOrderId

    @property
    def SubOrderIds(self):
        """小订单ID，进入大订单的详情页，可以看到小订单ID
        :rtype: list of str
        """
        return self._SubOrderIds

    @SubOrderIds.setter
    def SubOrderIds(self, SubOrderIds):
        self._SubOrderIds = SubOrderIds


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        self._SubOrderIds = params.get("SubOrderIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOrderStatusResponse(AbstractModel):
    """ModifyOrderStatus返回参数结构体

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


class ModifySiteDeviceInfoRequest(AbstractModel):
    """ModifySiteDeviceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteId: 机房ID
        :type SiteId: str
        :param _FiberType: 您将使用光纤类型将CDC设备连接到网络。有单模和多模两种选项。
        :type FiberType: str
        :param _OpticalStandard: 您将CDC连接到网络时采用的光学标准。此字段取决于上行链路速度、光纤类型和到上游设备的距离。
        :type OpticalStandard: str
        :param _PowerConnectors: 电源连接器类型
        :type PowerConnectors: str
        :param _PowerFeedDrop: 从机架上方还是下方供电。取值范围：["UP","DOWN"]
        :type PowerFeedDrop: str
        :param _MaxWeight: 最大承重(KG)
        :type MaxWeight: int
        :param _PowerDrawKva: 功耗(KW)
        :type PowerDrawKva: int
        :param _UplinkSpeedGbps: 网络到腾讯云Region区域的上行链路速度(Gbps)
        :type UplinkSpeedGbps: int
        :param _UplinkCount: 将CDC连接到网络时，每台CDC网络设备(每个机架 2 台设备)使用的上行链路数量。
        :type UplinkCount: int
        :param _ConditionRequirement: 是否满足下面环境条件：
1、场地没有材料要求或验收标准会影响 CDC 设备配送和安装。
2、确定的机架位置包含:
温度范围为 41 到 104°F (5 到 40°C)。
湿度范围为 10°F (-12°C)和 8% RH (相对湿度)到 70°F(21°C)和 80% RH。
机架位置的气流方向为从前向后，且应具有足够的 CFM (每分钟立方英尺)，散热功率须达到CDC运行功率值的 145.8 倍以上。
        :type ConditionRequirement: bool
        :param _DimensionRequirement: 是否满足下面的尺寸条件：
您的装货站台可以容纳一个机架箱(高 x 宽 x 深 = 94" x 54" x 48")。
您可以提供从机架(高 x 宽 x 深 = 80" x 24" x 48")交货地点到机架最终安置位置的明确通道。测量深度时，应包括站台、走廊通道、门、转弯、坡道、货梯，并将其他通道限制考虑在内。
在最终的 CDC安置位置，前部间隙可以为 48" 或更大，后部间隙可以为 24" 或更大。
        :type DimensionRequirement: bool
        :param _RedundantNetworking: 是否提供冗余的上游设备(交换机或路由器)，以便实现网络出口的高可用。
        :type RedundantNetworking: bool
        :param _NeedHelp: 是否需要腾讯云团队协助完成机架支撑工作
        :type NeedHelp: bool
        :param _RedundantPower: 是否电源冗余
        :type RedundantPower: bool
        :param _BreakerRequirement: 上游断路器是否具备
        :type BreakerRequirement: bool
        """
        self._SiteId = None
        self._FiberType = None
        self._OpticalStandard = None
        self._PowerConnectors = None
        self._PowerFeedDrop = None
        self._MaxWeight = None
        self._PowerDrawKva = None
        self._UplinkSpeedGbps = None
        self._UplinkCount = None
        self._ConditionRequirement = None
        self._DimensionRequirement = None
        self._RedundantNetworking = None
        self._NeedHelp = None
        self._RedundantPower = None
        self._BreakerRequirement = None

    @property
    def SiteId(self):
        """机房ID
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def FiberType(self):
        """您将使用光纤类型将CDC设备连接到网络。有单模和多模两种选项。
        :rtype: str
        """
        return self._FiberType

    @FiberType.setter
    def FiberType(self, FiberType):
        self._FiberType = FiberType

    @property
    def OpticalStandard(self):
        """您将CDC连接到网络时采用的光学标准。此字段取决于上行链路速度、光纤类型和到上游设备的距离。
        :rtype: str
        """
        return self._OpticalStandard

    @OpticalStandard.setter
    def OpticalStandard(self, OpticalStandard):
        self._OpticalStandard = OpticalStandard

    @property
    def PowerConnectors(self):
        """电源连接器类型
        :rtype: str
        """
        return self._PowerConnectors

    @PowerConnectors.setter
    def PowerConnectors(self, PowerConnectors):
        self._PowerConnectors = PowerConnectors

    @property
    def PowerFeedDrop(self):
        """从机架上方还是下方供电。取值范围：["UP","DOWN"]
        :rtype: str
        """
        return self._PowerFeedDrop

    @PowerFeedDrop.setter
    def PowerFeedDrop(self, PowerFeedDrop):
        self._PowerFeedDrop = PowerFeedDrop

    @property
    def MaxWeight(self):
        """最大承重(KG)
        :rtype: int
        """
        return self._MaxWeight

    @MaxWeight.setter
    def MaxWeight(self, MaxWeight):
        self._MaxWeight = MaxWeight

    @property
    def PowerDrawKva(self):
        """功耗(KW)
        :rtype: int
        """
        return self._PowerDrawKva

    @PowerDrawKva.setter
    def PowerDrawKva(self, PowerDrawKva):
        self._PowerDrawKva = PowerDrawKva

    @property
    def UplinkSpeedGbps(self):
        """网络到腾讯云Region区域的上行链路速度(Gbps)
        :rtype: int
        """
        return self._UplinkSpeedGbps

    @UplinkSpeedGbps.setter
    def UplinkSpeedGbps(self, UplinkSpeedGbps):
        self._UplinkSpeedGbps = UplinkSpeedGbps

    @property
    def UplinkCount(self):
        """将CDC连接到网络时，每台CDC网络设备(每个机架 2 台设备)使用的上行链路数量。
        :rtype: int
        """
        return self._UplinkCount

    @UplinkCount.setter
    def UplinkCount(self, UplinkCount):
        self._UplinkCount = UplinkCount

    @property
    def ConditionRequirement(self):
        """是否满足下面环境条件：
1、场地没有材料要求或验收标准会影响 CDC 设备配送和安装。
2、确定的机架位置包含:
温度范围为 41 到 104°F (5 到 40°C)。
湿度范围为 10°F (-12°C)和 8% RH (相对湿度)到 70°F(21°C)和 80% RH。
机架位置的气流方向为从前向后，且应具有足够的 CFM (每分钟立方英尺)，散热功率须达到CDC运行功率值的 145.8 倍以上。
        :rtype: bool
        """
        return self._ConditionRequirement

    @ConditionRequirement.setter
    def ConditionRequirement(self, ConditionRequirement):
        self._ConditionRequirement = ConditionRequirement

    @property
    def DimensionRequirement(self):
        """是否满足下面的尺寸条件：
您的装货站台可以容纳一个机架箱(高 x 宽 x 深 = 94" x 54" x 48")。
您可以提供从机架(高 x 宽 x 深 = 80" x 24" x 48")交货地点到机架最终安置位置的明确通道。测量深度时，应包括站台、走廊通道、门、转弯、坡道、货梯，并将其他通道限制考虑在内。
在最终的 CDC安置位置，前部间隙可以为 48" 或更大，后部间隙可以为 24" 或更大。
        :rtype: bool
        """
        return self._DimensionRequirement

    @DimensionRequirement.setter
    def DimensionRequirement(self, DimensionRequirement):
        self._DimensionRequirement = DimensionRequirement

    @property
    def RedundantNetworking(self):
        """是否提供冗余的上游设备(交换机或路由器)，以便实现网络出口的高可用。
        :rtype: bool
        """
        return self._RedundantNetworking

    @RedundantNetworking.setter
    def RedundantNetworking(self, RedundantNetworking):
        self._RedundantNetworking = RedundantNetworking

    @property
    def NeedHelp(self):
        """是否需要腾讯云团队协助完成机架支撑工作
        :rtype: bool
        """
        return self._NeedHelp

    @NeedHelp.setter
    def NeedHelp(self, NeedHelp):
        self._NeedHelp = NeedHelp

    @property
    def RedundantPower(self):
        """是否电源冗余
        :rtype: bool
        """
        return self._RedundantPower

    @RedundantPower.setter
    def RedundantPower(self, RedundantPower):
        self._RedundantPower = RedundantPower

    @property
    def BreakerRequirement(self):
        """上游断路器是否具备
        :rtype: bool
        """
        return self._BreakerRequirement

    @BreakerRequirement.setter
    def BreakerRequirement(self, BreakerRequirement):
        self._BreakerRequirement = BreakerRequirement


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._FiberType = params.get("FiberType")
        self._OpticalStandard = params.get("OpticalStandard")
        self._PowerConnectors = params.get("PowerConnectors")
        self._PowerFeedDrop = params.get("PowerFeedDrop")
        self._MaxWeight = params.get("MaxWeight")
        self._PowerDrawKva = params.get("PowerDrawKva")
        self._UplinkSpeedGbps = params.get("UplinkSpeedGbps")
        self._UplinkCount = params.get("UplinkCount")
        self._ConditionRequirement = params.get("ConditionRequirement")
        self._DimensionRequirement = params.get("DimensionRequirement")
        self._RedundantNetworking = params.get("RedundantNetworking")
        self._NeedHelp = params.get("NeedHelp")
        self._RedundantPower = params.get("RedundantPower")
        self._BreakerRequirement = params.get("BreakerRequirement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySiteDeviceInfoResponse(AbstractModel):
    """ModifySiteDeviceInfo返回参数结构体

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


class ModifySiteInfoRequest(AbstractModel):
    """ModifySiteInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteId: 机房ID
        :type SiteId: str
        :param _Name: 站点名称
        :type Name: str
        :param _Description: 站点描述
        :type Description: str
        :param _Note: 注意事项
        :type Note: str
        :param _Country: 站点所在国家
        :type Country: str
        :param _Province: 站点所在省份
        :type Province: str
        :param _City: 站点所在城市
        :type City: str
        :param _PostalCode: 站点所在地区的邮编
        :type PostalCode: str
        :param _AddressLine: 站点所在地区的详细地址信息
        :type AddressLine: str
        """
        self._SiteId = None
        self._Name = None
        self._Description = None
        self._Note = None
        self._Country = None
        self._Province = None
        self._City = None
        self._PostalCode = None
        self._AddressLine = None

    @property
    def SiteId(self):
        """机房ID
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def Name(self):
        """站点名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """站点描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Note(self):
        """注意事项
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Country(self):
        """站点所在国家
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """站点所在省份
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """站点所在城市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def PostalCode(self):
        """站点所在地区的邮编
        :rtype: str
        """
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def AddressLine(self):
        """站点所在地区的详细地址信息
        :rtype: str
        """
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, AddressLine):
        self._AddressLine = AddressLine


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Note = params.get("Note")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._PostalCode = params.get("PostalCode")
        self._AddressLine = params.get("AddressLine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySiteInfoResponse(AbstractModel):
    """ModifySiteInfo返回参数结构体

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


class OutBandwidth(AbstractModel):
    """出带宽数据。

    """

    def __init__(self):
        r"""
        :param _Timestamps: 时间戳
        :type Timestamps: list of float
        :param _Values: 对应时间的值
        :type Values: list of float
        """
        self._Timestamps = None
        self._Values = None

    @property
    def Timestamps(self):
        """时间戳
        :rtype: list of float
        """
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def Values(self):
        """对应时间的值
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Timestamps = params.get("Timestamps")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionZoneInfo(AbstractModel):
    """RegionZoneInfo信息

    """

    def __init__(self):
        r"""
        :param _RegionId: Region id
        :type RegionId: int
        :param _Zones: ZoneInfo数组
        :type Zones: list of ZoneInfo
        """
        self._RegionId = None
        self._Zones = None

    @property
    def RegionId(self):
        """Region id
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Zones(self):
        """ZoneInfo数组
        :rtype: list of ZoneInfo
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._Zones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetInfo(AbstractModel):
    """云硬盘的仓库级别信息

    """

    def __init__(self):
        r"""
        :param _SetId: 云硬盘仓库id
        :type SetId: str
        :param _SetName: 云硬盘仓库名称
        :type SetName: str
        :param _SetType: 云硬盘仓库类型
        :type SetType: str
        :param _SetSize: 云硬盘仓库容量
        :type SetSize: float
        :param _SetStatus: 云硬盘仓库状态
        :type SetStatus: str
        :param _CreateTime: 云硬盘仓库创建时间
        :type CreateTime: str
        :param _ReadTraffic: 读流量
        :type ReadTraffic: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        :param _WriteTraffic: 写流量
        :type WriteTraffic: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        :param _ReadIO: 读IO
        :type ReadIO: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        :param _WriteIO: 写IO
        :type WriteIO: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        :param _Await: 平均等待时间
        :type Await: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        :param _Util: 利用率
        :type Util: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        self._SetId = None
        self._SetName = None
        self._SetType = None
        self._SetSize = None
        self._SetStatus = None
        self._CreateTime = None
        self._ReadTraffic = None
        self._WriteTraffic = None
        self._ReadIO = None
        self._WriteIO = None
        self._Await = None
        self._Util = None

    @property
    def SetId(self):
        """云硬盘仓库id
        :rtype: str
        """
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def SetName(self):
        """云硬盘仓库名称
        :rtype: str
        """
        return self._SetName

    @SetName.setter
    def SetName(self, SetName):
        self._SetName = SetName

    @property
    def SetType(self):
        """云硬盘仓库类型
        :rtype: str
        """
        return self._SetType

    @SetType.setter
    def SetType(self, SetType):
        self._SetType = SetType

    @property
    def SetSize(self):
        """云硬盘仓库容量
        :rtype: float
        """
        return self._SetSize

    @SetSize.setter
    def SetSize(self, SetSize):
        self._SetSize = SetSize

    @property
    def SetStatus(self):
        """云硬盘仓库状态
        :rtype: str
        """
        return self._SetStatus

    @SetStatus.setter
    def SetStatus(self, SetStatus):
        self._SetStatus = SetStatus

    @property
    def CreateTime(self):
        """云硬盘仓库创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ReadTraffic(self):
        """读流量
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._ReadTraffic

    @ReadTraffic.setter
    def ReadTraffic(self, ReadTraffic):
        self._ReadTraffic = ReadTraffic

    @property
    def WriteTraffic(self):
        """写流量
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._WriteTraffic

    @WriteTraffic.setter
    def WriteTraffic(self, WriteTraffic):
        self._WriteTraffic = WriteTraffic

    @property
    def ReadIO(self):
        """读IO
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._ReadIO

    @ReadIO.setter
    def ReadIO(self, ReadIO):
        self._ReadIO = ReadIO

    @property
    def WriteIO(self):
        """写IO
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._WriteIO

    @WriteIO.setter
    def WriteIO(self, WriteIO):
        self._WriteIO = WriteIO

    @property
    def Await(self):
        """平均等待时间
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._Await

    @Await.setter
    def Await(self, Await):
        self._Await = Await

    @property
    def Util(self):
        """利用率
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._Util

    @Util.setter
    def Util(self, Util):
        self._Util = Util


    def _deserialize(self, params):
        self._SetId = params.get("SetId")
        self._SetName = params.get("SetName")
        self._SetType = params.get("SetType")
        self._SetSize = params.get("SetSize")
        self._SetStatus = params.get("SetStatus")
        self._CreateTime = params.get("CreateTime")
        if params.get("ReadTraffic") is not None:
            self._ReadTraffic = DetailData()
            self._ReadTraffic._deserialize(params.get("ReadTraffic"))
        if params.get("WriteTraffic") is not None:
            self._WriteTraffic = DetailData()
            self._WriteTraffic._deserialize(params.get("WriteTraffic"))
        if params.get("ReadIO") is not None:
            self._ReadIO = DetailData()
            self._ReadIO._deserialize(params.get("ReadIO"))
        if params.get("WriteIO") is not None:
            self._WriteIO = DetailData()
            self._WriteIO._deserialize(params.get("WriteIO"))
        if params.get("Await") is not None:
            self._Await = DetailData()
            self._Await._deserialize(params.get("Await"))
        if params.get("Util") is not None:
            self._Util = DetailData()
            self._Util._deserialize(params.get("Util"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Site(AbstractModel):
    """客户站点信息

    """

    def __init__(self):
        r"""
        :param _Name: 站点名称
        :type Name: str
        :param _SiteId: 站点id
        :type SiteId: str
        :param _Description: 站点描述
        :type Description: str
        :param _CreateTime: 站点创建时间
        :type CreateTime: str
        """
        self._Name = None
        self._SiteId = None
        self._Description = None
        self._CreateTime = None

    @property
    def Name(self):
        """站点名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SiteId(self):
        """站点id
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def Description(self):
        """站点描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        """站点创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._SiteId = params.get("SiteId")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SiteDetail(AbstractModel):
    """站点详情

    """

    def __init__(self):
        r"""
        :param _SiteId: 站点id
        :type SiteId: str
        :param _Name: 站点名称
        :type Name: str
        :param _Description: 站点描述
        :type Description: str
        :param _CreateTime: 站点创建时间
        :type CreateTime: str
        :param _FiberType: 光纤类型
        :type FiberType: str
        :param _UplinkSpeedGbps: 网络到腾讯云Region区域的上行链路速度
        :type UplinkSpeedGbps: int
        :param _UplinkCount: 将CDC连接到网络时，每台CDC网络设备(每个机架 2 台设备)使用的上行链路数量。
        :type UplinkCount: int
        :param _OpticalStandard: 将CDC连接到网络时采用的光学标准
        :type OpticalStandard: str
        :param _RedundantNetworking: 是否提供冗余的上游设备(交换机或路由器)，以便两台  网络设备都能连接到网络设备。
        :type RedundantNetworking: bool
        :param _PowerConnectors: 电源连接器类型
        :type PowerConnectors: str
        :param _PowerFeedDrop: 从机架上方还是下方供电。
        :type PowerFeedDrop: str
        :param _PowerDrawKva: 功耗(KW)
        :type PowerDrawKva: float
        :param _ConditionRequirement: 是否满足下面环境条件：
1、场地没有材料要求或验收标准会影响 CDC 设备配送和安装。
2、确定的机架位置包含:
温度范围为 41 到 104°F (5 到 40°C)。
湿度范围为 10°F (-12°C)和 8% RH (相对湿度)到 70°F(21°C)和 80% RH。
机架位置的气流方向为从前向后，且应具有足够的 CFM (每分钟立方英尺)。CFM 必须是 CDC 配置的 kVA 功耗值的 145.8 倍。
        :type ConditionRequirement: bool
        :param _DimensionRequirement: 是否满足下面的尺寸条件：
您的装货站台可以容纳一个机架箱(高 x 宽 x 深 = 94" x 54" x 48")。
您可以提供从机架(高 x 宽 x 深 = 80" x 24" x 48")交货地点到机架最终安置位置的明确通道。测量深度时，应包括站台、走廊通道、门、转弯、坡道、货梯，并将其他通道限制考虑在内。
在最终的 CDC安置位置，前部间隙可以为 48" 或更大，后部间隙可以为 24" 或更大。
        :type DimensionRequirement: bool
        :param _MaxWeight: 最大承重(KG)
        :type MaxWeight: int
        :param _AddressLine: 站点地址
        :type AddressLine: str
        :param _OptionalAddressLine: 站点所在地区的详细地址信息（补充）
        :type OptionalAddressLine: str
        :param _NeedHelp: 是否需要腾讯云团队协助完成机架支撑工作
        :type NeedHelp: bool
        :param _BreakerRequirement: 上游断路器是否具备
        :type BreakerRequirement: bool
        :param _RedundantPower: 是否电源冗余
        :type RedundantPower: bool
        :param _Country: 站点所在国家
        :type Country: str
        :param _Province: 站点所在省份
        :type Province: str
        :param _City: 站点所在城市
        :type City: str
        :param _PostalCode: 站点所在地区的邮编
        :type PostalCode: int
        """
        self._SiteId = None
        self._Name = None
        self._Description = None
        self._CreateTime = None
        self._FiberType = None
        self._UplinkSpeedGbps = None
        self._UplinkCount = None
        self._OpticalStandard = None
        self._RedundantNetworking = None
        self._PowerConnectors = None
        self._PowerFeedDrop = None
        self._PowerDrawKva = None
        self._ConditionRequirement = None
        self._DimensionRequirement = None
        self._MaxWeight = None
        self._AddressLine = None
        self._OptionalAddressLine = None
        self._NeedHelp = None
        self._BreakerRequirement = None
        self._RedundantPower = None
        self._Country = None
        self._Province = None
        self._City = None
        self._PostalCode = None

    @property
    def SiteId(self):
        """站点id
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def Name(self):
        """站点名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """站点描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        """站点创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FiberType(self):
        """光纤类型
        :rtype: str
        """
        return self._FiberType

    @FiberType.setter
    def FiberType(self, FiberType):
        self._FiberType = FiberType

    @property
    def UplinkSpeedGbps(self):
        """网络到腾讯云Region区域的上行链路速度
        :rtype: int
        """
        return self._UplinkSpeedGbps

    @UplinkSpeedGbps.setter
    def UplinkSpeedGbps(self, UplinkSpeedGbps):
        self._UplinkSpeedGbps = UplinkSpeedGbps

    @property
    def UplinkCount(self):
        """将CDC连接到网络时，每台CDC网络设备(每个机架 2 台设备)使用的上行链路数量。
        :rtype: int
        """
        return self._UplinkCount

    @UplinkCount.setter
    def UplinkCount(self, UplinkCount):
        self._UplinkCount = UplinkCount

    @property
    def OpticalStandard(self):
        """将CDC连接到网络时采用的光学标准
        :rtype: str
        """
        return self._OpticalStandard

    @OpticalStandard.setter
    def OpticalStandard(self, OpticalStandard):
        self._OpticalStandard = OpticalStandard

    @property
    def RedundantNetworking(self):
        """是否提供冗余的上游设备(交换机或路由器)，以便两台  网络设备都能连接到网络设备。
        :rtype: bool
        """
        return self._RedundantNetworking

    @RedundantNetworking.setter
    def RedundantNetworking(self, RedundantNetworking):
        self._RedundantNetworking = RedundantNetworking

    @property
    def PowerConnectors(self):
        """电源连接器类型
        :rtype: str
        """
        return self._PowerConnectors

    @PowerConnectors.setter
    def PowerConnectors(self, PowerConnectors):
        self._PowerConnectors = PowerConnectors

    @property
    def PowerFeedDrop(self):
        """从机架上方还是下方供电。
        :rtype: str
        """
        return self._PowerFeedDrop

    @PowerFeedDrop.setter
    def PowerFeedDrop(self, PowerFeedDrop):
        self._PowerFeedDrop = PowerFeedDrop

    @property
    def PowerDrawKva(self):
        """功耗(KW)
        :rtype: float
        """
        return self._PowerDrawKva

    @PowerDrawKva.setter
    def PowerDrawKva(self, PowerDrawKva):
        self._PowerDrawKva = PowerDrawKva

    @property
    def ConditionRequirement(self):
        """是否满足下面环境条件：
1、场地没有材料要求或验收标准会影响 CDC 设备配送和安装。
2、确定的机架位置包含:
温度范围为 41 到 104°F (5 到 40°C)。
湿度范围为 10°F (-12°C)和 8% RH (相对湿度)到 70°F(21°C)和 80% RH。
机架位置的气流方向为从前向后，且应具有足够的 CFM (每分钟立方英尺)。CFM 必须是 CDC 配置的 kVA 功耗值的 145.8 倍。
        :rtype: bool
        """
        return self._ConditionRequirement

    @ConditionRequirement.setter
    def ConditionRequirement(self, ConditionRequirement):
        self._ConditionRequirement = ConditionRequirement

    @property
    def DimensionRequirement(self):
        """是否满足下面的尺寸条件：
您的装货站台可以容纳一个机架箱(高 x 宽 x 深 = 94" x 54" x 48")。
您可以提供从机架(高 x 宽 x 深 = 80" x 24" x 48")交货地点到机架最终安置位置的明确通道。测量深度时，应包括站台、走廊通道、门、转弯、坡道、货梯，并将其他通道限制考虑在内。
在最终的 CDC安置位置，前部间隙可以为 48" 或更大，后部间隙可以为 24" 或更大。
        :rtype: bool
        """
        return self._DimensionRequirement

    @DimensionRequirement.setter
    def DimensionRequirement(self, DimensionRequirement):
        self._DimensionRequirement = DimensionRequirement

    @property
    def MaxWeight(self):
        """最大承重(KG)
        :rtype: int
        """
        return self._MaxWeight

    @MaxWeight.setter
    def MaxWeight(self, MaxWeight):
        self._MaxWeight = MaxWeight

    @property
    def AddressLine(self):
        """站点地址
        :rtype: str
        """
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, AddressLine):
        self._AddressLine = AddressLine

    @property
    def OptionalAddressLine(self):
        """站点所在地区的详细地址信息（补充）
        :rtype: str
        """
        return self._OptionalAddressLine

    @OptionalAddressLine.setter
    def OptionalAddressLine(self, OptionalAddressLine):
        self._OptionalAddressLine = OptionalAddressLine

    @property
    def NeedHelp(self):
        """是否需要腾讯云团队协助完成机架支撑工作
        :rtype: bool
        """
        return self._NeedHelp

    @NeedHelp.setter
    def NeedHelp(self, NeedHelp):
        self._NeedHelp = NeedHelp

    @property
    def BreakerRequirement(self):
        """上游断路器是否具备
        :rtype: bool
        """
        return self._BreakerRequirement

    @BreakerRequirement.setter
    def BreakerRequirement(self, BreakerRequirement):
        self._BreakerRequirement = BreakerRequirement

    @property
    def RedundantPower(self):
        """是否电源冗余
        :rtype: bool
        """
        return self._RedundantPower

    @RedundantPower.setter
    def RedundantPower(self, RedundantPower):
        self._RedundantPower = RedundantPower

    @property
    def Country(self):
        """站点所在国家
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """站点所在省份
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """站点所在城市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def PostalCode(self):
        """站点所在地区的邮编
        :rtype: int
        """
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._FiberType = params.get("FiberType")
        self._UplinkSpeedGbps = params.get("UplinkSpeedGbps")
        self._UplinkCount = params.get("UplinkCount")
        self._OpticalStandard = params.get("OpticalStandard")
        self._RedundantNetworking = params.get("RedundantNetworking")
        self._PowerConnectors = params.get("PowerConnectors")
        self._PowerFeedDrop = params.get("PowerFeedDrop")
        self._PowerDrawKva = params.get("PowerDrawKva")
        self._ConditionRequirement = params.get("ConditionRequirement")
        self._DimensionRequirement = params.get("DimensionRequirement")
        self._MaxWeight = params.get("MaxWeight")
        self._AddressLine = params.get("AddressLine")
        self._OptionalAddressLine = params.get("OptionalAddressLine")
        self._NeedHelp = params.get("NeedHelp")
        self._BreakerRequirement = params.get("BreakerRequirement")
        self._RedundantPower = params.get("RedundantPower")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._PostalCode = params.get("PostalCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpngwBandwidthData(AbstractModel):
    """VPN网关的流量监控数据。

    """

    def __init__(self):
        r"""
        :param _OutBandwidth: 出带宽流量
        :type OutBandwidth: :class:`tencentcloud.cdc.v20201214.models.OutBandwidth`
        :param _InBandwidth: 入带宽流量
        :type InBandwidth: :class:`tencentcloud.cdc.v20201214.models.InBandwidth`
        """
        self._OutBandwidth = None
        self._InBandwidth = None

    @property
    def OutBandwidth(self):
        """出带宽流量
        :rtype: :class:`tencentcloud.cdc.v20201214.models.OutBandwidth`
        """
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InBandwidth(self):
        """入带宽流量
        :rtype: :class:`tencentcloud.cdc.v20201214.models.InBandwidth`
        """
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth


    def _deserialize(self, params):
        if params.get("OutBandwidth") is not None:
            self._OutBandwidth = OutBandwidth()
            self._OutBandwidth._deserialize(params.get("OutBandwidth"))
        if params.get("InBandwidth") is not None:
            self._InBandwidth = InBandwidth()
            self._InBandwidth._deserialize(params.get("InBandwidth"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区名称
        :type Zone: str
        :param _ZoneName: 可用区描述
        :type ZoneName: str
        :param _ZoneId: 可用区ID
        :type ZoneId: int
        :param _ZoneState: 可用区状态，包含AVAILABLE和UNAVAILABLE。AVAILABLE代表可用，UNAVAILABLE代表不可用。
        :type ZoneState: str
        """
        self._Zone = None
        self._ZoneName = None
        self._ZoneId = None
        self._ZoneState = None

    @property
    def Zone(self):
        """可用区名称
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        """可用区描述
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneId(self):
        """可用区ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneState(self):
        """可用区状态，包含AVAILABLE和UNAVAILABLE。AVAILABLE代表可用，UNAVAILABLE代表不可用。
        :rtype: str
        """
        return self._ZoneState

    @ZoneState.setter
    def ZoneState(self, ZoneState):
        self._ZoneState = ZoneState


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneState = params.get("ZoneState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        