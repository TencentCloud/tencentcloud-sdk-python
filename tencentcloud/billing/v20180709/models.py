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


class ActionSummaryOverviewItem(AbstractModel):
    """按交易类型汇总消费详情

    """

    def __init__(self):
        """
        :param ActionType: 交易类型：包年包月新购/续费/升降配/退款、按量计费扣费、调账补偿/扣费等类型\n        :type ActionType: str\n        :param ActionTypeName: 交易类型名称\n        :type ActionTypeName: str\n        :param RealTotalCost: 实际花费\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: 费用所占百分比，两位小数\n        :type RealTotalCostRatio: str\n        :param CashPayAmount: 现金金额\n        :type CashPayAmount: str\n        :param IncentivePayAmount: 赠送金金额\n        :type IncentivePayAmount: str\n        :param VoucherPayAmount: 代金券金额\n        :type VoucherPayAmount: str\n        :param BillMonth: 账单月份，格式2019-08\n        :type BillMonth: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetail(AbstractModel):
    """账单明细数据对象

    """

    def __init__(self):
        """
        :param BusinessCodeName: 产品名称：云产品大类，如云服务器CVM、云数据库MySQL\n        :type BusinessCodeName: str\n        :param ProductCodeName: 子产品名称：云产品子类，如云服务器CVM-标准型S1\n        :type ProductCodeName: str\n        :param PayModeName: 计费模式：包年包月和按量计费\n        :type PayModeName: str\n        :param ProjectName: 项目:资源所属项目\n        :type ProjectName: str\n        :param RegionName: 区域：资源所属地域，如华南地区（广州）\n        :type RegionName: str\n        :param ZoneName: 可用区：资源所属可用区，如广州三区\n        :type ZoneName: str\n        :param ResourceId: 资源实例ID\n        :type ResourceId: str\n        :param ResourceName: 实例名称\n        :type ResourceName: str\n        :param ActionTypeName: 交易类型\n        :type ActionTypeName: str\n        :param OrderId: 订单ID\n        :type OrderId: str\n        :param BillId: 交易ID\n        :type BillId: str\n        :param PayTime: 扣费时间\n        :type PayTime: str\n        :param FeeBeginTime: 开始使用时间\n        :type FeeBeginTime: str\n        :param FeeEndTime: 结束使用时间\n        :type FeeEndTime: str\n        :param ComponentSet: 组件列表\n        :type ComponentSet: list of BillDetailComponent\n        :param PayerUin: 支付者UIN\n        :type PayerUin: str\n        :param OwnerUin: 使用者UIN\n        :type OwnerUin: str\n        :param OperateUin: 操作者UIN\n        :type OperateUin: str\n        :param Tags: Tag 信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of BillTagInfo\n        :param BusinessCode: 商品名称代码
注意：此字段可能返回 null，表示取不到有效值。\n        :type BusinessCode: str\n        :param ProductCode: 子商品名称代码
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductCode: str\n        :param ActionType: 交易类型代码（未开放的字段）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActionType: str\n        :param RegionId: 区域ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionId: str\n        :param ProjectId: 项目ID:资源所属项目ID\n        :type ProjectId: int\n        """
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
        self.ProjectId = None


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
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetailComponent(AbstractModel):
    """账单明细组件对象

    """

    def __init__(self):
        """
        :param ComponentCodeName: 组件类型:资源组件类型的名称，如内存、硬盘等\n        :type ComponentCodeName: str\n        :param ItemCodeName: 组件名称:资源组件的名称，如云数据库MySQL-内存等\n        :type ItemCodeName: str\n        :param SinglePrice: 组件刊例价:资源组件的原始价格，保持原始粒度\n        :type SinglePrice: str\n        :param SpecifiedPrice: 组件指定价\n        :type SpecifiedPrice: str\n        :param PriceUnit: 价格单位\n        :type PriceUnit: str\n        :param UsedAmount: 组件用量\n        :type UsedAmount: str\n        :param UsedAmountUnit: 组件用量单位\n        :type UsedAmountUnit: str\n        :param TimeSpan: 使用时长\n        :type TimeSpan: str\n        :param TimeUnitName: 时长单位\n        :type TimeUnitName: str\n        :param Cost: 组件原价\n        :type Cost: str\n        :param Discount: 折扣率\n        :type Discount: str\n        :param ReduceType: 优惠类型\n        :type ReduceType: str\n        :param RealCost: 优惠后总价\n        :type RealCost: str\n        :param VoucherPayAmount: 代金券支付金额\n        :type VoucherPayAmount: str\n        :param CashPayAmount: 现金支付金额\n        :type CashPayAmount: str\n        :param IncentivePayAmount: 赠送账户支付金额\n        :type IncentivePayAmount: str\n        :param ItemCode: 组件类型代码
注意：此字段可能返回 null，表示取不到有效值。\n        :type ItemCode: str\n        :param ComponentCode: 组件名称代码
注意：此字段可能返回 null，表示取不到有效值。\n        :type ComponentCode: str\n        :param ContractPrice: 合同价
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContractPrice: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillResourceSummary(AbstractModel):
    """账单资源汇总数据对象

    """

    def __init__(self):
        """
        :param BusinessCodeName: 产品名称：云产品大类，如云服务器CVM、云数据库MySQL\n        :type BusinessCodeName: str\n        :param ProductCodeName: 子产品：云产品子类，如云服务器CVM-标准型S1， 当没有获取到子产品名称时，返回"-"\n        :type ProductCodeName: str\n        :param PayModeName: 计费模式：包年包月和按量计费\n        :type PayModeName: str\n        :param ProjectName: 项目\n        :type ProjectName: str\n        :param RegionName: 地域\n        :type RegionName: str\n        :param ZoneName: 可用区\n        :type ZoneName: str\n        :param ResourceId: 资源实例ID\n        :type ResourceId: str\n        :param ResourceName: 资源实例名称\n        :type ResourceName: str\n        :param ActionTypeName: 交易类型：包年包月新购/续费/升降配/退款、按量计费扣费、调账补偿/扣费等类型\n        :type ActionTypeName: str\n        :param OrderId: 订单ID\n        :type OrderId: str\n        :param PayTime: 扣费时间\n        :type PayTime: str\n        :param FeeBeginTime: 开始使用时间\n        :type FeeBeginTime: str\n        :param FeeEndTime: 结束使用时间\n        :type FeeEndTime: str\n        :param ConfigDesc: 配置描述\n        :type ConfigDesc: str\n        :param ExtendField1: 扩展字段1\n        :type ExtendField1: str\n        :param ExtendField2: 扩展字段2\n        :type ExtendField2: str\n        :param TotalCost: 原价，单位为元\n        :type TotalCost: str\n        :param Discount: 折扣率\n        :type Discount: str\n        :param ReduceType: 优惠类型\n        :type ReduceType: str\n        :param RealTotalCost: 优惠后总价，单位为元\n        :type RealTotalCost: str\n        :param VoucherPayAmount: 代金券支付金额，单位为元\n        :type VoucherPayAmount: str\n        :param CashPayAmount: 现金账户支付金额，单位为元\n        :type CashPayAmount: str\n        :param IncentivePayAmount: 赠送账户支付金额，单位为元\n        :type IncentivePayAmount: str\n        :param ExtendField3: 扩展字段3\n        :type ExtendField3: str\n        :param ExtendField4: 扩展字段4\n        :type ExtendField4: str\n        :param ExtendField5: 扩展字段5\n        :type ExtendField5: str\n        :param Tags: Tag 信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of BillTagInfo\n        :param PayerUin: 付款方uin\n        :type PayerUin: str\n        :param OwnerUin: 资源所有者uin,无值则返回"-"\n        :type OwnerUin: str\n        :param OperateUin: 操作者uin,无值则返回"-"\n        :type OperateUin: str\n        :param BusinessCode: 商品名称代码\n        :type BusinessCode: str\n        :param ProductCode: 子商品名称代码\n        :type ProductCode: str\n        :param RegionId: 区域ID\n        :type RegionId: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillTagInfo(AbstractModel):
    """账单 Tag 信息

    """

    def __init__(self):
        """
        :param TagKey: 分账标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        """
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
        


class BillTransactionInfo(AbstractModel):
    """收支明细的流水信息

    """

    def __init__(self):
        """
        :param ActionType: 收支类型：deduct 扣费, recharge 充值, return 退费， block 冻结, unblock 解冻\n        :type ActionType: str\n        :param Amount: 流水金额，单位（分）；正数表示入账，负数表示出账\n        :type Amount: int\n        :param Balance: 可用余额，单位（分）；正数表示入账，负数表示出账\n        :type Balance: int\n        :param BillId: 流水号，如20190131020000236005203583326401\n        :type BillId: str\n        :param OperationInfo: 描述信息\n        :type OperationInfo: str\n        :param OperationTime: 操作时间"2019-01-31 23:35:10.000"\n        :type OperationTime: str\n        :param Cash: 现金账户余额，单位（分）\n        :type Cash: int\n        :param Incentive: 赠送金余额，单位（分）\n        :type Incentive: int\n        :param Freezing: 冻结余额，单位（分）\n        :type Freezing: int\n        :param PayChannel: 交易渠道\n        :type PayChannel: str\n        :param DeductMode: 扣费模式：trade 包年包月(预付费)，hourh  按量-小时结，hourd 按量-日结，hourm 按量-月结，month 按量-月结\n        :type DeductMode: str\n        """
        self.ActionType = None
        self.Amount = None
        self.Balance = None
        self.BillId = None
        self.OperationInfo = None
        self.OperationTime = None
        self.Cash = None
        self.Incentive = None
        self.Freezing = None
        self.PayChannel = None
        self.DeductMode = None


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
        self.PayChannel = params.get("PayChannel")
        self.DeductMode = params.get("DeductMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessSummaryOverviewItem(AbstractModel):
    """按产品汇总产品详情

    """

    def __init__(self):
        """
        :param BusinessCode: 产品码
注意：此字段可能返回 null，表示取不到有效值。\n        :type BusinessCode: str\n        :param BusinessCodeName: 产品名称：云产品大类，如云服务器CVM、云数据库MySQL\n        :type BusinessCodeName: str\n        :param RealTotalCost: 实际花费\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: 费用所占百分比，两位小数\n        :type RealTotalCostRatio: str\n        :param CashPayAmount: 现金金额\n        :type CashPayAmount: str\n        :param IncentivePayAmount: 赠送金金额\n        :type IncentivePayAmount: str\n        :param VoucherPayAmount: 代金券金额\n        :type VoucherPayAmount: str\n        :param BillMonth: 账单月份，格式2019-08\n        :type BillMonth: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessSummaryTotal(AbstractModel):
    """按产品汇总总费用

    """

    def __init__(self):
        """
        :param RealTotalCost: 总花费\n        :type RealTotalCost: str\n        :param VoucherPayAmount: 代金券金额\n        :type VoucherPayAmount: str\n        :param IncentivePayAmount: 赠送金金额\n        :type IncentivePayAmount: str\n        :param CashPayAmount: 现金金额\n        :type CashPayAmount: str\n        """
        self.RealTotalCost = None
        self.VoucherPayAmount = None
        self.IncentivePayAmount = None
        self.CashPayAmount = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionBusiness(AbstractModel):
    """产品过滤条件

    """

    def __init__(self):
        """
        :param BusinessCode: 产品码\n        :type BusinessCode: str\n        :param BusinessCodeName: 产品名称\n        :type BusinessCodeName: str\n        """
        self.BusinessCode = None
        self.BusinessCodeName = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionPayMode(AbstractModel):
    """付费模式过滤条件

    """

    def __init__(self):
        """
        :param PayMode: 付费模式\n        :type PayMode: str\n        :param PayModeName: 付费模式名称\n        :type PayModeName: str\n        """
        self.PayMode = None
        self.PayModeName = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.PayModeName = params.get("PayModeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionProject(AbstractModel):
    """项目过滤条件

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        """
        self.ProjectId = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionRegion(AbstractModel):
    """地域过滤条件

    """

    def __init__(self):
        """
        :param RegionId: 地域ID\n        :type RegionId: str\n        :param RegionName: 地域名称\n        :type RegionName: str\n        """
        self.RegionId = None
        self.RegionName = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Conditions(AbstractModel):
    """账单筛选条件对象

    """

    def __init__(self):
        """
        :param TimeRange: 只支持6和12两个值\n        :type TimeRange: int\n        :param BusinessCode: 产品编码\n        :type BusinessCode: str\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param RegionId: 地域ID\n        :type RegionId: int\n        :param PayMode: 付费模式，可选prePay和postPay\n        :type PayMode: str\n        :param ResourceKeyword: 资源关键字\n        :type ResourceKeyword: str\n        :param BusinessCodes: 产品编码\n        :type BusinessCodes: list of str\n        :param ProductCodes: 子产品编码\n        :type ProductCodes: list of str\n        :param RegionIds: 地域ID\n        :type RegionIds: list of int\n        :param ProjectIds: 项目ID\n        :type ProjectIds: list of int\n        :param PayModes: 付费模式，可选prePay和postPay\n        :type PayModes: list of str\n        :param ActionTypes: 交易类型\n        :type ActionTypes: list of str\n        :param HideFreeCost: 是否隐藏0元流水\n        :type HideFreeCost: int\n        :param OrderByCost: 排序规则，可选desc和asc\n        :type OrderByCost: str\n        :param BillIds: 交易ID\n        :type BillIds: list of str\n        :param ComponentCodes: 组件编码\n        :type ComponentCodes: list of str\n        :param FileIds: 文件ID\n        :type FileIds: list of str\n        :param FileTypes: 文件类型\n        :type FileTypes: list of str\n        :param Status: 状态\n        :type Status: list of int non-negative\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionBusinessSummaryDataItem(AbstractModel):
    """消耗按产品汇总详情

    """

    def __init__(self):
        """
        :param BusinessCode: 产品码\n        :type BusinessCode: str\n        :param BusinessCodeName: 产品名称\n        :type BusinessCodeName: str\n        :param RealTotalCost: 折后总价\n        :type RealTotalCost: str\n        :param Trend: 费用趋势\n        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionProjectSummaryDataItem(AbstractModel):
    """消耗按项目汇总详情

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param RealTotalCost: 折后总价\n        :type RealTotalCost: str\n        :param Trend: 趋势\n        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`\n        :param Business: 产品消耗详情\n        :type Business: list of ConsumptionBusinessSummaryDataItem\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionRegionSummaryDataItem(AbstractModel):
    """消耗按地域汇总详情

    """

    def __init__(self):
        """
        :param RegionId: 地域ID\n        :type RegionId: str\n        :param RegionName: 地域名称\n        :type RegionName: str\n        :param RealTotalCost: 折后总价\n        :type RealTotalCost: str\n        :param Trend: 趋势\n        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`\n        :param Business: 产品消费详情\n        :type Business: list of ConsumptionBusinessSummaryDataItem\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionResourceSummaryConditionValue(AbstractModel):
    """消耗按资源汇总过滤条件

    """

    def __init__(self):
        """
        :param Business: 产品列表\n        :type Business: list of ConditionBusiness\n        :param Project: 项目列表\n        :type Project: list of ConditionProject\n        :param Region: 地域列表\n        :type Region: list of ConditionRegion\n        :param PayMode: 付费模式列表\n        :type PayMode: list of ConditionPayMode\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionResourceSummaryDataItem(AbstractModel):
    """消耗按资源汇总详情

    """

    def __init__(self):
        """
        :param ResourceId: 资源ID\n        :type ResourceId: str\n        :param ResourceName: 资源名称\n        :type ResourceName: str\n        :param RealTotalCost: 折后总价\n        :type RealTotalCost: str\n        :param CashPayAmount: 现金花费\n        :type CashPayAmount: str\n        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param RegionId: 地域ID\n        :type RegionId: str\n        :param RegionName: 地域名称\n        :type RegionName: str\n        :param PayMode: 付费模式\n        :type PayMode: str\n        :param PayModeName: 付费模式名称\n        :type PayModeName: str\n        :param BusinessCode: 产品码\n        :type BusinessCode: str\n        :param BusinessCodeName: 产品名称\n        :type BusinessCodeName: str\n        :param ConsumptionTypeName: 消耗类型\n        :type ConsumptionTypeName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionSummaryTotal(AbstractModel):
    """消耗汇总详情

    """

    def __init__(self):
        """
        :param RealTotalCost: 折后总价\n        :type RealTotalCost: str\n        """
        self.RealTotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionSummaryTrend(AbstractModel):
    """消耗费用趋势

    """

    def __init__(self):
        """
        :param Type: 趋势类型，upward上升/downward下降/none无\n        :type Type: str\n        :param Value: 趋势值，Type为none是该字段值为null
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosDetailSets(AbstractModel):
    """cos产品用量明细返回数据结构

    """

    def __init__(self):
        """
        :param BucketName: 存储桶名称\n        :type BucketName: str\n        :param DosageBeginTime: 用量开始时间\n        :type DosageBeginTime: str\n        :param DosageEndTime: 用量结束时间\n        :type DosageEndTime: str\n        :param SubProductCodeName: 一级产品类型名称\n        :type SubProductCodeName: str\n        :param BillingItemCodeName: 二级产品类型名称\n        :type BillingItemCodeName: str\n        :param DosageValue: 用量\n        :type DosageValue: str\n        :param Unit: 单位\n        :type Unit: str\n        """
        self.BucketName = None
        self.DosageBeginTime = None
        self.DosageEndTime = None
        self.SubProductCodeName = None
        self.BillingItemCodeName = None
        self.DosageValue = None
        self.Unit = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.DosageBeginTime = params.get("DosageBeginTime")
        self.DosageEndTime = params.get("DosageEndTime")
        self.SubProductCodeName = params.get("SubProductCodeName")
        self.BillingItemCodeName = params.get("BillingItemCodeName")
        self.DosageValue = params.get("DosageValue")
        self.Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CostComponentSet(AbstractModel):
    """消耗组件明细

    """

    def __init__(self):
        """
        :param ComponentCodeName: 组件类型名称\n        :type ComponentCodeName: str\n        :param ItemCodeName: 组件名称\n        :type ItemCodeName: str\n        :param SinglePrice: 刊例价\n        :type SinglePrice: str\n        :param PriceUnit: 刊例价单位\n        :type PriceUnit: str\n        :param UsedAmount: 用量\n        :type UsedAmount: str\n        :param UsedAmountUnit: 用量单位\n        :type UsedAmountUnit: str\n        :param Cost: 原价\n        :type Cost: str\n        :param Discount: 折扣\n        :type Discount: str\n        :param RealCost: 折后价\n        :type RealCost: str\n        :param VoucherPayAmount: 代金券支付金额\n        :type VoucherPayAmount: str\n        :param CashPayAmount: 现金支付金额\n        :type CashPayAmount: str\n        :param IncentivePayAmount: 赠送金支付金额\n        :type IncentivePayAmount: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CostDetail(AbstractModel):
    """消耗明细数据类型

    """

    def __init__(self):
        """
        :param PayerUin: 支付者uin\n        :type PayerUin: str\n        :param BusinessCodeName: 业务名称\n        :type BusinessCodeName: str\n        :param ProductCodeName: 产品名称\n        :type ProductCodeName: str\n        :param PayModeName: 计费模式名称\n        :type PayModeName: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param RegionName: 区域名称\n        :type RegionName: str\n        :param ZoneName: 地区名称\n        :type ZoneName: str\n        :param ResourceId: 资源id\n        :type ResourceId: str\n        :param ResourceName: 资源名称\n        :type ResourceName: str\n        :param ActionTypeName: 类型名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActionTypeName: str\n        :param OrderId: 订单id\n        :type OrderId: str\n        :param BillId: 交易id\n        :type BillId: str\n        :param FeeBeginTime: 费用开始时间\n        :type FeeBeginTime: str\n        :param FeeEndTime: 费用结束时间\n        :type FeeEndTime: str\n        :param ComponentSet: 组件明细\n        :type ComponentSet: list of CostComponentSet\n        :param ProductCode: 产品代码\n        :type ProductCode: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Deal(AbstractModel):
    """订单数据对象

    """

    def __init__(self):
        """
        :param OrderId: 订单号\n        :type OrderId: str\n        :param Status: 订单状态\n        :type Status: int\n        :param Payer: 支付者\n        :type Payer: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param Creator: 创建人\n        :type Creator: str\n        :param RealTotalCost: 实际支付金额（分）\n        :type RealTotalCost: int\n        :param VoucherDecline: 代金券抵扣金额（分）\n        :type VoucherDecline: int\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param GoodsCategoryId: 产品分类ID\n        :type GoodsCategoryId: int\n        :param ProductInfo: 产品详情\n        :type ProductInfo: list of ProductInfo\n        :param TimeSpan: 时长\n        :type TimeSpan: float\n        :param TimeUnit: 时间单位\n        :type TimeUnit: str\n        :param Currency: 货币单位\n        :type Currency: str\n        :param Policy: 折扣率\n        :type Policy: float\n        :param Price: 单价（分）\n        :type Price: float\n        :param TotalCost: 原价（分）\n        :type TotalCost: float\n        :param ProductCode: 产品编码
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductCode: str\n        :param SubProductCode: 子产品编码\n        :type SubProductCode: str\n        :param BigDealId: 大订单号\n        :type BigDealId: str\n        :param Formula: 退费公式
注意：此字段可能返回 null，表示取不到有效值。\n        :type Formula: str\n        :param RefReturnDeals: 退费涉及订单信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type RefReturnDeals: str\n        :param PayMode: 付费模式：prePay 预付费 postPay后付费 riPay预留实例\n        :type PayMode: str\n        """
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
        self.BigDealId = None
        self.Formula = None
        self.RefReturnDeals = None
        self.PayMode = None


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
        self.BigDealId = params.get("BigDealId")
        self.Formula = params.get("Formula")
        self.RefReturnDeals = params.get("RefReturnDeals")
        self.PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountBalanceRequest(AbstractModel):
    """DescribeAccountBalance请求参数结构体

    """


class DescribeAccountBalanceResponse(AbstractModel):
    """DescribeAccountBalance返回参数结构体

    """

    def __init__(self):
        """
        :param Balance: 接口做过变更,为兼容老接口,本字段与RealBalance相同,为当前真实可用余额,单位 分\n        :type Balance: int\n        :param Uin: 查询的用户Uin\n        :type Uin: int\n        :param RealBalance: 当前真实可用余额,单位 分\n        :type RealBalance: float\n        :param CashAccountBalance: 现金账户余额,单位 分\n        :type CashAccountBalance: float\n        :param IncomeIntoAccountBalance: 收益转入账户余额,单位 分\n        :type IncomeIntoAccountBalance: float\n        :param PresentAccountBalance: 赠送账户余额,单位 分\n        :type PresentAccountBalance: float\n        :param FreezeAmount: 冻结金额,单位 分\n        :type FreezeAmount: float\n        :param OweAmount: 欠费金额,单位 分\n        :type OweAmount: float\n        :param IsAllowArrears: 是否允许欠费消费\n        :type IsAllowArrears: bool\n        :param IsCreditLimited: 是否限制信用额度\n        :type IsCreditLimited: bool\n        :param CreditAmount: 信用额度\n        :type CreditAmount: float\n        :param CreditBalance: 可用信用额度\n        :type CreditBalance: float\n        :param RealCreditBalance: 真实可用信用额度\n        :type RealCreditBalance: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Balance = None
        self.Uin = None
        self.RealBalance = None
        self.CashAccountBalance = None
        self.IncomeIntoAccountBalance = None
        self.PresentAccountBalance = None
        self.FreezeAmount = None
        self.OweAmount = None
        self.IsAllowArrears = None
        self.IsCreditLimited = None
        self.CreditAmount = None
        self.CreditBalance = None
        self.RealCreditBalance = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Balance = params.get("Balance")
        self.Uin = params.get("Uin")
        self.RealBalance = params.get("RealBalance")
        self.CashAccountBalance = params.get("CashAccountBalance")
        self.IncomeIntoAccountBalance = params.get("IncomeIntoAccountBalance")
        self.PresentAccountBalance = params.get("PresentAccountBalance")
        self.FreezeAmount = params.get("FreezeAmount")
        self.OweAmount = params.get("OweAmount")
        self.IsAllowArrears = params.get("IsAllowArrears")
        self.IsCreditLimited = params.get("IsCreditLimited")
        self.CreditAmount = params.get("CreditAmount")
        self.CreditBalance = params.get("CreditBalance")
        self.RealCreditBalance = params.get("RealCreditBalance")
        self.RequestId = params.get("RequestId")


class DescribeBillDetailRequest(AbstractModel):
    """DescribeBillDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 数量，最大值为100\n        :type Limit: int\n        :param PeriodType: 周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。\n        :type PeriodType: str\n        :param Month: 月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。\n        :type Month: str\n        :param BeginTime: 周期开始时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。(不支持跨月查询)\n        :type BeginTime: str\n        :param EndTime: 周期结束时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。（不支持跨月查询）\n        :type EndTime: str\n        :param NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要\n        :type NeedRecordNum: int\n        :param ProductCode: 查询指定产品信息（暂时未开放获取）\n        :type ProductCode: str\n        :param PayMode: 付费模式 prePay/postPay\n        :type PayMode: str\n        :param ResourceId: 查询指定资源信息\n        :type ResourceId: str\n        :param ActionType: 查询交易类型。如 按量计费日结，按量计费小时结 等\n        :type ActionType: str\n        :param ProjectId: 项目ID:资源所属项目ID\n        :type ProjectId: int\n        """
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
        self.ProjectId = None


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
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillDetailResponse(AbstractModel):
    """DescribeBillDetail返回参数结构体

    """

    def __init__(self):
        """
        :param DetailSet: 详情列表\n        :type DetailSet: list of BillDetail\n        :param Total: 总记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param StartTime: 查询范围的起始时间（包含）\n        :type StartTime: str\n        :param EndTime: 查询范围的结束时间（包含）\n        :type EndTime: str\n        :param Offset: 翻页偏移量，初始值为0\n        :type Offset: int\n        :param Limit: 每页的限制数量\n        :type Limit: int\n        :param PayType: 交易类型： all所有交易类型，recharge充值，return退款，unblock解冻，agentin资金转入，advanced垫付，cash提现，deduct扣费，block冻结，agentout资金转出，repay垫付回款，repayment还款(仅国际信用账户)，adj_refund调增(仅国际信用账户)，adj_deduct调减(仅国际信用账户)\n        :type PayType: list of str\n        :param SubPayType: 扣费模式，
当所选的交易类型为扣费deduct时： 
all所有扣费类型;trade预付费支付;hour_h按量小时结;hour_d按量日结;hour_m按量月结;decompensate调账扣费;other第三方扣费;panshi 线下项目扣费;offline 线下产品扣费;

当所选的交易类型为扣费recharge时： 
online 在线充值;bank-enterprice 银企直连;offline 线下充值;transfer 分成充值

当所选的交易类型为扣费cash时： 
online 线上提现;offline 线下提现;panshi 赠送金清零

当所选的交易类型为扣费advanced时： 
advanced 垫付充值

当所选的交易类型为扣费repay时： 
panshi 垫付回款

当所选的交易类型为扣费block时： 
other 第三方冻结;hour 按量冻结;month按月冻结

当所选的交易类型为扣费return时： 
compensate 调账补偿;trade 预付费退款

当所选的交易类型为扣费unblock时：
other 第三方解冻;hour 按量解冻;month 按月解冻\n        :type SubPayType: list of str\n        :param WithZeroAmount: 是否返回0元交易金额的交易项，取值：0-不返回，1-返回。不传该参数则不返回\n        :type WithZeroAmount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillListResponse(AbstractModel):
    """DescribeBillList返回参数结构体

    """

    def __init__(self):
        """
        :param TransactionList: 收支明细列表\n        :type TransactionList: list of BillTransactionInfo\n        :param Total: 总条数\n        :type Total: int\n        :param ReturnAmount: 退费总额，单位（分）\n        :type ReturnAmount: float\n        :param RechargeAmount: 充值总额，单位（分）\n        :type RechargeAmount: float\n        :param BlockAmount: 冻结总额，单位（分）\n        :type BlockAmount: float\n        :param UnblockAmount: 解冻总额，单位（分）\n        :type UnblockAmount: float\n        :param DeductAmount: 扣费总额，单位（分）\n        :type DeductAmount: float\n        :param AgentInAmount: 资金转入总额，单位（分）\n        :type AgentInAmount: float\n        :param AdvanceRechargeAmount: 垫付充值总额，单位（分）\n        :type AdvanceRechargeAmount: float\n        :param WithdrawAmount: 提现扣减总额，单位（分）\n        :type WithdrawAmount: float\n        :param AgentOutAmount: 资金转出总额，单位（分）\n        :type AgentOutAmount: float\n        :param AdvancePayAmount: 还垫付总额，单位（分）\n        :type AdvancePayAmount: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TransactionList = None
        self.Total = None
        self.ReturnAmount = None
        self.RechargeAmount = None
        self.BlockAmount = None
        self.UnblockAmount = None
        self.DeductAmount = None
        self.AgentInAmount = None
        self.AdvanceRechargeAmount = None
        self.WithdrawAmount = None
        self.AgentOutAmount = None
        self.AdvancePayAmount = None
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
        self.AgentInAmount = params.get("AgentInAmount")
        self.AdvanceRechargeAmount = params.get("AdvanceRechargeAmount")
        self.WithdrawAmount = params.get("WithdrawAmount")
        self.AgentOutAmount = params.get("AgentOutAmount")
        self.AdvancePayAmount = params.get("AdvancePayAmount")
        self.RequestId = params.get("RequestId")


class DescribeBillResourceSummaryRequest(AbstractModel):
    """DescribeBillResourceSummary请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 数量，最大值为1000\n        :type Limit: int\n        :param PeriodType: 周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。\n        :type PeriodType: str\n        :param Month: 月份，格式为yyyy-mm。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。\n        :type Month: str\n        :param NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要\n        :type NeedRecordNum: int\n        :param ActionType: 查询交易类型。如 按量计费日结，按量计费小时结 等\n        :type ActionType: str\n        :param ResourceId: 查询指定资源信息\n        :type ResourceId: str\n        :param PayMode: 付费模式 prePay/postPay\n        :type PayMode: str\n        """
        self.Offset = None
        self.Limit = None
        self.PeriodType = None
        self.Month = None
        self.NeedRecordNum = None
        self.ActionType = None
        self.ResourceId = None
        self.PayMode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PeriodType = params.get("PeriodType")
        self.Month = params.get("Month")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.ActionType = params.get("ActionType")
        self.ResourceId = params.get("ResourceId")
        self.PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillResourceSummaryResponse(AbstractModel):
    """DescribeBillResourceSummary返回参数结构体

    """

    def __init__(self):
        """
        :param ResourceSummarySet: 资源汇总列表\n        :type ResourceSummarySet: list of BillResourceSummary\n        :param Total: 资源汇总列表总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type BeginTime: str\n        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type EndTime: str\n        :param PayerUin: 查询账单数据的用户UIN\n        :type PayerUin: str\n        """
        self.BeginTime = None
        self.EndTime = None
        self.PayerUin = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByPayModeResponse(AbstractModel):
    """DescribeBillSummaryByPayMode返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好\n        :type Ready: int\n        :param SummaryOverview: 各付费模式花费分布详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type SummaryOverview: list of PayModeSummaryOverviewItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type BeginTime: str\n        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type EndTime: str\n        :param PayerUin: 查询账单数据的用户UIN\n        :type PayerUin: str\n        """
        self.BeginTime = None
        self.EndTime = None
        self.PayerUin = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByProductResponse(AbstractModel):
    """DescribeBillSummaryByProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好\n        :type Ready: int\n        :param SummaryTotal: 总花费详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type SummaryTotal: :class:`tencentcloud.billing.v20180709.models.BusinessSummaryTotal`\n        :param SummaryOverview: 各产品花费分布
注意：此字段可能返回 null，表示取不到有效值。\n        :type SummaryOverview: list of BusinessSummaryOverviewItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type BeginTime: str\n        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type EndTime: str\n        :param PayerUin: 查询账单数据的用户UIN\n        :type PayerUin: str\n        """
        self.BeginTime = None
        self.EndTime = None
        self.PayerUin = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByProjectResponse(AbstractModel):
    """DescribeBillSummaryByProject返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好\n        :type Ready: int\n        :param SummaryOverview: 各项目花费分布详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type SummaryOverview: list of ProjectSummaryOverviewItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type BeginTime: str\n        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type EndTime: str\n        :param PayerUin: 查询账单数据的用户UIN\n        :type PayerUin: str\n        """
        self.BeginTime = None
        self.EndTime = None
        self.PayerUin = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByRegionResponse(AbstractModel):
    """DescribeBillSummaryByRegion返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好\n        :type Ready: int\n        :param SummaryOverview: 各地域花费分布详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type SummaryOverview: list of RegionSummaryOverviewItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type BeginTime: str\n        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type EndTime: str\n        :param TagKey: 分账标签键\n        :type TagKey: str\n        :param PayerUin: 查询账单数据的用户UIN\n        :type PayerUin: str\n        """
        self.BeginTime = None
        self.EndTime = None
        self.TagKey = None
        self.PayerUin = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TagKey = params.get("TagKey")
        self.PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByTagResponse(AbstractModel):
    """DescribeBillSummaryByTag返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好\n        :type Ready: int\n        :param SummaryOverview: 各标签值花费分布详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type SummaryOverview: list of TagSummaryOverviewItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Limit: 数量，最大值为100\n        :type Limit: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param BeginTime: 周期开始时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为同一月份，暂不支持跨月拉取。可拉取的数据是开通成本分析后，且距今 24 个月内的数据。\n        :type BeginTime: str\n        :param EndTime: 周期结束时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为同一月份，暂不支持跨月拉取。可拉取的数据是开通成本分析后，且距今 24 个月内的数据。\n        :type EndTime: str\n        :param NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要\n        :type NeedRecordNum: int\n        :param Month: 月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通成本分析的月份，最多可拉取24个月内的数据。\n        :type Month: str\n        :param ProductCode: 查询指定产品信息（暂时未开放获取）\n        :type ProductCode: str\n        :param PayMode: 付费模式 prePay/postPay\n        :type PayMode: str\n        :param ResourceId: 查询指定资源信息\n        :type ResourceId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostDetailResponse(AbstractModel):
    """DescribeCostDetail返回参数结构体

    """

    def __init__(self):
        """
        :param DetailSet: 消耗明细
注意：此字段可能返回 null，表示取不到有效值。\n        :type DetailSet: list of CostDetail\n        :param Total: 记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type BeginTime: str\n        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type EndTime: str\n        :param Limit: 每次获取数据量\n        :type Limit: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param PayerUin: 查询账单数据的用户UIN\n        :type PayerUin: str\n        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要\n        :type NeedRecordNum: int\n        """
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.PayerUin = None
        self.NeedRecordNum = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.PayerUin = params.get("PayerUin")
        self.NeedRecordNum = params.get("NeedRecordNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByProductResponse(AbstractModel):
    """DescribeCostSummaryByProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好\n        :type Ready: int\n        :param Total: 消耗详情\n        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`\n        :param Data: 消耗按产品汇总详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: list of ConsumptionBusinessSummaryDataItem\n        :param RecordNum: 记录数量，NeedRecordNum为0是返回null
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordNum: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type BeginTime: str\n        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type EndTime: str\n        :param Limit: 每次获取数据量\n        :type Limit: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param PayerUin: 查询账单数据的用户UIN\n        :type PayerUin: str\n        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要\n        :type NeedRecordNum: int\n        """
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.PayerUin = None
        self.NeedRecordNum = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.PayerUin = params.get("PayerUin")
        self.NeedRecordNum = params.get("NeedRecordNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByProjectResponse(AbstractModel):
    """DescribeCostSummaryByProject返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好\n        :type Ready: int\n        :param Total: 消耗详情\n        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`\n        :param Data: 消耗按业务汇总详情\n        :type Data: list of ConsumptionProjectSummaryDataItem\n        :param RecordNum: 记录数量，NeedRecordNum为0是返回null\n        :type RecordNum: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type BeginTime: str\n        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type EndTime: str\n        :param Limit: 每次获取数据量\n        :type Limit: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param PayerUin: 查询账单数据的用户UIN\n        :type PayerUin: str\n        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要\n        :type NeedRecordNum: int\n        """
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.PayerUin = None
        self.NeedRecordNum = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.PayerUin = params.get("PayerUin")
        self.NeedRecordNum = params.get("NeedRecordNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByRegionResponse(AbstractModel):
    """DescribeCostSummaryByRegion返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好\n        :type Ready: int\n        :param Total: 消耗详情\n        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`\n        :param Data: 消耗按地域汇总详情\n        :type Data: list of ConsumptionRegionSummaryDataItem\n        :param RecordNum: 记录数量，NeedRecordNum为0是返回null
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordNum: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type BeginTime: str\n        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。\n        :type EndTime: str\n        :param Limit: 每次获取数据量\n        :type Limit: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param PayerUin: 查询账单数据的用户UIN\n        :type PayerUin: str\n        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要\n        :type NeedRecordNum: int\n        :param NeedConditionValue: 是否需要返回过滤条件，0不需要，1需要，默认不需要\n        :type NeedConditionValue: int\n        :param Conditions: 过滤条件，只支持ResourceKeyword(资源关键字，支持资源id及资源名称模糊查询)，ProjectIds（项目id），RegionIds(地域id)，PayModes(付费模式，可选prePay和postPay)，HideFreeCost（是否隐藏0元流水，可选0和1），OrderByCost（按费用排序规则，可选desc和asc）\n        :type Conditions: :class:`tencentcloud.billing.v20180709.models.Conditions`\n        """
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.PayerUin = None
        self.NeedRecordNum = None
        self.NeedConditionValue = None
        self.Conditions = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.PayerUin = params.get("PayerUin")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.NeedConditionValue = params.get("NeedConditionValue")
        if params.get("Conditions") is not None:
            self.Conditions = Conditions()
            self.Conditions._deserialize(params.get("Conditions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByResourceResponse(AbstractModel):
    """DescribeCostSummaryByResource返回参数结构体

    """

    def __init__(self):
        """
        :param Ready: 数据是否准备好，0未准备好，1准备好\n        :type Ready: int\n        :param Total: 消耗详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`\n        :param ConditionValue: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConditionValue: :class:`tencentcloud.billing.v20180709.models.ConsumptionResourceSummaryConditionValue`\n        :param RecordNum: 记录数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordNum: int\n        :param Data: 资源消耗详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: list of ConsumptionResourceSummaryDataItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param StartTime: 开始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Limit: 一页多少条数据，默认是20条，最大不超过1000\n        :type Limit: int\n        :param Offset: 第多少页，从0开始，默认是0\n        :type Offset: int\n        :param Status: 订单状态,默认为4（成功的订单）
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
12：支付中\n        :type Status: int\n        :param OrderId: 订单号\n        :type OrderId: str\n        :param BigDealId: 大订单号\n        :type BigDealId: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.OrderId = None
        self.BigDealId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.OrderId = params.get("OrderId")
        self.BigDealId = params.get("BigDealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDealsByCondResponse(AbstractModel):
    """DescribeDealsByCond返回参数结构体

    """

    def __init__(self):
        """
        :param Deals: 订单列表\n        :type Deals: list of Deal\n        :param TotalCount: 订单总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeDosageCosDetailByDateRequest(AbstractModel):
    """DescribeDosageCosDetailByDate请求参数结构体

    """

    def __init__(self):
        """
        :param StartDate: 查询用量开始时间\n        :type StartDate: str\n        :param EndDate: 查询用量结束时间（与开始时间同月，不支持跨月查询）\n        :type EndDate: str\n        :param BucketName: COS 存储桶名称，可通过Get Service 接口是用来获取请求者名下的所有存储空间列表（Bucket list）https://tcloud-dev.oa.com/document/product/555/30925?!preview&!document=1\n        :type BucketName: str\n        """
        self.StartDate = None
        self.EndDate = None
        self.BucketName = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.BucketName = params.get("BucketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDosageCosDetailByDateResponse(AbstractModel):
    """DescribeDosageCosDetailByDate返回参数结构体

    """

    def __init__(self):
        """
        :param DetailSets: 用量数组\n        :type DetailSets: list of CosDetailSets\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DetailSets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailSets") is not None:
            self.DetailSets = []
            for item in params.get("DetailSets"):
                obj = CosDetailSets()
                obj._deserialize(item)
                self.DetailSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDosageDetailByDateRequest(AbstractModel):
    """DescribeDosageDetailByDate请求参数结构体

    """

    def __init__(self):
        """
        :param StartDate: 查询账单开始日期，如 2019-01-01\n        :type StartDate: str\n        :param EndDate: 查询账单结束日期，如 2019-01-01， 时间跨度不超过7天\n        :type EndDate: str\n        :param ProductCode: 互动直播：
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
100762 视频直播宽带(海外)\n        :type ProductCode: str\n        :param Domain: 查询域名 例如 www.qq.com
非CDN业务查询时值为空\n        :type Domain: str\n        :param InstanceID: 1、如果为空，则返回EIP或CLB所有实例的明细；
2、如果传入实例名，则返回该实例明细\n        :type InstanceID: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDosageDetailByDateResponse(AbstractModel):
    """DescribeDosageDetailByDate返回参数结构体

    """

    def __init__(self):
        """
        :param Unit: 计量单位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Unit: str\n        :param DetailSets: 用量数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type DetailSets: list of DetailSet\n        :param RetCode: 错误码
注意：此字段可能返回 null，表示取不到有效值。\n        :type RetCode: int\n        :param RetMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type RetMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Time: 时间\n        :type Time: str\n        :param Value: 值\n        :type Value: str\n        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetailSet(AbstractModel):
    """由域名和使用明细组成的数据结构

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param DetailPoints: 使用数据明细\n        :type DetailPoints: list of DetailPoint\n        :param InstanceID: 实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceID: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayDealsRequest(AbstractModel):
    """PayDeals请求参数结构体

    """

    def __init__(self):
        """
        :param OrderIds: 需要支付的一个或者多个子订单号，与BigDealIds字段两者必须且仅传一个参数\n        :type OrderIds: list of str\n        :param AutoVoucher: 是否自动使用代金券,1:是,0否,默认0\n        :type AutoVoucher: int\n        :param VoucherIds: 代金券ID列表,目前仅支持指定一张代金券\n        :type VoucherIds: list of str\n        :param BigDealIds: 需要支付的一个或者多个大订单号，与OrderIds字段两者必须且仅传一个参数\n        :type BigDealIds: list of str\n        """
        self.OrderIds = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.BigDealIds = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.BigDealIds = params.get("BigDealIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayDealsResponse(AbstractModel):
    """PayDeals返回参数结构体

    """

    def __init__(self):
        """
        :param OrderIds: 此次操作支付成功的子订单号数组\n        :type OrderIds: list of str\n        :param ResourceIds: 此次操作支付成功的资源Id数组\n        :type ResourceIds: list of str\n        :param BigDealIds: 此次操作支付成功的大订单号数组\n        :type BigDealIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OrderIds = None
        self.ResourceIds = None
        self.BigDealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")
        self.ResourceIds = params.get("ResourceIds")
        self.BigDealIds = params.get("BigDealIds")
        self.RequestId = params.get("RequestId")


class PayModeSummaryOverviewItem(AbstractModel):
    """按付费模式汇总消费详情

    """

    def __init__(self):
        """
        :param PayMode: 付费模式\n        :type PayMode: str\n        :param PayModeName: 付费模式名称\n        :type PayModeName: str\n        :param RealTotalCost: 实际花费\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: 费用所占百分比，两位小数\n        :type RealTotalCostRatio: str\n        :param Detail: 按交易类型：包年包月新购/续费/升降配/退款、按量计费扣费、调账补偿/扣费等类型汇总消费详情\n        :type Detail: list of ActionSummaryOverviewItem\n        :param CashPayAmount: 现金金额\n        :type CashPayAmount: str\n        :param IncentivePayAmount: 赠送金金额\n        :type IncentivePayAmount: str\n        :param VoucherPayAmount: 代金券金额\n        :type VoucherPayAmount: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductInfo(AbstractModel):
    """商品详细信息

    """

    def __init__(self):
        """
        :param Name: 商品详情名称标识\n        :type Name: str\n        :param Value: 商品详情\n        :type Value: str\n        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectSummaryOverviewItem(AbstractModel):
    """按项目汇总消费详情

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param RealTotalCost: 实际花费\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: 费用所占百分比，两位小数\n        :type RealTotalCostRatio: str\n        :param CashPayAmount: 现金金额\n        :type CashPayAmount: str\n        :param IncentivePayAmount: 赠送金金额\n        :type IncentivePayAmount: str\n        :param VoucherPayAmount: 代金券金额\n        :type VoucherPayAmount: str\n        :param BillMonth: 账单月份，格式2019-08\n        :type BillMonth: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionSummaryOverviewItem(AbstractModel):
    """按地域汇总消费详情

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionId: str\n        :param RegionName: 地域名称\n        :type RegionName: str\n        :param RealTotalCost: 实际花费\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: 费用所占百分比，两位小数\n        :type RealTotalCostRatio: str\n        :param CashPayAmount: 现金金额\n        :type CashPayAmount: str\n        :param IncentivePayAmount: 赠送金金额\n        :type IncentivePayAmount: str\n        :param VoucherPayAmount: 代金券金额\n        :type VoucherPayAmount: str\n        :param BillMonth: 账单月份，格式2019-08\n        :type BillMonth: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSummaryOverviewItem(AbstractModel):
    """按标签汇总消费详情

    """

    def __init__(self):
        """
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagValue: str\n        :param RealTotalCost: 实际花费
注意：此字段可能返回 null，表示取不到有效值。\n        :type RealTotalCost: str\n        :param RealTotalCostRatio: 费用所占百分比，两位小数
注意：此字段可能返回 null，表示取不到有效值。\n        :type RealTotalCostRatio: str\n        """
        self.TagValue = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None


    def _deserialize(self, params):
        self.TagValue = params.get("TagValue")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        