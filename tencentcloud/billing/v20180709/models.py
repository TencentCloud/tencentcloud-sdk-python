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
        :param _ActionType: 交易类型编码
        :type ActionType: str
        :param _ActionTypeName: 交易类型：如包年包月新购、包年包月续费、按量计费扣费等类型
        :type ActionTypeName: str
        :param _RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param _RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        :param _BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        :param _TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        """
        self._ActionType = None
        self._ActionTypeName = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._BillMonth = None
        self._TotalCost = None

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._BillMonth = params.get("BillMonth")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicableProducts(AbstractModel):
    """适用商品信息

    """

    def __init__(self):
        r"""
        :param _GoodsName: 适用商品名称，值为“全产品通用”或商品名称组成的string，以","分割。
        :type GoodsName: str
        :param _PayMode: postPay后付费/prePay预付费/riPay预留实例/空字符串或者"*"表示全部模式。如GoodsName为多个商品名以","分割组成的string，而PayMode为"*"，表示每一件商品的模式都为"*"。
        :type PayMode: str
        """
        self._GoodsName = None
        self._PayMode = None

    @property
    def GoodsName(self):
        return self._GoodsName

    @GoodsName.setter
    def GoodsName(self, GoodsName):
        self._GoodsName = GoodsName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._GoodsName = params.get("GoodsName")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetail(AbstractModel):
    """账单明细数据对象

    """

    def __init__(self):
        r"""
        :param _BusinessCodeName: 产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :type BusinessCodeName: str
        :param _ProductCodeName: 子产品名称：用户采购的具体产品细分类型，例如：云服务器 CVM-标准型 S1
        :type ProductCodeName: str
        :param _PayModeName: 计费模式：资源的计费模式，区分为包年包月和按量计费
        :type PayModeName: str
        :param _ProjectName: 项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :type ProjectName: str
        :param _RegionName: 地域：资源所属地域，如华南地区（广州）
        :type RegionName: str
        :param _ZoneName: 可用区：资源所属可用区，如广州三区
        :type ZoneName: str
        :param _ResourceId: 资源 ID：账单中出账对象 ID，不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID
        :type ResourceId: str
        :param _ResourceName: 资源别名：用户在控制台为资源设置的名称，如果未设置，则默认为空
        :type ResourceName: str
        :param _ActionTypeName: 交易类型，如包年包月新购、包年包月续费、按量计费扣费等类型
        :type ActionTypeName: str
        :param _OrderId: 订单ID：包年包月计费模式下订购的订单号
        :type OrderId: str
        :param _BillId: 交易ID：结算扣费单号
        :type BillId: str
        :param _PayTime: 扣费时间：结算扣费时间
        :type PayTime: str
        :param _FeeBeginTime: 开始使用时间：产品服务开始使用时间
        :type FeeBeginTime: str
        :param _FeeEndTime: 结束使用时间：产品服务结束使用时间
        :type FeeEndTime: str
        :param _ComponentSet: 组件列表
        :type ComponentSet: list of BillDetailComponent
        :param _PayerUin: 支付者UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :type PayerUin: str
        :param _OwnerUin: 使用者UIN：实际使用资源的账号 ID
        :type OwnerUin: str
        :param _OperateUin: 操作者UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的 ID 或者角色 ID ）
        :type OperateUin: str
        :param _Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of BillTagInfo
        :param _BusinessCode: 产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessCode: str
        :param _ProductCode: 子产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param _ActionType: 交易类型编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionType: str
        :param _RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _PriceInfo: 价格属性
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceInfo: list of str
        """
        self._BusinessCodeName = None
        self._ProductCodeName = None
        self._PayModeName = None
        self._ProjectName = None
        self._RegionName = None
        self._ZoneName = None
        self._ResourceId = None
        self._ResourceName = None
        self._ActionTypeName = None
        self._OrderId = None
        self._BillId = None
        self._PayTime = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._ComponentSet = None
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._Tags = None
        self._BusinessCode = None
        self._ProductCode = None
        self._ActionType = None
        self._RegionId = None
        self._ProjectId = None
        self._PriceInfo = None

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def PayTime(self):
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentSet(self):
        return self._ComponentSet

    @ComponentSet.setter
    def ComponentSet(self, ComponentSet):
        self._ComponentSet = ComponentSet

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PriceInfo(self):
        return self._PriceInfo

    @PriceInfo.setter
    def PriceInfo(self, PriceInfo):
        self._PriceInfo = PriceInfo


    def _deserialize(self, params):
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCodeName = params.get("ProductCodeName")
        self._PayModeName = params.get("PayModeName")
        self._ProjectName = params.get("ProjectName")
        self._RegionName = params.get("RegionName")
        self._ZoneName = params.get("ZoneName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._ActionTypeName = params.get("ActionTypeName")
        self._OrderId = params.get("OrderId")
        self._BillId = params.get("BillId")
        self._PayTime = params.get("PayTime")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        if params.get("ComponentSet") is not None:
            self._ComponentSet = []
            for item in params.get("ComponentSet"):
                obj = BillDetailComponent()
                obj._deserialize(item)
                self._ComponentSet.append(obj)
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._BusinessCode = params.get("BusinessCode")
        self._ProductCode = params.get("ProductCode")
        self._ActionType = params.get("ActionType")
        self._RegionId = params.get("RegionId")
        self._ProjectId = params.get("ProjectId")
        self._PriceInfo = params.get("PriceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetailComponent(AbstractModel):
    """账单明细组件对象

    """

    def __init__(self):
        r"""
        :param _ComponentCodeName: 组件类型：用户购买的产品或服务对应的组件大类，例如：云服务器 CVM 的组件：CPU、内存等
        :type ComponentCodeName: str
        :param _ItemCodeName: 组件名称：用户购买的产品或服务，所包含的具体组件
        :type ItemCodeName: str
        :param _SinglePrice: 组件刊例价：组件的官网原始单价（如果客户享受一口价/合同价则默认不展示）
        :type SinglePrice: str
        :param _SpecifiedPrice: 组件指定价（已废弃）
        :type SpecifiedPrice: str
        :param _PriceUnit: 组件价格单位：组件价格的单位，单位构成：元/用量单位/时长单位
        :type PriceUnit: str
        :param _UsedAmount: 组件用量：该组件实际结算用量，组件用量 = 组件原始用量 - 抵扣用量（含资源包
        :type UsedAmount: str
        :param _UsedAmountUnit: 组件用量单位：组件用量对应的单位
        :type UsedAmountUnit: str
        :param _RealTotalMeasure: 原始用量/时长：组件被资源包抵扣前的原始用量/时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalMeasure: str
        :param _DeductedMeasure: 抵扣用量/时长（含资源包）：组件被资源包抵扣的用量/时长
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductedMeasure: str
        :param _TimeSpan: 使用时长：资源使用的时长
        :type TimeSpan: str
        :param _TimeUnitName: 时长单位：资源使用时长的单位
        :type TimeUnitName: str
        :param _Cost: 组件原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如果客户享受一口价/合同价则默认不展示，退费类场景也默认不展示）
        :type Cost: str
        :param _Discount: 折扣率：本资源享受的折扣率（如果客户享受一口价/合同价则默认不展示，退费场景也默认不展示）
        :type Discount: str
        :param _ReduceType: 优惠类型
        :type ReduceType: str
        :param _RealCost: 优惠后总价：优惠后总价=（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :type RealCost: str
        :param _VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        :param _ItemCode: 组件类型编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemCode: str
        :param _ComponentCode: 组件名称编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentCode: str
        :param _ContractPrice: 组件单价：组件的折后单价，组件单价 = 刊例价 * 折扣
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractPrice: str
        :param _InstanceType: 实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。正常的实例展示默认为不展示
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _RiTimeSpan: 预留实例抵扣的使用时长：本产品或服务使用预留实例抵扣的使用时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RiTimeSpan: str
        :param _OriginalCostWithRI: 预留实例抵扣组件原价：本产品或服务使用预留实例抵扣的组件原价金额
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCostWithRI: str
        :param _SPDeductionRate: 节省计划抵扣率：节省计划可用余额额度范围内，节省计划对于此组件打的折扣率
注意：此字段可能返回 null，表示取不到有效值。
        :type SPDeductionRate: str
        :param _SPDeduction: 节省计划抵扣金额（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type SPDeduction: str
        :param _OriginalCostWithSP: 节省计划抵扣组件原价：节省计划抵扣原价=节省计划包抵扣金额/节省计划抵扣率
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCostWithSP: str
        :param _BlendedDiscount: 混合折扣率：综合各类折扣抵扣信息后的最终折扣率，混合折扣率 = 优惠后总价 / 组件原价
注意：此字段可能返回 null，表示取不到有效值。
        :type BlendedDiscount: str
        """
        self._ComponentCodeName = None
        self._ItemCodeName = None
        self._SinglePrice = None
        self._SpecifiedPrice = None
        self._PriceUnit = None
        self._UsedAmount = None
        self._UsedAmountUnit = None
        self._RealTotalMeasure = None
        self._DeductedMeasure = None
        self._TimeSpan = None
        self._TimeUnitName = None
        self._Cost = None
        self._Discount = None
        self._ReduceType = None
        self._RealCost = None
        self._VoucherPayAmount = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._ItemCode = None
        self._ComponentCode = None
        self._ContractPrice = None
        self._InstanceType = None
        self._RiTimeSpan = None
        self._OriginalCostWithRI = None
        self._SPDeductionRate = None
        self._SPDeduction = None
        self._OriginalCostWithSP = None
        self._BlendedDiscount = None

    @property
    def ComponentCodeName(self):
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def ItemCodeName(self):
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def SinglePrice(self):
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def SpecifiedPrice(self):
        warnings.warn("parameter `SpecifiedPrice` is deprecated", DeprecationWarning) 

        return self._SpecifiedPrice

    @SpecifiedPrice.setter
    def SpecifiedPrice(self, SpecifiedPrice):
        warnings.warn("parameter `SpecifiedPrice` is deprecated", DeprecationWarning) 

        self._SpecifiedPrice = SpecifiedPrice

    @property
    def PriceUnit(self):
        return self._PriceUnit

    @PriceUnit.setter
    def PriceUnit(self, PriceUnit):
        self._PriceUnit = PriceUnit

    @property
    def UsedAmount(self):
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def RealTotalMeasure(self):
        return self._RealTotalMeasure

    @RealTotalMeasure.setter
    def RealTotalMeasure(self, RealTotalMeasure):
        self._RealTotalMeasure = RealTotalMeasure

    @property
    def DeductedMeasure(self):
        return self._DeductedMeasure

    @DeductedMeasure.setter
    def DeductedMeasure(self, DeductedMeasure):
        self._DeductedMeasure = DeductedMeasure

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnitName(self):
        return self._TimeUnitName

    @TimeUnitName.setter
    def TimeUnitName(self, TimeUnitName):
        self._TimeUnitName = TimeUnitName

    @property
    def Cost(self):
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ReduceType(self):
        return self._ReduceType

    @ReduceType.setter
    def ReduceType(self, ReduceType):
        self._ReduceType = ReduceType

    @property
    def RealCost(self):
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ItemCode(self):
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ComponentCode(self):
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ContractPrice(self):
        return self._ContractPrice

    @ContractPrice.setter
    def ContractPrice(self, ContractPrice):
        self._ContractPrice = ContractPrice

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def RiTimeSpan(self):
        return self._RiTimeSpan

    @RiTimeSpan.setter
    def RiTimeSpan(self, RiTimeSpan):
        self._RiTimeSpan = RiTimeSpan

    @property
    def OriginalCostWithRI(self):
        return self._OriginalCostWithRI

    @OriginalCostWithRI.setter
    def OriginalCostWithRI(self, OriginalCostWithRI):
        self._OriginalCostWithRI = OriginalCostWithRI

    @property
    def SPDeductionRate(self):
        return self._SPDeductionRate

    @SPDeductionRate.setter
    def SPDeductionRate(self, SPDeductionRate):
        self._SPDeductionRate = SPDeductionRate

    @property
    def SPDeduction(self):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        self._SPDeduction = SPDeduction

    @property
    def OriginalCostWithSP(self):
        return self._OriginalCostWithSP

    @OriginalCostWithSP.setter
    def OriginalCostWithSP(self, OriginalCostWithSP):
        self._OriginalCostWithSP = OriginalCostWithSP

    @property
    def BlendedDiscount(self):
        return self._BlendedDiscount

    @BlendedDiscount.setter
    def BlendedDiscount(self, BlendedDiscount):
        self._BlendedDiscount = BlendedDiscount


    def _deserialize(self, params):
        self._ComponentCodeName = params.get("ComponentCodeName")
        self._ItemCodeName = params.get("ItemCodeName")
        self._SinglePrice = params.get("SinglePrice")
        self._SpecifiedPrice = params.get("SpecifiedPrice")
        self._PriceUnit = params.get("PriceUnit")
        self._UsedAmount = params.get("UsedAmount")
        self._UsedAmountUnit = params.get("UsedAmountUnit")
        self._RealTotalMeasure = params.get("RealTotalMeasure")
        self._DeductedMeasure = params.get("DeductedMeasure")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnitName = params.get("TimeUnitName")
        self._Cost = params.get("Cost")
        self._Discount = params.get("Discount")
        self._ReduceType = params.get("ReduceType")
        self._RealCost = params.get("RealCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._ItemCode = params.get("ItemCode")
        self._ComponentCode = params.get("ComponentCode")
        self._ContractPrice = params.get("ContractPrice")
        self._InstanceType = params.get("InstanceType")
        self._RiTimeSpan = params.get("RiTimeSpan")
        self._OriginalCostWithRI = params.get("OriginalCostWithRI")
        self._SPDeductionRate = params.get("SPDeductionRate")
        self._SPDeduction = params.get("SPDeduction")
        self._OriginalCostWithSP = params.get("OriginalCostWithSP")
        self._BlendedDiscount = params.get("BlendedDiscount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillResourceSummary(AbstractModel):
    """账单资源汇总数据对象

    """

    def __init__(self):
        r"""
        :param _BusinessCodeName: 产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :type BusinessCodeName: str
        :param _ProductCodeName: 子产品名称：用户采购的具体产品细分类型，例如：云服务器 CVM-标准型 S1
        :type ProductCodeName: str
        :param _PayModeName: 计费模式：资源的计费模式，区分为包年包月和按量计费
        :type PayModeName: str
        :param _ProjectName: 项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :type ProjectName: str
        :param _RegionName: 地域：资源所属地域，如华南地区（广州）
        :type RegionName: str
        :param _ZoneName: 可用区：资源所属可用区，如广州三区
        :type ZoneName: str
        :param _ResourceId: 资源 ID：账单中出账对象 ID，不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID	
        :type ResourceId: str
        :param _ResourceName: 资源别名：用户在控制台为资源设置的名称，如果未设置，则默认为空
        :type ResourceName: str
        :param _ActionTypeName: 交易类型：如包年包月新购、包年包月续费、按量计费扣费等类型
        :type ActionTypeName: str
        :param _OrderId: 订单ID：包年包月计费模式下订购的订单号
        :type OrderId: str
        :param _PayTime: 扣费时间：结算扣费时间
        :type PayTime: str
        :param _FeeBeginTime: 开始使用时间：产品服务开始使用时间
        :type FeeBeginTime: str
        :param _FeeEndTime: 结束使用时间：产品服务结束使用时间
        :type FeeEndTime: str
        :param _ConfigDesc: 配置描述：该资源下的计费项名称和用量合并展示，仅在资源账单体现
        :type ConfigDesc: str
        :param _ExtendField1: 扩展字段1：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField1: str
        :param _ExtendField2: 扩展字段2：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField2: str
        :param _TotalCost: 原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如果客户享受一口价/合同价则默认不展示，退费类场景也默认不展示）
        :type TotalCost: str
        :param _Discount: 折扣率：本资源享受的折扣率（如果客户享受一口价/合同价则默认不展示，退费场景也默认不展示）
        :type Discount: str
        :param _ReduceType: 优惠类型
        :type ReduceType: str
        :param _RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param _VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        :param _ExtendField3: 扩展字段3：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField3: str
        :param _ExtendField4: 扩展字段4：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField4: str
        :param _ExtendField5: 扩展字段5：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField5: str
        :param _Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of BillTagInfo
        :param _PayerUin: 支付者UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :type PayerUin: str
        :param _OwnerUin: 使用者UIN：实际使用资源的账号 ID
        :type OwnerUin: str
        :param _OperateUin: 操作者UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的 ID 或者角色 ID ）
        :type OperateUin: str
        :param _BusinessCode: 产品编码
        :type BusinessCode: str
        :param _ProductCode: 子产品编码
        :type ProductCode: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _InstanceType: 实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。正常的实例展示默认为不展示
        :type InstanceType: str
        :param _OriginalCostWithRI: 预留实例抵扣组件原价：本产品或服务使用预留实例抵扣的组件原价金额	
        :type OriginalCostWithRI: str
        :param _SPDeduction: 节省计划抵扣金额（已废弃）
        :type SPDeduction: str
        :param _OriginalCostWithSP: 节省计划抵扣组件原价：节省计划抵扣原价=节省计划包抵扣金额/节省计划抵扣率	
        :type OriginalCostWithSP: str
        """
        self._BusinessCodeName = None
        self._ProductCodeName = None
        self._PayModeName = None
        self._ProjectName = None
        self._RegionName = None
        self._ZoneName = None
        self._ResourceId = None
        self._ResourceName = None
        self._ActionTypeName = None
        self._OrderId = None
        self._PayTime = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._ConfigDesc = None
        self._ExtendField1 = None
        self._ExtendField2 = None
        self._TotalCost = None
        self._Discount = None
        self._ReduceType = None
        self._RealTotalCost = None
        self._VoucherPayAmount = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._ExtendField3 = None
        self._ExtendField4 = None
        self._ExtendField5 = None
        self._Tags = None
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._BusinessCode = None
        self._ProductCode = None
        self._RegionId = None
        self._InstanceType = None
        self._OriginalCostWithRI = None
        self._SPDeduction = None
        self._OriginalCostWithSP = None

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def PayTime(self):
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ConfigDesc(self):
        return self._ConfigDesc

    @ConfigDesc.setter
    def ConfigDesc(self, ConfigDesc):
        self._ConfigDesc = ConfigDesc

    @property
    def ExtendField1(self):
        return self._ExtendField1

    @ExtendField1.setter
    def ExtendField1(self, ExtendField1):
        self._ExtendField1 = ExtendField1

    @property
    def ExtendField2(self):
        return self._ExtendField2

    @ExtendField2.setter
    def ExtendField2(self, ExtendField2):
        self._ExtendField2 = ExtendField2

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ReduceType(self):
        return self._ReduceType

    @ReduceType.setter
    def ReduceType(self, ReduceType):
        self._ReduceType = ReduceType

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ExtendField3(self):
        return self._ExtendField3

    @ExtendField3.setter
    def ExtendField3(self, ExtendField3):
        self._ExtendField3 = ExtendField3

    @property
    def ExtendField4(self):
        return self._ExtendField4

    @ExtendField4.setter
    def ExtendField4(self, ExtendField4):
        self._ExtendField4 = ExtendField4

    @property
    def ExtendField5(self):
        return self._ExtendField5

    @ExtendField5.setter
    def ExtendField5(self, ExtendField5):
        self._ExtendField5 = ExtendField5

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OriginalCostWithRI(self):
        return self._OriginalCostWithRI

    @OriginalCostWithRI.setter
    def OriginalCostWithRI(self, OriginalCostWithRI):
        self._OriginalCostWithRI = OriginalCostWithRI

    @property
    def SPDeduction(self):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        self._SPDeduction = SPDeduction

    @property
    def OriginalCostWithSP(self):
        return self._OriginalCostWithSP

    @OriginalCostWithSP.setter
    def OriginalCostWithSP(self, OriginalCostWithSP):
        self._OriginalCostWithSP = OriginalCostWithSP


    def _deserialize(self, params):
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCodeName = params.get("ProductCodeName")
        self._PayModeName = params.get("PayModeName")
        self._ProjectName = params.get("ProjectName")
        self._RegionName = params.get("RegionName")
        self._ZoneName = params.get("ZoneName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._ActionTypeName = params.get("ActionTypeName")
        self._OrderId = params.get("OrderId")
        self._PayTime = params.get("PayTime")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        self._ConfigDesc = params.get("ConfigDesc")
        self._ExtendField1 = params.get("ExtendField1")
        self._ExtendField2 = params.get("ExtendField2")
        self._TotalCost = params.get("TotalCost")
        self._Discount = params.get("Discount")
        self._ReduceType = params.get("ReduceType")
        self._RealTotalCost = params.get("RealTotalCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._ExtendField3 = params.get("ExtendField3")
        self._ExtendField4 = params.get("ExtendField4")
        self._ExtendField5 = params.get("ExtendField5")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._BusinessCode = params.get("BusinessCode")
        self._ProductCode = params.get("ProductCode")
        self._RegionId = params.get("RegionId")
        self._InstanceType = params.get("InstanceType")
        self._OriginalCostWithRI = params.get("OriginalCostWithRI")
        self._SPDeduction = params.get("SPDeduction")
        self._OriginalCostWithSP = params.get("OriginalCostWithSP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillTagInfo(AbstractModel):
    """账单 Tag 信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 分账标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillTransactionInfo(AbstractModel):
    """收支明细的流水信息

    """

    def __init__(self):
        r"""
        :param _ActionType: 收支类型：deduct 扣费, recharge 充值, return 退费， block 冻结, unblock 解冻
        :type ActionType: str
        :param _Amount: 流水金额，单位（分）；正数表示入账，负数表示出账
        :type Amount: int
        :param _Balance: 可用余额，单位（分）；正数表示入账，负数表示出账
        :type Balance: int
        :param _BillId: 流水号，如20190131020000236005203583326401
        :type BillId: str
        :param _OperationInfo: 描述信息
        :type OperationInfo: str
        :param _OperationTime: 操作时间"2019-01-31 23:35:10.000"
        :type OperationTime: str
        :param _Cash: 现金账户余额，单位（分）
        :type Cash: int
        :param _Incentive: 赠送金余额，单位（分）
        :type Incentive: int
        :param _Freezing: 冻结余额，单位（分）
        :type Freezing: int
        :param _PayChannel: 交易渠道
        :type PayChannel: str
        :param _DeductMode: 扣费模式：trade 包年包月(预付费)，hourh  按量-小时结，hourd 按量-日结，hourm 按量-月结，month 按量-月结
        :type DeductMode: str
        """
        self._ActionType = None
        self._Amount = None
        self._Balance = None
        self._BillId = None
        self._OperationInfo = None
        self._OperationTime = None
        self._Cash = None
        self._Incentive = None
        self._Freezing = None
        self._PayChannel = None
        self._DeductMode = None

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def Balance(self):
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def BillId(self):
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def OperationInfo(self):
        return self._OperationInfo

    @OperationInfo.setter
    def OperationInfo(self, OperationInfo):
        self._OperationInfo = OperationInfo

    @property
    def OperationTime(self):
        return self._OperationTime

    @OperationTime.setter
    def OperationTime(self, OperationTime):
        self._OperationTime = OperationTime

    @property
    def Cash(self):
        return self._Cash

    @Cash.setter
    def Cash(self, Cash):
        self._Cash = Cash

    @property
    def Incentive(self):
        return self._Incentive

    @Incentive.setter
    def Incentive(self, Incentive):
        self._Incentive = Incentive

    @property
    def Freezing(self):
        return self._Freezing

    @Freezing.setter
    def Freezing(self, Freezing):
        self._Freezing = Freezing

    @property
    def PayChannel(self):
        return self._PayChannel

    @PayChannel.setter
    def PayChannel(self, PayChannel):
        self._PayChannel = PayChannel

    @property
    def DeductMode(self):
        return self._DeductMode

    @DeductMode.setter
    def DeductMode(self, DeductMode):
        self._DeductMode = DeductMode


    def _deserialize(self, params):
        self._ActionType = params.get("ActionType")
        self._Amount = params.get("Amount")
        self._Balance = params.get("Balance")
        self._BillId = params.get("BillId")
        self._OperationInfo = params.get("OperationInfo")
        self._OperationTime = params.get("OperationTime")
        self._Cash = params.get("Cash")
        self._Incentive = params.get("Incentive")
        self._Freezing = params.get("Freezing")
        self._PayChannel = params.get("PayChannel")
        self._DeductMode = params.get("DeductMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessSummaryInfo(AbstractModel):
    """产品汇总信息

    """

    def __init__(self):
        r"""
        :param _BusinessCode: 产品编码
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :type BusinessCodeName: str
        :param _TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: str
        :param _RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._TotalCost = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._TotalCost = params.get("TotalCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessSummaryOverviewItem(AbstractModel):
    """按产品汇总产品详情

    """

    def __init__(self):
        r"""
        :param _BusinessCode: 产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :type BusinessCodeName: str
        :param _RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param _RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param _BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        :param _TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._BillMonth = None
        self._TotalCost = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._BillMonth = params.get("BillMonth")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessSummaryTotal(AbstractModel):
    """按产品汇总总费用

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: 优惠后总价

        :type RealTotalCost: str
        :param _VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param _TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        """
        self._RealTotalCost = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._CashPayAmount = None
        self._TransferPayAmount = None
        self._TotalCost = None

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._RealTotalCost = params.get("RealTotalCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._CashPayAmount = params.get("CashPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionBusiness(AbstractModel):
    """产品过滤条件

    """

    def __init__(self):
        r"""
        :param _BusinessCode: 产品名称代码
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionPayMode(AbstractModel):
    """付费模式过滤条件

    """

    def __init__(self):
        r"""
        :param _PayMode: 付费模式
        :type PayMode: str
        :param _PayModeName: 付费模式名称
        :type PayModeName: str
        """
        self._PayMode = None
        self._PayModeName = None

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionProject(AbstractModel):
    """项目过滤条件

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        """
        self._ProjectId = None
        self._ProjectName = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionRegion(AbstractModel):
    """地域过滤条件

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: str
        :param _RegionName: 地域名称
        :type RegionName: str
        """
        self._RegionId = None
        self._RegionName = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Conditions(AbstractModel):
    """账单筛选条件对象

    """

    def __init__(self):
        r"""
        :param _TimeRange: 只支持6和12两个值
        :type TimeRange: int
        :param _BusinessCode: 产品名称代码
        :type BusinessCode: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _PayMode: 付费模式，可选prePay和postPay
        :type PayMode: str
        :param _ResourceKeyword: 资源关键字
        :type ResourceKeyword: str
        :param _BusinessCodes: 产品名称代码
        :type BusinessCodes: list of str
        :param _ProductCodes: 子产品名称代码
        :type ProductCodes: list of str
        :param _RegionIds: 地域ID
        :type RegionIds: list of int
        :param _ProjectIds: 项目ID
        :type ProjectIds: list of int
        :param _PayModes: 付费模式，可选prePay和postPay
        :type PayModes: list of str
        :param _ActionTypes: 交易类型
        :type ActionTypes: list of str
        :param _HideFreeCost: 是否隐藏0元流水
        :type HideFreeCost: int
        :param _OrderByCost: 排序规则，可选desc和asc
        :type OrderByCost: str
        :param _BillIds: 交易ID
        :type BillIds: list of str
        :param _ComponentCodes: 组件编码
        :type ComponentCodes: list of str
        :param _FileIds: 文件ID
        :type FileIds: list of str
        :param _FileTypes: 文件类型
        :type FileTypes: list of str
        :param _Status: 状态
        :type Status: list of int non-negative
        """
        self._TimeRange = None
        self._BusinessCode = None
        self._ProjectId = None
        self._RegionId = None
        self._PayMode = None
        self._ResourceKeyword = None
        self._BusinessCodes = None
        self._ProductCodes = None
        self._RegionIds = None
        self._ProjectIds = None
        self._PayModes = None
        self._ActionTypes = None
        self._HideFreeCost = None
        self._OrderByCost = None
        self._BillIds = None
        self._ComponentCodes = None
        self._FileIds = None
        self._FileTypes = None
        self._Status = None

    @property
    def TimeRange(self):
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceKeyword(self):
        return self._ResourceKeyword

    @ResourceKeyword.setter
    def ResourceKeyword(self, ResourceKeyword):
        self._ResourceKeyword = ResourceKeyword

    @property
    def BusinessCodes(self):
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def ProductCodes(self):
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def PayModes(self):
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def HideFreeCost(self):
        return self._HideFreeCost

    @HideFreeCost.setter
    def HideFreeCost(self, HideFreeCost):
        self._HideFreeCost = HideFreeCost

    @property
    def OrderByCost(self):
        return self._OrderByCost

    @OrderByCost.setter
    def OrderByCost(self, OrderByCost):
        self._OrderByCost = OrderByCost

    @property
    def BillIds(self):
        return self._BillIds

    @BillIds.setter
    def BillIds(self, BillIds):
        self._BillIds = BillIds

    @property
    def ComponentCodes(self):
        return self._ComponentCodes

    @ComponentCodes.setter
    def ComponentCodes(self, ComponentCodes):
        self._ComponentCodes = ComponentCodes

    @property
    def FileIds(self):
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def FileTypes(self):
        return self._FileTypes

    @FileTypes.setter
    def FileTypes(self, FileTypes):
        self._FileTypes = FileTypes

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TimeRange = params.get("TimeRange")
        self._BusinessCode = params.get("BusinessCode")
        self._ProjectId = params.get("ProjectId")
        self._RegionId = params.get("RegionId")
        self._PayMode = params.get("PayMode")
        self._ResourceKeyword = params.get("ResourceKeyword")
        self._BusinessCodes = params.get("BusinessCodes")
        self._ProductCodes = params.get("ProductCodes")
        self._RegionIds = params.get("RegionIds")
        self._ProjectIds = params.get("ProjectIds")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._HideFreeCost = params.get("HideFreeCost")
        self._OrderByCost = params.get("OrderByCost")
        self._BillIds = params.get("BillIds")
        self._ComponentCodes = params.get("ComponentCodes")
        self._FileIds = params.get("FileIds")
        self._FileTypes = params.get("FileTypes")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionBusinessSummaryDataItem(AbstractModel):
    """消耗按产品汇总详情

    """

    def __init__(self):
        r"""
        :param _BusinessCode: 产品名称代码
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        :param _RealTotalCost: 折后总价
        :type RealTotalCost: str
        :param _Trend: 费用趋势
        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        :param _CashPayAmount: 现金
注意：此字段可能返回 null，表示取不到有效值。
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送金
注意：此字段可能返回 null，表示取不到有效值。
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 代金券
注意：此字段可能返回 null，表示取不到有效值。
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._RealTotalCost = None
        self._Trend = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self._Trend = ConsumptionSummaryTrend()
            self._Trend._deserialize(params.get("Trend"))
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionProjectSummaryDataItem(AbstractModel):
    """消耗按项目汇总详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _RealTotalCost: 折后总价
        :type RealTotalCost: str
        :param _Trend: 趋势
        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        :param _Business: 产品消耗详情
        :type Business: list of ConsumptionBusinessSummaryDataItem
        :param _CashPayAmount: 现金
注意：此字段可能返回 null，表示取不到有效值。
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送金
注意：此字段可能返回 null，表示取不到有效值。
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 代金券
注意：此字段可能返回 null，表示取不到有效值。
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._RealTotalCost = None
        self._Trend = None
        self._Business = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self._Trend = ConsumptionSummaryTrend()
            self._Trend._deserialize(params.get("Trend"))
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self._Business.append(obj)
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionRegionSummaryDataItem(AbstractModel):
    """消耗按地域汇总详情

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: str
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _RealTotalCost: 折后总价
        :type RealTotalCost: str
        :param _Trend: 趋势
        :type Trend: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        :param _Business: 产品消费详情
        :type Business: list of ConsumptionBusinessSummaryDataItem
        """
        self._RegionId = None
        self._RegionName = None
        self._RealTotalCost = None
        self._Trend = None
        self._Business = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self._Trend = ConsumptionSummaryTrend()
            self._Trend._deserialize(params.get("Trend"))
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self._Business.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionResourceSummaryConditionValue(AbstractModel):
    """消耗按资源汇总过滤条件

    """

    def __init__(self):
        r"""
        :param _Business: 产品列表
        :type Business: list of ConditionBusiness
        :param _Project: 项目列表
        :type Project: list of ConditionProject
        :param _Region: 地域列表
        :type Region: list of ConditionRegion
        :param _PayMode: 付费模式列表
        :type PayMode: list of ConditionPayMode
        """
        self._Business = None
        self._Project = None
        self._Region = None
        self._PayMode = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = ConditionBusiness()
                obj._deserialize(item)
                self._Business.append(obj)
        if params.get("Project") is not None:
            self._Project = []
            for item in params.get("Project"):
                obj = ConditionProject()
                obj._deserialize(item)
                self._Project.append(obj)
        if params.get("Region") is not None:
            self._Region = []
            for item in params.get("Region"):
                obj = ConditionRegion()
                obj._deserialize(item)
                self._Region.append(obj)
        if params.get("PayMode") is not None:
            self._PayMode = []
            for item in params.get("PayMode"):
                obj = ConditionPayMode()
                obj._deserialize(item)
                self._PayMode.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionResourceSummaryDataItem(AbstractModel):
    """消耗按资源汇总详情

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _ResourceName: 资源名称
        :type ResourceName: str
        :param _RealTotalCost: 折后总价
        :type RealTotalCost: str
        :param _CashPayAmount: 现金花费
        :type CashPayAmount: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _RegionId: 地域ID
        :type RegionId: str
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _PayMode: 付费模式
        :type PayMode: str
        :param _PayModeName: 付费模式名称
        :type PayModeName: str
        :param _BusinessCode: 产品名称代码
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        :param _ConsumptionTypeName: 消耗类型
        :type ConsumptionTypeName: str
        :param _RealCost: 折前价
注意：此字段可能返回 null，表示取不到有效值。
        :type RealCost: str
        :param _FeeBeginTime: 费用起始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeBeginTime: str
        :param _FeeEndTime: 费用结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeEndTime: str
        :param _DayDiff: 天数
注意：此字段可能返回 null，表示取不到有效值。
        :type DayDiff: str
        :param _DailyTotalCost: 每日消耗
注意：此字段可能返回 null，表示取不到有效值。
        :type DailyTotalCost: str
        :param _OrderId: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param _VoucherPayAmount: 代金券
注意：此字段可能返回 null，表示取不到有效值。
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: 赠送金
注意：此字段可能返回 null，表示取不到有效值。
        :type IncentivePayAmount: str
        :param _TransferPayAmount: 分成金
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        """
        self._ResourceId = None
        self._ResourceName = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._ProjectId = None
        self._ProjectName = None
        self._RegionId = None
        self._RegionName = None
        self._PayMode = None
        self._PayModeName = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._ConsumptionTypeName = None
        self._RealCost = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._DayDiff = None
        self._DailyTotalCost = None
        self._OrderId = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ConsumptionTypeName(self):
        return self._ConsumptionTypeName

    @ConsumptionTypeName.setter
    def ConsumptionTypeName(self, ConsumptionTypeName):
        self._ConsumptionTypeName = ConsumptionTypeName

    @property
    def RealCost(self):
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def FeeBeginTime(self):
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def DayDiff(self):
        return self._DayDiff

    @DayDiff.setter
    def DayDiff(self, DayDiff):
        self._DayDiff = DayDiff

    @property
    def DailyTotalCost(self):
        return self._DailyTotalCost

    @DailyTotalCost.setter
    def DailyTotalCost(self, DailyTotalCost):
        self._DailyTotalCost = DailyTotalCost

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ConsumptionTypeName = params.get("ConsumptionTypeName")
        self._RealCost = params.get("RealCost")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        self._DayDiff = params.get("DayDiff")
        self._DailyTotalCost = params.get("DailyTotalCost")
        self._OrderId = params.get("OrderId")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionSummaryTotal(AbstractModel):
    """消耗汇总详情

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: 折后总价
        :type RealTotalCost: str
        """
        self._RealTotalCost = None

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost


    def _deserialize(self, params):
        self._RealTotalCost = params.get("RealTotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionSummaryTrend(AbstractModel):
    """消耗费用趋势

    """

    def __init__(self):
        r"""
        :param _Type: 趋势类型，upward上升/downward下降/none无
        :type Type: str
        :param _Value: 趋势值，Type为none是该字段值为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosDetailSets(AbstractModel):
    """cos产品用量明细返回数据结构

    """

    def __init__(self):
        r"""
        :param _BucketName: 存储桶名称
        :type BucketName: str
        :param _DosageBeginTime: 用量开始时间
        :type DosageBeginTime: str
        :param _DosageEndTime: 用量结束时间
        :type DosageEndTime: str
        :param _SubProductCodeName: 子产品名称
        :type SubProductCodeName: str
        :param _BillingItemCodeName: 计费项名称
        :type BillingItemCodeName: str
        :param _DosageValue: 用量
        :type DosageValue: str
        :param _Unit: 单位
        :type Unit: str
        """
        self._BucketName = None
        self._DosageBeginTime = None
        self._DosageEndTime = None
        self._SubProductCodeName = None
        self._BillingItemCodeName = None
        self._DosageValue = None
        self._Unit = None

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def DosageBeginTime(self):
        return self._DosageBeginTime

    @DosageBeginTime.setter
    def DosageBeginTime(self, DosageBeginTime):
        self._DosageBeginTime = DosageBeginTime

    @property
    def DosageEndTime(self):
        return self._DosageEndTime

    @DosageEndTime.setter
    def DosageEndTime(self, DosageEndTime):
        self._DosageEndTime = DosageEndTime

    @property
    def SubProductCodeName(self):
        return self._SubProductCodeName

    @SubProductCodeName.setter
    def SubProductCodeName(self, SubProductCodeName):
        self._SubProductCodeName = SubProductCodeName

    @property
    def BillingItemCodeName(self):
        return self._BillingItemCodeName

    @BillingItemCodeName.setter
    def BillingItemCodeName(self, BillingItemCodeName):
        self._BillingItemCodeName = BillingItemCodeName

    @property
    def DosageValue(self):
        return self._DosageValue

    @DosageValue.setter
    def DosageValue(self, DosageValue):
        self._DosageValue = DosageValue

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._BucketName = params.get("BucketName")
        self._DosageBeginTime = params.get("DosageBeginTime")
        self._DosageEndTime = params.get("DosageEndTime")
        self._SubProductCodeName = params.get("SubProductCodeName")
        self._BillingItemCodeName = params.get("BillingItemCodeName")
        self._DosageValue = params.get("DosageValue")
        self._Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CostComponentSet(AbstractModel):
    """消耗组件明细

    """

    def __init__(self):
        r"""
        :param _ComponentCodeName: 组件类型名称
        :type ComponentCodeName: str
        :param _ItemCodeName: 组件名称
        :type ItemCodeName: str
        :param _SinglePrice: 刊例价
        :type SinglePrice: str
        :param _PriceUnit: 刊例价单位
        :type PriceUnit: str
        :param _UsedAmount: 用量
        :type UsedAmount: str
        :param _UsedAmountUnit: 用量单位
        :type UsedAmountUnit: str
        :param _Cost: 原价
        :type Cost: str
        :param _Discount: 折扣
        :type Discount: str
        :param _RealCost: 折后价
        :type RealCost: str
        :param _VoucherPayAmount: 代金券支付金额
        :type VoucherPayAmount: str
        :param _CashPayAmount: 现金支付金额
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送金支付金额
        :type IncentivePayAmount: str
        """
        self._ComponentCodeName = None
        self._ItemCodeName = None
        self._SinglePrice = None
        self._PriceUnit = None
        self._UsedAmount = None
        self._UsedAmountUnit = None
        self._Cost = None
        self._Discount = None
        self._RealCost = None
        self._VoucherPayAmount = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None

    @property
    def ComponentCodeName(self):
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def ItemCodeName(self):
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def SinglePrice(self):
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def PriceUnit(self):
        return self._PriceUnit

    @PriceUnit.setter
    def PriceUnit(self, PriceUnit):
        self._PriceUnit = PriceUnit

    @property
    def UsedAmount(self):
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def Cost(self):
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def RealCost(self):
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount


    def _deserialize(self, params):
        self._ComponentCodeName = params.get("ComponentCodeName")
        self._ItemCodeName = params.get("ItemCodeName")
        self._SinglePrice = params.get("SinglePrice")
        self._PriceUnit = params.get("PriceUnit")
        self._UsedAmount = params.get("UsedAmount")
        self._UsedAmountUnit = params.get("UsedAmountUnit")
        self._Cost = params.get("Cost")
        self._Discount = params.get("Discount")
        self._RealCost = params.get("RealCost")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CostDetail(AbstractModel):
    """消耗明细数据类型

    """

    def __init__(self):
        r"""
        :param _PayerUin: 支付者uin
        :type PayerUin: str
        :param _BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        :param _ProductCodeName: 子产品名称
        :type ProductCodeName: str
        :param _PayModeName: 计费模式名称
        :type PayModeName: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _RegionName: 区域名称
        :type RegionName: str
        :param _ZoneName: 地区名称
        :type ZoneName: str
        :param _ResourceId: 资源id
        :type ResourceId: str
        :param _ResourceName: 资源名称
        :type ResourceName: str
        :param _ActionTypeName: 类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionTypeName: str
        :param _OrderId: 订单id
        :type OrderId: str
        :param _BillId: 交易id
        :type BillId: str
        :param _FeeBeginTime: 费用开始时间
        :type FeeBeginTime: str
        :param _FeeEndTime: 费用结束时间
        :type FeeEndTime: str
        :param _ComponentSet: 组件明细
        :type ComponentSet: list of CostComponentSet
        :param _ProductCode: 子产品名称代码
        :type ProductCode: str
        """
        self._PayerUin = None
        self._BusinessCodeName = None
        self._ProductCodeName = None
        self._PayModeName = None
        self._ProjectName = None
        self._RegionName = None
        self._ZoneName = None
        self._ResourceId = None
        self._ResourceName = None
        self._ActionTypeName = None
        self._OrderId = None
        self._BillId = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._ComponentSet = None
        self._ProductCode = None

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def BusinessCodeName(self):
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def FeeBeginTime(self):
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentSet(self):
        return self._ComponentSet

    @ComponentSet.setter
    def ComponentSet(self, ComponentSet):
        self._ComponentSet = ComponentSet

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode


    def _deserialize(self, params):
        self._PayerUin = params.get("PayerUin")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCodeName = params.get("ProductCodeName")
        self._PayModeName = params.get("PayModeName")
        self._ProjectName = params.get("ProjectName")
        self._RegionName = params.get("RegionName")
        self._ZoneName = params.get("ZoneName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._ActionTypeName = params.get("ActionTypeName")
        self._OrderId = params.get("OrderId")
        self._BillId = params.get("BillId")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        if params.get("ComponentSet") is not None:
            self._ComponentSet = []
            for item in params.get("ComponentSet"):
                obj = CostComponentSet()
                obj._deserialize(item)
                self._ComponentSet.append(obj)
        self._ProductCode = params.get("ProductCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Deal(AbstractModel):
    """订单数据对象

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单号
        :type OrderId: str
        :param _Status: 订单的状态 1：未支付 2：已支付3：发货中 4：已发货 5：发货失败 6：已退款 7：已关单 8：订单过期 9：订单已失效 10：产品已失效 11：代付拒绝 12：支付中
        :type Status: int
        :param _Payer: 支付者
        :type Payer: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Creator: 创建人
        :type Creator: str
        :param _RealTotalCost: 实际支付金额（分）
        :type RealTotalCost: int
        :param _VoucherDecline: 代金券抵扣金额（分）
        :type VoucherDecline: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _GoodsCategoryId: 产品分类ID
        :type GoodsCategoryId: int
        :param _ProductInfo: 产品详情
        :type ProductInfo: list of ProductInfo
        :param _TimeSpan: 时长
        :type TimeSpan: float
        :param _TimeUnit: 时间单位
        :type TimeUnit: str
        :param _Currency: 货币单位
        :type Currency: str
        :param _Policy: 折扣率
        :type Policy: float
        :param _Price: 单价（分）
        :type Price: float
        :param _TotalCost: 原价（分）
        :type TotalCost: float
        :param _ProductCode: 产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param _SubProductCode: 子产品编码
        :type SubProductCode: str
        :param _BigDealId: 大订单号
        :type BigDealId: str
        :param _Formula: 退费公式
注意：此字段可能返回 null，表示取不到有效值。
        :type Formula: str
        :param _RefReturnDeals: 退费涉及订单信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RefReturnDeals: str
        :param _PayMode: 付费模式：prePay 预付费 postPay后付费 riPay预留实例
        :type PayMode: str
        :param _Action: 交易类型
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
        :param _ProductName: 产品编码中文名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _SubProductName: 子产品编码中文名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProductName: str
        :param _ResourceId: 订单对应的资源id, 查询参数Limit超过200，将返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: list of str
        """
        self._OrderId = None
        self._Status = None
        self._Payer = None
        self._CreateTime = None
        self._Creator = None
        self._RealTotalCost = None
        self._VoucherDecline = None
        self._ProjectId = None
        self._GoodsCategoryId = None
        self._ProductInfo = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._Currency = None
        self._Policy = None
        self._Price = None
        self._TotalCost = None
        self._ProductCode = None
        self._SubProductCode = None
        self._BigDealId = None
        self._Formula = None
        self._RefReturnDeals = None
        self._PayMode = None
        self._Action = None
        self._ProductName = None
        self._SubProductName = None
        self._ResourceId = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Payer(self):
        return self._Payer

    @Payer.setter
    def Payer(self, Payer):
        self._Payer = Payer

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherDecline(self):
        return self._VoucherDecline

    @VoucherDecline.setter
    def VoucherDecline(self, VoucherDecline):
        self._VoucherDecline = VoucherDecline

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsCategoryId(self):
        return self._GoodsCategoryId

    @GoodsCategoryId.setter
    def GoodsCategoryId(self, GoodsCategoryId):
        self._GoodsCategoryId = GoodsCategoryId

    @property
    def ProductInfo(self):
        return self._ProductInfo

    @ProductInfo.setter
    def ProductInfo(self, ProductInfo):
        self._ProductInfo = ProductInfo

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def BigDealId(self):
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def Formula(self):
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def RefReturnDeals(self):
        return self._RefReturnDeals

    @RefReturnDeals.setter
    def RefReturnDeals(self, RefReturnDeals):
        self._RefReturnDeals = RefReturnDeals

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductName(self):
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._Status = params.get("Status")
        self._Payer = params.get("Payer")
        self._CreateTime = params.get("CreateTime")
        self._Creator = params.get("Creator")
        self._RealTotalCost = params.get("RealTotalCost")
        self._VoucherDecline = params.get("VoucherDecline")
        self._ProjectId = params.get("ProjectId")
        self._GoodsCategoryId = params.get("GoodsCategoryId")
        if params.get("ProductInfo") is not None:
            self._ProductInfo = []
            for item in params.get("ProductInfo"):
                obj = ProductInfo()
                obj._deserialize(item)
                self._ProductInfo.append(obj)
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._Currency = params.get("Currency")
        self._Policy = params.get("Policy")
        self._Price = params.get("Price")
        self._TotalCost = params.get("TotalCost")
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._BigDealId = params.get("BigDealId")
        self._Formula = params.get("Formula")
        self._RefReturnDeals = params.get("RefReturnDeals")
        self._PayMode = params.get("PayMode")
        self._Action = params.get("Action")
        self._ProductName = params.get("ProductName")
        self._SubProductName = params.get("SubProductName")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
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
        :param _Balance: 接口做过变更,为兼容老接口,本字段与RealBalance相同,为当前真实可用余额,单位 分
        :type Balance: int
        :param _Uin: 查询的用户Uin
        :type Uin: int
        :param _RealBalance: 当前真实可用余额,单位 分
        :type RealBalance: float
        :param _CashAccountBalance: 现金账户余额,单位 分
        :type CashAccountBalance: float
        :param _IncomeIntoAccountBalance: 收益转入账户余额,单位 分
        :type IncomeIntoAccountBalance: float
        :param _PresentAccountBalance: 赠送账户余额,单位 分
        :type PresentAccountBalance: float
        :param _FreezeAmount: 冻结金额,单位 分
        :type FreezeAmount: float
        :param _OweAmount: 欠费金额,单位 分
        :type OweAmount: float
        :param _IsAllowArrears: 是否允许欠费消费
        :type IsAllowArrears: bool
        :param _IsCreditLimited: 是否限制信用额度
        :type IsCreditLimited: bool
        :param _CreditAmount: 信用额度
        :type CreditAmount: float
        :param _CreditBalance: 可用信用额度
        :type CreditBalance: float
        :param _RealCreditBalance: 真实可用信用额度
        :type RealCreditBalance: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Balance = None
        self._Uin = None
        self._RealBalance = None
        self._CashAccountBalance = None
        self._IncomeIntoAccountBalance = None
        self._PresentAccountBalance = None
        self._FreezeAmount = None
        self._OweAmount = None
        self._IsAllowArrears = None
        self._IsCreditLimited = None
        self._CreditAmount = None
        self._CreditBalance = None
        self._RealCreditBalance = None
        self._RequestId = None

    @property
    def Balance(self):
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RealBalance(self):
        return self._RealBalance

    @RealBalance.setter
    def RealBalance(self, RealBalance):
        self._RealBalance = RealBalance

    @property
    def CashAccountBalance(self):
        return self._CashAccountBalance

    @CashAccountBalance.setter
    def CashAccountBalance(self, CashAccountBalance):
        self._CashAccountBalance = CashAccountBalance

    @property
    def IncomeIntoAccountBalance(self):
        return self._IncomeIntoAccountBalance

    @IncomeIntoAccountBalance.setter
    def IncomeIntoAccountBalance(self, IncomeIntoAccountBalance):
        self._IncomeIntoAccountBalance = IncomeIntoAccountBalance

    @property
    def PresentAccountBalance(self):
        return self._PresentAccountBalance

    @PresentAccountBalance.setter
    def PresentAccountBalance(self, PresentAccountBalance):
        self._PresentAccountBalance = PresentAccountBalance

    @property
    def FreezeAmount(self):
        return self._FreezeAmount

    @FreezeAmount.setter
    def FreezeAmount(self, FreezeAmount):
        self._FreezeAmount = FreezeAmount

    @property
    def OweAmount(self):
        return self._OweAmount

    @OweAmount.setter
    def OweAmount(self, OweAmount):
        self._OweAmount = OweAmount

    @property
    def IsAllowArrears(self):
        return self._IsAllowArrears

    @IsAllowArrears.setter
    def IsAllowArrears(self, IsAllowArrears):
        self._IsAllowArrears = IsAllowArrears

    @property
    def IsCreditLimited(self):
        return self._IsCreditLimited

    @IsCreditLimited.setter
    def IsCreditLimited(self, IsCreditLimited):
        self._IsCreditLimited = IsCreditLimited

    @property
    def CreditAmount(self):
        return self._CreditAmount

    @CreditAmount.setter
    def CreditAmount(self, CreditAmount):
        self._CreditAmount = CreditAmount

    @property
    def CreditBalance(self):
        return self._CreditBalance

    @CreditBalance.setter
    def CreditBalance(self, CreditBalance):
        self._CreditBalance = CreditBalance

    @property
    def RealCreditBalance(self):
        return self._RealCreditBalance

    @RealCreditBalance.setter
    def RealCreditBalance(self, RealCreditBalance):
        self._RealCreditBalance = RealCreditBalance

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Balance = params.get("Balance")
        self._Uin = params.get("Uin")
        self._RealBalance = params.get("RealBalance")
        self._CashAccountBalance = params.get("CashAccountBalance")
        self._IncomeIntoAccountBalance = params.get("IncomeIntoAccountBalance")
        self._PresentAccountBalance = params.get("PresentAccountBalance")
        self._FreezeAmount = params.get("FreezeAmount")
        self._OweAmount = params.get("OweAmount")
        self._IsAllowArrears = params.get("IsAllowArrears")
        self._IsCreditLimited = params.get("IsCreditLimited")
        self._CreditAmount = params.get("CreditAmount")
        self._CreditBalance = params.get("CreditBalance")
        self._RealCreditBalance = params.get("RealCreditBalance")
        self._RequestId = params.get("RequestId")


class DescribeBillDetailRequest(AbstractModel):
    """DescribeBillDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :type Offset: int
        :param _Limit: 数量，最大值为100
        :type Limit: int
        :param _PeriodType: 周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :type PeriodType: str
        :param _Month: 月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通账单2.0的月份，最多可拉取18个月内的数据。
        :type Month: str
        :param _BeginTime: 周期开始时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取18个月内的数据。(不支持跨月查询)
        :type BeginTime: str
        :param _EndTime: 周期结束时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取18个月内的数据。（不支持跨月查询）
        :type EndTime: str
        :param _NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param _ProductCode: 已废弃参数，未开放
        :type ProductCode: str
        :param _PayMode: 付费模式 prePay/postPay
        :type PayMode: str
        :param _ResourceId: 查询指定资源信息
        :type ResourceId: str
        :param _ActionType: 查询交易类型（请使用交易类型名称入参），入参示例枚举如下：
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
        :param _ProjectId: 项目ID:资源所属项目ID
        :type ProjectId: int
        :param _BusinessCode: 产品名称代码
备注：如需获取当月使用过的BusinessCode，请调用API：<a href="https://cloud.tencent.com/document/product/555/35761">获取产品汇总费用分布</a>
        :type BusinessCode: str
        :param _Context: 上一次请求返回的上下文信息，翻页查询Month>=2023-05的月份的数据可加快查询速度，数据量10万级别以上的用户建议使用，查询速度可提升2~10倍
        :type Context: str
        :param _PayerUin: 支付者的账号 ID（账号 ID 是用户在腾讯云的唯一账号标识），默认查询本账号账单，如集团管理账号需查询成员账号自付的账单，该字段需入参成员账号UIN
        :type PayerUin: str
        """
        self._Offset = None
        self._Limit = None
        self._PeriodType = None
        self._Month = None
        self._BeginTime = None
        self._EndTime = None
        self._NeedRecordNum = None
        self._ProductCode = None
        self._PayMode = None
        self._ResourceId = None
        self._ActionType = None
        self._ProjectId = None
        self._BusinessCode = None
        self._Context = None
        self._PayerUin = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PeriodType(self):
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PeriodType = params.get("PeriodType")
        self._Month = params.get("Month")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._NeedRecordNum = params.get("NeedRecordNum")
        self._ProductCode = params.get("ProductCode")
        self._PayMode = params.get("PayMode")
        self._ResourceId = params.get("ResourceId")
        self._ActionType = params.get("ActionType")
        self._ProjectId = params.get("ProjectId")
        self._BusinessCode = params.get("BusinessCode")
        self._Context = params.get("Context")
        self._PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillDetailResponse(AbstractModel):
    """DescribeBillDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetailSet: 详情列表
        :type DetailSet: list of BillDetail
        :param _Total: 总记录数，24小时缓存一次，可能比实际总记录数少
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Context: 本次请求的上下文信息，可用于下一次请求的请求参数中，加快查询速度
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailSet = None
        self._Total = None
        self._Context = None
        self._RequestId = None

    @property
    def DetailSet(self):
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = BillDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        self._Total = params.get("Total")
        self._Context = params.get("Context")
        self._RequestId = params.get("RequestId")


class DescribeBillListRequest(AbstractModel):
    """DescribeBillList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询范围的起始时间（包含）时间格式 yyyy-MM-dd HH:mm:ss 开始时间和结束时间差值小于等于六个月
        :type StartTime: str
        :param _EndTime: 查询范围的结束时间（包含）时间格式 yyyy-MM-dd HH:mm:ss ，开始时间和结束时间差值小于等于六个月
        :type EndTime: str
        :param _Offset: 翻页偏移量，初始值为0
        :type Offset: int
        :param _Limit: 每页的限制数量
        :type Limit: int
        :param _PayType: 交易类型： all所有交易类型，recharge充值，return退款，unblock解冻，agentin资金转入，advanced垫付，cash提现，deduct扣费，block冻结，agentout资金转出，repay垫付回款，repayment还款(仅国际信用账户)，adj_refund调增(仅国际信用账户)，adj_deduct调减(仅国际信用账户)
        :type PayType: list of str
        :param _SubPayType: 扣费模式，
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
        :param _WithZeroAmount: 是否返回0元交易金额的交易项，取值：0-不返回，1-返回。不传该参数则不返回
        :type WithZeroAmount: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._PayType = None
        self._SubPayType = None
        self._WithZeroAmount = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def SubPayType(self):
        return self._SubPayType

    @SubPayType.setter
    def SubPayType(self, SubPayType):
        self._SubPayType = SubPayType

    @property
    def WithZeroAmount(self):
        return self._WithZeroAmount

    @WithZeroAmount.setter
    def WithZeroAmount(self, WithZeroAmount):
        self._WithZeroAmount = WithZeroAmount


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PayType = params.get("PayType")
        self._SubPayType = params.get("SubPayType")
        self._WithZeroAmount = params.get("WithZeroAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillListResponse(AbstractModel):
    """DescribeBillList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TransactionList: 收支明细列表
        :type TransactionList: list of BillTransactionInfo
        :param _Total: 总条数
        :type Total: int
        :param _ReturnAmount: 退费总额，单位（分）
        :type ReturnAmount: float
        :param _RechargeAmount: 充值总额，单位（分）
        :type RechargeAmount: float
        :param _BlockAmount: 冻结总额，单位（分）
        :type BlockAmount: float
        :param _UnblockAmount: 解冻总额，单位（分）
        :type UnblockAmount: float
        :param _DeductAmount: 扣费总额，单位（分）
        :type DeductAmount: float
        :param _AgentInAmount: 资金转入总额，单位（分）
        :type AgentInAmount: float
        :param _AdvanceRechargeAmount: 垫付充值总额，单位（分）
        :type AdvanceRechargeAmount: float
        :param _WithdrawAmount: 提现扣减总额，单位（分）
        :type WithdrawAmount: float
        :param _AgentOutAmount: 资金转出总额，单位（分）
        :type AgentOutAmount: float
        :param _AdvancePayAmount: 还垫付总额，单位（分）
        :type AdvancePayAmount: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TransactionList = None
        self._Total = None
        self._ReturnAmount = None
        self._RechargeAmount = None
        self._BlockAmount = None
        self._UnblockAmount = None
        self._DeductAmount = None
        self._AgentInAmount = None
        self._AdvanceRechargeAmount = None
        self._WithdrawAmount = None
        self._AgentOutAmount = None
        self._AdvancePayAmount = None
        self._RequestId = None

    @property
    def TransactionList(self):
        return self._TransactionList

    @TransactionList.setter
    def TransactionList(self, TransactionList):
        self._TransactionList = TransactionList

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ReturnAmount(self):
        return self._ReturnAmount

    @ReturnAmount.setter
    def ReturnAmount(self, ReturnAmount):
        self._ReturnAmount = ReturnAmount

    @property
    def RechargeAmount(self):
        return self._RechargeAmount

    @RechargeAmount.setter
    def RechargeAmount(self, RechargeAmount):
        self._RechargeAmount = RechargeAmount

    @property
    def BlockAmount(self):
        return self._BlockAmount

    @BlockAmount.setter
    def BlockAmount(self, BlockAmount):
        self._BlockAmount = BlockAmount

    @property
    def UnblockAmount(self):
        return self._UnblockAmount

    @UnblockAmount.setter
    def UnblockAmount(self, UnblockAmount):
        self._UnblockAmount = UnblockAmount

    @property
    def DeductAmount(self):
        return self._DeductAmount

    @DeductAmount.setter
    def DeductAmount(self, DeductAmount):
        self._DeductAmount = DeductAmount

    @property
    def AgentInAmount(self):
        return self._AgentInAmount

    @AgentInAmount.setter
    def AgentInAmount(self, AgentInAmount):
        self._AgentInAmount = AgentInAmount

    @property
    def AdvanceRechargeAmount(self):
        return self._AdvanceRechargeAmount

    @AdvanceRechargeAmount.setter
    def AdvanceRechargeAmount(self, AdvanceRechargeAmount):
        self._AdvanceRechargeAmount = AdvanceRechargeAmount

    @property
    def WithdrawAmount(self):
        return self._WithdrawAmount

    @WithdrawAmount.setter
    def WithdrawAmount(self, WithdrawAmount):
        self._WithdrawAmount = WithdrawAmount

    @property
    def AgentOutAmount(self):
        return self._AgentOutAmount

    @AgentOutAmount.setter
    def AgentOutAmount(self, AgentOutAmount):
        self._AgentOutAmount = AgentOutAmount

    @property
    def AdvancePayAmount(self):
        return self._AdvancePayAmount

    @AdvancePayAmount.setter
    def AdvancePayAmount(self, AdvancePayAmount):
        self._AdvancePayAmount = AdvancePayAmount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TransactionList") is not None:
            self._TransactionList = []
            for item in params.get("TransactionList"):
                obj = BillTransactionInfo()
                obj._deserialize(item)
                self._TransactionList.append(obj)
        self._Total = params.get("Total")
        self._ReturnAmount = params.get("ReturnAmount")
        self._RechargeAmount = params.get("RechargeAmount")
        self._BlockAmount = params.get("BlockAmount")
        self._UnblockAmount = params.get("UnblockAmount")
        self._DeductAmount = params.get("DeductAmount")
        self._AgentInAmount = params.get("AgentInAmount")
        self._AdvanceRechargeAmount = params.get("AdvanceRechargeAmount")
        self._WithdrawAmount = params.get("WithdrawAmount")
        self._AgentOutAmount = params.get("AgentOutAmount")
        self._AdvancePayAmount = params.get("AdvancePayAmount")
        self._RequestId = params.get("RequestId")


class DescribeBillResourceSummaryRequest(AbstractModel):
    """DescribeBillResourceSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :type Offset: int
        :param _Limit: 数量，最大值为1000
        :type Limit: int
        :param _Month: 月份，格式为yyyy-mm。不能早于开通账单2.0的月份
        :type Month: str
        :param _PeriodType: 周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :type PeriodType: str
        :param _NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param _ActionType: 查询交易类型（请使用交易类型名称入参），入参示例枚举如下：
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
        :param _ResourceId: 查询指定资源信息
        :type ResourceId: str
        :param _PayMode: 付费模式 prePay/postPay
        :type PayMode: str
        :param _BusinessCode: 产品名称代码
备注：如需获取当月使用过的BusinessCode，请调用API：<a href="https://cloud.tencent.com/document/product/555/35761">获取产品汇总费用分布</a>
        :type BusinessCode: str
        :param _PayerUin: 支付者的账号 ID（账号 ID 是用户在腾讯云的唯一账号标识），默认查询本账号账单，如集团管理账号需查询成员账号自付的账单，该字段需入参成员账号UIN
        :type PayerUin: str
        """
        self._Offset = None
        self._Limit = None
        self._Month = None
        self._PeriodType = None
        self._NeedRecordNum = None
        self._ActionType = None
        self._ResourceId = None
        self._PayMode = None
        self._BusinessCode = None
        self._PayerUin = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Month = params.get("Month")
        self._PeriodType = params.get("PeriodType")
        self._NeedRecordNum = params.get("NeedRecordNum")
        self._ActionType = params.get("ActionType")
        self._ResourceId = params.get("ResourceId")
        self._PayMode = params.get("PayMode")
        self._BusinessCode = params.get("BusinessCode")
        self._PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillResourceSummaryResponse(AbstractModel):
    """DescribeBillResourceSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceSummarySet: 资源汇总列表
        :type ResourceSummarySet: list of BillResourceSummary
        :param _Total: 资源汇总列表总数，入参NeedRecordNum为0时不返回
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceSummarySet = None
        self._Total = None
        self._RequestId = None

    @property
    def ResourceSummarySet(self):
        return self._ResourceSummarySet

    @ResourceSummarySet.setter
    def ResourceSummarySet(self, ResourceSummarySet):
        self._ResourceSummarySet = ResourceSummarySet

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResourceSummarySet") is not None:
            self._ResourceSummarySet = []
            for item in params.get("ResourceSummarySet"):
                obj = BillResourceSummary()
                obj._deserialize(item)
                self._ResourceSummarySet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByPayModeRequest(AbstractModel):
    """DescribeBillSummaryByPayMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param _EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param _PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._PayerUin = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByPayModeResponse(AbstractModel):
    """DescribeBillSummaryByPayMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :type Ready: int
        :param _SummaryOverview: 各付费模式花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of PayModeSummaryOverviewItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = PayModeSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByProductRequest(AbstractModel):
    """DescribeBillSummaryByProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param _EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param _PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param _PayType: 款项类别，与L0账单上的汇总类别对应。
此参数自账单3.0（即2021-05）之后开始生效。
枚举值：
consume-消费
refund-退款
adjustment-调账
        :type PayType: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._PayerUin = None
        self._PayType = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._PayerUin = params.get("PayerUin")
        self._PayType = params.get("PayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByProductResponse(AbstractModel):
    """DescribeBillSummaryByProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :type Ready: int
        :param _SummaryTotal: 总花费详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryTotal: :class:`tencentcloud.billing.v20180709.models.BusinessSummaryTotal`
        :param _SummaryOverview: 各产品花费分布
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of BusinessSummaryOverviewItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryTotal = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryTotal(self):
        return self._SummaryTotal

    @SummaryTotal.setter
    def SummaryTotal(self, SummaryTotal):
        self._SummaryTotal = SummaryTotal

    @property
    def SummaryOverview(self):
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryTotal") is not None:
            self._SummaryTotal = BusinessSummaryTotal()
            self._SummaryTotal._deserialize(params.get("SummaryTotal"))
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = BusinessSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByProjectRequest(AbstractModel):
    """DescribeBillSummaryByProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param _EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param _PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._PayerUin = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByProjectResponse(AbstractModel):
    """DescribeBillSummaryByProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :type Ready: int
        :param _SummaryOverview: 各项目花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of ProjectSummaryOverviewItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = ProjectSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByRegionRequest(AbstractModel):
    """DescribeBillSummaryByRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param _EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param _PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._PayerUin = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._PayerUin = params.get("PayerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByRegionResponse(AbstractModel):
    """DescribeBillSummaryByRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :type Ready: int
        :param _SummaryOverview: 各地域花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of RegionSummaryOverviewItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = RegionSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryByTagRequest(AbstractModel):
    """DescribeBillSummaryByTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param _EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param _TagKey: 分账标签键，用户自定义
        :type TagKey: str
        :param _PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param _TagValue: 分账标签值
        :type TagValue: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._TagKey = None
        self._PayerUin = None
        self._TagValue = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._TagKey = params.get("TagKey")
        self._PayerUin = params.get("PayerUin")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryByTagResponse(AbstractModel):
    """DescribeBillSummaryByTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :type Ready: int
        :param _SummaryOverview: 各标签值花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of TagSummaryOverviewItem
        :param _SummaryTotal: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryTotal: :class:`tencentcloud.billing.v20180709.models.SummaryTotal`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._SummaryTotal = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def SummaryTotal(self):
        return self._SummaryTotal

    @SummaryTotal.setter
    def SummaryTotal(self, SummaryTotal):
        self._SummaryTotal = SummaryTotal

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self._SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = TagSummaryOverviewItem()
                obj._deserialize(item)
                self._SummaryOverview.append(obj)
        if params.get("SummaryTotal") is not None:
            self._SummaryTotal = SummaryTotal()
            self._SummaryTotal._deserialize(params.get("SummaryTotal"))
        self._RequestId = params.get("RequestId")


class DescribeBillSummaryRequest(AbstractModel):
    """DescribeBillSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Month: 账单月份，格式为2023-04
        :type Month: str
        :param _GroupType: 账单维度类型，枚举值如下：business、project、region、payMode、tag
        :type GroupType: str
        :param _TagKey: 标签键，GroupType=tag获取标签维度账单时传
        :type TagKey: list of str
        """
        self._Month = None
        self._GroupType = None
        self._TagKey = None

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._GroupType = params.get("GroupType")
        self._TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillSummaryResponse(AbstractModel):
    """DescribeBillSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :type Ready: int
        :param _SummaryDetail: 账单多维度汇总消费详情
        :type SummaryDetail: list of SummaryDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryDetail = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryDetail(self):
        return self._SummaryDetail

    @SummaryDetail.setter
    def SummaryDetail(self, SummaryDetail):
        self._SummaryDetail = SummaryDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("SummaryDetail") is not None:
            self._SummaryDetail = []
            for item in params.get("SummaryDetail"):
                obj = SummaryDetail()
                obj._deserialize(item)
                self._SummaryDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCostDetailRequest(AbstractModel):
    """DescribeCostDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量，最大值为100
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _BeginTime: 周期开始时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为同一月份，暂不支持跨月拉取。可拉取的数据是开通成本分析后，且距今 24 个月内的数据。
        :type BeginTime: str
        :param _EndTime: 周期结束时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为同一月份，暂不支持跨月拉取。可拉取的数据是开通成本分析后，且距今 24 个月内的数据。
        :type EndTime: str
        :param _NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param _Month: 月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通成本分析的月份，最多可拉取24个月内的数据。
        :type Month: str
        :param _ProductCode: 查询指定产品信息（暂时未开放获取）
        :type ProductCode: str
        :param _PayMode: 付费模式 prePay/postPay
        :type PayMode: str
        :param _ResourceId: 查询指定资源信息
        :type ResourceId: str
        """
        self._Limit = None
        self._Offset = None
        self._BeginTime = None
        self._EndTime = None
        self._NeedRecordNum = None
        self._Month = None
        self._ProductCode = None
        self._PayMode = None
        self._ResourceId = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._NeedRecordNum = params.get("NeedRecordNum")
        self._Month = params.get("Month")
        self._ProductCode = params.get("ProductCode")
        self._PayMode = params.get("PayMode")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostDetailResponse(AbstractModel):
    """DescribeCostDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetailSet: 消耗明细
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailSet: list of CostDetail
        :param _Total: 记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailSet = None
        self._Total = None
        self._RequestId = None

    @property
    def DetailSet(self):
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = CostDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCostSummaryByProductRequest(AbstractModel):
    """DescribeCostSummaryByProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param _EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param _Limit: 每次获取数据量，最大值为100
        :type Limit: int
        :param _Offset: 偏移量,默认从0开始
        :type Offset: int
        :param _PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param _NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._PayerUin = None
        self._NeedRecordNum = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._PayerUin = params.get("PayerUin")
        self._NeedRecordNum = params.get("NeedRecordNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByProductResponse(AbstractModel):
    """DescribeCostSummaryByProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param _Total: 消耗详情
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _Data: 消耗按产品汇总详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ConsumptionBusinessSummaryDataItem
        :param _RecordNum: 记录数量，NeedRecordNum为0是返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._Total = None
        self._Data = None
        self._RecordNum = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("Total") is not None:
            self._Total = ConsumptionSummaryTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RecordNum = params.get("RecordNum")
        self._RequestId = params.get("RequestId")


class DescribeCostSummaryByProjectRequest(AbstractModel):
    """DescribeCostSummaryByProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param _EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param _Limit: 每次获取数据量，最大值为100
        :type Limit: int
        :param _Offset: 偏移量,默认从0开始
        :type Offset: int
        :param _PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param _NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._PayerUin = None
        self._NeedRecordNum = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._PayerUin = params.get("PayerUin")
        self._NeedRecordNum = params.get("NeedRecordNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByProjectResponse(AbstractModel):
    """DescribeCostSummaryByProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param _Total: 消耗详情
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _Data: 消耗按业务汇总详情
        :type Data: list of ConsumptionProjectSummaryDataItem
        :param _RecordNum: 记录数量，NeedRecordNum为0是返回null
        :type RecordNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._Total = None
        self._Data = None
        self._RecordNum = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("Total") is not None:
            self._Total = ConsumptionSummaryTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ConsumptionProjectSummaryDataItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RecordNum = params.get("RecordNum")
        self._RequestId = params.get("RequestId")


class DescribeCostSummaryByRegionRequest(AbstractModel):
    """DescribeCostSummaryByRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param _EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param _Limit: 每次获取数据量，最大值为100
        :type Limit: int
        :param _Offset: 偏移量,默认从0开始
        :type Offset: int
        :param _PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param _NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._PayerUin = None
        self._NeedRecordNum = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._PayerUin = params.get("PayerUin")
        self._NeedRecordNum = params.get("NeedRecordNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByRegionResponse(AbstractModel):
    """DescribeCostSummaryByRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param _Total: 消耗详情
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _Data: 消耗按地域汇总详情
        :type Data: list of ConsumptionRegionSummaryDataItem
        :param _RecordNum: 记录数量，NeedRecordNum为0是返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._Total = None
        self._Data = None
        self._RecordNum = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("Total") is not None:
            self._Total = ConsumptionSummaryTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ConsumptionRegionSummaryDataItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RecordNum = params.get("RecordNum")
        self._RequestId = params.get("RequestId")


class DescribeCostSummaryByResourceRequest(AbstractModel):
    """DescribeCostSummaryByResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type BeginTime: str
        :param _EndTime: 目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :type EndTime: str
        :param _Limit: 每次获取数据量，最大值为100
        :type Limit: int
        :param _Offset: 偏移量,默认从0开始
        :type Offset: int
        :param _PayerUin: 查询账单数据的用户UIN
        :type PayerUin: str
        :param _NeedRecordNum: 是否需要返回记录数量，0不需要，1需要，默认不需要
        :type NeedRecordNum: int
        :param _NeedConditionValue: 是否需要返回过滤条件，0不需要，1需要，默认不需要
        :type NeedConditionValue: int
        :param _Conditions: 过滤条件，只支持ResourceKeyword(资源关键字，支持资源id及资源名称模糊查询)，ProjectIds（项目id），RegionIds(地域id)，PayModes(付费模式，可选prePay和postPay)，HideFreeCost（是否隐藏0元流水，可选0和1），OrderByCost（按费用排序规则，可选desc和asc）
        :type Conditions: :class:`tencentcloud.billing.v20180709.models.Conditions`
        """
        self._BeginTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._PayerUin = None
        self._NeedRecordNum = None
        self._NeedConditionValue = None
        self._Conditions = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def NeedConditionValue(self):
        return self._NeedConditionValue

    @NeedConditionValue.setter
    def NeedConditionValue(self, NeedConditionValue):
        self._NeedConditionValue = NeedConditionValue

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._PayerUin = params.get("PayerUin")
        self._NeedRecordNum = params.get("NeedRecordNum")
        self._NeedConditionValue = params.get("NeedConditionValue")
        if params.get("Conditions") is not None:
            self._Conditions = Conditions()
            self._Conditions._deserialize(params.get("Conditions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostSummaryByResourceResponse(AbstractModel):
    """DescribeCostSummaryByResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 数据是否准备好，0未准备好，1准备好
        :type Ready: int
        :param _Total: 消耗详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _ConditionValue: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionValue: :class:`tencentcloud.billing.v20180709.models.ConsumptionResourceSummaryConditionValue`
        :param _RecordNum: 记录数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordNum: int
        :param _Data: 资源消耗详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ConsumptionResourceSummaryDataItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._Total = None
        self._ConditionValue = None
        self._RecordNum = None
        self._Data = None
        self._RequestId = None

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConditionValue(self):
        return self._ConditionValue

    @ConditionValue.setter
    def ConditionValue(self, ConditionValue):
        self._ConditionValue = ConditionValue

    @property
    def RecordNum(self):
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ready = params.get("Ready")
        if params.get("Total") is not None:
            self._Total = ConsumptionSummaryTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("ConditionValue") is not None:
            self._ConditionValue = ConsumptionResourceSummaryConditionValue()
            self._ConditionValue._deserialize(params.get("ConditionValue"))
        self._RecordNum = params.get("RecordNum")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ConsumptionResourceSummaryDataItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDealsByCondRequest(AbstractModel):
    """DescribeDealsByCond请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间 2016-01-01 00:00:00
        :type StartTime: str
        :param _EndTime: 结束时间 2016-02-01 00:00:00 建议跨度不超过3个月
        :type EndTime: str
        :param _Limit: 一页多少条数据，默认是20条，最大不超过1000
        :type Limit: int
        :param _Offset: 第多少页，从0开始，默认是0
        :type Offset: int
        :param _Status: 订单状态,默认为4（成功的订单）
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
        :param _OrderId: 订单号
        :type OrderId: str
        :param _BigDealId: 大订单号
        :type BigDealId: str
        :param _ResourceId: 资源id
        :type ResourceId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._OrderId = None
        self._BigDealId = None
        self._ResourceId = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BigDealId(self):
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._OrderId = params.get("OrderId")
        self._BigDealId = params.get("BigDealId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDealsByCondResponse(AbstractModel):
    """DescribeDealsByCond返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Deals: 订单列表
        :type Deals: list of Deal
        :param _TotalCount: 订单总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Deals = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Deals(self):
        return self._Deals

    @Deals.setter
    def Deals(self, Deals):
        self._Deals = Deals

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Deals") is not None:
            self._Deals = []
            for item in params.get("Deals"):
                obj = Deal()
                obj._deserialize(item)
                self._Deals.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDosageCosDetailByDateRequest(AbstractModel):
    """DescribeDosageCosDetailByDate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDate: 查询用量开始时间，例如：2020-09-01
        :type StartDate: str
        :param _EndDate: 查询用量结束时间，例如：2020-09-30（与开始时间同月，不支持跨月查询）
        :type EndDate: str
        :param _BucketName: COS 存储桶名称，可通过Get Service 接口是用来获取请求者名下的所有存储空间列表（Bucket list）https://cloud.tencent.com/document/product/436/8291
        :type BucketName: str
        """
        self._StartDate = None
        self._EndDate = None
        self._BucketName = None

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._BucketName = params.get("BucketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDosageCosDetailByDateResponse(AbstractModel):
    """DescribeDosageCosDetailByDate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetailSets: 用量数组
        :type DetailSets: list of CosDetailSets
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailSets = None
        self._RequestId = None

    @property
    def DetailSets(self):
        return self._DetailSets

    @DetailSets.setter
    def DetailSets(self, DetailSets):
        self._DetailSets = DetailSets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailSets") is not None:
            self._DetailSets = []
            for item in params.get("DetailSets"):
                obj = CosDetailSets()
                obj._deserialize(item)
                self._DetailSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDosageDetailByDateRequest(AbstractModel):
    """DescribeDosageDetailByDate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDate: 查询账单开始日期，如 2019-01-01
        :type StartDate: str
        :param _EndDate: 查询账单结束日期，如 2019-01-01， 时间跨度不超过7天
        :type EndDate: str
        :param _ProductCode: 互动直播：
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
        :param _Domain: 查询域名 例如 www.qq.com
非CDN业务查询时传入空字符串，返回的值为空
        :type Domain: str
        :param _InstanceID: 1、如果为空，则返回EIP或CLB所有实例的明细；
2、如果传入实例名，则返回该实例明细
        :type InstanceID: str
        """
        self._StartDate = None
        self._EndDate = None
        self._ProductCode = None
        self._Domain = None
        self._InstanceID = None

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._ProductCode = params.get("ProductCode")
        self._Domain = params.get("Domain")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDosageDetailByDateResponse(AbstractModel):
    """DescribeDosageDetailByDate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Unit: 计量单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _DetailSets: 用量数组
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailSets: list of DetailSet
        :param _RetCode: 错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type RetCode: int
        :param _RetMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RetMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Unit = None
        self._DetailSets = None
        self._RetCode = None
        self._RetMsg = None
        self._RequestId = None

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def DetailSets(self):
        return self._DetailSets

    @DetailSets.setter
    def DetailSets(self, DetailSets):
        self._DetailSets = DetailSets

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def RetMsg(self):
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Unit = params.get("Unit")
        if params.get("DetailSets") is not None:
            self._DetailSets = []
            for item in params.get("DetailSets"):
                obj = DetailSet()
                obj._deserialize(item)
                self._DetailSets.append(obj)
        self._RetCode = params.get("RetCode")
        self._RetMsg = params.get("RetMsg")
        self._RequestId = params.get("RequestId")


class DescribeVoucherInfoRequest(AbstractModel):
    """DescribeVoucherInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 一页多少条数据，默认是20条，最大不超过1000
        :type Limit: int
        :param _Offset: 第多少页，默认是1
        :type Offset: int
        :param _Status: 券状态：待使用：unUsed，已使用： used，已发货：delivered，已作废： cancel，已过期：overdue
        :type Status: str
        :param _VoucherId: 代金券id
        :type VoucherId: str
        :param _CodeId: 代金券订单id
        :type CodeId: str
        :param _ProductCode: 商品码
        :type ProductCode: str
        :param _ActivityId: 活动id
        :type ActivityId: str
        :param _VoucherName: 代金券名称
        :type VoucherName: str
        :param _TimeFrom: 发放开始时间,例：2021-01-01
        :type TimeFrom: str
        :param _TimeTo: 发放结束时间，例：2021-01-01
        :type TimeTo: str
        :param _SortField: 指定排序字段：BeginTime开始时间、EndTime到期时间、CreateTime创建时间
        :type SortField: str
        :param _SortOrder: 指定升序降序：desc、asc
        :type SortOrder: str
        :param _PayMode: 付费模式，postPay后付费/prePay预付费/riPay预留实例/""或者"*"表示全部模式，如果payMode为""或"*"，那么productCode与subProductCode必须传空
        :type PayMode: str
        :param _PayScene: 付费场景PayMode=postPay时：spotpay-竞价实例,"settle account"-普通后付费PayMode=prePay时：purchase-包年包月新购，renew-包年包月续费（自动续费），modify-包年包月配置变更(变配）PayMode=riPay时：oneOffFee-预留实例预付，hourlyFee-预留实例每小时扣费，*-支持全部付费场景
        :type PayScene: str
        :param _Operator: 操作人，默认就是用户uin
        :type Operator: str
        """
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._VoucherId = None
        self._CodeId = None
        self._ProductCode = None
        self._ActivityId = None
        self._VoucherName = None
        self._TimeFrom = None
        self._TimeTo = None
        self._SortField = None
        self._SortOrder = None
        self._PayMode = None
        self._PayScene = None
        self._Operator = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VoucherId(self):
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def CodeId(self):
        return self._CodeId

    @CodeId.setter
    def CodeId(self, CodeId):
        self._CodeId = CodeId

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def VoucherName(self):
        return self._VoucherName

    @VoucherName.setter
    def VoucherName(self, VoucherName):
        self._VoucherName = VoucherName

    @property
    def TimeFrom(self):
        return self._TimeFrom

    @TimeFrom.setter
    def TimeFrom(self, TimeFrom):
        self._TimeFrom = TimeFrom

    @property
    def TimeTo(self):
        return self._TimeTo

    @TimeTo.setter
    def TimeTo(self, TimeTo):
        self._TimeTo = TimeTo

    @property
    def SortField(self):
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortOrder(self):
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayScene(self):
        return self._PayScene

    @PayScene.setter
    def PayScene(self, PayScene):
        self._PayScene = PayScene

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._VoucherId = params.get("VoucherId")
        self._CodeId = params.get("CodeId")
        self._ProductCode = params.get("ProductCode")
        self._ActivityId = params.get("ActivityId")
        self._VoucherName = params.get("VoucherName")
        self._TimeFrom = params.get("TimeFrom")
        self._TimeTo = params.get("TimeTo")
        self._SortField = params.get("SortField")
        self._SortOrder = params.get("SortOrder")
        self._PayMode = params.get("PayMode")
        self._PayScene = params.get("PayScene")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVoucherInfoResponse(AbstractModel):
    """DescribeVoucherInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 券总数
        :type TotalCount: int
        :param _TotalBalance: 总余额（微分）
        :type TotalBalance: int
        :param _VoucherInfos: 代金券相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VoucherInfos: list of VoucherInfos
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TotalBalance = None
        self._VoucherInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalBalance(self):
        return self._TotalBalance

    @TotalBalance.setter
    def TotalBalance(self, TotalBalance):
        self._TotalBalance = TotalBalance

    @property
    def VoucherInfos(self):
        return self._VoucherInfos

    @VoucherInfos.setter
    def VoucherInfos(self, VoucherInfos):
        self._VoucherInfos = VoucherInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalBalance = params.get("TotalBalance")
        if params.get("VoucherInfos") is not None:
            self._VoucherInfos = []
            for item in params.get("VoucherInfos"):
                obj = VoucherInfos()
                obj._deserialize(item)
                self._VoucherInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVoucherUsageDetailsRequest(AbstractModel):
    """DescribeVoucherUsageDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 一页多少条数据，默认是20条，最大不超过1000
        :type Limit: int
        :param _Offset: 第多少页，默认是1
        :type Offset: int
        :param _VoucherId: 代金券id
        :type VoucherId: str
        :param _Operator: 操作人，默认就是用户uin
        :type Operator: str
        """
        self._Limit = None
        self._Offset = None
        self._VoucherId = None
        self._Operator = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def VoucherId(self):
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._VoucherId = params.get("VoucherId")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVoucherUsageDetailsResponse(AbstractModel):
    """DescribeVoucherUsageDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 券总数
        :type TotalCount: int
        :param _TotalUsedAmount: 总已用金额（微分）
        :type TotalUsedAmount: int
        :param _UsageRecords: 代金券使用记录细节
注意：此字段可能返回 null，表示取不到有效值。
        :type UsageRecords: list of UsageRecords
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TotalUsedAmount = None
        self._UsageRecords = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalUsedAmount(self):
        return self._TotalUsedAmount

    @TotalUsedAmount.setter
    def TotalUsedAmount(self, TotalUsedAmount):
        self._TotalUsedAmount = TotalUsedAmount

    @property
    def UsageRecords(self):
        return self._UsageRecords

    @UsageRecords.setter
    def UsageRecords(self, UsageRecords):
        self._UsageRecords = UsageRecords

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalUsedAmount = params.get("TotalUsedAmount")
        if params.get("UsageRecords") is not None:
            self._UsageRecords = []
            for item in params.get("UsageRecords"):
                obj = UsageRecords()
                obj._deserialize(item)
                self._UsageRecords.append(obj)
        self._RequestId = params.get("RequestId")


class DetailPoint(AbstractModel):
    """由时间和值组成的数据结构

    """

    def __init__(self):
        r"""
        :param _Time: 时间
        :type Time: str
        :param _Value: 值
        :type Value: str
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetailSet(AbstractModel):
    """由域名和使用明细组成的数据结构

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DetailPoints: 使用数据明细
        :type DetailPoints: list of DetailPoint
        :param _InstanceID: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceID: str
        """
        self._Domain = None
        self._DetailPoints = None
        self._InstanceID = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DetailPoints(self):
        return self._DetailPoints

    @DetailPoints.setter
    def DetailPoints(self, DetailPoints):
        self._DetailPoints = DetailPoints

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("DetailPoints") is not None:
            self._DetailPoints = []
            for item in params.get("DetailPoints"):
                obj = DetailPoint()
                obj._deserialize(item)
                self._DetailPoints.append(obj)
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExcludedProducts(AbstractModel):
    """不适用商品信息

    """

    def __init__(self):
        r"""
        :param _GoodsName: 不适用商品名称
        :type GoodsName: str
        :param _PayMode: postPay后付费/prePay预付费/riPay预留实例/空字符串或者"*"表示全部模式。
        :type PayMode: str
        """
        self._GoodsName = None
        self._PayMode = None

    @property
    def GoodsName(self):
        return self._GoodsName

    @GoodsName.setter
    def GoodsName(self, GoodsName):
        self._GoodsName = GoodsName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._GoodsName = params.get("GoodsName")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayDealsRequest(AbstractModel):
    """PayDeals请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderIds: 需要支付的一个或者多个子订单号，与BigDealIds字段两者必须且仅传一个参数
        :type OrderIds: list of str
        :param _AutoVoucher: 是否自动使用代金券,1:是,0否,默认0
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID列表,目前仅支持指定一张代金券
        :type VoucherIds: list of str
        :param _BigDealIds: 需要支付的一个或者多个大订单号，与OrderIds字段两者必须且仅传一个参数
        :type BigDealIds: list of str
        """
        self._OrderIds = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._BigDealIds = None

    @property
    def OrderIds(self):
        return self._OrderIds

    @OrderIds.setter
    def OrderIds(self, OrderIds):
        self._OrderIds = OrderIds

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds


    def _deserialize(self, params):
        self._OrderIds = params.get("OrderIds")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._BigDealIds = params.get("BigDealIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayDealsResponse(AbstractModel):
    """PayDeals返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderIds: 此次操作支付成功的子订单号数组
        :type OrderIds: list of str
        :param _ResourceIds: 此次操作支付成功的资源Id数组
        :type ResourceIds: list of str
        :param _BigDealIds: 此次操作支付成功的大订单号数组
        :type BigDealIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderIds = None
        self._ResourceIds = None
        self._BigDealIds = None
        self._RequestId = None

    @property
    def OrderIds(self):
        return self._OrderIds

    @OrderIds.setter
    def OrderIds(self, OrderIds):
        self._OrderIds = OrderIds

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrderIds = params.get("OrderIds")
        self._ResourceIds = params.get("ResourceIds")
        self._BigDealIds = params.get("BigDealIds")
        self._RequestId = params.get("RequestId")


class PayModeSummaryOverviewItem(AbstractModel):
    """按计费模式汇总消费详情

    """

    def __init__(self):
        r"""
        :param _PayMode: 计费模式编码
        :type PayMode: str
        :param _PayModeName: 计费模式：区分为包年包月和按量计费
        :type PayModeName: str
        :param _RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param _RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param _TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        :param _Detail: 按交易类型汇总消费详情
        :type Detail: list of ActionSummaryOverviewItem
        """
        self._PayMode = None
        self._PayModeName = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._TotalCost = None
        self._Detail = None

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._TotalCost = params.get("TotalCost")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = ActionSummaryOverviewItem()
                obj._deserialize(item)
                self._Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductInfo(AbstractModel):
    """商品详细信息

    """

    def __init__(self):
        r"""
        :param _Name: 商品详情名称标识
        :type Name: str
        :param _Value: 商品详情
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectSummaryOverviewItem(AbstractModel):
    """按项目汇总消费详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProjectName: 项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :type ProjectName: str
        :param _RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param _RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param _BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        :param _TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._BillMonth = None
        self._TotalCost = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._BillMonth = params.get("BillMonth")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionSummaryOverviewItem(AbstractModel):
    """按地域汇总消费详情

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        :param _RegionName: 地域名称：资源所属地域，例如华南地区（广州）
        :type RegionName: str
        :param _RealTotalCostRatio: 费用所占百分比，两位小数
        :type RealTotalCostRatio: str
        :param _RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param _BillMonth: 账单月份，格式2019-08
        :type BillMonth: str
        :param _TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        """
        self._RegionId = None
        self._RegionName = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._BillMonth = None
        self._TotalCost = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._BillMonth = params.get("BillMonth")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryDetail(AbstractModel):
    """账单多维度汇总消费详情

    """

    def __init__(self):
        r"""
        :param _GroupKey: 账单维度编码
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupKey: str
        :param _GroupValue: 账单维度值
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupValue: str
        :param _TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        :param _RealTotalCost: 优惠后总价
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        :param _Business: 产品汇总信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Business: list of BusinessSummaryInfo
        """
        self._GroupKey = None
        self._GroupValue = None
        self._TotalCost = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._Business = None

    @property
    def GroupKey(self):
        return self._GroupKey

    @GroupKey.setter
    def GroupKey(self, GroupKey):
        self._GroupKey = GroupKey

    @property
    def GroupValue(self):
        return self._GroupValue

    @GroupValue.setter
    def GroupValue(self, GroupValue):
        self._GroupValue = GroupValue

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business


    def _deserialize(self, params):
        self._GroupKey = params.get("GroupKey")
        self._GroupValue = params.get("GroupValue")
        self._TotalCost = params.get("TotalCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = BusinessSummaryInfo()
                obj._deserialize(item)
                self._Business.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryTotal(AbstractModel):
    """总数

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: 优惠后总价
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalCost: str
        :param _TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: str
        """
        self._RealTotalCost = None
        self._TotalCost = None

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._RealTotalCost = params.get("RealTotalCost")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSummaryOverviewItem(AbstractModel):
    """按标签汇总消费详情

    """

    def __init__(self):
        r"""
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        :param _RealTotalCostRatio: 费用所占百分比，两位小数
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalCostRatio: str
        :param _RealTotalCost: 优惠后总价
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出：通过现金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出：使用赠送金支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金账户支出：通过分成金账户支付的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        :param _TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: str
        """
        self._TagValue = None
        self._RealTotalCostRatio = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._TotalCost = None

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def RealTotalCostRatio(self):
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._TagValue = params.get("TagValue")
        self._RealTotalCostRatio = params.get("RealTotalCostRatio")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageDetails(AbstractModel):
    """购买商品信息

    """

    def __init__(self):
        r"""
        :param _ProductName: 商品名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _SubProductName: 商品细节
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProductName: str
        """
        self._ProductName = None
        self._SubProductName = None

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductName(self):
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._SubProductName = params.get("SubProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageRecords(AbstractModel):
    """使用记录

    """

    def __init__(self):
        r"""
        :param _UsedAmount: 使用金额（微分）
        :type UsedAmount: int
        :param _UsedTime: 使用时间
        :type UsedTime: str
        :param _UsageDetails: 使用记录细节
注意：此字段可能返回 null，表示取不到有效值。
        :type UsageDetails: list of UsageDetails
        """
        self._UsedAmount = None
        self._UsedTime = None
        self._UsageDetails = None

    @property
    def UsedAmount(self):
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedTime(self):
        return self._UsedTime

    @UsedTime.setter
    def UsedTime(self, UsedTime):
        self._UsedTime = UsedTime

    @property
    def UsageDetails(self):
        return self._UsageDetails

    @UsageDetails.setter
    def UsageDetails(self, UsageDetails):
        self._UsageDetails = UsageDetails


    def _deserialize(self, params):
        self._UsedAmount = params.get("UsedAmount")
        self._UsedTime = params.get("UsedTime")
        if params.get("UsageDetails") is not None:
            self._UsageDetails = []
            for item in params.get("UsageDetails"):
                obj = UsageDetails()
                obj._deserialize(item)
                self._UsageDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoucherInfos(AbstractModel):
    """代金券相关信息

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 代金券拥有者
        :type OwnerUin: str
        :param _Status: 券状态：待使用：unUsed，已使用： used，已发货：delivered，已作废： cancel，已过期：overdue
        :type Status: str
        :param _NominalValue: 代金券面额（微分）
        :type NominalValue: int
        :param _Balance: 剩余金额（微分）
        :type Balance: int
        :param _VoucherId: 代金券id
        :type VoucherId: str
        :param _PayMode: postPay后付费/prePay预付费/riPay预留实例/空字符串或者'*'表示全部模式
        :type PayMode: str
        :param _PayScene: 付费场景PayMode=postPay时：spotpay-竞价实例,"settle account"-普通后付费PayMode=prePay时：purchase-包年包月新购，renew-包年包月续费（自动续费），modify-包年包月配置变更(变配）PayMode=riPay时：oneOffFee-预留实例预付，hourlyFee-预留实例每小时扣费，*-支持全部付费场景
        :type PayScene: str
        :param _BeginTime: 有效期生效时间
        :type BeginTime: str
        :param _EndTime: 有效期截止时间
        :type EndTime: str
        :param _ApplicableProducts: 适用商品信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicableProducts: :class:`tencentcloud.billing.v20180709.models.ApplicableProducts`
        :param _ExcludedProducts: 不适用商品信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludedProducts: list of ExcludedProducts
        """
        self._OwnerUin = None
        self._Status = None
        self._NominalValue = None
        self._Balance = None
        self._VoucherId = None
        self._PayMode = None
        self._PayScene = None
        self._BeginTime = None
        self._EndTime = None
        self._ApplicableProducts = None
        self._ExcludedProducts = None

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NominalValue(self):
        return self._NominalValue

    @NominalValue.setter
    def NominalValue(self, NominalValue):
        self._NominalValue = NominalValue

    @property
    def Balance(self):
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def VoucherId(self):
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayScene(self):
        return self._PayScene

    @PayScene.setter
    def PayScene(self, PayScene):
        self._PayScene = PayScene

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ApplicableProducts(self):
        return self._ApplicableProducts

    @ApplicableProducts.setter
    def ApplicableProducts(self, ApplicableProducts):
        self._ApplicableProducts = ApplicableProducts

    @property
    def ExcludedProducts(self):
        return self._ExcludedProducts

    @ExcludedProducts.setter
    def ExcludedProducts(self, ExcludedProducts):
        self._ExcludedProducts = ExcludedProducts


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._Status = params.get("Status")
        self._NominalValue = params.get("NominalValue")
        self._Balance = params.get("Balance")
        self._VoucherId = params.get("VoucherId")
        self._PayMode = params.get("PayMode")
        self._PayScene = params.get("PayScene")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        if params.get("ApplicableProducts") is not None:
            self._ApplicableProducts = ApplicableProducts()
            self._ApplicableProducts._deserialize(params.get("ApplicableProducts"))
        if params.get("ExcludedProducts") is not None:
            self._ExcludedProducts = []
            for item in params.get("ExcludedProducts"):
                obj = ExcludedProducts()
                obj._deserialize(item)
                self._ExcludedProducts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        