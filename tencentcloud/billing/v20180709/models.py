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


class ActionSummaryOverviewItem(AbstractModel):
    """按交易类型汇总消费详情

    """

    def __init__(self):
        """
        :param ActionType: 交易类型：包年包月新购/续费/升降配/退款、按量计费扣费、调账补偿/扣费等类型
        :type ActionType: str
        :param ActionTypeName: 交易类型名称
        :type ActionTypeName: str
        :param RealTotalCost: 实际花费
        :type RealTotalCost: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param CashPayAmount: 现金金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送金金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 代金券金额
        :type VoucherPayAmount: str
        :param BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        """
        self.ActionType = None
        self.ActionTypeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        self.ActionTypeName = params.get("ActionTypeName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")


class BillDetail(AbstractModel):
    """账单明细数据对象

    """

    def __init__(self):
        """
        :param BusinessCodeName: 产品名称：云产品大类，如云服务器CVM、云数据库MySQL
        :type BusinessCodeName: str
        :param ProductCodeName: 子产品名称：云产品子类，如云服务器CVM-标准型S1
        :type ProductCodeName: str
        :param PayModeName: 计费模式：包年包月和按量计费
        :type PayModeName: str
        :param ProjectName: 项目:资源所属项目
        :type ProjectName: str
        :param RegionName: 区域：资源所属地域，如华南地区（广州）
        :type RegionName: str
        :param ZoneName: 可用区：资源所属可用区，如广州三区
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
        :param Tags: Tag 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of BillTagInfo
        :param BusinessCode: 商品名称代码（未开放的字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessCode: str
        :param ProductCode: 子商品名称代码 （未开放的字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param ActionType: 交易类型代码（未开放的字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionType: str
        :param RegionId: 区域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
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
        self.Tags = None
        self.BusinessCode = None
        self.ProductCode = None
        self.ActionType = None
        self.RegionId = None


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
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.BusinessCode = params.get("BusinessCode")
        self.ProductCode = params.get("ProductCode")
        self.ActionType = params.get("ActionType")
        self.RegionId = params.get("RegionId")


class BillDetailComponent(AbstractModel):
    """账单明细组件对象

    """

    def __init__(self):
        """
        :param ComponentCodeName: 组件类型:资源组件类型的名称，如内存、硬盘等
        :type ComponentCodeName: str
        :param ItemCodeName: 组件名称:资源组件的名称，如云数据库MySQL-内存等
        :type ItemCodeName: str
        :param SinglePrice: 组件刊例价:资源组件的原始价格，保持原始粒度
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
        :param ItemCode: 组件类型代码（未开放的字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemCode: str
        :param ComponentCode: 组件名称代码（未开放的字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentCode: str
        :param ContractPrice: 合同价
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractPrice: str
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
        self.ItemCode = None
        self.ComponentCode = None
        self.ContractPrice = None


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
        self.ItemCode = params.get("ItemCode")
        self.ComponentCode = params.get("ComponentCode")
        self.ContractPrice = params.get("ContractPrice")


class BillResourceSummary(AbstractModel):
    """账单资源汇总数据对象

    """

    def __init__(self):
        """
        :param BusinessCodeName: 产品名称：云产品大类，如云服务器CVM、云数据库MySQL
        :type BusinessCodeName: str
        :param ProductCodeName: 子产品：云产品子类，如云服务器CVM-标准型S1， 当没有获取到子产品名称时，返回"-"
        :type ProductCodeName: str
        :param PayModeName: 计费模式：包年包月和按量计费
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
        :param ActionTypeName: 交易类型：包年包月新购/续费/升降配/退款、按量计费扣费、调账补偿/扣费等类型
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
        :param Tags: Tag 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of BillTagInfo
        :param PayerUin: 付款方uin
        :type PayerUin: str
        :param OwnerUin: 资源所有者uin,无值则返回"-"
        :type OwnerUin: str
        :param OperateUin: 操作者uin,无值则返回"-"
        :type OperateUin: str
        :param BusinessCode: 商品名称代码
        :type BusinessCode: str
        :param ProductCode: 子商品名称代码
        :type ProductCode: str
        :param RegionId: 区域ID
        :type RegionId: int
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
        self.Tags = None
        self.PayerUin = None
        self.OwnerUin = None
        self.OperateUin = None
        self.BusinessCode = None
        self.ProductCode = None
        self.RegionId = None


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
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.PayerUin = params.get("PayerUin")
        self.OwnerUin = params.get("OwnerUin")
        self.OperateUin = params.get("OperateUin")
        self.BusinessCode = params.get("BusinessCode")
        self.ProductCode = params.get("ProductCode")
        self.RegionId = params.get("RegionId")


class BillTagInfo(AbstractModel):
    """账单 Tag 信息

    """

    def __init__(self):
        """
        :param TagKey: 分账标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class BillTransactionInfo(AbstractModel):
    """收支明细的流水信息

    """

    def __init__(self):
        """
        :param ActionType: 收支类型：deduct 扣费, recharge 充值, return 退费， block 冻结, unblock 解冻
        :type ActionType: str
        :param Amount: 流水金额，单位（分）；正数表示入账，负数表示出账
        :type Amount: int
        :param Balance: 可用余额，单位（分）；正数表示入账，负数表示出账
        :type Balance: int
        :param BillId: 流水号，如20190131020000236005203583326401
        :type BillId: str
        :param OperationInfo: 描述信息
        :type OperationInfo: str
        :param OperationTime: 操作时间"2019-01-31 23:35:10.000"
        :type OperationTime: str
        :param Cash: 现金账户余额，单位（分）
        :type Cash: int
        :param Incentive: 赠送金余额，单位（分）
        :type Incentive: int
        :param Freezing: 冻结余额，单位（分）
        :type Freezing: int
        """
        self.ActionType = None
        self.Amount = None
        self.Balance = None
        self.BillId = None
        self.OperationInfo = None
        self.OperationTime = None
        self.Cash = None
        self.Incentive = None
        self.Freezing = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        self.Amount = params.get("Amount")
        self.Balance = params.get("Balance")
        self.BillId = params.get("BillId")
        self.OperationInfo = params.get("OperationInfo")
        self.OperationTime = params.get("OperationTime")
        self.Cash = params.get("Cash")
        self.Incentive = params.get("Incentive")
        self.Freezing = params.get("Freezing")


class BusinessSummaryOverviewItem(AbstractModel):
    """按产品汇总产品详情

    """

    def __init__(self):
        """
        :param BusinessCode: 产品码
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessCode: str
        :param BusinessCodeName: 产品名称：云产品大类，如云服务器CVM、云数据库MySQL
        :type BusinessCodeName: str
        :param RealTotalCost: 实际花费
        :type RealTotalCost: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param CashPayAmount: 现金金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送金金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 代金券金额
        :type VoucherPayAmount: str
        :param BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        """
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")


class BusinessSummaryTotal(AbstractModel):
    """按产品汇总总费用

    """

    def __init__(self):
        """
        :param RealTotalCost: 总花费
        :type RealTotalCost: str
        :param VoucherPayAmount: 代金券金额
        :type VoucherPayAmount: str
        :param IncentivePayAmount: 赠送金金额
        :type IncentivePayAmount: str
        :param CashPayAmount: 现金金额
        :type CashPayAmount: str
        """
        self.RealTotalCost = None
        self.VoucherPayAmount = None
        self.IncentivePayAmount = None
        self.CashPayAmount = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.CashPayAmount = params.get("CashPayAmount")


class ConditionBusiness(AbstractModel):
    """产品过滤条件

    """

    def __init__(self):
        """
        :param BusinessCode: 产品码
        :type BusinessCode: str
        :param BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        """
        self.BusinessCode = None
        self.BusinessCodeName = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")


class ConditionPayMode(AbstractModel):
    """付费模式过滤条件

    """

    def __init__(self):
        """
        :param PayMode: 付费模式
        :type PayMode: str
        :param PayModeName: 付费模式名称
        :type PayModeName: str
        """
        self.PayMode = None
        self.PayModeName = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.PayModeName = params.get("PayModeName")


class ConditionProject(AbstractModel):
    """项目过滤条件

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        """
        self.ProjectId = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")


class ConditionRegion(AbstractModel):
    """地域过滤条件

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
        :type RegionId: str
        :param RegionName: 地域名称
        :type RegionName: str
        """
        self.RegionId = None
        self.RegionName = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")


class Conditions(AbstractModel):
    """账单筛选条件对象

    """

    def __init__(self):
        """
        :param TimeRange: 只支持6和12两个值
        :type TimeRange: int
        :param BusinessCode: 产品编码
        :type BusinessCode: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param RegionId: 地域ID
        :type RegionId: int
        :param PayMode: 付费模式，可选prePay和postPay
        :type PayMode: str
        :param ResourceKeyword: 资源关键字
        :type ResourceKeyword: str
        :param BusinessCodes: 产品编码
        :type BusinessCodes: list of str
        :param ProductCodes: 子产品编码
        :type ProductCodes: list of str
        :param RegionIds: 地域ID
        :type RegionIds: list of int
        :param ProjectIds: 项目ID
        :type ProjectIds: list of int
        :param PayModes: 付费模式，可选prePay和postPay
        :type PayModes: list of str
        :param ActionTypes: 交易类型
        :type ActionTypes: list of str
        :param HideFreeCost: 是否隐藏0元流水
        :type HideFreeCost: int
        :param OrderByCost: 排序规则，可选desc和asc
        :type OrderByCost: str
        :param BillIds: 交易ID
        :type BillIds: list of str
        :param ComponentCodes: 组件编码
        :type ComponentCodes: list of str
        :param FileIds: 文件ID
        :type FileIds: list of str
        :param FileTypes: 文件类型
        :type FileTypes: list of str
        :param Status: 状态
        :type Status: list of int non-negative
        """
        self.TimeRange = None
        self.BusinessCode = None
        self.ProjectId = None
        self.RegionId = None
        self.PayMode = None
        self.ResourceKeyword = None
        self.BusinessCodes = None
        self.ProductCodes = None
        self.RegionIds = None
        self.ProjectIds = None
        self.PayModes = None
        self.ActionTypes = None
        self.HideFreeCost = None
        self.OrderByCost = None
        self.BillIds = None
        self.ComponentCodes = None
        self.FileIds = None
        self.FileTypes = None
        self.Status = None


    def _deserialize(self, params):
        self.TimeRange = params.get("TimeRange")
        self.BusinessCode = params.get("BusinessCode")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.PayMode = params.get("PayMode")
        self.ResourceKeyword = params.get("ResourceKeyword")
        self.BusinessCodes = params.get("BusinessCodes")
        self.ProductCodes = params.get("ProductCodes")
        self.RegionIds = params.get("RegionIds")
        self.ProjectIds = params.get("ProjectIds")
        self.PayModes = params.get("PayModes")
        self.ActionTypes = params.get("ActionTypes")
        self.HideFreeCost = params.get("HideFreeCost")
        self.OrderByCost = params.get("OrderByCost")
        self.BillIds = params.get("BillIds")
        self.ComponentCodes = params.get("ComponentCodes")
        self.FileIds = params.get("FileIds")
        self.FileTypes = params.get("FileTypes")
        self.Status = params.get("Status")


class ConsumptionBusinessSummaryDataItem(AbstractModel):
    """消耗按产品汇总详情

    """

    def __init__(self):
        """
        :param BusinessCode: 产品码
        :type BusinessCode: str
        :param BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        :param RealTotalCost: 折后总价
        :type RealTotalCost: str
        :param Trend: 费用趋势
        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        """
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.RealTotalCost = None
        self.Trend = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self.Trend = ConsumptionSummaryTrend()
            self.Trend._deserialize(params.get("Trend"))


class ConsumptionProjectSummaryDataItem(AbstractModel):
    """消耗按项目汇总详情

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param RealTotalCost: 折后总价
        :type RealTotalCost: str
        :param Trend: 趋势
        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        :param Business: 产品消耗详情
        :type Business: list of ConsumptionBusinessSummaryDataItem
        """
        self.ProjectId = None
        self.ProjectName = None
        self.RealTotalCost = None
        self.Trend = None
        self.Business = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self.Trend = ConsumptionSummaryTrend()
            self.Trend._deserialize(params.get("Trend"))
        if params.get("Business") is not None:
            self.Business = []
            for item in params.get("Business"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self.Business.append(obj)


class ConsumptionRegionSummaryDataItem(AbstractModel):
    """消耗按地域汇总详情

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
        :type RegionId: str
        :param RegionName: 地域名称
        :type RegionName: str
        :param RealTotalCost: 折后总价
        :type RealTotalCost: str
        :param Trend: 趋势
        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        :param Business: 产品消费详情
        :type Business: list of ConsumptionBusinessSummaryDataItem
        """
        self.RegionId = None
        self.RegionName = None
        self.RealTotalCost = None
        self.Trend = None
        self.Business = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self.Trend = ConsumptionSummaryTrend()
            self.Trend._deserialize(params.get("Trend"))
        if params.get("Business") is not None:
            self.Business = []
            for item in params.get("Business"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self.Business.append(obj)


class ConsumptionResourceSummaryConditionValue(AbstractModel):
    """消耗按资源汇总过滤条件

    """

    def __init__(self):
        """
        :param Business: 产品列表
        :type Business: list of ConditionBusiness
        :param Project: 项目列表
        :type Project: list of ConditionProject
        :param Region: 地域列表
        :type Region: list of ConditionRegion
        :param PayMode: 付费模式列表
        :type PayMode: list of ConditionPayMode
        """
        self.Business = None
        self.Project = None
        self.Region = None
        self.PayMode = None


    def _deserialize(self, params):
        if params.get("Business") is not None:
            self.Business = []
            for item in params.get("Business"):
                obj = ConditionBusiness()
                obj._deserialize(item)
                self.Business.append(obj)
        if params.get("Project") is not None:
            self.Project = []
            for item in params.get("Project"):
                obj = ConditionProject()
                obj._deserialize(item)
                self.Project.append(obj)
        if params.get("Region") is not None:
            self.Region = []
            for item in params.get("Region"):
                obj = ConditionRegion()
                obj._deserialize(item)
                self.Region.append(obj)
        if params.get("PayMode") is not None:
            self.PayMode = []
            for item in params.get("PayMode"):
                obj = ConditionPayMode()
                obj._deserialize(item)
                self.PayMode.append(obj)


class ConsumptionResourceSummaryDataItem(AbstractModel):
    """消耗按资源汇总详情

    """

    def __init__(self):
        """
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param ResourceName: 资源名称
        :type ResourceName: str
        :param RealTotalCost: 折后总价
        :type RealTotalCost: str
        :param CashPayAmount: 现金花费
        :type CashPayAmount: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param RegionId: 地域ID
        :type RegionId: str
        :param RegionName: 地域名称
        :type RegionName: str
        :param PayMode: 付费模式
        :type PayMode: str
        :param PayModeName: 付费模式名称
        :type PayModeName: str
        :param BusinessCode: 产品码
        :type BusinessCode: str
        :param BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        :param ConsumptionTypeName: 消耗类型
        :type ConsumptionTypeName: str
        """
        self.ResourceId = None
        self.ResourceName = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.ProjectId = None
        self.ProjectName = None
        self.RegionId = None
        self.RegionName = None
        self.PayMode = None
        self.PayModeName = None
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.ConsumptionTypeName = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.PayMode = params.get("PayMode")
        self.PayModeName = params.get("PayModeName")
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.ConsumptionTypeName = params.get("ConsumptionTypeName")


class ConsumptionSummaryTotal(AbstractModel):
    """消耗汇总详情

    """

    def __init__(self):
        """
        :param RealTotalCost: 折后总价
        :type RealTotalCost: str
        """
        self.RealTotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")


class ConsumptionSummaryTrend(AbstractModel):
    """消耗费用趋势

    """

    def __init__(self):
        """
        :param Type: 趋势类型，upward上升/downward下降/none无
        :type Type: str
        :param Value: 趋势值，Type为none是该字段值为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")


class CostComponentSet(AbstractModel):
    """消耗组件明细

    """

    def __init__(self):
        """
        :param ComponentCodeName: 组件类型名称
        :type ComponentCodeName: str
        :param ItemCodeName: 组件名称
        :type ItemCodeName: str
        :param SinglePrice: 刊例价
        :type SinglePrice: str
        :param PriceUnit: 刊例价单位
        :type PriceUnit: str
        :param UsedAmount: 用量
        :type UsedAmount: str
        :param UsedAmountUnit: 用量单位
        :type UsedAmountUnit: str
        :param Cost: 原价
        :type Cost: str
        :param Discount: 折扣
        :type Discount: str
        :param RealCost: 折后价
        :type RealCost: str
        :param VoucherPayAmount: 代金券支付金额
        :type VoucherPayAmount: str
        :param CashPayAmount: 现金支付金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送金支付金额
        :type IncentivePayAmount: str
        """
        self.ComponentCodeName = None
        self.ItemCodeName = None
        self.SinglePrice = None
        self.PriceUnit = None
        self.UsedAmount = None
        self.UsedAmountUnit = None
        self.Cost = None
        self.Discount = None
        self.RealCost = None
        self.VoucherPayAmount = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None


    def _deserialize(self, params):
        self.ComponentCodeName = params.get("ComponentCodeName")
        self.ItemCodeName = params.get("ItemCodeName")
        self.SinglePrice = params.get("SinglePrice")
        self.PriceUnit = params.get("PriceUnit")
        self.UsedAmount = params.get("UsedAmount")
        self.UsedAmountUnit = params.get("UsedAmountUnit")
        self.Cost = params.get("Cost")
        self.Discount = params.get("Discount")
        self.RealCost = params.get("RealCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")


class CostDetail(AbstractModel):
    """消耗明细数据类型

    """

    def __init__(self):
        """
        :param PayerUin: 支付者uin
        :type PayerUin: str
        :param BusinessCodeName: 业务名称
        :type BusinessCodeName: str
        :param ProductCodeName: 产品名称
        :type ProductCodeName: str
        :param PayModeName: 计费模式名称
        :type PayModeName: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param RegionName: 区域名称
        :type RegionName: str
        :param ZoneName: 地区名称
        :type ZoneName: str
        :param ResourceId: 资源id
        :type ResourceId: str
        :param ResourceName: 资源名称
        :type ResourceName: str
        :param ActionTypeName: 类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionTypeName: str
        :param OrderId: 订单id
        :type OrderId: str
        :param BillId: 交易id
        :type BillId: str
        :param FeeBeginTime: 费用开始时间
        :type FeeBeginTime: str
        :param FeeEndTime: 费用结束时间
        :type FeeEndTime: str
        :param ComponentSet: 组件明细
        :type ComponentSet: list of CostComponentSet
        :param ProductCode: 产品代码
        :type ProductCode: str
        """
        self.PayerUin = None
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
        self.FeeBeginTime = None
        self.FeeEndTime = None
        self.ComponentSet = None
        self.ProductCode = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
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
        self.FeeBeginTime = params.get("FeeBeginTime")
        self.FeeEndTime = params.get("FeeEndTime")
        if params.get("ComponentSet") is not None:
            self.ComponentSet = []
            for item in params.get("ComponentSet"):
                obj = CostComponentSet()
                obj._deserialize(item)
                self.ComponentSet.append(obj)
        self.ProductCode = params.get("ProductCode")


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
        :param ProductCode: 产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param SubProductCode: 子产品编码
        :type SubProductCode: str
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
        self.ProductCode = None
        self.SubProductCode = None


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
        self.ProductCode = params.get("ProductCode")
        self.SubProductCode = params.get("SubProductCode")


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
        :param PeriodType: 周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :type PeriodType: str
        :param Month: 月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。
        :type Month: str
        :param BeginTime: 周期开始时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。(不支持跨月查询)
        :type BeginTime: str
        :param EndTime: 周期结束时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。（不支持跨月查询）
        :type EndTime: str
        :param NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param ProductCode: 查询指定产品信息
        :type ProductCode: str
        :param PayMode: 付费模式 prePay/postPay
        :type PayMode: str
        :param ResourceId: 查询指定资源信息
        :type ResourceId: str
        :param ActionType: 查询交易类型。如 按量计费日结，按量计费小时结 等
        :type ActionType: str
        """
        self.Offset = None
        self.Limit = None
        self.PeriodType = None
        self.Month = None
        self.BeginTime = None
        self.EndTime = None
        self.NeedRecordNum = None
        self.ProductCode = None
        self.PayMode = None
        self.ResourceId = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PeriodType = params.get("PeriodType")
        self.Month = params.get("Month")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.ProductCode = params.get("ProductCode")
        self.PayMode = params.get("PayMode")
        self.ResourceId = params.get("ResourceId")
        self.ActionType = params.get("ActionType")


class DescribeBillDetailResponse(AbstractModel):
    """DescribeBillDetail返回参数结构体

    """

    def __init__(self):
        """
        :param DetailSet: 详情列表
        :type DetailSet: list of BillDetail
        :param Total: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DetailSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = BillDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeBillListRequest(AbstractModel):
    """DescribeBillList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询范围的起始时间（包含）
        :type StartTime: str
        :param EndTime: 查询范围的结束时间（包含）
        :type EndTime: str
        :param Offset: 翻页偏移量，初始值为0
        :type Offset: int
        :param Limit: 每页的限制数量
        :type Limit: int
        :param PayType: 交易类型： all所有交易类型，recharge充值，return退款，unblock解冻，agentin资金转入，advanced垫付，cash提现，deduct扣费，block冻结，agentout资金转出，repay垫付回款，repayment还款(仅国际信用账户)，adj_refund调增(仅国际信用账户)，adj_deduct调减(仅国际信用账户)
        :type PayType: list of str
        :param SubPayType: 扣费模式，当所选的交易类型中包含扣费deduct时有意义： all所有扣费类型，trade预付费支付，hour_h按量小时结，hour_d按量日结，hour_m按量月结，decompensate调账扣费，other其他扣费
        :type SubPayType: list of str
        :param WithZeroAmount: 是否返回0元交易金额的交易项，取值：0-不返回，1-返回。不传该参数则不返回
        :type WithZeroAmount: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.PayType = None
        self.SubPayType = None
        self.WithZeroAmount = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PayType = params.get("PayType")
        self.SubPayType = params.get("SubPayType")
        self.WithZeroAmount = params.get("WithZeroAmount")


class DescribeBillListResponse(AbstractModel):
    """DescribeBillList返回参数结构体

    """

    def __init__(self):
        """
        :param TransactionList: 收支明细列表
        :type TransactionList: list of BillTransactionInfo
        :param Total: 总条数
        :type Total: int
        :param ReturnAmount: 退费总额，单位（分）
        :type ReturnAmount: float
        :param RechargeAmount: 充值总额，单位（分）
        :type RechargeAmount: float
        :param BlockAmount: 冻结总额，单位（分）
        :type BlockAmount: float
        :param UnblockAmount: 解冻总额，单位（分）
        :type UnblockAmount: float
        :param DeductAmount: 扣费总额，单位（分）
        :type DeductAmount: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TransactionList = None
        self.Total = None
        self.ReturnAmount = None
        self.RechargeAmount = None
        self.BlockAmount = None
        self.UnblockAmount = None
        self.DeductAmount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TransactionList") is not None:
            self.TransactionList = []
            for item in params.get("TransactionList"):
                obj = BillTransactionInfo()
                obj._deserialize(item)
                self.TransactionList.append(obj)
        self.Total = params.get("Total")
        self.ReturnAmount = params.get("ReturnAmount")
        self.RechargeAmount = params.get("RechargeAmount")
        self.BlockAmount = params.get("BlockAmount")
        self.UnblockAmount = params.get("UnblockAmount")
        self.DeductAmount = params.get("DeductAmount")
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
        :param PeriodType: 周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :type PeriodType: str
        :param Month: 月份，格式为yyyy-mm。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。
        :type Month: str
        :param NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param ActionType: 查询交易类型。如 按量计费日结，按量计费小时结 等
        :type ActionType: str
        """
        self.Offset = None
        self.Limit = None
        self.PeriodType = None
        self.Month = None
        self.NeedRecordNum = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PeriodType = params.get("PeriodType")
        self.Month = params.get("Month")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.ActionType = params.get("ActionType")


class DescribeBillResourceSummaryResponse(AbstractModel):
    """DescribeBillResourceSummary返回参数结构体

    """

    def __init__(self):
        """
        :param ResourceSummarySet: 资源汇总列表
        :type ResourceSummarySet: list of BillResourceSummary
        :param Total: 资源汇总列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResourceSummarySet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceSummarySet") is not None:
            self.ResourceSummarySet = []
            for item in params.get("ResourceSummarySet"):
                obj = BillResourceSummary()
                obj._deserialize(item)
                self.ResourceSummarySet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByPayModeRequest(AbstractModel):
    """DescribeBillSummaryByPayMode请求参数结构体

    """

    def __init__(self):
        """
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param BeginTime: 目前只支持传当月开始，且必须和EndTime为相同月份，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支持传当月结束，且必须和BeginTime为相同月份，例 2018-09-30 23:59:59
        :type EndTime: str
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")


class DescribeBillSummaryByPayModeResponse(AbstractModel):
    """DescribeBillSummaryByPayMode返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param SummaryOverview: 各付费模式花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of PayModeSummaryOverviewItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = PayModeSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByProductRequest(AbstractModel):
    """DescribeBillSummaryByProduct请求参数结构体

    """

    def __init__(self):
        """
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param BeginTime: 目前只支持传当月开始，且必须和EndTime为相同月份，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支持传当月结束，且必须和BeginTime为相同月份，例 2018-09-30 23:59:59
        :type EndTime: str
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")


class DescribeBillSummaryByProductResponse(AbstractModel):
    """DescribeBillSummaryByProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param SummaryTotal: 总花费详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryTotal: :class:`tencentcloud.billing.v20180709.models.BusinessSummaryTotal`
        :param SummaryOverview: 各产品花费分布
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of BusinessSummaryOverviewItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryTotal = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryTotal") is not None:
            self.SummaryTotal = BusinessSummaryTotal()
            self.SummaryTotal._deserialize(params.get("SummaryTotal"))
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = BusinessSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByProjectRequest(AbstractModel):
    """DescribeBillSummaryByProject请求参数结构体

    """

    def __init__(self):
        """
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param BeginTime: 目前只支持传当月开始，且必须和EndTime为相同月份，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支持传当月结束，且必须和BeginTime为相同月份，例 2018-09-30 23:59:59
        :type EndTime: str
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")


class DescribeBillSummaryByProjectResponse(AbstractModel):
    """DescribeBillSummaryByProject返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param SummaryOverview: 各项目花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of ProjectSummaryOverviewItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = ProjectSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByRegionRequest(AbstractModel):
    """DescribeBillSummaryByRegion请求参数结构体

    """

    def __init__(self):
        """
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param BeginTime: 目前只支持传当月开始，且必须和EndTime为相同月份，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支持传当月结束，且必须和BeginTime为相同月份，例 2018-09-30 23:59:59
        :type EndTime: str
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")


class DescribeBillSummaryByRegionResponse(AbstractModel):
    """DescribeBillSummaryByRegion返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param SummaryOverview: 各地域花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of RegionSummaryOverviewItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = RegionSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByTagRequest(AbstractModel):
    """DescribeBillSummaryByTag请求参数结构体

    """

    def __init__(self):
        """
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param BeginTime: 目前只支持传当月开始，且必须和EndTime为相同月份，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支持传当月结束，且必须和BeginTime为相同月份，例 2018-09-30 23:59:59
        :type EndTime: str
        :param TagKey: 分账标签键
        :type TagKey: str
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None
        self.TagKey = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TagKey = params.get("TagKey")


class DescribeBillSummaryByTagResponse(AbstractModel):
    """DescribeBillSummaryByTag返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param SummaryOverview: 各标签值花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of TagSummaryOverviewItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = TagSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCostDetailRequest(AbstractModel):
    """DescribeCostDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 数量，最大值为100
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param BeginTime: 周期开始时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通成本分析的月份，最多可拉取24个月内的数据。
        :type BeginTime: str
        :param EndTime: 周期结束时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通成本分析的月份，最多可拉取24个月内的数据。
        :type EndTime: str
        :param NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param Month: 月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通成本分析的月份，最多可拉取24个月内的数据。
        :type Month: str
        :param ProductCode: 查询指定产品信息
        :type ProductCode: str
        :param PayMode: 付费模式 prePay/postPay
        :type PayMode: str
        :param ResourceId: 查询指定资源信息
        :type ResourceId: str
        """
        self.Limit = None
        self.Offset = None
        self.BeginTime = None
        self.EndTime = None
        self.NeedRecordNum = None
        self.Month = None
        self.ProductCode = None
        self.PayMode = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.Month = params.get("Month")
        self.ProductCode = params.get("ProductCode")
        self.PayMode = params.get("PayMode")
        self.ResourceId = params.get("ResourceId")


class DescribeCostDetailResponse(AbstractModel):
    """DescribeCostDetail返回参数结构体

    """

    def __init__(self):
        """
        :param DetailSet: 消耗明细
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailSet: list of CostDetail
        :param Total: 记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DetailSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = CostDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeCostSummaryByProductRequest(AbstractModel):
    """DescribeCostSummaryByProduct请求参数结构体

    """

    def __init__(self):
        """
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param BeginTime: 目前只支持传当月1号 00:00:00，且必须和EndTime为相同月份，不支持跨月查询，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支持传当月最后一天 23:59:59，且必须和BeginTime为相同月份，不支持跨月查询，例 2018-09-30 23:59:59
        :type EndTime: str
        :param Limit: 每次获取数据量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.NeedRecordNum = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NeedRecordNum = params.get("NeedRecordNum")


class DescribeCostSummaryByProductResponse(AbstractModel):
    """DescribeCostSummaryByProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param Total: 消耗详情
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param Data: 消耗按产品汇总详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ConsumptionBusinessSummaryDataItem
        :param RecordNum: 记录数量，NeedRecordNum为0是返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.Total = None
        self.Data = None
        self.RecordNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("Total") is not None:
            self.Total = ConsumptionSummaryTotal()
            self.Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RecordNum = params.get("RecordNum")
        self.RequestId = params.get("RequestId")


class DescribeCostSummaryByProjectRequest(AbstractModel):
    """DescribeCostSummaryByProject请求参数结构体

    """

    def __init__(self):
        """
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param BeginTime: 目前只支持传当月1号 00:00:00，且必须和EndTime为相同月份，不支持跨月查询，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支持传当月最后一天 23:59:59，且必须和BeginTime为相同月份，不支持跨月查询，例 2018-09-30 23:59:59
        :type EndTime: str
        :param Limit: 每次获取数据量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.NeedRecordNum = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NeedRecordNum = params.get("NeedRecordNum")


class DescribeCostSummaryByProjectResponse(AbstractModel):
    """DescribeCostSummaryByProject返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param Total: 消耗详情
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param Data: 消耗按业务汇总详情
        :type Data: list of ConsumptionProjectSummaryDataItem
        :param RecordNum: 记录数量，NeedRecordNum为0是返回null
        :type RecordNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.Total = None
        self.Data = None
        self.RecordNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("Total") is not None:
            self.Total = ConsumptionSummaryTotal()
            self.Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ConsumptionProjectSummaryDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RecordNum = params.get("RecordNum")
        self.RequestId = params.get("RequestId")


class DescribeCostSummaryByRegionRequest(AbstractModel):
    """DescribeCostSummaryByRegion请求参数结构体

    """

    def __init__(self):
        """
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param BeginTime: 目前只支持传当月1号 00:00:00，且必须和EndTime为相同月份，不支持跨月查询，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支持传当月最后一天 23:59:59，且必须和BeginTime为相同月份，不支持跨月查询，例 2018-09-30 23:59:59
        :type EndTime: str
        :param Limit: 每次获取数据量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.NeedRecordNum = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NeedRecordNum = params.get("NeedRecordNum")


class DescribeCostSummaryByRegionResponse(AbstractModel):
    """DescribeCostSummaryByRegion返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param Total: 消耗详情
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param Data: 消耗按地域汇总详情
        :type Data: list of ConsumptionRegionSummaryDataItem
        :param RecordNum: 记录数量，NeedRecordNum为0是返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.Total = None
        self.Data = None
        self.RecordNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("Total") is not None:
            self.Total = ConsumptionSummaryTotal()
            self.Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ConsumptionRegionSummaryDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RecordNum = params.get("RecordNum")
        self.RequestId = params.get("RequestId")


class DescribeCostSummaryByResourceRequest(AbstractModel):
    """DescribeCostSummaryByResource请求参数结构体

    """

    def __init__(self):
        """
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param BeginTime: 目前只支持传当月1号 00:00:00，且必须和EndTime为相同月份，不支持跨月查询，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支持传当月最后一天 23:59:59，且必须和BeginTime为相同月份，不支持跨月查询，例 2018-09-30 23:59:59
        :type EndTime: str
        :param Limit: 每次获取数据量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        :param NeedConditionValue: 是否需要返回过滤条件，0不需要，1需要，默认不需要
        :type NeedConditionValue: int
        :param Conditions: 过滤条件，只支持ResourceKeyword(资源关键字，支持资源id及资源名称模糊查询)，ProjectIds（项目id），RegionIds(地域id)，PayModes(付费模式，可选prePay和postPay)，HideFreeCost（是否隐藏0元流水，可选0和1），OrderByCost（按费用排序规则，可选desc和asc）
        :type Conditions: :class:`tencentcloud.billing.v20180709.models.Conditions`
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.NeedRecordNum = None
        self.NeedConditionValue = None
        self.Conditions = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.NeedConditionValue = params.get("NeedConditionValue")
        if params.get("Conditions") is not None:
            self.Conditions = Conditions()
            self.Conditions._deserialize(params.get("Conditions"))


class DescribeCostSummaryByResourceResponse(AbstractModel):
    """DescribeCostSummaryByResource返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param Total: 消耗详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param ConditionValue: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionValue: :class:`tencentcloud.billing.v20180709.models.ConsumptionResourceSummaryConditionValue`
        :param RecordNum: 记录数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordNum: int
        :param Data: 资源消耗详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ConsumptionResourceSummaryDataItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.Total = None
        self.ConditionValue = None
        self.RecordNum = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("Total") is not None:
            self.Total = ConsumptionSummaryTotal()
            self.Total._deserialize(params.get("Total"))
        if params.get("ConditionValue") is not None:
            self.ConditionValue = ConsumptionResourceSummaryConditionValue()
            self.ConditionValue._deserialize(params.get("ConditionValue"))
        self.RecordNum = params.get("RecordNum")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ConsumptionResourceSummaryDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
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
        :param EndDate: 查询账单结束日期，如 2019-01-01， 时间跨度不超过7天
        :type EndDate: str
        :param ProductCode: 互动直播：
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

视频直播
10226 视频直播流量(国内)
10227 视频直播带宽(国内)
100763 视频直播流量(海外)
100762 视频直播宽带(海外)
        :type ProductCode: str
        :param Domain: 查询域名 例如 www.qq.com
非CDN业务查询时值为空
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


class PayModeSummaryOverviewItem(AbstractModel):
    """按付费模式汇总消费详情

    """

    def __init__(self):
        """
        :param PayMode: 付费模式
        :type PayMode: str
        :param PayModeName: 付费模式名称
        :type PayModeName: str
        :param RealTotalCost: 实际花费
        :type RealTotalCost: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param Detail: 按交易类型：包年包月新购/续费/升降配/退款、按量计费扣费、调账补偿/扣费等类型汇总消费详情
        :type Detail: list of ActionSummaryOverviewItem
        :param CashPayAmount: 现金金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送金金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 代金券金额
        :type VoucherPayAmount: str
        """
        self.PayMode = None
        self.PayModeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.Detail = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.PayModeName = params.get("PayModeName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = ActionSummaryOverviewItem()
                obj._deserialize(item)
                self.Detail.append(obj)
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")


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


class ProjectSummaryOverviewItem(AbstractModel):
    """按项目汇总消费详情

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param RealTotalCost: 实际花费
        :type RealTotalCost: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param CashPayAmount: 现金金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送金金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 代金券金额
        :type VoucherPayAmount: str
        :param BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")


class RegionSummaryOverviewItem(AbstractModel):
    """按地域汇总消费详情

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        :param RegionName: 地域名称
        :type RegionName: str
        :param RealTotalCost: 实际花费
        :type RealTotalCost: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param CashPayAmount: 现金金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送金金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 代金券金额
        :type VoucherPayAmount: str
        :param BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        """
        self.RegionId = None
        self.RegionName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")


class TagSummaryOverviewItem(AbstractModel):
    """按标签汇总消费详情

    """

    def __init__(self):
        """
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        :param RealTotalCost: 实际花费
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalCost: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalCostRatio: str
        """
        self.TagValue = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None


    def _deserialize(self, params):
        self.TagValue = params.get("TagValue")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")