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


class DescribeProductsRequest(AbstractModel):
    r"""DescribeProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductsResponse(AbstractModel):
    r"""DescribeProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 产品详细信息列表。
        :type Products: list of RegionProduct
        :param _TotalCount: 产品总数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Products = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Products(self):
        r"""产品详细信息列表。
        :rtype: list of RegionProduct
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def TotalCount(self):
        r"""产品总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = RegionProduct()
                obj._deserialize(item)
                self._Products.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    r"""DescribeRegions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 待查询产品的名称，例如cvm，具体取值请查询DescribeProducts接口
        :type Product: str
        """
        self._Product = None

    @property
    def Product(self):
        r"""待查询产品的名称，例如cvm，具体取值请查询DescribeProducts接口
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionsResponse(AbstractModel):
    r"""DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 地域数量
        :type TotalCount: int
        :param _RegionSet: 地域列表信息
        :type RegionSet: list of RegionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""地域数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        r"""地域列表信息
        :rtype: list of RegionInfo
        """
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    r"""DescribeZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 待查询产品的名称，例如cvm，具体取值请查询DescribeProducts接口
        :type Product: str
        """
        self._Product = None

    @property
    def Product(self):
        r"""待查询产品的名称，例如cvm，具体取值请查询DescribeProducts接口
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    r"""DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 可用区数量。
        :type TotalCount: int
        :param _ZoneSet: 可用区列表信息。
        :type ZoneSet: list of ZoneInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ZoneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""可用区数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ZoneSet(self):
        r"""可用区列表信息。
        :rtype: list of ZoneInfo
        """
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    r"""地域信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域名称，例如，ap-guangzhou
        :type Region: str
        :param _RegionName: 地域描述，例如，华南地区(广州)
        :type RegionName: str
        :param _RegionState: 地域是否可用状态
        :type RegionState: str
        :param _RegionTypeMC: 控制台类型，api调用时默认null
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionTypeMC: int
        :param _LocationMC: 不同语言的地区
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationMC: str
        :param _RegionNameMC: 控制台展示的地域描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionNameMC: str
        :param _RegionIdMC: 控制台展示的RegionId
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionIdMC: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionState = None
        self._RegionTypeMC = None
        self._LocationMC = None
        self._RegionNameMC = None
        self._RegionIdMC = None

    @property
    def Region(self):
        r"""地域名称，例如，ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        r"""地域描述，例如，华南地区(广州)
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        r"""地域是否可用状态
        :rtype: str
        """
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState

    @property
    def RegionTypeMC(self):
        r"""控制台类型，api调用时默认null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RegionTypeMC

    @RegionTypeMC.setter
    def RegionTypeMC(self, RegionTypeMC):
        self._RegionTypeMC = RegionTypeMC

    @property
    def LocationMC(self):
        r"""不同语言的地区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LocationMC

    @LocationMC.setter
    def LocationMC(self, LocationMC):
        self._LocationMC = LocationMC

    @property
    def RegionNameMC(self):
        r"""控制台展示的地域描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RegionNameMC

    @RegionNameMC.setter
    def RegionNameMC(self, RegionNameMC):
        self._RegionNameMC = RegionNameMC

    @property
    def RegionIdMC(self):
        r"""控制台展示的RegionId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RegionIdMC

    @RegionIdMC.setter
    def RegionIdMC(self, RegionIdMC):
        self._RegionIdMC = RegionIdMC


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionState = params.get("RegionState")
        self._RegionTypeMC = params.get("RegionTypeMC")
        self._LocationMC = params.get("LocationMC")
        self._RegionNameMC = params.get("RegionNameMC")
        self._RegionIdMC = params.get("RegionIdMC")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionProduct(AbstractModel):
    r"""地域管理系统支持的产品信息

    """

    def __init__(self):
        r"""
        :param _Name: 产品名称，如cvm
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        r"""产品名称，如cvm
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    r"""可用区信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区名称，例如，ap-guangzhou-3
全网可用区名称如下：
<li> ap-chongqing-1 </li>
<li> ap-seoul-1 </li>
<li> ap-seoul-2 </li>
<li> ap-chengdu-1 </li>
<li> ap-chengdu-2 </li>
<li> ap-hongkong-1 </li>
<li> ap-hongkong-2 </li>
<li> ap-shenzhen-fsi-1 </li>
<li> ap-shenzhen-fsi-2 </li>
<li> ap-shenzhen-fsi-3 </li>
<li> ap-guangzhou-1（售罄）</li>
<li> ap-guangzhou-2（售罄）</li>
<li> ap-guangzhou-3 </li>
<li> ap-guangzhou-4 </li>
<li> ap-guangzhou-6 </li>
<li> ap-tokyo-1 </li>
<li> ap-singapore-1 </li>
<li> ap-singapore-2 </li>
<li> ap-shanghai-fsi-1 </li>
<li> ap-shanghai-fsi-2 </li>
<li> ap-shanghai-fsi-3 </li>
<li> ap-bangkok-1 </li>
<li> ap-shanghai-1（售罄） </li>
<li> ap-shanghai-2 </li>
<li> ap-shanghai-3 </li>
<li> ap-shanghai-4 </li>
<li> ap-shanghai-5 </li>
<li> ap-mumbai-1 </li>
<li> ap-mumbai-2 </li>
<li> eu-moscow-1 </li>
<li> ap-beijing-1 </li>
<li> ap-beijing-2 </li>
<li> ap-beijing-3 </li>
<li> ap-beijing-4 </li>
<li> ap-beijing-5 </li>
<li> na-siliconvalley-1 </li>
<li> na-siliconvalley-2 </li>
<li> eu-frankfurt-1 </li>
<li> na-toronto-1 </li>
<li> na-ashburn-1 </li>
<li> na-ashburn-2 </li>
<li> ap-nanjing-1 </li>
<li> ap-nanjing-2 </li>
        :type Zone: str
        :param _ZoneName: 可用区描述，例如，广州三区
        :type ZoneName: str
        :param _ZoneId: 可用区ID
        :type ZoneId: str
        :param _ZoneState: 可用区状态，包含AVAILABLE和UNAVAILABLE。AVAILABLE代表可用，UNAVAILABLE代表不可用。
        :type ZoneState: str
        :param _ParentZone: 父级zone
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentZone: str
        :param _ParentZoneId: 父级可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentZoneId: str
        :param _ParentZoneName: 父级可用区描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentZoneName: str
        :param _ZoneType: zone类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneType: str
        :param _MachineRoomTypeMC: 控制台类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineRoomTypeMC: str
        :param _ZoneIdMC: 和ZoneId一样，适用于控制台调用
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneIdMC: str
        """
        self._Zone = None
        self._ZoneName = None
        self._ZoneId = None
        self._ZoneState = None
        self._ParentZone = None
        self._ParentZoneId = None
        self._ParentZoneName = None
        self._ZoneType = None
        self._MachineRoomTypeMC = None
        self._ZoneIdMC = None

    @property
    def Zone(self):
        r"""可用区名称，例如，ap-guangzhou-3
全网可用区名称如下：
<li> ap-chongqing-1 </li>
<li> ap-seoul-1 </li>
<li> ap-seoul-2 </li>
<li> ap-chengdu-1 </li>
<li> ap-chengdu-2 </li>
<li> ap-hongkong-1 </li>
<li> ap-hongkong-2 </li>
<li> ap-shenzhen-fsi-1 </li>
<li> ap-shenzhen-fsi-2 </li>
<li> ap-shenzhen-fsi-3 </li>
<li> ap-guangzhou-1（售罄）</li>
<li> ap-guangzhou-2（售罄）</li>
<li> ap-guangzhou-3 </li>
<li> ap-guangzhou-4 </li>
<li> ap-guangzhou-6 </li>
<li> ap-tokyo-1 </li>
<li> ap-singapore-1 </li>
<li> ap-singapore-2 </li>
<li> ap-shanghai-fsi-1 </li>
<li> ap-shanghai-fsi-2 </li>
<li> ap-shanghai-fsi-3 </li>
<li> ap-bangkok-1 </li>
<li> ap-shanghai-1（售罄） </li>
<li> ap-shanghai-2 </li>
<li> ap-shanghai-3 </li>
<li> ap-shanghai-4 </li>
<li> ap-shanghai-5 </li>
<li> ap-mumbai-1 </li>
<li> ap-mumbai-2 </li>
<li> eu-moscow-1 </li>
<li> ap-beijing-1 </li>
<li> ap-beijing-2 </li>
<li> ap-beijing-3 </li>
<li> ap-beijing-4 </li>
<li> ap-beijing-5 </li>
<li> na-siliconvalley-1 </li>
<li> na-siliconvalley-2 </li>
<li> eu-frankfurt-1 </li>
<li> na-toronto-1 </li>
<li> na-ashburn-1 </li>
<li> na-ashburn-2 </li>
<li> ap-nanjing-1 </li>
<li> ap-nanjing-2 </li>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        r"""可用区描述，例如，广州三区
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneId(self):
        r"""可用区ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneState(self):
        r"""可用区状态，包含AVAILABLE和UNAVAILABLE。AVAILABLE代表可用，UNAVAILABLE代表不可用。
        :rtype: str
        """
        return self._ZoneState

    @ZoneState.setter
    def ZoneState(self, ZoneState):
        self._ZoneState = ZoneState

    @property
    def ParentZone(self):
        r"""父级zone
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentZone

    @ParentZone.setter
    def ParentZone(self, ParentZone):
        self._ParentZone = ParentZone

    @property
    def ParentZoneId(self):
        r"""父级可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentZoneId

    @ParentZoneId.setter
    def ParentZoneId(self, ParentZoneId):
        self._ParentZoneId = ParentZoneId

    @property
    def ParentZoneName(self):
        r"""父级可用区描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentZoneName

    @ParentZoneName.setter
    def ParentZoneName(self, ParentZoneName):
        self._ParentZoneName = ParentZoneName

    @property
    def ZoneType(self):
        r"""zone类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneType

    @ZoneType.setter
    def ZoneType(self, ZoneType):
        self._ZoneType = ZoneType

    @property
    def MachineRoomTypeMC(self):
        r"""控制台类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MachineRoomTypeMC

    @MachineRoomTypeMC.setter
    def MachineRoomTypeMC(self, MachineRoomTypeMC):
        self._MachineRoomTypeMC = MachineRoomTypeMC

    @property
    def ZoneIdMC(self):
        r"""和ZoneId一样，适用于控制台调用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneIdMC

    @ZoneIdMC.setter
    def ZoneIdMC(self, ZoneIdMC):
        self._ZoneIdMC = ZoneIdMC


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneState = params.get("ZoneState")
        self._ParentZone = params.get("ParentZone")
        self._ParentZoneId = params.get("ParentZoneId")
        self._ParentZoneName = params.get("ParentZoneName")
        self._ZoneType = params.get("ZoneType")
        self._MachineRoomTypeMC = params.get("MachineRoomTypeMC")
        self._ZoneIdMC = params.get("ZoneIdMC")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        