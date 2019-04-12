# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class BillDetail(AbstractModel):
    """账单明细数据对象

    """

    def __init__(self):
        """
        :param BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        :param ProductCodeName: 子产品名称
        :type ProductCodeName: str
        :param PayModeName: 计费模式
        :type PayModeName: str
        :param ProjectName: 项目
        :type ProjectName: str
        :param RegionName: 区域
        :type RegionName: str
        :param ZoneName: 可用区
        :type ZoneName: str
        :param ResourceId: 资源实例ID
        :type ResourceId: str
        :param ResourceName: 实例名称
        :type ResourceName: str
        :param ActionTypeName: 交易类型
        :type ActionTypeName: str
        :param OrderId: 订单ID
        :type OrderId: str
        :param BillId: 交易ID
        :type BillId: str
        :param PayTime: 扣费时间
        :type PayTime: str
        :param FeeBeginTime: 开始使用时间
        :type FeeBeginTime: str
        :param FeeEndTime: 结束使用时间
        :type FeeEndTime: str
        :param ComponentSet: 组件列表
        :type ComponentSet: list of BillDetailComponent
        :param PayerUin: 支付者UIN
        :type PayerUin: str
        :param OwnerUin: 使用者UIN
        :type OwnerUin: str
        :param OperateUin: 操作者UIN
        :type OperateUin: str
        """
        self.BusinessCodeName = None
        self.ProductCodeName = None
        self.PayModeName = None
        self.ProjectName = None
        self.RegionName = None
        self.ZoneName = None
        self.ResourceId = None
        self.ResourceName = None
        self.ActionTypeName = None
        self.OrderId = None
        self.BillId = None
        self.PayTime = None
        self.FeeBeginTime = None
        self.FeeEndTime = None
        self.ComponentSet = None
        self.PayerUin = None
        self.OwnerUin = None
        self.OperateUin = None


    def _deserialize(self, params):
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.ProductCodeName = params.get("ProductCodeName")
        self.PayModeName = params.get("PayModeName")
        self.ProjectName = params.get("ProjectName")
        self.RegionName = params.get("RegionName")
        self.ZoneName = params.get("ZoneName")
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.ActionTypeName = params.get("ActionTypeName")
        self.OrderId = params.get("OrderId")
        self.BillId = params.get("BillId")
        self.PayTime = params.get("PayTime")
        self.FeeBeginTime = params.get("FeeBeginTime")
        self.FeeEndTime = params.get("FeeEndTime")
        if params.get("ComponentSet") is not None:
            self.ComponentSet = []
            for item in params.get("ComponentSet"):
                obj = BillDetailComponent()
                obj._deserialize(item)
                self.ComponentSet.append(obj)
        self.PayerUin = params.get("PayerUin")
        self.OwnerUin = params.get("OwnerUin")
        self.OperateUin = params.get("OperateUin")


class BillDetailComponent(AbstractModel):
    """账单明细组件对象

    """

    def __init__(self):
        """
        :param ComponentCodeName: 组件名称
        :type ComponentCodeName: str
        :param ItemCodeName: 组件类型名称
        :type ItemCodeName: str
        :param SinglePrice: 组件刊例价
        :type SinglePrice: str
        :param SpecifiedPrice: 组件指定价
        :type SpecifiedPrice: str
        :param PriceUnit: 价格单位
        :type PriceUnit: str
        :param UsedAmount: 组件用量
        :type UsedAmount: str
        :param UsedAmountUnit: 组件用量单位
        :type UsedAmountUnit: str
        :param TimeSpan: 使用时长
        :type TimeSpan: str
        :param TimeUnitName: 时长单位
        :type TimeUnitName: str
        :param Cost: 组件原价
        :type Cost: str
        :param Discount: 折扣率
        :type Discount: str
        :param ReduceType: 优惠类型
        :type ReduceType: str
        :param RealCost: 优惠后总价
        :type RealCost: str
        :param VoucherPayAmount: 代金券支付金额
        :type VoucherPayAmount: str
        :param CashPayAmount: 现金支付金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支付金额
        :type IncentivePayAmount: str
        """
        self.ComponentCodeName = None
        self.ItemCodeName = None
        self.SinglePrice = None
        self.SpecifiedPrice = None
        self.PriceUnit = None
        self.UsedAmount = None
        self.UsedAmountUnit = None
        self.TimeSpan = None
        self.TimeUnitName = None
        self.Cost = None
        self.Discount = None
        self.ReduceType = None
        self.RealCost = None
        self.VoucherPayAmount = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None


    def _deserialize(self, params):
        self.ComponentCodeName = params.get("ComponentCodeName")
        self.ItemCodeName = params.get("ItemCodeName")
        self.SinglePrice = params.get("SinglePrice")
        self.SpecifiedPrice = params.get("SpecifiedPrice")
        self.PriceUnit = params.get("PriceUnit")
        self.UsedAmount = params.get("UsedAmount")
        self.UsedAmountUnit = params.get("UsedAmountUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnitName = params.get("TimeUnitName")
        self.Cost = params.get("Cost")
        self.Discount = params.get("Discount")
        self.ReduceType = params.get("ReduceType")
        self.RealCost = params.get("RealCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")


class BillResourceSummary(AbstractModel):
    """账单资源汇总数据对象

    """

    def __init__(self):
        """
        :param BusinessCodeName: 产品
        :type BusinessCodeName: str
        :param ProductCodeName: 子产品
        :type ProductCodeName: str
        :param PayModeName: 计费模式
        :type PayModeName: str
        :param ProjectName: 项目
        :type ProjectName: str
        :param RegionName: 地域
        :type RegionName: str
        :param ZoneName: 可用区
        :type ZoneName: str
        :param ResourceId: 资源实例ID
        :type ResourceId: str
        :param ResourceName: 资源实例名称
        :type ResourceName: str
        :param ActionTypeName: 交易类型
        :type ActionTypeName: str
        :param OrderId: 订单ID
        :type OrderId: str
        :param PayTime: 扣费时间
        :type PayTime: str
        :param FeeBeginTime: 开始使用时间
        :type FeeBeginTime: str
        :param FeeEndTime: 结束使用时间
        :type FeeEndTime: str
        :param ConfigDesc: 配置描述
        :type ConfigDesc: str
        :param ExtendField1: 扩展字段1
        :type ExtendField1: str
        :param ExtendField2: 扩展字段2
        :type ExtendField2: str
        :param TotalCost: 原价，单位为元
        :type TotalCost: str
        :param Discount: 折扣率
        :type Discount: str
        :param ReduceType: 优惠类型
        :type ReduceType: str
        :param RealTotalCost: 优惠后总价，单位为元
        :type RealTotalCost: str
        :param VoucherPayAmount: 代金券支付金额，单位为元
        :type VoucherPayAmount: str
        :param CashPayAmount: 现金账户支付金额，单位为元
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支付金额，单位为元
        :type IncentivePayAmount: str
        :param ExtendField3: 扩展字段3
        :type ExtendField3: str
        :param ExtendField4: 扩展字段4
        :type ExtendField4: str
        :param ExtendField5: 扩展字段5
        :type ExtendField5: str
        """
        self.BusinessCodeName = None
        self.ProductCodeName = None
        self.PayModeName = None
        self.ProjectName = None
        self.RegionName = None
        self.ZoneName = None
        self.ResourceId = None
        self.ResourceName = None
        self.ActionTypeName = None
        self.OrderId = None
        self.PayTime = None
        self.FeeBeginTime = None
        self.FeeEndTime = None
        self.ConfigDesc = None
        self.ExtendField1 = None
        self.ExtendField2 = None
        self.TotalCost = None
        self.Discount = None
        self.ReduceType = None
        self.RealTotalCost = None
        self.VoucherPayAmount = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.ExtendField3 = None
        self.ExtendField4 = None
        self.ExtendField5 = None


    def _deserialize(self, params):
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.ProductCodeName = params.get("ProductCodeName")
        self.PayModeName = params.get("PayModeName")
        self.ProjectName = params.get("ProjectName")
        self.RegionName = params.get("RegionName")
        self.ZoneName = params.get("ZoneName")
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.ActionTypeName = params.get("ActionTypeName")
        self.OrderId = params.get("OrderId")
        self.PayTime = params.get("PayTime")
        self.FeeBeginTime = params.get("FeeBeginTime")
        self.FeeEndTime = params.get("FeeEndTime")
        self.ConfigDesc = params.get("ConfigDesc")
        self.ExtendField1 = params.get("ExtendField1")
        self.ExtendField2 = params.get("ExtendField2")
        self.TotalCost = params.get("TotalCost")
        self.Discount = params.get("Discount")
        self.ReduceType = params.get("ReduceType")
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.ExtendField3 = params.get("ExtendField3")
        self.ExtendField4 = params.get("ExtendField4")
        self.ExtendField5 = params.get("ExtendField5")


class Deal(AbstractModel):
    """订单数据对象

    """

    def __init__(self):
        """
        :param OrderId: 订单号
        :type OrderId: str
        :param Status: 订单状态
        :type Status: int
        :param Payer: 支付者
        :type Payer: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Creator: 创建人
        :type Creator: str
        :param RealTotalCost: 实际支付金额（分）
        :type RealTotalCost: int
        :param VoucherDecline: 代金券抵扣金额（分）
        :type VoucherDecline: int
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param GoodsCategoryId: 产品分类ID
        :type GoodsCategoryId: int
        :param ProductInfo: 产品详情
        :type ProductInfo: list of ProductInfo
        :param TimeSpan: 时长
        :type TimeSpan: float
        :param TimeUnit: 时间单位
        :type TimeUnit: str
        :param Currency: 货币单位
        :type Currency: str
        :param Policy: 折扣率
        :type Policy: float
        :param Price: 单价（分）
        :type Price: float
        :param TotalCost: 原价（分）
        :type TotalCost: float
        """
        self.OrderId = None
        self.Status = None
        self.Payer = None
        self.CreateTime = None
        self.Creator = None
        self.RealTotalCost = None
        self.VoucherDecline = None
        self.ProjectId = None
        self.GoodsCategoryId = None
        self.ProductInfo = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.Currency = None
        self.Policy = None
        self.Price = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Status = params.get("Status")
        self.Payer = params.get("Payer")
        self.CreateTime = params.get("CreateTime")
        self.Creator = params.get("Creator")
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherDecline = params.get("VoucherDecline")
        self.ProjectId = params.get("ProjectId")
        self.GoodsCategoryId = params.get("GoodsCategoryId")
        if params.get("ProductInfo") is not None:
            self.ProductInfo = []
            for item in params.get("ProductInfo"):
                obj = ProductInfo()
                obj._deserialize(item)
                self.ProductInfo.append(obj)
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.Currency = params.get("Currency")
        self.Policy = params.get("Policy")
        self.Price = params.get("Price")
        self.TotalCost = params.get("TotalCost")


class DescribeAccountBalanceRequest(AbstractModel):
    """DescribeAccountBalance请求参数结构体

    """


class DescribeAccountBalanceResponse(AbstractModel):
    """DescribeAccountBalance返回参数结构体

    """

    def __init__(self):
        """
        :param Balance: 云账户信息中的”展示可用余额”字段，单位为"分"
        :type Balance: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Balance = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Balance = params.get("Balance")
        self.RequestId = params.get("RequestId")


class DescribeBillDetailRequest(AbstractModel):
    """DescribeBillDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 数量，最大值为100
        :type Limit: int
        :param PeriodType: 周期类型，byPayTime按扣费周期/byUsedTime按计费周期。需要与费用中心该月份账单的周期保持一致。
        :type PeriodType: str
        :param Month: 月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。
        :type Month: str
        :param BeginTime: 周期开始时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。
        :type BeginTime: str
        :param EndTime: 周期结束时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。
        :type EndTime: str
        """
        self.Offset = None
        self.Limit = None
        self.PeriodType = None
        self.Month = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PeriodType = params.get("PeriodType")
        self.Month = params.get("Month")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")


class DescribeBillDetailResponse(AbstractModel):
    """DescribeBillDetail返回参数结构体

    """

    def __init__(self):
        """
        :param DetailSet: 详情列表
        :type DetailSet: list of BillDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DetailSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = BillDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillResourceSummaryRequest(AbstractModel):
    """DescribeBillResourceSummary请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 数量，最大值为1000
        :type Limit: int
        :param PeriodType: 周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。
        :type PeriodType: str
        :param Month: 月份，格式为yyyy-mm。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。
        :type Month: str
        """
        self.Offset = None
        self.Limit = None
        self.PeriodType = None
        self.Month = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PeriodType = params.get("PeriodType")
        self.Month = params.get("Month")


class DescribeBillResourceSummaryResponse(AbstractModel):
    """DescribeBillResourceSummary返回参数结构体

    """

    def __init__(self):
        """
        :param ResourceSummarySet: 资源汇总列表
        :type ResourceSummarySet: list of BillResourceSummary
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResourceSummarySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceSummarySet") is not None:
            self.ResourceSummarySet = []
            for item in params.get("ResourceSummarySet"):
                obj = BillResourceSummary()
                obj._deserialize(item)
                self.ResourceSummarySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDealsByCondRequest(AbstractModel):
    """DescribeDealsByCond请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Limit: 一页多少条数据，默认是20条，最大不超过1000
        :type Limit: int
        :param Offset: 第多少页，从0开始，默认是0
        :type Offset: int
        :param Status: 订单状态,默认为4（成功的订单）
订单的状态
1：未支付
2：已支付3：发货中
4：已发货
5：发货失败
6：已退款
7：已关单
8：订单过期
9：订单已失效
10：产品已失效
11：代付拒绝
12：支付中
        :type Status: int
        :param OrderId: 订单号
        :type OrderId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.OrderId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.OrderId = params.get("OrderId")


class DescribeDealsByCondResponse(AbstractModel):
    """DescribeDealsByCond返回参数结构体

    """

    def __init__(self):
        """
        :param Deals: 订单列表
        :type Deals: list of Deal
        :param TotalCount: 订单总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Deals = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Deals") is not None:
            self.Deals = []
            for item in params.get("Deals"):
                obj = Deal()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDosageDetailByDateRequest(AbstractModel):
    """DescribeDosageDetailByDate请求参数结构体

    """

    def __init__(self):
        """
        :param StartDate: 查询账单开始日期，如 2019-01-01
        :type StartDate: str
        :param EndDate: 查询账单结束日期，如 2019-01-01
        :type EndDate: str
        :param ProductCode: 视频业务：
10194   互动直播-核心机房           :
10195   互动直播-边缘机房

cdn业务：
10180：CDN静态加速流量(国内)
10181：CDN静态加速带宽(国内)
10182：CDN静态加速普通流量
10183：CDN静态加速普通带宽
10231：CDN静态加速流量(海外)
10232：CDN静态加速带宽(海外)

100967：弹性公网IP-按流量计费
101065：公网负载均衡-按流量计费
        :type ProductCode: str
        :param Domain: 查询域名 例如 www.qq.com
非CDN业务查询时可以设置为空
        :type Domain: str
        :param InstanceID: 1、如果为空，则返回EIP或CLB所有实例的明细；
2、如果传入实例名，则返回该实例明细
        :type InstanceID: str
        """
        self.StartDate = None
        self.EndDate = None
        self.ProductCode = None
        self.Domain = None
        self.InstanceID = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ProductCode = params.get("ProductCode")
        self.Domain = params.get("Domain")
        self.InstanceID = params.get("InstanceID")


class DescribeDosageDetailByDateResponse(AbstractModel):
    """DescribeDosageDetailByDate返回参数结构体

    """

    def __init__(self):
        """
        :param Unit: 计量单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param DetailSets: 用量数组
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailSets: list of DetailSet
        :param RetCode: 错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type RetCode: int
        :param RetMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RetMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Unit = None
        self.DetailSets = None
        self.RetCode = None
        self.RetMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Unit = params.get("Unit")
        if params.get("DetailSets") is not None:
            self.DetailSets = []
            for item in params.get("DetailSets"):
                obj = DetailSet()
                obj._deserialize(item)
                self.DetailSets.append(obj)
        self.RetCode = params.get("RetCode")
        self.RetMsg = params.get("RetMsg")
        self.RequestId = params.get("RequestId")


class DetailPoint(AbstractModel):
    """由时间和值组成的数据结构

    """

    def __init__(self):
        """
        :param Time: 时间
        :type Time: str
        :param Value: 值
        :type Value: str
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class DetailSet(AbstractModel):
    """由域名和使用明细组成的数据结构

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param DetailPoints: 使用数据明细
        :type DetailPoints: list of DetailPoint
        :param InstanceID: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceID: str
        """
        self.Domain = None
        self.DetailPoints = None
        self.InstanceID = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("DetailPoints") is not None:
            self.DetailPoints = []
            for item in params.get("DetailPoints"):
                obj = DetailPoint()
                obj._deserialize(item)
                self.DetailPoints.append(obj)
        self.InstanceID = params.get("InstanceID")


class PayDealsRequest(AbstractModel):
    """PayDeals请求参数结构体

    """

    def __init__(self):
        """
        :param OrderIds: 需要支付的一个或者多个订单号
        :type OrderIds: list of str
        :param AutoVoucher: 是否自动使用代金券,1:是,0否,默认0
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表,目前仅支持指定一张代金券
        :type VoucherIds: list of str
        """
        self.OrderIds = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class PayDealsResponse(AbstractModel):
    """PayDeals返回参数结构体

    """

    def __init__(self):
        """
        :param OrderIds: 此次操作支付成功的订单号数组
        :type OrderIds: list of str
        :param ResourceIds: 此次操作支付成功的资源Id数组
        :type ResourceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OrderIds = None
        self.ResourceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")
        self.ResourceIds = params.get("ResourceIds")
        self.RequestId = params.get("RequestId")


class ProductInfo(AbstractModel):
    """商品详细信息

    """

    def __init__(self):
        """
        :param Name: 商品详情名称标识
        :type Name: str
        :param Value: 商品详情
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")