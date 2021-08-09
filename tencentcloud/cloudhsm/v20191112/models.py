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


class DescribeHSMBySubnetIdRequest(AbstractModel):
    """DescribeHSMBySubnetId请求参数结构体

    """

    def __init__(self):
        """
        :param SubnetId: Subnet标识符\n        :type SubnetId: str\n        """
        self.SubnetId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHSMBySubnetIdResponse(AbstractModel):
    """DescribeHSMBySubnetId返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: HSM数量\n        :type TotalCount: int\n        :param SubnetId: 作为查询条件的SubnetId\n        :type SubnetId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SubnetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.SubnetId = params.get("SubnetId")
        self.RequestId = params.get("RequestId")


class DescribeHSMByVpcIdRequest(AbstractModel):
    """DescribeHSMByVpcId请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC标识符\n        :type VpcId: str\n        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHSMByVpcIdResponse(AbstractModel):
    """DescribeHSMByVpcId返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: HSM数量\n        :type TotalCount: int\n        :param VpcId: 作为查询条件的VpcId\n        :type VpcId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.VpcId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.VpcId = params.get("VpcId")
        self.RequestId = params.get("RequestId")


class DescribeSubnetRequest(AbstractModel):
    """DescribeSubnet请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量。\n        :type Limit: int\n        :param Offset: 偏移量。\n        :type Offset: int\n        :param VpcId: 查询指定VpcId下的子网信息。\n        :type VpcId: str\n        :param SearchWord: 查找关键字\n        :type SearchWord: str\n        """
        self.Limit = None
        self.Offset = None
        self.VpcId = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.VpcId = params.get("VpcId")
        self.SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetResponse(AbstractModel):
    """DescribeSubnet返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的子网数量。\n        :type TotalCount: int\n        :param SubnetList: 返回的子网实例列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetList: list of Subnet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SubnetList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SubnetList") is not None:
            self.SubnetList = []
            for item in params.get("SubnetList"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSupportedHsmRequest(AbstractModel):
    """DescribeSupportedHsm请求参数结构体

    """


class DescribeSupportedHsmResponse(AbstractModel):
    """DescribeSupportedHsm返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceTypes: 当前地域所支持的设备列表\n        :type DeviceTypes: list of DeviceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DeviceTypes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceTypes") is not None:
            self.DeviceTypes = []
            for item in params.get("DeviceTypes"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.DeviceTypes.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUsgRequest(AbstractModel):
    """DescribeUsg请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，当Offset和Limit均为0时将一次性返回用户所有的安全组列表。\n        :type Offset: int\n        :param Limit: 返回量，当Offset和Limit均为0时将一次性返回用户所有的安全组列表。\n        :type Limit: int\n        :param SearchWord: 搜索关键字\n        :type SearchWord: str\n        """
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsgResponse(AbstractModel):
    """DescribeUsg返回参数结构体

    """

    def __init__(self):
        """
        :param SgList: 用户的安全组列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SgList: list of SgUnit\n        :param TotalCount: 返回的安全组数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SgList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SgList") is not None:
            self.SgList = []
            for item in params.get("SgList"):
                obj = SgUnit()
                obj._deserialize(item)
                self.SgList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUsgRuleRequest(AbstractModel):
    """DescribeUsgRule请求参数结构体

    """

    def __init__(self):
        """
        :param SgIds: 根据安全组Id获取安全组详情\n        :type SgIds: list of str\n        """
        self.SgIds = None


    def _deserialize(self, params):
        self.SgIds = params.get("SgIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsgRuleResponse(AbstractModel):
    """DescribeUsgRule返回参数结构体

    """

    def __init__(self):
        """
        :param SgRules: 安全组详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type SgRules: list of UsgRuleDetail\n        :param TotalCount: 安全组详情数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SgRules = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SgRules") is not None:
            self.SgRules = []
            for item in params.get("SgRules"):
                obj = UsgRuleDetail()
                obj._deserialize(item)
                self.SgRules.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcRequest(AbstractModel):
    """DescribeVpc请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 返回偏移量。\n        :type Offset: int\n        :param Limit: 返回数量。\n        :type Limit: int\n        :param SearchWord: 搜索关键字\n        :type SearchWord: str\n        """
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcResponse(AbstractModel):
    """DescribeVpc返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 可查询到的所有Vpc实例总数。\n        :type TotalCount: int\n        :param VpcList: Vpc对象列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcList: list of Vpc\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.VpcList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpcList") is not None:
            self.VpcList = []
            for item in params.get("VpcList"):
                obj = Vpc()
                obj._deserialize(item)
                self.VpcList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVsmAttributesRequest(AbstractModel):
    """DescribeVsmAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceId: 资源Id\n        :type ResourceId: str\n        """
        self.ResourceId = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVsmAttributesResponse(AbstractModel):
    """DescribeVsmAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param ResourceId: 资源Id\n        :type ResourceId: str\n        :param ResourceName: 资源名称\n        :type ResourceName: str\n        :param Status: 资源状态，1表示资源为正常，2表示资源处于隔离状态\n        :type Status: int\n        :param Vip: 资源IP\n        :type Vip: str\n        :param VpcId: 资源所属Vpc\n        :type VpcId: str\n        :param SubnetId: 资源所属子网\n        :type SubnetId: str\n        :param Model: 资源所属HSM的规格\n        :type Model: str\n        :param VsmType: 资源类型，17表示EVSM，33表示GVSM，49表示SVSM\n        :type VsmType: int\n        :param RegionId: 地域Id，返回腾讯云地域代码，如广州为1，北京为8\n        :type RegionId: int\n        :param ZoneId: 区域Id，返回腾讯云每个地域的可用区代码\n        :type ZoneId: int\n        :param ExpireTime: 过期时间\n        :type ExpireTime: int\n        :param SgList: 安全组详情信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type SgList: list of UsgRuleDetail\n        :param SubnetName: 子网名
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetName: str\n        :param RegionName: 地域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionName: str\n        :param ZoneName: 区域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneName: str\n        :param Expired: 实例是否已经过期
注意：此字段可能返回 null，表示取不到有效值。\n        :type Expired: bool\n        :param RemainSeconds: 为正数表示实例距离过期时间剩余秒数，为负数表示实例已经过期多少秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type RemainSeconds: int\n        :param VpcName: 私有虚拟网络名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcName: str\n        :param VpcCidrBlock: VPC的IPv4 CIDR
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcCidrBlock: str\n        :param SubnetCidrBlock: 子网的CIDR
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetCidrBlock: str\n        :param Tags: 资源所关联的Tag
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param RenewFlag: 资源续费标识，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)
注意：此字段可能返回 null，表示取不到有效值。\n        :type RenewFlag: int\n        :param Manufacturer: 厂商
注意：此字段可能返回 null，表示取不到有效值。\n        :type Manufacturer: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResourceId = None
        self.ResourceName = None
        self.Status = None
        self.Vip = None
        self.VpcId = None
        self.SubnetId = None
        self.Model = None
        self.VsmType = None
        self.RegionId = None
        self.ZoneId = None
        self.ExpireTime = None
        self.SgList = None
        self.SubnetName = None
        self.RegionName = None
        self.ZoneName = None
        self.Expired = None
        self.RemainSeconds = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.SubnetCidrBlock = None
        self.Tags = None
        self.RenewFlag = None
        self.Manufacturer = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Model = params.get("Model")
        self.VsmType = params.get("VsmType")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.ExpireTime = params.get("ExpireTime")
        if params.get("SgList") is not None:
            self.SgList = []
            for item in params.get("SgList"):
                obj = UsgRuleDetail()
                obj._deserialize(item)
                self.SgList.append(obj)
        self.SubnetName = params.get("SubnetName")
        self.RegionName = params.get("RegionName")
        self.ZoneName = params.get("ZoneName")
        self.Expired = params.get("Expired")
        self.RemainSeconds = params.get("RemainSeconds")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RenewFlag = params.get("RenewFlag")
        self.Manufacturer = params.get("Manufacturer")
        self.RequestId = params.get("RequestId")


class DescribeVsmsRequest(AbstractModel):
    """DescribeVsms请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移\n        :type Offset: int\n        :param Limit: 最大数量\n        :type Limit: int\n        :param SearchWord: 查询关键字\n        :type SearchWord: str\n        :param TagFilters: 标签过滤条件\n        :type TagFilters: list of TagFilter\n        :param Manufacturer: 设备所属的厂商名称，根据厂商来进行筛选\n        :type Manufacturer: str\n        """
        self.Offset = None
        self.Limit = None
        self.SearchWord = None
        self.TagFilters = None
        self.Manufacturer = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.Manufacturer = params.get("Manufacturer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVsmsResponse(AbstractModel):
    """DescribeVsms返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 获取实例的总个数\n        :type TotalCount: int\n        :param VsmList: 资源信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type VsmList: list of ResourceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.VsmList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VsmList") is not None:
            self.VsmList = []
            for item in params.get("VsmList"):
                obj = ResourceInfo()
                obj._deserialize(item)
                self.VsmList.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    """设备厂商信息

    """

    def __init__(self):
        """
        :param Manufacturer: 厂商名称\n        :type Manufacturer: str\n        :param HsmTypes: 此厂商旗下的设备信息列表\n        :type HsmTypes: list of HsmInfo\n        """
        self.Manufacturer = None
        self.HsmTypes = None


    def _deserialize(self, params):
        self.Manufacturer = params.get("Manufacturer")
        if params.get("HsmTypes") is not None:
            self.HsmTypes = []
            for item in params.get("HsmTypes"):
                obj = HsmInfo()
                obj._deserialize(item)
                self.HsmTypes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HsmInfo(AbstractModel):
    """支持的加密机类型信息

    """

    def __init__(self):
        """
        :param Model: 加密机型号\n        :type Model: str\n        :param VsmTypes: 此类型的加密机所支持的VSM类型列表\n        :type VsmTypes: list of VsmInfo\n        """
        self.Model = None
        self.VsmTypes = None


    def _deserialize(self, params):
        self.Model = params.get("Model")
        if params.get("VsmTypes") is not None:
            self.VsmTypes = []
            for item in params.get("VsmTypes"):
                obj = VsmInfo()
                obj._deserialize(item)
                self.VsmTypes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceBuyVsmRequest(AbstractModel):
    """InquiryPriceBuyVsm请求参数结构体

    """

    def __init__(self):
        """
        :param GoodsNum: 需购买实例的数量\n        :type GoodsNum: int\n        :param PayMode: 付费模式：0表示按需计费/后付费，1表示预付费\n        :type PayMode: int\n        :param TimeSpan: 商品的时间大小\n        :type TimeSpan: str\n        :param TimeUnit: 商品的时间单位，m表示月，y表示年\n        :type TimeUnit: str\n        :param Currency: 货币类型，默认为CNY\n        :type Currency: str\n        :param Type: 默认为CREATE，可选RENEW\n        :type Type: str\n        """
        self.GoodsNum = None
        self.PayMode = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.Currency = None
        self.Type = None


    def _deserialize(self, params):
        self.GoodsNum = params.get("GoodsNum")
        self.PayMode = params.get("PayMode")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.Currency = params.get("Currency")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceBuyVsmResponse(AbstractModel):
    """InquiryPriceBuyVsm返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCost: 原始总金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCost: float\n        :param GoodsNum: 购买的实例数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type GoodsNum: int\n        :param TimeSpan: 商品的时间大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeSpan: str\n        :param TimeUnit: 商品的时间单位
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeUnit: str\n        :param OriginalCost: 应付总金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginalCost: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCost = None
        self.GoodsNum = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.OriginalCost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCost = params.get("TotalCost")
        self.GoodsNum = params.get("GoodsNum")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.OriginalCost = params.get("OriginalCost")
        self.RequestId = params.get("RequestId")


class ModifyVsmAttributesRequest(AbstractModel):
    """ModifyVsmAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceId: 资源Id\n        :type ResourceId: str\n        :param Type: UpdateResourceName-修改资源名称,
UpdateSgIds-修改安全组名称,
UpdateNetWork-修改网络,
Default-默认不修改\n        :type Type: list of str\n        :param ResourceName: 资源名称\n        :type ResourceName: str\n        :param SgIds: 安全组Id\n        :type SgIds: list of str\n        :param VpcId: 虚拟专网Id\n        :type VpcId: str\n        :param SubnetId: 子网Id\n        :type SubnetId: str\n        """
        self.ResourceId = None
        self.Type = None
        self.ResourceName = None
        self.SgIds = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Type = params.get("Type")
        self.ResourceName = params.get("ResourceName")
        self.SgIds = params.get("SgIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVsmAttributesResponse(AbstractModel):
    """ModifyVsmAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceInfo(AbstractModel):
    """资源信息

    """

    def __init__(self):
        """
        :param ResourceId: 资源Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceId: str\n        :param ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceName: str\n        :param Status: 资源状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param Vip: 资源IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type Vip: str\n        :param VpcId: 资源所属Vpc
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param SubnetId: 资源所属子网
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetId: str\n        :param Model: 资源所属HSM规格
注意：此字段可能返回 null，表示取不到有效值。\n        :type Model: str\n        :param VsmType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type VsmType: int\n        :param RegionId: 地域Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionId: int\n        :param ZoneId: 区域Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneId: int\n        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireTime: int\n        :param RegionName: 地域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionName: str\n        :param ZoneName: 区域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneName: str\n        :param SgList: 实例的安全组列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SgList: list of SgUnit\n        :param SubnetName: 子网名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetName: str\n        :param Expired: 当前实例是否已经过期
注意：此字段可能返回 null，表示取不到有效值。\n        :type Expired: bool\n        :param RemainSeconds: 为正数表示实例距离过期时间还剩余多少秒，为负数表示已经过期多少秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type RemainSeconds: int\n        :param VpcName: Vpc名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcName: str\n        :param CreateUin: 创建者Uin账号
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateUin: str\n        :param RenewFlag: 自动续费状态标识， 0-手动续费，1-自动续费，2-到期不续
注意：此字段可能返回 null，表示取不到有效值。\n        :type RenewFlag: int\n        :param Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param Manufacturer: 厂商
注意：此字段可能返回 null，表示取不到有效值。\n        :type Manufacturer: str\n        """
        self.ResourceId = None
        self.ResourceName = None
        self.Status = None
        self.Vip = None
        self.VpcId = None
        self.SubnetId = None
        self.Model = None
        self.VsmType = None
        self.RegionId = None
        self.ZoneId = None
        self.ExpireTime = None
        self.RegionName = None
        self.ZoneName = None
        self.SgList = None
        self.SubnetName = None
        self.Expired = None
        self.RemainSeconds = None
        self.VpcName = None
        self.CreateUin = None
        self.RenewFlag = None
        self.Tags = None
        self.Manufacturer = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Model = params.get("Model")
        self.VsmType = params.get("VsmType")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.ExpireTime = params.get("ExpireTime")
        self.RegionName = params.get("RegionName")
        self.ZoneName = params.get("ZoneName")
        if params.get("SgList") is not None:
            self.SgList = []
            for item in params.get("SgList"):
                obj = SgUnit()
                obj._deserialize(item)
                self.SgList.append(obj)
        self.SubnetName = params.get("SubnetName")
        self.Expired = params.get("Expired")
        self.RemainSeconds = params.get("RemainSeconds")
        self.VpcName = params.get("VpcName")
        self.CreateUin = params.get("CreateUin")
        self.RenewFlag = params.get("RenewFlag")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Manufacturer = params.get("Manufacturer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SgUnit(AbstractModel):
    """安全组基础信息

    """

    def __init__(self):
        """
        :param SgId: 安全组Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type SgId: str\n        :param SgName: 安全组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type SgName: str\n        :param SgRemark: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type SgRemark: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        """
        self.SgId = None
        self.SgName = None
        self.SgRemark = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.SgId = params.get("SgId")
        self.SgName = params.get("SgName")
        self.SgRemark = params.get("SgRemark")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Subnet(AbstractModel):
    """Subnet对象

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param SubnetId: 子网实例ID，例如：subnet-bthucmmy。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetId: str\n        :param SubnetName: 子网名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetName: str\n        :param CidrBlock: 子网的 IPv4 CIDR。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CidrBlock: str\n        :param CreatedTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param AvailableIpAddressCount: 可用IP数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AvailableIpAddressCount: int\n        :param Ipv6CidrBlock: 子网的 IPv6 CIDR。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv6CidrBlock: str\n        :param TotalIpAddressCount: 总IP数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalIpAddressCount: int\n        :param IsDefault: 是否为默认Subnet
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDefault: bool\n        """
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.CreatedTime = None
        self.AvailableIpAddressCount = None
        self.Ipv6CidrBlock = None
        self.TotalIpAddressCount = None
        self.IsDefault = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.CreatedTime = params.get("CreatedTime")
        self.AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.TotalIpAddressCount = params.get("TotalIpAddressCount")
        self.IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """标签过滤参数

    """

    def __init__(self):
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: list of str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsgPolicy(AbstractModel):
    """安全组策略

    """

    def __init__(self):
        """
        :param Ip: cidr格式地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ip: str\n        :param Id: 安全组id代表的地址集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: str\n        :param AddressModule: 地址组id代表的地址集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type AddressModule: str\n        :param Proto: 协议
注意：此字段可能返回 null，表示取不到有效值。\n        :type Proto: str\n        :param Port: 端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: str\n        :param ServiceModule: 服务组id代表的协议和端口集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceModule: str\n        :param Desc: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Desc: str\n        :param Action: 匹配后行为:ACCEPT/DROP
注意：此字段可能返回 null，表示取不到有效值。\n        :type Action: str\n        """
        self.Ip = None
        self.Id = None
        self.AddressModule = None
        self.Proto = None
        self.Port = None
        self.ServiceModule = None
        self.Desc = None
        self.Action = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Id = params.get("Id")
        self.AddressModule = params.get("AddressModule")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.ServiceModule = params.get("ServiceModule")
        self.Desc = params.get("Desc")
        self.Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsgRuleDetail(AbstractModel):
    """安全组规则详情

    """

    def __init__(self):
        """
        :param InBound: 入站规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type InBound: list of UsgPolicy\n        :param OutBound: 出站规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutBound: list of UsgPolicy\n        :param SgId: 安全组Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type SgId: str\n        :param SgName: 安全组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type SgName: str\n        :param SgRemark: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type SgRemark: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param Version: 版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type Version: int\n        """
        self.InBound = None
        self.OutBound = None
        self.SgId = None
        self.SgName = None
        self.SgRemark = None
        self.CreateTime = None
        self.Version = None


    def _deserialize(self, params):
        if params.get("InBound") is not None:
            self.InBound = []
            for item in params.get("InBound"):
                obj = UsgPolicy()
                obj._deserialize(item)
                self.InBound.append(obj)
        if params.get("OutBound") is not None:
            self.OutBound = []
            for item in params.get("OutBound"):
                obj = UsgPolicy()
                obj._deserialize(item)
                self.OutBound.append(obj)
        self.SgId = params.get("SgId")
        self.SgName = params.get("SgName")
        self.SgRemark = params.get("SgRemark")
        self.CreateTime = params.get("CreateTime")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Vpc(AbstractModel):
    """VPC对象

    """

    def __init__(self):
        """
        :param VpcName: Vpc名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcName: str\n        :param VpcId: VpcId
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param IsDefault: 是否为默认VPC
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDefault: bool\n        """
        self.VpcName = None
        self.VpcId = None
        self.CreatedTime = None
        self.IsDefault = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.VpcId = params.get("VpcId")
        self.CreatedTime = params.get("CreatedTime")
        self.IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VsmInfo(AbstractModel):
    """支持的Vsm类型信息

    """

    def __init__(self):
        """
        :param TypeName: VSM类型名称\n        :type TypeName: str\n        :param TypeID: VSM类型值\n        :type TypeID: int\n        """
        self.TypeName = None
        self.TypeID = None


    def _deserialize(self, params):
        self.TypeName = params.get("TypeName")
        self.TypeID = params.get("TypeID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        