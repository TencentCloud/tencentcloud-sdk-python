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
        r"""
        :param SubnetId: Subnet标识符
        :type SubnetId: str
        """
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
        r"""
        :param TotalCount: HSM数量
        :type TotalCount: int
        :param SubnetId: 作为查询条件的SubnetId
        :type SubnetId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param VpcId: VPC标识符
        :type VpcId: str
        """
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
        r"""
        :param TotalCount: HSM数量
        :type TotalCount: int
        :param VpcId: 作为查询条件的VpcId
        :type VpcId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Limit: 返回数量。
        :type Limit: int
        :param Offset: 偏移量。
        :type Offset: int
        :param VpcId: 查询指定VpcId下的子网信息。
        :type VpcId: str
        :param SearchWord: 查找关键字
        :type SearchWord: str
        """
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
        r"""
        :param TotalCount: 返回的子网数量。
        :type TotalCount: int
        :param SubnetList: 返回的子网实例列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetList: list of Subnet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param DeviceTypes: 当前地域所支持的设备列表
        :type DeviceTypes: list of DeviceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Offset: 偏移量，当Offset和Limit均为0时将一次性返回用户所有的安全组列表。
        :type Offset: int
        :param Limit: 返回量，当Offset和Limit均为0时将一次性返回用户所有的安全组列表。
        :type Limit: int
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        """
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
        r"""
        :param SgList: 用户的安全组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SgList: list of SgUnit
        :param TotalCount: 返回的安全组数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param SgIds: 根据安全组Id获取安全组详情
        :type SgIds: list of str
        """
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
        r"""
        :param SgRules: 安全组详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SgRules: list of UsgRuleDetail
        :param TotalCount: 安全组详情数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Offset: 返回偏移量。
        :type Offset: int
        :param Limit: 返回数量。
        :type Limit: int
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        """
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
        r"""
        :param TotalCount: 可查询到的所有Vpc实例总数。
        :type TotalCount: int
        :param VpcList: Vpc对象列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcList: list of Vpc
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ResourceId: 资源Id
        :type ResourceId: str
        """
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
        r"""
        :param ResourceId: 资源Id
        :type ResourceId: str
        :param ResourceName: 资源名称
        :type ResourceName: str
        :param Status: 资源状态，1表示资源为正常，2表示资源处于隔离状态
        :type Status: int
        :param Vip: 资源IP
        :type Vip: str
        :param VpcId: 资源所属Vpc
        :type VpcId: str
        :param SubnetId: 资源所属子网
        :type SubnetId: str
        :param Model: 资源所属HSM的规格
        :type Model: str
        :param VsmType: 资源类型，17表示EVSM，33表示GVSM，49表示SVSM
        :type VsmType: int
        :param RegionId: 地域Id，返回腾讯云地域代码，如广州为1，北京为8
        :type RegionId: int
        :param ZoneId: 区域Id，返回腾讯云每个地域的可用区代码
        :type ZoneId: int
        :param ExpireTime: 过期时间
        :type ExpireTime: int
        :param SgList: 安全组详情信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SgList: list of UsgRuleDetail
        :param SubnetName: 子网名
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param RegionName: 地域名
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param ZoneName: 区域名
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneName: str
        :param Expired: 实例是否已经过期
注意：此字段可能返回 null，表示取不到有效值。
        :type Expired: bool
        :param RemainSeconds: 为正数表示实例距离过期时间剩余秒数，为负数表示实例已经过期多少秒
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainSeconds: int
        :param VpcName: 私有虚拟网络名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param VpcCidrBlock: VPC的IPv4 CIDR
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcCidrBlock: str
        :param SubnetCidrBlock: 子网的CIDR
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetCidrBlock: str
        :param Tags: 资源所关联的Tag
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param RenewFlag: 资源续费标识，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param Manufacturer: 厂商
注意：此字段可能返回 null，表示取不到有效值。
        :type Manufacturer: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Offset: 偏移
        :type Offset: int
        :param Limit: 最大数量
        :type Limit: int
        :param SearchWord: 查询关键字
        :type SearchWord: str
        :param TagFilters: 标签过滤条件
        :type TagFilters: list of TagFilter
        :param Manufacturer: 设备所属的厂商名称，根据厂商来进行筛选
        :type Manufacturer: str
        """
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
        r"""
        :param TotalCount: 获取实例的总个数
        :type TotalCount: int
        :param VsmList: 资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VsmList: list of ResourceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Manufacturer: 厂商名称
        :type Manufacturer: str
        :param HsmTypes: 此厂商旗下的设备信息列表
        :type HsmTypes: list of HsmInfo
        """
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
        r"""
        :param Model: 加密机型号
        :type Model: str
        :param VsmTypes: 此类型的加密机所支持的VSM类型列表
        :type VsmTypes: list of VsmInfo
        """
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
        r"""
        :param GoodsNum: 需购买实例的数量
        :type GoodsNum: int
        :param PayMode: 付费模式：0表示按需计费/后付费，1表示预付费
        :type PayMode: int
        :param TimeSpan: 商品的时间大小
        :type TimeSpan: str
        :param TimeUnit: 商品的时间单位，m表示月，y表示年
        :type TimeUnit: str
        :param Currency: 货币类型，默认为CNY
        :type Currency: str
        :param Type: 默认为CREATE，可选RENEW
        :type Type: str
        """
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
        r"""
        :param TotalCost: 原始总金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: float
        :param GoodsNum: 购买的实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsNum: int
        :param TimeSpan: 商品的时间大小
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: str
        :param TimeUnit: 商品的时间单位
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param OriginalCost: 应付总金额
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ResourceId: 资源Id
        :type ResourceId: str
        :param Type: UpdateResourceName-修改资源名称,
UpdateSgIds-修改安全组名称,
UpdateNetWork-修改网络,
Default-默认不修改
        :type Type: list of str
        :param ResourceName: 资源名称
        :type ResourceName: str
        :param SgIds: 安全组Id
        :type SgIds: list of str
        :param VpcId: 虚拟专网Id
        :type VpcId: str
        :param SubnetId: 子网Id
        :type SubnetId: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceInfo(AbstractModel):
    """资源信息

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param Status: 资源状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Vip: 资源IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param VpcId: 资源所属Vpc
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 资源所属子网
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param Model: 资源所属HSM规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: str
        :param VsmType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VsmType: int
        :param RegionId: 地域Id
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param ZoneId: 区域Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param RegionName: 地域名
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param ZoneName: 区域名
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneName: str
        :param SgList: 实例的安全组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SgList: list of SgUnit
        :param SubnetName: 子网名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param Expired: 当前实例是否已经过期
注意：此字段可能返回 null，表示取不到有效值。
        :type Expired: bool
        :param RemainSeconds: 为正数表示实例距离过期时间还剩余多少秒，为负数表示已经过期多少秒
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainSeconds: int
        :param VpcName: Vpc名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param CreateUin: 创建者Uin账号
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: str
        :param RenewFlag: 自动续费状态标识， 0-手动续费，1-自动续费，2-到期不续
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Manufacturer: 厂商
注意：此字段可能返回 null，表示取不到有效值。
        :type Manufacturer: str
        """
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
        r"""
        :param SgId: 安全组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SgId: str
        :param SgName: 安全组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SgName: str
        :param SgRemark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type SgRemark: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
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
        r"""
        :param VpcId: VPC实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 子网实例ID，例如：subnet-bthucmmy。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param SubnetName: 子网名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param CidrBlock: 子网的 IPv4 CIDR。
注意：此字段可能返回 null，表示取不到有效值。
        :type CidrBlock: str
        :param CreatedTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param AvailableIpAddressCount: 可用IP数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableIpAddressCount: int
        :param Ipv6CidrBlock: 子网的 IPv6 CIDR。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6CidrBlock: str
        :param TotalIpAddressCount: 总IP数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalIpAddressCount: int
        :param IsDefault: 是否为默认Subnet
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: bool
        """
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
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
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
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: list of str
        """
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
        r"""
        :param Ip: cidr格式地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Id: 安全组id代表的地址集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param AddressModule: 地址组id代表的地址集合
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressModule: str
        :param Proto: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Proto: str
        :param Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        :param ServiceModule: 服务组id代表的协议和端口集合
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceModule: str
        :param Desc: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param Action: 匹配后行为:ACCEPT/DROP
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        """
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
        r"""
        :param InBound: 入站规则
注意：此字段可能返回 null，表示取不到有效值。
        :type InBound: list of UsgPolicy
        :param OutBound: 出站规则
注意：此字段可能返回 null，表示取不到有效值。
        :type OutBound: list of UsgPolicy
        :param SgId: 安全组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SgId: str
        :param SgName: 安全组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SgName: str
        :param SgRemark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type SgRemark: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Version: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: int
        """
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
        r"""
        :param VpcName: Vpc名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param VpcId: VpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param IsDefault: 是否为默认VPC
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: bool
        """
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
        r"""
        :param TypeName: VSM类型名称
        :type TypeName: str
        :param TypeID: VSM类型值
        :type TypeID: int
        """
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
        