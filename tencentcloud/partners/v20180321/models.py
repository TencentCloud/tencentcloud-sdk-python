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


class AgentAuditedClient(AbstractModel):
    """已审核代客信息

    """

    def __init__(self):
        """
        :param Uin: 代理商账号ID\n        :type Uin: str\n        :param ClientUin: 代客账号ID\n        :type ClientUin: str\n        :param AgentTime: 代客审核通过时间戳\n        :type AgentTime: str\n        :param ClientFlag: 代客类型，可能值为a/b/c\n        :type ClientFlag: str\n        :param ClientRemark: 代客备注\n        :type ClientRemark: str\n        :param ClientName: 代客名称（首选实名认证名称）\n        :type ClientName: str\n        :param AuthType: 认证类型, 0：个人，1：企业；其他：未认证\n        :type AuthType: str\n        :param AppId: 代客APPID\n        :type AppId: str\n        :param LastMonthAmt: 上月消费金额\n        :type LastMonthAmt: int\n        :param ThisMonthAmt: 本月消费金额\n        :type ThisMonthAmt: int\n        :param HasOverdueBill: 是否欠费,0：不欠费；1：欠费\n        :type HasOverdueBill: int\n        :param ClientType: 客户类型：可以为new(新拓)/assign(指定)/old(存量已关联)/old_newchecking(存量-新关联考核中)/old_newnotpass(存量-新关联未达标)/direct(直销)/direct_newopp(直销(新商机))/空\n        :type ClientType: str\n        :param ProjectType: 项目类型：可以为self(自拓项目)/platform(合作项目)/repeat(复算项目  )/空\n        :type ProjectType: str\n        :param SalesUin: 业务员ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SalesUin: str\n        :param SalesName: 业务员姓名
注意：此字段可能返回 null，表示取不到有效值。\n        :type SalesName: str\n        :param Mail: 代客邮箱
注意：此字段可能返回 null，表示取不到有效值。\n        :type Mail: str\n        """
        self.Uin = None
        self.ClientUin = None
        self.AgentTime = None
        self.ClientFlag = None
        self.ClientRemark = None
        self.ClientName = None
        self.AuthType = None
        self.AppId = None
        self.LastMonthAmt = None
        self.ThisMonthAmt = None
        self.HasOverdueBill = None
        self.ClientType = None
        self.ProjectType = None
        self.SalesUin = None
        self.SalesName = None
        self.Mail = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.ClientUin = params.get("ClientUin")
        self.AgentTime = params.get("AgentTime")
        self.ClientFlag = params.get("ClientFlag")
        self.ClientRemark = params.get("ClientRemark")
        self.ClientName = params.get("ClientName")
        self.AuthType = params.get("AuthType")
        self.AppId = params.get("AppId")
        self.LastMonthAmt = params.get("LastMonthAmt")
        self.ThisMonthAmt = params.get("ThisMonthAmt")
        self.HasOverdueBill = params.get("HasOverdueBill")
        self.ClientType = params.get("ClientType")
        self.ProjectType = params.get("ProjectType")
        self.SalesUin = params.get("SalesUin")
        self.SalesName = params.get("SalesName")
        self.Mail = params.get("Mail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentBillElem(AbstractModel):
    """业务信息定义

    """

    def __init__(self):
        """
        :param Uin: 代理商账号ID\n        :type Uin: str\n        :param OrderId: 订单号，仅对预付费账单有意义\n        :type OrderId: str\n        :param ClientUin: 代客账号ID\n        :type ClientUin: str\n        :param ClientRemark: 代客备注名称\n        :type ClientRemark: str\n        :param PayTime: 支付时间\n        :type PayTime: str\n        :param GoodsType: 云产品名称\n        :type GoodsType: str\n        :param PayMode: 预付费/后付费\n        :type PayMode: str\n        :param SettleMonth: 支付月份\n        :type SettleMonth: str\n        :param Amt: 支付金额，单位分\n        :type Amt: int\n        :param PayerMode: agentpay：代付；selfpay：自付\n        :type PayerMode: str\n        :param ClientType: 客户类型：可以为new(新拓)/assign(指定)/old(存量)/空
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientType: str\n        :param ProjectType: 项目类型：可以为self(自拓项目)/platform(合作项目)/repeat(复算项目  )/空
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectType: str\n        :param ActivityId: 活动ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityId: str\n        """
        self.Uin = None
        self.OrderId = None
        self.ClientUin = None
        self.ClientRemark = None
        self.PayTime = None
        self.GoodsType = None
        self.PayMode = None
        self.SettleMonth = None
        self.Amt = None
        self.PayerMode = None
        self.ClientType = None
        self.ProjectType = None
        self.ActivityId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.OrderId = params.get("OrderId")
        self.ClientUin = params.get("ClientUin")
        self.ClientRemark = params.get("ClientRemark")
        self.PayTime = params.get("PayTime")
        self.GoodsType = params.get("GoodsType")
        self.PayMode = params.get("PayMode")
        self.SettleMonth = params.get("SettleMonth")
        self.Amt = params.get("Amt")
        self.PayerMode = params.get("PayerMode")
        self.ClientType = params.get("ClientType")
        self.ProjectType = params.get("ProjectType")
        self.ActivityId = params.get("ActivityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentClientElem(AbstractModel):
    """描述待审核代客信息

    """

    def __init__(self):
        """
        :param Uin: 代理商账号ID\n        :type Uin: str\n        :param ClientUin: 代客账号ID\n        :type ClientUin: str\n        :param ApplyTime: 代客申请时间戳\n        :type ApplyTime: int\n        :param ClientFlag: 代客类型，可能值为a/b/c\n        :type ClientFlag: str\n        :param Mail: 代客邮箱，打码显示\n        :type Mail: str\n        :param Phone: 代客手机，打码显示\n        :type Phone: str\n        :param HasOverdueBill: 0表示不欠费，1表示欠费\n        :type HasOverdueBill: int\n        :param Status: 1:待代理商审核;2:待腾讯云审核4:待腾讯云渠道审批\n        :type Status: int\n        :param SalesUin: 业务员ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SalesUin: str\n        :param SalesName: 业务员姓名
注意：此字段可能返回 null，表示取不到有效值。\n        :type SalesName: str\n        :param ClientName: 客户名称，此字段和控制台返回一致。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientName: str\n        """
        self.Uin = None
        self.ClientUin = None
        self.ApplyTime = None
        self.ClientFlag = None
        self.Mail = None
        self.Phone = None
        self.HasOverdueBill = None
        self.Status = None
        self.SalesUin = None
        self.SalesName = None
        self.ClientName = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.ClientUin = params.get("ClientUin")
        self.ApplyTime = params.get("ApplyTime")
        self.ClientFlag = params.get("ClientFlag")
        self.Mail = params.get("Mail")
        self.Phone = params.get("Phone")
        self.HasOverdueBill = params.get("HasOverdueBill")
        self.Status = params.get("Status")
        self.SalesUin = params.get("SalesUin")
        self.SalesName = params.get("SalesName")
        self.ClientName = params.get("ClientName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentDealElem(AbstractModel):
    """描述代理商代付的订单信息

    """

    def __init__(self):
        """
        :param DealId: 订单自增 ID\n        :type DealId: str\n        :param DealName: 订单号\n        :type DealName: str\n        :param GoodsCategoryId: 商品类型 ID\n        :type GoodsCategoryId: str\n        :param OwnerUin: 订单所有者\n        :type OwnerUin: str\n        :param AppId: 订单所有者对应 appId
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppId: str\n        :param GoodsNum: 商品数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type GoodsNum: str\n        :param GoodsPrice: 价格详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type GoodsPrice: :class:`tencentcloud.partners.v20180321.models.DealGoodsPriceElem`\n        :param Creater: 下单人
注意：此字段可能返回 null，表示取不到有效值。\n        :type Creater: str\n        :param CreatTime: 下单时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatTime: str\n        :param PayEndTime: 支付结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayEndTime: str\n        :param BillId: 扣费流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type BillId: str\n        :param Payer: 支付人
注意：此字段可能返回 null，表示取不到有效值。\n        :type Payer: str\n        :param DealStatus: 订单状态，中文描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type DealStatus: str\n        :param Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param GoodsName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GoodsName: str\n        :param ClientRemark: 客户备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientRemark: str\n        :param ActionType: 订单操作类型，purchase（新购），renew（续费），modify（配置变更）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActionType: str\n        :param VoucherDecline: 代金券抵扣金额，单位分
注意：此字段可能返回 null，表示取不到有效值。\n        :type VoucherDecline: str\n        :param BigDealId: 大订单号
注意：此字段可能返回 null，表示取不到有效值。\n        :type BigDealId: str\n        :param ClientType: 客户类型（new：新拓；old：存量；assign：指派）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientType: str\n        :param ProjectType: 项目类型（self：自拓；repeat：直销；platform：官网合作）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectType: str\n        :param SalesUin: 业务员账号ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SalesUin: str\n        :param PayerMode: 支付方式，0：自付；1：代付
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayerMode: str\n        :param ActivityId: 活动ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityId: str\n        :param OverdueTime: 订单过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type OverdueTime: str\n        :param ProductInfo: 产品详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductInfo: list of ProductInfoElem\n        :param PaymentMethod: 付款方式
注意：此字段可能返回 null，表示取不到有效值。\n        :type PaymentMethod: str\n        :param UpdateTime: 订单更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        """
        self.DealId = None
        self.DealName = None
        self.GoodsCategoryId = None
        self.OwnerUin = None
        self.AppId = None
        self.GoodsNum = None
        self.GoodsPrice = None
        self.Creater = None
        self.CreatTime = None
        self.PayEndTime = None
        self.BillId = None
        self.Payer = None
        self.DealStatus = None
        self.Status = None
        self.GoodsName = None
        self.ClientRemark = None
        self.ActionType = None
        self.VoucherDecline = None
        self.BigDealId = None
        self.ClientType = None
        self.ProjectType = None
        self.SalesUin = None
        self.PayerMode = None
        self.ActivityId = None
        self.OverdueTime = None
        self.ProductInfo = None
        self.PaymentMethod = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.DealName = params.get("DealName")
        self.GoodsCategoryId = params.get("GoodsCategoryId")
        self.OwnerUin = params.get("OwnerUin")
        self.AppId = params.get("AppId")
        self.GoodsNum = params.get("GoodsNum")
        if params.get("GoodsPrice") is not None:
            self.GoodsPrice = DealGoodsPriceElem()
            self.GoodsPrice._deserialize(params.get("GoodsPrice"))
        self.Creater = params.get("Creater")
        self.CreatTime = params.get("CreatTime")
        self.PayEndTime = params.get("PayEndTime")
        self.BillId = params.get("BillId")
        self.Payer = params.get("Payer")
        self.DealStatus = params.get("DealStatus")
        self.Status = params.get("Status")
        self.GoodsName = params.get("GoodsName")
        self.ClientRemark = params.get("ClientRemark")
        self.ActionType = params.get("ActionType")
        self.VoucherDecline = params.get("VoucherDecline")
        self.BigDealId = params.get("BigDealId")
        self.ClientType = params.get("ClientType")
        self.ProjectType = params.get("ProjectType")
        self.SalesUin = params.get("SalesUin")
        self.PayerMode = params.get("PayerMode")
        self.ActivityId = params.get("ActivityId")
        self.OverdueTime = params.get("OverdueTime")
        if params.get("ProductInfo") is not None:
            self.ProductInfo = []
            for item in params.get("ProductInfo"):
                obj = ProductInfoElem()
                obj._deserialize(item)
                self.ProductInfo.append(obj)
        self.PaymentMethod = params.get("PaymentMethod")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentDealNewElem(AbstractModel):
    """描述代理商代付的订单信息

    """

    def __init__(self):
        """
        :param DealId: 订单自增 ID\n        :type DealId: str\n        :param DealName: 订单号\n        :type DealName: str\n        :param GoodsCategoryId: 商品类型 ID\n        :type GoodsCategoryId: str\n        :param OwnerUin: 订单所有者\n        :type OwnerUin: str\n        :param AppId: 订单所有者对应 appId
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppId: str\n        :param GoodsNum: 商品数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type GoodsNum: str\n        :param GoodsPrice: 价格详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type GoodsPrice: :class:`tencentcloud.partners.v20180321.models.DealGoodsPriceNewElem`\n        :param Creater: 下单人
注意：此字段可能返回 null，表示取不到有效值。\n        :type Creater: str\n        :param CreatTime: 下单时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatTime: str\n        :param PayEndTime: 支付结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayEndTime: str\n        :param BillId: 扣费流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type BillId: str\n        :param Payer: 支付人
注意：此字段可能返回 null，表示取不到有效值。\n        :type Payer: str\n        :param DealStatus: 订单状态，中文描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type DealStatus: str\n        :param Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param GoodsName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GoodsName: str\n        :param ClientRemark: 客户备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientRemark: str\n        :param ActionType: 订单操作类型，purchase（新购），renew（续费），modify（配置变更）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActionType: str\n        :param VoucherDecline: 代金券抵扣金额，单位分
注意：此字段可能返回 null，表示取不到有效值。\n        :type VoucherDecline: str\n        :param BigDealId: 大订单号
注意：此字段可能返回 null，表示取不到有效值。\n        :type BigDealId: str\n        :param ClientType: 客户类型（new：新拓；old：存量；assign：指派）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientType: str\n        :param ProjectType: 项目类型（self：自拓；repeat：直销；platform：官网合作）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectType: str\n        :param SalesUin: 业务员账号ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SalesUin: str\n        :param PayerMode: 支付方式，0：自付；1：代付
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayerMode: str\n        :param ActivityId: 活动ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityId: str\n        :param OverdueTime: 订单过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type OverdueTime: str\n        :param ProductInfo: 产品详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductInfo: list of ProductInfoElem\n        :param PaymentMethod: 付款方式
注意：此字段可能返回 null，表示取不到有效值。\n        :type PaymentMethod: str\n        :param UpdateTime: 订单更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        """
        self.DealId = None
        self.DealName = None
        self.GoodsCategoryId = None
        self.OwnerUin = None
        self.AppId = None
        self.GoodsNum = None
        self.GoodsPrice = None
        self.Creater = None
        self.CreatTime = None
        self.PayEndTime = None
        self.BillId = None
        self.Payer = None
        self.DealStatus = None
        self.Status = None
        self.GoodsName = None
        self.ClientRemark = None
        self.ActionType = None
        self.VoucherDecline = None
        self.BigDealId = None
        self.ClientType = None
        self.ProjectType = None
        self.SalesUin = None
        self.PayerMode = None
        self.ActivityId = None
        self.OverdueTime = None
        self.ProductInfo = None
        self.PaymentMethod = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.DealName = params.get("DealName")
        self.GoodsCategoryId = params.get("GoodsCategoryId")
        self.OwnerUin = params.get("OwnerUin")
        self.AppId = params.get("AppId")
        self.GoodsNum = params.get("GoodsNum")
        if params.get("GoodsPrice") is not None:
            self.GoodsPrice = DealGoodsPriceNewElem()
            self.GoodsPrice._deserialize(params.get("GoodsPrice"))
        self.Creater = params.get("Creater")
        self.CreatTime = params.get("CreatTime")
        self.PayEndTime = params.get("PayEndTime")
        self.BillId = params.get("BillId")
        self.Payer = params.get("Payer")
        self.DealStatus = params.get("DealStatus")
        self.Status = params.get("Status")
        self.GoodsName = params.get("GoodsName")
        self.ClientRemark = params.get("ClientRemark")
        self.ActionType = params.get("ActionType")
        self.VoucherDecline = params.get("VoucherDecline")
        self.BigDealId = params.get("BigDealId")
        self.ClientType = params.get("ClientType")
        self.ProjectType = params.get("ProjectType")
        self.SalesUin = params.get("SalesUin")
        self.PayerMode = params.get("PayerMode")
        self.ActivityId = params.get("ActivityId")
        self.OverdueTime = params.get("OverdueTime")
        if params.get("ProductInfo") is not None:
            self.ProductInfo = []
            for item in params.get("ProductInfo"):
                obj = ProductInfoElem()
                obj._deserialize(item)
                self.ProductInfo.append(obj)
        self.PaymentMethod = params.get("PaymentMethod")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentPayDealsRequest(AbstractModel):
    """AgentPayDeals请求参数结构体

    """

    def __init__(self):
        """
        :param OwnerUin: 订单所有者uin\n        :type OwnerUin: str\n        :param AgentPay: 代付标志，1：代付；0：自付\n        :type AgentPay: int\n        :param DealNames: 订单号数组\n        :type DealNames: list of str\n        """
        self.OwnerUin = None
        self.AgentPay = None
        self.DealNames = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.AgentPay = params.get("AgentPay")
        self.DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentPayDealsResponse(AbstractModel):
    """AgentPayDeals返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AgentSalesmanElem(AbstractModel):
    """代理商业务员信息

    """

    def __init__(self):
        """
        :param Uin: 代理商账号ID\n        :type Uin: str\n        :param SalesUin: 业务员ID\n        :type SalesUin: str\n        :param SalesName: 业务员姓名\n        :type SalesName: str\n        :param CreateTime: 业务员创建时间\n        :type CreateTime: str\n        """
        self.Uin = None
        self.SalesUin = None
        self.SalesName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.SalesUin = params.get("SalesUin")
        self.SalesName = params.get("SalesName")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentTransferMoneyRequest(AbstractModel):
    """AgentTransferMoney请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 客户账号ID\n        :type ClientUin: str\n        :param Amount: 转账金额，单位分\n        :type Amount: int\n        """
        self.ClientUin = None
        self.Amount = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.Amount = params.get("Amount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentTransferMoneyResponse(AbstractModel):
    """AgentTransferMoney返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AuditApplyClientRequest(AbstractModel):
    """AuditApplyClient请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 待审核客户账号ID\n        :type ClientUin: str\n        :param AuditResult: 审核结果，可能的取值：accept/reject\n        :type AuditResult: str\n        :param Note: 申请理由，B类客户审核通过时必须填写申请理由\n        :type Note: str\n        """
        self.ClientUin = None
        self.AuditResult = None
        self.Note = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.AuditResult = params.get("AuditResult")
        self.Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditApplyClientResponse(AbstractModel):
    """AuditApplyClient返回参数结构体

    """

    def __init__(self):
        """
        :param Uin: 代理商账号ID\n        :type Uin: str\n        :param ClientUin: 客户账号ID\n        :type ClientUin: str\n        :param AuditResult: 审核结果，包括accept/reject/qcloudaudit（腾讯云审核）\n        :type AuditResult: str\n        :param AgentTime: 关联时间对应的时间戳\n        :type AgentTime: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Uin = None
        self.ClientUin = None
        self.AuditResult = None
        self.AgentTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.ClientUin = params.get("ClientUin")
        self.AuditResult = params.get("AuditResult")
        self.AgentTime = params.get("AgentTime")
        self.RequestId = params.get("RequestId")


class ClientBaseElem(AbstractModel):
    """代客基础信息

    """

    def __init__(self):
        """
        :param AgentUin: 代客关联的代理商UIN\n        :type AgentUin: str\n        :param ClientUin: 代客UIN\n        :type ClientUin: str\n        :param ClientRelateType: 代客关联类型 0:代理 1:转售\n        :type ClientRelateType: int\n        :param AgentCooperationMode: 代理商合作模式 0:代理 1:转售\n        :type AgentCooperationMode: int\n        :param AgentCountry: 代理商国家编码 China:中国  其他:海外，如US等\n        :type AgentCountry: str\n        """
        self.AgentUin = None
        self.ClientUin = None
        self.ClientRelateType = None
        self.AgentCooperationMode = None
        self.AgentCountry = None


    def _deserialize(self, params):
        self.AgentUin = params.get("AgentUin")
        self.ClientUin = params.get("ClientUin")
        self.ClientRelateType = params.get("ClientRelateType")
        self.AgentCooperationMode = params.get("AgentCooperationMode")
        self.AgentCountry = params.get("AgentCountry")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePayRelationForClientRequest(AbstractModel):
    """CreatePayRelationForClient请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 客户账号ID\n        :type ClientUin: str\n        """
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePayRelationForClientResponse(AbstractModel):
    """CreatePayRelationForClient返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DealGoodsPriceElem(AbstractModel):
    """订单价格详情

    """

    def __init__(self):
        """
        :param RealTotalCost: 实付金额（单位：分）\n        :type RealTotalCost: int\n        :param OriginalTotalCost: 订单实际金额（不含折扣，单位：分）\n        :type OriginalTotalCost: int\n        """
        self.RealTotalCost = None
        self.OriginalTotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.OriginalTotalCost = params.get("OriginalTotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DealGoodsPriceNewElem(AbstractModel):
    """订单价格详情

    """

    def __init__(self):
        """
        :param RealTotalCost: 实付金额（单位：分）\n        :type RealTotalCost: int\n        :param OriginalTotalCost: 原始金额（不含折扣，单位：分）\n        :type OriginalTotalCost: int\n        """
        self.RealTotalCost = None
        self.OriginalTotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.OriginalTotalCost = params.get("OriginalTotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentAuditedClientsRequest(AbstractModel):
    """DescribeAgentAuditedClients请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 客户账号ID\n        :type ClientUin: str\n        :param ClientName: 客户名称。由于涉及隐私，名称打码显示，故名称仅支持打码后的模糊搜索\n        :type ClientName: str\n        :param ClientFlag: 客户类型，a/b，类型定义参考代理商相关政策文档\n        :type ClientFlag: str\n        :param OrderDirection: ASC/DESC， 不区分大小写，按审核通过时间排序\n        :type OrderDirection: str\n        :param ClientUins: 客户账号ID列表\n        :type ClientUins: list of str\n        :param HasOverdueBill: 是否欠费。0：不欠费；1：欠费\n        :type HasOverdueBill: int\n        :param ClientRemark: 客户备注\n        :type ClientRemark: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param ClientType: 客户类型：可以为new(新拓)/assign(指定)/old(存量已关联)/old_newchecking(存量-新关联考核中)/old_newnotpass(存量-新关联未达标)/direct(直销)/direct_newopp(直销(新商机))/空\n        :type ClientType: str\n        :param ProjectType: 项目类型：可以为self(自拓项目)/platform(合作项目)/repeat(复算项目  )/空\n        :type ProjectType: str\n        :param SalesUin: 业务员ID\n        :type SalesUin: str\n        :param SalesName: 业务员姓名（模糊查询）\n        :type SalesName: str\n        """
        self.ClientUin = None
        self.ClientName = None
        self.ClientFlag = None
        self.OrderDirection = None
        self.ClientUins = None
        self.HasOverdueBill = None
        self.ClientRemark = None
        self.Offset = None
        self.Limit = None
        self.ClientType = None
        self.ProjectType = None
        self.SalesUin = None
        self.SalesName = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.ClientName = params.get("ClientName")
        self.ClientFlag = params.get("ClientFlag")
        self.OrderDirection = params.get("OrderDirection")
        self.ClientUins = params.get("ClientUins")
        self.HasOverdueBill = params.get("HasOverdueBill")
        self.ClientRemark = params.get("ClientRemark")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClientType = params.get("ClientType")
        self.ProjectType = params.get("ProjectType")
        self.SalesUin = params.get("SalesUin")
        self.SalesName = params.get("SalesName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentAuditedClientsResponse(AbstractModel):
    """DescribeAgentAuditedClients返回参数结构体

    """

    def __init__(self):
        """
        :param AgentClientSet: 已审核代客列表\n        :type AgentClientSet: list of AgentAuditedClient\n        :param TotalCount: 符合条件的代客总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentClientSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentClientSet") is not None:
            self.AgentClientSet = []
            for item in params.get("AgentClientSet"):
                obj = AgentAuditedClient()
                obj._deserialize(item)
                self.AgentClientSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAgentBillsRequest(AbstractModel):
    """DescribeAgentBills请求参数结构体

    """

    def __init__(self):
        """
        :param SettleMonth: 支付月份，如2018-02\n        :type SettleMonth: str\n        :param ClientUin: 客户账号ID\n        :type ClientUin: str\n        :param PayMode: 支付方式，prepay/postpay\n        :type PayMode: str\n        :param OrderId: 预付费订单号\n        :type OrderId: str\n        :param ClientRemark: 客户备注名称\n        :type ClientRemark: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        """
        self.SettleMonth = None
        self.ClientUin = None
        self.PayMode = None
        self.OrderId = None
        self.ClientRemark = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SettleMonth = params.get("SettleMonth")
        self.ClientUin = params.get("ClientUin")
        self.PayMode = params.get("PayMode")
        self.OrderId = params.get("OrderId")
        self.ClientRemark = params.get("ClientRemark")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentBillsResponse(AbstractModel):
    """DescribeAgentBills返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件列表总数量\n        :type TotalCount: int\n        :param AgentBillSet: 业务明细列表\n        :type AgentBillSet: list of AgentBillElem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AgentBillSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AgentBillSet") is not None:
            self.AgentBillSet = []
            for item in params.get("AgentBillSet"):
                obj = AgentBillElem()
                obj._deserialize(item)
                self.AgentBillSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAgentClientGradeRequest(AbstractModel):
    """DescribeAgentClientGrade请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 代客uin\n        :type ClientUin: str\n        """
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentClientGradeResponse(AbstractModel):
    """DescribeAgentClientGrade返回参数结构体

    """

    def __init__(self):
        """
        :param AuditStatus: 审核状态：0待审核，1，已审核\n        :type AuditStatus: int\n        :param AuthState: 实名认证状态：0，未实名认证，1实名认证\n        :type AuthState: int\n        :param ClientGrade: 客户级别\n        :type ClientGrade: str\n        :param ClientType: 客户类型：1，个人；2，企业；3，其他\n        :type ClientType: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AuditStatus = None
        self.AuthState = None
        self.ClientGrade = None
        self.ClientType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuditStatus = params.get("AuditStatus")
        self.AuthState = params.get("AuthState")
        self.ClientGrade = params.get("ClientGrade")
        self.ClientType = params.get("ClientType")
        self.RequestId = params.get("RequestId")


class DescribeAgentClientsRequest(AbstractModel):
    """DescribeAgentClients请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 客户账号ID\n        :type ClientUin: str\n        :param ClientName: 客户名称。由于涉及隐私，名称打码显示，故名称仅支持打码后的模糊搜索\n        :type ClientName: str\n        :param ClientFlag: 客户类型，a/b，类型定义参考代理商相关政策文档\n        :type ClientFlag: str\n        :param OrderDirection: ASC/DESC， 不区分大小写，按申请时间排序\n        :type OrderDirection: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param SalesUin: 业务员ID\n        :type SalesUin: str\n        :param SalesName: 业务员姓名（模糊查询）\n        :type SalesName: str\n        """
        self.ClientUin = None
        self.ClientName = None
        self.ClientFlag = None
        self.OrderDirection = None
        self.Offset = None
        self.Limit = None
        self.SalesUin = None
        self.SalesName = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.ClientName = params.get("ClientName")
        self.ClientFlag = params.get("ClientFlag")
        self.OrderDirection = params.get("OrderDirection")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SalesUin = params.get("SalesUin")
        self.SalesName = params.get("SalesName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentClientsResponse(AbstractModel):
    """DescribeAgentClients返回参数结构体

    """

    def __init__(self):
        """
        :param AgentClientSet: 待审核代客列表\n        :type AgentClientSet: list of AgentClientElem\n        :param TotalCount: 符合条件的代客总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentClientSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentClientSet") is not None:
            self.AgentClientSet = []
            for item in params.get("AgentClientSet"):
                obj = AgentClientElem()
                obj._deserialize(item)
                self.AgentClientSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAgentDealsByCacheRequest(AbstractModel):
    """DescribeAgentDealsByCache请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param CreatTimeRangeStart: 下单时间范围起始点\n        :type CreatTimeRangeStart: str\n        :param CreatTimeRangeEnd: 下单时间范围终止点\n        :type CreatTimeRangeEnd: str\n        :param Order: 0:下单时间降序；其他：下单时间升序\n        :type Order: int\n        :param Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)\n        :type Status: int\n        :param OwnerUins: 下单人账号ID列表\n        :type OwnerUins: list of str\n        :param DealNames: 订单号列表\n        :type DealNames: list of str\n        :param PayerMode: 支付方式，0：自付；1：代付\n        :type PayerMode: int\n        """
        self.Offset = None
        self.Limit = None
        self.CreatTimeRangeStart = None
        self.CreatTimeRangeEnd = None
        self.Order = None
        self.Status = None
        self.OwnerUins = None
        self.DealNames = None
        self.PayerMode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreatTimeRangeStart = params.get("CreatTimeRangeStart")
        self.CreatTimeRangeEnd = params.get("CreatTimeRangeEnd")
        self.Order = params.get("Order")
        self.Status = params.get("Status")
        self.OwnerUins = params.get("OwnerUins")
        self.DealNames = params.get("DealNames")
        self.PayerMode = params.get("PayerMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentDealsByCacheResponse(AbstractModel):
    """DescribeAgentDealsByCache返回参数结构体

    """

    def __init__(self):
        """
        :param AgentDealSet: 订单数组\n        :type AgentDealSet: list of AgentDealNewElem\n        :param TotalCount: 符合条件的订单总数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentDealSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentDealSet") is not None:
            self.AgentDealSet = []
            for item in params.get("AgentDealSet"):
                obj = AgentDealNewElem()
                obj._deserialize(item)
                self.AgentDealSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAgentDealsCacheRequest(AbstractModel):
    """DescribeAgentDealsCache请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param CreatTimeRangeStart: 下单时间范围起始点\n        :type CreatTimeRangeStart: str\n        :param CreatTimeRangeEnd: 下单时间范围终止点\n        :type CreatTimeRangeEnd: str\n        :param Order: 0:下单时间降序；其他：下单时间升序\n        :type Order: int\n        :param Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)\n        :type Status: int\n        :param OwnerUins: 下单人账号ID列表\n        :type OwnerUins: list of str\n        :param DealNames: 订单号列表\n        :type DealNames: list of str\n        :param PayerMode: 支付方式，0：自付；1：代付\n        :type PayerMode: int\n        """
        self.Offset = None
        self.Limit = None
        self.CreatTimeRangeStart = None
        self.CreatTimeRangeEnd = None
        self.Order = None
        self.Status = None
        self.OwnerUins = None
        self.DealNames = None
        self.PayerMode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreatTimeRangeStart = params.get("CreatTimeRangeStart")
        self.CreatTimeRangeEnd = params.get("CreatTimeRangeEnd")
        self.Order = params.get("Order")
        self.Status = params.get("Status")
        self.OwnerUins = params.get("OwnerUins")
        self.DealNames = params.get("DealNames")
        self.PayerMode = params.get("PayerMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentDealsCacheResponse(AbstractModel):
    """DescribeAgentDealsCache返回参数结构体

    """

    def __init__(self):
        """
        :param AgentDealSet: 订单数组\n        :type AgentDealSet: list of AgentDealElem\n        :param TotalCount: 符合条件的订单总数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentDealSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentDealSet") is not None:
            self.AgentDealSet = []
            for item in params.get("AgentDealSet"):
                obj = AgentDealElem()
                obj._deserialize(item)
                self.AgentDealSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAgentPayDealsRequest(AbstractModel):
    """DescribeAgentPayDeals请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param CreatTimeRangeStart: 下单时间范围起始点(不传时会默认查15天内订单，传值时需要传15天内的起始时间)\n        :type CreatTimeRangeStart: str\n        :param CreatTimeRangeEnd: 下单时间范围终止点\n        :type CreatTimeRangeEnd: str\n        :param Order: 0:下单时间降序；其他：下单时间升序\n        :type Order: int\n        :param Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)\n        :type Status: int\n        :param OwnerUins: 下单人账号ID列表\n        :type OwnerUins: list of str\n        :param DealNames: 订单号列表\n        :type DealNames: list of str\n        """
        self.Offset = None
        self.Limit = None
        self.CreatTimeRangeStart = None
        self.CreatTimeRangeEnd = None
        self.Order = None
        self.Status = None
        self.OwnerUins = None
        self.DealNames = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreatTimeRangeStart = params.get("CreatTimeRangeStart")
        self.CreatTimeRangeEnd = params.get("CreatTimeRangeEnd")
        self.Order = params.get("Order")
        self.Status = params.get("Status")
        self.OwnerUins = params.get("OwnerUins")
        self.DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentPayDealsResponse(AbstractModel):
    """DescribeAgentPayDeals返回参数结构体

    """

    def __init__(self):
        """
        :param AgentPayDealSet: 订单数组\n        :type AgentPayDealSet: list of AgentDealElem\n        :param TotalCount: 符合条件的订单总数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentPayDealSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentPayDealSet") is not None:
            self.AgentPayDealSet = []
            for item in params.get("AgentPayDealSet"):
                obj = AgentDealElem()
                obj._deserialize(item)
                self.AgentPayDealSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAgentPayDealsV2Request(AbstractModel):
    """DescribeAgentPayDealsV2请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param CreatTimeRangeStart: 下单时间范围起始点(不传时会默认查15天内订单，传值时需要传15天内的起始时间)\n        :type CreatTimeRangeStart: str\n        :param CreatTimeRangeEnd: 下单时间范围终止点\n        :type CreatTimeRangeEnd: str\n        :param Order: 0:下单时间降序；其他：下单时间升序\n        :type Order: int\n        :param Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)\n        :type Status: int\n        :param OwnerUins: 下单人账号ID列表\n        :type OwnerUins: list of str\n        :param DealNames: 订单号列表\n        :type DealNames: list of str\n        """
        self.Offset = None
        self.Limit = None
        self.CreatTimeRangeStart = None
        self.CreatTimeRangeEnd = None
        self.Order = None
        self.Status = None
        self.OwnerUins = None
        self.DealNames = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreatTimeRangeStart = params.get("CreatTimeRangeStart")
        self.CreatTimeRangeEnd = params.get("CreatTimeRangeEnd")
        self.Order = params.get("Order")
        self.Status = params.get("Status")
        self.OwnerUins = params.get("OwnerUins")
        self.DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentPayDealsV2Response(AbstractModel):
    """DescribeAgentPayDealsV2返回参数结构体

    """

    def __init__(self):
        """
        :param AgentPayDealSet: 订单数组\n        :type AgentPayDealSet: list of AgentDealNewElem\n        :param TotalCount: 符合条件的订单总数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentPayDealSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentPayDealSet") is not None:
            self.AgentPayDealSet = []
            for item in params.get("AgentPayDealSet"):
                obj = AgentDealNewElem()
                obj._deserialize(item)
                self.AgentPayDealSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAgentSelfPayDealsRequest(AbstractModel):
    """DescribeAgentSelfPayDeals请求参数结构体

    """

    def __init__(self):
        """
        :param OwnerUin: 下单人账号ID\n        :type OwnerUin: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param CreatTimeRangeStart: 下单时间范围起始点(不传时会默认查15天内订单，传值时需要传15天内的起始时间)\n        :type CreatTimeRangeStart: str\n        :param CreatTimeRangeEnd: 下单时间范围终止点\n        :type CreatTimeRangeEnd: str\n        :param Order: 0:下单时间降序；其他：下单时间升序\n        :type Order: int\n        :param Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)\n        :type Status: int\n        :param DealNames: 订单号列表\n        :type DealNames: list of str\n        """
        self.OwnerUin = None
        self.Offset = None
        self.Limit = None
        self.CreatTimeRangeStart = None
        self.CreatTimeRangeEnd = None
        self.Order = None
        self.Status = None
        self.DealNames = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreatTimeRangeStart = params.get("CreatTimeRangeStart")
        self.CreatTimeRangeEnd = params.get("CreatTimeRangeEnd")
        self.Order = params.get("Order")
        self.Status = params.get("Status")
        self.DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentSelfPayDealsResponse(AbstractModel):
    """DescribeAgentSelfPayDeals返回参数结构体

    """

    def __init__(self):
        """
        :param AgentPayDealSet: 订单数组\n        :type AgentPayDealSet: list of AgentDealElem\n        :param TotalCount: 符合条件的订单总数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentPayDealSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentPayDealSet") is not None:
            self.AgentPayDealSet = []
            for item in params.get("AgentPayDealSet"):
                obj = AgentDealElem()
                obj._deserialize(item)
                self.AgentPayDealSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAgentSelfPayDealsV2Request(AbstractModel):
    """DescribeAgentSelfPayDealsV2请求参数结构体

    """

    def __init__(self):
        """
        :param OwnerUin: 下单人账号ID\n        :type OwnerUin: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param CreatTimeRangeStart: 下单时间范围起始点(不传时会默认查15天内订单，传值时需要传15天内的起始时间)\n        :type CreatTimeRangeStart: str\n        :param CreatTimeRangeEnd: 下单时间范围终止点\n        :type CreatTimeRangeEnd: str\n        :param Order: 0:下单时间降序；其他：下单时间升序\n        :type Order: int\n        :param Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)\n        :type Status: int\n        :param DealNames: 订单号列表\n        :type DealNames: list of str\n        """
        self.OwnerUin = None
        self.Offset = None
        self.Limit = None
        self.CreatTimeRangeStart = None
        self.CreatTimeRangeEnd = None
        self.Order = None
        self.Status = None
        self.DealNames = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreatTimeRangeStart = params.get("CreatTimeRangeStart")
        self.CreatTimeRangeEnd = params.get("CreatTimeRangeEnd")
        self.Order = params.get("Order")
        self.Status = params.get("Status")
        self.DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentSelfPayDealsV2Response(AbstractModel):
    """DescribeAgentSelfPayDealsV2返回参数结构体

    """

    def __init__(self):
        """
        :param AgentPayDealSet: 订单数组\n        :type AgentPayDealSet: list of AgentDealNewElem\n        :param TotalCount: 符合条件的订单总数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentPayDealSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentPayDealSet") is not None:
            self.AgentPayDealSet = []
            for item in params.get("AgentPayDealSet"):
                obj = AgentDealNewElem()
                obj._deserialize(item)
                self.AgentPayDealSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClientBalanceNewRequest(AbstractModel):
    """DescribeClientBalanceNew请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 客户(代客)账号ID\n        :type ClientUin: str\n        """
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientBalanceNewResponse(AbstractModel):
    """DescribeClientBalanceNew返回参数结构体

    """

    def __init__(self):
        """
        :param Balance: 账户可用余额，单位分 （可用余额 = 现金余额 + 赠送金余额 - 欠费金额 - 冻结金额）\n        :type Balance: int\n        :param Cash: 账户现金余额，单位分\n        :type Cash: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Balance = None
        self.Cash = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Balance = params.get("Balance")
        self.Cash = params.get("Cash")
        self.RequestId = params.get("RequestId")


class DescribeClientBalanceRequest(AbstractModel):
    """DescribeClientBalance请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 客户(代客)账号ID\n        :type ClientUin: str\n        """
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientBalanceResponse(AbstractModel):
    """DescribeClientBalance返回参数结构体

    """

    def __init__(self):
        """
        :param Balance: 账户可用余额，单位分 （可用余额 = 现金余额 - 冻结金额）\n        :type Balance: int\n        :param Cash: 账户现金余额，单位分\n        :type Cash: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Balance = None
        self.Cash = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Balance = params.get("Balance")
        self.Cash = params.get("Cash")
        self.RequestId = params.get("RequestId")


class DescribeClientBaseInfoRequest(AbstractModel):
    """DescribeClientBaseInfo请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 代客UIN\n        :type ClientUin: str\n        """
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientBaseInfoResponse(AbstractModel):
    """DescribeClientBaseInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ClientBaseSet: 代客基础信息数组\n        :type ClientBaseSet: list of ClientBaseElem\n        :param TotalCount: 符合条件的代客数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ClientBaseSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClientBaseSet") is not None:
            self.ClientBaseSet = []
            for item in params.get("ClientBaseSet"):
                obj = ClientBaseElem()
                obj._deserialize(item)
                self.ClientBaseSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRebateInfosRequest(AbstractModel):
    """DescribeRebateInfos请求参数结构体

    """

    def __init__(self):
        """
        :param RebateMonth: 返佣月份，如2018-02\n        :type RebateMonth: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        """
        self.RebateMonth = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RebateMonth = params.get("RebateMonth")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRebateInfosResponse(AbstractModel):
    """DescribeRebateInfos返回参数结构体

    """

    def __init__(self):
        """
        :param RebateInfoSet: 返佣信息列表\n        :type RebateInfoSet: list of RebateInfoElem\n        :param TotalCount: 符合查询条件返佣信息数目\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RebateInfoSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RebateInfoSet") is not None:
            self.RebateInfoSet = []
            for item in params.get("RebateInfoSet"):
                obj = RebateInfoElem()
                obj._deserialize(item)
                self.RebateInfoSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSalesmansRequest(AbstractModel):
    """DescribeSalesmans请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param SalesName: 业务员姓名(模糊查询)\n        :type SalesName: str\n        :param SalesUin: 业务员ID\n        :type SalesUin: str\n        :param OrderDirection: ASC/DESC， 不区分大小写，按创建通过时间排序\n        :type OrderDirection: str\n        """
        self.Offset = None
        self.Limit = None
        self.SalesName = None
        self.SalesUin = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SalesName = params.get("SalesName")
        self.SalesUin = params.get("SalesUin")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSalesmansResponse(AbstractModel):
    """DescribeSalesmans返回参数结构体

    """

    def __init__(self):
        """
        :param AgentSalesmanSet: 业务员列表\n        :type AgentSalesmanSet: list of AgentSalesmanElem\n        :param TotalCount: 符合条件的代客总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentSalesmanSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentSalesmanSet") is not None:
            self.AgentSalesmanSet = []
            for item in params.get("AgentSalesmanSet"):
                obj = AgentSalesmanElem()
                obj._deserialize(item)
                self.AgentSalesmanSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUnbindClientListRequest(AbstractModel):
    """DescribeUnbindClientList请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 解绑状态：0:所有,1:审核中,2已解绑\n        :type Status: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        :param UnbindUin: 解绑账号ID\n        :type UnbindUin: str\n        :param ApplyTimeStart: 解绑申请时间范围起始点\n        :type ApplyTimeStart: str\n        :param ApplyTimeEnd: 解绑申请时间范围终止点\n        :type ApplyTimeEnd: str\n        :param OrderDirection: 对申请时间的升序降序，值：asc，desc\n        :type OrderDirection: str\n        """
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.UnbindUin = None
        self.ApplyTimeStart = None
        self.ApplyTimeEnd = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.UnbindUin = params.get("UnbindUin")
        self.ApplyTimeStart = params.get("ApplyTimeStart")
        self.ApplyTimeEnd = params.get("ApplyTimeEnd")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnbindClientListResponse(AbstractModel):
    """DescribeUnbindClientList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的解绑客户数量\n        :type TotalCount: int\n        :param UnbindClientList: 符合条件的解绑客户列表\n        :type UnbindClientList: list of UnbindClientElem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.UnbindClientList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UnbindClientList") is not None:
            self.UnbindClientList = []
            for item in params.get("UnbindClientList"):
                obj = UnbindClientElem()
                obj._deserialize(item)
                self.UnbindClientList.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyClientRemarkRequest(AbstractModel):
    """ModifyClientRemark请求参数结构体

    """

    def __init__(self):
        """
        :param ClientRemark: 客户备注名称\n        :type ClientRemark: str\n        :param ClientUin: 客户账号ID\n        :type ClientUin: str\n        """
        self.ClientRemark = None
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientRemark = params.get("ClientRemark")
        self.ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClientRemarkResponse(AbstractModel):
    """ModifyClientRemark返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProductInfoElem(AbstractModel):
    """产品详情

    """

    def __init__(self):
        """
        :param Name: 产品属性\n        :type Name: str\n        :param Value: 产品属性值\n        :type Value: str\n        """
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
        


class RebateInfoElem(AbstractModel):
    """返佣信息定义

    """

    def __init__(self):
        """
        :param Uin: 代理商账号ID\n        :type Uin: str\n        :param RebateMonth: 返佣月份，如2018-02\n        :type RebateMonth: str\n        :param Amt: 返佣金额，单位分\n        :type Amt: int\n        :param MonthSales: 月度业绩，单位分\n        :type MonthSales: int\n        :param QuarterSales: 季度业绩，单位分\n        :type QuarterSales: int\n        :param ExceptionFlag: NORMAL(正常)/HAS_OVERDUE_BILL(欠费)/NO_CONTRACT(缺合同)\n        :type ExceptionFlag: str\n        """
        self.Uin = None
        self.RebateMonth = None
        self.Amt = None
        self.MonthSales = None
        self.QuarterSales = None
        self.ExceptionFlag = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.RebateMonth = params.get("RebateMonth")
        self.Amt = params.get("Amt")
        self.MonthSales = params.get("MonthSales")
        self.QuarterSales = params.get("QuarterSales")
        self.ExceptionFlag = params.get("ExceptionFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemovePayRelationForClientRequest(AbstractModel):
    """RemovePayRelationForClient请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 客户账号ID\n        :type ClientUin: str\n        """
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemovePayRelationForClientResponse(AbstractModel):
    """RemovePayRelationForClient返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindClientElem(AbstractModel):
    """解绑客户信息

    """

    def __init__(self):
        """
        :param Uin: 解绑账号ID\n        :type Uin: str\n        :param Name: 名称\n        :type Name: str\n        :param Status: 状态：0:审核中；1：已解绑；2：已撤销 3：关联撤销 4: 已驳回\n        :type Status: int\n        :param ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplyTime: str\n        :param ActionTime: 解绑/撤销时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActionTime: str\n        """
        self.Uin = None
        self.Name = None
        self.Status = None
        self.ApplyTime = None
        self.ActionTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.ApplyTime = params.get("ApplyTime")
        self.ActionTime = params.get("ActionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        