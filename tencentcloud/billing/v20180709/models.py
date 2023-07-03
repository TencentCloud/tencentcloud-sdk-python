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
        r"""
        :param ActionType: 交易类型编码
        :type ActionType: str
        :param ActionTypeName: 交易类型：如包年包月新购、包年包月续费、按量计费扣费等类型
        :type ActionTypeName: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        :param BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        :param TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        """
        self.ActionType = None
        self.ActionTypeName = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.BillMonth = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        self.ActionTypeName = params.get("ActionTypeName")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.BillMonth = params.get("BillMonth")
        self.TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicableProducts(AbstractModel):
    """适用商品信息

    """

    def __init__(self):
        r"""
        :param GoodsName: 适用商品名称，值为“全产品通用”或商品名称组成的string，以","分割。
        :type GoodsName: str
        :param PayMode: postPay后付费/prePay预付费/riPay预留实例/空字符串或者"*"表示全部模式。如GoodsName为多个商品名以","分割组成的string，而PayMode为"*"，表示每一件商品的模式都为"*"。
        :type PayMode: str
        """
        self.GoodsName = None
        self.PayMode = None


    def _deserialize(self, params):
        self.GoodsName = params.get("GoodsName")
        self.PayMode = params.get("PayMode")
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
        r"""
        :param BusinessCodeName: 产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :type BusinessCodeName: str
        :param ProductCodeName: 子产品名称：用户采购的具体产品细分类型，例如：云服务器 CVM-标准型 S1
        :type ProductCodeName: str
        :param PayModeName: 计费模式：资源的计费模式，区分为包年包月和按量计费
        :type PayModeName: str
        :param ProjectName: 项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :type ProjectName: str
        :param RegionName: 地域：资源所属地域，如华南地区（广州）
        :type RegionName: str
        :param ZoneName: 可用区：资源所属可用区，如广州三区
        :type ZoneName: str
        :param ResourceId: 资源 ID：账单中出账对象 ID，不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID
        :type ResourceId: str
        :param ResourceName: 资源别名：用户在控制台为资源设置的名称，如果未设置，则默认为空
        :type ResourceName: str
        :param ActionTypeName: 交易类型，如包年包月新购、包年包月续费、按量计费扣费等类型
        :type ActionTypeName: str
        :param OrderId: 订单ID：包年包月计费模式下订购的订单号
        :type OrderId: str
        :param BillId: 交易ID：结算扣费单号
        :type BillId: str
        :param PayTime: 扣费时间：结算扣费时间
        :type PayTime: str
        :param FeeBeginTime: 开始使用时间：产品服务开始使用时间
        :type FeeBeginTime: str
        :param FeeEndTime: 结束使用时间：产品服务结束使用时间
        :type FeeEndTime: str
        :param ComponentSet: 组件列表
        :type ComponentSet: list of BillDetailComponent
        :param PayerUin: 支付者UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :type PayerUin: str
        :param OwnerUin: 使用者UIN：实际使用资源的账号 ID
        :type OwnerUin: str
        :param OperateUin: 操作者UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的 ID 或者角色 ID ）
        :type OperateUin: str
        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of BillTagInfo
        :param BusinessCode: 产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessCode: str
        :param ProductCode: 子产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param ActionType: 交易类型编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionType: str
        :param RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param PriceInfo: 价格属性
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceInfo: list of str
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
        self.ProjectId = None
        self.PriceInfo = None


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
        self.PriceInfo = params.get("PriceInfo")
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
        r"""
        :param ComponentCodeName: 组件类型：用户购买的产品或服务对应的组件大类，例如：云服务器 CVM 的组件：CPU、内存等
        :type ComponentCodeName: str
        :param ItemCodeName: 组件名称：用户购买的产品或服务，所包含的具体组件
        :type ItemCodeName: str
        :param SinglePrice: 组件刊例价：组件的官网原始单价（如果客户享受一口价/合同价则默认不展示）
        :type SinglePrice: str
        :param SpecifiedPrice: 组件指定价（已废弃）
        :type SpecifiedPrice: str
        :param PriceUnit: 组件价格单位：组件价格的单位，单位构成：元/用量单位/时长单位
        :type PriceUnit: str
        :param UsedAmount: 组件用量：该组件实际结算用量，组件用量 = 组件原始用量 - 抵扣用量（含资源包
        :type UsedAmount: str
        :param UsedAmountUnit: 组件用量单位：组件用量对应的单位
        :type UsedAmountUnit: str
        :param RealTotalMeasure: 原始用量/时长：组件被资源包抵扣前的原始用量/时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalMeasure: str
        :param DeductedMeasure: 抵扣用量/时长（含资源包）：组件被资源包抵扣的用量/时长
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductedMeasure: str
        :param TimeSpan: 使用时长：资源使用的时长
        :type TimeSpan: str
        :param TimeUnitName: 时长单位：资源使用时长的单位
        :type TimeUnitName: str
        :param Cost: 组件原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如果客户享受一口价/合同价则默认不展示，退费类场景也默认不展示）
        :type Cost: str
        :param Discount: 折扣率：本资源享受的折扣率（如果客户享受一口价/合同价则默认不展示，退费场景也默认不展示）
        :type Discount: str
        :param ReduceType: 优惠类型
        :type ReduceType: str
        :param RealCost: 优惠后总价：优惠后总价=（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :type RealCost: str
        :param VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        :param ItemCode: 组件类型编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemCode: str
        :param ComponentCode: 组件名称编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentCode: str
        :param ContractPrice: 组件单价：组件的折后单价，组件单价 = 刊例价 * 折扣
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractPrice: str
        :param InstanceType: 实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。正常的实例展示默认为不展示
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param RiTimeSpan: 预留实例抵扣的使用时长：本产品或服务使用预留实例抵扣的使用时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RiTimeSpan: str
        :param OriginalCostWithRI: 预留实例抵扣组件原价：本产品或服务使用预留实例抵扣的组件原价金额
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCostWithRI: str
        :param SPDeductionRate: 节省计划抵扣率：节省计划可用余额额度范围内，节省计划对于此组件打的折扣率
注意：此字段可能返回 null，表示取不到有效值。
        :type SPDeductionRate: str
        :param SPDeduction: 节省计划抵扣金额（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type SPDeduction: str
        :param OriginalCostWithSP: 节省计划抵扣组件原价：节省计划抵扣原价=节省计划包抵扣金额/节省计划抵扣率
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCostWithSP: str
        :param BlendedDiscount: 混合折扣率：综合各类折扣抵扣信息后的最终折扣率，混合折扣率 = 优惠后总价 / 组件原价
注意：此字段可能返回 null，表示取不到有效值。
        :type BlendedDiscount: str
        """
        self.ComponentCodeName = None
        self.ItemCodeName = None
        self.SinglePrice = None
        self.SpecifiedPrice = None
        self.PriceUnit = None
        self.UsedAmount = None
        self.UsedAmountUnit = None
        self.RealTotalMeasure = None
        self.DeductedMeasure = None
        self.TimeSpan = None
        self.TimeUnitName = None
        self.Cost = None
        self.Discount = None
        self.ReduceType = None
        self.RealCost = None
        self.VoucherPayAmount = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.TransferPayAmount = None
        self.ItemCode = None
        self.ComponentCode = None
        self.ContractPrice = None
        self.InstanceType = None
        self.RiTimeSpan = None
        self.OriginalCostWithRI = None
        self.SPDeductionRate = None
        self.SPDeduction = None
        self.OriginalCostWithSP = None
        self.BlendedDiscount = None


    def _deserialize(self, params):
        self.ComponentCodeName = params.get("ComponentCodeName")
        self.ItemCodeName = params.get("ItemCodeName")
        self.SinglePrice = params.get("SinglePrice")
        self.SpecifiedPrice = params.get("SpecifiedPrice")
        self.PriceUnit = params.get("PriceUnit")
        self.UsedAmount = params.get("UsedAmount")
        self.UsedAmountUnit = params.get("UsedAmountUnit")
        self.RealTotalMeasure = params.get("RealTotalMeasure")
        self.DeductedMeasure = params.get("DeductedMeasure")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnitName = params.get("TimeUnitName")
        self.Cost = params.get("Cost")
        self.Discount = params.get("Discount")
        self.ReduceType = params.get("ReduceType")
        self.RealCost = params.get("RealCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.ItemCode = params.get("ItemCode")
        self.ComponentCode = params.get("ComponentCode")
        self.ContractPrice = params.get("ContractPrice")
        self.InstanceType = params.get("InstanceType")
        self.RiTimeSpan = params.get("RiTimeSpan")
        self.OriginalCostWithRI = params.get("OriginalCostWithRI")
        self.SPDeductionRate = params.get("SPDeductionRate")
        self.SPDeduction = params.get("SPDeduction")
        self.OriginalCostWithSP = params.get("OriginalCostWithSP")
        self.BlendedDiscount = params.get("BlendedDiscount")
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
        r"""
        :param BusinessCodeName: 产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :type BusinessCodeName: str
        :param ProductCodeName: 子产品名称：用户采购的具体产品细分类型，例如：云服务器 CVM-标准型 S1
        :type ProductCodeName: str
        :param PayModeName: 计费模式：资源的计费模式，区分为包年包月和按量计费
        :type PayModeName: str
        :param ProjectName: 项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :type ProjectName: str
        :param RegionName: 地域：资源所属地域，如华南地区（广州）
        :type RegionName: str
        :param ZoneName: 可用区：资源所属可用区，如广州三区
        :type ZoneName: str
        :param ResourceId: 资源 ID：账单中出账对象 ID，不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID	
        :type ResourceId: str
        :param ResourceName: 资源别名：用户在控制台为资源设置的名称，如果未设置，则默认为空
        :type ResourceName: str
        :param ActionTypeName: 交易类型：如包年包月新购、包年包月续费、按量计费扣费等类型
        :type ActionTypeName: str
        :param OrderId: 订单ID：包年包月计费模式下订购的订单号
        :type OrderId: str
        :param PayTime: 扣费时间：结算扣费时间
        :type PayTime: str
        :param FeeBeginTime: 开始使用时间：产品服务开始使用时间
        :type FeeBeginTime: str
        :param FeeEndTime: 结束使用时间：产品服务结束使用时间
        :type FeeEndTime: str
        :param ConfigDesc: 配置描述：该资源下的计费项名称和用量合并展示，仅在资源账单体现
        :type ConfigDesc: str
        :param ExtendField1: 扩展字段1：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField1: str
        :param ExtendField2: 扩展字段2：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField2: str
        :param TotalCost: 原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如果客户享受一口价/合同价则默认不展示，退费类场景也默认不展示）
        :type TotalCost: str
        :param Discount: 折扣率：本资源享受的折扣率（如果客户享受一口价/合同价则默认不展示，退费场景也默认不展示）
        :type Discount: str
        :param ReduceType: 优惠类型
        :type ReduceType: str
        :param RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        :param ExtendField3: 扩展字段3：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField3: str
        :param ExtendField4: 扩展字段4：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField4: str
        :param ExtendField5: 扩展字段5：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField5: str
        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of BillTagInfo
        :param PayerUin: 支付者UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :type PayerUin: str
        :param OwnerUin: 使用者UIN：实际使用资源的账号 ID
        :type OwnerUin: str
        :param OperateUin: 操作者UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的 ID 或者角色 ID ）
        :type OperateUin: str
        :param BusinessCode: 产品编码
        :type BusinessCode: str
        :param ProductCode: 子产品编码
        :type ProductCode: str
        :param RegionId: 地域ID
        :type RegionId: int
        :param InstanceType: 实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。正常的实例展示默认为不展示
        :type InstanceType: str
        :param OriginalCostWithRI: 预留实例抵扣组件原价：本产品或服务使用预留实例抵扣的组件原价金额	
        :type OriginalCostWithRI: str
        :param SPDeduction: 节省计划抵扣金额（已废弃）
        :type SPDeduction: str
        :param OriginalCostWithSP: 节省计划抵扣组件原价：节省计划抵扣原价=节省计划包抵扣金额/节省计划抵扣率	
        :type OriginalCostWithSP: str
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
        self.TransferPayAmount = None
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
        self.InstanceType = None
        self.OriginalCostWithRI = None
        self.SPDeduction = None
        self.OriginalCostWithSP = None


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
        self.TransferPayAmount = params.get("TransferPayAmount")
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
        self.InstanceType = params.get("InstanceType")
        self.OriginalCostWithRI = params.get("OriginalCostWithRI")
        self.SPDeduction = params.get("SPDeduction")
        self.OriginalCostWithSP = params.get("OriginalCostWithSP")
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
        r"""
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
        r"""
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
        :param PayChannel: 交易渠道
        :type PayChannel: str
        :param DeductMode: 扣费模式：trade 包年包月(预付费)，hourh  按量-小时结，hourd 按量-日结，hourm 按量-月结，month 按量-月结
        :type DeductMode: str
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
        


class BusinessSummaryInfo(AbstractModel):
    """产品汇总信息

    """

    def __init__(self):
        r"""
        :param BusinessCode: 产品编码
        :type BusinessCode: str
        :param BusinessCodeName: 产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :type BusinessCodeName: str
        :param TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: str
        :param RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        """
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.TotalCost = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
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
        r"""
        :param BusinessCode: 产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessCode: str
        :param BusinessCodeName: 产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :type BusinessCodeName: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        :param TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        """
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.BillMonth = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.BillMonth = params.get("BillMonth")
        self.TotalCost = params.get("TotalCost")
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
        r"""
        :param RealTotalCost: 优惠后总价

        :type RealTotalCost: str
        :param VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        """
        self.RealTotalCost = None
        self.VoucherPayAmount = None
        self.IncentivePayAmount = None
        self.CashPayAmount = None
        self.TransferPayAmount = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.TotalCost = params.get("TotalCost")
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
        r"""
        :param BusinessCode: 产品名称代码
        :type BusinessCode: str
        :param BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param TimeRange: 只支持6和12两个值
        :type TimeRange: int
        :param BusinessCode: 产品名称代码
        :type BusinessCode: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param RegionId: 地域ID
        :type RegionId: int
        :param PayMode: 付费模式，可选prePay和postPay
        :type PayMode: str
        :param ResourceKeyword: 资源关键字
        :type ResourceKeyword: str
        :param BusinessCodes: 产品名称代码
        :type BusinessCodes: list of str
        :param ProductCodes: 子产品名称代码
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
        r"""
        :param BusinessCode: 产品名称代码
        :type BusinessCode: str
        :param BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        :param RealTotalCost: 折后总价
        :type RealTotalCost: str
        :param Trend: 费用趋势
        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        :param CashPayAmount: 现金
注意：此字段可能返回 null，表示取不到有效值。
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送金
注意：此字段可能返回 null，表示取不到有效值。
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 代金券
注意：此字段可能返回 null，表示取不到有效值。
        :type VoucherPayAmount: str
        :param TransferPayAmount: 分成金
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        """
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.RealTotalCost = None
        self.Trend = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self.Trend = ConsumptionSummaryTrend()
            self.Trend._deserialize(params.get("Trend"))
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
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
        r"""
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
        :param CashPayAmount: 现金
注意：此字段可能返回 null，表示取不到有效值。
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送金
注意：此字段可能返回 null，表示取不到有效值。
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 代金券
注意：此字段可能返回 null，表示取不到有效值。
        :type VoucherPayAmount: str
        :param TransferPayAmount: 分成金
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.RealTotalCost = None
        self.Trend = None
        self.Business = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None


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
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
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
        r"""
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
        r"""
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
        r"""
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
        :param BusinessCode: 产品名称代码
        :type BusinessCode: str
        :param BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        :param ConsumptionTypeName: 消耗类型
        :type ConsumptionTypeName: str
        :param RealCost: 折前价
注意：此字段可能返回 null，表示取不到有效值。
        :type RealCost: str
        :param FeeBeginTime: 费用起始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeBeginTime: str
        :param FeeEndTime: 费用结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeEndTime: str
        :param DayDiff: 天数
注意：此字段可能返回 null，表示取不到有效值。
        :type DayDiff: str
        :param DailyTotalCost: 每日消耗
注意：此字段可能返回 null，表示取不到有效值。
        :type DailyTotalCost: str
        :param OrderId: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param VoucherPayAmount: 代金券
注意：此字段可能返回 null，表示取不到有效值。
        :type VoucherPayAmount: str
        :param IncentivePayAmount: 赠送金
注意：此字段可能返回 null，表示取不到有效值。
        :type IncentivePayAmount: str
        :param TransferPayAmount: 分成金
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
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
        self.RealCost = None
        self.FeeBeginTime = None
        self.FeeEndTime = None
        self.DayDiff = None
        self.DailyTotalCost = None
        self.OrderId = None
        self.VoucherPayAmount = None
        self.IncentivePayAmount = None
        self.TransferPayAmount = None


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
        self.RealCost = params.get("RealCost")
        self.FeeBeginTime = params.get("FeeBeginTime")
        self.FeeEndTime = params.get("FeeEndTime")
        self.DayDiff = params.get("DayDiff")
        self.DailyTotalCost = params.get("DailyTotalCost")
        self.OrderId = params.get("OrderId")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
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
        r"""
        :param RealTotalCost: 折后总价
        :type RealTotalCost: str
        """
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
        r"""
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
        r"""
        :param BucketName: 存储桶名称
        :type BucketName: str
        :param DosageBeginTime: 用量开始时间
        :type DosageBeginTime: str
        :param DosageEndTime: 用量结束时间
        :type DosageEndTime: str
        :param SubProductCodeName: 子产品名称
        :type SubProductCodeName: str
        :param BillingItemCodeName: 计费项名称
        :type BillingItemCodeName: str
        :param DosageValue: 用量
        :type DosageValue: str
        :param Unit: 单位
        :type Unit: str
        """
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
        r"""
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
        r"""
        :param PayerUin: 支付者uin
        :type PayerUin: str
        :param BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        :param ProductCodeName: 子产品名称
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
        :param ProductCode: 子产品名称代码
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
        r"""
        :param OrderId: 订单号
        :type OrderId: str
        :param Status: 订单的状态 1：未支付 2：已支付3：发货中 4：已发货 5：发货失败 6：已退款 7：已关单 8：订单过期 9：订单已失效 10：产品已失效 11：代付拒绝 12：支付中
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
        :param BigDealId: 大订单号
        :type BigDealId: str
        :param Formula: 退费公式
注意：此字段可能返回 null，表示取不到有效值。
        :type Formula: str
        :param RefReturnDeals: 退费涉及订单信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RefReturnDeals: str
        :param PayMode: 付费模式：prePay 预付费 postPay后付费 riPay预留实例
        :type PayMode: str
        :param Action: 交易类型
modifyNetworkMode 调整带宽模式
modifyNetworkSize 调整带宽大小
refund 退款
downgrade 降配
upgrade 升配
renew 续费
purchase 购买
preMoveOut 包年包月迁出资源
preMoveIn 包年包月迁入资源
preToPost 预付费转后付费
postMoveOut 按量计费迁出资源
postMoveIn 按量计费迁入资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param ProductName: 产品编码中文名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param SubProductName: 子产品编码中文名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProductName: str
        :param ResourceId: 订单对应的资源id, 查询参数Limit超过200，将返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: list of str
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
        self.BigDealId = None
        self.Formula = None
        self.RefReturnDeals = None
        self.PayMode = None
        self.Action = None
        self.ProductName = None
        self.SubProductName = None
        self.ResourceId = None


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
        self.Action = params.get("Action")
        self.ProductName = params.get("ProductName")
        self.SubProductName = params.get("SubProductName")
        self.ResourceId = params.get("ResourceId")
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
        r"""
        :param Balance: 接口做过变更,为兼容老接口,本字段与RealBalance相同,为当前真实可用余额,单位 分
        :type Balance: int
        :param Uin: 查询的用户Uin
        :type Uin: int
        :param RealBalance: 当前真实可用余额,单位 分
        :type RealBalance: float
        :param CashAccountBalance: 现金账户余额,单位 分
        :type CashAccountBalance: float
        :param IncomeIntoAccountBalance: 收益转入账户余额,单位 分
        :type IncomeIntoAccountBalance: float
        :param PresentAccountBalance: 赠送账户余额,单位 分
        :type PresentAccountBalance: float
        :param FreezeAmount: 冻结金额,单位 分
        :type FreezeAmount: float
        :param OweAmount: 欠费金额,单位 分
        :type OweAmount: float
        :param IsAllowArrears: 是否允许欠费消费
        :type IsAllowArrears: bool
        :param IsCreditLimited: 是否限制信用额度
        :type IsCreditLimited: bool
        :param CreditAmount: 信用额度
        :type CreditAmount: float
        :param CreditBalance: 可用信用额度
        :type CreditBalance: float
        :param RealCreditBalance: 真实可用信用额度
        :type RealCreditBalance: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :type Offset: int
        :param Limit: 数量，最大值为100
        :type Limit: int
        :param PeriodType: 周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :type PeriodType: str
        :param Month: 月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通账单2.0的月份，最多可拉取18个月内的数据。
        :type Month: str
        :param BeginTime: 周期开始时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取18个月内的数据。(不支持跨月查询)
        :type BeginTime: str
        :param EndTime: 周期结束时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取18个月内的数据。（不支持跨月查询）
        :type EndTime: str
        :param NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param ProductCode: 已废弃参数，未开放
        :type ProductCode: str
        :param PayMode: 付费模式 prePay/postPay
        :type PayMode: str
        :param ResourceId: 查询指定资源信息
        :type ResourceId: str
        :param ActionType: 查询交易类型（请使用交易类型名称入参），入参示例枚举如下：
包年包月新购
包年包月续费
包年包月配置变更
包年包月退款 
按量计费扣费 
线下项目扣费 
线下产品扣费 
调账扣费 
调账补偿 
按量计费小时结 
按量计费日结 
按量计费月结 
竞价实例小时结 
线下项目调账补偿 
线下产品调账补偿 
优惠扣费 
优惠补偿 
按量计费迁入资源 
按量计费迁出资源 
包年包月迁入资源 
包年包月迁出资源 
预付费用 
小时费用 
预留实例退款 
按量计费冲正 
包年包月转按量 
保底扣款 
节省计划小时费用
        :type ActionType: str
        :param ProjectId: 项目ID:资源所属项目ID
        :type ProjectId: int
        :param BusinessCode: 产品名称代码
备注：如需获取当月使用过的BusinessCode，请调用API：<a href="https://cloud.tencent.com/document/product/555/35761">获取产品汇总费用分布</a>
        :type BusinessCode: str
        :param Context: 上一次请求返回的上下文信息，翻页查询Month>=2023-05的月份的数据可加快查询速度，数据量10万级别以上的用户建议使用，查询速度可提升2~10倍
        :type Context: str
        :param PayerUin: 支付者的账号 ID（账号 ID 是用户在腾讯云的唯一账号标识），默认查询本账号账单，如集团管理账号需查询成员账号自付的账单，该字段需入参成员账号UIN
        :type PayerUin: str
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
        self.ProjectId = None
        self.BusinessCode = None
        self.Context = None
        self.PayerUin = None


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
        self.BusinessCode = params.get("BusinessCode")
        self.Context = params.get("Context")
        self.PayerUin = params.get("PayerUin")
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
        r"""
        :param DetailSet: 详情列表
        :type DetailSet: list of BillDetail
        :param Total: 总记录数，24小时缓存一次，可能比实际总记录数少
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Context: 本次请求的上下文信息，可用于下一次请求的请求参数中，加快查询速度
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DetailSet = None
        self.Total = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = BillDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)
        self.Total = params.get("Total")
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class DescribeBillListRequest(AbstractModel):
    """DescribeBillList请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 查询范围的起始时间（包含）时间格式 yyyy-MM-dd HH:mm:ss 开始时间和结束时间差值小于等于六个月
        :type StartTime: str
        :param EndTime: 查询范围的结束时间（包含）时间格式 yyyy-MM-dd HH:mm:ss ，开始时间和结束时间差值小于等于六个月
        :type EndTime: str
        :param Offset: 翻页偏移量，初始值为0
        :type Offset: int
        :param Limit: 每页的限制数量
        :type Limit: int
        :param PayType: 交易类型： all所有交易类型，recharge充值，return退款，unblock解冻，agentin资金转入，advanced垫付，cash提现，deduct扣费，block冻结，agentout资金转出，repay垫付回款，repayment还款(仅国际信用账户)，adj_refund调增(仅国际信用账户)，adj_deduct调减(仅国际信用账户)
        :type PayType: list of str
        :param SubPayType: 扣费模式，
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
other 第三方解冻;hour 按量解冻;month 按月解冻
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
        r"""
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
        :param AgentInAmount: 资金转入总额，单位（分）
        :type AgentInAmount: float
        :param AdvanceRechargeAmount: 垫付充值总额，单位（分）
        :type AdvanceRechargeAmount: float
        :param WithdrawAmount: 提现扣减总额，单位（分）
        :type WithdrawAmount: float
        :param AgentOutAmount: 资金转出总额，单位（分）
        :type AgentOutAmount: float
        :param AdvancePayAmount: 还垫付总额，单位（分）
        :type AdvancePayAmount: float
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
        r"""
        :param Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :type Offset: int
        :param Limit: 数量，最大值为1000
        :type Limit: int
        :param Month: 月份，格式为yyyy-mm。不能早于开通账单2.0的月份
        :type Month: str
        :param PeriodType: 周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :type PeriodType: str
        :param NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param ActionType: 查询交易类型（请使用交易类型名称入参），入参示例枚举如下：
包年包月新购
包年包月续费
包年包月配置变更
包年包月退款 
按量计费扣费 
线下项目扣费 
线下产品扣费 
调账扣费 
调账补偿 
按量计费小时结 
按量计费日结 
按量计费月结 
竞价实例小时结 
线下项目调账补偿 
线下产品调账补偿 
优惠扣费 
优惠补偿 
按量计费迁入资源 
按量计费迁出资源 
包年包月迁入资源 
包年包月迁出资源 
预付费用 
小时费用 
预留实例退款 
按量计费冲正 
包年包月转按量 
保底扣款 
节省计划小时费用
        :type ActionType: str
        :param ResourceId: 查询指定资源信息
        :type ResourceId: str
        :param PayMode: 付费模式 prePay/postPay
        :type PayMode: str
        :param BusinessCode: 产品名称代码
备注：如需获取当月使用过的BusinessCode，请调用API：<a href="https://cloud.tencent.com/document/product/555/35761">获取产品汇总费用分布</a>
        :type BusinessCode: str
        :param PayerUin: 支付者的账号 ID（账号 ID 是用户在腾讯云的唯一账号标识），默认查询本账号账单，如集团管理账号需查询成员账号自付的账单，该字段需入参成员账号UIN
        :type PayerUin: str
        """
        self.Offset = None
        self.Limit = None
        self.Month = None
        self.PeriodType = None
        self.NeedRecordNum = None
        self.ActionType = None
        self.ResourceId = None
        self.PayMode = None
        self.BusinessCode = None
        self.PayerUin = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Month = params.get("Month")
        self.PeriodType = params.get("PeriodType")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.ActionType = params.get("ActionType")
        self.ResourceId = params.get("ResourceId")
        self.PayMode = params.get("PayMode")
        self.BusinessCode = params.get("BusinessCode")
        self.PayerUin = params.get("PayerUin")
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
        r"""
        :param ResourceSummarySet: 资源汇总列表
        :type ResourceSummarySet: list of BillResourceSummary
        :param Total: 资源汇总列表总数，入参NeedRecordNum为0时不返回
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
        r"""
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        """
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
        r"""
        :param Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
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
        r"""
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param PayType: 款项类别，与L0账单上的汇总类别对应。
此参数自账单3.0（即2021-05）之后开始生效。
枚举值：
consume-消费
refund-退款
adjustment-调账
        :type PayType: str
        """
        self.BeginTime = None
        self.EndTime = None
        self.PayerUin = None
        self.PayType = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.PayerUin = params.get("PayerUin")
        self.PayType = params.get("PayType")
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
        r"""
        :param Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
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
        r"""
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        """
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
        r"""
        :param Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
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
        r"""
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        """
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
        r"""
        :param Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
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
        r"""
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param TagKey: 分账标签键，用户自定义
        :type TagKey: str
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param TagValue: 分账标签值
        :type TagValue: str
        """
        self.BeginTime = None
        self.EndTime = None
        self.TagKey = None
        self.PayerUin = None
        self.TagValue = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TagKey = params.get("TagKey")
        self.PayerUin = params.get("PayerUin")
        self.TagValue = params.get("TagValue")
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
        r"""
        :param Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :type Ready: int
        :param SummaryOverview: 各标签值花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of TagSummaryOverviewItem
        :param SummaryTotal: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryTotal: :class:`tencentcloud.billing.v20180709.models.SummaryTotal`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.SummaryTotal = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = TagSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        if params.get("SummaryTotal") is not None:
            self.SummaryTotal = SummaryTotal()
            self.SummaryTotal._deserialize(params.get("SummaryTotal"))
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryRequest(AbstractModel):
    """DescribeBillSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param Month: 账单月份，格式为2023-04
        :type Month: str
        :param GroupType: 账单维度类型，枚举值如下：business、project、region、payMode、tag
        :type GroupType: str
        :param TagKey: 标签键，GroupType=tag获取标签维度账单时传
        :type TagKey: list of str
        """
        self.Month = None
        self.GroupType = None
        self.TagKey = None


    def _deserialize(self, params):
        self.Month = params.get("Month")
        self.GroupType = params.get("GroupType")
        self.TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryResponse(AbstractModel):
    """DescribeBillSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :type Ready: int
        :param SummaryDetail: 账单多维度汇总消费详情
        :type SummaryDetail: list of SummaryDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryDetail") is not None:
            self.SummaryDetail = []
            for item in params.get("SummaryDetail"):
                obj = SummaryDetail()
                obj._deserialize(item)
                self.SummaryDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCostDetailRequest(AbstractModel):
    """DescribeCostDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 数量，最大值为100
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param BeginTime: 周期开始时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为同一月份，暂不支持跨月拉取。可拉取的数据是开通成本分析后，且距今 24 个月内的数据。
        :type BeginTime: str
        :param EndTime: 周期结束时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为同一月份，暂不支持跨月拉取。可拉取的数据是开通成本分析后，且距今 24 个月内的数据。
        :type EndTime: str
        :param NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param Month: 月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通成本分析的月份，最多可拉取24个月内的数据。
        :type Month: str
        :param ProductCode: 查询指定产品信息（暂时未开放获取）
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
        r"""
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
        r"""
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param Limit: 每次获取数据量，最大值为100
        :type Limit: int
        :param Offset: 偏移量,默认从0开始
        :type Offset: int
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        """
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
        r"""
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
        r"""
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param Limit: 每次获取数据量，最大值为100
        :type Limit: int
        :param Offset: 偏移量,默认从0开始
        :type Offset: int
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        """
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
        r"""
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
        r"""
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param Limit: 每次获取数据量，最大值为100
        :type Limit: int
        :param Offset: 偏移量,默认从0开始
        :type Offset: int
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        """
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
        r"""
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
        r"""
        :param BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param Limit: 每次获取数据量，最大值为100
        :type Limit: int
        :param Offset: 偏移量,默认从0开始
        :type Offset: int
        :param PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        :param NeedConditionValue: 是否需要返回过滤条件，0不需要，1需要，默认不需要
        :type NeedConditionValue: int
        :param Conditions: 过滤条件，只支持ResourceKeyword(资源关键字，支持资源id及资源名称模糊查询)，ProjectIds（项目id），RegionIds(地域id)，PayModes(付费模式，可选prePay和postPay)，HideFreeCost（是否隐藏0元流水，可选0和1），OrderByCost（按费用排序规则，可选desc和asc）
        :type Conditions: :class:`tencentcloud.billing.v20180709.models.Conditions`
        """
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
        r"""
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
        r"""
        :param StartTime: 开始时间 2016-01-01 00:00:00
        :type StartTime: str
        :param EndTime: 结束时间 2016-02-01 00:00:00 建议跨度不超过3个月
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
        :param BigDealId: 大订单号
        :type BigDealId: str
        :param ResourceId: 资源id
        :type ResourceId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.OrderId = None
        self.BigDealId = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.OrderId = params.get("OrderId")
        self.BigDealId = params.get("BigDealId")
        self.ResourceId = params.get("ResourceId")
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
        r"""
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


class DescribeDosageCosDetailByDateRequest(AbstractModel):
    """DescribeDosageCosDetailByDate请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartDate: 查询用量开始时间，例如：2020-09-01
        :type StartDate: str
        :param EndDate: 查询用量结束时间，例如：2020-09-30（与开始时间同月，不支持跨月查询）
        :type EndDate: str
        :param BucketName: COS 存储桶名称，可通过Get Service 接口是用来获取请求者名下的所有存储空间列表（Bucket list）https://cloud.tencent.com/document/product/436/8291
        :type BucketName: str
        """
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
        r"""
        :param DetailSets: 用量数组
        :type DetailSets: list of CosDetailSets
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param StartDate: 查询账单开始日期，如 2019-01-01
        :type StartDate: str
        :param EndDate: 查询账单结束日期，如 2019-01-01， 时间跨度不超过7天
        :type EndDate: str
        :param ProductCode: 互动直播：
10194   互动直播-核心机房           :
10195   互动直播-边缘机房

cdn业务：
102383：CDN静态加速流量(国内)
102384：CDN静态加速带宽(国内)
102385：CDN静态加速流量(海外)
102386：CDN静态加速带宽(海外)

100967：弹性公网IP-按流量计费
101065：公网负载均衡-按流量计费

视频直播
10226 视频直播流量(国内)
10227 视频直播带宽(国内)
100763 视频直播流量(海外)
100762 视频直播宽带(海外)
        :type ProductCode: str
        :param Domain: 查询域名 例如 www.qq.com
非CDN业务查询时传入空字符串，返回的值为空
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
        r"""
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


class DescribeVoucherInfoRequest(AbstractModel):
    """DescribeVoucherInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 一页多少条数据，默认是20条，最大不超过1000
        :type Limit: int
        :param Offset: 第多少页，默认是1
        :type Offset: int
        :param Status: 券状态：待使用：unUsed，已使用： used，已发货：delivered，已作废： cancel，已过期：overdue
        :type Status: str
        :param VoucherId: 代金券id
        :type VoucherId: str
        :param CodeId: 代金券订单id
        :type CodeId: str
        :param ProductCode: 商品码
        :type ProductCode: str
        :param ActivityId: 活动id
        :type ActivityId: str
        :param VoucherName: 代金券名称
        :type VoucherName: str
        :param TimeFrom: 发放开始时间,例：2021-01-01
        :type TimeFrom: str
        :param TimeTo: 发放结束时间，例：2021-01-01
        :type TimeTo: str
        :param SortField: 指定排序字段：BeginTime开始时间、EndTime到期时间、CreateTime创建时间
        :type SortField: str
        :param SortOrder: 指定升序降序：desc、asc
        :type SortOrder: str
        :param PayMode: 付费模式，postPay后付费/prePay预付费/riPay预留实例/""或者"*"表示全部模式，如果payMode为""或"*"，那么productCode与subProductCode必须传空
        :type PayMode: str
        :param PayScene: 付费场景PayMode=postPay时：spotpay-竞价实例,"settle account"-普通后付费PayMode=prePay时：purchase-包年包月新购，renew-包年包月续费（自动续费），modify-包年包月配置变更(变配）PayMode=riPay时：oneOffFee-预留实例预付，hourlyFee-预留实例每小时扣费，*-支持全部付费场景
        :type PayScene: str
        :param Operator: 操作人，默认就是用户uin
        :type Operator: str
        """
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.VoucherId = None
        self.CodeId = None
        self.ProductCode = None
        self.ActivityId = None
        self.VoucherName = None
        self.TimeFrom = None
        self.TimeTo = None
        self.SortField = None
        self.SortOrder = None
        self.PayMode = None
        self.PayScene = None
        self.Operator = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.VoucherId = params.get("VoucherId")
        self.CodeId = params.get("CodeId")
        self.ProductCode = params.get("ProductCode")
        self.ActivityId = params.get("ActivityId")
        self.VoucherName = params.get("VoucherName")
        self.TimeFrom = params.get("TimeFrom")
        self.TimeTo = params.get("TimeTo")
        self.SortField = params.get("SortField")
        self.SortOrder = params.get("SortOrder")
        self.PayMode = params.get("PayMode")
        self.PayScene = params.get("PayScene")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVoucherInfoResponse(AbstractModel):
    """DescribeVoucherInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 券总数
        :type TotalCount: int
        :param TotalBalance: 总余额（微分）
        :type TotalBalance: int
        :param VoucherInfos: 代金券相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VoucherInfos: list of VoucherInfos
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TotalBalance = None
        self.VoucherInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.TotalBalance = params.get("TotalBalance")
        if params.get("VoucherInfos") is not None:
            self.VoucherInfos = []
            for item in params.get("VoucherInfos"):
                obj = VoucherInfos()
                obj._deserialize(item)
                self.VoucherInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVoucherUsageDetailsRequest(AbstractModel):
    """DescribeVoucherUsageDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 一页多少条数据，默认是20条，最大不超过1000
        :type Limit: int
        :param Offset: 第多少页，默认是1
        :type Offset: int
        :param VoucherId: 代金券id
        :type VoucherId: str
        :param Operator: 操作人，默认就是用户uin
        :type Operator: str
        """
        self.Limit = None
        self.Offset = None
        self.VoucherId = None
        self.Operator = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.VoucherId = params.get("VoucherId")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVoucherUsageDetailsResponse(AbstractModel):
    """DescribeVoucherUsageDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 券总数
        :type TotalCount: int
        :param TotalUsedAmount: 总已用金额（微分）
        :type TotalUsedAmount: int
        :param UsageRecords: 代金券使用记录细节
注意：此字段可能返回 null，表示取不到有效值。
        :type UsageRecords: list of UsageRecords
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TotalUsedAmount = None
        self.UsageRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.TotalUsedAmount = params.get("TotalUsedAmount")
        if params.get("UsageRecords") is not None:
            self.UsageRecords = []
            for item in params.get("UsageRecords"):
                obj = UsageRecords()
                obj._deserialize(item)
                self.UsageRecords.append(obj)
        self.RequestId = params.get("RequestId")


class DetailPoint(AbstractModel):
    """由时间和值组成的数据结构

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExcludedProducts(AbstractModel):
    """不适用商品信息

    """

    def __init__(self):
        r"""
        :param GoodsName: 不适用商品名称
        :type GoodsName: str
        :param PayMode: postPay后付费/prePay预付费/riPay预留实例/空字符串或者"*"表示全部模式。
        :type PayMode: str
        """
        self.GoodsName = None
        self.PayMode = None


    def _deserialize(self, params):
        self.GoodsName = params.get("GoodsName")
        self.PayMode = params.get("PayMode")
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
        r"""
        :param OrderIds: 需要支付的一个或者多个子订单号，与BigDealIds字段两者必须且仅传一个参数
        :type OrderIds: list of str
        :param AutoVoucher: 是否自动使用代金券,1:是,0否,默认0
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表,目前仅支持指定一张代金券
        :type VoucherIds: list of str
        :param BigDealIds: 需要支付的一个或者多个大订单号，与OrderIds字段两者必须且仅传一个参数
        :type BigDealIds: list of str
        """
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
        r"""
        :param OrderIds: 此次操作支付成功的子订单号数组
        :type OrderIds: list of str
        :param ResourceIds: 此次操作支付成功的资源Id数组
        :type ResourceIds: list of str
        :param BigDealIds: 此次操作支付成功的大订单号数组
        :type BigDealIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
    """按计费模式汇总消费详情

    """

    def __init__(self):
        r"""
        :param PayMode: 计费模式编码
        :type PayMode: str
        :param PayModeName: 计费模式：区分为包年包月和按量计费
        :type PayModeName: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        :param Detail: 按交易类型汇总消费详情
        :type Detail: list of ActionSummaryOverviewItem
        """
        self.PayMode = None
        self.PayModeName = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.TotalCost = None
        self.Detail = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.PayModeName = params.get("PayModeName")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.TotalCost = params.get("TotalCost")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = ActionSummaryOverviewItem()
                obj._deserialize(item)
                self.Detail.append(obj)
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
        r"""
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
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :type ProjectName: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        :param TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.BillMonth = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.BillMonth = params.get("BillMonth")
        self.TotalCost = params.get("TotalCost")
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
        r"""
        :param RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        :param RegionName: 地域名称：资源所属地域，例如华南地区（广州）
        :type RegionName: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        :param TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        """
        self.RegionId = None
        self.RegionName = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.BillMonth = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.BillMonth = params.get("BillMonth")
        self.TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryDetail(AbstractModel):
    """账单多维度汇总消费详情

    """

    def __init__(self):
        r"""
        :param GroupKey: 账单维度编码
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupKey: str
        :param GroupValue: 账单维度值
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupValue: str
        :param TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        :param RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        :param Business: 产品汇总信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Business: list of BusinessSummaryInfo
        """
        self.GroupKey = None
        self.GroupValue = None
        self.TotalCost = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.Business = None


    def _deserialize(self, params):
        self.GroupKey = params.get("GroupKey")
        self.GroupValue = params.get("GroupValue")
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        if params.get("Business") is not None:
            self.Business = []
            for item in params.get("Business"):
                obj = BusinessSummaryInfo()
                obj._deserialize(item)
                self.Business.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryTotal(AbstractModel):
    """总数

    """

    def __init__(self):
        r"""
        :param RealTotalCost: 优惠后总价
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalCost: str
        :param TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: str
        """
        self.RealTotalCost = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.TotalCost = params.get("TotalCost")
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
        r"""
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        :param RealTotalCostRatio: 费用所占百分比，两位小数
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalCostRatio: str
        :param RealTotalCost: 优惠后总价
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalCost: str
        :param CashPayAmount: 现金账户支出：通过现金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type CashPayAmount: str
        :param IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type IncentivePayAmount: str
        :param VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type VoucherPayAmount: str
        :param TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        :param TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: str
        """
        self.TagValue = None
        self.RealTotalCostRatio = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.TransferPayAmount = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.TagValue = params.get("TagValue")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.TransferPayAmount = params.get("TransferPayAmount")
        self.TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageDetails(AbstractModel):
    """购买商品信息

    """

    def __init__(self):
        r"""
        :param ProductName: 商品名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param SubProductName: 商品细节
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProductName: str
        """
        self.ProductName = None
        self.SubProductName = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.SubProductName = params.get("SubProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageRecords(AbstractModel):
    """使用记录

    """

    def __init__(self):
        r"""
        :param UsedAmount: 使用金额（微分）
        :type UsedAmount: int
        :param UsedTime: 使用时间
        :type UsedTime: str
        :param UsageDetails: 使用记录细节
注意：此字段可能返回 null，表示取不到有效值。
        :type UsageDetails: list of UsageDetails
        """
        self.UsedAmount = None
        self.UsedTime = None
        self.UsageDetails = None


    def _deserialize(self, params):
        self.UsedAmount = params.get("UsedAmount")
        self.UsedTime = params.get("UsedTime")
        if params.get("UsageDetails") is not None:
            self.UsageDetails = []
            for item in params.get("UsageDetails"):
                obj = UsageDetails()
                obj._deserialize(item)
                self.UsageDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoucherInfos(AbstractModel):
    """代金券相关信息

    """

    def __init__(self):
        r"""
        :param OwnerUin: 代金券拥有者
        :type OwnerUin: str
        :param Status: 券状态：待使用：unUsed，已使用： used，已发货：delivered，已作废： cancel，已过期：overdue
        :type Status: str
        :param NominalValue: 代金券面额（微分）
        :type NominalValue: int
        :param Balance: 剩余金额（微分）
        :type Balance: int
        :param VoucherId: 代金券id
        :type VoucherId: str
        :param PayMode: postPay后付费/prePay预付费/riPay预留实例/空字符串或者'*'表示全部模式
        :type PayMode: str
        :param PayScene: 付费场景PayMode=postPay时：spotpay-竞价实例,"settle account"-普通后付费PayMode=prePay时：purchase-包年包月新购，renew-包年包月续费（自动续费），modify-包年包月配置变更(变配）PayMode=riPay时：oneOffFee-预留实例预付，hourlyFee-预留实例每小时扣费，*-支持全部付费场景
        :type PayScene: str
        :param BeginTime: 有效期生效时间
        :type BeginTime: str
        :param EndTime: 有效期截止时间
        :type EndTime: str
        :param ApplicableProducts: 适用商品信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicableProducts: :class:`tencentcloud.billing.v20180709.models.ApplicableProducts`
        :param ExcludedProducts: 不适用商品信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludedProducts: list of ExcludedProducts
        """
        self.OwnerUin = None
        self.Status = None
        self.NominalValue = None
        self.Balance = None
        self.VoucherId = None
        self.PayMode = None
        self.PayScene = None
        self.BeginTime = None
        self.EndTime = None
        self.ApplicableProducts = None
        self.ExcludedProducts = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.Status = params.get("Status")
        self.NominalValue = params.get("NominalValue")
        self.Balance = params.get("Balance")
        self.VoucherId = params.get("VoucherId")
        self.PayMode = params.get("PayMode")
        self.PayScene = params.get("PayScene")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        if params.get("ApplicableProducts") is not None:
            self.ApplicableProducts = ApplicableProducts()
            self.ApplicableProducts._deserialize(params.get("ApplicableProducts"))
        if params.get("ExcludedProducts") is not None:
            self.ExcludedProducts = []
            for item in params.get("ExcludedProducts"):
                obj = ExcludedProducts()
                obj._deserialize(item)
                self.ExcludedProducts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        