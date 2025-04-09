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
        """交易类型编码
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        """交易类型：如包年包月新购、包年包月续费、按量计费扣费等类型
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def RealTotalCostRatio(self):
        """费用所占百分比，两位小数
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        """优惠后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        """账单月份，格式2019-08
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        """原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :rtype: str
        """
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
        


class AdjustInfoDetail(AbstractModel):
    """UIN异常调整明细

    """

    def __init__(self):
        r"""
        :param _PayerUin: 支付者UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :type PayerUin: str
        :param _Month: 账单月份，格式：yyyy-MM
        :type Month: str
        :param _AdjustType: 调整类型
调账：manualAdjustment
补结算：supplementarySettlement
重结算：reSettlement
        :type AdjustType: str
        :param _AdjustNum: 调整单号
        :type AdjustNum: str
        :param _AdjustCompletionTime: 异常调整完成时间，格式：yyyy-MM-dd HH:mm:ss
        :type AdjustCompletionTime: str
        :param _AdjustAmount: 调整金额
        :type AdjustAmount: float
        """
        self._PayerUin = None
        self._Month = None
        self._AdjustType = None
        self._AdjustNum = None
        self._AdjustCompletionTime = None
        self._AdjustAmount = None

    @property
    def PayerUin(self):
        """支付者UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def Month(self):
        """账单月份，格式：yyyy-MM
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def AdjustType(self):
        """调整类型
调账：manualAdjustment
补结算：supplementarySettlement
重结算：reSettlement
        :rtype: str
        """
        return self._AdjustType

    @AdjustType.setter
    def AdjustType(self, AdjustType):
        self._AdjustType = AdjustType

    @property
    def AdjustNum(self):
        """调整单号
        :rtype: str
        """
        return self._AdjustNum

    @AdjustNum.setter
    def AdjustNum(self, AdjustNum):
        self._AdjustNum = AdjustNum

    @property
    def AdjustCompletionTime(self):
        """异常调整完成时间，格式：yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._AdjustCompletionTime

    @AdjustCompletionTime.setter
    def AdjustCompletionTime(self, AdjustCompletionTime):
        self._AdjustCompletionTime = AdjustCompletionTime

    @property
    def AdjustAmount(self):
        """调整金额
        :rtype: float
        """
        return self._AdjustAmount

    @AdjustAmount.setter
    def AdjustAmount(self, AdjustAmount):
        self._AdjustAmount = AdjustAmount


    def _deserialize(self, params):
        self._PayerUin = params.get("PayerUin")
        self._Month = params.get("Month")
        self._AdjustType = params.get("AdjustType")
        self._AdjustNum = params.get("AdjustNum")
        self._AdjustCompletionTime = params.get("AdjustCompletionTime")
        self._AdjustAmount = params.get("AdjustAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationAverageData(AbstractModel):
    """分账账单趋势图平均值

    """

    def __init__(self):
        r"""
        :param _BeginMonth: 起始月份
        :type BeginMonth: str
        :param _EndMonth: 结束月份
        :type EndMonth: str
        :param _RealTotalCost: 合计费用(折后总额)平均值
        :type RealTotalCost: str
        """
        self._BeginMonth = None
        self._EndMonth = None
        self._RealTotalCost = None

    @property
    def BeginMonth(self):
        """起始月份
        :rtype: str
        """
        return self._BeginMonth

    @BeginMonth.setter
    def BeginMonth(self, BeginMonth):
        self._BeginMonth = BeginMonth

    @property
    def EndMonth(self):
        """结束月份
        :rtype: str
        """
        return self._EndMonth

    @EndMonth.setter
    def EndMonth(self, EndMonth):
        self._EndMonth = EndMonth

    @property
    def RealTotalCost(self):
        """合计费用(折后总额)平均值
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost


    def _deserialize(self, params):
        self._BeginMonth = params.get("BeginMonth")
        self._EndMonth = params.get("EndMonth")
        self._RealTotalCost = params.get("RealTotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationBillTrendDetail(AbstractModel):
    """分账趋势图详情数据

    """

    def __init__(self):
        r"""
        :param _Month: 账单月份
        :type Month: str
        :param _Name: 账单月份展示名称
        :type Name: str
        :param _RealTotalCost: 合计费用(折后总额)：分账单元总费用，归集费用(折后总额) + 分摊费用(折后总额)
        :type RealTotalCost: str
        """
        self._Month = None
        self._Name = None
        self._RealTotalCost = None

    @property
    def Month(self):
        """账单月份
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def Name(self):
        """账单月份展示名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RealTotalCost(self):
        """合计费用(折后总额)：分账单元总费用，归集费用(折后总额) + 分摊费用(折后总额)
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._Name = params.get("Name")
        self._RealTotalCost = params.get("RealTotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationDetail(AbstractModel):
    """分账账单明细

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: 分账单元唯一标识
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: 分账单元名称
        :type TreeNodeUniqKeyName: str
        :param _BillDate: 日期：结算日期
        :type BillDate: str
        :param _PayerUin: 支付者 UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :type PayerUin: str
        :param _OwnerUin: 使用者 UIN：实际使用资源的账号 ID
        :type OwnerUin: str
        :param _OperateUin: 操作者 UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的ID或者角色 ID）
        :type OperateUin: str
        :param _BusinessCode: 产品编码
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称：用户所采购的各类云产品
        :type BusinessCodeName: str
        :param _PayMode: 计费模式编码
        :type PayMode: str
        :param _PayModeName: 计费模式：资源的计费模式，区分为包年包月和按量计费
        :type PayModeName: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _ProjectName: 项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :type ProjectName: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _RegionName: 地域名称：资源所属地域
        :type RegionName: str
        :param _ZoneId: 可用区ID
        :type ZoneId: int
        :param _ZoneName: 可用区：资源所属可用区
        :type ZoneName: str
        :param _ResourceId: 资源ID：不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID； 若该产品被分拆，则展示产品分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
        :type ResourceId: str
        :param _ResourceName: 实例名称：用户在控制台为资源设置的名称，如未设置默认为空；若该产品被分拆，则展示分拆产品分拆后的分拆项资源别名
        :type ResourceName: str
        :param _InstanceType: 实例类型编码
        :type InstanceType: str
        :param _InstanceTypeName: 实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。常规实例默认展示“-”
        :type InstanceTypeName: str
        :param _SplitItemId: 分拆项 ID：涉及分拆产品的分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type SplitItemId: str
        :param _SplitItemName: 分拆项名称：涉及分拆产品的分拆后的分拆项
注意：此字段可能返回 null，表示取不到有效值。
        :type SplitItemName: str
        :param _ProductCode: 子产品编码
        :type ProductCode: str
        :param _ProductCodeName: 子产品名称：用户采购的具体产品细分类型
        :type ProductCodeName: str
        :param _ActionType: 交易类型编码
        :type ActionType: str
        :param _ActionTypeName: 交易类型：明细交易类型
        :type ActionTypeName: str
        :param _OrderId: 订单 ID：包年包月计费模式下订购的订单号

        :type OrderId: str
        :param _BillId: 交易 ID：结算扣费单号
        :type BillId: str
        :param _PayTime: 扣费时间：结算扣费时间
        :type PayTime: str
        :param _FeeBeginTime: 开始使用时间：产品服务开始使用时间
        :type FeeBeginTime: str
        :param _FeeEndTime: 结束使用时间：产品服务结束使用时间
        :type FeeEndTime: str
        :param _ComponentCode: 组件类型编码
        :type ComponentCode: str
        :param _ComponentCodeName: 组件类型：用户购买的产品或服务对应的组件大类
        :type ComponentCodeName: str
        :param _SinglePrice: 组件刊例价：组件的官网原始单价（如客户享受一口价/合同价则默认不展示）
        :type SinglePrice: str
        :param _ContractPrice: 组件单价：组件的折后单价，组件单价 = 刊例价 * 折扣
        :type ContractPrice: str
        :param _SinglePriceUnit: 组件价格单位：组件价格的单位，单位构成：元/用量单位/时长单位
        :type SinglePriceUnit: str
        :param _UsedAmount: 组件用量：该组件实际结算用量，组件用量=组件原始用量-抵扣用量（含资源包）
        :type UsedAmount: str
        :param _UsedAmountUnit: 组件用量单位：组件用量对应的单位
        :type UsedAmountUnit: str
        :param _TimeSpan: 使用时长：资源使用的时长，组件用量=组件原始使用时长-抵扣时长（含资源包）
        :type TimeSpan: str
        :param _TimeUnit: 时长单位：资源使用时长的单位
        :type TimeUnit: str
        :param _ReserveDetail: 备注属性（实例配置）：其他备注信息，如预留实例的预留实例类型和交易类型、CCN 产品的两端地域信息
        :type ReserveDetail: str
        :param _SplitRatio: 分拆项用量/时长占比：分拆项用量（时长）占比，分拆项用量（时长）/ 拆分前合计用量（时长）
        :type SplitRatio: str
        :param _TotalCost: 组件原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如客户享受一口价/合同价则默认不展示，退费类场景也默认不展示），指定价模式
        :type TotalCost: str
        :param _RITimeSpan: 预留实例抵扣时长：本产品或服务使用预留实例抵扣的使用时长
        :type RITimeSpan: str
        :param _RICost: 预留实例抵扣原价：本产品或服务使用预留实例抵扣的组件原价金额
        :type RICost: str
        :param _SPCost: 节省计划抵扣原价：节省计划抵扣原价 = 节省计划包抵扣面值 / 节省计划抵扣率
        :type SPCost: str
        :param _Discount: 折扣率：本资源享受的折扣率（如客户享受一口价/合同价则默认不展示，退费场景也默认不展示）
        :type Discount: str
        :param _BlendedDiscount: 混合折扣率：综合各类折扣抵扣信息后的最终折扣率，混合折扣率=优惠后总价/原价
        :type BlendedDiscount: str
        :param _RealTotalCost: 优惠后总价：优惠后总价 =（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出(元)：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _VoucherPayAmount: 代金券支出(元)：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出(元)：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _TransferPayAmount: 分成账户支出(元)：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param _Tag: 分账标签：资源绑定的标签
        :type Tag: list of BillTag
        :param _RegionType: 国内国际编码
        :type RegionType: str
        :param _RegionTypeName: 国内国际：资源所属区域类型（国内、国际）
        :type RegionTypeName: str
        :param _ItemCode: 组件名称编码
        :type ItemCode: str
        :param _ItemCodeName: 组件名称：用户购买的产品或服务，所包含的具体组件
        :type ItemCodeName: str
        :param _AssociatedOrder: 关联单据ID：和本笔交易关联单据ID，如退费订单对应的原新购订单等
        :type AssociatedOrder: str
        :param _PriceInfo: 价格属性：该组件除单价、时长外的其他影响折扣定价的属性信息
        :type PriceInfo: list of str
        :param _Formula: 计算规则说明：特殊交易类型计费结算的详细计算说明，如退费及变配
        :type Formula: str
        :param _FormulaUrl: 计费规则：各产品详细的计费规则官网说明链接
        :type FormulaUrl: str
        :param _RealTotalMeasure: 原始用量/时长：组件被资源包抵扣前的原始用量
（目前仅实时音视频、弹性微服务、云呼叫中心及专属可用区产品支持该信息外显，其他产品尚在接入中）
        :type RealTotalMeasure: str
        :param _DeductedMeasure: 抵扣用量/时长（含资源包）：组件被资源包抵扣的用量
（目前仅实时音视频、弹性微服务、云呼叫中心及专属可用区产品支持该信息外显，其他产品尚在接入中）
        :type DeductedMeasure: str
        :param _ComponentConfig: 配置描述：资源配置规格信息
        :type ComponentConfig: str
        :param _AllocationType: 费用归集类型：费用来源类型，分摊、归集、未分配
0 - 分摊
1 - 归集
2 - 未分配
        :type AllocationType: int
        :param _DiscountObject: 当前消费项的优惠对象，例如：官网折扣、用户折扣、活动折扣。
        :type DiscountObject: str
        :param _DiscountType: 当前消费项的优惠类型，例如：折扣、合同价。
        :type DiscountType: str
        :param _DiscountContent: 对优惠类型的补充描述，例如：商务折扣8折，则优惠类型为“折扣”，优惠内容为“0.8”。
        :type DiscountContent: str
        :param _SPDeduction: SPDeduction
        :type SPDeduction: str
        :param _SPDeductionRate: SPDeduction
        :type SPDeductionRate: str
        :param _BillMonth: 账单月
        :type BillMonth: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._BillDate = None
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._PayMode = None
        self._PayModeName = None
        self._ProjectId = None
        self._ProjectName = None
        self._RegionId = None
        self._RegionName = None
        self._ZoneId = None
        self._ZoneName = None
        self._ResourceId = None
        self._ResourceName = None
        self._InstanceType = None
        self._InstanceTypeName = None
        self._SplitItemId = None
        self._SplitItemName = None
        self._ProductCode = None
        self._ProductCodeName = None
        self._ActionType = None
        self._ActionTypeName = None
        self._OrderId = None
        self._BillId = None
        self._PayTime = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._ComponentCode = None
        self._ComponentCodeName = None
        self._SinglePrice = None
        self._ContractPrice = None
        self._SinglePriceUnit = None
        self._UsedAmount = None
        self._UsedAmountUnit = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._ReserveDetail = None
        self._SplitRatio = None
        self._TotalCost = None
        self._RITimeSpan = None
        self._RICost = None
        self._SPCost = None
        self._Discount = None
        self._BlendedDiscount = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._Tag = None
        self._RegionType = None
        self._RegionTypeName = None
        self._ItemCode = None
        self._ItemCodeName = None
        self._AssociatedOrder = None
        self._PriceInfo = None
        self._Formula = None
        self._FormulaUrl = None
        self._RealTotalMeasure = None
        self._DeductedMeasure = None
        self._ComponentConfig = None
        self._AllocationType = None
        self._DiscountObject = None
        self._DiscountType = None
        self._DiscountContent = None
        self._SPDeduction = None
        self._SPDeductionRate = None
        self._BillMonth = None

    @property
    def TreeNodeUniqKey(self):
        """分账单元唯一标识
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        """分账单元名称
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def BillDate(self):
        """日期：结算日期
        :rtype: str
        """
        return self._BillDate

    @BillDate.setter
    def BillDate(self, BillDate):
        self._BillDate = BillDate

    @property
    def PayerUin(self):
        """支付者 UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        """使用者 UIN：实际使用资源的账号 ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        """操作者 UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的ID或者角色 ID）
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def BusinessCode(self):
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def PayMode(self):
        """计费模式编码
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        """计费模式：资源的计费模式，区分为包年包月和按量计费
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionId(self):
        """地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称：资源所属地域
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

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
    def ZoneName(self):
        """可用区：资源所属可用区
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        """资源ID：不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID； 若该产品被分拆，则展示产品分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """实例名称：用户在控制台为资源设置的名称，如未设置默认为空；若该产品被分拆，则展示分拆产品分拆后的分拆项资源别名
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def InstanceType(self):
        """实例类型编码
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        """实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。常规实例默认展示“-”
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName

    @property
    def SplitItemId(self):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        """分拆项 ID：涉及分拆产品的分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SplitItemId

    @SplitItemId.setter
    def SplitItemId(self, SplitItemId):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        self._SplitItemId = SplitItemId

    @property
    def SplitItemName(self):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        """分拆项名称：涉及分拆产品的分拆后的分拆项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SplitItemName

    @SplitItemName.setter
    def SplitItemName(self, SplitItemName):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        self._SplitItemName = SplitItemName

    @property
    def ProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        """子产品名称：用户采购的具体产品细分类型
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def ActionType(self):
        """交易类型编码
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        """交易类型：明细交易类型
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        """订单 ID：包年包月计费模式下订购的订单号

        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        """交易 ID：结算扣费单号
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def PayTime(self):
        """扣费时间：结算扣费时间
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        """开始使用时间：产品服务开始使用时间
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        """结束使用时间：产品服务结束使用时间
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentCode(self):
        """组件类型编码
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ComponentCodeName(self):
        """组件类型：用户购买的产品或服务对应的组件大类
        :rtype: str
        """
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def SinglePrice(self):
        """组件刊例价：组件的官网原始单价（如客户享受一口价/合同价则默认不展示）
        :rtype: str
        """
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def ContractPrice(self):
        """组件单价：组件的折后单价，组件单价 = 刊例价 * 折扣
        :rtype: str
        """
        return self._ContractPrice

    @ContractPrice.setter
    def ContractPrice(self, ContractPrice):
        self._ContractPrice = ContractPrice

    @property
    def SinglePriceUnit(self):
        """组件价格单位：组件价格的单位，单位构成：元/用量单位/时长单位
        :rtype: str
        """
        return self._SinglePriceUnit

    @SinglePriceUnit.setter
    def SinglePriceUnit(self, SinglePriceUnit):
        self._SinglePriceUnit = SinglePriceUnit

    @property
    def UsedAmount(self):
        """组件用量：该组件实际结算用量，组件用量=组件原始用量-抵扣用量（含资源包）
        :rtype: str
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        """组件用量单位：组件用量对应的单位
        :rtype: str
        """
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def TimeSpan(self):
        """使用时长：资源使用的时长，组件用量=组件原始使用时长-抵扣时长（含资源包）
        :rtype: str
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """时长单位：资源使用时长的单位
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def ReserveDetail(self):
        """备注属性（实例配置）：其他备注信息，如预留实例的预留实例类型和交易类型、CCN 产品的两端地域信息
        :rtype: str
        """
        return self._ReserveDetail

    @ReserveDetail.setter
    def ReserveDetail(self, ReserveDetail):
        self._ReserveDetail = ReserveDetail

    @property
    def SplitRatio(self):
        """分拆项用量/时长占比：分拆项用量（时长）占比，分拆项用量（时长）/ 拆分前合计用量（时长）
        :rtype: str
        """
        return self._SplitRatio

    @SplitRatio.setter
    def SplitRatio(self, SplitRatio):
        self._SplitRatio = SplitRatio

    @property
    def TotalCost(self):
        """组件原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如客户享受一口价/合同价则默认不展示，退费类场景也默认不展示），指定价模式
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RITimeSpan(self):
        """预留实例抵扣时长：本产品或服务使用预留实例抵扣的使用时长
        :rtype: str
        """
        return self._RITimeSpan

    @RITimeSpan.setter
    def RITimeSpan(self, RITimeSpan):
        self._RITimeSpan = RITimeSpan

    @property
    def RICost(self):
        """预留实例抵扣原价：本产品或服务使用预留实例抵扣的组件原价金额
        :rtype: str
        """
        return self._RICost

    @RICost.setter
    def RICost(self, RICost):
        self._RICost = RICost

    @property
    def SPCost(self):
        """节省计划抵扣原价：节省计划抵扣原价 = 节省计划包抵扣面值 / 节省计划抵扣率
        :rtype: str
        """
        return self._SPCost

    @SPCost.setter
    def SPCost(self, SPCost):
        self._SPCost = SPCost

    @property
    def Discount(self):
        """折扣率：本资源享受的折扣率（如客户享受一口价/合同价则默认不展示，退费场景也默认不展示）
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def BlendedDiscount(self):
        """混合折扣率：综合各类折扣抵扣信息后的最终折扣率，混合折扣率=优惠后总价/原价
        :rtype: str
        """
        return self._BlendedDiscount

    @BlendedDiscount.setter
    def BlendedDiscount(self, BlendedDiscount):
        self._BlendedDiscount = BlendedDiscount

    @property
    def RealTotalCost(self):
        """优惠后总价：优惠后总价 =（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出(元)：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        """代金券支出(元)：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出(元)：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        """分成账户支出(元)：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def Tag(self):
        """分账标签：资源绑定的标签
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def RegionType(self):
        """国内国际编码
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        """国内国际：资源所属区域类型（国内、国际）
        :rtype: str
        """
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def ItemCode(self):
        """组件名称编码
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ItemCodeName(self):
        """组件名称：用户购买的产品或服务，所包含的具体组件
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def AssociatedOrder(self):
        """关联单据ID：和本笔交易关联单据ID，如退费订单对应的原新购订单等
        :rtype: str
        """
        return self._AssociatedOrder

    @AssociatedOrder.setter
    def AssociatedOrder(self, AssociatedOrder):
        self._AssociatedOrder = AssociatedOrder

    @property
    def PriceInfo(self):
        """价格属性：该组件除单价、时长外的其他影响折扣定价的属性信息
        :rtype: list of str
        """
        return self._PriceInfo

    @PriceInfo.setter
    def PriceInfo(self, PriceInfo):
        self._PriceInfo = PriceInfo

    @property
    def Formula(self):
        """计算规则说明：特殊交易类型计费结算的详细计算说明，如退费及变配
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def FormulaUrl(self):
        """计费规则：各产品详细的计费规则官网说明链接
        :rtype: str
        """
        return self._FormulaUrl

    @FormulaUrl.setter
    def FormulaUrl(self, FormulaUrl):
        self._FormulaUrl = FormulaUrl

    @property
    def RealTotalMeasure(self):
        """原始用量/时长：组件被资源包抵扣前的原始用量
（目前仅实时音视频、弹性微服务、云呼叫中心及专属可用区产品支持该信息外显，其他产品尚在接入中）
        :rtype: str
        """
        return self._RealTotalMeasure

    @RealTotalMeasure.setter
    def RealTotalMeasure(self, RealTotalMeasure):
        self._RealTotalMeasure = RealTotalMeasure

    @property
    def DeductedMeasure(self):
        """抵扣用量/时长（含资源包）：组件被资源包抵扣的用量
（目前仅实时音视频、弹性微服务、云呼叫中心及专属可用区产品支持该信息外显，其他产品尚在接入中）
        :rtype: str
        """
        return self._DeductedMeasure

    @DeductedMeasure.setter
    def DeductedMeasure(self, DeductedMeasure):
        self._DeductedMeasure = DeductedMeasure

    @property
    def ComponentConfig(self):
        """配置描述：资源配置规格信息
        :rtype: str
        """
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig

    @property
    def AllocationType(self):
        """费用归集类型：费用来源类型，分摊、归集、未分配
0 - 分摊
1 - 归集
2 - 未分配
        :rtype: int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType

    @property
    def DiscountObject(self):
        """当前消费项的优惠对象，例如：官网折扣、用户折扣、活动折扣。
        :rtype: str
        """
        return self._DiscountObject

    @DiscountObject.setter
    def DiscountObject(self, DiscountObject):
        self._DiscountObject = DiscountObject

    @property
    def DiscountType(self):
        """当前消费项的优惠类型，例如：折扣、合同价。
        :rtype: str
        """
        return self._DiscountType

    @DiscountType.setter
    def DiscountType(self, DiscountType):
        self._DiscountType = DiscountType

    @property
    def DiscountContent(self):
        """对优惠类型的补充描述，例如：商务折扣8折，则优惠类型为“折扣”，优惠内容为“0.8”。
        :rtype: str
        """
        return self._DiscountContent

    @DiscountContent.setter
    def DiscountContent(self, DiscountContent):
        self._DiscountContent = DiscountContent

    @property
    def SPDeduction(self):
        """SPDeduction
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        self._SPDeduction = SPDeduction

    @property
    def SPDeductionRate(self):
        """SPDeduction
        :rtype: str
        """
        return self._SPDeductionRate

    @SPDeductionRate.setter
    def SPDeductionRate(self, SPDeductionRate):
        self._SPDeductionRate = SPDeductionRate

    @property
    def BillMonth(self):
        """账单月
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._BillDate = params.get("BillDate")
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        self._SplitItemId = params.get("SplitItemId")
        self._SplitItemName = params.get("SplitItemName")
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        self._OrderId = params.get("OrderId")
        self._BillId = params.get("BillId")
        self._PayTime = params.get("PayTime")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        self._ComponentCode = params.get("ComponentCode")
        self._ComponentCodeName = params.get("ComponentCodeName")
        self._SinglePrice = params.get("SinglePrice")
        self._ContractPrice = params.get("ContractPrice")
        self._SinglePriceUnit = params.get("SinglePriceUnit")
        self._UsedAmount = params.get("UsedAmount")
        self._UsedAmountUnit = params.get("UsedAmountUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._ReserveDetail = params.get("ReserveDetail")
        self._SplitRatio = params.get("SplitRatio")
        self._TotalCost = params.get("TotalCost")
        self._RITimeSpan = params.get("RITimeSpan")
        self._RICost = params.get("RICost")
        self._SPCost = params.get("SPCost")
        self._Discount = params.get("Discount")
        self._BlendedDiscount = params.get("BlendedDiscount")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._RegionType = params.get("RegionType")
        self._RegionTypeName = params.get("RegionTypeName")
        self._ItemCode = params.get("ItemCode")
        self._ItemCodeName = params.get("ItemCodeName")
        self._AssociatedOrder = params.get("AssociatedOrder")
        self._PriceInfo = params.get("PriceInfo")
        self._Formula = params.get("Formula")
        self._FormulaUrl = params.get("FormulaUrl")
        self._RealTotalMeasure = params.get("RealTotalMeasure")
        self._DeductedMeasure = params.get("DeductedMeasure")
        self._ComponentConfig = params.get("ComponentConfig")
        self._AllocationType = params.get("AllocationType")
        self._DiscountObject = params.get("DiscountObject")
        self._DiscountType = params.get("DiscountType")
        self._DiscountContent = params.get("DiscountContent")
        self._SPDeduction = params.get("SPDeduction")
        self._SPDeductionRate = params.get("SPDeductionRate")
        self._BillMonth = params.get("BillMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationMonthOverviewDetail(AbstractModel):
    """分账账单月概览金额明细

    """

    def __init__(self):
        r"""
        :param _GatherCashPayAmount: 归集费用(现金)：基于归集规则直接归集到分账单元的现金
        :type GatherCashPayAmount: str
        :param _GatherVoucherPayAmount: 归集费用(优惠券)：基于归集规则直接归集到分账单元的资源优惠券
        :type GatherVoucherPayAmount: str
        :param _GatherIncentivePayAmount: 归集费用(赠送金)：基于归集规则直接归集到分账单元的资源赠送金
        :type GatherIncentivePayAmount: str
        :param _GatherTransferPayAmount: 归集费用(分成金)：基于归集规则直接归集到分账单元的资源分成金
        :type GatherTransferPayAmount: str
        :param _AllocateCashPayAmount: 分摊费用(现金)：基于分摊规则分摊到分账单元的资源现金
        :type AllocateCashPayAmount: str
        :param _AllocateVoucherPayAmount: 分摊费用(优惠券)：基于分摊规则分摊到分账单元的资源优惠券
        :type AllocateVoucherPayAmount: str
        :param _AllocateIncentivePayAmount: 分摊费用(赠送金)：基于分摊规则分摊到分账单元的资源赠送金
        :type AllocateIncentivePayAmount: str
        :param _AllocateTransferPayAmount: 分摊费用(分成金)：基于分摊规则分摊到分账单元的资源分成金
        :type AllocateTransferPayAmount: str
        :param _TotalCashPayAmount: 合计费用(现金)：分账单元总费用，归集费用(现金) + 分摊费用(现金)
        :type TotalCashPayAmount: str
        :param _TotalVoucherPayAmount: 合计费用(优惠券)：分账单元总费用，归集费用(优惠券) + 分摊费用(优惠券)
        :type TotalVoucherPayAmount: str
        :param _TotalIncentivePayAmount: 合计费用(赠送金)：分账单元总费用，归集费用(赠送金) + 分摊费用(赠送金)
        :type TotalIncentivePayAmount: str
        :param _TotalTransferPayAmount: 合计费用(分成金)：分账单元总费用，归集费用(分成金)+分摊费用(分成金)
        :type TotalTransferPayAmount: str
        :param _GatherRealCost: 归集费用(折后总额)：基于归集规则直接归集到分账单元的资源优惠后总价
        :type GatherRealCost: str
        :param _AllocateRealCost: 分摊费用(折后总额)：基于分摊规则分摊到分账单元的资源优惠后总价
        :type AllocateRealCost: str
        :param _RealTotalCost: 合计费用(折后总额)：分账单元总费用，归集费用(折后总额) + 分摊费用(折后总额)
        :type RealTotalCost: str
        :param _Ratio: 占比(折后总额)：本分账单元合计费用(折后总额)/合计费用(折后总额)*100%
        :type Ratio: str
        :param _Trend: 环比(折后总额)：[本月分账单元合计费用(折后总额) - 上月分账单元合计费用(折后总额)] / 上月分账单元合计费用(折后总额) * 100%
        :type Trend: str
        :param _TrendType: 环比箭头
upward -上升
downward - 下降
none - 平稳
        :type TrendType: str
        """
        self._GatherCashPayAmount = None
        self._GatherVoucherPayAmount = None
        self._GatherIncentivePayAmount = None
        self._GatherTransferPayAmount = None
        self._AllocateCashPayAmount = None
        self._AllocateVoucherPayAmount = None
        self._AllocateIncentivePayAmount = None
        self._AllocateTransferPayAmount = None
        self._TotalCashPayAmount = None
        self._TotalVoucherPayAmount = None
        self._TotalIncentivePayAmount = None
        self._TotalTransferPayAmount = None
        self._GatherRealCost = None
        self._AllocateRealCost = None
        self._RealTotalCost = None
        self._Ratio = None
        self._Trend = None
        self._TrendType = None

    @property
    def GatherCashPayAmount(self):
        """归集费用(现金)：基于归集规则直接归集到分账单元的现金
        :rtype: str
        """
        return self._GatherCashPayAmount

    @GatherCashPayAmount.setter
    def GatherCashPayAmount(self, GatherCashPayAmount):
        self._GatherCashPayAmount = GatherCashPayAmount

    @property
    def GatherVoucherPayAmount(self):
        """归集费用(优惠券)：基于归集规则直接归集到分账单元的资源优惠券
        :rtype: str
        """
        return self._GatherVoucherPayAmount

    @GatherVoucherPayAmount.setter
    def GatherVoucherPayAmount(self, GatherVoucherPayAmount):
        self._GatherVoucherPayAmount = GatherVoucherPayAmount

    @property
    def GatherIncentivePayAmount(self):
        """归集费用(赠送金)：基于归集规则直接归集到分账单元的资源赠送金
        :rtype: str
        """
        return self._GatherIncentivePayAmount

    @GatherIncentivePayAmount.setter
    def GatherIncentivePayAmount(self, GatherIncentivePayAmount):
        self._GatherIncentivePayAmount = GatherIncentivePayAmount

    @property
    def GatherTransferPayAmount(self):
        """归集费用(分成金)：基于归集规则直接归集到分账单元的资源分成金
        :rtype: str
        """
        return self._GatherTransferPayAmount

    @GatherTransferPayAmount.setter
    def GatherTransferPayAmount(self, GatherTransferPayAmount):
        self._GatherTransferPayAmount = GatherTransferPayAmount

    @property
    def AllocateCashPayAmount(self):
        """分摊费用(现金)：基于分摊规则分摊到分账单元的资源现金
        :rtype: str
        """
        return self._AllocateCashPayAmount

    @AllocateCashPayAmount.setter
    def AllocateCashPayAmount(self, AllocateCashPayAmount):
        self._AllocateCashPayAmount = AllocateCashPayAmount

    @property
    def AllocateVoucherPayAmount(self):
        """分摊费用(优惠券)：基于分摊规则分摊到分账单元的资源优惠券
        :rtype: str
        """
        return self._AllocateVoucherPayAmount

    @AllocateVoucherPayAmount.setter
    def AllocateVoucherPayAmount(self, AllocateVoucherPayAmount):
        self._AllocateVoucherPayAmount = AllocateVoucherPayAmount

    @property
    def AllocateIncentivePayAmount(self):
        """分摊费用(赠送金)：基于分摊规则分摊到分账单元的资源赠送金
        :rtype: str
        """
        return self._AllocateIncentivePayAmount

    @AllocateIncentivePayAmount.setter
    def AllocateIncentivePayAmount(self, AllocateIncentivePayAmount):
        self._AllocateIncentivePayAmount = AllocateIncentivePayAmount

    @property
    def AllocateTransferPayAmount(self):
        """分摊费用(分成金)：基于分摊规则分摊到分账单元的资源分成金
        :rtype: str
        """
        return self._AllocateTransferPayAmount

    @AllocateTransferPayAmount.setter
    def AllocateTransferPayAmount(self, AllocateTransferPayAmount):
        self._AllocateTransferPayAmount = AllocateTransferPayAmount

    @property
    def TotalCashPayAmount(self):
        """合计费用(现金)：分账单元总费用，归集费用(现金) + 分摊费用(现金)
        :rtype: str
        """
        return self._TotalCashPayAmount

    @TotalCashPayAmount.setter
    def TotalCashPayAmount(self, TotalCashPayAmount):
        self._TotalCashPayAmount = TotalCashPayAmount

    @property
    def TotalVoucherPayAmount(self):
        """合计费用(优惠券)：分账单元总费用，归集费用(优惠券) + 分摊费用(优惠券)
        :rtype: str
        """
        return self._TotalVoucherPayAmount

    @TotalVoucherPayAmount.setter
    def TotalVoucherPayAmount(self, TotalVoucherPayAmount):
        self._TotalVoucherPayAmount = TotalVoucherPayAmount

    @property
    def TotalIncentivePayAmount(self):
        """合计费用(赠送金)：分账单元总费用，归集费用(赠送金) + 分摊费用(赠送金)
        :rtype: str
        """
        return self._TotalIncentivePayAmount

    @TotalIncentivePayAmount.setter
    def TotalIncentivePayAmount(self, TotalIncentivePayAmount):
        self._TotalIncentivePayAmount = TotalIncentivePayAmount

    @property
    def TotalTransferPayAmount(self):
        """合计费用(分成金)：分账单元总费用，归集费用(分成金)+分摊费用(分成金)
        :rtype: str
        """
        return self._TotalTransferPayAmount

    @TotalTransferPayAmount.setter
    def TotalTransferPayAmount(self, TotalTransferPayAmount):
        self._TotalTransferPayAmount = TotalTransferPayAmount

    @property
    def GatherRealCost(self):
        """归集费用(折后总额)：基于归集规则直接归集到分账单元的资源优惠后总价
        :rtype: str
        """
        return self._GatherRealCost

    @GatherRealCost.setter
    def GatherRealCost(self, GatherRealCost):
        self._GatherRealCost = GatherRealCost

    @property
    def AllocateRealCost(self):
        """分摊费用(折后总额)：基于分摊规则分摊到分账单元的资源优惠后总价
        :rtype: str
        """
        return self._AllocateRealCost

    @AllocateRealCost.setter
    def AllocateRealCost(self, AllocateRealCost):
        self._AllocateRealCost = AllocateRealCost

    @property
    def RealTotalCost(self):
        """合计费用(折后总额)：分账单元总费用，归集费用(折后总额) + 分摊费用(折后总额)
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Ratio(self):
        """占比(折后总额)：本分账单元合计费用(折后总额)/合计费用(折后总额)*100%
        :rtype: str
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Trend(self):
        """环比(折后总额)：[本月分账单元合计费用(折后总额) - 上月分账单元合计费用(折后总额)] / 上月分账单元合计费用(折后总额) * 100%
        :rtype: str
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def TrendType(self):
        """环比箭头
upward -上升
downward - 下降
none - 平稳
        :rtype: str
        """
        return self._TrendType

    @TrendType.setter
    def TrendType(self, TrendType):
        self._TrendType = TrendType


    def _deserialize(self, params):
        self._GatherCashPayAmount = params.get("GatherCashPayAmount")
        self._GatherVoucherPayAmount = params.get("GatherVoucherPayAmount")
        self._GatherIncentivePayAmount = params.get("GatherIncentivePayAmount")
        self._GatherTransferPayAmount = params.get("GatherTransferPayAmount")
        self._AllocateCashPayAmount = params.get("AllocateCashPayAmount")
        self._AllocateVoucherPayAmount = params.get("AllocateVoucherPayAmount")
        self._AllocateIncentivePayAmount = params.get("AllocateIncentivePayAmount")
        self._AllocateTransferPayAmount = params.get("AllocateTransferPayAmount")
        self._TotalCashPayAmount = params.get("TotalCashPayAmount")
        self._TotalVoucherPayAmount = params.get("TotalVoucherPayAmount")
        self._TotalIncentivePayAmount = params.get("TotalIncentivePayAmount")
        self._TotalTransferPayAmount = params.get("TotalTransferPayAmount")
        self._GatherRealCost = params.get("GatherRealCost")
        self._AllocateRealCost = params.get("AllocateRealCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._Ratio = params.get("Ratio")
        self._Trend = params.get("Trend")
        self._TrendType = params.get("TrendType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationOverviewDetail(AbstractModel):
    """分账概览明细

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: 分账单元唯一标识
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: 分账单元名称
        :type TreeNodeUniqKeyName: str
        :param _BillDate: 日期：结算日期
        :type BillDate: str
        :param _GatherCashPayAmount: 归集费用(现金)：基于归集规则直接归集到分账单元的现金
        :type GatherCashPayAmount: str
        :param _GatherVoucherPayAmount: 归集费用(优惠券)：基于归集规则直接归集到分账单元的资源优惠券
        :type GatherVoucherPayAmount: str
        :param _GatherIncentivePayAmount: 归集费用(赠送金)：基于归集规则直接归集到分账单元的资源赠送金
        :type GatherIncentivePayAmount: str
        :param _GatherTransferPayAmount: 归集费用(分成金)：基于归集规则直接归集到分账单元的资源分成金
        :type GatherTransferPayAmount: str
        :param _AllocateCashPayAmount: 分摊费用(现金)：基于分摊规则分摊到分账单元的资源现金
        :type AllocateCashPayAmount: str
        :param _AllocateVoucherPayAmount: 分摊费用(优惠券)：基于分摊规则分摊到分账单元的资源优惠券
        :type AllocateVoucherPayAmount: str
        :param _AllocateIncentivePayAmount: 分摊费用(赠送金)：基于分摊规则分摊到分账单元的资源赠送金
        :type AllocateIncentivePayAmount: str
        :param _AllocateTransferPayAmount: 分摊费用(分成金)：基于分摊规则分摊到分账单元的资源分成金
        :type AllocateTransferPayAmount: str
        :param _TotalCashPayAmount: 合计费用(现金)：分账单元总费用，归集费用(现金) + 分摊费用(现金)
        :type TotalCashPayAmount: str
        :param _TotalVoucherPayAmount: 合计费用(优惠券)：分账单元总费用，归集费用(优惠券) + 分摊费用(优惠券)
        :type TotalVoucherPayAmount: str
        :param _TotalIncentivePayAmount: 合计费用(赠送金)：分账单元总费用，归集费用(赠送金) + 分摊费用(赠送金)
        :type TotalIncentivePayAmount: str
        :param _TotalTransferPayAmount: 合计费用(分成金)：分账单元总费用，归集费用(分成金)+分摊费用(分成金)
        :type TotalTransferPayAmount: str
        :param _GatherRealCost: 归集费用(折后总额)：基于归集规则直接归集到分账单元的资源优惠后总价
        :type GatherRealCost: str
        :param _AllocateRealCost: 分摊费用(折后总额)：基于分摊规则分摊到分账单元的资源优惠后总价
        :type AllocateRealCost: str
        :param _RealTotalCost: 合计费用(折后总额)：分账单元总费用，归集费用(折后总额) + 分摊费用(折后总额)
        :type RealTotalCost: str
        :param _Ratio: 占比(折后总额)：本分账单元合计费用(折后总额)/合计费用(折后总额)*100%
        :type Ratio: str
        :param _Trend: 环比(折后总额)：[本月分账单元合计费用(折后总额) - 上月分账单元合计费用(折后总额)] / 上月分账单元合计费用(折后总额) * 100%
        :type Trend: str
        :param _TrendType: 环比箭头
upward -上升
downward - 下降
none - 平稳
        :type TrendType: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._BillDate = None
        self._GatherCashPayAmount = None
        self._GatherVoucherPayAmount = None
        self._GatherIncentivePayAmount = None
        self._GatherTransferPayAmount = None
        self._AllocateCashPayAmount = None
        self._AllocateVoucherPayAmount = None
        self._AllocateIncentivePayAmount = None
        self._AllocateTransferPayAmount = None
        self._TotalCashPayAmount = None
        self._TotalVoucherPayAmount = None
        self._TotalIncentivePayAmount = None
        self._TotalTransferPayAmount = None
        self._GatherRealCost = None
        self._AllocateRealCost = None
        self._RealTotalCost = None
        self._Ratio = None
        self._Trend = None
        self._TrendType = None

    @property
    def TreeNodeUniqKey(self):
        """分账单元唯一标识
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        """分账单元名称
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def BillDate(self):
        """日期：结算日期
        :rtype: str
        """
        return self._BillDate

    @BillDate.setter
    def BillDate(self, BillDate):
        self._BillDate = BillDate

    @property
    def GatherCashPayAmount(self):
        """归集费用(现金)：基于归集规则直接归集到分账单元的现金
        :rtype: str
        """
        return self._GatherCashPayAmount

    @GatherCashPayAmount.setter
    def GatherCashPayAmount(self, GatherCashPayAmount):
        self._GatherCashPayAmount = GatherCashPayAmount

    @property
    def GatherVoucherPayAmount(self):
        """归集费用(优惠券)：基于归集规则直接归集到分账单元的资源优惠券
        :rtype: str
        """
        return self._GatherVoucherPayAmount

    @GatherVoucherPayAmount.setter
    def GatherVoucherPayAmount(self, GatherVoucherPayAmount):
        self._GatherVoucherPayAmount = GatherVoucherPayAmount

    @property
    def GatherIncentivePayAmount(self):
        """归集费用(赠送金)：基于归集规则直接归集到分账单元的资源赠送金
        :rtype: str
        """
        return self._GatherIncentivePayAmount

    @GatherIncentivePayAmount.setter
    def GatherIncentivePayAmount(self, GatherIncentivePayAmount):
        self._GatherIncentivePayAmount = GatherIncentivePayAmount

    @property
    def GatherTransferPayAmount(self):
        """归集费用(分成金)：基于归集规则直接归集到分账单元的资源分成金
        :rtype: str
        """
        return self._GatherTransferPayAmount

    @GatherTransferPayAmount.setter
    def GatherTransferPayAmount(self, GatherTransferPayAmount):
        self._GatherTransferPayAmount = GatherTransferPayAmount

    @property
    def AllocateCashPayAmount(self):
        """分摊费用(现金)：基于分摊规则分摊到分账单元的资源现金
        :rtype: str
        """
        return self._AllocateCashPayAmount

    @AllocateCashPayAmount.setter
    def AllocateCashPayAmount(self, AllocateCashPayAmount):
        self._AllocateCashPayAmount = AllocateCashPayAmount

    @property
    def AllocateVoucherPayAmount(self):
        """分摊费用(优惠券)：基于分摊规则分摊到分账单元的资源优惠券
        :rtype: str
        """
        return self._AllocateVoucherPayAmount

    @AllocateVoucherPayAmount.setter
    def AllocateVoucherPayAmount(self, AllocateVoucherPayAmount):
        self._AllocateVoucherPayAmount = AllocateVoucherPayAmount

    @property
    def AllocateIncentivePayAmount(self):
        """分摊费用(赠送金)：基于分摊规则分摊到分账单元的资源赠送金
        :rtype: str
        """
        return self._AllocateIncentivePayAmount

    @AllocateIncentivePayAmount.setter
    def AllocateIncentivePayAmount(self, AllocateIncentivePayAmount):
        self._AllocateIncentivePayAmount = AllocateIncentivePayAmount

    @property
    def AllocateTransferPayAmount(self):
        """分摊费用(分成金)：基于分摊规则分摊到分账单元的资源分成金
        :rtype: str
        """
        return self._AllocateTransferPayAmount

    @AllocateTransferPayAmount.setter
    def AllocateTransferPayAmount(self, AllocateTransferPayAmount):
        self._AllocateTransferPayAmount = AllocateTransferPayAmount

    @property
    def TotalCashPayAmount(self):
        """合计费用(现金)：分账单元总费用，归集费用(现金) + 分摊费用(现金)
        :rtype: str
        """
        return self._TotalCashPayAmount

    @TotalCashPayAmount.setter
    def TotalCashPayAmount(self, TotalCashPayAmount):
        self._TotalCashPayAmount = TotalCashPayAmount

    @property
    def TotalVoucherPayAmount(self):
        """合计费用(优惠券)：分账单元总费用，归集费用(优惠券) + 分摊费用(优惠券)
        :rtype: str
        """
        return self._TotalVoucherPayAmount

    @TotalVoucherPayAmount.setter
    def TotalVoucherPayAmount(self, TotalVoucherPayAmount):
        self._TotalVoucherPayAmount = TotalVoucherPayAmount

    @property
    def TotalIncentivePayAmount(self):
        """合计费用(赠送金)：分账单元总费用，归集费用(赠送金) + 分摊费用(赠送金)
        :rtype: str
        """
        return self._TotalIncentivePayAmount

    @TotalIncentivePayAmount.setter
    def TotalIncentivePayAmount(self, TotalIncentivePayAmount):
        self._TotalIncentivePayAmount = TotalIncentivePayAmount

    @property
    def TotalTransferPayAmount(self):
        """合计费用(分成金)：分账单元总费用，归集费用(分成金)+分摊费用(分成金)
        :rtype: str
        """
        return self._TotalTransferPayAmount

    @TotalTransferPayAmount.setter
    def TotalTransferPayAmount(self, TotalTransferPayAmount):
        self._TotalTransferPayAmount = TotalTransferPayAmount

    @property
    def GatherRealCost(self):
        """归集费用(折后总额)：基于归集规则直接归集到分账单元的资源优惠后总价
        :rtype: str
        """
        return self._GatherRealCost

    @GatherRealCost.setter
    def GatherRealCost(self, GatherRealCost):
        self._GatherRealCost = GatherRealCost

    @property
    def AllocateRealCost(self):
        """分摊费用(折后总额)：基于分摊规则分摊到分账单元的资源优惠后总价
        :rtype: str
        """
        return self._AllocateRealCost

    @AllocateRealCost.setter
    def AllocateRealCost(self, AllocateRealCost):
        self._AllocateRealCost = AllocateRealCost

    @property
    def RealTotalCost(self):
        """合计费用(折后总额)：分账单元总费用，归集费用(折后总额) + 分摊费用(折后总额)
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Ratio(self):
        """占比(折后总额)：本分账单元合计费用(折后总额)/合计费用(折后总额)*100%
        :rtype: str
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Trend(self):
        """环比(折后总额)：[本月分账单元合计费用(折后总额) - 上月分账单元合计费用(折后总额)] / 上月分账单元合计费用(折后总额) * 100%
        :rtype: str
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def TrendType(self):
        """环比箭头
upward -上升
downward - 下降
none - 平稳
        :rtype: str
        """
        return self._TrendType

    @TrendType.setter
    def TrendType(self, TrendType):
        self._TrendType = TrendType


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._BillDate = params.get("BillDate")
        self._GatherCashPayAmount = params.get("GatherCashPayAmount")
        self._GatherVoucherPayAmount = params.get("GatherVoucherPayAmount")
        self._GatherIncentivePayAmount = params.get("GatherIncentivePayAmount")
        self._GatherTransferPayAmount = params.get("GatherTransferPayAmount")
        self._AllocateCashPayAmount = params.get("AllocateCashPayAmount")
        self._AllocateVoucherPayAmount = params.get("AllocateVoucherPayAmount")
        self._AllocateIncentivePayAmount = params.get("AllocateIncentivePayAmount")
        self._AllocateTransferPayAmount = params.get("AllocateTransferPayAmount")
        self._TotalCashPayAmount = params.get("TotalCashPayAmount")
        self._TotalVoucherPayAmount = params.get("TotalVoucherPayAmount")
        self._TotalIncentivePayAmount = params.get("TotalIncentivePayAmount")
        self._TotalTransferPayAmount = params.get("TotalTransferPayAmount")
        self._GatherRealCost = params.get("GatherRealCost")
        self._AllocateRealCost = params.get("AllocateRealCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._Ratio = params.get("Ratio")
        self._Trend = params.get("Trend")
        self._TrendType = params.get("TrendType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationOverviewNode(AbstractModel):
    """分账账单月概览详情

    """

    def __init__(self):
        r"""
        :param _Id: 分账单元ID
        :type Id: int
        :param _Name: 分账单元名称
        :type Name: str
        :param _TreeNodeUniqKey: 分账单元唯一标识
        :type TreeNodeUniqKey: str
        :param _Symbol: 分账单元包含规则标志
0 - 不存在规则
1 - 同时存在归集规则和公摊规则
2 - 仅存在归集规则
3 - 仅存在公摊规则
        :type Symbol: int
        :param _Children: 子单元月概览详情
        :type Children: list of AllocationOverviewNode
        :param _Detail: 分账账单月概览金额明细
        :type Detail: :class:`tencentcloud.billing.v20180709.models.AllocationMonthOverviewDetail`
        """
        self._Id = None
        self._Name = None
        self._TreeNodeUniqKey = None
        self._Symbol = None
        self._Children = None
        self._Detail = None

    @property
    def Id(self):
        """分账单元ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """分账单元名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TreeNodeUniqKey(self):
        """分账单元唯一标识
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def Symbol(self):
        """分账单元包含规则标志
0 - 不存在规则
1 - 同时存在归集规则和公摊规则
2 - 仅存在归集规则
3 - 仅存在公摊规则
        :rtype: int
        """
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def Children(self):
        """子单元月概览详情
        :rtype: list of AllocationOverviewNode
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    @property
    def Detail(self):
        """分账账单月概览金额明细
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationMonthOverviewDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._Symbol = params.get("Symbol")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = AllocationOverviewNode()
                obj._deserialize(item)
                self._Children.append(obj)
        if params.get("Detail") is not None:
            self._Detail = AllocationMonthOverviewDetail()
            self._Detail._deserialize(params.get("Detail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationOverviewTotal(AbstractModel):
    """分账账单概览金额汇总

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: 总费用：现金费用合计+分成金费用合计+赠送金费用合计+优惠券费用合计
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalCost: str
        :param _CashPayAmount: 现金： 现金费用合计
注意：此字段可能返回 null，表示取不到有效值。
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送金：赠送金费用合计
注意：此字段可能返回 null，表示取不到有效值。
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 优惠券：优惠券费用合计
注意：此字段可能返回 null，表示取不到有效值。
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金：分成金费用合计
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferPayAmount: str
        """
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None

    @property
    def RealTotalCost(self):
        """总费用：现金费用合计+分成金费用合计+赠送金费用合计+优惠券费用合计
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金： 现金费用合计
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送金：赠送金费用合计
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        """优惠券：优惠券费用合计
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        """分成金：分成金费用合计
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount


    def _deserialize(self, params):
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
        


class AllocationRule(AbstractModel):
    """当前资源命中公摊规则信息

    """

    def __init__(self):
        r"""
        :param _RuleId: 公摊规则ID
        :type RuleId: int
        :param _RuleName: 公摊规则名称
        :type RuleName: str
        """
        self._RuleId = None
        self._RuleName = None

    @property
    def RuleId(self):
        """公摊规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """公摊规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationStat(AbstractModel):
    """分账账单趋势图

    """

    def __init__(self):
        r"""
        :param _Average: 费用平均信息
        :type Average: :class:`tencentcloud.billing.v20180709.models.AllocationAverageData`
        """
        self._Average = None

    @property
    def Average(self):
        """费用平均信息
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationAverageData`
        """
        return self._Average

    @Average.setter
    def Average(self, Average):
        self._Average = Average


    def _deserialize(self, params):
        if params.get("Average") is not None:
            self._Average = AllocationAverageData()
            self._Average._deserialize(params.get("Average"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationSummaryByBusiness(AbstractModel):
    """分账账单按产品汇总明细

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: 分账单元唯一标识
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: 分账单元名称
        :type TreeNodeUniqKeyName: str
        :param _BillDate: 日期：结算日期
        :type BillDate: str
        :param _GatherCashPayAmount: 归集费用(现金)：基于归集规则直接归集到分账单元的现金
        :type GatherCashPayAmount: str
        :param _GatherVoucherPayAmount: 归集费用(优惠券)：基于归集规则直接归集到分账单元的资源优惠券
        :type GatherVoucherPayAmount: str
        :param _GatherIncentivePayAmount: 归集费用(赠送金)：基于归集规则直接归集到分账单元的资源赠送金
        :type GatherIncentivePayAmount: str
        :param _GatherTransferPayAmount: 归集费用(分成金)：基于归集规则直接归集到分账单元的资源分成金
        :type GatherTransferPayAmount: str
        :param _AllocateCashPayAmount: 分摊费用(现金)：基于分摊规则分摊到分账单元的资源现金
        :type AllocateCashPayAmount: str
        :param _AllocateVoucherPayAmount: 分摊费用(优惠券)：基于分摊规则分摊到分账单元的资源优惠券
        :type AllocateVoucherPayAmount: str
        :param _AllocateIncentivePayAmount: 分摊费用(赠送金)：基于分摊规则分摊到分账单元的资源赠送金
        :type AllocateIncentivePayAmount: str
        :param _AllocateTransferPayAmount: 分摊费用(分成金)：基于分摊规则分摊到分账单元的资源分成金
        :type AllocateTransferPayAmount: str
        :param _TotalCashPayAmount: 合计费用(现金)：分账单元总费用，归集费用(现金) + 分摊费用(现金)
        :type TotalCashPayAmount: str
        :param _TotalVoucherPayAmount: 合计费用(优惠券)：分账单元总费用，归集费用(优惠券) + 分摊费用(优惠券)
        :type TotalVoucherPayAmount: str
        :param _TotalIncentivePayAmount: 合计费用(赠送金)：分账单元总费用，归集费用(赠送金) + 分摊费用(赠送金)
        :type TotalIncentivePayAmount: str
        :param _TotalTransferPayAmount: 合计费用(分成金)：分账单元总费用，归集费用(分成金)+分摊费用(分成金)
        :type TotalTransferPayAmount: str
        :param _GatherRealCost: 归集费用(折后总额)：基于归集规则直接归集到分账单元的资源优惠后总价
        :type GatherRealCost: str
        :param _AllocateRealCost: 分摊费用(折后总额)：基于分摊规则分摊到分账单元的资源优惠后总价
        :type AllocateRealCost: str
        :param _RealTotalCost: 合计费用(折后总额)：分账单元总费用，归集费用(折后总额) + 分摊费用(折后总额)
        :type RealTotalCost: str
        :param _Ratio: 占比(折后总额)：本分账单元合计费用(折后总额)/合计费用(折后总额)*100%
        :type Ratio: str
        :param _Trend: 环比(折后总额)：[本月分账单元合计费用(折后总额) - 上月分账单元合计费用(折后总额)] / 上月分账单元合计费用(折后总额) * 100%
        :type Trend: str
        :param _TrendType: 环比箭头
upward -上升
downward - 下降
none - 平稳
        :type TrendType: str
        :param _BusinessCode: 产品编码
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称：用户所采购的各类云产品
        :type BusinessCodeName: str
        :param _TotalCost: 组件原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如客户享受一口价/合同价则默认不展示，退费类场景也默认不展示），指定价模式
        :type TotalCost: str
        :param _RICost: 预留实例抵扣原价：本产品或服务使用预留实例抵扣的组件原价金额
        :type RICost: str
        :param _SPCost: 节省计划抵扣原价：节省计划抵扣原价 = 节省计划包抵扣面值 / 节省计划抵扣率
        :type SPCost: str
        :param _CashPayAmount: 现金账户支出(元)：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _VoucherPayAmount: 代金券支出(元)：使用各类优惠券（如代金券、现金券等）支付的金额

        :type VoucherPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出(元)：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _TransferPayAmount: 分成账户支出(元)：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param _AllocationRealTotalCost: 优惠后总价：优惠后总价 =（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :type AllocationRealTotalCost: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._BillDate = None
        self._GatherCashPayAmount = None
        self._GatherVoucherPayAmount = None
        self._GatherIncentivePayAmount = None
        self._GatherTransferPayAmount = None
        self._AllocateCashPayAmount = None
        self._AllocateVoucherPayAmount = None
        self._AllocateIncentivePayAmount = None
        self._AllocateTransferPayAmount = None
        self._TotalCashPayAmount = None
        self._TotalVoucherPayAmount = None
        self._TotalIncentivePayAmount = None
        self._TotalTransferPayAmount = None
        self._GatherRealCost = None
        self._AllocateRealCost = None
        self._RealTotalCost = None
        self._Ratio = None
        self._Trend = None
        self._TrendType = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._TotalCost = None
        self._RICost = None
        self._SPCost = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._AllocationRealTotalCost = None

    @property
    def TreeNodeUniqKey(self):
        """分账单元唯一标识
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        """分账单元名称
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def BillDate(self):
        """日期：结算日期
        :rtype: str
        """
        return self._BillDate

    @BillDate.setter
    def BillDate(self, BillDate):
        self._BillDate = BillDate

    @property
    def GatherCashPayAmount(self):
        """归集费用(现金)：基于归集规则直接归集到分账单元的现金
        :rtype: str
        """
        return self._GatherCashPayAmount

    @GatherCashPayAmount.setter
    def GatherCashPayAmount(self, GatherCashPayAmount):
        self._GatherCashPayAmount = GatherCashPayAmount

    @property
    def GatherVoucherPayAmount(self):
        """归集费用(优惠券)：基于归集规则直接归集到分账单元的资源优惠券
        :rtype: str
        """
        return self._GatherVoucherPayAmount

    @GatherVoucherPayAmount.setter
    def GatherVoucherPayAmount(self, GatherVoucherPayAmount):
        self._GatherVoucherPayAmount = GatherVoucherPayAmount

    @property
    def GatherIncentivePayAmount(self):
        """归集费用(赠送金)：基于归集规则直接归集到分账单元的资源赠送金
        :rtype: str
        """
        return self._GatherIncentivePayAmount

    @GatherIncentivePayAmount.setter
    def GatherIncentivePayAmount(self, GatherIncentivePayAmount):
        self._GatherIncentivePayAmount = GatherIncentivePayAmount

    @property
    def GatherTransferPayAmount(self):
        """归集费用(分成金)：基于归集规则直接归集到分账单元的资源分成金
        :rtype: str
        """
        return self._GatherTransferPayAmount

    @GatherTransferPayAmount.setter
    def GatherTransferPayAmount(self, GatherTransferPayAmount):
        self._GatherTransferPayAmount = GatherTransferPayAmount

    @property
    def AllocateCashPayAmount(self):
        """分摊费用(现金)：基于分摊规则分摊到分账单元的资源现金
        :rtype: str
        """
        return self._AllocateCashPayAmount

    @AllocateCashPayAmount.setter
    def AllocateCashPayAmount(self, AllocateCashPayAmount):
        self._AllocateCashPayAmount = AllocateCashPayAmount

    @property
    def AllocateVoucherPayAmount(self):
        """分摊费用(优惠券)：基于分摊规则分摊到分账单元的资源优惠券
        :rtype: str
        """
        return self._AllocateVoucherPayAmount

    @AllocateVoucherPayAmount.setter
    def AllocateVoucherPayAmount(self, AllocateVoucherPayAmount):
        self._AllocateVoucherPayAmount = AllocateVoucherPayAmount

    @property
    def AllocateIncentivePayAmount(self):
        """分摊费用(赠送金)：基于分摊规则分摊到分账单元的资源赠送金
        :rtype: str
        """
        return self._AllocateIncentivePayAmount

    @AllocateIncentivePayAmount.setter
    def AllocateIncentivePayAmount(self, AllocateIncentivePayAmount):
        self._AllocateIncentivePayAmount = AllocateIncentivePayAmount

    @property
    def AllocateTransferPayAmount(self):
        """分摊费用(分成金)：基于分摊规则分摊到分账单元的资源分成金
        :rtype: str
        """
        return self._AllocateTransferPayAmount

    @AllocateTransferPayAmount.setter
    def AllocateTransferPayAmount(self, AllocateTransferPayAmount):
        self._AllocateTransferPayAmount = AllocateTransferPayAmount

    @property
    def TotalCashPayAmount(self):
        """合计费用(现金)：分账单元总费用，归集费用(现金) + 分摊费用(现金)
        :rtype: str
        """
        return self._TotalCashPayAmount

    @TotalCashPayAmount.setter
    def TotalCashPayAmount(self, TotalCashPayAmount):
        self._TotalCashPayAmount = TotalCashPayAmount

    @property
    def TotalVoucherPayAmount(self):
        """合计费用(优惠券)：分账单元总费用，归集费用(优惠券) + 分摊费用(优惠券)
        :rtype: str
        """
        return self._TotalVoucherPayAmount

    @TotalVoucherPayAmount.setter
    def TotalVoucherPayAmount(self, TotalVoucherPayAmount):
        self._TotalVoucherPayAmount = TotalVoucherPayAmount

    @property
    def TotalIncentivePayAmount(self):
        """合计费用(赠送金)：分账单元总费用，归集费用(赠送金) + 分摊费用(赠送金)
        :rtype: str
        """
        return self._TotalIncentivePayAmount

    @TotalIncentivePayAmount.setter
    def TotalIncentivePayAmount(self, TotalIncentivePayAmount):
        self._TotalIncentivePayAmount = TotalIncentivePayAmount

    @property
    def TotalTransferPayAmount(self):
        """合计费用(分成金)：分账单元总费用，归集费用(分成金)+分摊费用(分成金)
        :rtype: str
        """
        return self._TotalTransferPayAmount

    @TotalTransferPayAmount.setter
    def TotalTransferPayAmount(self, TotalTransferPayAmount):
        self._TotalTransferPayAmount = TotalTransferPayAmount

    @property
    def GatherRealCost(self):
        """归集费用(折后总额)：基于归集规则直接归集到分账单元的资源优惠后总价
        :rtype: str
        """
        return self._GatherRealCost

    @GatherRealCost.setter
    def GatherRealCost(self, GatherRealCost):
        self._GatherRealCost = GatherRealCost

    @property
    def AllocateRealCost(self):
        """分摊费用(折后总额)：基于分摊规则分摊到分账单元的资源优惠后总价
        :rtype: str
        """
        return self._AllocateRealCost

    @AllocateRealCost.setter
    def AllocateRealCost(self, AllocateRealCost):
        self._AllocateRealCost = AllocateRealCost

    @property
    def RealTotalCost(self):
        """合计费用(折后总额)：分账单元总费用，归集费用(折后总额) + 分摊费用(折后总额)
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Ratio(self):
        """占比(折后总额)：本分账单元合计费用(折后总额)/合计费用(折后总额)*100%
        :rtype: str
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Trend(self):
        """环比(折后总额)：[本月分账单元合计费用(折后总额) - 上月分账单元合计费用(折后总额)] / 上月分账单元合计费用(折后总额) * 100%
        :rtype: str
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def TrendType(self):
        """环比箭头
upward -上升
downward - 下降
none - 平稳
        :rtype: str
        """
        return self._TrendType

    @TrendType.setter
    def TrendType(self, TrendType):
        self._TrendType = TrendType

    @property
    def BusinessCode(self):
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def TotalCost(self):
        """组件原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如客户享受一口价/合同价则默认不展示，退费类场景也默认不展示），指定价模式
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RICost(self):
        """预留实例抵扣原价：本产品或服务使用预留实例抵扣的组件原价金额
        :rtype: str
        """
        return self._RICost

    @RICost.setter
    def RICost(self, RICost):
        self._RICost = RICost

    @property
    def SPCost(self):
        """节省计划抵扣原价：节省计划抵扣原价 = 节省计划包抵扣面值 / 节省计划抵扣率
        :rtype: str
        """
        return self._SPCost

    @SPCost.setter
    def SPCost(self, SPCost):
        self._SPCost = SPCost

    @property
    def CashPayAmount(self):
        """现金账户支出(元)：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        """代金券支出(元)：使用各类优惠券（如代金券、现金券等）支付的金额

        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出(元)：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        """分成账户支出(元)：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def AllocationRealTotalCost(self):
        """优惠后总价：优惠后总价 =（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :rtype: str
        """
        return self._AllocationRealTotalCost

    @AllocationRealTotalCost.setter
    def AllocationRealTotalCost(self, AllocationRealTotalCost):
        self._AllocationRealTotalCost = AllocationRealTotalCost


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._BillDate = params.get("BillDate")
        self._GatherCashPayAmount = params.get("GatherCashPayAmount")
        self._GatherVoucherPayAmount = params.get("GatherVoucherPayAmount")
        self._GatherIncentivePayAmount = params.get("GatherIncentivePayAmount")
        self._GatherTransferPayAmount = params.get("GatherTransferPayAmount")
        self._AllocateCashPayAmount = params.get("AllocateCashPayAmount")
        self._AllocateVoucherPayAmount = params.get("AllocateVoucherPayAmount")
        self._AllocateIncentivePayAmount = params.get("AllocateIncentivePayAmount")
        self._AllocateTransferPayAmount = params.get("AllocateTransferPayAmount")
        self._TotalCashPayAmount = params.get("TotalCashPayAmount")
        self._TotalVoucherPayAmount = params.get("TotalVoucherPayAmount")
        self._TotalIncentivePayAmount = params.get("TotalIncentivePayAmount")
        self._TotalTransferPayAmount = params.get("TotalTransferPayAmount")
        self._GatherRealCost = params.get("GatherRealCost")
        self._AllocateRealCost = params.get("AllocateRealCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._Ratio = params.get("Ratio")
        self._Trend = params.get("Trend")
        self._TrendType = params.get("TrendType")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._TotalCost = params.get("TotalCost")
        self._RICost = params.get("RICost")
        self._SPCost = params.get("SPCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._AllocationRealTotalCost = params.get("AllocationRealTotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationSummaryByItem(AbstractModel):
    """分账账单按组件汇总明细

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: 分账单元唯一标识
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: 分账单元名称
        :type TreeNodeUniqKeyName: str
        :param _BillDate: 日期：结算日期
        :type BillDate: str
        :param _PayerUin: 支付者 UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :type PayerUin: str
        :param _OwnerUin: 使用者 UIN：实际使用资源的账号 ID
        :type OwnerUin: str
        :param _OperateUin: 操作者 UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的ID或者角色 ID）
        :type OperateUin: str
        :param _PayMode: 计费模式编码
        :type PayMode: str
        :param _PayModeName: 计费模式：资源的计费模式，区分为包年包月和按量计费
        :type PayModeName: str
        :param _ActionType: 交易类型编码
        :type ActionType: str
        :param _ActionTypeName: 交易类型：明细交易类型
        :type ActionTypeName: str
        :param _BusinessCode: 产品编码
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称：用户所采购的各类云产品
        :type BusinessCodeName: str
        :param _ProductCode: 子产品编码
        :type ProductCode: str
        :param _ProductCodeName: 子产品名称：用户采购的具体产品细分类型
        :type ProductCodeName: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _RegionName: 地域名称：资源所属地域
        :type RegionName: str
        :param _ZoneId: 可用区ID
        :type ZoneId: int
        :param _ZoneName: 可用区：资源所属可用区
        :type ZoneName: str
        :param _InstanceType: 实例类型编码
        :type InstanceType: str
        :param _InstanceTypeName: 实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。常规实例默认展示“-”
        :type InstanceTypeName: str
        :param _ResourceId: 资源ID：不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID； 若该产品被分拆，则展示产品分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
        :type ResourceId: str
        :param _ResourceName: 实例名称：用户在控制台为资源设置的名称，如未设置默认为空；若该产品被分拆，则展示分拆产品分拆后的分拆项资源别名
        :type ResourceName: str
        :param _Tag: 分账标签：资源绑定的标签
        :type Tag: list of BillTag
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _ProjectName: 项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :type ProjectName: str
        :param _AllocationType: 费用归集类型：费用来源类型，分摊、归集、未分配
0 - 分摊
1 - 归集
-1 - 未分配
        :type AllocationType: int
        :param _TotalCost: 组件原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如客户享受一口价/合同价则默认不展示，退费类场景也默认不展示），指定价模式
        :type TotalCost: str
        :param _RiTimeSpan: 预留实例抵扣时长：本产品或服务使用预留实例抵扣的使用时长
        :type RiTimeSpan: str
        :param _RiCost: 预留实例抵扣原价：本产品或服务使用预留实例抵扣的组件原价金额
        :type RiCost: str
        :param _RealTotalCost: 优惠后总价：优惠后总价 =（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出(元)：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _VoucherPayAmount: 代金券支出(元)：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出(元)：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _TransferPayAmount: 分成账户支出(元)：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param _ItemCode: 组件名称编码
        :type ItemCode: str
        :param _ItemCodeName: 组件名称：用户购买的产品或服务，所包含的具体组件
        :type ItemCodeName: str
        :param _ComponentCode: 组件类型编码
        :type ComponentCode: str
        :param _ComponentCodeName: 组件类型：用户购买的产品或服务对应的组件大类
        :type ComponentCodeName: str
        :param _SplitItemId: 分拆项 ID：涉及分拆产品的分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type SplitItemId: str
        :param _SplitItemName: 分拆项名称：涉及分拆产品的分拆后的分拆项
注意：此字段可能返回 null，表示取不到有效值。
        :type SplitItemName: str
        :param _FeeBeginTime: 开始使用时间：产品服务开始使用时间
        :type FeeBeginTime: str
        :param _FeeEndTime: 结束使用时间：产品服务结束使用时间
        :type FeeEndTime: str
        :param _SPCost: 节省计划抵扣原价：节省计划抵扣原价 = 节省计划包抵扣面值 / 节省计划抵扣率
        :type SPCost: str
        :param _RegionType: 国内国际编码
        :type RegionType: str
        :param _RegionTypeName: 国内国际：资源所属区域类型（国内、国际）
        :type RegionTypeName: str
        :param _SinglePrice: 组件刊例价：组件的官网原始单价（如客户享受一口价/合同价则默认不展示）
        :type SinglePrice: str
        :param _ContractPrice: 组件单价：组件的折后单价，组件单价 = 刊例价 * 折扣
        :type ContractPrice: str
        :param _SinglePriceUnit: 组件价格单位：组件价格的单位，单位构成：元/用量单位/时长单位
        :type SinglePriceUnit: str
        :param _UsedAmount: 组件用量：该组件实际结算用量，组件用量=组件原始用量-抵扣用量（含资源包）
        :type UsedAmount: str
        :param _UsedAmountUnit: 组件用量单位：组件用量对应的单位
        :type UsedAmountUnit: str
        :param _TimeSpan: 使用时长：资源使用的时长，组件用量=组件原始使用时长-抵扣时长（含资源包）
        :type TimeSpan: str
        :param _TimeUnit: 时长单位：资源使用时长的单位
        :type TimeUnit: str
        :param _ReserveDetail: 备注属性（实例配置）：其他备注信息，如预留实例的预留实例类型和交易类型、CCN 产品的两端地域信息
        :type ReserveDetail: str
        :param _RealTotalMeasure: 原始用量/时长：组件被资源包抵扣前的原始用量
（目前仅实时音视频、弹性微服务、云呼叫中心及专属可用区产品支持该信息外显，其他产品尚在接入中）
        :type RealTotalMeasure: str
        :param _DeductedMeasure: 抵扣用量/时长（含资源包）：组件被资源包抵扣的用量
（目前仅实时音视频、弹性微服务、云呼叫中心及专属可用区产品支持该信息外显，其他产品尚在接入中）
        :type DeductedMeasure: str
        :param _Discount: 折扣率：本资源享受的折扣率（如客户享受一口价/合同价则默认不展示，退费场景也默认不展示）
        :type Discount: str
        :param _BlendedDiscount: 混合折扣率：综合各类折扣抵扣信息后的最终折扣率，混合折扣率=优惠后总价/原价
        :type BlendedDiscount: str
        :param _PriceInfo: 价格属性：该组件除单价、时长外的其他影响折扣定价的属性信息
        :type PriceInfo: list of str
        :param _Formula: 计算规则说明：特殊交易类型计费结算的详细计算说明，如退费及变配
        :type Formula: str
        :param _FormulaUrl: 计费规则：各产品详细的计费规则官网说明链接
        :type FormulaUrl: str
        :param _ComponentConfig: 配置描述：资源配置规格信息
        :type ComponentConfig: str
        :param _SPDeduction: SPDeduction
        :type SPDeduction: str
        :param _SPDeductionRate: 节省计划抵扣率：节省计划可用余额额度范围内，节省计划对于此组件打的折扣率
        :type SPDeductionRate: str
        :param _AssociatedOrder: AssociatedOrder
        :type AssociatedOrder: str
        :param _DiscountObject: 当前消费项的优惠对象，例如：官网折扣、用户折扣、活动折扣。
        :type DiscountObject: str
        :param _DiscountType: 当前消费项的优惠类型，例如：折扣、合同价。
        :type DiscountType: str
        :param _DiscountContent: 对优惠类型的补充描述，例如：商务折扣8折，则优惠类型为“折扣”，优惠内容为“0.8”。
        :type DiscountContent: str
        :param _BillMonth: 账单月
        :type BillMonth: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._BillDate = None
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._PayMode = None
        self._PayModeName = None
        self._ActionType = None
        self._ActionTypeName = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._ProductCode = None
        self._ProductCodeName = None
        self._RegionId = None
        self._RegionName = None
        self._ZoneId = None
        self._ZoneName = None
        self._InstanceType = None
        self._InstanceTypeName = None
        self._ResourceId = None
        self._ResourceName = None
        self._Tag = None
        self._ProjectId = None
        self._ProjectName = None
        self._AllocationType = None
        self._TotalCost = None
        self._RiTimeSpan = None
        self._RiCost = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._ItemCode = None
        self._ItemCodeName = None
        self._ComponentCode = None
        self._ComponentCodeName = None
        self._SplitItemId = None
        self._SplitItemName = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._SPCost = None
        self._RegionType = None
        self._RegionTypeName = None
        self._SinglePrice = None
        self._ContractPrice = None
        self._SinglePriceUnit = None
        self._UsedAmount = None
        self._UsedAmountUnit = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._ReserveDetail = None
        self._RealTotalMeasure = None
        self._DeductedMeasure = None
        self._Discount = None
        self._BlendedDiscount = None
        self._PriceInfo = None
        self._Formula = None
        self._FormulaUrl = None
        self._ComponentConfig = None
        self._SPDeduction = None
        self._SPDeductionRate = None
        self._AssociatedOrder = None
        self._DiscountObject = None
        self._DiscountType = None
        self._DiscountContent = None
        self._BillMonth = None

    @property
    def TreeNodeUniqKey(self):
        """分账单元唯一标识
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        """分账单元名称
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def BillDate(self):
        """日期：结算日期
        :rtype: str
        """
        return self._BillDate

    @BillDate.setter
    def BillDate(self, BillDate):
        self._BillDate = BillDate

    @property
    def PayerUin(self):
        """支付者 UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        """使用者 UIN：实际使用资源的账号 ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        """操作者 UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的ID或者角色 ID）
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def PayMode(self):
        """计费模式编码
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        """计费模式：资源的计费模式，区分为包年包月和按量计费
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ActionType(self):
        """交易类型编码
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        """交易类型：明细交易类型
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def BusinessCode(self):
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        """子产品名称：用户采购的具体产品细分类型
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def RegionId(self):
        """地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称：资源所属地域
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

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
    def ZoneName(self):
        """可用区：资源所属可用区
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def InstanceType(self):
        """实例类型编码
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        """实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。常规实例默认展示“-”
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName

    @property
    def ResourceId(self):
        """资源ID：不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID； 若该产品被分拆，则展示产品分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """实例名称：用户在控制台为资源设置的名称，如未设置默认为空；若该产品被分拆，则展示分拆产品分拆后的分拆项资源别名
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Tag(self):
        """分账标签：资源绑定的标签
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def AllocationType(self):
        """费用归集类型：费用来源类型，分摊、归集、未分配
0 - 分摊
1 - 归集
-1 - 未分配
        :rtype: int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType

    @property
    def TotalCost(self):
        """组件原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如客户享受一口价/合同价则默认不展示，退费类场景也默认不展示），指定价模式
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RiTimeSpan(self):
        """预留实例抵扣时长：本产品或服务使用预留实例抵扣的使用时长
        :rtype: str
        """
        return self._RiTimeSpan

    @RiTimeSpan.setter
    def RiTimeSpan(self, RiTimeSpan):
        self._RiTimeSpan = RiTimeSpan

    @property
    def RiCost(self):
        """预留实例抵扣原价：本产品或服务使用预留实例抵扣的组件原价金额
        :rtype: str
        """
        return self._RiCost

    @RiCost.setter
    def RiCost(self, RiCost):
        self._RiCost = RiCost

    @property
    def RealTotalCost(self):
        """优惠后总价：优惠后总价 =（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出(元)：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        """代金券支出(元)：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出(元)：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        """分成账户支出(元)：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ItemCode(self):
        """组件名称编码
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ItemCodeName(self):
        """组件名称：用户购买的产品或服务，所包含的具体组件
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def ComponentCode(self):
        """组件类型编码
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ComponentCodeName(self):
        """组件类型：用户购买的产品或服务对应的组件大类
        :rtype: str
        """
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def SplitItemId(self):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        """分拆项 ID：涉及分拆产品的分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SplitItemId

    @SplitItemId.setter
    def SplitItemId(self, SplitItemId):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        self._SplitItemId = SplitItemId

    @property
    def SplitItemName(self):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        """分拆项名称：涉及分拆产品的分拆后的分拆项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SplitItemName

    @SplitItemName.setter
    def SplitItemName(self, SplitItemName):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        self._SplitItemName = SplitItemName

    @property
    def FeeBeginTime(self):
        """开始使用时间：产品服务开始使用时间
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        """结束使用时间：产品服务结束使用时间
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def SPCost(self):
        """节省计划抵扣原价：节省计划抵扣原价 = 节省计划包抵扣面值 / 节省计划抵扣率
        :rtype: str
        """
        return self._SPCost

    @SPCost.setter
    def SPCost(self, SPCost):
        self._SPCost = SPCost

    @property
    def RegionType(self):
        """国内国际编码
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        """国内国际：资源所属区域类型（国内、国际）
        :rtype: str
        """
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def SinglePrice(self):
        """组件刊例价：组件的官网原始单价（如客户享受一口价/合同价则默认不展示）
        :rtype: str
        """
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def ContractPrice(self):
        """组件单价：组件的折后单价，组件单价 = 刊例价 * 折扣
        :rtype: str
        """
        return self._ContractPrice

    @ContractPrice.setter
    def ContractPrice(self, ContractPrice):
        self._ContractPrice = ContractPrice

    @property
    def SinglePriceUnit(self):
        """组件价格单位：组件价格的单位，单位构成：元/用量单位/时长单位
        :rtype: str
        """
        return self._SinglePriceUnit

    @SinglePriceUnit.setter
    def SinglePriceUnit(self, SinglePriceUnit):
        self._SinglePriceUnit = SinglePriceUnit

    @property
    def UsedAmount(self):
        """组件用量：该组件实际结算用量，组件用量=组件原始用量-抵扣用量（含资源包）
        :rtype: str
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        """组件用量单位：组件用量对应的单位
        :rtype: str
        """
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def TimeSpan(self):
        """使用时长：资源使用的时长，组件用量=组件原始使用时长-抵扣时长（含资源包）
        :rtype: str
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """时长单位：资源使用时长的单位
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def ReserveDetail(self):
        """备注属性（实例配置）：其他备注信息，如预留实例的预留实例类型和交易类型、CCN 产品的两端地域信息
        :rtype: str
        """
        return self._ReserveDetail

    @ReserveDetail.setter
    def ReserveDetail(self, ReserveDetail):
        self._ReserveDetail = ReserveDetail

    @property
    def RealTotalMeasure(self):
        """原始用量/时长：组件被资源包抵扣前的原始用量
（目前仅实时音视频、弹性微服务、云呼叫中心及专属可用区产品支持该信息外显，其他产品尚在接入中）
        :rtype: str
        """
        return self._RealTotalMeasure

    @RealTotalMeasure.setter
    def RealTotalMeasure(self, RealTotalMeasure):
        self._RealTotalMeasure = RealTotalMeasure

    @property
    def DeductedMeasure(self):
        """抵扣用量/时长（含资源包）：组件被资源包抵扣的用量
（目前仅实时音视频、弹性微服务、云呼叫中心及专属可用区产品支持该信息外显，其他产品尚在接入中）
        :rtype: str
        """
        return self._DeductedMeasure

    @DeductedMeasure.setter
    def DeductedMeasure(self, DeductedMeasure):
        self._DeductedMeasure = DeductedMeasure

    @property
    def Discount(self):
        """折扣率：本资源享受的折扣率（如客户享受一口价/合同价则默认不展示，退费场景也默认不展示）
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def BlendedDiscount(self):
        """混合折扣率：综合各类折扣抵扣信息后的最终折扣率，混合折扣率=优惠后总价/原价
        :rtype: str
        """
        return self._BlendedDiscount

    @BlendedDiscount.setter
    def BlendedDiscount(self, BlendedDiscount):
        self._BlendedDiscount = BlendedDiscount

    @property
    def PriceInfo(self):
        """价格属性：该组件除单价、时长外的其他影响折扣定价的属性信息
        :rtype: list of str
        """
        return self._PriceInfo

    @PriceInfo.setter
    def PriceInfo(self, PriceInfo):
        self._PriceInfo = PriceInfo

    @property
    def Formula(self):
        """计算规则说明：特殊交易类型计费结算的详细计算说明，如退费及变配
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def FormulaUrl(self):
        """计费规则：各产品详细的计费规则官网说明链接
        :rtype: str
        """
        return self._FormulaUrl

    @FormulaUrl.setter
    def FormulaUrl(self, FormulaUrl):
        self._FormulaUrl = FormulaUrl

    @property
    def ComponentConfig(self):
        """配置描述：资源配置规格信息
        :rtype: str
        """
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig

    @property
    def SPDeduction(self):
        """SPDeduction
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        self._SPDeduction = SPDeduction

    @property
    def SPDeductionRate(self):
        """节省计划抵扣率：节省计划可用余额额度范围内，节省计划对于此组件打的折扣率
        :rtype: str
        """
        return self._SPDeductionRate

    @SPDeductionRate.setter
    def SPDeductionRate(self, SPDeductionRate):
        self._SPDeductionRate = SPDeductionRate

    @property
    def AssociatedOrder(self):
        """AssociatedOrder
        :rtype: str
        """
        return self._AssociatedOrder

    @AssociatedOrder.setter
    def AssociatedOrder(self, AssociatedOrder):
        self._AssociatedOrder = AssociatedOrder

    @property
    def DiscountObject(self):
        """当前消费项的优惠对象，例如：官网折扣、用户折扣、活动折扣。
        :rtype: str
        """
        return self._DiscountObject

    @DiscountObject.setter
    def DiscountObject(self, DiscountObject):
        self._DiscountObject = DiscountObject

    @property
    def DiscountType(self):
        """当前消费项的优惠类型，例如：折扣、合同价。
        :rtype: str
        """
        return self._DiscountType

    @DiscountType.setter
    def DiscountType(self, DiscountType):
        self._DiscountType = DiscountType

    @property
    def DiscountContent(self):
        """对优惠类型的补充描述，例如：商务折扣8折，则优惠类型为“折扣”，优惠内容为“0.8”。
        :rtype: str
        """
        return self._DiscountContent

    @DiscountContent.setter
    def DiscountContent(self, DiscountContent):
        self._DiscountContent = DiscountContent

    @property
    def BillMonth(self):
        """账单月
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._BillDate = params.get("BillDate")
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._AllocationType = params.get("AllocationType")
        self._TotalCost = params.get("TotalCost")
        self._RiTimeSpan = params.get("RiTimeSpan")
        self._RiCost = params.get("RiCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._ItemCode = params.get("ItemCode")
        self._ItemCodeName = params.get("ItemCodeName")
        self._ComponentCode = params.get("ComponentCode")
        self._ComponentCodeName = params.get("ComponentCodeName")
        self._SplitItemId = params.get("SplitItemId")
        self._SplitItemName = params.get("SplitItemName")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        self._SPCost = params.get("SPCost")
        self._RegionType = params.get("RegionType")
        self._RegionTypeName = params.get("RegionTypeName")
        self._SinglePrice = params.get("SinglePrice")
        self._ContractPrice = params.get("ContractPrice")
        self._SinglePriceUnit = params.get("SinglePriceUnit")
        self._UsedAmount = params.get("UsedAmount")
        self._UsedAmountUnit = params.get("UsedAmountUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._ReserveDetail = params.get("ReserveDetail")
        self._RealTotalMeasure = params.get("RealTotalMeasure")
        self._DeductedMeasure = params.get("DeductedMeasure")
        self._Discount = params.get("Discount")
        self._BlendedDiscount = params.get("BlendedDiscount")
        self._PriceInfo = params.get("PriceInfo")
        self._Formula = params.get("Formula")
        self._FormulaUrl = params.get("FormulaUrl")
        self._ComponentConfig = params.get("ComponentConfig")
        self._SPDeduction = params.get("SPDeduction")
        self._SPDeductionRate = params.get("SPDeductionRate")
        self._AssociatedOrder = params.get("AssociatedOrder")
        self._DiscountObject = params.get("DiscountObject")
        self._DiscountType = params.get("DiscountType")
        self._DiscountContent = params.get("DiscountContent")
        self._BillMonth = params.get("BillMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationSummaryByResource(AbstractModel):
    """分账账单按资源汇总明细

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: 分账单元唯一标识
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: 分账单元名称
        :type TreeNodeUniqKeyName: str
        :param _BillDate: 日期：结算日期
        :type BillDate: str
        :param _PayerUin: 支付者 UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :type PayerUin: str
        :param _OwnerUin: 使用者 UIN：实际使用资源的账号 ID
        :type OwnerUin: str
        :param _OperateUin: 操作者 UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的ID或者角色 ID）
        :type OperateUin: str
        :param _PayMode: 计费模式编码
        :type PayMode: str
        :param _PayModeName: 计费模式：资源的计费模式，区分为包年包月和按量计费
        :type PayModeName: str
        :param _ActionType: 交易类型编码
        :type ActionType: str
        :param _ActionTypeName: 交易类型：明细交易类型
        :type ActionTypeName: str
        :param _BusinessCode: 产品编码
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称：用户所采购的各类云产品
        :type BusinessCodeName: str
        :param _ProductCode: 子产品编码
        :type ProductCode: str
        :param _ProductCodeName: 子产品名称：用户采购的具体产品细分类型
        :type ProductCodeName: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _RegionName: 地域名称：资源所属地域
        :type RegionName: str
        :param _ZoneId: 可用区ID
        :type ZoneId: int
        :param _ZoneName: 可用区：资源所属可用区
        :type ZoneName: str
        :param _InstanceType: 实例类型编码
        :type InstanceType: str
        :param _InstanceTypeName: 实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。常规实例默认展示“-”
        :type InstanceTypeName: str
        :param _ResourceId: 资源ID：不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID； 若该产品被分拆，则展示产品分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
        :type ResourceId: str
        :param _ResourceName: 实例名称：用户在控制台为资源设置的名称，如未设置默认为空；若该产品被分拆，则展示分拆产品分拆后的分拆项资源别名
        :type ResourceName: str
        :param _Tag: 分账标签：资源绑定的标签
        :type Tag: list of BillTag
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _ProjectName: 项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :type ProjectName: str
        :param _AllocationType: 费用归集类型：费用来源类型，分摊、归集、未分配
0 - 分摊 
1 - 归集 
-1 -  未分配
        :type AllocationType: int
        :param _TotalCost: 组件原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如客户享受一口价/合同价则默认不展示，退费类场景也默认不展示），指定价模式
        :type TotalCost: str
        :param _RiTimeSpan: 预留实例抵扣时长：本产品或服务使用预留实例抵扣的使用时长
        :type RiTimeSpan: str
        :param _RiCost: 预留实例抵扣原价：本产品或服务使用预留实例抵扣的组件原价金额
        :type RiCost: str
        :param _RealTotalCost: 优惠后总价：优惠后总价 =（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出(元)：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _VoucherPayAmount: 代金券支出(元)：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出(元)：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _TransferPayAmount: 分成账户支出(元)：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param _SplitItemId: 分拆项 ID：涉及分拆产品的分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type SplitItemId: str
        :param _SplitItemName: 分拆项名称：涉及分拆产品的分拆后的分拆项
注意：此字段可能返回 null，表示取不到有效值。
        :type SplitItemName: str
        :param _FeeBeginTime: 开始使用时间：产品服务开始使用时间
        :type FeeBeginTime: str
        :param _FeeEndTime: 结束使用时间：产品服务结束使用时间
        :type FeeEndTime: str
        :param _SPCost: 节省计划抵扣原价：节省计划抵扣原价 = 节省计划包抵扣面值 / 节省计划抵扣率
        :type SPCost: str
        :param _RegionType: 国内国际编码
        :type RegionType: str
        :param _RegionTypeName: 国内国际：资源所属区域类型（国内、国际）
        :type RegionTypeName: str
        :param _ComponentConfig: 配置描述：对应资源下各组件名称及用量（如组件为用量累加型计费则为合计用量）
        :type ComponentConfig: str
        :param _SPDeduction: SPDeduction
        :type SPDeduction: str
        :param _BillMonth: 账单月
        :type BillMonth: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._BillDate = None
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._PayMode = None
        self._PayModeName = None
        self._ActionType = None
        self._ActionTypeName = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._ProductCode = None
        self._ProductCodeName = None
        self._RegionId = None
        self._RegionName = None
        self._ZoneId = None
        self._ZoneName = None
        self._InstanceType = None
        self._InstanceTypeName = None
        self._ResourceId = None
        self._ResourceName = None
        self._Tag = None
        self._ProjectId = None
        self._ProjectName = None
        self._AllocationType = None
        self._TotalCost = None
        self._RiTimeSpan = None
        self._RiCost = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._SplitItemId = None
        self._SplitItemName = None
        self._FeeBeginTime = None
        self._FeeEndTime = None
        self._SPCost = None
        self._RegionType = None
        self._RegionTypeName = None
        self._ComponentConfig = None
        self._SPDeduction = None
        self._BillMonth = None

    @property
    def TreeNodeUniqKey(self):
        """分账单元唯一标识
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        """分账单元名称
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def BillDate(self):
        """日期：结算日期
        :rtype: str
        """
        return self._BillDate

    @BillDate.setter
    def BillDate(self, BillDate):
        self._BillDate = BillDate

    @property
    def PayerUin(self):
        """支付者 UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        """使用者 UIN：实际使用资源的账号 ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        """操作者 UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的ID或者角色 ID）
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def PayMode(self):
        """计费模式编码
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        """计费模式：资源的计费模式，区分为包年包月和按量计费
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ActionType(self):
        """交易类型编码
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        """交易类型：明细交易类型
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def BusinessCode(self):
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        """子产品名称：用户采购的具体产品细分类型
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def RegionId(self):
        """地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称：资源所属地域
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

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
    def ZoneName(self):
        """可用区：资源所属可用区
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def InstanceType(self):
        """实例类型编码
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        """实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。常规实例默认展示“-”
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName

    @property
    def ResourceId(self):
        """资源ID：不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID； 若该产品被分拆，则展示产品分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """实例名称：用户在控制台为资源设置的名称，如未设置默认为空；若该产品被分拆，则展示分拆产品分拆后的分拆项资源别名
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Tag(self):
        """分账标签：资源绑定的标签
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def AllocationType(self):
        """费用归集类型：费用来源类型，分摊、归集、未分配
0 - 分摊 
1 - 归集 
-1 -  未分配
        :rtype: int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType

    @property
    def TotalCost(self):
        """组件原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如客户享受一口价/合同价则默认不展示，退费类场景也默认不展示），指定价模式
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RiTimeSpan(self):
        """预留实例抵扣时长：本产品或服务使用预留实例抵扣的使用时长
        :rtype: str
        """
        return self._RiTimeSpan

    @RiTimeSpan.setter
    def RiTimeSpan(self, RiTimeSpan):
        self._RiTimeSpan = RiTimeSpan

    @property
    def RiCost(self):
        """预留实例抵扣原价：本产品或服务使用预留实例抵扣的组件原价金额
        :rtype: str
        """
        return self._RiCost

    @RiCost.setter
    def RiCost(self, RiCost):
        self._RiCost = RiCost

    @property
    def RealTotalCost(self):
        """优惠后总价：优惠后总价 =（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出(元)：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        """代金券支出(元)：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出(元)：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        """分成账户支出(元)：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def SplitItemId(self):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        """分拆项 ID：涉及分拆产品的分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SplitItemId

    @SplitItemId.setter
    def SplitItemId(self, SplitItemId):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        self._SplitItemId = SplitItemId

    @property
    def SplitItemName(self):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        """分拆项名称：涉及分拆产品的分拆后的分拆项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SplitItemName

    @SplitItemName.setter
    def SplitItemName(self, SplitItemName):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        self._SplitItemName = SplitItemName

    @property
    def FeeBeginTime(self):
        """开始使用时间：产品服务开始使用时间
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        """结束使用时间：产品服务结束使用时间
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def SPCost(self):
        """节省计划抵扣原价：节省计划抵扣原价 = 节省计划包抵扣面值 / 节省计划抵扣率
        :rtype: str
        """
        return self._SPCost

    @SPCost.setter
    def SPCost(self, SPCost):
        self._SPCost = SPCost

    @property
    def RegionType(self):
        """国内国际编码
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        """国内国际：资源所属区域类型（国内、国际）
        :rtype: str
        """
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def ComponentConfig(self):
        """配置描述：对应资源下各组件名称及用量（如组件为用量累加型计费则为合计用量）
        :rtype: str
        """
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig

    @property
    def SPDeduction(self):
        """SPDeduction
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        self._SPDeduction = SPDeduction

    @property
    def BillMonth(self):
        """账单月
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._BillDate = params.get("BillDate")
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._AllocationType = params.get("AllocationType")
        self._TotalCost = params.get("TotalCost")
        self._RiTimeSpan = params.get("RiTimeSpan")
        self._RiCost = params.get("RiCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._SplitItemId = params.get("SplitItemId")
        self._SplitItemName = params.get("SplitItemName")
        self._FeeBeginTime = params.get("FeeBeginTime")
        self._FeeEndTime = params.get("FeeEndTime")
        self._SPCost = params.get("SPCost")
        self._RegionType = params.get("RegionType")
        self._RegionTypeName = params.get("RegionTypeName")
        self._ComponentConfig = params.get("ComponentConfig")
        self._SPDeduction = params.get("SPDeduction")
        self._BillMonth = params.get("BillMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocationTreeNode(AbstractModel):
    """当前归属单元信息

    """

    def __init__(self):
        r"""
        :param _TreeNodeUniqKey: 分账单元唯一标识
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: 分账单元名称
        :type TreeNodeUniqKeyName: str
        """
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None

    @property
    def TreeNodeUniqKey(self):
        """分账单元唯一标识
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        """分账单元名称
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName


    def _deserialize(self, params):
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseActionTypeDetail(AbstractModel):
    """成本分析交易类型复杂类型

    """

    def __init__(self):
        r"""
        :param _ActionType: 交易类型code
        :type ActionType: str
        :param _ActionTypeName: 交易类型Name
        :type ActionTypeName: str
        """
        self._ActionType = None
        self._ActionTypeName = None

    @property
    def ActionType(self):
        """交易类型code
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        """交易类型Name
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName


    def _deserialize(self, params):
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseAmountDetail(AbstractModel):
    """成本分析金额返回数据模型

    """

    def __init__(self):
        r"""
        :param _Key: 费用类型
        :type Key: str
        :param _Display: 是否展示
        :type Display: int
        """
        self._Key = None
        self._Display = None

    @property
    def Key(self):
        """费用类型
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Display(self):
        """是否展示
        :rtype: int
        """
        return self._Display

    @Display.setter
    def Display(self, Display):
        self._Display = Display


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Display = params.get("Display")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseBusinessDetail(AbstractModel):
    """成本分析产品返回复杂类型

    """

    def __init__(self):
        r"""
        :param _BusinessCode: 产品码code
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None

    @property
    def BusinessCode(self):
        """产品码code
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称
        :rtype: str
        """
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
        


class AnalyseConditionDetail(AbstractModel):
    """成本分析过滤框复杂类型

    """

    def __init__(self):
        r"""
        :param _Business: 产品
        :type Business: list of AnalyseBusinessDetail
        :param _Project: 项目
        :type Project: list of AnalyseProjectDetail
        :param _Region: 地域
        :type Region: list of AnalyseRegionDetail
        :param _PayMode: 计费模式
        :type PayMode: list of AnalysePayModeDetail
        :param _ActionType: 交易类型
        :type ActionType: list of AnalyseActionTypeDetail
        :param _Zone: 可用区
        :type Zone: list of AnalyseZoneDetail
        :param _OwnerUin: 资源所有者Uin
        :type OwnerUin: list of AnalyseOwnerUinDetail
        :param _Amount: 费用类型
        :type Amount: list of AnalyseAmountDetail
        """
        self._Business = None
        self._Project = None
        self._Region = None
        self._PayMode = None
        self._ActionType = None
        self._Zone = None
        self._OwnerUin = None
        self._Amount = None

    @property
    def Business(self):
        """产品
        :rtype: list of AnalyseBusinessDetail
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Project(self):
        """项目
        :rtype: list of AnalyseProjectDetail
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Region(self):
        """地域
        :rtype: list of AnalyseRegionDetail
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayMode(self):
        """计费模式
        :rtype: list of AnalysePayModeDetail
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ActionType(self):
        """交易类型
        :rtype: list of AnalyseActionTypeDetail
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Zone(self):
        """可用区
        :rtype: list of AnalyseZoneDetail
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def OwnerUin(self):
        """资源所有者Uin
        :rtype: list of AnalyseOwnerUinDetail
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Amount(self):
        """费用类型
        :rtype: list of AnalyseAmountDetail
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount


    def _deserialize(self, params):
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = AnalyseBusinessDetail()
                obj._deserialize(item)
                self._Business.append(obj)
        if params.get("Project") is not None:
            self._Project = []
            for item in params.get("Project"):
                obj = AnalyseProjectDetail()
                obj._deserialize(item)
                self._Project.append(obj)
        if params.get("Region") is not None:
            self._Region = []
            for item in params.get("Region"):
                obj = AnalyseRegionDetail()
                obj._deserialize(item)
                self._Region.append(obj)
        if params.get("PayMode") is not None:
            self._PayMode = []
            for item in params.get("PayMode"):
                obj = AnalysePayModeDetail()
                obj._deserialize(item)
                self._PayMode.append(obj)
        if params.get("ActionType") is not None:
            self._ActionType = []
            for item in params.get("ActionType"):
                obj = AnalyseActionTypeDetail()
                obj._deserialize(item)
                self._ActionType.append(obj)
        if params.get("Zone") is not None:
            self._Zone = []
            for item in params.get("Zone"):
                obj = AnalyseZoneDetail()
                obj._deserialize(item)
                self._Zone.append(obj)
        if params.get("OwnerUin") is not None:
            self._OwnerUin = []
            for item in params.get("OwnerUin"):
                obj = AnalyseOwnerUinDetail()
                obj._deserialize(item)
                self._OwnerUin.append(obj)
        if params.get("Amount") is not None:
            self._Amount = []
            for item in params.get("Amount"):
                obj = AnalyseAmountDetail()
                obj._deserialize(item)
                self._Amount.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseConditions(AbstractModel):
    """成本分析查询条件

    """

    def __init__(self):
        r"""
        :param _BusinessCodes: 产品名称代码
        :type BusinessCodes: str
        :param _ProductCodes: 子产品名称代码
        :type ProductCodes: str
        :param _ComponentCode: 组件类型代码
        :type ComponentCode: str
        :param _ZoneIds: 可用区ID：资源所属可用区ID
        :type ZoneIds: str
        :param _RegionIds: 地域ID:资源所属地域ID
        :type RegionIds: str
        :param _ProjectIds: 项目ID:资源所属项目ID
        :type ProjectIds: str
        :param _PayModes: 计费模式 prePay(表示包年包月)/postPay(表示按量计费)
        :type PayModes: str
        :param _ActionTypes: 交易类型，查询交易类型（请使用交易类型code入参）
        :type ActionTypes: str
        :param _Tags: 分账标签键
        :type Tags: str
        :param _FeeType: 费用类型，查询费用类型（请使用费用类型code入参)入参枚举如下：
cashPayAmount:现金 
incentivePayAmount:赠送金 
voucherPayAmount:优惠券 
tax:税金 
costBeforeTax:税前价
        :type FeeType: str
        :param _PayerUins: 查询成本分析数据的用户UIN
        :type PayerUins: str
        :param _OwnerUins: 使用资源的用户UIN
        :type OwnerUins: str
        :param _ConsumptionTypes: 消耗类型，查询消耗类型（请使用消耗类型code入参）
        :type ConsumptionTypes: str
        """
        self._BusinessCodes = None
        self._ProductCodes = None
        self._ComponentCode = None
        self._ZoneIds = None
        self._RegionIds = None
        self._ProjectIds = None
        self._PayModes = None
        self._ActionTypes = None
        self._Tags = None
        self._FeeType = None
        self._PayerUins = None
        self._OwnerUins = None
        self._ConsumptionTypes = None

    @property
    def BusinessCodes(self):
        """产品名称代码
        :rtype: str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def ProductCodes(self):
        """子产品名称代码
        :rtype: str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def ComponentCode(self):
        """组件类型代码
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ZoneIds(self):
        """可用区ID：资源所属可用区ID
        :rtype: str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def RegionIds(self):
        """地域ID:资源所属地域ID
        :rtype: str
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ProjectIds(self):
        """项目ID:资源所属项目ID
        :rtype: str
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def PayModes(self):
        """计费模式 prePay(表示包年包月)/postPay(表示按量计费)
        :rtype: str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        """交易类型，查询交易类型（请使用交易类型code入参）
        :rtype: str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def Tags(self):
        """分账标签键
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def FeeType(self):
        """费用类型，查询费用类型（请使用费用类型code入参)入参枚举如下：
cashPayAmount:现金 
incentivePayAmount:赠送金 
voucherPayAmount:优惠券 
tax:税金 
costBeforeTax:税前价
        :rtype: str
        """
        return self._FeeType

    @FeeType.setter
    def FeeType(self, FeeType):
        self._FeeType = FeeType

    @property
    def PayerUins(self):
        """查询成本分析数据的用户UIN
        :rtype: str
        """
        return self._PayerUins

    @PayerUins.setter
    def PayerUins(self, PayerUins):
        self._PayerUins = PayerUins

    @property
    def OwnerUins(self):
        """使用资源的用户UIN
        :rtype: str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def ConsumptionTypes(self):
        """消耗类型，查询消耗类型（请使用消耗类型code入参）
        :rtype: str
        """
        return self._ConsumptionTypes

    @ConsumptionTypes.setter
    def ConsumptionTypes(self, ConsumptionTypes):
        self._ConsumptionTypes = ConsumptionTypes


    def _deserialize(self, params):
        self._BusinessCodes = params.get("BusinessCodes")
        self._ProductCodes = params.get("ProductCodes")
        self._ComponentCode = params.get("ComponentCode")
        self._ZoneIds = params.get("ZoneIds")
        self._RegionIds = params.get("RegionIds")
        self._ProjectIds = params.get("ProjectIds")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._Tags = params.get("Tags")
        self._FeeType = params.get("FeeType")
        self._PayerUins = params.get("PayerUins")
        self._OwnerUins = params.get("OwnerUins")
        self._ConsumptionTypes = params.get("ConsumptionTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseDetail(AbstractModel):
    """成本分析数据复杂类型

    """

    def __init__(self):
        r"""
        :param _Name: 时间
        :type Name: str
        :param _Total: 金额
        :type Total: str
        :param _TimeDetail: 日期明细金额
        :type TimeDetail: list of AnalyseTimeDetail
        """
        self._Name = None
        self._Total = None
        self._TimeDetail = None

    @property
    def Name(self):
        """时间
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        """金额
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TimeDetail(self):
        """日期明细金额
        :rtype: list of AnalyseTimeDetail
        """
        return self._TimeDetail

    @TimeDetail.setter
    def TimeDetail(self, TimeDetail):
        self._TimeDetail = TimeDetail


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Total = params.get("Total")
        if params.get("TimeDetail") is not None:
            self._TimeDetail = []
            for item in params.get("TimeDetail"):
                obj = AnalyseTimeDetail()
                obj._deserialize(item)
                self._TimeDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseHeaderDetail(AbstractModel):
    """成本分析表头数据复杂类型

    """

    def __init__(self):
        r"""
        :param _HeadDetail: 表头日期
        :type HeadDetail: list of AnalyseHeaderTimeDetail
        :param _Name: 时间
        :type Name: str
        :param _Total: 总计
        :type Total: str
        """
        self._HeadDetail = None
        self._Name = None
        self._Total = None

    @property
    def HeadDetail(self):
        """表头日期
        :rtype: list of AnalyseHeaderTimeDetail
        """
        return self._HeadDetail

    @HeadDetail.setter
    def HeadDetail(self, HeadDetail):
        self._HeadDetail = HeadDetail

    @property
    def Name(self):
        """时间
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        """总计
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        if params.get("HeadDetail") is not None:
            self._HeadDetail = []
            for item in params.get("HeadDetail"):
                obj = AnalyseHeaderTimeDetail()
                obj._deserialize(item)
                self._HeadDetail.append(obj)
        self._Name = params.get("Name")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseHeaderTimeDetail(AbstractModel):
    """成本分析header表头数据

    """

    def __init__(self):
        r"""
        :param _Name: 日期
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """日期
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
        


class AnalyseOwnerUinDetail(AbstractModel):
    """成本分析使用者uin复杂类型

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 使用者uin
        :type OwnerUin: str
        """
        self._OwnerUin = None

    @property
    def OwnerUin(self):
        """使用者uin
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalysePayModeDetail(AbstractModel):
    """成本分析支付方式复杂类型

    """

    def __init__(self):
        r"""
        :param _PayMode: 计费模式code
        :type PayMode: str
        :param _PayModeName: 计费模式Name
        :type PayModeName: str
        """
        self._PayMode = None
        self._PayModeName = None

    @property
    def PayMode(self):
        """计费模式code
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        """计费模式Name
        :rtype: str
        """
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
        


class AnalyseProjectDetail(AbstractModel):
    """成本分析项目返回复杂类型

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _ProjectName: 默认项目
        :type ProjectName: str
        """
        self._ProjectId = None
        self._ProjectName = None

    @property
    def ProjectId(self):
        """项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """默认项目
        :rtype: str
        """
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
        


class AnalyseRegionDetail(AbstractModel):
    """成本分析地域返回复杂类型

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域id
        :type RegionId: str
        :param _RegionName: 地域名称
        :type RegionName: str
        """
        self._RegionId = None
        self._RegionName = None

    @property
    def RegionId(self):
        """地域id
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称
        :rtype: str
        """
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
        


class AnalyseTimeDetail(AbstractModel):
    """成本分返回值复杂类型

    """

    def __init__(self):
        r"""
        :param _Time: 日期
        :type Time: str
        :param _Money: 金额
        :type Money: str
        """
        self._Time = None
        self._Money = None

    @property
    def Time(self):
        """日期
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Money(self):
        """金额
        :rtype: str
        """
        return self._Money

    @Money.setter
    def Money(self, Money):
        self._Money = Money


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Money = params.get("Money")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseZoneDetail(AbstractModel):
    """成本分析可用区复杂类型

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区id
        :type ZoneId: str
        :param _ZoneName: 可用区Name
        :type ZoneName: str
        """
        self._ZoneId = None
        self._ZoneName = None

    @property
    def ZoneId(self):
        """可用区id
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """可用区Name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
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
        """适用商品名称，值为“全产品通用”或商品名称组成的string，以","分割。
        :rtype: str
        """
        return self._GoodsName

    @GoodsName.setter
    def GoodsName(self, GoodsName):
        self._GoodsName = GoodsName

    @property
    def PayMode(self):
        """postPay后付费/prePay预付费/riPay预留实例/空字符串或者"*"表示全部模式。如GoodsName为多个商品名以","分割组成的string，而PayMode为"*"，表示每一件商品的模式都为"*"。
        :rtype: str
        """
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
        


class BillActionType(AbstractModel):
    """交易类型筛选列表

    """

    def __init__(self):
        r"""
        :param _ActionType: 交易类型编码
        :type ActionType: str
        :param _ActionTypeName: 交易类型：明细交易类型
        :type ActionTypeName: str
        """
        self._ActionType = None
        self._ActionTypeName = None

    @property
    def ActionType(self):
        """交易类型编码
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        """交易类型：明细交易类型
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName


    def _deserialize(self, params):
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillBusiness(AbstractModel):
    """产品筛选列表

    """

    def __init__(self):
        r"""
        :param _BusinessCode: 产品编码

        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称：用户所采购的各类云产品
        :type BusinessCodeName: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None

    @property
    def BusinessCode(self):
        """产品编码

        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品
        :rtype: str
        """
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
        


class BillBusinessLink(AbstractModel):
    """产品级联筛选值

    """

    def __init__(self):
        r"""
        :param _BusinessCode: 产品编码
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称
        :type BusinessCodeName: str
        :param _Children: 子产品
        :type Children: list of BillProductLink
        """
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._Children = None

    @property
    def BusinessCode(self):
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def Children(self):
        """子产品
        :rtype: list of BillProductLink
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = BillProductLink()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillComponent(AbstractModel):
    """组件类型筛选列表

    """

    def __init__(self):
        r"""
        :param _ComponentCode: 组件类型编码
        :type ComponentCode: str
        :param _ComponentCodeName: 组件类型：用户购买的产品或服务对应的组件大类
        :type ComponentCodeName: str
        """
        self._ComponentCode = None
        self._ComponentCodeName = None

    @property
    def ComponentCode(self):
        """组件类型编码
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ComponentCodeName(self):
        """组件类型：用户购买的产品或服务对应的组件大类
        :rtype: str
        """
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName


    def _deserialize(self, params):
        self._ComponentCode = params.get("ComponentCode")
        self._ComponentCodeName = params.get("ComponentCodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDays(AbstractModel):
    """日期筛选列表

    """

    def __init__(self):
        r"""
        :param _BillDay: 日期：结算日期
        :type BillDay: str
        """
        self._BillDay = None

    @property
    def BillDay(self):
        """日期：结算日期
        :rtype: str
        """
        return self._BillDay

    @BillDay.setter
    def BillDay(self, BillDay):
        self._BillDay = BillDay


    def _deserialize(self, params):
        self._BillDay = params.get("BillDay")
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
        :type Tags: list of BillTagInfo
        :param _BusinessCode: 产品编码
        :type BusinessCode: str
        :param _ProductCode: 子产品编码
        :type ProductCode: str
        :param _ActionType: 交易类型编码
        :type ActionType: str
        :param _RegionId: 地域ID
        :type RegionId: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _PriceInfo: 价格属性：该组件除单价、时长外的其他影响折扣定价的属性信息
        :type PriceInfo: list of str
        :param _AssociatedOrder: 关联交易单据ID：和本笔交易关联单据 ID，如，冲销订单，记录原订单、重结订单，退费单记录对应的原购买订单号
        :type AssociatedOrder: :class:`tencentcloud.billing.v20180709.models.BillDetailAssociatedOrder`
        :param _Formula: 计算说明：特殊交易类型计费结算的详细计算说明，如退费及变配
        :type Formula: str
        :param _FormulaUrl: 计费规则：各产品详细的计费规则官网说明链接
        :type FormulaUrl: str
        :param _BillDay: 账单归属日
        :type BillDay: str
        :param _BillMonth: 账单归属月
        :type BillMonth: str
        :param _Id: 账单记录ID
        :type Id: str
        :param _RegionType: 国内国际编码
        :type RegionType: str
        :param _RegionTypeName: 国内国际：资源所属区域类型（国内、国际）
        :type RegionTypeName: str
        :param _ReserveDetail: 备注属性（实例配置）：其他备注信息，如预留实例的预留实例类型和交易类型、CCN 产品的两端地域信息
        :type ReserveDetail: str
        :param _DiscountObject: 优惠对象
        :type DiscountObject: str
        :param _DiscountType: 优惠类型
        :type DiscountType: str
        :param _DiscountContent: 优惠内容
        :type DiscountContent: str
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
        self._AssociatedOrder = None
        self._Formula = None
        self._FormulaUrl = None
        self._BillDay = None
        self._BillMonth = None
        self._Id = None
        self._RegionType = None
        self._RegionTypeName = None
        self._ReserveDetail = None
        self._DiscountObject = None
        self._DiscountType = None
        self._DiscountContent = None

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        """子产品名称：用户采购的具体产品细分类型，例如：云服务器 CVM-标准型 S1
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        """计费模式：资源的计费模式，区分为包年包月和按量计费
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        """项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        """地域：资源所属地域，如华南地区（广州）
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        """可用区：资源所属可用区，如广州三区
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        """资源 ID：账单中出账对象 ID，不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """资源别名：用户在控制台为资源设置的名称，如果未设置，则默认为空
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        """交易类型，如包年包月新购、包年包月续费、按量计费扣费等类型
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        """订单ID：包年包月计费模式下订购的订单号
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        """交易ID：结算扣费单号
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def PayTime(self):
        """扣费时间：结算扣费时间
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        """开始使用时间：产品服务开始使用时间
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        """结束使用时间：产品服务结束使用时间
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentSet(self):
        """组件列表
        :rtype: list of BillDetailComponent
        """
        return self._ComponentSet

    @ComponentSet.setter
    def ComponentSet(self, ComponentSet):
        self._ComponentSet = ComponentSet

    @property
    def PayerUin(self):
        """支付者UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        """使用者UIN：实际使用资源的账号 ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        """操作者UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的 ID 或者角色 ID ）
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def Tags(self):
        """标签信息
        :rtype: list of BillTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def BusinessCode(self):
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ActionType(self):
        """交易类型编码
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def RegionId(self):
        """地域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PriceInfo(self):
        """价格属性：该组件除单价、时长外的其他影响折扣定价的属性信息
        :rtype: list of str
        """
        return self._PriceInfo

    @PriceInfo.setter
    def PriceInfo(self, PriceInfo):
        self._PriceInfo = PriceInfo

    @property
    def AssociatedOrder(self):
        """关联交易单据ID：和本笔交易关联单据 ID，如，冲销订单，记录原订单、重结订单，退费单记录对应的原购买订单号
        :rtype: :class:`tencentcloud.billing.v20180709.models.BillDetailAssociatedOrder`
        """
        return self._AssociatedOrder

    @AssociatedOrder.setter
    def AssociatedOrder(self, AssociatedOrder):
        self._AssociatedOrder = AssociatedOrder

    @property
    def Formula(self):
        """计算说明：特殊交易类型计费结算的详细计算说明，如退费及变配
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def FormulaUrl(self):
        """计费规则：各产品详细的计费规则官网说明链接
        :rtype: str
        """
        return self._FormulaUrl

    @FormulaUrl.setter
    def FormulaUrl(self, FormulaUrl):
        self._FormulaUrl = FormulaUrl

    @property
    def BillDay(self):
        """账单归属日
        :rtype: str
        """
        return self._BillDay

    @BillDay.setter
    def BillDay(self, BillDay):
        self._BillDay = BillDay

    @property
    def BillMonth(self):
        """账单归属月
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def Id(self):
        """账单记录ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RegionType(self):
        """国内国际编码
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        """国内国际：资源所属区域类型（国内、国际）
        :rtype: str
        """
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def ReserveDetail(self):
        """备注属性（实例配置）：其他备注信息，如预留实例的预留实例类型和交易类型、CCN 产品的两端地域信息
        :rtype: str
        """
        return self._ReserveDetail

    @ReserveDetail.setter
    def ReserveDetail(self, ReserveDetail):
        self._ReserveDetail = ReserveDetail

    @property
    def DiscountObject(self):
        """优惠对象
        :rtype: str
        """
        return self._DiscountObject

    @DiscountObject.setter
    def DiscountObject(self, DiscountObject):
        self._DiscountObject = DiscountObject

    @property
    def DiscountType(self):
        """优惠类型
        :rtype: str
        """
        return self._DiscountType

    @DiscountType.setter
    def DiscountType(self, DiscountType):
        self._DiscountType = DiscountType

    @property
    def DiscountContent(self):
        """优惠内容
        :rtype: str
        """
        return self._DiscountContent

    @DiscountContent.setter
    def DiscountContent(self, DiscountContent):
        self._DiscountContent = DiscountContent


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
        if params.get("AssociatedOrder") is not None:
            self._AssociatedOrder = BillDetailAssociatedOrder()
            self._AssociatedOrder._deserialize(params.get("AssociatedOrder"))
        self._Formula = params.get("Formula")
        self._FormulaUrl = params.get("FormulaUrl")
        self._BillDay = params.get("BillDay")
        self._BillMonth = params.get("BillMonth")
        self._Id = params.get("Id")
        self._RegionType = params.get("RegionType")
        self._RegionTypeName = params.get("RegionTypeName")
        self._ReserveDetail = params.get("ReserveDetail")
        self._DiscountObject = params.get("DiscountObject")
        self._DiscountType = params.get("DiscountType")
        self._DiscountContent = params.get("DiscountContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetailAssociatedOrder(AbstractModel):
    """明细账单关联单据信息

    """

    def __init__(self):
        r"""
        :param _PrepayPurchase: 新购订单
        :type PrepayPurchase: str
        :param _PrepayRenew: 续费订单
        :type PrepayRenew: str
        :param _PrepayModifyUp: 升配订单
        :type PrepayModifyUp: str
        :param _ReverseOrder: 冲销订单
        :type ReverseOrder: str
        :param _NewOrder: 优惠调整后订单
        :type NewOrder: str
        :param _Original: 优惠调整前订单
        :type Original: str
        """
        self._PrepayPurchase = None
        self._PrepayRenew = None
        self._PrepayModifyUp = None
        self._ReverseOrder = None
        self._NewOrder = None
        self._Original = None

    @property
    def PrepayPurchase(self):
        """新购订单
        :rtype: str
        """
        return self._PrepayPurchase

    @PrepayPurchase.setter
    def PrepayPurchase(self, PrepayPurchase):
        self._PrepayPurchase = PrepayPurchase

    @property
    def PrepayRenew(self):
        """续费订单
        :rtype: str
        """
        return self._PrepayRenew

    @PrepayRenew.setter
    def PrepayRenew(self, PrepayRenew):
        self._PrepayRenew = PrepayRenew

    @property
    def PrepayModifyUp(self):
        """升配订单
        :rtype: str
        """
        return self._PrepayModifyUp

    @PrepayModifyUp.setter
    def PrepayModifyUp(self, PrepayModifyUp):
        self._PrepayModifyUp = PrepayModifyUp

    @property
    def ReverseOrder(self):
        """冲销订单
        :rtype: str
        """
        return self._ReverseOrder

    @ReverseOrder.setter
    def ReverseOrder(self, ReverseOrder):
        self._ReverseOrder = ReverseOrder

    @property
    def NewOrder(self):
        """优惠调整后订单
        :rtype: str
        """
        return self._NewOrder

    @NewOrder.setter
    def NewOrder(self, NewOrder):
        self._NewOrder = NewOrder

    @property
    def Original(self):
        """优惠调整前订单
        :rtype: str
        """
        return self._Original

    @Original.setter
    def Original(self, Original):
        self._Original = Original


    def _deserialize(self, params):
        self._PrepayPurchase = params.get("PrepayPurchase")
        self._PrepayRenew = params.get("PrepayRenew")
        self._PrepayModifyUp = params.get("PrepayModifyUp")
        self._ReverseOrder = params.get("ReverseOrder")
        self._NewOrder = params.get("NewOrder")
        self._Original = params.get("Original")
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
        :type RealTotalMeasure: str
        :param _DeductedMeasure: 抵扣用量/时长（含资源包）：组件被资源包抵扣的用量/时长
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
        :type TransferPayAmount: str
        :param _ItemCode: 组件类型编码
        :type ItemCode: str
        :param _ComponentCode: 组件名称编码
        :type ComponentCode: str
        :param _ContractPrice: 组件单价：组件的折后单价，组件单价 = 刊例价 * 折扣
        :type ContractPrice: str
        :param _InstanceType: 实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。正常的实例展示默认为不展示
        :type InstanceType: str
        :param _RiTimeSpan: 预留实例抵扣的使用时长：本产品或服务使用预留实例抵扣的使用时长
        :type RiTimeSpan: str
        :param _OriginalCostWithRI: 预留实例抵扣组件原价：本产品或服务使用预留实例抵扣的组件原价金额
        :type OriginalCostWithRI: str
        :param _SPDeductionRate: 节省计划抵扣率：节省计划可用余额额度范围内，节省计划对于此组件打的折扣率
        :type SPDeductionRate: str
        :param _SPDeduction: 节省计划抵扣金额（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type SPDeduction: str
        :param _OriginalCostWithSP: 节省计划抵扣组件原价：节省计划抵扣原价=节省计划包抵扣金额/节省计划抵扣率
        :type OriginalCostWithSP: str
        :param _BlendedDiscount: 混合折扣率：综合各类折扣抵扣信息后的最终折扣率，混合折扣率 = 优惠后总价 / 组件原价
        :type BlendedDiscount: str
        :param _ComponentConfig: 配置描述：资源配置规格信息
        :type ComponentConfig: list of BillDetailComponentConfig
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
        self._ComponentConfig = None

    @property
    def ComponentCodeName(self):
        """组件类型：用户购买的产品或服务对应的组件大类，例如：云服务器 CVM 的组件：CPU、内存等
        :rtype: str
        """
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def ItemCodeName(self):
        """组件名称：用户购买的产品或服务，所包含的具体组件
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def SinglePrice(self):
        """组件刊例价：组件的官网原始单价（如果客户享受一口价/合同价则默认不展示）
        :rtype: str
        """
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def SpecifiedPrice(self):
        warnings.warn("parameter `SpecifiedPrice` is deprecated", DeprecationWarning) 

        """组件指定价（已废弃）
        :rtype: str
        """
        return self._SpecifiedPrice

    @SpecifiedPrice.setter
    def SpecifiedPrice(self, SpecifiedPrice):
        warnings.warn("parameter `SpecifiedPrice` is deprecated", DeprecationWarning) 

        self._SpecifiedPrice = SpecifiedPrice

    @property
    def PriceUnit(self):
        """组件价格单位：组件价格的单位，单位构成：元/用量单位/时长单位
        :rtype: str
        """
        return self._PriceUnit

    @PriceUnit.setter
    def PriceUnit(self, PriceUnit):
        self._PriceUnit = PriceUnit

    @property
    def UsedAmount(self):
        """组件用量：该组件实际结算用量，组件用量 = 组件原始用量 - 抵扣用量（含资源包
        :rtype: str
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        """组件用量单位：组件用量对应的单位
        :rtype: str
        """
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def RealTotalMeasure(self):
        """原始用量/时长：组件被资源包抵扣前的原始用量/时长
        :rtype: str
        """
        return self._RealTotalMeasure

    @RealTotalMeasure.setter
    def RealTotalMeasure(self, RealTotalMeasure):
        self._RealTotalMeasure = RealTotalMeasure

    @property
    def DeductedMeasure(self):
        """抵扣用量/时长（含资源包）：组件被资源包抵扣的用量/时长
        :rtype: str
        """
        return self._DeductedMeasure

    @DeductedMeasure.setter
    def DeductedMeasure(self, DeductedMeasure):
        self._DeductedMeasure = DeductedMeasure

    @property
    def TimeSpan(self):
        """使用时长：资源使用的时长
        :rtype: str
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnitName(self):
        """时长单位：资源使用时长的单位
        :rtype: str
        """
        return self._TimeUnitName

    @TimeUnitName.setter
    def TimeUnitName(self, TimeUnitName):
        self._TimeUnitName = TimeUnitName

    @property
    def Cost(self):
        """组件原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如果客户享受一口价/合同价则默认不展示，退费类场景也默认不展示）
        :rtype: str
        """
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def Discount(self):
        """折扣率：本资源享受的折扣率（如果客户享受一口价/合同价则默认不展示，退费场景也默认不展示）
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ReduceType(self):
        """优惠类型
        :rtype: str
        """
        return self._ReduceType

    @ReduceType.setter
    def ReduceType(self, ReduceType):
        self._ReduceType = ReduceType

    @property
    def RealCost(self):
        """优惠后总价：优惠后总价=（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :rtype: str
        """
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ItemCode(self):
        """组件类型编码
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ComponentCode(self):
        """组件名称编码
        :rtype: str
        """
        return self._ComponentCode

    @ComponentCode.setter
    def ComponentCode(self, ComponentCode):
        self._ComponentCode = ComponentCode

    @property
    def ContractPrice(self):
        """组件单价：组件的折后单价，组件单价 = 刊例价 * 折扣
        :rtype: str
        """
        return self._ContractPrice

    @ContractPrice.setter
    def ContractPrice(self, ContractPrice):
        self._ContractPrice = ContractPrice

    @property
    def InstanceType(self):
        """实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。正常的实例展示默认为不展示
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def RiTimeSpan(self):
        """预留实例抵扣的使用时长：本产品或服务使用预留实例抵扣的使用时长
        :rtype: str
        """
        return self._RiTimeSpan

    @RiTimeSpan.setter
    def RiTimeSpan(self, RiTimeSpan):
        self._RiTimeSpan = RiTimeSpan

    @property
    def OriginalCostWithRI(self):
        """预留实例抵扣组件原价：本产品或服务使用预留实例抵扣的组件原价金额
        :rtype: str
        """
        return self._OriginalCostWithRI

    @OriginalCostWithRI.setter
    def OriginalCostWithRI(self, OriginalCostWithRI):
        self._OriginalCostWithRI = OriginalCostWithRI

    @property
    def SPDeductionRate(self):
        """节省计划抵扣率：节省计划可用余额额度范围内，节省计划对于此组件打的折扣率
        :rtype: str
        """
        return self._SPDeductionRate

    @SPDeductionRate.setter
    def SPDeductionRate(self, SPDeductionRate):
        self._SPDeductionRate = SPDeductionRate

    @property
    def SPDeduction(self):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        """节省计划抵扣金额（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        self._SPDeduction = SPDeduction

    @property
    def OriginalCostWithSP(self):
        """节省计划抵扣组件原价：节省计划抵扣原价=节省计划包抵扣金额/节省计划抵扣率
        :rtype: str
        """
        return self._OriginalCostWithSP

    @OriginalCostWithSP.setter
    def OriginalCostWithSP(self, OriginalCostWithSP):
        self._OriginalCostWithSP = OriginalCostWithSP

    @property
    def BlendedDiscount(self):
        """混合折扣率：综合各类折扣抵扣信息后的最终折扣率，混合折扣率 = 优惠后总价 / 组件原价
        :rtype: str
        """
        return self._BlendedDiscount

    @BlendedDiscount.setter
    def BlendedDiscount(self, BlendedDiscount):
        self._BlendedDiscount = BlendedDiscount

    @property
    def ComponentConfig(self):
        """配置描述：资源配置规格信息
        :rtype: list of BillDetailComponentConfig
        """
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig


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
        if params.get("ComponentConfig") is not None:
            self._ComponentConfig = []
            for item in params.get("ComponentConfig"):
                obj = BillDetailComponentConfig()
                obj._deserialize(item)
                self._ComponentConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDetailComponentConfig(AbstractModel):
    """明细账单配置描述结构

    """

    def __init__(self):
        r"""
        :param _Name: 配置描述名称
        :type Name: str
        :param _Value: 配置描述值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """配置描述名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """配置描述值
        :rtype: str
        """
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
        


class BillDistributionResourceSummary(AbstractModel):
    """经销账单资源汇总数据对象

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
        :type TransferPayAmount: str
        :param _ExtendField3: 扩展字段3：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField3: str
        :param _ExtendField4: 扩展字段4：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField4: str
        :param _ExtendField5: 扩展字段5：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField5: str
        :param _Tags: 标签信息
        :type Tags: list of BillTagInfo
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
        :param _BillMonth: 账单归属月
        :type BillMonth: str
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
        self._OwnerUin = None
        self._OperateUin = None
        self._BusinessCode = None
        self._ProductCode = None
        self._RegionId = None
        self._InstanceType = None
        self._OriginalCostWithRI = None
        self._SPDeduction = None
        self._OriginalCostWithSP = None
        self._BillMonth = None

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        """子产品名称：用户采购的具体产品细分类型，例如：云服务器 CVM-标准型 S1
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        """计费模式：资源的计费模式，区分为包年包月和按量计费
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        """项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        """地域：资源所属地域，如华南地区（广州）
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        """可用区：资源所属可用区，如广州三区
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        """资源 ID：账单中出账对象 ID，不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID	
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """资源别名：用户在控制台为资源设置的名称，如果未设置，则默认为空
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        """交易类型：如包年包月新购、包年包月续费、按量计费扣费等类型
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        """订单ID：包年包月计费模式下订购的订单号
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def PayTime(self):
        """扣费时间：结算扣费时间
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        """开始使用时间：产品服务开始使用时间
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        """结束使用时间：产品服务结束使用时间
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ConfigDesc(self):
        """配置描述：该资源下的计费项名称和用量合并展示，仅在资源账单体现
        :rtype: str
        """
        return self._ConfigDesc

    @ConfigDesc.setter
    def ConfigDesc(self, ConfigDesc):
        self._ConfigDesc = ConfigDesc

    @property
    def ExtendField1(self):
        """扩展字段1：产品对应的扩展属性信息，仅在资源账单体现
        :rtype: str
        """
        return self._ExtendField1

    @ExtendField1.setter
    def ExtendField1(self, ExtendField1):
        self._ExtendField1 = ExtendField1

    @property
    def ExtendField2(self):
        """扩展字段2：产品对应的扩展属性信息，仅在资源账单体现
        :rtype: str
        """
        return self._ExtendField2

    @ExtendField2.setter
    def ExtendField2(self, ExtendField2):
        self._ExtendField2 = ExtendField2

    @property
    def TotalCost(self):
        """原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如果客户享受一口价/合同价则默认不展示，退费类场景也默认不展示）
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Discount(self):
        """折扣率：本资源享受的折扣率（如果客户享受一口价/合同价则默认不展示，退费场景也默认不展示）
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ReduceType(self):
        """优惠类型
        :rtype: str
        """
        return self._ReduceType

    @ReduceType.setter
    def ReduceType(self, ReduceType):
        self._ReduceType = ReduceType

    @property
    def RealTotalCost(self):
        """优惠后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ExtendField3(self):
        """扩展字段3：产品对应的扩展属性信息，仅在资源账单体现
        :rtype: str
        """
        return self._ExtendField3

    @ExtendField3.setter
    def ExtendField3(self, ExtendField3):
        self._ExtendField3 = ExtendField3

    @property
    def ExtendField4(self):
        """扩展字段4：产品对应的扩展属性信息，仅在资源账单体现
        :rtype: str
        """
        return self._ExtendField4

    @ExtendField4.setter
    def ExtendField4(self, ExtendField4):
        self._ExtendField4 = ExtendField4

    @property
    def ExtendField5(self):
        """扩展字段5：产品对应的扩展属性信息，仅在资源账单体现
        :rtype: str
        """
        return self._ExtendField5

    @ExtendField5.setter
    def ExtendField5(self, ExtendField5):
        self._ExtendField5 = ExtendField5

    @property
    def Tags(self):
        """标签信息
        :rtype: list of BillTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def OwnerUin(self):
        """使用者UIN：实际使用资源的账号 ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        """操作者UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的 ID 或者角色 ID ）
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def BusinessCode(self):
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def RegionId(self):
        """地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def InstanceType(self):
        """实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。正常的实例展示默认为不展示
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OriginalCostWithRI(self):
        """预留实例抵扣组件原价：本产品或服务使用预留实例抵扣的组件原价金额	
        :rtype: str
        """
        return self._OriginalCostWithRI

    @OriginalCostWithRI.setter
    def OriginalCostWithRI(self, OriginalCostWithRI):
        self._OriginalCostWithRI = OriginalCostWithRI

    @property
    def SPDeduction(self):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        """节省计划抵扣金额（已废弃）
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        self._SPDeduction = SPDeduction

    @property
    def OriginalCostWithSP(self):
        """节省计划抵扣组件原价：节省计划抵扣原价=节省计划包抵扣金额/节省计划抵扣率	
        :rtype: str
        """
        return self._OriginalCostWithSP

    @OriginalCostWithSP.setter
    def OriginalCostWithSP(self, OriginalCostWithSP):
        self._OriginalCostWithSP = OriginalCostWithSP

    @property
    def BillMonth(self):
        """账单归属月
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth


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
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._BusinessCode = params.get("BusinessCode")
        self._ProductCode = params.get("ProductCode")
        self._RegionId = params.get("RegionId")
        self._InstanceType = params.get("InstanceType")
        self._OriginalCostWithRI = params.get("OriginalCostWithRI")
        self._SPDeduction = params.get("SPDeduction")
        self._OriginalCostWithSP = params.get("OriginalCostWithSP")
        self._BillMonth = params.get("BillMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillInstanceType(AbstractModel):
    """实例类型筛选列表

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型编码
        :type InstanceType: str
        :param _InstanceTypeName: 实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。常规实例默认展示“-”
        :type InstanceTypeName: str
        """
        self._InstanceType = None
        self._InstanceTypeName = None

    @property
    def InstanceType(self):
        """实例类型编码
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        """实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。常规实例默认展示“-”
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillItem(AbstractModel):
    """组件名称筛选列表

    """

    def __init__(self):
        r"""
        :param _ItemCode: 组件名称编码
        :type ItemCode: str
        :param _ItemCodeName: 组件名称：用户购买的产品或服务，所包含的具体组件
        :type ItemCodeName: str
        """
        self._ItemCode = None
        self._ItemCodeName = None

    @property
    def ItemCode(self):
        """组件名称编码
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ItemCodeName(self):
        """组件名称：用户购买的产品或服务，所包含的具体组件
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName


    def _deserialize(self, params):
        self._ItemCode = params.get("ItemCode")
        self._ItemCodeName = params.get("ItemCodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillOperateUin(AbstractModel):
    """操作者 UIN筛选列表

    """

    def __init__(self):
        r"""
        :param _OperateUin: 操作者 UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的ID或者角色 ID）
        :type OperateUin: str
        """
        self._OperateUin = None

    @property
    def OperateUin(self):
        """操作者 UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的ID或者角色 ID）
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin


    def _deserialize(self, params):
        self._OperateUin = params.get("OperateUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillOwnerUin(AbstractModel):
    """使用者 UIN筛选列表

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 使用者 UIN：实际使用资源的账号 ID
        :type OwnerUin: str
        """
        self._OwnerUin = None

    @property
    def OwnerUin(self):
        """使用者 UIN：实际使用资源的账号 ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillPayMode(AbstractModel):
    """计费模式筛选列表

    """

    def __init__(self):
        r"""
        :param _PayMode: 计费模式编码
        :type PayMode: str
        :param _PayModeName: 计费模式：资源的计费模式，区分为包年包月和按量计费
        :type PayModeName: str
        """
        self._PayMode = None
        self._PayModeName = None

    @property
    def PayMode(self):
        """计费模式编码
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        """计费模式：资源的计费模式，区分为包年包月和按量计费
        :rtype: str
        """
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
        


class BillProduct(AbstractModel):
    """子产品筛选列表

    """

    def __init__(self):
        r"""
        :param _ProductCode: 子产品编码
        :type ProductCode: str
        :param _ProductCodeName: 子产品名称：用户采购的具体产品细分类型
        :type ProductCodeName: str
        """
        self._ProductCode = None
        self._ProductCodeName = None

    @property
    def ProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        """子产品名称：用户采购的具体产品细分类型
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName


    def _deserialize(self, params):
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillProductLink(AbstractModel):
    """分账条件子产品筛选

    """

    def __init__(self):
        r"""
        :param _ProductCode: 子产品编码
        :type ProductCode: str
        :param _ProductCodeName: 子产品名称
        :type ProductCodeName: str
        :param _Children: 组件名称
        :type Children: list of BillItem
        """
        self._ProductCode = None
        self._ProductCodeName = None
        self._Children = None

    @property
    def ProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        """子产品名称
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def Children(self):
        """组件名称
        :rtype: list of BillItem
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = BillItem()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillProject(AbstractModel):
    """项目筛选列表

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _ProjectName: 项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :type ProjectName: str
        """
        self._ProjectId = None
        self._ProjectName = None

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :rtype: str
        """
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
        


class BillRegion(AbstractModel):
    """地域筛选列表

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _RegionName: 地域名称：资源所属地域
        :type RegionName: str
        """
        self._RegionId = None
        self._RegionName = None

    @property
    def RegionId(self):
        """地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称：资源所属地域
        :rtype: str
        """
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
        :type TransferPayAmount: str
        :param _ExtendField3: 扩展字段3：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField3: str
        :param _ExtendField4: 扩展字段4：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField4: str
        :param _ExtendField5: 扩展字段5：产品对应的扩展属性信息，仅在资源账单体现
        :type ExtendField5: str
        :param _Tags: 标签信息
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
        :param _BillMonth: 账单归属月
        :type BillMonth: str
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
        self._BillMonth = None

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        """子产品名称：用户采购的具体产品细分类型，例如：云服务器 CVM-标准型 S1
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        """计费模式：资源的计费模式，区分为包年包月和按量计费
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        """项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        """地域：资源所属地域，如华南地区（广州）
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        """可用区：资源所属可用区，如广州三区
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        """资源 ID：账单中出账对象 ID，不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID	
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """资源别名：用户在控制台为资源设置的名称，如果未设置，则默认为空
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        """交易类型：如包年包月新购、包年包月续费、按量计费扣费等类型
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        """订单ID：包年包月计费模式下订购的订单号
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def PayTime(self):
        """扣费时间：结算扣费时间
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        """开始使用时间：产品服务开始使用时间
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        """结束使用时间：产品服务结束使用时间
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ConfigDesc(self):
        """配置描述：该资源下的计费项名称和用量合并展示，仅在资源账单体现
        :rtype: str
        """
        return self._ConfigDesc

    @ConfigDesc.setter
    def ConfigDesc(self, ConfigDesc):
        self._ConfigDesc = ConfigDesc

    @property
    def ExtendField1(self):
        """扩展字段1：产品对应的扩展属性信息，仅在资源账单体现
        :rtype: str
        """
        return self._ExtendField1

    @ExtendField1.setter
    def ExtendField1(self, ExtendField1):
        self._ExtendField1 = ExtendField1

    @property
    def ExtendField2(self):
        """扩展字段2：产品对应的扩展属性信息，仅在资源账单体现
        :rtype: str
        """
        return self._ExtendField2

    @ExtendField2.setter
    def ExtendField2(self, ExtendField2):
        self._ExtendField2 = ExtendField2

    @property
    def TotalCost(self):
        """原价：原价 = 组件刊例价 * 组件用量 * 使用时长（如果客户享受一口价/合同价则默认不展示，退费类场景也默认不展示）
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Discount(self):
        """折扣率：本资源享受的折扣率（如果客户享受一口价/合同价则默认不展示，退费场景也默认不展示）
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ReduceType(self):
        """优惠类型
        :rtype: str
        """
        return self._ReduceType

    @ReduceType.setter
    def ReduceType(self, ReduceType):
        self._ReduceType = ReduceType

    @property
    def RealTotalCost(self):
        """优惠后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def ExtendField3(self):
        """扩展字段3：产品对应的扩展属性信息，仅在资源账单体现
        :rtype: str
        """
        return self._ExtendField3

    @ExtendField3.setter
    def ExtendField3(self, ExtendField3):
        self._ExtendField3 = ExtendField3

    @property
    def ExtendField4(self):
        """扩展字段4：产品对应的扩展属性信息，仅在资源账单体现
        :rtype: str
        """
        return self._ExtendField4

    @ExtendField4.setter
    def ExtendField4(self, ExtendField4):
        self._ExtendField4 = ExtendField4

    @property
    def ExtendField5(self):
        """扩展字段5：产品对应的扩展属性信息，仅在资源账单体现
        :rtype: str
        """
        return self._ExtendField5

    @ExtendField5.setter
    def ExtendField5(self, ExtendField5):
        self._ExtendField5 = ExtendField5

    @property
    def Tags(self):
        """标签信息
        :rtype: list of BillTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PayerUin(self):
        """支付者UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        """使用者UIN：实际使用资源的账号 ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        """操作者UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的 ID 或者角色 ID ）
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def BusinessCode(self):
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def RegionId(self):
        """地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def InstanceType(self):
        """实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。正常的实例展示默认为不展示
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OriginalCostWithRI(self):
        """预留实例抵扣组件原价：本产品或服务使用预留实例抵扣的组件原价金额	
        :rtype: str
        """
        return self._OriginalCostWithRI

    @OriginalCostWithRI.setter
    def OriginalCostWithRI(self, OriginalCostWithRI):
        self._OriginalCostWithRI = OriginalCostWithRI

    @property
    def SPDeduction(self):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        """节省计划抵扣金额（已废弃）
        :rtype: str
        """
        return self._SPDeduction

    @SPDeduction.setter
    def SPDeduction(self, SPDeduction):
        warnings.warn("parameter `SPDeduction` is deprecated", DeprecationWarning) 

        self._SPDeduction = SPDeduction

    @property
    def OriginalCostWithSP(self):
        """节省计划抵扣组件原价：节省计划抵扣原价=节省计划包抵扣金额/节省计划抵扣率	
        :rtype: str
        """
        return self._OriginalCostWithSP

    @OriginalCostWithSP.setter
    def OriginalCostWithSP(self, OriginalCostWithSP):
        self._OriginalCostWithSP = OriginalCostWithSP

    @property
    def BillMonth(self):
        """账单归属月
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth


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
        self._BillMonth = params.get("BillMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillTag(AbstractModel):
    """标签筛选列表

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: str
        """
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
        """分账标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: str
        """
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
        """收支类型：deduct 扣费, recharge 充值, return 退费， block 冻结, unblock 解冻
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Amount(self):
        """流水金额，单位（分）；正数表示入账，负数表示出账
        :rtype: int
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def Balance(self):
        """可用余额，单位（分）；正数表示入账，负数表示出账
        :rtype: int
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def BillId(self):
        """流水号，如20190131020000236005203583326401
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def OperationInfo(self):
        """描述信息
        :rtype: str
        """
        return self._OperationInfo

    @OperationInfo.setter
    def OperationInfo(self, OperationInfo):
        self._OperationInfo = OperationInfo

    @property
    def OperationTime(self):
        """操作时间"2019-01-31 23:35:10.000"
        :rtype: str
        """
        return self._OperationTime

    @OperationTime.setter
    def OperationTime(self, OperationTime):
        self._OperationTime = OperationTime

    @property
    def Cash(self):
        """现金账户余额，单位（分）
        :rtype: int
        """
        return self._Cash

    @Cash.setter
    def Cash(self, Cash):
        self._Cash = Cash

    @property
    def Incentive(self):
        """赠送金余额，单位（分）
        :rtype: int
        """
        return self._Incentive

    @Incentive.setter
    def Incentive(self, Incentive):
        self._Incentive = Incentive

    @property
    def Freezing(self):
        """冻结余额，单位（分）
        :rtype: int
        """
        return self._Freezing

    @Freezing.setter
    def Freezing(self, Freezing):
        self._Freezing = Freezing

    @property
    def PayChannel(self):
        """交易渠道
        :rtype: str
        """
        return self._PayChannel

    @PayChannel.setter
    def PayChannel(self, PayChannel):
        self._PayChannel = PayChannel

    @property
    def DeductMode(self):
        """扣费模式：trade 包年包月(预付费)，hourh  按量-小时结，hourd 按量-日结，hourm 按量-月结，month 按量-月结
        :rtype: str
        """
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
        


class BillZoneId(AbstractModel):
    """可用区筛选列表

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区ID
        :type ZoneId: int
        :param _ZoneName: 可用区：资源所属可用区
        :type ZoneName: str
        """
        self._ZoneId = None
        self._ZoneName = None

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
    def ZoneName(self):
        """可用区：资源所属可用区
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
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
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def TotalCost(self):
        """原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        """优惠后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
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
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def RealTotalCostRatio(self):
        """费用所占百分比，两位小数
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        """优惠后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        """账单月份，格式2019-08
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        """原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :rtype: str
        """
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
        """优惠后总价

        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        """原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :rtype: str
        """
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
        """产品名称代码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称
        :rtype: str
        """
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
        """付费模式
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        """付费模式名称
        :rtype: str
        """
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
        """项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """项目名称
        :rtype: str
        """
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
        """地域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称
        :rtype: str
        """
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
        """只支持6和12两个值
        :rtype: int
        """
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def BusinessCode(self):
        """产品名称代码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        """地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def PayMode(self):
        """付费模式，可选prePay和postPay
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceKeyword(self):
        """资源关键字
        :rtype: str
        """
        return self._ResourceKeyword

    @ResourceKeyword.setter
    def ResourceKeyword(self, ResourceKeyword):
        self._ResourceKeyword = ResourceKeyword

    @property
    def BusinessCodes(self):
        """产品名称代码
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def ProductCodes(self):
        """子产品名称代码
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        """地域ID
        :rtype: list of int
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ProjectIds(self):
        """项目ID
        :rtype: list of int
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def PayModes(self):
        """付费模式，可选prePay和postPay
        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        """交易类型
        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def HideFreeCost(self):
        """是否隐藏0元流水
        :rtype: int
        """
        return self._HideFreeCost

    @HideFreeCost.setter
    def HideFreeCost(self, HideFreeCost):
        self._HideFreeCost = HideFreeCost

    @property
    def OrderByCost(self):
        """排序规则，可选desc和asc
        :rtype: str
        """
        return self._OrderByCost

    @OrderByCost.setter
    def OrderByCost(self, OrderByCost):
        self._OrderByCost = OrderByCost

    @property
    def BillIds(self):
        """交易ID
        :rtype: list of str
        """
        return self._BillIds

    @BillIds.setter
    def BillIds(self, BillIds):
        self._BillIds = BillIds

    @property
    def ComponentCodes(self):
        """组件编码
        :rtype: list of str
        """
        return self._ComponentCodes

    @ComponentCodes.setter
    def ComponentCodes(self, ComponentCodes):
        self._ComponentCodes = ComponentCodes

    @property
    def FileIds(self):
        """文件ID
        :rtype: list of str
        """
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def FileTypes(self):
        """文件类型
        :rtype: list of str
        """
        return self._FileTypes

    @FileTypes.setter
    def FileTypes(self, FileTypes):
        self._FileTypes = FileTypes

    @property
    def Status(self):
        """状态
        :rtype: list of int non-negative
        """
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
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送金
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 代金券
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金
        :type TransferPayAmount: str
        :param _RegionName: 地域名称（仅在地域汇总总展示）
        :type RegionName: str
        """
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._RealTotalCost = None
        self._Trend = None
        self._CashPayAmount = None
        self._IncentivePayAmount = None
        self._VoucherPayAmount = None
        self._TransferPayAmount = None
        self._RegionName = None

    @property
    def BusinessCode(self):
        """产品名称代码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def RealTotalCost(self):
        """折后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        """费用趋势
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def CashPayAmount(self):
        """现金
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送金
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        """代金券
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        """分成金
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def RegionName(self):
        """地域名称（仅在地域汇总总展示）
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


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
        self._RegionName = params.get("RegionName")
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
        :type CashPayAmount: str
        :param _IncentivePayAmount: 赠送金
        :type IncentivePayAmount: str
        :param _VoucherPayAmount: 代金券
        :type VoucherPayAmount: str
        :param _TransferPayAmount: 分成金
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
        """项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """项目名称
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RealTotalCost(self):
        """折后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        """趋势
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def Business(self):
        """产品消耗详情
        :rtype: list of ConsumptionBusinessSummaryDataItem
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CashPayAmount(self):
        """现金
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送金
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        """代金券
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        """分成金
        :rtype: str
        """
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
        :param _CashPayAmount: 现金
        :type CashPayAmount: str
        :param _VoucherPayAmount: 代金券
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: 赠送金
        :type IncentivePayAmount: str
        :param _TransferPayAmount: 分成金
        :type TransferPayAmount: str
        """
        self._RegionId = None
        self._RegionName = None
        self._RealTotalCost = None
        self._Trend = None
        self._Business = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None

    @property
    def RegionId(self):
        """地域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RealTotalCost(self):
        """折后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Trend(self):
        """趋势
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        """
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def Business(self):
        """产品消费详情
        :rtype: list of ConsumptionBusinessSummaryDataItem
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CashPayAmount(self):
        """现金
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        """代金券
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送金
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        """分成金
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount


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
        self._CashPayAmount = params.get("CashPayAmount")
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
        """产品列表
        :rtype: list of ConditionBusiness
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Project(self):
        """项目列表
        :rtype: list of ConditionProject
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Region(self):
        """地域列表
        :rtype: list of ConditionRegion
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayMode(self):
        """付费模式列表
        :rtype: list of ConditionPayMode
        """
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
        :type RealCost: str
        :param _FeeBeginTime: 费用起始时间
        :type FeeBeginTime: str
        :param _FeeEndTime: 费用结束时间
        :type FeeEndTime: str
        :param _DayDiff: 天数
        :type DayDiff: str
        :param _DailyTotalCost: 每日消耗
        :type DailyTotalCost: str
        :param _OrderId: 订单号
        :type OrderId: str
        :param _VoucherPayAmount: 代金券
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: 赠送金
        :type IncentivePayAmount: str
        :param _TransferPayAmount: 分成金
        :type TransferPayAmount: str
        :param _PayerUin: 支付者UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :type PayerUin: str
        :param _OwnerUin: 使用者UIN：实际使用资源的账号 ID
        :type OwnerUin: str
        :param _OperateUin: 操作者UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的 ID 或者角色 ID ）
        :type OperateUin: str
        :param _ProductCode: 子产品编码
        :type ProductCode: str
        :param _ProductCodeName: 子产品名称：用户采购的具体产品细分类型，例如：云服务器 CVM-标准型 S1
        :type ProductCodeName: str
        :param _RegionType: 地域类型
        :type RegionType: str
        :param _RegionTypeName: 地域类型名称
        :type RegionTypeName: str
        :param _Extend1: 扩展字段1
        :type Extend1: str
        :param _Extend2: 扩展字段2
        :type Extend2: str
        :param _Extend3: 扩展字段3
        :type Extend3: str
        :param _Extend4: 扩展字段4
        :type Extend4: str
        :param _Extend5: 扩展字段5
        :type Extend5: str
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _InstanceTypeName: 实例类型名称
        :type InstanceTypeName: str
        :param _PayTime: 扣费时间：结算扣费时间
        :type PayTime: str
        :param _ZoneName: 可用区：资源所属可用区，如广州三区
        :type ZoneName: str
        :param _ComponentConfig: 配置描述
        :type ComponentConfig: str
        :param _Tags: 标签信息
        :type Tags: str
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
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._ProductCode = None
        self._ProductCodeName = None
        self._RegionType = None
        self._RegionTypeName = None
        self._Extend1 = None
        self._Extend2 = None
        self._Extend3 = None
        self._Extend4 = None
        self._Extend5 = None
        self._InstanceType = None
        self._InstanceTypeName = None
        self._PayTime = None
        self._ZoneName = None
        self._ComponentConfig = None
        self._Tags = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """资源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def RealTotalCost(self):
        """折后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金花费
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def ProjectId(self):
        """项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """项目名称
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionId(self):
        """地域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def PayMode(self):
        """付费模式
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        """付费模式名称
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def BusinessCode(self):
        """产品名称代码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ConsumptionTypeName(self):
        """消耗类型
        :rtype: str
        """
        return self._ConsumptionTypeName

    @ConsumptionTypeName.setter
    def ConsumptionTypeName(self, ConsumptionTypeName):
        self._ConsumptionTypeName = ConsumptionTypeName

    @property
    def RealCost(self):
        """折前价
        :rtype: str
        """
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def FeeBeginTime(self):
        """费用起始时间
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        """费用结束时间
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def DayDiff(self):
        """天数
        :rtype: str
        """
        return self._DayDiff

    @DayDiff.setter
    def DayDiff(self, DayDiff):
        self._DayDiff = DayDiff

    @property
    def DailyTotalCost(self):
        """每日消耗
        :rtype: str
        """
        return self._DailyTotalCost

    @DailyTotalCost.setter
    def DailyTotalCost(self, DailyTotalCost):
        self._DailyTotalCost = DailyTotalCost

    @property
    def OrderId(self):
        """订单号
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def VoucherPayAmount(self):
        """代金券
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送金
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        """分成金
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def PayerUin(self):
        """支付者UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        """使用者UIN：实际使用资源的账号 ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        """操作者UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的 ID 或者角色 ID ）
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def ProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        """子产品名称：用户采购的具体产品细分类型，例如：云服务器 CVM-标准型 S1
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def RegionType(self):
        """地域类型
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def RegionTypeName(self):
        """地域类型名称
        :rtype: str
        """
        return self._RegionTypeName

    @RegionTypeName.setter
    def RegionTypeName(self, RegionTypeName):
        self._RegionTypeName = RegionTypeName

    @property
    def Extend1(self):
        """扩展字段1
        :rtype: str
        """
        return self._Extend1

    @Extend1.setter
    def Extend1(self, Extend1):
        self._Extend1 = Extend1

    @property
    def Extend2(self):
        """扩展字段2
        :rtype: str
        """
        return self._Extend2

    @Extend2.setter
    def Extend2(self, Extend2):
        self._Extend2 = Extend2

    @property
    def Extend3(self):
        """扩展字段3
        :rtype: str
        """
        return self._Extend3

    @Extend3.setter
    def Extend3(self, Extend3):
        self._Extend3 = Extend3

    @property
    def Extend4(self):
        """扩展字段4
        :rtype: str
        """
        return self._Extend4

    @Extend4.setter
    def Extend4(self, Extend4):
        self._Extend4 = Extend4

    @property
    def Extend5(self):
        """扩展字段5
        :rtype: str
        """
        return self._Extend5

    @Extend5.setter
    def Extend5(self, Extend5):
        self._Extend5 = Extend5

    @property
    def InstanceType(self):
        """实例类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        """实例类型名称
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName

    @property
    def PayTime(self):
        """扣费时间：结算扣费时间
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def ZoneName(self):
        """可用区：资源所属可用区，如广州三区
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ComponentConfig(self):
        """配置描述
        :rtype: str
        """
        return self._ComponentConfig

    @ComponentConfig.setter
    def ComponentConfig(self, ComponentConfig):
        self._ComponentConfig = ComponentConfig

    @property
    def Tags(self):
        """标签信息
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


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
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        self._RegionType = params.get("RegionType")
        self._RegionTypeName = params.get("RegionTypeName")
        self._Extend1 = params.get("Extend1")
        self._Extend2 = params.get("Extend2")
        self._Extend3 = params.get("Extend3")
        self._Extend4 = params.get("Extend4")
        self._Extend5 = params.get("Extend5")
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        self._PayTime = params.get("PayTime")
        self._ZoneName = params.get("ZoneName")
        self._ComponentConfig = params.get("ComponentConfig")
        self._Tags = params.get("Tags")
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
        """折后总价
        :rtype: str
        """
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
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        """趋势类型，upward上升/downward下降/none无
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        """趋势值，Type为none是该字段值为null
        :rtype: str
        """
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
        """存储桶名称
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def DosageBeginTime(self):
        """用量开始时间
        :rtype: str
        """
        return self._DosageBeginTime

    @DosageBeginTime.setter
    def DosageBeginTime(self, DosageBeginTime):
        self._DosageBeginTime = DosageBeginTime

    @property
    def DosageEndTime(self):
        """用量结束时间
        :rtype: str
        """
        return self._DosageEndTime

    @DosageEndTime.setter
    def DosageEndTime(self, DosageEndTime):
        self._DosageEndTime = DosageEndTime

    @property
    def SubProductCodeName(self):
        """子产品名称
        :rtype: str
        """
        return self._SubProductCodeName

    @SubProductCodeName.setter
    def SubProductCodeName(self, SubProductCodeName):
        self._SubProductCodeName = SubProductCodeName

    @property
    def BillingItemCodeName(self):
        """计费项名称
        :rtype: str
        """
        return self._BillingItemCodeName

    @BillingItemCodeName.setter
    def BillingItemCodeName(self, BillingItemCodeName):
        self._BillingItemCodeName = BillingItemCodeName

    @property
    def DosageValue(self):
        """用量
        :rtype: str
        """
        return self._DosageValue

    @DosageValue.setter
    def DosageValue(self, DosageValue):
        self._DosageValue = DosageValue

    @property
    def Unit(self):
        """单位
        :rtype: str
        """
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
        """组件类型名称
        :rtype: str
        """
        return self._ComponentCodeName

    @ComponentCodeName.setter
    def ComponentCodeName(self, ComponentCodeName):
        self._ComponentCodeName = ComponentCodeName

    @property
    def ItemCodeName(self):
        """组件名称
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def SinglePrice(self):
        """刊例价
        :rtype: str
        """
        return self._SinglePrice

    @SinglePrice.setter
    def SinglePrice(self, SinglePrice):
        self._SinglePrice = SinglePrice

    @property
    def PriceUnit(self):
        """刊例价单位
        :rtype: str
        """
        return self._PriceUnit

    @PriceUnit.setter
    def PriceUnit(self, PriceUnit):
        self._PriceUnit = PriceUnit

    @property
    def UsedAmount(self):
        """用量
        :rtype: str
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedAmountUnit(self):
        """用量单位
        :rtype: str
        """
        return self._UsedAmountUnit

    @UsedAmountUnit.setter
    def UsedAmountUnit(self, UsedAmountUnit):
        self._UsedAmountUnit = UsedAmountUnit

    @property
    def Cost(self):
        """原价
        :rtype: str
        """
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def Discount(self):
        """折扣
        :rtype: str
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def RealCost(self):
        """折后价
        :rtype: str
        """
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def VoucherPayAmount(self):
        """代金券支付金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def CashPayAmount(self):
        """现金支付金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送金支付金额
        :rtype: str
        """
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
        """支付者uin
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def BusinessCodeName(self):
        """产品名称
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        """子产品名称
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        """计费模式名称
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        """项目名称
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        """区域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        """地区名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        """资源id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """资源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        """类型名称
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        """订单id
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        """交易id
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def FeeBeginTime(self):
        """费用开始时间
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        """费用结束时间
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentSet(self):
        """组件明细
        :rtype: list of CostComponentSet
        """
        return self._ComponentSet

    @ComponentSet.setter
    def ComponentSet(self, ComponentSet):
        self._ComponentSet = ComponentSet

    @property
    def ProductCode(self):
        """子产品名称代码
        :rtype: str
        """
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
        


class CreateAllocationTagRequest(AbstractModel):
    """CreateAllocationTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 用户分账标签键
        :type TagKey: list of str
        """
        self._TagKey = None

    @property
    def TagKey(self):
        """用户分账标签键
        :rtype: list of str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAllocationTagResponse(AbstractModel):
    """CreateAllocationTag返回参数结构体

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
        :type ProductCode: str
        :param _SubProductCode: 子产品编码
        :type SubProductCode: str
        :param _BigDealId: 大订单号
        :type BigDealId: str
        :param _Formula: 退费公式
        :type Formula: str
        :param _RefReturnDeals: 退费涉及订单信息
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
        :type Action: str
        :param _ProductName: 产品编码中文名称
        :type ProductName: str
        :param _SubProductName: 子产品编码中文名称
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
        """订单号
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Status(self):
        """订单的状态 1：未支付 2：已支付3：发货中 4：已发货 5：发货失败 6：已退款 7：已关单 8：订单过期 9：订单已失效 10：产品已失效 11：代付拒绝 12：支付中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Payer(self):
        """支付者
        :rtype: str
        """
        return self._Payer

    @Payer.setter
    def Payer(self, Payer):
        self._Payer = Payer

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Creator(self):
        """创建人
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def RealTotalCost(self):
        """实际支付金额（分）
        :rtype: int
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def VoucherDecline(self):
        """代金券抵扣金额（分）
        :rtype: int
        """
        return self._VoucherDecline

    @VoucherDecline.setter
    def VoucherDecline(self, VoucherDecline):
        self._VoucherDecline = VoucherDecline

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsCategoryId(self):
        """产品分类ID
        :rtype: int
        """
        return self._GoodsCategoryId

    @GoodsCategoryId.setter
    def GoodsCategoryId(self, GoodsCategoryId):
        self._GoodsCategoryId = GoodsCategoryId

    @property
    def ProductInfo(self):
        """产品详情
        :rtype: list of ProductInfo
        """
        return self._ProductInfo

    @ProductInfo.setter
    def ProductInfo(self, ProductInfo):
        self._ProductInfo = ProductInfo

    @property
    def TimeSpan(self):
        """时长
        :rtype: float
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """时间单位
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Currency(self):
        """货币单位
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def Policy(self):
        """折扣率
        :rtype: float
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Price(self):
        """单价（分）
        :rtype: float
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def TotalCost(self):
        """原价（分）
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def ProductCode(self):
        """产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def BigDealId(self):
        """大订单号
        :rtype: str
        """
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def Formula(self):
        """退费公式
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def RefReturnDeals(self):
        """退费涉及订单信息
        :rtype: str
        """
        return self._RefReturnDeals

    @RefReturnDeals.setter
    def RefReturnDeals(self, RefReturnDeals):
        self._RefReturnDeals = RefReturnDeals

    @property
    def PayMode(self):
        """付费模式：prePay 预付费 postPay后付费 riPay预留实例
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Action(self):
        """交易类型
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
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ProductName(self):
        """产品编码中文名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductName(self):
        """子产品编码中文名称
        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def ResourceId(self):
        """订单对应的资源id, 查询参数Limit超过200，将返回null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
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
        


class DeleteAllocationTagRequest(AbstractModel):
    """DeleteAllocationTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 用户分账标签键
        :type TagKey: list of str
        """
        self._TagKey = None

    @property
    def TagKey(self):
        """用户分账标签键
        :rtype: list of str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAllocationTagResponse(AbstractModel):
    """DeleteAllocationTag返回参数结构体

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
        :param _CreditAmount: 信用额度,单位 分
        :type CreditAmount: float
        :param _CreditBalance: 可用信用额度,单位 分
        :type CreditBalance: float
        :param _RealCreditBalance: 真实可用信用额度,单位 分
        :type RealCreditBalance: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        """接口做过变更,为兼容老接口,本字段与RealBalance相同,为当前真实可用余额,单位 分
        :rtype: int
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def Uin(self):
        """查询的用户Uin
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RealBalance(self):
        """当前真实可用余额,单位 分
        :rtype: float
        """
        return self._RealBalance

    @RealBalance.setter
    def RealBalance(self, RealBalance):
        self._RealBalance = RealBalance

    @property
    def CashAccountBalance(self):
        """现金账户余额,单位 分
        :rtype: float
        """
        return self._CashAccountBalance

    @CashAccountBalance.setter
    def CashAccountBalance(self, CashAccountBalance):
        self._CashAccountBalance = CashAccountBalance

    @property
    def IncomeIntoAccountBalance(self):
        """收益转入账户余额,单位 分
        :rtype: float
        """
        return self._IncomeIntoAccountBalance

    @IncomeIntoAccountBalance.setter
    def IncomeIntoAccountBalance(self, IncomeIntoAccountBalance):
        self._IncomeIntoAccountBalance = IncomeIntoAccountBalance

    @property
    def PresentAccountBalance(self):
        """赠送账户余额,单位 分
        :rtype: float
        """
        return self._PresentAccountBalance

    @PresentAccountBalance.setter
    def PresentAccountBalance(self, PresentAccountBalance):
        self._PresentAccountBalance = PresentAccountBalance

    @property
    def FreezeAmount(self):
        """冻结金额,单位 分
        :rtype: float
        """
        return self._FreezeAmount

    @FreezeAmount.setter
    def FreezeAmount(self, FreezeAmount):
        self._FreezeAmount = FreezeAmount

    @property
    def OweAmount(self):
        """欠费金额,单位 分
        :rtype: float
        """
        return self._OweAmount

    @OweAmount.setter
    def OweAmount(self, OweAmount):
        self._OweAmount = OweAmount

    @property
    def IsAllowArrears(self):
        warnings.warn("parameter `IsAllowArrears` is deprecated", DeprecationWarning) 

        """是否允许欠费消费
        :rtype: bool
        """
        return self._IsAllowArrears

    @IsAllowArrears.setter
    def IsAllowArrears(self, IsAllowArrears):
        warnings.warn("parameter `IsAllowArrears` is deprecated", DeprecationWarning) 

        self._IsAllowArrears = IsAllowArrears

    @property
    def IsCreditLimited(self):
        warnings.warn("parameter `IsCreditLimited` is deprecated", DeprecationWarning) 

        """是否限制信用额度
        :rtype: bool
        """
        return self._IsCreditLimited

    @IsCreditLimited.setter
    def IsCreditLimited(self, IsCreditLimited):
        warnings.warn("parameter `IsCreditLimited` is deprecated", DeprecationWarning) 

        self._IsCreditLimited = IsCreditLimited

    @property
    def CreditAmount(self):
        """信用额度,单位 分
        :rtype: float
        """
        return self._CreditAmount

    @CreditAmount.setter
    def CreditAmount(self, CreditAmount):
        self._CreditAmount = CreditAmount

    @property
    def CreditBalance(self):
        """可用信用额度,单位 分
        :rtype: float
        """
        return self._CreditBalance

    @CreditBalance.setter
    def CreditBalance(self, CreditBalance):
        self._CreditBalance = CreditBalance

    @property
    def RealCreditBalance(self):
        """真实可用信用额度,单位 分
        :rtype: float
        """
        return self._RealCreditBalance

    @RealCreditBalance.setter
    def RealCreditBalance(self, RealCreditBalance):
        self._RealCreditBalance = RealCreditBalance

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


class DescribeAllocateConditionsRequest(AbstractModel):
    """DescribeAllocateConditions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Month: 账单月份，格式为2024-02，不传默认当前月
        :type Month: str
        """
        self._Month = None

    @property
    def Month(self):
        """账单月份，格式为2024-02，不传默认当前月
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocateConditionsResponse(AbstractModel):
    """DescribeAllocateConditions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 产品筛选列表
        :type Business: list of BillBusinessLink
        :param _Product: 子产品筛选列表
        :type Product: list of BillProduct
        :param _Item: 组件名称筛选列表
        :type Item: list of BillItem
        :param _Region: 地域筛选列表
        :type Region: list of BillRegion
        :param _InstanceType: 实例类型筛选列表
        :type InstanceType: list of BillInstanceType
        :param _PayMode: 计费模式筛选列表
        :type PayMode: list of BillPayMode
        :param _Project: 项目筛选列表
        :type Project: list of BillProject
        :param _Tag: 标签筛选列表
        :type Tag: list of BillTag
        :param _OwnerUin: 使用者 UIN 筛选列表
        :type OwnerUin: list of BillOwnerUin
        :param _OperateUin: 操作者 UIN 筛选列表
        :type OperateUin: list of BillOperateUin
        :param _ActionType: 交易类型筛选列表
        :type ActionType: list of BillActionType
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Product = None
        self._Item = None
        self._Region = None
        self._InstanceType = None
        self._PayMode = None
        self._Project = None
        self._Tag = None
        self._OwnerUin = None
        self._OperateUin = None
        self._ActionType = None
        self._RequestId = None

    @property
    def Business(self):
        """产品筛选列表
        :rtype: list of BillBusinessLink
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Product(self):
        """子产品筛选列表
        :rtype: list of BillProduct
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Item(self):
        """组件名称筛选列表
        :rtype: list of BillItem
        """
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def Region(self):
        """地域筛选列表
        :rtype: list of BillRegion
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceType(self):
        """实例类型筛选列表
        :rtype: list of BillInstanceType
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PayMode(self):
        """计费模式筛选列表
        :rtype: list of BillPayMode
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Project(self):
        """项目筛选列表
        :rtype: list of BillProject
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Tag(self):
        """标签筛选列表
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def OwnerUin(self):
        """使用者 UIN 筛选列表
        :rtype: list of BillOwnerUin
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        """操作者 UIN 筛选列表
        :rtype: list of BillOperateUin
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def ActionType(self):
        """交易类型筛选列表
        :rtype: list of BillActionType
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

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
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = BillBusinessLink()
                obj._deserialize(item)
                self._Business.append(obj)
        if params.get("Product") is not None:
            self._Product = []
            for item in params.get("Product"):
                obj = BillProduct()
                obj._deserialize(item)
                self._Product.append(obj)
        if params.get("Item") is not None:
            self._Item = []
            for item in params.get("Item"):
                obj = BillItem()
                obj._deserialize(item)
                self._Item.append(obj)
        if params.get("Region") is not None:
            self._Region = []
            for item in params.get("Region"):
                obj = BillRegion()
                obj._deserialize(item)
                self._Region.append(obj)
        if params.get("InstanceType") is not None:
            self._InstanceType = []
            for item in params.get("InstanceType"):
                obj = BillInstanceType()
                obj._deserialize(item)
                self._InstanceType.append(obj)
        if params.get("PayMode") is not None:
            self._PayMode = []
            for item in params.get("PayMode"):
                obj = BillPayMode()
                obj._deserialize(item)
                self._PayMode.append(obj)
        if params.get("Project") is not None:
            self._Project = []
            for item in params.get("Project"):
                obj = BillProject()
                obj._deserialize(item)
                self._Project.append(obj)
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("OwnerUin") is not None:
            self._OwnerUin = []
            for item in params.get("OwnerUin"):
                obj = BillOwnerUin()
                obj._deserialize(item)
                self._OwnerUin.append(obj)
        if params.get("OperateUin") is not None:
            self._OperateUin = []
            for item in params.get("OperateUin"):
                obj = BillOperateUin()
                obj._deserialize(item)
                self._OperateUin.append(obj)
        if params.get("ActionType") is not None:
            self._ActionType = []
            for item in params.get("ActionType"):
                obj = BillActionType()
                obj._deserialize(item)
                self._ActionType.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationBillConditionsRequest(AbstractModel):
    """DescribeAllocationBillConditions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Month: 账单月份，格式为2024-02，不传默认当前月
        :type Month: str
        :param _TreeNodeUniqKeys: 分账单元唯一标识，用作筛选
        :type TreeNodeUniqKeys: list of str
        :param _BillDates: 日期
        :type BillDates: list of str
        :param _BusinessCodes: 产品编码
        :type BusinessCodes: list of str
        :param _OwnerUins: 使用者UIN
        :type OwnerUins: list of str
        :param _OperateUins: 操作者UIN
        :type OperateUins: list of str
        :param _PayModes: 计费模式编码
        :type PayModes: list of str
        :param _ActionTypes: 交易类型编码
        :type ActionTypes: list of str
        :param _ProductCodes: 子产品编码
        :type ProductCodes: list of str
        :param _RegionIds: 地域ID
        :type RegionIds: list of str
        :param _ZoneIds: 可用区ID
        :type ZoneIds: list of str
        :param _InstanceTypes: 实例类型编码
        :type InstanceTypes: list of str
        :param _Tag: 标签
        :type Tag: list of str
        :param _ComponentCodes: 组件类型编码
        :type ComponentCodes: list of str
        :param _ItemCodes: 组件名称编码
        :type ItemCodes: list of str
        :param _SearchKey: 模糊搜索条件
        :type SearchKey: str
        :param _ProjectIds: 项目id
        :type ProjectIds: list of int non-negative
        :param _AllocationType: 费用归集类型
        :type AllocationType: list of int
        """
        self._Month = None
        self._TreeNodeUniqKeys = None
        self._BillDates = None
        self._BusinessCodes = None
        self._OwnerUins = None
        self._OperateUins = None
        self._PayModes = None
        self._ActionTypes = None
        self._ProductCodes = None
        self._RegionIds = None
        self._ZoneIds = None
        self._InstanceTypes = None
        self._Tag = None
        self._ComponentCodes = None
        self._ItemCodes = None
        self._SearchKey = None
        self._ProjectIds = None
        self._AllocationType = None

    @property
    def Month(self):
        """账单月份，格式为2024-02，不传默认当前月
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TreeNodeUniqKeys(self):
        """分账单元唯一标识，用作筛选
        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def BillDates(self):
        """日期
        :rtype: list of str
        """
        return self._BillDates

    @BillDates.setter
    def BillDates(self, BillDates):
        self._BillDates = BillDates

    @property
    def BusinessCodes(self):
        """产品编码
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def OwnerUins(self):
        """使用者UIN
        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def OperateUins(self):
        """操作者UIN
        :rtype: list of str
        """
        return self._OperateUins

    @OperateUins.setter
    def OperateUins(self, OperateUins):
        self._OperateUins = OperateUins

    @property
    def PayModes(self):
        """计费模式编码
        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        """交易类型编码
        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def ProductCodes(self):
        """子产品编码
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        """地域ID
        :rtype: list of str
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ZoneIds(self):
        """可用区ID
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceTypes(self):
        """实例类型编码
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Tag(self):
        """标签
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ComponentCodes(self):
        """组件类型编码
        :rtype: list of str
        """
        return self._ComponentCodes

    @ComponentCodes.setter
    def ComponentCodes(self, ComponentCodes):
        self._ComponentCodes = ComponentCodes

    @property
    def ItemCodes(self):
        """组件名称编码
        :rtype: list of str
        """
        return self._ItemCodes

    @ItemCodes.setter
    def ItemCodes(self, ItemCodes):
        self._ItemCodes = ItemCodes

    @property
    def SearchKey(self):
        """模糊搜索条件
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        """项目id
        :rtype: list of int non-negative
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def AllocationType(self):
        """费用归集类型
        :rtype: list of int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._BillDates = params.get("BillDates")
        self._BusinessCodes = params.get("BusinessCodes")
        self._OwnerUins = params.get("OwnerUins")
        self._OperateUins = params.get("OperateUins")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._ProductCodes = params.get("ProductCodes")
        self._RegionIds = params.get("RegionIds")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Tag = params.get("Tag")
        self._ComponentCodes = params.get("ComponentCodes")
        self._ItemCodes = params.get("ItemCodes")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        self._AllocationType = params.get("AllocationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationBillConditionsResponse(AbstractModel):
    """DescribeAllocationBillConditions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 产品筛选列表
        :type Business: list of BillBusiness
        :param _Product: 子产品筛选列表
        :type Product: list of BillProduct
        :param _Item: 组件名称筛选列表
        :type Item: list of BillItem
        :param _Region: 地域筛选列表
        :type Region: list of BillRegion
        :param _InstanceType: 实例类型筛选列表
        :type InstanceType: list of BillInstanceType
        :param _PayMode: 计费模式筛选列表
        :type PayMode: list of BillPayMode
        :param _Project: 项目筛选列表
        :type Project: list of BillProject
        :param _Tag: 标签筛选列表
        :type Tag: list of BillTag
        :param _OwnerUin: 使用者 UIN 筛选列表
        :type OwnerUin: list of BillOwnerUin
        :param _OperateUin: 操作者 UIN 筛选列表
        :type OperateUin: list of BillOperateUin
        :param _BillDay: 日期筛选列表
        :type BillDay: list of BillDays
        :param _ActionType: 交易类型筛选列表
        :type ActionType: list of BillActionType
        :param _Component: 组件类型筛选列表
        :type Component: list of BillComponent
        :param _Zone: 可用区筛选列表
        :type Zone: list of BillZoneId
        :param _AllocationTreeNode: 分账单元筛选列表
        :type AllocationTreeNode: list of AllocationTreeNode
        :param _TagKey: 分账标签键
        :type TagKey: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Product = None
        self._Item = None
        self._Region = None
        self._InstanceType = None
        self._PayMode = None
        self._Project = None
        self._Tag = None
        self._OwnerUin = None
        self._OperateUin = None
        self._BillDay = None
        self._ActionType = None
        self._Component = None
        self._Zone = None
        self._AllocationTreeNode = None
        self._TagKey = None
        self._RequestId = None

    @property
    def Business(self):
        """产品筛选列表
        :rtype: list of BillBusiness
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Product(self):
        """子产品筛选列表
        :rtype: list of BillProduct
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Item(self):
        """组件名称筛选列表
        :rtype: list of BillItem
        """
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def Region(self):
        """地域筛选列表
        :rtype: list of BillRegion
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceType(self):
        """实例类型筛选列表
        :rtype: list of BillInstanceType
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PayMode(self):
        """计费模式筛选列表
        :rtype: list of BillPayMode
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Project(self):
        """项目筛选列表
        :rtype: list of BillProject
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Tag(self):
        """标签筛选列表
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def OwnerUin(self):
        """使用者 UIN 筛选列表
        :rtype: list of BillOwnerUin
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        """操作者 UIN 筛选列表
        :rtype: list of BillOperateUin
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def BillDay(self):
        """日期筛选列表
        :rtype: list of BillDays
        """
        return self._BillDay

    @BillDay.setter
    def BillDay(self, BillDay):
        self._BillDay = BillDay

    @property
    def ActionType(self):
        """交易类型筛选列表
        :rtype: list of BillActionType
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Component(self):
        """组件类型筛选列表
        :rtype: list of BillComponent
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Zone(self):
        """可用区筛选列表
        :rtype: list of BillZoneId
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AllocationTreeNode(self):
        """分账单元筛选列表
        :rtype: list of AllocationTreeNode
        """
        return self._AllocationTreeNode

    @AllocationTreeNode.setter
    def AllocationTreeNode(self, AllocationTreeNode):
        self._AllocationTreeNode = AllocationTreeNode

    @property
    def TagKey(self):
        """分账标签键
        :rtype: list of str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

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
        if params.get("Business") is not None:
            self._Business = []
            for item in params.get("Business"):
                obj = BillBusiness()
                obj._deserialize(item)
                self._Business.append(obj)
        if params.get("Product") is not None:
            self._Product = []
            for item in params.get("Product"):
                obj = BillProduct()
                obj._deserialize(item)
                self._Product.append(obj)
        if params.get("Item") is not None:
            self._Item = []
            for item in params.get("Item"):
                obj = BillItem()
                obj._deserialize(item)
                self._Item.append(obj)
        if params.get("Region") is not None:
            self._Region = []
            for item in params.get("Region"):
                obj = BillRegion()
                obj._deserialize(item)
                self._Region.append(obj)
        if params.get("InstanceType") is not None:
            self._InstanceType = []
            for item in params.get("InstanceType"):
                obj = BillInstanceType()
                obj._deserialize(item)
                self._InstanceType.append(obj)
        if params.get("PayMode") is not None:
            self._PayMode = []
            for item in params.get("PayMode"):
                obj = BillPayMode()
                obj._deserialize(item)
                self._PayMode.append(obj)
        if params.get("Project") is not None:
            self._Project = []
            for item in params.get("Project"):
                obj = BillProject()
                obj._deserialize(item)
                self._Project.append(obj)
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("OwnerUin") is not None:
            self._OwnerUin = []
            for item in params.get("OwnerUin"):
                obj = BillOwnerUin()
                obj._deserialize(item)
                self._OwnerUin.append(obj)
        if params.get("OperateUin") is not None:
            self._OperateUin = []
            for item in params.get("OperateUin"):
                obj = BillOperateUin()
                obj._deserialize(item)
                self._OperateUin.append(obj)
        if params.get("BillDay") is not None:
            self._BillDay = []
            for item in params.get("BillDay"):
                obj = BillDays()
                obj._deserialize(item)
                self._BillDay.append(obj)
        if params.get("ActionType") is not None:
            self._ActionType = []
            for item in params.get("ActionType"):
                obj = BillActionType()
                obj._deserialize(item)
                self._ActionType.append(obj)
        if params.get("Component") is not None:
            self._Component = []
            for item in params.get("Component"):
                obj = BillComponent()
                obj._deserialize(item)
                self._Component.append(obj)
        if params.get("Zone") is not None:
            self._Zone = []
            for item in params.get("Zone"):
                obj = BillZoneId()
                obj._deserialize(item)
                self._Zone.append(obj)
        if params.get("AllocationTreeNode") is not None:
            self._AllocationTreeNode = []
            for item in params.get("AllocationTreeNode"):
                obj = AllocationTreeNode()
                obj._deserialize(item)
                self._AllocationTreeNode.append(obj)
        self._TagKey = params.get("TagKey")
        self._RequestId = params.get("RequestId")


class DescribeAllocationBillDetailRequest(AbstractModel):
    """DescribeAllocationBillDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量，最大值为1000
        :type Limit: int
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :type Offset: int
        :param _Month: 账单月份，格式为2024-02，不传默认当前月
        :type Month: str
        :param _TreeNodeUniqKeys: 分账单元唯一标识，用作筛选
        :type TreeNodeUniqKeys: list of str
        :param _Sort: 排序字段，枚举值如下：
RiTimeSpan - 预留实例抵扣时长
ExtendPayAmount1 - 预留实例抵扣组件原价
RealCost - 折后总价
CashPayAmount - 现金金额
VoucherPayAmount - 代金券金额
IncentivePayAmount - 赠送金金额
TransferPayAmount -分成金金额
Cost - 组件原价
        :type Sort: str
        :param _SortType: 排序类型，枚举值如下：
asc - 升序
desc - 降序
        :type SortType: str
        :param _BusinessCodes: 产品编码，用作筛选
        :type BusinessCodes: list of str
        :param _OwnerUins: 使用者UIN，用作筛选
        :type OwnerUins: list of str
        :param _OperateUins: 操作者UIN，用作筛选
        :type OperateUins: list of str
        :param _PayModes: 计费模式编码，用作筛选
        :type PayModes: list of str
        :param _ActionTypes: 交易类型编码，用作筛选
        :type ActionTypes: list of str
        :param _ProductCodes: 子产品编码，用作筛选
        :type ProductCodes: list of str
        :param _RegionIds: 地域ID，用作筛选
        :type RegionIds: list of str
        :param _ZoneIds: 可用区ID，用作筛选
        :type ZoneIds: list of str
        :param _InstanceTypes: 实例类型编码，用作筛选
        :type InstanceTypes: list of str
        :param _Tag: 标签，用作筛选
        :type Tag: list of str
        :param _ComponentCodes: 组件类型编码，用作筛选
        :type ComponentCodes: list of str
        :param _ItemCodes: 组件名称编码，用作筛选
        :type ItemCodes: list of str
        :param _SearchKey: 模糊搜索：支持标签、资源id、资源别名
        :type SearchKey: str
        :param _ProjectIds: 项目ID，用作筛选
        :type ProjectIds: list of int non-negative
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._TreeNodeUniqKeys = None
        self._Sort = None
        self._SortType = None
        self._BusinessCodes = None
        self._OwnerUins = None
        self._OperateUins = None
        self._PayModes = None
        self._ActionTypes = None
        self._ProductCodes = None
        self._RegionIds = None
        self._ZoneIds = None
        self._InstanceTypes = None
        self._Tag = None
        self._ComponentCodes = None
        self._ItemCodes = None
        self._SearchKey = None
        self._ProjectIds = None

    @property
    def Limit(self):
        """数量，最大值为1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        """账单月份，格式为2024-02，不传默认当前月
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TreeNodeUniqKeys(self):
        """分账单元唯一标识，用作筛选
        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def Sort(self):
        """排序字段，枚举值如下：
RiTimeSpan - 预留实例抵扣时长
ExtendPayAmount1 - 预留实例抵扣组件原价
RealCost - 折后总价
CashPayAmount - 现金金额
VoucherPayAmount - 代金券金额
IncentivePayAmount - 赠送金金额
TransferPayAmount -分成金金额
Cost - 组件原价
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SortType(self):
        """排序类型，枚举值如下：
asc - 升序
desc - 降序
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def BusinessCodes(self):
        """产品编码，用作筛选
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def OwnerUins(self):
        """使用者UIN，用作筛选
        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def OperateUins(self):
        """操作者UIN，用作筛选
        :rtype: list of str
        """
        return self._OperateUins

    @OperateUins.setter
    def OperateUins(self, OperateUins):
        self._OperateUins = OperateUins

    @property
    def PayModes(self):
        """计费模式编码，用作筛选
        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        """交易类型编码，用作筛选
        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def ProductCodes(self):
        """子产品编码，用作筛选
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        """地域ID，用作筛选
        :rtype: list of str
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ZoneIds(self):
        """可用区ID，用作筛选
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceTypes(self):
        """实例类型编码，用作筛选
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Tag(self):
        """标签，用作筛选
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ComponentCodes(self):
        """组件类型编码，用作筛选
        :rtype: list of str
        """
        return self._ComponentCodes

    @ComponentCodes.setter
    def ComponentCodes(self, ComponentCodes):
        self._ComponentCodes = ComponentCodes

    @property
    def ItemCodes(self):
        """组件名称编码，用作筛选
        :rtype: list of str
        """
        return self._ItemCodes

    @ItemCodes.setter
    def ItemCodes(self, ItemCodes):
        self._ItemCodes = ItemCodes

    @property
    def SearchKey(self):
        """模糊搜索：支持标签、资源id、资源别名
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        """项目ID，用作筛选
        :rtype: list of int non-negative
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._Sort = params.get("Sort")
        self._SortType = params.get("SortType")
        self._BusinessCodes = params.get("BusinessCodes")
        self._OwnerUins = params.get("OwnerUins")
        self._OperateUins = params.get("OperateUins")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._ProductCodes = params.get("ProductCodes")
        self._RegionIds = params.get("RegionIds")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Tag = params.get("Tag")
        self._ComponentCodes = params.get("ComponentCodes")
        self._ItemCodes = params.get("ItemCodes")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationBillDetailResponse(AbstractModel):
    """DescribeAllocationBillDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordNum: 总条数
        :type RecordNum: int
        :param _Total: 分账账单概览金额汇总
        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _Detail: 分账账单明细
        :type Detail: list of AllocationDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordNum = None
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def RecordNum(self):
        """总条数
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Total(self):
        """分账账单概览金额汇总
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        """分账账单明细
        :rtype: list of AllocationDetail
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        self._RecordNum = params.get("RecordNum")
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationDetail()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationMonthOverviewRequest(AbstractModel):
    """DescribeAllocationMonthOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Month: 账单月份，格式为2024-02，不传默认当前月
        :type Month: str
        """
        self._Month = None

    @property
    def Month(self):
        """账单月份，格式为2024-02，不传默认当前月
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month


    def _deserialize(self, params):
        self._Month = params.get("Month")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationMonthOverviewResponse(AbstractModel):
    """DescribeAllocationMonthOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Detail: 分账账单月概览详情
        :type Detail: list of AllocationOverviewNode
        :param _Total: 分账账单概览金额汇总
        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Detail = None
        self._Total = None
        self._RequestId = None

    @property
    def Detail(self):
        """分账账单月概览详情
        :rtype: list of AllocationOverviewNode
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Total(self):
        """分账账单概览金额汇总
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationOverviewNode()
                obj._deserialize(item)
                self._Detail.append(obj)
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        self._RequestId = params.get("RequestId")


class DescribeAllocationOverviewRequest(AbstractModel):
    """DescribeAllocationOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量，最大值为1000
        :type Limit: int
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :type Offset: int
        :param _Month: 账单月份，格式为2024-02，不传默认当前月
        :type Month: str
        :param _PeriodType: 统计周期，枚举值如下
month - 月
day - 日
        :type PeriodType: str
        :param _TreeNodeUniqKeys: 分账单元唯一标识，用作筛选
        :type TreeNodeUniqKeys: list of str
        :param _Sort: 排序字段，枚举值如下： 
GatherCashPayAmount - 归集费用(现金)
GatherVoucherPayAmount- 归集费用(优惠券)
GatherIncentivePayAmount -  归集费用(赠送金)
GatherTransferPayAmount - 归集费用(分成金)
AllocateCashPayAmount - 分摊费用(现金)
AllocateVoucherPayAmount - 分摊费用(优惠券)
AllocateIncentivePayAmount - 分摊费用(赠送金)
AllocateTransferPayAmount - 分摊费用(分成金)
TotalCashPayAmount - 合计费用(现金)
TotalVoucherPayAmount - 合计费用(优惠券)
TotalIncentivePayAmount - 合计费用(赠送金)
TotalTransferPayAmount - 合计费用(分成金)
GatherRealCost - 归集费用(折后总额)
AllocateRealCost - 分摊费用(折后总额)
RealTotalCost - 合计费用(折后总额)
Ratio  - 占比(折后总额)
        :type Sort: str
        :param _SortType: 排序类型，枚举值如下：
asc - 升序
desc - 降序
        :type SortType: str
        :param _BillDates: 日期，用作筛选
        :type BillDates: list of str
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._PeriodType = None
        self._TreeNodeUniqKeys = None
        self._Sort = None
        self._SortType = None
        self._BillDates = None

    @property
    def Limit(self):
        """数量，最大值为1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        """账单月份，格式为2024-02，不传默认当前月
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        """统计周期，枚举值如下
month - 月
day - 日
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def TreeNodeUniqKeys(self):
        """分账单元唯一标识，用作筛选
        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def Sort(self):
        """排序字段，枚举值如下： 
GatherCashPayAmount - 归集费用(现金)
GatherVoucherPayAmount- 归集费用(优惠券)
GatherIncentivePayAmount -  归集费用(赠送金)
GatherTransferPayAmount - 归集费用(分成金)
AllocateCashPayAmount - 分摊费用(现金)
AllocateVoucherPayAmount - 分摊费用(优惠券)
AllocateIncentivePayAmount - 分摊费用(赠送金)
AllocateTransferPayAmount - 分摊费用(分成金)
TotalCashPayAmount - 合计费用(现金)
TotalVoucherPayAmount - 合计费用(优惠券)
TotalIncentivePayAmount - 合计费用(赠送金)
TotalTransferPayAmount - 合计费用(分成金)
GatherRealCost - 归集费用(折后总额)
AllocateRealCost - 分摊费用(折后总额)
RealTotalCost - 合计费用(折后总额)
Ratio  - 占比(折后总额)
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SortType(self):
        """排序类型，枚举值如下：
asc - 升序
desc - 降序
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def BillDates(self):
        """日期，用作筛选
        :rtype: list of str
        """
        return self._BillDates

    @BillDates.setter
    def BillDates(self, BillDates):
        self._BillDates = BillDates


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._PeriodType = params.get("PeriodType")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._Sort = params.get("Sort")
        self._SortType = params.get("SortType")
        self._BillDates = params.get("BillDates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationOverviewResponse(AbstractModel):
    """DescribeAllocationOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordNum: 总条数
        :type RecordNum: int
        :param _Total: 分账账单概览金额汇总
        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _Detail: 分账概览明细
        :type Detail: list of AllocationOverviewDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordNum = None
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def RecordNum(self):
        """总条数
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Total(self):
        """分账账单概览金额汇总
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        """分账概览明细
        :rtype: list of AllocationOverviewDetail
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        self._RecordNum = params.get("RecordNum")
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationOverviewDetail()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationSummaryByBusinessRequest(AbstractModel):
    """DescribeAllocationSummaryByBusiness请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量，最大值为1000
        :type Limit: int
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :type Offset: int
        :param _Month: 账单月份，格式为2024-02，不传默认当前月

        :type Month: str
        :param _PeriodType: 统计周期，枚举值如下
month - 月
day - 日
        :type PeriodType: str
        :param _TreeNodeUniqKeys: 分账单元唯一标识，用作筛选

        :type TreeNodeUniqKeys: list of str
        :param _SortType: 排序类型，枚举值如下：
asc - 升序
desc - 降序
        :type SortType: str
        :param _Sort: 排序字段，枚举值如下：
GatherCashPayAmount - 归集费用(现金)
GatherVoucherPayAmount- 归集费用(优惠券)
GatherIncentivePayAmount - 归集费用(赠送金)
GatherTransferPayAmount - 归集费用(分成金)
AllocateCashPayAmount - 分摊费用(现金)
AllocateVoucherPayAmount - 分摊费用(优惠券)
AllocateIncentivePayAmount - 分摊费用(赠送金)
AllocateTransferPayAmount - 分摊费用(分成金)
TotalCashPayAmount - 合计费用(现金)
TotalVoucherPayAmount - 合计费用(优惠券)
TotalIncentivePayAmount - 合计费用(赠送金)
TotalTransferPayAmount - 合计费用(分成金)
GatherRealCost - 归集费用(折后总额)
AllocateRealCost - 分摊费用(折后总额)
RealTotalCost - 合计费用(折后总额)
BusinessCode - 产品代码
Ratio - 占比(折后总额)
Trend - 环比(折后总额)
        :type Sort: str
        :param _BillDates: 日期，用作筛选，PeriodType=day时可传

        :type BillDates: list of str
        :param _BusinessCodes: 产品编码，用作筛选
        :type BusinessCodes: list of str
        :param _SearchKey: 模糊搜索条件
        :type SearchKey: str
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._PeriodType = None
        self._TreeNodeUniqKeys = None
        self._SortType = None
        self._Sort = None
        self._BillDates = None
        self._BusinessCodes = None
        self._SearchKey = None

    @property
    def Limit(self):
        """数量，最大值为1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        """账单月份，格式为2024-02，不传默认当前月

        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        """统计周期，枚举值如下
month - 月
day - 日
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def TreeNodeUniqKeys(self):
        """分账单元唯一标识，用作筛选

        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def SortType(self):
        """排序类型，枚举值如下：
asc - 升序
desc - 降序
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def Sort(self):
        """排序字段，枚举值如下：
GatherCashPayAmount - 归集费用(现金)
GatherVoucherPayAmount- 归集费用(优惠券)
GatherIncentivePayAmount - 归集费用(赠送金)
GatherTransferPayAmount - 归集费用(分成金)
AllocateCashPayAmount - 分摊费用(现金)
AllocateVoucherPayAmount - 分摊费用(优惠券)
AllocateIncentivePayAmount - 分摊费用(赠送金)
AllocateTransferPayAmount - 分摊费用(分成金)
TotalCashPayAmount - 合计费用(现金)
TotalVoucherPayAmount - 合计费用(优惠券)
TotalIncentivePayAmount - 合计费用(赠送金)
TotalTransferPayAmount - 合计费用(分成金)
GatherRealCost - 归集费用(折后总额)
AllocateRealCost - 分摊费用(折后总额)
RealTotalCost - 合计费用(折后总额)
BusinessCode - 产品代码
Ratio - 占比(折后总额)
Trend - 环比(折后总额)
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def BillDates(self):
        """日期，用作筛选，PeriodType=day时可传

        :rtype: list of str
        """
        return self._BillDates

    @BillDates.setter
    def BillDates(self, BillDates):
        self._BillDates = BillDates

    @property
    def BusinessCodes(self):
        """产品编码，用作筛选
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def SearchKey(self):
        warnings.warn("parameter `SearchKey` is deprecated", DeprecationWarning) 

        """模糊搜索条件
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        warnings.warn("parameter `SearchKey` is deprecated", DeprecationWarning) 

        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._PeriodType = params.get("PeriodType")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._SortType = params.get("SortType")
        self._Sort = params.get("Sort")
        self._BillDates = params.get("BillDates")
        self._BusinessCodes = params.get("BusinessCodes")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationSummaryByBusinessResponse(AbstractModel):
    """DescribeAllocationSummaryByBusiness返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordNum: 总条数
        :type RecordNum: int
        :param _Total: 分账账单概览金额汇总

        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _Detail: 分账账单按产品汇总明细
        :type Detail: list of AllocationSummaryByBusiness
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordNum = None
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def RecordNum(self):
        """总条数
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Total(self):
        """分账账单概览金额汇总

        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        """分账账单按产品汇总明细
        :rtype: list of AllocationSummaryByBusiness
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        self._RecordNum = params.get("RecordNum")
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationSummaryByBusiness()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationSummaryByItemRequest(AbstractModel):
    """DescribeAllocationSummaryByItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量，最大值为1000

        :type Limit: int
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :type Offset: int
        :param _Month: 账单月份，格式为2024-02，不传默认当前月

        :type Month: str
        :param _PeriodType: 统计周期，枚举值如下
month - 月
day - 日
        :type PeriodType: str
        :param _TreeNodeUniqKeys: 分账单元唯一标识，用作筛选

        :type TreeNodeUniqKeys: list of str
        :param _Sort: 排序字段，枚举值如下：
RiTimeSpan - 预留实例抵扣时长
ExtendPayAmount1 - 预留实例抵扣组件原价
RealCost - 折后总价
CashPayAmount - 现金金额
VoucherPayAmount - 代金券金额
IncentivePayAmount - 赠送金金额
TransferPayAmount -分成金金额
Cost - 组件原价
        :type Sort: str
        :param _SortType: 排序类型，枚举值如下：
asc - 升序
desc - 降序
        :type SortType: str
        :param _BillDates: 日期，用作筛选

        :type BillDates: list of str
        :param _BusinessCodes: 产品编码，用作筛选

        :type BusinessCodes: list of str
        :param _OwnerUins: 使用者UIN，用作筛选

        :type OwnerUins: list of str
        :param _OperateUins: 操作者UIN，用作筛选

        :type OperateUins: list of str
        :param _PayModes: 计费模式编码，用作筛选

        :type PayModes: list of str
        :param _ActionTypes: 交易类型编码，用作筛选

        :type ActionTypes: list of str
        :param _ProductCodes: 子产品编码，用作筛选

        :type ProductCodes: list of str
        :param _RegionIds: 地域ID，用作筛选

        :type RegionIds: list of str
        :param _ZoneIds: 可用区ID，用作筛选

        :type ZoneIds: list of str
        :param _InstanceTypes: 实例类型编码，用作筛选

        :type InstanceTypes: list of str
        :param _Tag: 标签，用作筛选

        :type Tag: list of str
        :param _ComponentCodes: 组件类型编码，用作筛选
        :type ComponentCodes: list of str
        :param _ItemCodes: 组件名称编码，用作筛选
        :type ItemCodes: list of str
        :param _SearchKey: 模糊搜索：支持标签、资源id、资源别名
        :type SearchKey: str
        :param _ProjectIds: 项目ID，用作筛选

        :type ProjectIds: list of int non-negative
        :param _AllocationType: 费用归集类型，枚举值如下：
0 - 分摊
1 - 归集
-1 - 未分配
        :type AllocationType: list of int
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._PeriodType = None
        self._TreeNodeUniqKeys = None
        self._Sort = None
        self._SortType = None
        self._BillDates = None
        self._BusinessCodes = None
        self._OwnerUins = None
        self._OperateUins = None
        self._PayModes = None
        self._ActionTypes = None
        self._ProductCodes = None
        self._RegionIds = None
        self._ZoneIds = None
        self._InstanceTypes = None
        self._Tag = None
        self._ComponentCodes = None
        self._ItemCodes = None
        self._SearchKey = None
        self._ProjectIds = None
        self._AllocationType = None

    @property
    def Limit(self):
        """数量，最大值为1000

        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        """账单月份，格式为2024-02，不传默认当前月

        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        """统计周期，枚举值如下
month - 月
day - 日
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def TreeNodeUniqKeys(self):
        """分账单元唯一标识，用作筛选

        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def Sort(self):
        """排序字段，枚举值如下：
RiTimeSpan - 预留实例抵扣时长
ExtendPayAmount1 - 预留实例抵扣组件原价
RealCost - 折后总价
CashPayAmount - 现金金额
VoucherPayAmount - 代金券金额
IncentivePayAmount - 赠送金金额
TransferPayAmount -分成金金额
Cost - 组件原价
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SortType(self):
        """排序类型，枚举值如下：
asc - 升序
desc - 降序
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def BillDates(self):
        """日期，用作筛选

        :rtype: list of str
        """
        return self._BillDates

    @BillDates.setter
    def BillDates(self, BillDates):
        self._BillDates = BillDates

    @property
    def BusinessCodes(self):
        """产品编码，用作筛选

        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def OwnerUins(self):
        """使用者UIN，用作筛选

        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def OperateUins(self):
        """操作者UIN，用作筛选

        :rtype: list of str
        """
        return self._OperateUins

    @OperateUins.setter
    def OperateUins(self, OperateUins):
        self._OperateUins = OperateUins

    @property
    def PayModes(self):
        """计费模式编码，用作筛选

        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        """交易类型编码，用作筛选

        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def ProductCodes(self):
        """子产品编码，用作筛选

        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        """地域ID，用作筛选

        :rtype: list of str
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ZoneIds(self):
        """可用区ID，用作筛选

        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceTypes(self):
        """实例类型编码，用作筛选

        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Tag(self):
        """标签，用作筛选

        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ComponentCodes(self):
        """组件类型编码，用作筛选
        :rtype: list of str
        """
        return self._ComponentCodes

    @ComponentCodes.setter
    def ComponentCodes(self, ComponentCodes):
        self._ComponentCodes = ComponentCodes

    @property
    def ItemCodes(self):
        """组件名称编码，用作筛选
        :rtype: list of str
        """
        return self._ItemCodes

    @ItemCodes.setter
    def ItemCodes(self, ItemCodes):
        self._ItemCodes = ItemCodes

    @property
    def SearchKey(self):
        """模糊搜索：支持标签、资源id、资源别名
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        """项目ID，用作筛选

        :rtype: list of int non-negative
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def AllocationType(self):
        """费用归集类型，枚举值如下：
0 - 分摊
1 - 归集
-1 - 未分配
        :rtype: list of int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._PeriodType = params.get("PeriodType")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._Sort = params.get("Sort")
        self._SortType = params.get("SortType")
        self._BillDates = params.get("BillDates")
        self._BusinessCodes = params.get("BusinessCodes")
        self._OwnerUins = params.get("OwnerUins")
        self._OperateUins = params.get("OperateUins")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._ProductCodes = params.get("ProductCodes")
        self._RegionIds = params.get("RegionIds")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Tag = params.get("Tag")
        self._ComponentCodes = params.get("ComponentCodes")
        self._ItemCodes = params.get("ItemCodes")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        self._AllocationType = params.get("AllocationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationSummaryByItemResponse(AbstractModel):
    """DescribeAllocationSummaryByItem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordNum: 总条数

        :type RecordNum: int
        :param _Total: 分账账单概览金额汇总
        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _Detail: 分账账单按组件汇总明细

        :type Detail: list of AllocationSummaryByItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordNum = None
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def RecordNum(self):
        """总条数

        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Total(self):
        """分账账单概览金额汇总
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        """分账账单按组件汇总明细

        :rtype: list of AllocationSummaryByItem
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        self._RecordNum = params.get("RecordNum")
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationSummaryByItem()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationSummaryByResourceRequest(AbstractModel):
    """DescribeAllocationSummaryByResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量，最大值为1000

        :type Limit: int
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :type Offset: int
        :param _Month: 账单月份，格式为2024-02，不传默认当前月

        :type Month: str
        :param _PeriodType: 统计周期，枚举值如下
month - 月
day - 日
        :type PeriodType: str
        :param _TreeNodeUniqKeys: 分账单元唯一标识，用作筛选
        :type TreeNodeUniqKeys: list of str
        :param _Sort: 排序字段，枚举值如下：
RiTimeSpan - 预留实例抵扣时长
ExtendPayAmount1 - 预留实例抵扣组件原价
RealCost - 折后总价
CashPayAmount - 现金金额
VoucherPayAmount - 代金券金额
IncentivePayAmount - 赠送金金额
TransferPayAmount -分成金金额
Cost - 组件原价
        :type Sort: str
        :param _SortType: 排序类型，枚举值如下：
asc - 升序
desc - 降序
        :type SortType: str
        :param _BillDates: 日期，用作筛选
        :type BillDates: list of str
        :param _BusinessCodes: 产品编码，用作筛选
        :type BusinessCodes: list of str
        :param _OwnerUins: 使用者UIN，用作筛选
        :type OwnerUins: list of str
        :param _OperateUins: 操作者UIN，用作筛选
        :type OperateUins: list of str
        :param _PayModes: 计费模式编码，用作筛选
        :type PayModes: list of str
        :param _ActionTypes: 交易类型编码，用作筛选
        :type ActionTypes: list of str
        :param _ProductCodes: 子产品编码，用作筛选
        :type ProductCodes: list of str
        :param _RegionIds: 地域ID，用作筛选
        :type RegionIds: list of str
        :param _ZoneIds: 可用区ID，用作筛选
        :type ZoneIds: list of str
        :param _InstanceTypes: 实例类型编码，用作筛选
        :type InstanceTypes: list of str
        :param _Tag: 标签，用作筛选
        :type Tag: list of str
        :param _SearchKey: 模糊搜索：支持标签、资源id、资源别名
        :type SearchKey: str
        :param _ProjectIds: 项目ID，用作筛选
        :type ProjectIds: list of int non-negative
        :param _AllocationType: 费用归集类型，枚举值如下：
0 - 分摊 
1 - 归集 
-1 -  未分配
        :type AllocationType: list of int
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._PeriodType = None
        self._TreeNodeUniqKeys = None
        self._Sort = None
        self._SortType = None
        self._BillDates = None
        self._BusinessCodes = None
        self._OwnerUins = None
        self._OperateUins = None
        self._PayModes = None
        self._ActionTypes = None
        self._ProductCodes = None
        self._RegionIds = None
        self._ZoneIds = None
        self._InstanceTypes = None
        self._Tag = None
        self._SearchKey = None
        self._ProjectIds = None
        self._AllocationType = None

    @property
    def Limit(self):
        """数量，最大值为1000

        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        """账单月份，格式为2024-02，不传默认当前月

        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        """统计周期，枚举值如下
month - 月
day - 日
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def TreeNodeUniqKeys(self):
        """分账单元唯一标识，用作筛选
        :rtype: list of str
        """
        return self._TreeNodeUniqKeys

    @TreeNodeUniqKeys.setter
    def TreeNodeUniqKeys(self, TreeNodeUniqKeys):
        self._TreeNodeUniqKeys = TreeNodeUniqKeys

    @property
    def Sort(self):
        """排序字段，枚举值如下：
RiTimeSpan - 预留实例抵扣时长
ExtendPayAmount1 - 预留实例抵扣组件原价
RealCost - 折后总价
CashPayAmount - 现金金额
VoucherPayAmount - 代金券金额
IncentivePayAmount - 赠送金金额
TransferPayAmount -分成金金额
Cost - 组件原价
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SortType(self):
        """排序类型，枚举值如下：
asc - 升序
desc - 降序
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def BillDates(self):
        """日期，用作筛选
        :rtype: list of str
        """
        return self._BillDates

    @BillDates.setter
    def BillDates(self, BillDates):
        self._BillDates = BillDates

    @property
    def BusinessCodes(self):
        """产品编码，用作筛选
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def OwnerUins(self):
        """使用者UIN，用作筛选
        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def OperateUins(self):
        """操作者UIN，用作筛选
        :rtype: list of str
        """
        return self._OperateUins

    @OperateUins.setter
    def OperateUins(self, OperateUins):
        self._OperateUins = OperateUins

    @property
    def PayModes(self):
        """计费模式编码，用作筛选
        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def ActionTypes(self):
        """交易类型编码，用作筛选
        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes

    @property
    def ProductCodes(self):
        """子产品编码，用作筛选
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def RegionIds(self):
        """地域ID，用作筛选
        :rtype: list of str
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def ZoneIds(self):
        """可用区ID，用作筛选
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceTypes(self):
        """实例类型编码，用作筛选
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Tag(self):
        """标签，用作筛选
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def SearchKey(self):
        """模糊搜索：支持标签、资源id、资源别名
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        """项目ID，用作筛选
        :rtype: list of int non-negative
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def AllocationType(self):
        """费用归集类型，枚举值如下：
0 - 分摊 
1 - 归集 
-1 -  未分配
        :rtype: list of int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._PeriodType = params.get("PeriodType")
        self._TreeNodeUniqKeys = params.get("TreeNodeUniqKeys")
        self._Sort = params.get("Sort")
        self._SortType = params.get("SortType")
        self._BillDates = params.get("BillDates")
        self._BusinessCodes = params.get("BusinessCodes")
        self._OwnerUins = params.get("OwnerUins")
        self._OperateUins = params.get("OperateUins")
        self._PayModes = params.get("PayModes")
        self._ActionTypes = params.get("ActionTypes")
        self._ProductCodes = params.get("ProductCodes")
        self._RegionIds = params.get("RegionIds")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Tag = params.get("Tag")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        self._AllocationType = params.get("AllocationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationSummaryByResourceResponse(AbstractModel):
    """DescribeAllocationSummaryByResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordNum: 总条数

        :type RecordNum: int
        :param _Total: 分账账单概览金额汇总

        :type Total: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        :param _Detail: 分账账单按资源汇总明细

        :type Detail: list of AllocationSummaryByResource
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordNum = None
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def RecordNum(self):
        """总条数

        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Total(self):
        """分账账单概览金额汇总

        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationOverviewTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        """分账账单按资源汇总明细

        :rtype: list of AllocationSummaryByResource
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        self._RecordNum = params.get("RecordNum")
        if params.get("Total") is not None:
            self._Total = AllocationOverviewTotal()
            self._Total._deserialize(params.get("Total"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AllocationSummaryByResource()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllocationTrendByMonthRequest(AbstractModel):
    """DescribeAllocationTrendByMonth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Month: 账单月份，格式为2024-02，不传默认当前月
        :type Month: str
        :param _TreeNodeUniqKey: 分账单元唯一标识
        :type TreeNodeUniqKey: str
        :param _BusinessCode: 产品编码，用作筛选
        :type BusinessCode: str
        """
        self._Month = None
        self._TreeNodeUniqKey = None
        self._BusinessCode = None

    @property
    def Month(self):
        """账单月份，格式为2024-02，不传默认当前月
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TreeNodeUniqKey(self):
        """分账单元唯一标识
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def BusinessCode(self):
        """产品编码，用作筛选
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._BusinessCode = params.get("BusinessCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllocationTrendByMonthResponse(AbstractModel):
    """DescribeAllocationTrendByMonth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Current: 当月费用信息
        :type Current: :class:`tencentcloud.billing.v20180709.models.AllocationBillTrendDetail`
        :param _Previous: 之前月份费用信息
        :type Previous: list of AllocationBillTrendDetail
        :param _Stat: 费用统计信息
        :type Stat: :class:`tencentcloud.billing.v20180709.models.AllocationStat`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Current = None
        self._Previous = None
        self._Stat = None
        self._RequestId = None

    @property
    def Current(self):
        """当月费用信息
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationBillTrendDetail`
        """
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current

    @property
    def Previous(self):
        """之前月份费用信息
        :rtype: list of AllocationBillTrendDetail
        """
        return self._Previous

    @Previous.setter
    def Previous(self, Previous):
        self._Previous = Previous

    @property
    def Stat(self):
        """费用统计信息
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationStat`
        """
        return self._Stat

    @Stat.setter
    def Stat(self, Stat):
        self._Stat = Stat

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
        if params.get("Current") is not None:
            self._Current = AllocationBillTrendDetail()
            self._Current._deserialize(params.get("Current"))
        if params.get("Previous") is not None:
            self._Previous = []
            for item in params.get("Previous"):
                obj = AllocationBillTrendDetail()
                obj._deserialize(item)
                self._Previous.append(obj)
        if params.get("Stat") is not None:
            self._Stat = AllocationStat()
            self._Stat._deserialize(params.get("Stat"))
        self._RequestId = params.get("RequestId")


class DescribeBillAdjustInfoRequest(AbstractModel):
    """DescribeBillAdjustInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Month: 格式：yyyy-MM
账单月份，month和timeFrom&timeTo必传一个，如果有传timeFrom&timeTo则month字段无效
        :type Month: str
        :param _TimeFrom: 格式：yyyy-MM-dd
开始时间，month和timeFrom&timeTo必传一个，如果有该字段则month字段无效。timeFrom和timeTo必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据
        :type TimeFrom: str
        :param _TimeTo: 格式：yyyy-MM-dd
截止时间，month和timeFrom&timeTo必传一个，如果有该字段则month字段无效。timeFrom和timeTo必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据
        :type TimeTo: str
        """
        self._Month = None
        self._TimeFrom = None
        self._TimeTo = None

    @property
    def Month(self):
        """格式：yyyy-MM
账单月份，month和timeFrom&timeTo必传一个，如果有传timeFrom&timeTo则month字段无效
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TimeFrom(self):
        """格式：yyyy-MM-dd
开始时间，month和timeFrom&timeTo必传一个，如果有该字段则month字段无效。timeFrom和timeTo必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据
        :rtype: str
        """
        return self._TimeFrom

    @TimeFrom.setter
    def TimeFrom(self, TimeFrom):
        self._TimeFrom = TimeFrom

    @property
    def TimeTo(self):
        """格式：yyyy-MM-dd
截止时间，month和timeFrom&timeTo必传一个，如果有该字段则month字段无效。timeFrom和timeTo必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据
        :rtype: str
        """
        return self._TimeTo

    @TimeTo.setter
    def TimeTo(self, TimeTo):
        self._TimeTo = TimeTo


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._TimeFrom = params.get("TimeFrom")
        self._TimeTo = params.get("TimeTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillAdjustInfoResponse(AbstractModel):
    """DescribeBillAdjustInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 数据总量
        :type Total: int
        :param _Data: 明细数据
        :type Data: list of AdjustInfoDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        """数据总量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """明细数据
        :rtype: list of AdjustInfoDetail
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AdjustInfoDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillDetailForOrganizationRequest(AbstractModel):
    """DescribeBillDetailForOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :type Offset: int
        :param _Limit: 数量，最大值为100
        :type Limit: int
        :param _PeriodType: 周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :type PeriodType: str
        :param _Month: 月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。最多可拉取近18个月内的数据。
        :type Month: str
        :param _BeginTime: 周期开始时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据。最多可拉取18个月内的数据。
        :type BeginTime: str
        :param _EndTime: 周期结束时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据。最多可拉取近18个月内的数据。
        :type EndTime: str
        :param _NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param _PayMode: 付费模式 prePay(表示包年包月)/postPay(表示按时按量)
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
        """
        self._Offset = None
        self._Limit = None
        self._PeriodType = None
        self._Month = None
        self._BeginTime = None
        self._EndTime = None
        self._NeedRecordNum = None
        self._PayMode = None
        self._ResourceId = None
        self._ActionType = None
        self._ProjectId = None
        self._BusinessCode = None
        self._Context = None

    @property
    def Offset(self):
        """分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """数量，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PeriodType(self):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        """周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        self._PeriodType = PeriodType

    @property
    def Month(self):
        """月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。最多可拉取近18个月内的数据。
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def BeginTime(self):
        """周期开始时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据。最多可拉取18个月内的数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """周期结束时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据。最多可拉取近18个月内的数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedRecordNum(self):
        """是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def PayMode(self):
        """付费模式 prePay(表示包年包月)/postPay(表示按时按量)
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceId(self):
        """查询指定资源信息
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ActionType(self):
        """查询交易类型（请使用交易类型名称入参），入参示例枚举如下：
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
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ProjectId(self):
        """项目ID:资源所属项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def BusinessCode(self):
        """产品名称代码
备注：如需获取当月使用过的BusinessCode，请调用API：<a href="https://cloud.tencent.com/document/product/555/35761">获取产品汇总费用分布</a>
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def Context(self):
        """上一次请求返回的上下文信息，翻页查询Month>=2023-05的月份的数据可加快查询速度，数据量10万级别以上的用户建议使用，查询速度可提升2~10倍
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PeriodType = params.get("PeriodType")
        self._Month = params.get("Month")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._NeedRecordNum = params.get("NeedRecordNum")
        self._PayMode = params.get("PayMode")
        self._ResourceId = params.get("ResourceId")
        self._ActionType = params.get("ActionType")
        self._ProjectId = params.get("ProjectId")
        self._BusinessCode = params.get("BusinessCode")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillDetailForOrganizationResponse(AbstractModel):
    """DescribeBillDetailForOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetailSet: 详情列表
        :type DetailSet: list of DistributionBillDetail
        :param _Total: 总记录数，24小时缓存一次，可能比实际总记录数少
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Context: 本次请求的上下文信息，可用于下一次请求的请求参数中，加快查询速度
        :type Context: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailSet = None
        self._Total = None
        self._Context = None
        self._RequestId = None

    @property
    def DetailSet(self):
        """详情列表
        :rtype: list of DistributionBillDetail
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        """总记录数，24小时缓存一次，可能比实际总记录数少
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Context(self):
        """本次请求的上下文信息，可用于下一次请求的请求参数中，加快查询速度
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

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
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = DistributionBillDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        self._Total = params.get("Total")
        self._Context = params.get("Context")
        self._RequestId = params.get("RequestId")


class DescribeBillDetailRequest(AbstractModel):
    """DescribeBillDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :type Offset: int
        :param _Limit: 数量，最大值为300
        :type Limit: int
        :param _PeriodType: 周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :type PeriodType: str
        :param _Month: 月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。最多可拉取近18个月内的数据。
        :type Month: str
        :param _BeginTime: 周期开始时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据。最多可拉取18个月内的数据。
        :type BeginTime: str
        :param _EndTime: 周期结束时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据。最多可拉取近18个月内的数据。
        :type EndTime: str
        :param _NeedRecordNum: 是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param _ProductCode: 已废弃参数，未开放
        :type ProductCode: str
        :param _PayMode: 付费模式 prePay(表示包年包月)/postPay(表示按时按量)
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
        """分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """数量，最大值为300
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PeriodType(self):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        """周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        self._PeriodType = PeriodType

    @property
    def Month(self):
        """月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。最多可拉取近18个月内的数据。
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def BeginTime(self):
        """周期开始时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据。最多可拉取18个月内的数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """周期结束时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为相同月份，不支持跨月查询，查询结果是整月数据。最多可拉取近18个月内的数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedRecordNum(self):
        """是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def ProductCode(self):
        """已废弃参数，未开放
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def PayMode(self):
        """付费模式 prePay(表示包年包月)/postPay(表示按时按量)
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceId(self):
        """查询指定资源信息
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ActionType(self):
        """查询交易类型（请使用交易类型名称入参），入参示例枚举如下：
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
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ProjectId(self):
        """项目ID:资源所属项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def BusinessCode(self):
        """产品名称代码
备注：如需获取当月使用过的BusinessCode，请调用API：<a href="https://cloud.tencent.com/document/product/555/35761">获取产品汇总费用分布</a>
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def Context(self):
        """上一次请求返回的上下文信息，翻页查询Month>=2023-05的月份的数据可加快查询速度，数据量10万级别以上的用户建议使用，查询速度可提升2~10倍
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def PayerUin(self):
        """支付者的账号 ID（账号 ID 是用户在腾讯云的唯一账号标识），默认查询本账号账单，如集团管理账号需查询成员账号自付的账单，该字段需入参成员账号UIN
        :rtype: str
        """
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
        :type Total: int
        :param _Context: 本次请求的上下文信息，可用于下一次请求的请求参数中，加快查询速度
        :type Context: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailSet = None
        self._Total = None
        self._Context = None
        self._RequestId = None

    @property
    def DetailSet(self):
        """详情列表
        :rtype: list of BillDetail
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        """总记录数，24小时缓存一次，可能比实际总记录数少
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Context(self):
        """本次请求的上下文信息，可用于下一次请求的请求参数中，加快查询速度
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

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
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = BillDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        self._Total = params.get("Total")
        self._Context = params.get("Context")
        self._RequestId = params.get("RequestId")


class DescribeBillDownloadUrlRequest(AbstractModel):
    """DescribeBillDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileType: 账单类型，枚举值
billOverview=L0-PDF账单
billSummary=L1-汇总账单	
billResource=L2-资源账单	
billDetail=L3-明细账单	
billPack=账单包
        :type FileType: str
        :param _Month: 账单月份
支持的最早开始月份为2021-01
L0-PDF&账单包不支持当月下载，当月账单请在次月1号19:00出账后下载
        :type Month: str
        :param _ChildUin: 下载的账号 ID列表，默认查询本账号账单，如集团管理账号需下载成员账号自付的账单，该字段需入参成员账号UIN
        :type ChildUin: list of str
        """
        self._FileType = None
        self._Month = None
        self._ChildUin = None

    @property
    def FileType(self):
        """账单类型，枚举值
billOverview=L0-PDF账单
billSummary=L1-汇总账单	
billResource=L2-资源账单	
billDetail=L3-明细账单	
billPack=账单包
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Month(self):
        """账单月份
支持的最早开始月份为2021-01
L0-PDF&账单包不支持当月下载，当月账单请在次月1号19:00出账后下载
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def ChildUin(self):
        """下载的账号 ID列表，默认查询本账号账单，如集团管理账号需下载成员账号自付的账单，该字段需入参成员账号UIN
        :rtype: list of str
        """
        return self._ChildUin

    @ChildUin.setter
    def ChildUin(self, ChildUin):
        self._ChildUin = ChildUin


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._Month = params.get("Month")
        self._ChildUin = params.get("ChildUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillDownloadUrlResponse(AbstractModel):
    """DescribeBillDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 账单文件是否准备就绪，0文件生成中，1文件已生成
        :type Ready: int
        :param _DownloadUrl: 账单文件下载链接，有效时长为一天
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def Ready(self):
        """账单文件是否准备就绪，0文件生成中，1文件已生成
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def DownloadUrl(self):
        """账单文件下载链接，有效时长为一天
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

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
        self._Ready = params.get("Ready")
        self._DownloadUrl = params.get("DownloadUrl")
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
        """查询范围的起始时间（包含）时间格式 yyyy-MM-dd HH:mm:ss 开始时间和结束时间差值小于等于六个月
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询范围的结束时间（包含）时间格式 yyyy-MM-dd HH:mm:ss ，开始时间和结束时间差值小于等于六个月
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """翻页偏移量，初始值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页的限制数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PayType(self):
        """交易类型： all所有交易类型，recharge充值，return退款，unblock解冻，agentin资金转入，advanced垫付，cash提现，deduct扣费，block冻结，agentout资金转出，repay垫付回款，repayment还款(仅国际信用账户)，adj_refund调增(仅国际信用账户)，adj_deduct调减(仅国际信用账户)
        :rtype: list of str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def SubPayType(self):
        """扣费模式，
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
        :rtype: list of str
        """
        return self._SubPayType

    @SubPayType.setter
    def SubPayType(self, SubPayType):
        self._SubPayType = SubPayType

    @property
    def WithZeroAmount(self):
        """是否返回0元交易金额的交易项，取值：0-不返回，1-返回。不传该参数则不返回
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        """收支明细列表
        :rtype: list of BillTransactionInfo
        """
        return self._TransactionList

    @TransactionList.setter
    def TransactionList(self, TransactionList):
        self._TransactionList = TransactionList

    @property
    def Total(self):
        """总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ReturnAmount(self):
        """退费总额，单位（分）
        :rtype: float
        """
        return self._ReturnAmount

    @ReturnAmount.setter
    def ReturnAmount(self, ReturnAmount):
        self._ReturnAmount = ReturnAmount

    @property
    def RechargeAmount(self):
        """充值总额，单位（分）
        :rtype: float
        """
        return self._RechargeAmount

    @RechargeAmount.setter
    def RechargeAmount(self, RechargeAmount):
        self._RechargeAmount = RechargeAmount

    @property
    def BlockAmount(self):
        """冻结总额，单位（分）
        :rtype: float
        """
        return self._BlockAmount

    @BlockAmount.setter
    def BlockAmount(self, BlockAmount):
        self._BlockAmount = BlockAmount

    @property
    def UnblockAmount(self):
        """解冻总额，单位（分）
        :rtype: float
        """
        return self._UnblockAmount

    @UnblockAmount.setter
    def UnblockAmount(self, UnblockAmount):
        self._UnblockAmount = UnblockAmount

    @property
    def DeductAmount(self):
        """扣费总额，单位（分）
        :rtype: float
        """
        return self._DeductAmount

    @DeductAmount.setter
    def DeductAmount(self, DeductAmount):
        self._DeductAmount = DeductAmount

    @property
    def AgentInAmount(self):
        """资金转入总额，单位（分）
        :rtype: float
        """
        return self._AgentInAmount

    @AgentInAmount.setter
    def AgentInAmount(self, AgentInAmount):
        self._AgentInAmount = AgentInAmount

    @property
    def AdvanceRechargeAmount(self):
        """垫付充值总额，单位（分）
        :rtype: float
        """
        return self._AdvanceRechargeAmount

    @AdvanceRechargeAmount.setter
    def AdvanceRechargeAmount(self, AdvanceRechargeAmount):
        self._AdvanceRechargeAmount = AdvanceRechargeAmount

    @property
    def WithdrawAmount(self):
        """提现扣减总额，单位（分）
        :rtype: float
        """
        return self._WithdrawAmount

    @WithdrawAmount.setter
    def WithdrawAmount(self, WithdrawAmount):
        self._WithdrawAmount = WithdrawAmount

    @property
    def AgentOutAmount(self):
        """资金转出总额，单位（分）
        :rtype: float
        """
        return self._AgentOutAmount

    @AgentOutAmount.setter
    def AgentOutAmount(self, AgentOutAmount):
        self._AgentOutAmount = AgentOutAmount

    @property
    def AdvancePayAmount(self):
        """还垫付总额，单位（分）
        :rtype: float
        """
        return self._AdvancePayAmount

    @AdvancePayAmount.setter
    def AdvancePayAmount(self, AdvancePayAmount):
        self._AdvancePayAmount = AdvancePayAmount

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


class DescribeBillResourceSummaryForOrganizationRequest(AbstractModel):
    """DescribeBillResourceSummaryForOrganization请求参数结构体

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
        :param _TagKey: 分账标签键，用户自定义（支持2021-01以后账单查询）
        :type TagKey: str
        :param _TagValue: 分账标签值，该参数为空表示该标签键下未设置标签值的记录
（支持2021-01以后账单查询）
        :type TagValue: str
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
        self._TagKey = None
        self._TagValue = None

    @property
    def Offset(self):
        """分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """数量，最大值为1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Month(self):
        """月份，格式为yyyy-mm。不能早于开通账单2.0的月份
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        """周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        self._PeriodType = PeriodType

    @property
    def NeedRecordNum(self):
        """是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def ActionType(self):
        """查询交易类型（请使用交易类型名称入参），入参示例枚举如下：
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
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceId(self):
        """查询指定资源信息
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def PayMode(self):
        """付费模式 prePay/postPay
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def BusinessCode(self):
        """产品名称代码
备注：如需获取当月使用过的BusinessCode，请调用API：<a href="https://cloud.tencent.com/document/product/555/35761">获取产品汇总费用分布</a>
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def TagKey(self):
        """分账标签键，用户自定义（支持2021-01以后账单查询）
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """分账标签值，该参数为空表示该标签键下未设置标签值的记录
（支持2021-01以后账单查询）
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


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
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillResourceSummaryForOrganizationResponse(AbstractModel):
    """DescribeBillResourceSummaryForOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceSummarySet: 资源汇总列表
        :type ResourceSummarySet: list of BillDistributionResourceSummary
        :param _Total: 资源汇总列表总数，入参NeedRecordNum为0时不返回
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceSummarySet = None
        self._Total = None
        self._RequestId = None

    @property
    def ResourceSummarySet(self):
        """资源汇总列表
        :rtype: list of BillDistributionResourceSummary
        """
        return self._ResourceSummarySet

    @ResourceSummarySet.setter
    def ResourceSummarySet(self, ResourceSummarySet):
        self._ResourceSummarySet = ResourceSummarySet

    @property
    def Total(self):
        """资源汇总列表总数，入参NeedRecordNum为0时不返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("ResourceSummarySet") is not None:
            self._ResourceSummarySet = []
            for item in params.get("ResourceSummarySet"):
                obj = BillDistributionResourceSummary()
                obj._deserialize(item)
                self._ResourceSummarySet.append(obj)
        self._Total = params.get("Total")
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
        :param _TagKey: 分账标签键，用户自定义（支持2021-01以后账单查询）
        :type TagKey: str
        :param _TagValue: 分账标签值，该参数为空表示该标签键下未设置标签值的记录
（支持2021-01以后账单查询）
        :type TagValue: str
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
        self._TagKey = None
        self._TagValue = None

    @property
    def Offset(self):
        """分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """数量，最大值为1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Month(self):
        """月份，格式为yyyy-mm。不能早于开通账单2.0的月份
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def PeriodType(self):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        """周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        warnings.warn("parameter `PeriodType` is deprecated", DeprecationWarning) 

        self._PeriodType = PeriodType

    @property
    def NeedRecordNum(self):
        """是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def ActionType(self):
        """查询交易类型（请使用交易类型名称入参），入参示例枚举如下：
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
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceId(self):
        """查询指定资源信息
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def PayMode(self):
        """付费模式 prePay/postPay
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def BusinessCode(self):
        """产品名称代码
备注：如需获取当月使用过的BusinessCode，请调用API：<a href="https://cloud.tencent.com/document/product/555/35761">获取产品汇总费用分布</a>
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def PayerUin(self):
        """支付者的账号 ID（账号 ID 是用户在腾讯云的唯一账号标识），默认查询本账号账单，如集团管理账号需查询成员账号自付的账单，该字段需入参成员账号UIN
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def TagKey(self):
        """分账标签键，用户自定义（支持2021-01以后账单查询）
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """分账标签值，该参数为空表示该标签键下未设置标签值的记录
（支持2021-01以后账单查询）
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


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
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceSummarySet = None
        self._Total = None
        self._RequestId = None

    @property
    def ResourceSummarySet(self):
        """资源汇总列表
        :rtype: list of BillResourceSummary
        """
        return self._ResourceSummarySet

    @ResourceSummarySet.setter
    def ResourceSummarySet(self, ResourceSummarySet):
        self._ResourceSummarySet = ResourceSummarySet

    @property
    def Total(self):
        """资源汇总列表总数，入参NeedRecordNum为0时不返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        """目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        """查询账单数据的用户UIN
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        """数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        """各付费模式花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PayModeSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

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
        """目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        """查询账单数据的用户UIN
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def PayType(self):
        """款项类别，与L0账单上的汇总类别对应。
此参数自账单3.0（即2021-05）之后开始生效。
枚举值：
consume-消费
refund-退款
adjustment-调账
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryTotal = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        """数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryTotal(self):
        """总花费详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.billing.v20180709.models.BusinessSummaryTotal`
        """
        return self._SummaryTotal

    @SummaryTotal.setter
    def SummaryTotal(self, SummaryTotal):
        self._SummaryTotal = SummaryTotal

    @property
    def SummaryOverview(self):
        """各产品花费分布
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BusinessSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

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
        """目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        """查询账单数据的用户UIN
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        """数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        """各项目花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ProjectSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

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
        """目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PayerUin(self):
        """查询账单数据的用户UIN
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._RequestId = None

    @property
    def Ready(self):
        """数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        """各地域花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RegionSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

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
        """目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TagKey(self):
        """分账标签键，用户自定义
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def PayerUin(self):
        """查询账单数据的用户UIN
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def TagValue(self):
        """分账标签值
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryOverview = None
        self._SummaryTotal = None
        self._RequestId = None

    @property
    def Ready(self):
        """数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryOverview(self):
        """各标签值花费分布详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TagSummaryOverviewItem
        """
        return self._SummaryOverview

    @SummaryOverview.setter
    def SummaryOverview(self, SummaryOverview):
        self._SummaryOverview = SummaryOverview

    @property
    def SummaryTotal(self):
        """总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.billing.v20180709.models.SummaryTotal`
        """
        return self._SummaryTotal

    @SummaryTotal.setter
    def SummaryTotal(self, SummaryTotal):
        self._SummaryTotal = SummaryTotal

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


class DescribeBillSummaryForOrganizationRequest(AbstractModel):
    """DescribeBillSummaryForOrganization请求参数结构体

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
        """账单月份，格式为2023-04
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def GroupType(self):
        """账单维度类型，枚举值如下：business、project、region、payMode、tag
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def TagKey(self):
        """标签键，GroupType=tag获取标签维度账单时传
        :rtype: list of str
        """
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
        


class DescribeBillSummaryForOrganizationResponse(AbstractModel):
    """DescribeBillSummaryForOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ready: 数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :type Ready: int
        :param _SummaryDetail: 账单多维度汇总消费详情
        :type SummaryDetail: list of SummaryDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryDetail = None
        self._RequestId = None

    @property
    def Ready(self):
        """数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryDetail(self):
        """账单多维度汇总消费详情
        :rtype: list of SummaryDetail
        """
        return self._SummaryDetail

    @SummaryDetail.setter
    def SummaryDetail(self, SummaryDetail):
        self._SummaryDetail = SummaryDetail

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
        self._Ready = params.get("Ready")
        if params.get("SummaryDetail") is not None:
            self._SummaryDetail = []
            for item in params.get("SummaryDetail"):
                obj = SummaryDetail()
                obj._deserialize(item)
                self._SummaryDetail.append(obj)
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
        """账单月份，格式为2023-04
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def GroupType(self):
        """账单维度类型，枚举值如下：business、project、region、payMode、tag
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def TagKey(self):
        """标签键，GroupType=tag获取标签维度账单时传
        :rtype: list of str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._SummaryDetail = None
        self._RequestId = None

    @property
    def Ready(self):
        """数据是否准备好，0准备中，1已就绪。（Ready=0，为当前UIN首次进行初始化出账，预计需要5~10分钟出账，请于10分钟后重试即可）
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def SummaryDetail(self):
        """账单多维度汇总消费详情
        :rtype: list of SummaryDetail
        """
        return self._SummaryDetail

    @SummaryDetail.setter
    def SummaryDetail(self, SummaryDetail):
        self._SummaryDetail = SummaryDetail

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
        """数量，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def BeginTime(self):
        """周期开始时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为同一月份，暂不支持跨月拉取。可拉取的数据是开通成本分析后，且距今 24 个月内的数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """周期结束时间，格式为yyyy-mm-dd hh:ii:ss，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传，且为同一月份，暂不支持跨月拉取。可拉取的数据是开通成本分析后，且距今 24 个月内的数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedRecordNum(self):
        """是否需要访问列表的总记录数，用于前端分页
1-表示需要， 0-表示不需要
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def Month(self):
        """月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通成本分析的月份，最多可拉取24个月内的数据。
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def ProductCode(self):
        """查询指定产品信息（暂时未开放获取）
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def PayMode(self):
        """付费模式 prePay/postPay
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResourceId(self):
        """查询指定资源信息
        :rtype: str
        """
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
        :type DetailSet: list of CostDetail
        :param _Total: 记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailSet = None
        self._Total = None
        self._RequestId = None

    @property
    def DetailSet(self):
        """消耗明细
        :rtype: list of CostDetail
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def Total(self):
        """记录数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = CostDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCostExplorerSummaryRequest(AbstractModel):
    """DescribeCostExplorerSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 周期开始时间，格式为yyyy-mm-dd hh:ii:ss
        :type BeginTime: str
        :param _EndTime: 周期结束时间，格式为yyyy-mm-dd hh:ii:ss
        :type EndTime: str
        :param _BillType: 账单类型：1-费用账单、2-消耗账单
        :type BillType: str
        :param _PeriodType: 统计周期：日-day，月-month；
        :type PeriodType: str
        :param _Dimensions: 分类维度（数据汇总维度），查询分类维度（请使用分类维度code入参）入参枚举值：
default=仅总计
feeType=费用类型
billType=账单类型
business=产品
product=子产品
region=地域
zone=可用区
actionType=交易类型
payMode =计费模式
tags=标签
project =项目
payerUin=支付者账号
ownerUin=使用者账号
        :type Dimensions: str
        :param _FeeType: 费用类型：cost-总费用，totalCost-原价费用
        :type FeeType: str
        :param _PageSize: 数量，每页最大值为100
        :type PageSize: int
        :param _PageNo: 起始页，当PageNo=1表示第一页， PageNo=2表示第二页，依次类推。
        :type PageNo: int
        :param _TagKeyStr: 分账标签值
        :type TagKeyStr: str
        :param _NeedConditionValue: 是否需要筛选框， 1-表示需要， 0-表示不需要，若不传默认不需要。
        :type NeedConditionValue: str
        :param _Conditions: 筛选参数
        :type Conditions: :class:`tencentcloud.billing.v20180709.models.AnalyseConditions`
        """
        self._BeginTime = None
        self._EndTime = None
        self._BillType = None
        self._PeriodType = None
        self._Dimensions = None
        self._FeeType = None
        self._PageSize = None
        self._PageNo = None
        self._TagKeyStr = None
        self._NeedConditionValue = None
        self._Conditions = None

    @property
    def BeginTime(self):
        """周期开始时间，格式为yyyy-mm-dd hh:ii:ss
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """周期结束时间，格式为yyyy-mm-dd hh:ii:ss
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BillType(self):
        """账单类型：1-费用账单、2-消耗账单
        :rtype: str
        """
        return self._BillType

    @BillType.setter
    def BillType(self, BillType):
        self._BillType = BillType

    @property
    def PeriodType(self):
        """统计周期：日-day，月-month；
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def Dimensions(self):
        """分类维度（数据汇总维度），查询分类维度（请使用分类维度code入参）入参枚举值：
default=仅总计
feeType=费用类型
billType=账单类型
business=产品
product=子产品
region=地域
zone=可用区
actionType=交易类型
payMode =计费模式
tags=标签
project =项目
payerUin=支付者账号
ownerUin=使用者账号
        :rtype: str
        """
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def FeeType(self):
        """费用类型：cost-总费用，totalCost-原价费用
        :rtype: str
        """
        return self._FeeType

    @FeeType.setter
    def FeeType(self, FeeType):
        self._FeeType = FeeType

    @property
    def PageSize(self):
        """数量，每页最大值为100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        """起始页，当PageNo=1表示第一页， PageNo=2表示第二页，依次类推。
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def TagKeyStr(self):
        """分账标签值
        :rtype: str
        """
        return self._TagKeyStr

    @TagKeyStr.setter
    def TagKeyStr(self, TagKeyStr):
        self._TagKeyStr = TagKeyStr

    @property
    def NeedConditionValue(self):
        """是否需要筛选框， 1-表示需要， 0-表示不需要，若不传默认不需要。
        :rtype: str
        """
        return self._NeedConditionValue

    @NeedConditionValue.setter
    def NeedConditionValue(self, NeedConditionValue):
        self._NeedConditionValue = NeedConditionValue

    @property
    def Conditions(self):
        """筛选参数
        :rtype: :class:`tencentcloud.billing.v20180709.models.AnalyseConditions`
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._BillType = params.get("BillType")
        self._PeriodType = params.get("PeriodType")
        self._Dimensions = params.get("Dimensions")
        self._FeeType = params.get("FeeType")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._TagKeyStr = params.get("TagKeyStr")
        self._NeedConditionValue = params.get("NeedConditionValue")
        if params.get("Conditions") is not None:
            self._Conditions = AnalyseConditions()
            self._Conditions._deserialize(params.get("Conditions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCostExplorerSummaryResponse(AbstractModel):
    """DescribeCostExplorerSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 数据条数
        :type Total: int
        :param _Header: 表头信息
        :type Header: :class:`tencentcloud.billing.v20180709.models.AnalyseHeaderDetail`
        :param _Detail: 数据明细
        :type Detail: list of AnalyseDetail
        :param _TotalDetail: 数据总计
        :type TotalDetail: :class:`tencentcloud.billing.v20180709.models.AnalyseDetail`
        :param _ConditionValue: 筛选框
        :type ConditionValue: :class:`tencentcloud.billing.v20180709.models.AnalyseConditionDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Header = None
        self._Detail = None
        self._TotalDetail = None
        self._ConditionValue = None
        self._RequestId = None

    @property
    def Total(self):
        """数据条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Header(self):
        """表头信息
        :rtype: :class:`tencentcloud.billing.v20180709.models.AnalyseHeaderDetail`
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Detail(self):
        """数据明细
        :rtype: list of AnalyseDetail
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def TotalDetail(self):
        """数据总计
        :rtype: :class:`tencentcloud.billing.v20180709.models.AnalyseDetail`
        """
        return self._TotalDetail

    @TotalDetail.setter
    def TotalDetail(self, TotalDetail):
        self._TotalDetail = TotalDetail

    @property
    def ConditionValue(self):
        """筛选框
        :rtype: :class:`tencentcloud.billing.v20180709.models.AnalyseConditionDetail`
        """
        return self._ConditionValue

    @ConditionValue.setter
    def ConditionValue(self, ConditionValue):
        self._ConditionValue = ConditionValue

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
        self._Total = params.get("Total")
        if params.get("Header") is not None:
            self._Header = AnalyseHeaderDetail()
            self._Header._deserialize(params.get("Header"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = AnalyseDetail()
                obj._deserialize(item)
                self._Detail.append(obj)
        if params.get("TotalDetail") is not None:
            self._TotalDetail = AnalyseDetail()
            self._TotalDetail._deserialize(params.get("TotalDetail"))
        if params.get("ConditionValue") is not None:
            self._ConditionValue = AnalyseConditionDetail()
            self._ConditionValue._deserialize(params.get("ConditionValue"))
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
        """目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """每次获取数据量，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量,默认从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        """查询账单数据的用户UIN
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        """是否需要返回记录数量，0不需要，1需要，默认不需要
        :rtype: int
        """
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
        :type Data: list of ConsumptionBusinessSummaryDataItem
        :param _RecordNum: 记录数量，NeedRecordNum为0时返回null
        :type RecordNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._Total = None
        self._Data = None
        self._RecordNum = None
        self._RequestId = None

    @property
    def Ready(self):
        """数据是否准备好，0未准备好，1准备好
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        """消耗详情
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """消耗按产品汇总详情
        :rtype: list of ConsumptionBusinessSummaryDataItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        """记录数量，NeedRecordNum为0时返回null
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

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
        """目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """每次获取数据量，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量,默认从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        """查询账单数据的用户UIN
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        """是否需要返回记录数量，0不需要，1需要，默认不需要
        :rtype: int
        """
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
        :param _RecordNum: 记录数量，NeedRecordNum为0时返回null
        :type RecordNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._Total = None
        self._Data = None
        self._RecordNum = None
        self._RequestId = None

    @property
    def Ready(self):
        """数据是否准备好，0未准备好，1准备好
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        """消耗详情
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """消耗按业务汇总详情
        :rtype: list of ConsumptionProjectSummaryDataItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        """记录数量，NeedRecordNum为0时返回null
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

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
        """目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """每次获取数据量，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量,默认从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        """查询账单数据的用户UIN
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        """是否需要返回记录数量，0不需要，1需要，默认不需要
        :rtype: int
        """
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
        :param _RecordNum: 记录数量，NeedRecordNum为0时返回null
        :type RecordNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ready = None
        self._Total = None
        self._Data = None
        self._RecordNum = None
        self._RequestId = None

    @property
    def Ready(self):
        """数据是否准备好，0未准备好，1准备好
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        """消耗详情
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """消耗按地域汇总详情
        :rtype: list of ConsumptionRegionSummaryDataItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RecordNum(self):
        """记录数量，NeedRecordNum为0时返回null
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

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
        """目前必须和EndTime相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """目前必须和BeginTime为相同月份，不支持跨月查询，且查询结果是整月数据，例如 BeginTime为2018-09，EndTime 为 2018-09，查询结果是 2018 年 9 月数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """每次获取数据量，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量,默认从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PayerUin(self):
        """查询账单数据的用户UIN
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def NeedRecordNum(self):
        """是否需要返回记录数量，0不需要，1需要，默认不需要
        :rtype: int
        """
        return self._NeedRecordNum

    @NeedRecordNum.setter
    def NeedRecordNum(self, NeedRecordNum):
        self._NeedRecordNum = NeedRecordNum

    @property
    def NeedConditionValue(self):
        """是否需要返回过滤条件，0不需要，1需要，默认不需要
        :rtype: int
        """
        return self._NeedConditionValue

    @NeedConditionValue.setter
    def NeedConditionValue(self, NeedConditionValue):
        self._NeedConditionValue = NeedConditionValue

    @property
    def Conditions(self):
        """过滤条件，只支持ResourceKeyword(资源关键字，支持资源id及资源名称模糊查询)，ProjectIds（项目id），RegionIds(地域id)，PayModes(付费模式，可选prePay和postPay)，HideFreeCost（是否隐藏0元流水，可选0和1），OrderByCost（按费用排序规则，可选desc和asc）
        :rtype: :class:`tencentcloud.billing.v20180709.models.Conditions`
        """
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
        :type Total: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param _ConditionValue: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionValue: :class:`tencentcloud.billing.v20180709.models.ConsumptionResourceSummaryConditionValue`
        :param _RecordNum: 记录数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordNum: int
        :param _Data: 资源消耗详情
        :type Data: list of ConsumptionResourceSummaryDataItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        """数据是否准备好，0未准备好，1准备好
        :rtype: int
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Total(self):
        """消耗详情
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConditionValue(self):
        """过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.billing.v20180709.models.ConsumptionResourceSummaryConditionValue`
        """
        return self._ConditionValue

    @ConditionValue.setter
    def ConditionValue(self, ConditionValue):
        self._ConditionValue = ConditionValue

    @property
    def RecordNum(self):
        """记录数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Data(self):
        """资源消耗详情
        :rtype: list of ConsumptionResourceSummaryDataItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        :param _OrderId: 子订单号
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
        """开始时间 2016-01-01 00:00:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间 2016-02-01 00:00:00 建议跨度不超过3个月
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """一页多少条数据，默认是20条，最大不超过1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """第多少页，从0开始，默认是0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        """订单状态,默认为4（成功的订单）
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
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderId(self):
        """子订单号
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BigDealId(self):
        """大订单号
        :rtype: str
        """
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def ResourceId(self):
        """资源id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Deals = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Deals(self):
        """订单列表
        :rtype: list of Deal
        """
        return self._Deals

    @Deals.setter
    def Deals(self, Deals):
        self._Deals = Deals

    @property
    def TotalCount(self):
        """订单总数
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
        :param _StartDate: 查询用量开始时间，格式为yyyy-mm-dd，例如：2020-09-01
        :type StartDate: str
        :param _EndDate: 查询用量结束时间，格式为yyyy-mm-dd，例如：2020-09-30（与开始时间同月，不支持跨月查询）
        :type EndDate: str
        :param _BucketName: COS 存储桶名称，可通过Get Service 接口是用来获取请求者名下的所有存储空间列表（Bucket list）https://cloud.tencent.com/document/product/436/8291
        :type BucketName: str
        """
        self._StartDate = None
        self._EndDate = None
        self._BucketName = None

    @property
    def StartDate(self):
        """查询用量开始时间，格式为yyyy-mm-dd，例如：2020-09-01
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """查询用量结束时间，格式为yyyy-mm-dd，例如：2020-09-30（与开始时间同月，不支持跨月查询）
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def BucketName(self):
        """COS 存储桶名称，可通过Get Service 接口是用来获取请求者名下的所有存储空间列表（Bucket list）https://cloud.tencent.com/document/product/436/8291
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailSets = None
        self._RequestId = None

    @property
    def DetailSets(self):
        """用量数组
        :rtype: list of CosDetailSets
        """
        return self._DetailSets

    @DetailSets.setter
    def DetailSets(self, DetailSets):
        self._DetailSets = DetailSets

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
        if params.get("DetailSets") is not None:
            self._DetailSets = []
            for item in params.get("DetailSets"):
                obj = CosDetailSets()
                obj._deserialize(item)
                self._DetailSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDosageDetail(AbstractModel):
    """计量标准接入类产品支持API接口获取用量明细返回数据结构

    """

    def __init__(self):
        r"""
        :param _Date: 日期
        :type Date: str
        :param _Uin: 账号 ID 是用户在腾讯云的唯一账号标识
        :type Uin: str
        :param _DosageType: 用量统计类型
        :type DosageType: str
        :param _ProductCode: 产品编码
        :type ProductCode: str
        :param _SubProductCode: 子产品编码
        :type SubProductCode: str
        :param _BillingItemCode: 组件类型编码

        :type BillingItemCode: str
        :param _SubBillingItemCode: 组件编码
        :type SubBillingItemCode: str
        :param _ProductCodeName: 产品名称
        :type ProductCodeName: str
        :param _SubProductCodeName: 子产品名称
        :type SubProductCodeName: str
        :param _BillingItemCodeName: 组件类型
        :type BillingItemCodeName: str
        :param _SubBillingItemCodeName: 组件
        :type SubBillingItemCodeName: str
        :param _DosageUnit: 用量单位
        :type DosageUnit: str
        :param _DosageBeginTime: 用量起始时间
        :type DosageBeginTime: str
        :param _DosageEndTime: 用量截止时间
        :type DosageEndTime: str
        :param _DosageValue: 标准用量
        :type DosageValue: float
        :param _DeductValue: 抵扣用量
        :type DeductValue: float
        :param _RemainValue: 抵扣余量
        :type RemainValue: float
        :param _SdkAppId: sdkAppId
        :type SdkAppId: str
        :param _AttrStr: 其他信息
        :type AttrStr: list of JsonObject
        :param _SheetName: 用量模板名称
        :type SheetName: list of str
        """
        self._Date = None
        self._Uin = None
        self._DosageType = None
        self._ProductCode = None
        self._SubProductCode = None
        self._BillingItemCode = None
        self._SubBillingItemCode = None
        self._ProductCodeName = None
        self._SubProductCodeName = None
        self._BillingItemCodeName = None
        self._SubBillingItemCodeName = None
        self._DosageUnit = None
        self._DosageBeginTime = None
        self._DosageEndTime = None
        self._DosageValue = None
        self._DeductValue = None
        self._RemainValue = None
        self._SdkAppId = None
        self._AttrStr = None
        self._SheetName = None

    @property
    def Date(self):
        """日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Uin(self):
        """账号 ID 是用户在腾讯云的唯一账号标识
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def DosageType(self):
        """用量统计类型
        :rtype: str
        """
        return self._DosageType

    @DosageType.setter
    def DosageType(self, DosageType):
        self._DosageType = DosageType

    @property
    def ProductCode(self):
        """产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def BillingItemCode(self):
        """组件类型编码

        :rtype: str
        """
        return self._BillingItemCode

    @BillingItemCode.setter
    def BillingItemCode(self, BillingItemCode):
        self._BillingItemCode = BillingItemCode

    @property
    def SubBillingItemCode(self):
        """组件编码
        :rtype: str
        """
        return self._SubBillingItemCode

    @SubBillingItemCode.setter
    def SubBillingItemCode(self, SubBillingItemCode):
        self._SubBillingItemCode = SubBillingItemCode

    @property
    def ProductCodeName(self):
        """产品名称
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def SubProductCodeName(self):
        """子产品名称
        :rtype: str
        """
        return self._SubProductCodeName

    @SubProductCodeName.setter
    def SubProductCodeName(self, SubProductCodeName):
        self._SubProductCodeName = SubProductCodeName

    @property
    def BillingItemCodeName(self):
        """组件类型
        :rtype: str
        """
        return self._BillingItemCodeName

    @BillingItemCodeName.setter
    def BillingItemCodeName(self, BillingItemCodeName):
        self._BillingItemCodeName = BillingItemCodeName

    @property
    def SubBillingItemCodeName(self):
        """组件
        :rtype: str
        """
        return self._SubBillingItemCodeName

    @SubBillingItemCodeName.setter
    def SubBillingItemCodeName(self, SubBillingItemCodeName):
        self._SubBillingItemCodeName = SubBillingItemCodeName

    @property
    def DosageUnit(self):
        """用量单位
        :rtype: str
        """
        return self._DosageUnit

    @DosageUnit.setter
    def DosageUnit(self, DosageUnit):
        self._DosageUnit = DosageUnit

    @property
    def DosageBeginTime(self):
        """用量起始时间
        :rtype: str
        """
        return self._DosageBeginTime

    @DosageBeginTime.setter
    def DosageBeginTime(self, DosageBeginTime):
        self._DosageBeginTime = DosageBeginTime

    @property
    def DosageEndTime(self):
        """用量截止时间
        :rtype: str
        """
        return self._DosageEndTime

    @DosageEndTime.setter
    def DosageEndTime(self, DosageEndTime):
        self._DosageEndTime = DosageEndTime

    @property
    def DosageValue(self):
        """标准用量
        :rtype: float
        """
        return self._DosageValue

    @DosageValue.setter
    def DosageValue(self, DosageValue):
        self._DosageValue = DosageValue

    @property
    def DeductValue(self):
        """抵扣用量
        :rtype: float
        """
        return self._DeductValue

    @DeductValue.setter
    def DeductValue(self, DeductValue):
        self._DeductValue = DeductValue

    @property
    def RemainValue(self):
        """抵扣余量
        :rtype: float
        """
        return self._RemainValue

    @RemainValue.setter
    def RemainValue(self, RemainValue):
        self._RemainValue = RemainValue

    @property
    def SdkAppId(self):
        """sdkAppId
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AttrStr(self):
        """其他信息
        :rtype: list of JsonObject
        """
        return self._AttrStr

    @AttrStr.setter
    def AttrStr(self, AttrStr):
        self._AttrStr = AttrStr

    @property
    def SheetName(self):
        """用量模板名称
        :rtype: list of str
        """
        return self._SheetName

    @SheetName.setter
    def SheetName(self, SheetName):
        self._SheetName = SheetName


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._Uin = params.get("Uin")
        self._DosageType = params.get("DosageType")
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._BillingItemCode = params.get("BillingItemCode")
        self._SubBillingItemCode = params.get("SubBillingItemCode")
        self._ProductCodeName = params.get("ProductCodeName")
        self._SubProductCodeName = params.get("SubProductCodeName")
        self._BillingItemCodeName = params.get("BillingItemCodeName")
        self._SubBillingItemCodeName = params.get("SubBillingItemCodeName")
        self._DosageUnit = params.get("DosageUnit")
        self._DosageBeginTime = params.get("DosageBeginTime")
        self._DosageEndTime = params.get("DosageEndTime")
        self._DosageValue = params.get("DosageValue")
        self._DeductValue = params.get("DeductValue")
        self._RemainValue = params.get("RemainValue")
        self._SdkAppId = params.get("SdkAppId")
        if params.get("AttrStr") is not None:
            self._AttrStr = []
            for item in params.get("AttrStr"):
                obj = JsonObject()
                obj._deserialize(item)
                self._AttrStr.append(obj)
        self._SheetName = params.get("SheetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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

仅支持以上产品
        :type ProductCode: str
        :param _Domain: 查询域名 例如 www.qq.com
非CDN业务查询时传入空字符串，返回的值为空
        :type Domain: str
        :param _InstanceID: 1、如果为空，则返回EIP或CLB所有实例的明细；
2、如果传入实例名，则返回该实例明细
        :type InstanceID: str
        :param _PayerUin: 支付者的账号 ID（账号 ID 是用户在腾讯云的唯一账号标识），默认查询本账号账单，如集团管理账号需查询成员账号自付的账单，该字段需入参成员账号UIN
        :type PayerUin: str
        """
        self._StartDate = None
        self._EndDate = None
        self._ProductCode = None
        self._Domain = None
        self._InstanceID = None
        self._PayerUin = None

    @property
    def StartDate(self):
        """查询账单开始日期，如 2019-01-01
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """查询账单结束日期，如 2019-01-01， 时间跨度不超过7天
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def ProductCode(self):
        """互动直播：
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

仅支持以上产品
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def Domain(self):
        """查询域名 例如 www.qq.com
非CDN业务查询时传入空字符串，返回的值为空
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def InstanceID(self):
        """1、如果为空，则返回EIP或CLB所有实例的明细；
2、如果传入实例名，则返回该实例明细
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def PayerUin(self):
        """支付者的账号 ID（账号 ID 是用户在腾讯云的唯一账号标识），默认查询本账号账单，如集团管理账号需查询成员账号自付的账单，该字段需入参成员账号UIN
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._ProductCode = params.get("ProductCode")
        self._Domain = params.get("Domain")
        self._InstanceID = params.get("InstanceID")
        self._PayerUin = params.get("PayerUin")
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
        :type Unit: str
        :param _DetailSets: 用量数组
        :type DetailSets: list of DetailSet
        :param _RetCode: 错误码
        :type RetCode: int
        :param _RetMsg: 错误信息
        :type RetMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Unit = None
        self._DetailSets = None
        self._RetCode = None
        self._RetMsg = None
        self._RequestId = None

    @property
    def Unit(self):
        """计量单位
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def DetailSets(self):
        """用量数组
        :rtype: list of DetailSet
        """
        return self._DetailSets

    @DetailSets.setter
    def DetailSets(self, DetailSets):
        self._DetailSets = DetailSets

    @property
    def RetCode(self):
        """错误码
        :rtype: int
        """
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def RetMsg(self):
        """错误信息
        :rtype: str
        """
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

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


class DescribeDosageDetailListRequest(AbstractModel):
    """DescribeDosageDetailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 用量起始时间，如：2023-02-01
        :type StartTime: str
        :param _EndTime: 用量截止时间，如：2023-02-28
        :type EndTime: str
        :param _ProductCode: 产品编码，已支持查询的产品如下：
p_ccc（云联络中心）
p_rav（实时音视频）
p_pstn（号码保护）
p_smh（智能媒资托管）
p_coding_devops（CODING DevOps）
p_dsa（全球IP应用加速）
        :type ProductCode: str
        :param _Offset: 数据偏移量（从0开始）
        :type Offset: int
        :param _Limit: 单次数据量（最大3000）
        :type Limit: int
        :param _DosageType: 用量统计类型：用量明细的数据统计汇总周期类型，包括minute-按5分钟汇总、hour-按小时汇总、day-按天汇总、month-按月汇总、comm-其他，默认查询所有类型明细，目前各产品已支持的统计类型如下：
p_ccc（云联络中心）：comm、day
p_rav（实时音视频）：minute、day
p_pstn（号码保护）：comm
p_smh（智能媒资托管）：day
p_coding_devops（CODING DevOps）：comm、day
p_dsa（全球IP应用加速）：minute
        :type DosageType: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ProductCode = None
        self._Offset = None
        self._Limit = None
        self._DosageType = None

    @property
    def StartTime(self):
        """用量起始时间，如：2023-02-01
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """用量截止时间，如：2023-02-28
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ProductCode(self):
        """产品编码，已支持查询的产品如下：
p_ccc（云联络中心）
p_rav（实时音视频）
p_pstn（号码保护）
p_smh（智能媒资托管）
p_coding_devops（CODING DevOps）
p_dsa（全球IP应用加速）
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def Offset(self):
        """数据偏移量（从0开始）
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """单次数据量（最大3000）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DosageType(self):
        """用量统计类型：用量明细的数据统计汇总周期类型，包括minute-按5分钟汇总、hour-按小时汇总、day-按天汇总、month-按月汇总、comm-其他，默认查询所有类型明细，目前各产品已支持的统计类型如下：
p_ccc（云联络中心）：comm、day
p_rav（实时音视频）：minute、day
p_pstn（号码保护）：comm
p_smh（智能媒资托管）：day
p_coding_devops（CODING DevOps）：comm、day
p_dsa（全球IP应用加速）：minute
        :rtype: str
        """
        return self._DosageType

    @DosageType.setter
    def DosageType(self, DosageType):
        self._DosageType = DosageType


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ProductCode = params.get("ProductCode")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DosageType = params.get("DosageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDosageDetailListResponse(AbstractModel):
    """DescribeDosageDetailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Record: 用量明细集合
        :type Record: list of DescribeDosageDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Record = None
        self._RequestId = None

    @property
    def Record(self):
        """用量明细集合
        :rtype: list of DescribeDosageDetail
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

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
        if params.get("Record") is not None:
            self._Record = []
            for item in params.get("Record"):
                obj = DescribeDosageDetail()
                obj._deserialize(item)
                self._Record.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGatherResourceRequest(AbstractModel):
    """DescribeGatherResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量，最大值为1000
        :type Limit: int
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :type Offset: int
        :param _Month: 账单月份，格式为2024-02，不传默认当前月
        :type Month: str
        :param _TreeNodeUniqKey: 分账单元唯一标识，用作筛选
        :type TreeNodeUniqKey: str
        :param _GatherType: 资源目录类别，枚举值如下：
all - 全部 
none - 未归集
        :type GatherType: str
        :param _Sort: 排序字段，枚举值如下：
realCost  - 折后总价
cashPayAmount - 现金金额
voucherPayAmount - 代金券金额
incentivePayAmount  - 赠送金金额
transferPayAmount -分成金金额
        :type Sort: str
        :param _SortType: 排序类型，枚举值如下：
asc - 升序
desc - 降序
        :type SortType: str
        :param _BusinessCodes: 产品编码，用作筛选
        :type BusinessCodes: list of str
        :param _ProductCodes: 子产品编码，用作筛选
        :type ProductCodes: list of str
        :param _ItemCodes: 组件名称编码，用作筛选
        :type ItemCodes: list of str
        :param _RegionIds: 地域ID，用作筛选
        :type RegionIds: list of int non-negative
        :param _InstanceTypes: 实例类型编码，用作筛选
        :type InstanceTypes: list of str
        :param _PayModes: 计费模式编码，用作筛选
        :type PayModes: list of str
        :param _OperateUins: 操作者UIN，用作筛选
        :type OperateUins: list of str
        :param _OwnerUins: 使用者UIN，用作筛选
        :type OwnerUins: list of str
        :param _SearchKey: 模糊搜索：支持标签、资源id、资源别名
        :type SearchKey: str
        :param _Tag: 标签，用作筛选
        :type Tag: list of str
        :param _ProjectIds: 项目ID，用作筛选
        :type ProjectIds: list of str
        :param _ActionTypes: 交易类型编码，用作筛选
        :type ActionTypes: list of str
        """
        self._Limit = None
        self._Offset = None
        self._Month = None
        self._TreeNodeUniqKey = None
        self._GatherType = None
        self._Sort = None
        self._SortType = None
        self._BusinessCodes = None
        self._ProductCodes = None
        self._ItemCodes = None
        self._RegionIds = None
        self._InstanceTypes = None
        self._PayModes = None
        self._OperateUins = None
        self._OwnerUins = None
        self._SearchKey = None
        self._Tag = None
        self._ProjectIds = None
        self._ActionTypes = None

    @property
    def Limit(self):
        """数量，最大值为1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Month(self):
        """账单月份，格式为2024-02，不传默认当前月
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TreeNodeUniqKey(self):
        """分账单元唯一标识，用作筛选
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def GatherType(self):
        """资源目录类别，枚举值如下：
all - 全部 
none - 未归集
        :rtype: str
        """
        return self._GatherType

    @GatherType.setter
    def GatherType(self, GatherType):
        self._GatherType = GatherType

    @property
    def Sort(self):
        """排序字段，枚举值如下：
realCost  - 折后总价
cashPayAmount - 现金金额
voucherPayAmount - 代金券金额
incentivePayAmount  - 赠送金金额
transferPayAmount -分成金金额
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SortType(self):
        """排序类型，枚举值如下：
asc - 升序
desc - 降序
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def BusinessCodes(self):
        """产品编码，用作筛选
        :rtype: list of str
        """
        return self._BusinessCodes

    @BusinessCodes.setter
    def BusinessCodes(self, BusinessCodes):
        self._BusinessCodes = BusinessCodes

    @property
    def ProductCodes(self):
        """子产品编码，用作筛选
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes

    @property
    def ItemCodes(self):
        """组件名称编码，用作筛选
        :rtype: list of str
        """
        return self._ItemCodes

    @ItemCodes.setter
    def ItemCodes(self, ItemCodes):
        self._ItemCodes = ItemCodes

    @property
    def RegionIds(self):
        """地域ID，用作筛选
        :rtype: list of int non-negative
        """
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def InstanceTypes(self):
        """实例类型编码，用作筛选
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def PayModes(self):
        """计费模式编码，用作筛选
        :rtype: list of str
        """
        return self._PayModes

    @PayModes.setter
    def PayModes(self, PayModes):
        self._PayModes = PayModes

    @property
    def OperateUins(self):
        """操作者UIN，用作筛选
        :rtype: list of str
        """
        return self._OperateUins

    @OperateUins.setter
    def OperateUins(self, OperateUins):
        self._OperateUins = OperateUins

    @property
    def OwnerUins(self):
        """使用者UIN，用作筛选
        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def SearchKey(self):
        """模糊搜索：支持标签、资源id、资源别名
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def Tag(self):
        """标签，用作筛选
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ProjectIds(self):
        """项目ID，用作筛选
        :rtype: list of str
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def ActionTypes(self):
        """交易类型编码，用作筛选
        :rtype: list of str
        """
        return self._ActionTypes

    @ActionTypes.setter
    def ActionTypes(self, ActionTypes):
        self._ActionTypes = ActionTypes


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Month = params.get("Month")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._GatherType = params.get("GatherType")
        self._Sort = params.get("Sort")
        self._SortType = params.get("SortType")
        self._BusinessCodes = params.get("BusinessCodes")
        self._ProductCodes = params.get("ProductCodes")
        self._ItemCodes = params.get("ItemCodes")
        self._RegionIds = params.get("RegionIds")
        self._InstanceTypes = params.get("InstanceTypes")
        self._PayModes = params.get("PayModes")
        self._OperateUins = params.get("OperateUins")
        self._OwnerUins = params.get("OwnerUins")
        self._SearchKey = params.get("SearchKey")
        self._Tag = params.get("Tag")
        self._ProjectIds = params.get("ProjectIds")
        self._ActionTypes = params.get("ActionTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatherResourceResponse(AbstractModel):
    """DescribeGatherResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordNum: 总条数
        :type RecordNum: int
        :param _GatherResourceSummary: 资源归集汇总
注意：此字段可能返回 null，表示取不到有效值。
        :type GatherResourceSummary: list of GatherResourceSummary
        :param _LastUpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordNum = None
        self._GatherResourceSummary = None
        self._LastUpdateTime = None
        self._RequestId = None

    @property
    def RecordNum(self):
        """总条数
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def GatherResourceSummary(self):
        """资源归集汇总
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of GatherResourceSummary
        """
        return self._GatherResourceSummary

    @GatherResourceSummary.setter
    def GatherResourceSummary(self, GatherResourceSummary):
        self._GatherResourceSummary = GatherResourceSummary

    @property
    def LastUpdateTime(self):
        """数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

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
        self._RecordNum = params.get("RecordNum")
        if params.get("GatherResourceSummary") is not None:
            self._GatherResourceSummary = []
            for item in params.get("GatherResourceSummary"):
                obj = GatherResourceSummary()
                obj._deserialize(item)
                self._GatherResourceSummary.append(obj)
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._RequestId = params.get("RequestId")


class DescribeSavingPlanResourceInfoRequest(AbstractModel):
    """DescribeSavingPlanResourceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量，最大值为100
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _CreateStartDate: 购买开始时间，格式yyyy-MM-dd
        :type CreateStartDate: str
        :param _CreateEndDate: 购买结束时间，格式yyyy-MM-dd
        :type CreateEndDate: str
        """
        self._Limit = None
        self._Offset = None
        self._CreateStartDate = None
        self._CreateEndDate = None

    @property
    def Limit(self):
        """数量，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CreateStartDate(self):
        """购买开始时间，格式yyyy-MM-dd
        :rtype: str
        """
        return self._CreateStartDate

    @CreateStartDate.setter
    def CreateStartDate(self, CreateStartDate):
        self._CreateStartDate = CreateStartDate

    @property
    def CreateEndDate(self):
        """购买结束时间，格式yyyy-MM-dd
        :rtype: str
        """
        return self._CreateEndDate

    @CreateEndDate.setter
    def CreateEndDate(self, CreateEndDate):
        self._CreateEndDate = CreateEndDate


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._CreateStartDate = params.get("CreateStartDate")
        self._CreateEndDate = params.get("CreateEndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSavingPlanResourceInfoResponse(AbstractModel):
    """DescribeSavingPlanResourceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 记录数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._RequestId = None

    @property
    def Total(self):
        """记录数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeTagListRequest(AbstractModel):
    """DescribeTagList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量，最大值为1000
        :type Limit: int
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :type Offset: int
        :param _TagKey: 分账标签键，用作模糊搜索
        :type TagKey: str
        :param _Status: 标签类型，枚举值：0普通标签，1分账标签，用作筛选，不传获取全部标签键
        :type Status: int
        :param _OrderType: 排序方式，枚举值：asc排升序，desc排降序
        :type OrderType: str
        """
        self._Limit = None
        self._Offset = None
        self._TagKey = None
        self._Status = None
        self._OrderType = None

    @property
    def Limit(self):
        """数量，最大值为1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，依次类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TagKey(self):
        """分账标签键，用作模糊搜索
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Status(self):
        """标签类型，枚举值：0普通标签，1分账标签，用作筛选，不传获取全部标签键
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderType(self):
        """排序方式，枚举值：asc排升序，desc排降序
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._TagKey = params.get("TagKey")
        self._Status = params.get("Status")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagListResponse(AbstractModel):
    """DescribeTagList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordNum: 总记录数
        :type RecordNum: int
        :param _Data: 标签信息
        :type Data: list of TagDataInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordNum = None
        self._Data = None
        self._RequestId = None

    @property
    def RecordNum(self):
        """总记录数
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def Data(self):
        """标签信息
        :rtype: list of TagDataInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._RecordNum = params.get("RecordNum")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TagDataInfo()
                obj._deserialize(item)
                self._Data.append(obj)
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
        :param _VoucherMainType: 代金券主类型 has_price 为有价现金券 no_price 为无价代金券
        :type VoucherMainType: str
        :param _VoucherSubType: 代金券副类型 discount 为折扣券 deduct 为抵扣券
        :type VoucherSubType: str
        :param _StartTimeFrom: 券有效时间开始时间
        :type StartTimeFrom: str
        :param _StartTimeTo: 券有效时间结束时间
        :type StartTimeTo: str
        :param _EndTimeFrom: 券失效时间开始时间
        :type EndTimeFrom: str
        :param _EndTimeTo: 券失效时间结束时间
        :type EndTimeTo: str
        :param _CreateTimeFrom: 发券时间开始时间
        :type CreateTimeFrom: str
        :param _CreateTimeTo: 发券时间结束时间
        :type CreateTimeTo: str
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
        self._VoucherMainType = None
        self._VoucherSubType = None
        self._StartTimeFrom = None
        self._StartTimeTo = None
        self._EndTimeFrom = None
        self._EndTimeTo = None
        self._CreateTimeFrom = None
        self._CreateTimeTo = None

    @property
    def Limit(self):
        """一页多少条数据，默认是20条，最大不超过1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """第多少页，默认是1
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        """券状态：待使用：unUsed，已使用： used，已发货：delivered，已作废： cancel，已过期：overdue
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VoucherId(self):
        """代金券id
        :rtype: str
        """
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def CodeId(self):
        """代金券订单id
        :rtype: str
        """
        return self._CodeId

    @CodeId.setter
    def CodeId(self, CodeId):
        self._CodeId = CodeId

    @property
    def ProductCode(self):
        """商品码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ActivityId(self):
        """活动id
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def VoucherName(self):
        """代金券名称
        :rtype: str
        """
        return self._VoucherName

    @VoucherName.setter
    def VoucherName(self, VoucherName):
        self._VoucherName = VoucherName

    @property
    def TimeFrom(self):
        """发放开始时间,例：2021-01-01
        :rtype: str
        """
        return self._TimeFrom

    @TimeFrom.setter
    def TimeFrom(self, TimeFrom):
        self._TimeFrom = TimeFrom

    @property
    def TimeTo(self):
        """发放结束时间，例：2021-01-01
        :rtype: str
        """
        return self._TimeTo

    @TimeTo.setter
    def TimeTo(self, TimeTo):
        self._TimeTo = TimeTo

    @property
    def SortField(self):
        """指定排序字段：BeginTime开始时间、EndTime到期时间、CreateTime创建时间
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortOrder(self):
        """指定升序降序：desc、asc
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder

    @property
    def PayMode(self):
        """付费模式，postPay后付费/prePay预付费/riPay预留实例/""或者"*"表示全部模式，如果payMode为""或"*"，那么productCode与subProductCode必须传空
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayScene(self):
        """付费场景PayMode=postPay时：spotpay-竞价实例,"settle account"-普通后付费PayMode=prePay时：purchase-包年包月新购，renew-包年包月续费（自动续费），modify-包年包月配置变更(变配）PayMode=riPay时：oneOffFee-预留实例预付，hourlyFee-预留实例每小时扣费，*-支持全部付费场景
        :rtype: str
        """
        return self._PayScene

    @PayScene.setter
    def PayScene(self, PayScene):
        self._PayScene = PayScene

    @property
    def Operator(self):
        """操作人，默认就是用户uin
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def VoucherMainType(self):
        """代金券主类型 has_price 为有价现金券 no_price 为无价代金券
        :rtype: str
        """
        return self._VoucherMainType

    @VoucherMainType.setter
    def VoucherMainType(self, VoucherMainType):
        self._VoucherMainType = VoucherMainType

    @property
    def VoucherSubType(self):
        """代金券副类型 discount 为折扣券 deduct 为抵扣券
        :rtype: str
        """
        return self._VoucherSubType

    @VoucherSubType.setter
    def VoucherSubType(self, VoucherSubType):
        self._VoucherSubType = VoucherSubType

    @property
    def StartTimeFrom(self):
        """券有效时间开始时间
        :rtype: str
        """
        return self._StartTimeFrom

    @StartTimeFrom.setter
    def StartTimeFrom(self, StartTimeFrom):
        self._StartTimeFrom = StartTimeFrom

    @property
    def StartTimeTo(self):
        """券有效时间结束时间
        :rtype: str
        """
        return self._StartTimeTo

    @StartTimeTo.setter
    def StartTimeTo(self, StartTimeTo):
        self._StartTimeTo = StartTimeTo

    @property
    def EndTimeFrom(self):
        """券失效时间开始时间
        :rtype: str
        """
        return self._EndTimeFrom

    @EndTimeFrom.setter
    def EndTimeFrom(self, EndTimeFrom):
        self._EndTimeFrom = EndTimeFrom

    @property
    def EndTimeTo(self):
        """券失效时间结束时间
        :rtype: str
        """
        return self._EndTimeTo

    @EndTimeTo.setter
    def EndTimeTo(self, EndTimeTo):
        self._EndTimeTo = EndTimeTo

    @property
    def CreateTimeFrom(self):
        """发券时间开始时间
        :rtype: str
        """
        return self._CreateTimeFrom

    @CreateTimeFrom.setter
    def CreateTimeFrom(self, CreateTimeFrom):
        self._CreateTimeFrom = CreateTimeFrom

    @property
    def CreateTimeTo(self):
        """发券时间结束时间
        :rtype: str
        """
        return self._CreateTimeTo

    @CreateTimeTo.setter
    def CreateTimeTo(self, CreateTimeTo):
        self._CreateTimeTo = CreateTimeTo


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
        self._VoucherMainType = params.get("VoucherMainType")
        self._VoucherSubType = params.get("VoucherSubType")
        self._StartTimeFrom = params.get("StartTimeFrom")
        self._StartTimeTo = params.get("StartTimeTo")
        self._EndTimeFrom = params.get("EndTimeFrom")
        self._EndTimeTo = params.get("EndTimeTo")
        self._CreateTimeFrom = params.get("CreateTimeFrom")
        self._CreateTimeTo = params.get("CreateTimeTo")
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
        :type VoucherInfos: list of VoucherInfos
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TotalBalance = None
        self._VoucherInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """券总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalBalance(self):
        """总余额（微分）
        :rtype: int
        """
        return self._TotalBalance

    @TotalBalance.setter
    def TotalBalance(self, TotalBalance):
        self._TotalBalance = TotalBalance

    @property
    def VoucherInfos(self):
        """代金券相关信息
        :rtype: list of VoucherInfos
        """
        return self._VoucherInfos

    @VoucherInfos.setter
    def VoucherInfos(self, VoucherInfos):
        self._VoucherInfos = VoucherInfos

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
        """一页多少条数据，默认是20条，最大不超过1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """第多少页，默认是1
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def VoucherId(self):
        """代金券id
        :rtype: str
        """
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def Operator(self):
        """操作人，默认就是用户uin
        :rtype: str
        """
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
        :type UsageRecords: list of UsageRecords
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TotalUsedAmount = None
        self._UsageRecords = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """券总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalUsedAmount(self):
        """总已用金额（微分）
        :rtype: int
        """
        return self._TotalUsedAmount

    @TotalUsedAmount.setter
    def TotalUsedAmount(self, TotalUsedAmount):
        self._TotalUsedAmount = TotalUsedAmount

    @property
    def UsageRecords(self):
        """代金券使用记录细节
        :rtype: list of UsageRecords
        """
        return self._UsageRecords

    @UsageRecords.setter
    def UsageRecords(self, UsageRecords):
        self._UsageRecords = UsageRecords

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
        """时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        """值
        :rtype: str
        """
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
        :type InstanceID: str
        """
        self._Domain = None
        self._DetailPoints = None
        self._InstanceID = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DetailPoints(self):
        """使用数据明细
        :rtype: list of DetailPoint
        """
        return self._DetailPoints

    @DetailPoints.setter
    def DetailPoints(self, DetailPoints):
        self._DetailPoints = DetailPoints

    @property
    def InstanceID(self):
        """实例ID
        :rtype: str
        """
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
        


class DistributionBillDetail(AbstractModel):
    """经销账单明细数据对象

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
        :param _OwnerUin: 使用者UIN：实际使用资源的账号 ID
        :type OwnerUin: str
        :param _OperateUin: 操作者UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的 ID 或者角色 ID ）
        :type OperateUin: str
        :param _Tags: 标签信息
        :type Tags: list of BillTagInfo
        :param _BusinessCode: 产品编码
        :type BusinessCode: str
        :param _ProductCode: 子产品编码
        :type ProductCode: str
        :param _ActionType: 交易类型编码
        :type ActionType: str
        :param _RegionId: 地域ID
        :type RegionId: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _PriceInfo: 价格属性：该组件除单价、时长外的其他影响折扣定价的属性信息
        :type PriceInfo: list of str
        :param _AssociatedOrder: 关联交易单据ID：和本笔交易关联单据 ID，如，冲销订单，记录原订单、重结订单，退费单记录对应的原购买订单号
        :type AssociatedOrder: :class:`tencentcloud.billing.v20180709.models.BillDetailAssociatedOrder`
        :param _Formula: 计算说明：特殊交易类型计费结算的详细计算说明，如退费及变配
        :type Formula: str
        :param _FormulaUrl: 计费规则：各产品详细的计费规则官网说明链接
        :type FormulaUrl: str
        :param _BillMonth: 账单归属月
        :type BillMonth: str
        :param _BillDay: 账单归属日
        :type BillDay: str
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
        self._OwnerUin = None
        self._OperateUin = None
        self._Tags = None
        self._BusinessCode = None
        self._ProductCode = None
        self._ActionType = None
        self._RegionId = None
        self._ProjectId = None
        self._PriceInfo = None
        self._AssociatedOrder = None
        self._Formula = None
        self._FormulaUrl = None
        self._BillMonth = None
        self._BillDay = None

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品，例如：云服务器 CVM
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ProductCodeName(self):
        """子产品名称：用户采购的具体产品细分类型，例如：云服务器 CVM-标准型 S1
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayModeName(self):
        """计费模式：资源的计费模式，区分为包年包月和按量计费
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ProjectName(self):
        """项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RegionName(self):
        """地域：资源所属地域，如华南地区（广州）
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        """可用区：资源所属可用区，如广州三区
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ResourceId(self):
        """资源 ID：账单中出账对象 ID，不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """资源别名：用户在控制台为资源设置的名称，如果未设置，则默认为空
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ActionTypeName(self):
        """交易类型，如包年包月新购、包年包月续费、按量计费扣费等类型
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def OrderId(self):
        """订单ID：包年包月计费模式下订购的订单号
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BillId(self):
        """交易ID：结算扣费单号
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def PayTime(self):
        """扣费时间：结算扣费时间
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def FeeBeginTime(self):
        """开始使用时间：产品服务开始使用时间
        :rtype: str
        """
        return self._FeeBeginTime

    @FeeBeginTime.setter
    def FeeBeginTime(self, FeeBeginTime):
        self._FeeBeginTime = FeeBeginTime

    @property
    def FeeEndTime(self):
        """结束使用时间：产品服务结束使用时间
        :rtype: str
        """
        return self._FeeEndTime

    @FeeEndTime.setter
    def FeeEndTime(self, FeeEndTime):
        self._FeeEndTime = FeeEndTime

    @property
    def ComponentSet(self):
        """组件列表
        :rtype: list of BillDetailComponent
        """
        return self._ComponentSet

    @ComponentSet.setter
    def ComponentSet(self, ComponentSet):
        self._ComponentSet = ComponentSet

    @property
    def OwnerUin(self):
        """使用者UIN：实际使用资源的账号 ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        """操作者UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的 ID 或者角色 ID ）
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def Tags(self):
        """标签信息
        :rtype: list of BillTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def BusinessCode(self):
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def ProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ActionType(self):
        """交易类型编码
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def RegionId(self):
        """地域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PriceInfo(self):
        """价格属性：该组件除单价、时长外的其他影响折扣定价的属性信息
        :rtype: list of str
        """
        return self._PriceInfo

    @PriceInfo.setter
    def PriceInfo(self, PriceInfo):
        self._PriceInfo = PriceInfo

    @property
    def AssociatedOrder(self):
        """关联交易单据ID：和本笔交易关联单据 ID，如，冲销订单，记录原订单、重结订单，退费单记录对应的原购买订单号
        :rtype: :class:`tencentcloud.billing.v20180709.models.BillDetailAssociatedOrder`
        """
        return self._AssociatedOrder

    @AssociatedOrder.setter
    def AssociatedOrder(self, AssociatedOrder):
        self._AssociatedOrder = AssociatedOrder

    @property
    def Formula(self):
        """计算说明：特殊交易类型计费结算的详细计算说明，如退费及变配
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def FormulaUrl(self):
        """计费规则：各产品详细的计费规则官网说明链接
        :rtype: str
        """
        return self._FormulaUrl

    @FormulaUrl.setter
    def FormulaUrl(self, FormulaUrl):
        self._FormulaUrl = FormulaUrl

    @property
    def BillMonth(self):
        """账单归属月
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def BillDay(self):
        """账单归属日
        :rtype: str
        """
        return self._BillDay

    @BillDay.setter
    def BillDay(self, BillDay):
        self._BillDay = BillDay


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
        if params.get("AssociatedOrder") is not None:
            self._AssociatedOrder = BillDetailAssociatedOrder()
            self._AssociatedOrder._deserialize(params.get("AssociatedOrder"))
        self._Formula = params.get("Formula")
        self._FormulaUrl = params.get("FormulaUrl")
        self._BillMonth = params.get("BillMonth")
        self._BillDay = params.get("BillDay")
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
        """不适用商品名称
        :rtype: str
        """
        return self._GoodsName

    @GoodsName.setter
    def GoodsName(self, GoodsName):
        self._GoodsName = GoodsName

    @property
    def PayMode(self):
        """postPay后付费/prePay预付费/riPay预留实例/空字符串或者"*"表示全部模式。
        :rtype: str
        """
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
        


class GatherResourceSummary(AbstractModel):
    """资源归集汇总

    """

    def __init__(self):
        r"""
        :param _PayerUin: 支付者 UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :type PayerUin: str
        :param _OwnerUin: 使用者 UIN：实际使用资源的账号 ID
        :type OwnerUin: str
        :param _OperateUin: 操作者 UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的ID或者角色 ID）
        :type OperateUin: str
        :param _InstanceType: 实例类型编码
        :type InstanceType: str
        :param _InstanceTypeName: 实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。常规实例默认展示“-”
        :type InstanceTypeName: str
        :param _ResourceId: 资源ID：不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID； 若该产品被分拆，则展示产品分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
        :type ResourceId: str
        :param _ResourceName: 实例名称：用户在控制台为资源设置的名称，如未设置默认为空；若该产品被分拆，则展示分拆产品分拆后的分拆项资源别名
        :type ResourceName: str
        :param _TreeNodeUniqKey: 分账单元唯一标识
        :type TreeNodeUniqKey: str
        :param _TreeNodeUniqKeyName: 分账单元名称
        :type TreeNodeUniqKeyName: str
        :param _RuleId: 资源命中公摊规则ID
        :type RuleId: int
        :param _RuleName: 资源命中公摊规则名称
        :type RuleName: str
        :param _BusinessCode: 产品编码
        :type BusinessCode: str
        :param _BusinessCodeName: 产品名称：用户所采购的各类云产品
        :type BusinessCodeName: str
        :param _ItemCode: 组件名称编码
        :type ItemCode: str
        :param _ItemCodeName: 组件名称：用户购买的产品或服务，所包含的具体组件
        :type ItemCodeName: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _RegionName: 地域名称：资源所属地域
        :type RegionName: str
        :param _Tag: 分账标签：资源绑定的标签
        :type Tag: list of BillTag
        :param _RealTotalCost: 优惠后总价：优惠后总价 =（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :type RealTotalCost: str
        :param _CashPayAmount: 现金账户支出(元)：通过现金账户支付的金额
        :type CashPayAmount: str
        :param _VoucherPayAmount: 代金券支出(元)：使用各类优惠券（如代金券、现金券等）支付的金额
        :type VoucherPayAmount: str
        :param _IncentivePayAmount: 赠送账户支出(元)：使用赠送金支付的金额
        :type IncentivePayAmount: str
        :param _TransferPayAmount: 分成账户支出(元)：通过分成金账户支付的金额
        :type TransferPayAmount: str
        :param _AllocationType: 费用归集类型：费用来源类型，分摊、归集、未分配
0 - 分摊
1 - 归集
-1 - 未分配
        :type AllocationType: int
        :param _BelongTreeNodeUniqKey: 当前归属单元信息
        :type BelongTreeNodeUniqKey: :class:`tencentcloud.billing.v20180709.models.AllocationTreeNode`
        :param _BelongRule: 当前资源命中公摊规则信息
        :type BelongRule: :class:`tencentcloud.billing.v20180709.models.AllocationRule`
        :param _OtherTreeNodeUniqKeys: 其它归属单元信息
        :type OtherTreeNodeUniqKeys: list of AllocationTreeNode
        :param _OtherRules: 其他命中规则信息
        :type OtherRules: list of AllocationRule
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _ProjectName: 项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :type ProjectName: str
        :param _ProductCode: 子产品编码
        :type ProductCode: str
        :param _ProductCodeName: 子产品名称：用户采购的具体产品细分类型
        :type ProductCodeName: str
        :param _PayMode: 计费模式编码
        :type PayMode: str
        :param _PayModeName: 计费模式：资源的计费模式，区分为包年包月和按量计费
        :type PayModeName: str
        :param _ActionType: 交易类型编码
        :type ActionType: str
        :param _ActionTypeName: 交易类型：明细交易类型
        :type ActionTypeName: str
        :param _SplitItemId: 分拆项 ID：涉及分拆产品的分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type SplitItemId: str
        :param _SplitItemName: 分拆项名称：涉及分拆产品的分拆后的分拆项
注意：此字段可能返回 null，表示取不到有效值。
        :type SplitItemName: str
        """
        self._PayerUin = None
        self._OwnerUin = None
        self._OperateUin = None
        self._InstanceType = None
        self._InstanceTypeName = None
        self._ResourceId = None
        self._ResourceName = None
        self._TreeNodeUniqKey = None
        self._TreeNodeUniqKeyName = None
        self._RuleId = None
        self._RuleName = None
        self._BusinessCode = None
        self._BusinessCodeName = None
        self._ItemCode = None
        self._ItemCodeName = None
        self._RegionId = None
        self._RegionName = None
        self._Tag = None
        self._RealTotalCost = None
        self._CashPayAmount = None
        self._VoucherPayAmount = None
        self._IncentivePayAmount = None
        self._TransferPayAmount = None
        self._AllocationType = None
        self._BelongTreeNodeUniqKey = None
        self._BelongRule = None
        self._OtherTreeNodeUniqKeys = None
        self._OtherRules = None
        self._ProjectId = None
        self._ProjectName = None
        self._ProductCode = None
        self._ProductCodeName = None
        self._PayMode = None
        self._PayModeName = None
        self._ActionType = None
        self._ActionTypeName = None
        self._SplitItemId = None
        self._SplitItemName = None

    @property
    def PayerUin(self):
        """支付者 UIN：支付者的账号 ID，账号 ID 是用户在腾讯云的唯一账号标识
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def OwnerUin(self):
        """使用者 UIN：实际使用资源的账号 ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OperateUin(self):
        """操作者 UIN：操作者账号 ID（预付费资源下单或后付费操作开通资源账号的ID或者角色 ID）
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def InstanceType(self):
        """实例类型编码
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceTypeName(self):
        """实例类型：购买的产品服务对应的实例类型，包括资源包、RI、SP、竞价实例。常规实例默认展示“-”
        :rtype: str
        """
        return self._InstanceTypeName

    @InstanceTypeName.setter
    def InstanceTypeName(self, InstanceTypeName):
        self._InstanceTypeName = InstanceTypeName

    @property
    def ResourceId(self):
        """资源ID：不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID； 若该产品被分拆，则展示产品分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """实例名称：用户在控制台为资源设置的名称，如未设置默认为空；若该产品被分拆，则展示分拆产品分拆后的分拆项资源别名
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def TreeNodeUniqKey(self):
        """分账单元唯一标识
        :rtype: str
        """
        return self._TreeNodeUniqKey

    @TreeNodeUniqKey.setter
    def TreeNodeUniqKey(self, TreeNodeUniqKey):
        self._TreeNodeUniqKey = TreeNodeUniqKey

    @property
    def TreeNodeUniqKeyName(self):
        """分账单元名称
        :rtype: str
        """
        return self._TreeNodeUniqKeyName

    @TreeNodeUniqKeyName.setter
    def TreeNodeUniqKeyName(self, TreeNodeUniqKeyName):
        self._TreeNodeUniqKeyName = TreeNodeUniqKeyName

    @property
    def RuleId(self):
        """资源命中公摊规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """资源命中公摊规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def BusinessCode(self):
        """产品编码
        :rtype: str
        """
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessCodeName(self):
        """产品名称：用户所采购的各类云产品
        :rtype: str
        """
        return self._BusinessCodeName

    @BusinessCodeName.setter
    def BusinessCodeName(self, BusinessCodeName):
        self._BusinessCodeName = BusinessCodeName

    @property
    def ItemCode(self):
        """组件名称编码
        :rtype: str
        """
        return self._ItemCode

    @ItemCode.setter
    def ItemCode(self, ItemCode):
        self._ItemCode = ItemCode

    @property
    def ItemCodeName(self):
        """组件名称：用户购买的产品或服务，所包含的具体组件
        :rtype: str
        """
        return self._ItemCodeName

    @ItemCodeName.setter
    def ItemCodeName(self, ItemCodeName):
        self._ItemCodeName = ItemCodeName

    @property
    def RegionId(self):
        """地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称：资源所属地域
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Tag(self):
        """分账标签：资源绑定的标签
        :rtype: list of BillTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def RealTotalCost(self):
        """优惠后总价：优惠后总价 =（原价 - 预留实例抵扣原价 - 节省计划抵扣原价）* 折扣率
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出(元)：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def VoucherPayAmount(self):
        """代金券支出(元)：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出(元)：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def TransferPayAmount(self):
        """分成账户支出(元)：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def AllocationType(self):
        """费用归集类型：费用来源类型，分摊、归集、未分配
0 - 分摊
1 - 归集
-1 - 未分配
        :rtype: int
        """
        return self._AllocationType

    @AllocationType.setter
    def AllocationType(self, AllocationType):
        self._AllocationType = AllocationType

    @property
    def BelongTreeNodeUniqKey(self):
        """当前归属单元信息
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationTreeNode`
        """
        return self._BelongTreeNodeUniqKey

    @BelongTreeNodeUniqKey.setter
    def BelongTreeNodeUniqKey(self, BelongTreeNodeUniqKey):
        self._BelongTreeNodeUniqKey = BelongTreeNodeUniqKey

    @property
    def BelongRule(self):
        """当前资源命中公摊规则信息
        :rtype: :class:`tencentcloud.billing.v20180709.models.AllocationRule`
        """
        return self._BelongRule

    @BelongRule.setter
    def BelongRule(self, BelongRule):
        self._BelongRule = BelongRule

    @property
    def OtherTreeNodeUniqKeys(self):
        """其它归属单元信息
        :rtype: list of AllocationTreeNode
        """
        return self._OtherTreeNodeUniqKeys

    @OtherTreeNodeUniqKeys.setter
    def OtherTreeNodeUniqKeys(self, OtherTreeNodeUniqKeys):
        self._OtherTreeNodeUniqKeys = OtherTreeNodeUniqKeys

    @property
    def OtherRules(self):
        """其他命中规则信息
        :rtype: list of AllocationRule
        """
        return self._OtherRules

    @OtherRules.setter
    def OtherRules(self, OtherRules):
        self._OtherRules = OtherRules

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProductCode(self):
        """子产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductCodeName(self):
        """子产品名称：用户采购的具体产品细分类型
        :rtype: str
        """
        return self._ProductCodeName

    @ProductCodeName.setter
    def ProductCodeName(self, ProductCodeName):
        self._ProductCodeName = ProductCodeName

    @property
    def PayMode(self):
        """计费模式编码
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        """计费模式：资源的计费模式，区分为包年包月和按量计费
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def ActionType(self):
        """交易类型编码
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionTypeName(self):
        """交易类型：明细交易类型
        :rtype: str
        """
        return self._ActionTypeName

    @ActionTypeName.setter
    def ActionTypeName(self, ActionTypeName):
        self._ActionTypeName = ActionTypeName

    @property
    def SplitItemId(self):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        """分拆项 ID：涉及分拆产品的分拆后的分拆项 ID，如 COS 桶 ID，CDN 域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SplitItemId

    @SplitItemId.setter
    def SplitItemId(self, SplitItemId):
        warnings.warn("parameter `SplitItemId` is deprecated", DeprecationWarning) 

        self._SplitItemId = SplitItemId

    @property
    def SplitItemName(self):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        """分拆项名称：涉及分拆产品的分拆后的分拆项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SplitItemName

    @SplitItemName.setter
    def SplitItemName(self, SplitItemName):
        warnings.warn("parameter `SplitItemName` is deprecated", DeprecationWarning) 

        self._SplitItemName = SplitItemName


    def _deserialize(self, params):
        self._PayerUin = params.get("PayerUin")
        self._OwnerUin = params.get("OwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._InstanceType = params.get("InstanceType")
        self._InstanceTypeName = params.get("InstanceTypeName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._TreeNodeUniqKey = params.get("TreeNodeUniqKey")
        self._TreeNodeUniqKeyName = params.get("TreeNodeUniqKeyName")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessCodeName = params.get("BusinessCodeName")
        self._ItemCode = params.get("ItemCode")
        self._ItemCodeName = params.get("ItemCodeName")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = BillTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._RealTotalCost = params.get("RealTotalCost")
        self._CashPayAmount = params.get("CashPayAmount")
        self._VoucherPayAmount = params.get("VoucherPayAmount")
        self._IncentivePayAmount = params.get("IncentivePayAmount")
        self._TransferPayAmount = params.get("TransferPayAmount")
        self._AllocationType = params.get("AllocationType")
        if params.get("BelongTreeNodeUniqKey") is not None:
            self._BelongTreeNodeUniqKey = AllocationTreeNode()
            self._BelongTreeNodeUniqKey._deserialize(params.get("BelongTreeNodeUniqKey"))
        if params.get("BelongRule") is not None:
            self._BelongRule = AllocationRule()
            self._BelongRule._deserialize(params.get("BelongRule"))
        if params.get("OtherTreeNodeUniqKeys") is not None:
            self._OtherTreeNodeUniqKeys = []
            for item in params.get("OtherTreeNodeUniqKeys"):
                obj = AllocationTreeNode()
                obj._deserialize(item)
                self._OtherTreeNodeUniqKeys.append(obj)
        if params.get("OtherRules") is not None:
            self._OtherRules = []
            for item in params.get("OtherRules"):
                obj = AllocationRule()
                obj._deserialize(item)
                self._OtherRules.append(obj)
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProductCode = params.get("ProductCode")
        self._ProductCodeName = params.get("ProductCodeName")
        self._PayMode = params.get("PayMode")
        self._PayModeName = params.get("PayModeName")
        self._ActionType = params.get("ActionType")
        self._ActionTypeName = params.get("ActionTypeName")
        self._SplitItemId = params.get("SplitItemId")
        self._SplitItemName = params.get("SplitItemName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JsonObject(AbstractModel):
    """Json对象

    """

    def __init__(self):
        r"""
        :param _Key: key值
        :type Key: str
        :param _Value: value值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """key值
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """value值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
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
        :param _AgentPay: 0非代理，1代理商代付，3集团代理，4代理商为代客下产品级代付单，默认0
        :type AgentPay: int
        :param _CpsUin: 推荐者，用于返利
        :type CpsUin: str
        """
        self._OrderIds = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._BigDealIds = None
        self._AgentPay = None
        self._CpsUin = None

    @property
    def OrderIds(self):
        """需要支付的一个或者多个子订单号，与BigDealIds字段两者必须且仅传一个参数
        :rtype: list of str
        """
        return self._OrderIds

    @OrderIds.setter
    def OrderIds(self, OrderIds):
        self._OrderIds = OrderIds

    @property
    def AutoVoucher(self):
        """是否自动使用代金券,1:是,0否,默认0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """代金券ID列表,目前仅支持指定一张代金券
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def BigDealIds(self):
        """需要支付的一个或者多个大订单号，与OrderIds字段两者必须且仅传一个参数
        :rtype: list of str
        """
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def AgentPay(self):
        """0非代理，1代理商代付，3集团代理，4代理商为代客下产品级代付单，默认0
        :rtype: int
        """
        return self._AgentPay

    @AgentPay.setter
    def AgentPay(self, AgentPay):
        self._AgentPay = AgentPay

    @property
    def CpsUin(self):
        """推荐者，用于返利
        :rtype: str
        """
        return self._CpsUin

    @CpsUin.setter
    def CpsUin(self, CpsUin):
        self._CpsUin = CpsUin


    def _deserialize(self, params):
        self._OrderIds = params.get("OrderIds")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._BigDealIds = params.get("BigDealIds")
        self._AgentPay = params.get("AgentPay")
        self._CpsUin = params.get("CpsUin")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderIds = None
        self._ResourceIds = None
        self._BigDealIds = None
        self._RequestId = None

    @property
    def OrderIds(self):
        """此次操作支付成功的子订单号数组
        :rtype: list of str
        """
        return self._OrderIds

    @OrderIds.setter
    def OrderIds(self, OrderIds):
        self._OrderIds = OrderIds

    @property
    def ResourceIds(self):
        """此次操作支付成功的资源Id数组
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def BigDealIds(self):
        """此次操作支付成功的大订单号数组
        :rtype: list of str
        """
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

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
        """计费模式编码
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeName(self):
        """计费模式：区分为包年包月和按量计费
        :rtype: str
        """
        return self._PayModeName

    @PayModeName.setter
    def PayModeName(self, PayModeName):
        self._PayModeName = PayModeName

    @property
    def RealTotalCostRatio(self):
        """费用所占百分比，两位小数
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        """优惠后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        """原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Detail(self):
        """按交易类型汇总消费详情
        :rtype: list of ActionSummaryOverviewItem
        """
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
        """商品详情名称标识
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """商品详情
        :rtype: str
        """
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
        """项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """项目名称：资源归属的项目，用户在控制台给资源自主分配项目，未分配则是默认项目
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def RealTotalCostRatio(self):
        """费用所占百分比，两位小数
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        """优惠后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        """账单月份，格式2019-08
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        """原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :rtype: str
        """
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
        """地域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称：资源所属地域，例如华南地区（广州）
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RealTotalCostRatio(self):
        """费用所占百分比，两位小数
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        """优惠后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def BillMonth(self):
        """账单月份，格式2019-08
        :rtype: str
        """
        return self._BillMonth

    @BillMonth.setter
    def BillMonth(self, BillMonth):
        self._BillMonth = BillMonth

    @property
    def TotalCost(self):
        """原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :rtype: str
        """
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
        :type GroupKey: str
        :param _GroupValue: 账单维度值
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
        :type TransferPayAmount: str
        :param _Business: 产品汇总信息
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
        """账单维度编码
        :rtype: str
        """
        return self._GroupKey

    @GroupKey.setter
    def GroupKey(self, GroupKey):
        self._GroupKey = GroupKey

    @property
    def GroupValue(self):
        """账单维度值
        :rtype: str
        """
        return self._GroupValue

    @GroupValue.setter
    def GroupValue(self, GroupValue):
        self._GroupValue = GroupValue

    @property
    def TotalCost(self):
        """原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        """优惠后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def Business(self):
        """产品汇总信息
        :rtype: list of BusinessSummaryInfo
        """
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
        :type RealTotalCost: str
        :param _TotalCost: 原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :type TotalCost: str
        """
        self._RealTotalCost = None
        self._TotalCost = None

    @property
    def RealTotalCost(self):
        """优惠后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def TotalCost(self):
        """原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :rtype: str
        """
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
        


class TagDataInfo(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 分账标签键
        :type TagKey: str
        :param _Status: 标签类型，0普通标签，1分账标签
        :type Status: int
        :param _UpdateTime: 设置分账标签时间，普通标签不返回
        :type UpdateTime: str
        """
        self._TagKey = None
        self._Status = None
        self._UpdateTime = None

    @property
    def TagKey(self):
        """分账标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Status(self):
        """标签类型，0普通标签，1分账标签
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        """设置分账标签时间，普通标签不返回
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._Status = params.get("Status")
        self._UpdateTime = params.get("UpdateTime")
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
        :type TagValue: str
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
        """标签值
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def RealTotalCostRatio(self):
        """费用所占百分比，两位小数
        :rtype: str
        """
        return self._RealTotalCostRatio

    @RealTotalCostRatio.setter
    def RealTotalCostRatio(self, RealTotalCostRatio):
        self._RealTotalCostRatio = RealTotalCostRatio

    @property
    def RealTotalCost(self):
        """优惠后总价
        :rtype: str
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def CashPayAmount(self):
        """现金账户支出：通过现金账户支付的金额
        :rtype: str
        """
        return self._CashPayAmount

    @CashPayAmount.setter
    def CashPayAmount(self, CashPayAmount):
        self._CashPayAmount = CashPayAmount

    @property
    def IncentivePayAmount(self):
        """赠送账户支出：使用赠送金支付的金额
        :rtype: str
        """
        return self._IncentivePayAmount

    @IncentivePayAmount.setter
    def IncentivePayAmount(self, IncentivePayAmount):
        self._IncentivePayAmount = IncentivePayAmount

    @property
    def VoucherPayAmount(self):
        """优惠券支出：使用各类优惠券（如代金券、现金券等）支付的金额
        :rtype: str
        """
        return self._VoucherPayAmount

    @VoucherPayAmount.setter
    def VoucherPayAmount(self, VoucherPayAmount):
        self._VoucherPayAmount = VoucherPayAmount

    @property
    def TransferPayAmount(self):
        """分成金账户支出：通过分成金账户支付的金额
        :rtype: str
        """
        return self._TransferPayAmount

    @TransferPayAmount.setter
    def TransferPayAmount(self, TransferPayAmount):
        self._TransferPayAmount = TransferPayAmount

    @property
    def TotalCost(self):
        """原价，单位为元。TotalCost字段自账单3.0（即2021-05）之后开始生效，账单3.0之前返回"-"。合同价的情况下，TotalCost字段与官网价格存在差异，也返回“-”。
        :rtype: str
        """
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
        :type ProductName: str
        :param _SubProductName: 商品细节
        :type SubProductName: str
        :param _ProductCode: 产品码	
        :type ProductCode: str
        :param _SubProductCode: 子产品码	
        :type SubProductCode: str
        :param _BillingItemCode: 计费项码	
        :type BillingItemCode: str
        :param _SubBillingItemCode: 计费细项码	
        :type SubBillingItemCode: str
        :param _ProductEnName: 产品英文名	
        :type ProductEnName: str
        :param _SubProductEnName: 子产品英文名	
        :type SubProductEnName: str
        :param _CalcUnit: 结算周期	
        :type CalcUnit: str
        :param _Action: payMode为prepay 且 payScene为common的情况下存在
        :type Action: str
        """
        self._ProductName = None
        self._SubProductName = None
        self._ProductCode = None
        self._SubProductCode = None
        self._BillingItemCode = None
        self._SubBillingItemCode = None
        self._ProductEnName = None
        self._SubProductEnName = None
        self._CalcUnit = None
        self._Action = None

    @property
    def ProductName(self):
        """商品名
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductName(self):
        """商品细节
        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def ProductCode(self):
        """产品码	
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        """子产品码	
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def BillingItemCode(self):
        """计费项码	
        :rtype: str
        """
        return self._BillingItemCode

    @BillingItemCode.setter
    def BillingItemCode(self, BillingItemCode):
        self._BillingItemCode = BillingItemCode

    @property
    def SubBillingItemCode(self):
        """计费细项码	
        :rtype: str
        """
        return self._SubBillingItemCode

    @SubBillingItemCode.setter
    def SubBillingItemCode(self, SubBillingItemCode):
        self._SubBillingItemCode = SubBillingItemCode

    @property
    def ProductEnName(self):
        """产品英文名	
        :rtype: str
        """
        return self._ProductEnName

    @ProductEnName.setter
    def ProductEnName(self, ProductEnName):
        self._ProductEnName = ProductEnName

    @property
    def SubProductEnName(self):
        """子产品英文名	
        :rtype: str
        """
        return self._SubProductEnName

    @SubProductEnName.setter
    def SubProductEnName(self, SubProductEnName):
        self._SubProductEnName = SubProductEnName

    @property
    def CalcUnit(self):
        """结算周期	
        :rtype: str
        """
        return self._CalcUnit

    @CalcUnit.setter
    def CalcUnit(self, CalcUnit):
        self._CalcUnit = CalcUnit

    @property
    def Action(self):
        """payMode为prepay 且 payScene为common的情况下存在
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._SubProductName = params.get("SubProductName")
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._BillingItemCode = params.get("BillingItemCode")
        self._SubBillingItemCode = params.get("SubBillingItemCode")
        self._ProductEnName = params.get("ProductEnName")
        self._SubProductEnName = params.get("SubProductEnName")
        self._CalcUnit = params.get("CalcUnit")
        self._Action = params.get("Action")
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
        :type UsageDetails: list of UsageDetails
        :param _PayMode: 付费模式
        :type PayMode: str
        :param _VoucherId: 查询的券id
        :type VoucherId: str
        :param _PayScene: 交易场景：（adjust：调账、common：正常交易场景）
        :type PayScene: str
        :param _SeqId: 唯一id,对应交易:预付费的dealName,调账/后付费的outTradeNo
        :type SeqId: str
        """
        self._UsedAmount = None
        self._UsedTime = None
        self._UsageDetails = None
        self._PayMode = None
        self._VoucherId = None
        self._PayScene = None
        self._SeqId = None

    @property
    def UsedAmount(self):
        """使用金额（微分）
        :rtype: int
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def UsedTime(self):
        """使用时间
        :rtype: str
        """
        return self._UsedTime

    @UsedTime.setter
    def UsedTime(self, UsedTime):
        self._UsedTime = UsedTime

    @property
    def UsageDetails(self):
        """使用记录细节
        :rtype: list of UsageDetails
        """
        return self._UsageDetails

    @UsageDetails.setter
    def UsageDetails(self, UsageDetails):
        self._UsageDetails = UsageDetails

    @property
    def PayMode(self):
        """付费模式
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def VoucherId(self):
        """查询的券id
        :rtype: str
        """
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def PayScene(self):
        """交易场景：（adjust：调账、common：正常交易场景）
        :rtype: str
        """
        return self._PayScene

    @PayScene.setter
    def PayScene(self, PayScene):
        self._PayScene = PayScene

    @property
    def SeqId(self):
        """唯一id,对应交易:预付费的dealName,调账/后付费的outTradeNo
        :rtype: str
        """
        return self._SeqId

    @SeqId.setter
    def SeqId(self, SeqId):
        self._SeqId = SeqId


    def _deserialize(self, params):
        self._UsedAmount = params.get("UsedAmount")
        self._UsedTime = params.get("UsedTime")
        if params.get("UsageDetails") is not None:
            self._UsageDetails = []
            for item in params.get("UsageDetails"):
                obj = UsageDetails()
                obj._deserialize(item)
                self._UsageDetails.append(obj)
        self._PayMode = params.get("PayMode")
        self._VoucherId = params.get("VoucherId")
        self._PayScene = params.get("PayScene")
        self._SeqId = params.get("SeqId")
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
        :type ApplicableProducts: :class:`tencentcloud.billing.v20180709.models.ApplicableProducts`
        :param _ExcludedProducts: 不适用商品信息
        :type ExcludedProducts: list of ExcludedProducts
        :param _PolicyRemark: 使用说明/批次备注
        :type PolicyRemark: str
        :param _CreateTime: 发券时间
        :type CreateTime: str
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
        self._PolicyRemark = None
        self._CreateTime = None

    @property
    def OwnerUin(self):
        """代金券拥有者
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Status(self):
        """券状态：待使用：unUsed，已使用： used，已发货：delivered，已作废： cancel，已过期：overdue
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NominalValue(self):
        """代金券面额（微分）
        :rtype: int
        """
        return self._NominalValue

    @NominalValue.setter
    def NominalValue(self, NominalValue):
        self._NominalValue = NominalValue

    @property
    def Balance(self):
        """剩余金额（微分）
        :rtype: int
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def VoucherId(self):
        """代金券id
        :rtype: str
        """
        return self._VoucherId

    @VoucherId.setter
    def VoucherId(self, VoucherId):
        self._VoucherId = VoucherId

    @property
    def PayMode(self):
        """postPay后付费/prePay预付费/riPay预留实例/空字符串或者'*'表示全部模式
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayScene(self):
        """付费场景PayMode=postPay时：spotpay-竞价实例,"settle account"-普通后付费PayMode=prePay时：purchase-包年包月新购，renew-包年包月续费（自动续费），modify-包年包月配置变更(变配）PayMode=riPay时：oneOffFee-预留实例预付，hourlyFee-预留实例每小时扣费，*-支持全部付费场景
        :rtype: str
        """
        return self._PayScene

    @PayScene.setter
    def PayScene(self, PayScene):
        self._PayScene = PayScene

    @property
    def BeginTime(self):
        """有效期生效时间
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """有效期截止时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ApplicableProducts(self):
        """适用商品信息
        :rtype: :class:`tencentcloud.billing.v20180709.models.ApplicableProducts`
        """
        return self._ApplicableProducts

    @ApplicableProducts.setter
    def ApplicableProducts(self, ApplicableProducts):
        self._ApplicableProducts = ApplicableProducts

    @property
    def ExcludedProducts(self):
        """不适用商品信息
        :rtype: list of ExcludedProducts
        """
        return self._ExcludedProducts

    @ExcludedProducts.setter
    def ExcludedProducts(self, ExcludedProducts):
        self._ExcludedProducts = ExcludedProducts

    @property
    def PolicyRemark(self):
        """使用说明/批次备注
        :rtype: str
        """
        return self._PolicyRemark

    @PolicyRemark.setter
    def PolicyRemark(self, PolicyRemark):
        self._PolicyRemark = PolicyRemark

    @property
    def CreateTime(self):
        """发券时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


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
        self._PolicyRemark = params.get("PolicyRemark")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        