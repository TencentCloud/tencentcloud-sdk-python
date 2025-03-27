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
        r"""
        :param _Uin: 代理商账号ID
        :type Uin: str
        :param _ClientUin: 代客账号ID
        :type ClientUin: str
        :param _AgentTime: 代客审核通过时间戳
        :type AgentTime: str
        :param _ClientFlag: 代客类型，可能值为a/b/c
        :type ClientFlag: str
        :param _ClientRemark: 代客备注
        :type ClientRemark: str
        :param _ClientName: 代客名称（首选实名认证名称）
        :type ClientName: str
        :param _AuthType: 认证类型, 0：个人，1：企业；其他：未认证或无效值
        :type AuthType: str
        :param _AppId: 代客APPID
        :type AppId: str
        :param _LastMonthAmt: 上月消费金额
        :type LastMonthAmt: int
        :param _ThisMonthAmt: 本月消费金额
        :type ThisMonthAmt: int
        :param _HasOverdueBill: 是否欠费,0：不欠费；1：欠费
        :type HasOverdueBill: int
        :param _ClientType: 客户类型：可以为new(自拓)/assign(指派)/old(官网)/direct(直销)/direct_newopp(直销(新商机))/空
        :type ClientType: str
        :param _ProjectType: 项目类型：可以为self(自拓项目)/platform(合作项目)/repeat(复算项目  )/空
        :type ProjectType: str
        :param _SalesUin: 业务员ID
        :type SalesUin: str
        :param _SalesName: 业务员姓名
        :type SalesName: str
        :param _Mail: 代客邮箱
        :type Mail: str
        :param _TransactionType: 交易类型:交易类型 1-原类型 2-代理型  3-代采型
        :type TransactionType: str
        """
        self._Uin = None
        self._ClientUin = None
        self._AgentTime = None
        self._ClientFlag = None
        self._ClientRemark = None
        self._ClientName = None
        self._AuthType = None
        self._AppId = None
        self._LastMonthAmt = None
        self._ThisMonthAmt = None
        self._HasOverdueBill = None
        self._ClientType = None
        self._ProjectType = None
        self._SalesUin = None
        self._SalesName = None
        self._Mail = None
        self._TransactionType = None

    @property
    def Uin(self):
        """代理商账号ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ClientUin(self):
        """代客账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def AgentTime(self):
        """代客审核通过时间戳
        :rtype: str
        """
        return self._AgentTime

    @AgentTime.setter
    def AgentTime(self, AgentTime):
        self._AgentTime = AgentTime

    @property
    def ClientFlag(self):
        """代客类型，可能值为a/b/c
        :rtype: str
        """
        return self._ClientFlag

    @ClientFlag.setter
    def ClientFlag(self, ClientFlag):
        self._ClientFlag = ClientFlag

    @property
    def ClientRemark(self):
        """代客备注
        :rtype: str
        """
        return self._ClientRemark

    @ClientRemark.setter
    def ClientRemark(self, ClientRemark):
        self._ClientRemark = ClientRemark

    @property
    def ClientName(self):
        """代客名称（首选实名认证名称）
        :rtype: str
        """
        return self._ClientName

    @ClientName.setter
    def ClientName(self, ClientName):
        self._ClientName = ClientName

    @property
    def AuthType(self):
        """认证类型, 0：个人，1：企业；其他：未认证或无效值
        :rtype: str
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def AppId(self):
        """代客APPID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def LastMonthAmt(self):
        """上月消费金额
        :rtype: int
        """
        return self._LastMonthAmt

    @LastMonthAmt.setter
    def LastMonthAmt(self, LastMonthAmt):
        self._LastMonthAmt = LastMonthAmt

    @property
    def ThisMonthAmt(self):
        """本月消费金额
        :rtype: int
        """
        return self._ThisMonthAmt

    @ThisMonthAmt.setter
    def ThisMonthAmt(self, ThisMonthAmt):
        self._ThisMonthAmt = ThisMonthAmt

    @property
    def HasOverdueBill(self):
        """是否欠费,0：不欠费；1：欠费
        :rtype: int
        """
        return self._HasOverdueBill

    @HasOverdueBill.setter
    def HasOverdueBill(self, HasOverdueBill):
        self._HasOverdueBill = HasOverdueBill

    @property
    def ClientType(self):
        """客户类型：可以为new(自拓)/assign(指派)/old(官网)/direct(直销)/direct_newopp(直销(新商机))/空
        :rtype: str
        """
        return self._ClientType

    @ClientType.setter
    def ClientType(self, ClientType):
        self._ClientType = ClientType

    @property
    def ProjectType(self):
        """项目类型：可以为self(自拓项目)/platform(合作项目)/repeat(复算项目  )/空
        :rtype: str
        """
        return self._ProjectType

    @ProjectType.setter
    def ProjectType(self, ProjectType):
        self._ProjectType = ProjectType

    @property
    def SalesUin(self):
        """业务员ID
        :rtype: str
        """
        return self._SalesUin

    @SalesUin.setter
    def SalesUin(self, SalesUin):
        self._SalesUin = SalesUin

    @property
    def SalesName(self):
        """业务员姓名
        :rtype: str
        """
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName

    @property
    def Mail(self):
        """代客邮箱
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def TransactionType(self):
        """交易类型:交易类型 1-原类型 2-代理型  3-代采型
        :rtype: str
        """
        return self._TransactionType

    @TransactionType.setter
    def TransactionType(self, TransactionType):
        self._TransactionType = TransactionType


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._ClientUin = params.get("ClientUin")
        self._AgentTime = params.get("AgentTime")
        self._ClientFlag = params.get("ClientFlag")
        self._ClientRemark = params.get("ClientRemark")
        self._ClientName = params.get("ClientName")
        self._AuthType = params.get("AuthType")
        self._AppId = params.get("AppId")
        self._LastMonthAmt = params.get("LastMonthAmt")
        self._ThisMonthAmt = params.get("ThisMonthAmt")
        self._HasOverdueBill = params.get("HasOverdueBill")
        self._ClientType = params.get("ClientType")
        self._ProjectType = params.get("ProjectType")
        self._SalesUin = params.get("SalesUin")
        self._SalesName = params.get("SalesName")
        self._Mail = params.get("Mail")
        self._TransactionType = params.get("TransactionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentBillElem(AbstractModel):
    """业务信息定义

    """

    def __init__(self):
        r"""
        :param _Uin: 代理商账号ID
        :type Uin: str
        :param _OrderId: 订单号，仅对预付费账单有意义
        :type OrderId: str
        :param _ClientUin: 代客账号ID
        :type ClientUin: str
        :param _ClientRemark: 代客备注名称
        :type ClientRemark: str
        :param _PayTime: 支付时间
        :type PayTime: str
        :param _GoodsType: 云产品名称
        :type GoodsType: str
        :param _PayMode: 预付费/后付费
        :type PayMode: str
        :param _SettleMonth: 支付月份
        :type SettleMonth: str
        :param _Amt: 支付金额，单位分
        :type Amt: int
        :param _PayerMode: agentpay：代付；selfpay：自付
        :type PayerMode: str
        :param _ClientType: 客户类型：可以为new(自拓)/assign(指定)/old(官网)/direct(直销)/direct_newopp(直销(新商机))/空
        :type ClientType: str
        :param _ProjectType: 项目类型：可以为self(自拓项目)/platform(合作项目)/repeat(复算项目  )/空
        :type ProjectType: str
        :param _ActivityId: 活动ID
        :type ActivityId: str
        """
        self._Uin = None
        self._OrderId = None
        self._ClientUin = None
        self._ClientRemark = None
        self._PayTime = None
        self._GoodsType = None
        self._PayMode = None
        self._SettleMonth = None
        self._Amt = None
        self._PayerMode = None
        self._ClientType = None
        self._ProjectType = None
        self._ActivityId = None

    @property
    def Uin(self):
        """代理商账号ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def OrderId(self):
        """订单号，仅对预付费账单有意义
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ClientUin(self):
        """代客账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def ClientRemark(self):
        """代客备注名称
        :rtype: str
        """
        return self._ClientRemark

    @ClientRemark.setter
    def ClientRemark(self, ClientRemark):
        self._ClientRemark = ClientRemark

    @property
    def PayTime(self):
        """支付时间
        :rtype: str
        """
        return self._PayTime

    @PayTime.setter
    def PayTime(self, PayTime):
        self._PayTime = PayTime

    @property
    def GoodsType(self):
        """云产品名称
        :rtype: str
        """
        return self._GoodsType

    @GoodsType.setter
    def GoodsType(self, GoodsType):
        self._GoodsType = GoodsType

    @property
    def PayMode(self):
        """预付费/后付费
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def SettleMonth(self):
        """支付月份
        :rtype: str
        """
        return self._SettleMonth

    @SettleMonth.setter
    def SettleMonth(self, SettleMonth):
        self._SettleMonth = SettleMonth

    @property
    def Amt(self):
        """支付金额，单位分
        :rtype: int
        """
        return self._Amt

    @Amt.setter
    def Amt(self, Amt):
        self._Amt = Amt

    @property
    def PayerMode(self):
        """agentpay：代付；selfpay：自付
        :rtype: str
        """
        return self._PayerMode

    @PayerMode.setter
    def PayerMode(self, PayerMode):
        self._PayerMode = PayerMode

    @property
    def ClientType(self):
        """客户类型：可以为new(自拓)/assign(指定)/old(官网)/direct(直销)/direct_newopp(直销(新商机))/空
        :rtype: str
        """
        return self._ClientType

    @ClientType.setter
    def ClientType(self, ClientType):
        self._ClientType = ClientType

    @property
    def ProjectType(self):
        """项目类型：可以为self(自拓项目)/platform(合作项目)/repeat(复算项目  )/空
        :rtype: str
        """
        return self._ProjectType

    @ProjectType.setter
    def ProjectType(self, ProjectType):
        self._ProjectType = ProjectType

    @property
    def ActivityId(self):
        """活动ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._OrderId = params.get("OrderId")
        self._ClientUin = params.get("ClientUin")
        self._ClientRemark = params.get("ClientRemark")
        self._PayTime = params.get("PayTime")
        self._GoodsType = params.get("GoodsType")
        self._PayMode = params.get("PayMode")
        self._SettleMonth = params.get("SettleMonth")
        self._Amt = params.get("Amt")
        self._PayerMode = params.get("PayerMode")
        self._ClientType = params.get("ClientType")
        self._ProjectType = params.get("ProjectType")
        self._ActivityId = params.get("ActivityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentClientElem(AbstractModel):
    """描述待审核代客信息

    """

    def __init__(self):
        r"""
        :param _Uin: 代理商账号ID
        :type Uin: str
        :param _ClientUin: 代客账号ID
        :type ClientUin: str
        :param _ApplyTime: 代客申请时间戳
        :type ApplyTime: int
        :param _ClientFlag: 代客类型，可能值为a/b/c/other
        :type ClientFlag: str
        :param _Mail: 代客邮箱，打码显示
        :type Mail: str
        :param _Phone: 代客手机，打码显示
        :type Phone: str
        :param _HasOverdueBill: 0表示不欠费，1表示欠费
        :type HasOverdueBill: int
        :param _Status: 1:待代理商审核;2:待腾讯云审核4:待腾讯云渠道审批
        :type Status: int
        :param _SalesUin: 业务员ID
        :type SalesUin: str
        :param _SalesName: 业务员姓名
        :type SalesName: str
        :param _ClientName: 客户名称，此字段和控制台返回一致。
        :type ClientName: str
        """
        self._Uin = None
        self._ClientUin = None
        self._ApplyTime = None
        self._ClientFlag = None
        self._Mail = None
        self._Phone = None
        self._HasOverdueBill = None
        self._Status = None
        self._SalesUin = None
        self._SalesName = None
        self._ClientName = None

    @property
    def Uin(self):
        """代理商账号ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ClientUin(self):
        """代客账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def ApplyTime(self):
        """代客申请时间戳
        :rtype: int
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def ClientFlag(self):
        """代客类型，可能值为a/b/c/other
        :rtype: str
        """
        return self._ClientFlag

    @ClientFlag.setter
    def ClientFlag(self, ClientFlag):
        self._ClientFlag = ClientFlag

    @property
    def Mail(self):
        """代客邮箱，打码显示
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Phone(self):
        """代客手机，打码显示
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def HasOverdueBill(self):
        """0表示不欠费，1表示欠费
        :rtype: int
        """
        return self._HasOverdueBill

    @HasOverdueBill.setter
    def HasOverdueBill(self, HasOverdueBill):
        self._HasOverdueBill = HasOverdueBill

    @property
    def Status(self):
        """1:待代理商审核;2:待腾讯云审核4:待腾讯云渠道审批
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SalesUin(self):
        """业务员ID
        :rtype: str
        """
        return self._SalesUin

    @SalesUin.setter
    def SalesUin(self, SalesUin):
        self._SalesUin = SalesUin

    @property
    def SalesName(self):
        """业务员姓名
        :rtype: str
        """
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName

    @property
    def ClientName(self):
        """客户名称，此字段和控制台返回一致。
        :rtype: str
        """
        return self._ClientName

    @ClientName.setter
    def ClientName(self, ClientName):
        self._ClientName = ClientName


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._ClientUin = params.get("ClientUin")
        self._ApplyTime = params.get("ApplyTime")
        self._ClientFlag = params.get("ClientFlag")
        self._Mail = params.get("Mail")
        self._Phone = params.get("Phone")
        self._HasOverdueBill = params.get("HasOverdueBill")
        self._Status = params.get("Status")
        self._SalesUin = params.get("SalesUin")
        self._SalesName = params.get("SalesName")
        self._ClientName = params.get("ClientName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentDealNewElem(AbstractModel):
    """描述代理商代付的订单信息

    """

    def __init__(self):
        r"""
        :param _DealId: 订单自增 ID【请勿依赖该字段作为唯一标识】
        :type DealId: str
        :param _DealName: 订单号【订单唯一键】
        :type DealName: str
        :param _GoodsCategoryId: 商品类型 ID
        :type GoodsCategoryId: str
        :param _OwnerUin: 订单所有者
        :type OwnerUin: str
        :param _AppId: 订单所有者对应 appId
        :type AppId: str
        :param _GoodsNum: 商品数量
        :type GoodsNum: str
        :param _GoodsPrice: 价格详情
        :type GoodsPrice: :class:`tencentcloud.partners.v20180321.models.DealGoodsPriceNewElem`
        :param _Creater: 下单人
        :type Creater: str
        :param _CreatTime: 下单时间
        :type CreatTime: str
        :param _PayEndTime: 支付结束时间
        :type PayEndTime: str
        :param _BillId: 扣费流水号
        :type BillId: str
        :param _Payer: 支付人
        :type Payer: str
        :param _DealStatus: 订单状态，中文描述
        :type DealStatus: str
        :param _Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)
        :type Status: str
        :param _GoodsName: 产品名称
        :type GoodsName: str
        :param _ClientRemark: 客户备注
        :type ClientRemark: str
        :param _ActionType: 订单操作类型，"purchase":"新购","upgrade":"升配","upConvertExpire":"升配","downgrade":"降配","downConvertExpire":"降配","renew":"续费","refund":"退货","modifyNetworkMode":"调整带宽模式","modifyNetworkSize":"调整带宽大小","preMoveOut":"资源迁出","preMoveIn":"资源迁入","preToPost":"包年包月转按量","modify":"变配","postMoveOut":"资源迁出","postMoveIn":"资源迁入","recoverRefundForward":"调账补偿","recoverPayReserve":"调账补偿","recoverPayForward":"调账扣费","recoverRefundReserve":"调账扣费"
        :type ActionType: str
        :param _VoucherDecline: 代金券抵扣金额，单位分
        :type VoucherDecline: str
        :param _BigDealId: 大订单号
        :type BigDealId: str
        :param _ClientType: 客户类型（new：自拓；old：官网；assign：指派；direct：直销；direct_newopp：直销(新商机)）
        :type ClientType: str
        :param _ProjectType: 项目类型（self：自拓；repeat：直销；platform：官网合作）
        :type ProjectType: str
        :param _SalesUin: 业务员账号ID
        :type SalesUin: str
        :param _PayerMode: 支付方式，0：自付；1：代付
        :type PayerMode: str
        :param _ActivityId: 活动ID
        :type ActivityId: str
        :param _OverdueTime: 订单过期时间
        :type OverdueTime: str
        :param _ProductInfo: 产品详情
        :type ProductInfo: list of ProductInfoElem
        :param _PaymentMethod: 付款方式
        :type PaymentMethod: str
        :param _UpdateTime: 订单更新时间
        :type UpdateTime: str
        :param _ResourceIds: 资源id
        :type ResourceIds: list of str
        :param _RefundMap: 退款单的原订单信息。当前仅 DescribeClientDealsByCache 接口会返回该字段
        :type RefundMap: list of RefundMap
        :param _SubGoodsName: 子产品名称
        :type SubGoodsName: str
        """
        self._DealId = None
        self._DealName = None
        self._GoodsCategoryId = None
        self._OwnerUin = None
        self._AppId = None
        self._GoodsNum = None
        self._GoodsPrice = None
        self._Creater = None
        self._CreatTime = None
        self._PayEndTime = None
        self._BillId = None
        self._Payer = None
        self._DealStatus = None
        self._Status = None
        self._GoodsName = None
        self._ClientRemark = None
        self._ActionType = None
        self._VoucherDecline = None
        self._BigDealId = None
        self._ClientType = None
        self._ProjectType = None
        self._SalesUin = None
        self._PayerMode = None
        self._ActivityId = None
        self._OverdueTime = None
        self._ProductInfo = None
        self._PaymentMethod = None
        self._UpdateTime = None
        self._ResourceIds = None
        self._RefundMap = None
        self._SubGoodsName = None

    @property
    def DealId(self):
        """订单自增 ID【请勿依赖该字段作为唯一标识】
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def DealName(self):
        """订单号【订单唯一键】
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def GoodsCategoryId(self):
        """商品类型 ID
        :rtype: str
        """
        return self._GoodsCategoryId

    @GoodsCategoryId.setter
    def GoodsCategoryId(self, GoodsCategoryId):
        self._GoodsCategoryId = GoodsCategoryId

    @property
    def OwnerUin(self):
        """订单所有者
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def AppId(self):
        """订单所有者对应 appId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def GoodsNum(self):
        """商品数量
        :rtype: str
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def GoodsPrice(self):
        """价格详情
        :rtype: :class:`tencentcloud.partners.v20180321.models.DealGoodsPriceNewElem`
        """
        return self._GoodsPrice

    @GoodsPrice.setter
    def GoodsPrice(self, GoodsPrice):
        self._GoodsPrice = GoodsPrice

    @property
    def Creater(self):
        """下单人
        :rtype: str
        """
        return self._Creater

    @Creater.setter
    def Creater(self, Creater):
        self._Creater = Creater

    @property
    def CreatTime(self):
        """下单时间
        :rtype: str
        """
        return self._CreatTime

    @CreatTime.setter
    def CreatTime(self, CreatTime):
        self._CreatTime = CreatTime

    @property
    def PayEndTime(self):
        """支付结束时间
        :rtype: str
        """
        return self._PayEndTime

    @PayEndTime.setter
    def PayEndTime(self, PayEndTime):
        self._PayEndTime = PayEndTime

    @property
    def BillId(self):
        """扣费流水号
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def Payer(self):
        """支付人
        :rtype: str
        """
        return self._Payer

    @Payer.setter
    def Payer(self, Payer):
        self._Payer = Payer

    @property
    def DealStatus(self):
        """订单状态，中文描述
        :rtype: str
        """
        return self._DealStatus

    @DealStatus.setter
    def DealStatus(self, DealStatus):
        self._DealStatus = DealStatus

    @property
    def Status(self):
        """订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GoodsName(self):
        """产品名称
        :rtype: str
        """
        return self._GoodsName

    @GoodsName.setter
    def GoodsName(self, GoodsName):
        self._GoodsName = GoodsName

    @property
    def ClientRemark(self):
        """客户备注
        :rtype: str
        """
        return self._ClientRemark

    @ClientRemark.setter
    def ClientRemark(self, ClientRemark):
        self._ClientRemark = ClientRemark

    @property
    def ActionType(self):
        """订单操作类型，"purchase":"新购","upgrade":"升配","upConvertExpire":"升配","downgrade":"降配","downConvertExpire":"降配","renew":"续费","refund":"退货","modifyNetworkMode":"调整带宽模式","modifyNetworkSize":"调整带宽大小","preMoveOut":"资源迁出","preMoveIn":"资源迁入","preToPost":"包年包月转按量","modify":"变配","postMoveOut":"资源迁出","postMoveIn":"资源迁入","recoverRefundForward":"调账补偿","recoverPayReserve":"调账补偿","recoverPayForward":"调账扣费","recoverRefundReserve":"调账扣费"
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def VoucherDecline(self):
        """代金券抵扣金额，单位分
        :rtype: str
        """
        return self._VoucherDecline

    @VoucherDecline.setter
    def VoucherDecline(self, VoucherDecline):
        self._VoucherDecline = VoucherDecline

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
    def ClientType(self):
        """客户类型（new：自拓；old：官网；assign：指派；direct：直销；direct_newopp：直销(新商机)）
        :rtype: str
        """
        return self._ClientType

    @ClientType.setter
    def ClientType(self, ClientType):
        self._ClientType = ClientType

    @property
    def ProjectType(self):
        """项目类型（self：自拓；repeat：直销；platform：官网合作）
        :rtype: str
        """
        return self._ProjectType

    @ProjectType.setter
    def ProjectType(self, ProjectType):
        self._ProjectType = ProjectType

    @property
    def SalesUin(self):
        """业务员账号ID
        :rtype: str
        """
        return self._SalesUin

    @SalesUin.setter
    def SalesUin(self, SalesUin):
        self._SalesUin = SalesUin

    @property
    def PayerMode(self):
        """支付方式，0：自付；1：代付
        :rtype: str
        """
        return self._PayerMode

    @PayerMode.setter
    def PayerMode(self, PayerMode):
        self._PayerMode = PayerMode

    @property
    def ActivityId(self):
        """活动ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def OverdueTime(self):
        """订单过期时间
        :rtype: str
        """
        return self._OverdueTime

    @OverdueTime.setter
    def OverdueTime(self, OverdueTime):
        self._OverdueTime = OverdueTime

    @property
    def ProductInfo(self):
        """产品详情
        :rtype: list of ProductInfoElem
        """
        return self._ProductInfo

    @ProductInfo.setter
    def ProductInfo(self, ProductInfo):
        self._ProductInfo = ProductInfo

    @property
    def PaymentMethod(self):
        """付款方式
        :rtype: str
        """
        return self._PaymentMethod

    @PaymentMethod.setter
    def PaymentMethod(self, PaymentMethod):
        self._PaymentMethod = PaymentMethod

    @property
    def UpdateTime(self):
        """订单更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ResourceIds(self):
        """资源id
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def RefundMap(self):
        """退款单的原订单信息。当前仅 DescribeClientDealsByCache 接口会返回该字段
        :rtype: list of RefundMap
        """
        return self._RefundMap

    @RefundMap.setter
    def RefundMap(self, RefundMap):
        self._RefundMap = RefundMap

    @property
    def SubGoodsName(self):
        """子产品名称
        :rtype: str
        """
        return self._SubGoodsName

    @SubGoodsName.setter
    def SubGoodsName(self, SubGoodsName):
        self._SubGoodsName = SubGoodsName


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._DealName = params.get("DealName")
        self._GoodsCategoryId = params.get("GoodsCategoryId")
        self._OwnerUin = params.get("OwnerUin")
        self._AppId = params.get("AppId")
        self._GoodsNum = params.get("GoodsNum")
        if params.get("GoodsPrice") is not None:
            self._GoodsPrice = DealGoodsPriceNewElem()
            self._GoodsPrice._deserialize(params.get("GoodsPrice"))
        self._Creater = params.get("Creater")
        self._CreatTime = params.get("CreatTime")
        self._PayEndTime = params.get("PayEndTime")
        self._BillId = params.get("BillId")
        self._Payer = params.get("Payer")
        self._DealStatus = params.get("DealStatus")
        self._Status = params.get("Status")
        self._GoodsName = params.get("GoodsName")
        self._ClientRemark = params.get("ClientRemark")
        self._ActionType = params.get("ActionType")
        self._VoucherDecline = params.get("VoucherDecline")
        self._BigDealId = params.get("BigDealId")
        self._ClientType = params.get("ClientType")
        self._ProjectType = params.get("ProjectType")
        self._SalesUin = params.get("SalesUin")
        self._PayerMode = params.get("PayerMode")
        self._ActivityId = params.get("ActivityId")
        self._OverdueTime = params.get("OverdueTime")
        if params.get("ProductInfo") is not None:
            self._ProductInfo = []
            for item in params.get("ProductInfo"):
                obj = ProductInfoElem()
                obj._deserialize(item)
                self._ProductInfo.append(obj)
        self._PaymentMethod = params.get("PaymentMethod")
        self._UpdateTime = params.get("UpdateTime")
        self._ResourceIds = params.get("ResourceIds")
        if params.get("RefundMap") is not None:
            self._RefundMap = []
            for item in params.get("RefundMap"):
                obj = RefundMap()
                obj._deserialize(item)
                self._RefundMap.append(obj)
        self._SubGoodsName = params.get("SubGoodsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentPayDealsRequest(AbstractModel):
    """AgentPayDeals请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 订单所有者uin
        :type OwnerUin: str
        :param _AgentPay: 代付标志，1：代付；0：自付
        :type AgentPay: int
        :param _DealNames: 订单号数组
        :type DealNames: list of str
        """
        self._OwnerUin = None
        self._AgentPay = None
        self._DealNames = None

    @property
    def OwnerUin(self):
        """订单所有者uin
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def AgentPay(self):
        """代付标志，1：代付；0：自付
        :rtype: int
        """
        return self._AgentPay

    @AgentPay.setter
    def AgentPay(self, AgentPay):
        self._AgentPay = AgentPay

    @property
    def DealNames(self):
        """订单号数组
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._AgentPay = params.get("AgentPay")
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentPayDealsResponse(AbstractModel):
    """AgentPayDeals返回参数结构体

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


class AgentSalesmanElem(AbstractModel):
    """代理商业务员信息

    """

    def __init__(self):
        r"""
        :param _Uin: 代理商账号ID
        :type Uin: str
        :param _SalesUin: 业务员ID
        :type SalesUin: str
        :param _SalesName: 业务员姓名
        :type SalesName: str
        :param _CreateTime: 业务员创建时间
        :type CreateTime: str
        """
        self._Uin = None
        self._SalesUin = None
        self._SalesName = None
        self._CreateTime = None

    @property
    def Uin(self):
        """代理商账号ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SalesUin(self):
        """业务员ID
        :rtype: str
        """
        return self._SalesUin

    @SalesUin.setter
    def SalesUin(self, SalesUin):
        self._SalesUin = SalesUin

    @property
    def SalesName(self):
        """业务员姓名
        :rtype: str
        """
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName

    @property
    def CreateTime(self):
        """业务员创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._SalesUin = params.get("SalesUin")
        self._SalesName = params.get("SalesName")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentTransferMoneyRequest(AbstractModel):
    """AgentTransferMoney请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUin: 客户账号ID
        :type ClientUin: str
        :param _Amount: 转账金额，单位分
        :type Amount: int
        """
        self._ClientUin = None
        self._Amount = None

    @property
    def ClientUin(self):
        """客户账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Amount(self):
        """转账金额，单位分
        :rtype: int
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._Amount = params.get("Amount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentTransferMoneyResponse(AbstractModel):
    """AgentTransferMoney返回参数结构体

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


class AssignClientsToSalesRequest(AbstractModel):
    """AssignClientsToSales请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUins: 代客/申请中代客uin列表，最大50条
        :type ClientUins: list of str
        :param _SalesUin: 业务员uin
        :type SalesUin: str
        :param _AssignClientStatus: 代客类型:normal-代客 apply-申请中代客
        :type AssignClientStatus: str
        :param _AssignActionType: 操作类型:assign-执行分派 cancel-取消分派
        :type AssignActionType: str
        """
        self._ClientUins = None
        self._SalesUin = None
        self._AssignClientStatus = None
        self._AssignActionType = None

    @property
    def ClientUins(self):
        """代客/申请中代客uin列表，最大50条
        :rtype: list of str
        """
        return self._ClientUins

    @ClientUins.setter
    def ClientUins(self, ClientUins):
        self._ClientUins = ClientUins

    @property
    def SalesUin(self):
        """业务员uin
        :rtype: str
        """
        return self._SalesUin

    @SalesUin.setter
    def SalesUin(self, SalesUin):
        self._SalesUin = SalesUin

    @property
    def AssignClientStatus(self):
        """代客类型:normal-代客 apply-申请中代客
        :rtype: str
        """
        return self._AssignClientStatus

    @AssignClientStatus.setter
    def AssignClientStatus(self, AssignClientStatus):
        self._AssignClientStatus = AssignClientStatus

    @property
    def AssignActionType(self):
        """操作类型:assign-执行分派 cancel-取消分派
        :rtype: str
        """
        return self._AssignActionType

    @AssignActionType.setter
    def AssignActionType(self, AssignActionType):
        self._AssignActionType = AssignActionType


    def _deserialize(self, params):
        self._ClientUins = params.get("ClientUins")
        self._SalesUin = params.get("SalesUin")
        self._AssignClientStatus = params.get("AssignClientStatus")
        self._AssignActionType = params.get("AssignActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignClientsToSalesResponse(AbstractModel):
    """AssignClientsToSales返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SucceedUins: 处理成功的代客uin列表
        :type SucceedUins: list of str
        :param _FailedUins: 处理失败的代客uin列表
        :type FailedUins: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SucceedUins = None
        self._FailedUins = None
        self._RequestId = None

    @property
    def SucceedUins(self):
        """处理成功的代客uin列表
        :rtype: list of str
        """
        return self._SucceedUins

    @SucceedUins.setter
    def SucceedUins(self, SucceedUins):
        self._SucceedUins = SucceedUins

    @property
    def FailedUins(self):
        """处理失败的代客uin列表
        :rtype: list of str
        """
        return self._FailedUins

    @FailedUins.setter
    def FailedUins(self, FailedUins):
        self._FailedUins = FailedUins

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
        self._SucceedUins = params.get("SucceedUins")
        self._FailedUins = params.get("FailedUins")
        self._RequestId = params.get("RequestId")


class AuditApplyClientRequest(AbstractModel):
    """AuditApplyClient请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUin: 待审核客户账号ID
        :type ClientUin: str
        :param _AuditResult: 审核结果，可能的取值：accept/reject
        :type AuditResult: str
        :param _Note: 申请理由，B类客户审核通过时必须填写申请理由
        :type Note: str
        """
        self._ClientUin = None
        self._AuditResult = None
        self._Note = None

    @property
    def ClientUin(self):
        """待审核客户账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def AuditResult(self):
        """审核结果，可能的取值：accept/reject
        :rtype: str
        """
        return self._AuditResult

    @AuditResult.setter
    def AuditResult(self, AuditResult):
        self._AuditResult = AuditResult

    @property
    def Note(self):
        """申请理由，B类客户审核通过时必须填写申请理由
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._AuditResult = params.get("AuditResult")
        self._Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditApplyClientResponse(AbstractModel):
    """AuditApplyClient返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Uin: 代理商账号ID
        :type Uin: str
        :param _ClientUin: 客户账号ID
        :type ClientUin: str
        :param _AuditResult: 审核结果，包括accept/reject/qcloudaudit（腾讯云审核）
        :type AuditResult: str
        :param _AgentTime: 关联时间对应的时间戳
        :type AgentTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Uin = None
        self._ClientUin = None
        self._AuditResult = None
        self._AgentTime = None
        self._RequestId = None

    @property
    def Uin(self):
        """代理商账号ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ClientUin(self):
        """客户账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def AuditResult(self):
        """审核结果，包括accept/reject/qcloudaudit（腾讯云审核）
        :rtype: str
        """
        return self._AuditResult

    @AuditResult.setter
    def AuditResult(self, AuditResult):
        self._AuditResult = AuditResult

    @property
    def AgentTime(self):
        """关联时间对应的时间戳
        :rtype: int
        """
        return self._AgentTime

    @AgentTime.setter
    def AgentTime(self, AgentTime):
        self._AgentTime = AgentTime

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
        self._Uin = params.get("Uin")
        self._ClientUin = params.get("ClientUin")
        self._AuditResult = params.get("AuditResult")
        self._AgentTime = params.get("AgentTime")
        self._RequestId = params.get("RequestId")


class ClientIncreaseInfoList(AbstractModel):
    """客户增量激励考核信息列表

    """

    def __init__(self):
        r"""
        :param _ClientUin: 客户UIN
        :type ClientUin: str
        :param _IsJoinIncrease: 是否参与增量政策，
Y：是，N：否
        :type IsJoinIncrease: str
        :param _IncreaseUseAssociateDate: 增量考核关联时间
        :type IncreaseUseAssociateDate: str
        :param _TLevel: 参与增量考核的原始客户等级
        :type TLevel: str
        :param _IncreaseGoal: 增量考核目标,分
        :type IncreaseGoal: str
        :param _TotalBaseAmt: 完成订单金额,分
        :type TotalBaseAmt: str
        """
        self._ClientUin = None
        self._IsJoinIncrease = None
        self._IncreaseUseAssociateDate = None
        self._TLevel = None
        self._IncreaseGoal = None
        self._TotalBaseAmt = None

    @property
    def ClientUin(self):
        """客户UIN
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def IsJoinIncrease(self):
        """是否参与增量政策，
Y：是，N：否
        :rtype: str
        """
        return self._IsJoinIncrease

    @IsJoinIncrease.setter
    def IsJoinIncrease(self, IsJoinIncrease):
        self._IsJoinIncrease = IsJoinIncrease

    @property
    def IncreaseUseAssociateDate(self):
        """增量考核关联时间
        :rtype: str
        """
        return self._IncreaseUseAssociateDate

    @IncreaseUseAssociateDate.setter
    def IncreaseUseAssociateDate(self, IncreaseUseAssociateDate):
        self._IncreaseUseAssociateDate = IncreaseUseAssociateDate

    @property
    def TLevel(self):
        """参与增量考核的原始客户等级
        :rtype: str
        """
        return self._TLevel

    @TLevel.setter
    def TLevel(self, TLevel):
        self._TLevel = TLevel

    @property
    def IncreaseGoal(self):
        """增量考核目标,分
        :rtype: str
        """
        return self._IncreaseGoal

    @IncreaseGoal.setter
    def IncreaseGoal(self, IncreaseGoal):
        self._IncreaseGoal = IncreaseGoal

    @property
    def TotalBaseAmt(self):
        """完成订单金额,分
        :rtype: str
        """
        return self._TotalBaseAmt

    @TotalBaseAmt.setter
    def TotalBaseAmt(self, TotalBaseAmt):
        self._TotalBaseAmt = TotalBaseAmt


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._IsJoinIncrease = params.get("IsJoinIncrease")
        self._IncreaseUseAssociateDate = params.get("IncreaseUseAssociateDate")
        self._TLevel = params.get("TLevel")
        self._IncreaseGoal = params.get("IncreaseGoal")
        self._TotalBaseAmt = params.get("TotalBaseAmt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePayRelationForClientRequest(AbstractModel):
    """CreatePayRelationForClient请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUin: 客户账号ID
        :type ClientUin: str
        """
        self._ClientUin = None

    @property
    def ClientUin(self):
        """客户账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePayRelationForClientResponse(AbstractModel):
    """CreatePayRelationForClient返回参数结构体

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


class DealGoodsPriceNewElem(AbstractModel):
    """订单价格详情

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: 实付金额（单位：分）
        :type RealTotalCost: int
        :param _OriginalTotalCost: 原始金额（不含折扣，单位：分）
        :type OriginalTotalCost: int
        """
        self._RealTotalCost = None
        self._OriginalTotalCost = None

    @property
    def RealTotalCost(self):
        """实付金额（单位：分）
        :rtype: int
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def OriginalTotalCost(self):
        """原始金额（不含折扣，单位：分）
        :rtype: int
        """
        return self._OriginalTotalCost

    @OriginalTotalCost.setter
    def OriginalTotalCost(self, OriginalTotalCost):
        self._OriginalTotalCost = OriginalTotalCost


    def _deserialize(self, params):
        self._RealTotalCost = params.get("RealTotalCost")
        self._OriginalTotalCost = params.get("OriginalTotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentAuditedClientsRequest(AbstractModel):
    """DescribeAgentAuditedClients请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUin: 客户账号ID
        :type ClientUin: str
        :param _ClientName: 客户名称。由于涉及隐私，名称打码显示，故名称仅支持打码后的模糊搜索
        :type ClientName: str
        :param _ClientFlag: 客户类型，a/b，类型定义参考代理商相关政策文档
        :type ClientFlag: str
        :param _OrderDirection: ASC/DESC， 不区分大小写，按审核通过时间排序
        :type OrderDirection: str
        :param _ClientUins: 客户账号ID列表
        :type ClientUins: list of str
        :param _HasOverdueBill: 是否欠费。0：不欠费；1：欠费
        :type HasOverdueBill: int
        :param _ClientRemark: 客户备注
        :type ClientRemark: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _ClientType: 可以为new(自拓)/assign(指派)/old(官网)/direct(直销)/direct_newopp(直销(新商机))/空
        :type ClientType: str
        :param _ProjectType: 项目类型：可以为self(自拓项目)/platform(合作项目)/repeat(复算项目  )/空
        :type ProjectType: str
        :param _SalesUin: 业务员ID
        :type SalesUin: str
        :param _SalesName: 业务员姓名（模糊查询）
        :type SalesName: str
        """
        self._ClientUin = None
        self._ClientName = None
        self._ClientFlag = None
        self._OrderDirection = None
        self._ClientUins = None
        self._HasOverdueBill = None
        self._ClientRemark = None
        self._Offset = None
        self._Limit = None
        self._ClientType = None
        self._ProjectType = None
        self._SalesUin = None
        self._SalesName = None

    @property
    def ClientUin(self):
        """客户账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def ClientName(self):
        """客户名称。由于涉及隐私，名称打码显示，故名称仅支持打码后的模糊搜索
        :rtype: str
        """
        return self._ClientName

    @ClientName.setter
    def ClientName(self, ClientName):
        self._ClientName = ClientName

    @property
    def ClientFlag(self):
        """客户类型，a/b，类型定义参考代理商相关政策文档
        :rtype: str
        """
        return self._ClientFlag

    @ClientFlag.setter
    def ClientFlag(self, ClientFlag):
        self._ClientFlag = ClientFlag

    @property
    def OrderDirection(self):
        """ASC/DESC， 不区分大小写，按审核通过时间排序
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def ClientUins(self):
        """客户账号ID列表
        :rtype: list of str
        """
        return self._ClientUins

    @ClientUins.setter
    def ClientUins(self, ClientUins):
        self._ClientUins = ClientUins

    @property
    def HasOverdueBill(self):
        """是否欠费。0：不欠费；1：欠费
        :rtype: int
        """
        return self._HasOverdueBill

    @HasOverdueBill.setter
    def HasOverdueBill(self, HasOverdueBill):
        self._HasOverdueBill = HasOverdueBill

    @property
    def ClientRemark(self):
        """客户备注
        :rtype: str
        """
        return self._ClientRemark

    @ClientRemark.setter
    def ClientRemark(self, ClientRemark):
        self._ClientRemark = ClientRemark

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
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ClientType(self):
        """可以为new(自拓)/assign(指派)/old(官网)/direct(直销)/direct_newopp(直销(新商机))/空
        :rtype: str
        """
        return self._ClientType

    @ClientType.setter
    def ClientType(self, ClientType):
        self._ClientType = ClientType

    @property
    def ProjectType(self):
        """项目类型：可以为self(自拓项目)/platform(合作项目)/repeat(复算项目  )/空
        :rtype: str
        """
        return self._ProjectType

    @ProjectType.setter
    def ProjectType(self, ProjectType):
        self._ProjectType = ProjectType

    @property
    def SalesUin(self):
        """业务员ID
        :rtype: str
        """
        return self._SalesUin

    @SalesUin.setter
    def SalesUin(self, SalesUin):
        self._SalesUin = SalesUin

    @property
    def SalesName(self):
        """业务员姓名（模糊查询）
        :rtype: str
        """
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._ClientName = params.get("ClientName")
        self._ClientFlag = params.get("ClientFlag")
        self._OrderDirection = params.get("OrderDirection")
        self._ClientUins = params.get("ClientUins")
        self._HasOverdueBill = params.get("HasOverdueBill")
        self._ClientRemark = params.get("ClientRemark")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClientType = params.get("ClientType")
        self._ProjectType = params.get("ProjectType")
        self._SalesUin = params.get("SalesUin")
        self._SalesName = params.get("SalesName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentAuditedClientsResponse(AbstractModel):
    """DescribeAgentAuditedClients返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentClientSet: 已审核代客列表
        :type AgentClientSet: list of AgentAuditedClient
        :param _TotalCount: 符合条件的代客总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentClientSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AgentClientSet(self):
        """已审核代客列表
        :rtype: list of AgentAuditedClient
        """
        return self._AgentClientSet

    @AgentClientSet.setter
    def AgentClientSet(self, AgentClientSet):
        self._AgentClientSet = AgentClientSet

    @property
    def TotalCount(self):
        """符合条件的代客总数
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
        if params.get("AgentClientSet") is not None:
            self._AgentClientSet = []
            for item in params.get("AgentClientSet"):
                obj = AgentAuditedClient()
                obj._deserialize(item)
                self._AgentClientSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAgentBillsRequest(AbstractModel):
    """DescribeAgentBills请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SettleMonth: 支付月份，如2018-02
        :type SettleMonth: str
        :param _ClientUin: 客户账号ID
        :type ClientUin: str
        :param _PayMode: 支付方式，prepay/postpay
        :type PayMode: str
        :param _OrderId: 预付费订单号
        :type OrderId: str
        :param _ClientRemark: 客户备注名称
        :type ClientRemark: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        """
        self._SettleMonth = None
        self._ClientUin = None
        self._PayMode = None
        self._OrderId = None
        self._ClientRemark = None
        self._Offset = None
        self._Limit = None

    @property
    def SettleMonth(self):
        """支付月份，如2018-02
        :rtype: str
        """
        return self._SettleMonth

    @SettleMonth.setter
    def SettleMonth(self, SettleMonth):
        self._SettleMonth = SettleMonth

    @property
    def ClientUin(self):
        """客户账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def PayMode(self):
        """支付方式，prepay/postpay
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def OrderId(self):
        """预付费订单号
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ClientRemark(self):
        """客户备注名称
        :rtype: str
        """
        return self._ClientRemark

    @ClientRemark.setter
    def ClientRemark(self, ClientRemark):
        self._ClientRemark = ClientRemark

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
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SettleMonth = params.get("SettleMonth")
        self._ClientUin = params.get("ClientUin")
        self._PayMode = params.get("PayMode")
        self._OrderId = params.get("OrderId")
        self._ClientRemark = params.get("ClientRemark")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentBillsResponse(AbstractModel):
    """DescribeAgentBills返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件列表总数量
        :type TotalCount: int
        :param _AgentBillSet: 业务明细列表
        :type AgentBillSet: list of AgentBillElem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AgentBillSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合查询条件列表总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AgentBillSet(self):
        """业务明细列表
        :rtype: list of AgentBillElem
        """
        return self._AgentBillSet

    @AgentBillSet.setter
    def AgentBillSet(self, AgentBillSet):
        self._AgentBillSet = AgentBillSet

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
        if params.get("AgentBillSet") is not None:
            self._AgentBillSet = []
            for item in params.get("AgentBillSet"):
                obj = AgentBillElem()
                obj._deserialize(item)
                self._AgentBillSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAgentClientGradeRequest(AbstractModel):
    """DescribeAgentClientGrade请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUin: 代客uin
        :type ClientUin: str
        """
        self._ClientUin = None

    @property
    def ClientUin(self):
        """代客uin
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentClientGradeResponse(AbstractModel):
    """DescribeAgentClientGrade返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditStatus: 审核状态：0待审核，1，已审核
        :type AuditStatus: int
        :param _AuthState: 实名认证状态：0，未实名认证，1实名认证
        :type AuthState: int
        :param _ClientGrade: 客户级别
        :type ClientGrade: str
        :param _ClientType: 客户类型：1，个人；2，企业；3，其他
        :type ClientType: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuditStatus = None
        self._AuthState = None
        self._ClientGrade = None
        self._ClientType = None
        self._RequestId = None

    @property
    def AuditStatus(self):
        """审核状态：0待审核，1，已审核
        :rtype: int
        """
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus

    @property
    def AuthState(self):
        """实名认证状态：0，未实名认证，1实名认证
        :rtype: int
        """
        return self._AuthState

    @AuthState.setter
    def AuthState(self, AuthState):
        self._AuthState = AuthState

    @property
    def ClientGrade(self):
        """客户级别
        :rtype: str
        """
        return self._ClientGrade

    @ClientGrade.setter
    def ClientGrade(self, ClientGrade):
        self._ClientGrade = ClientGrade

    @property
    def ClientType(self):
        """客户类型：1，个人；2，企业；3，其他
        :rtype: int
        """
        return self._ClientType

    @ClientType.setter
    def ClientType(self, ClientType):
        self._ClientType = ClientType

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
        self._AuditStatus = params.get("AuditStatus")
        self._AuthState = params.get("AuthState")
        self._ClientGrade = params.get("ClientGrade")
        self._ClientType = params.get("ClientType")
        self._RequestId = params.get("RequestId")


class DescribeAgentClientsRequest(AbstractModel):
    """DescribeAgentClients请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUin: 客户账号ID
        :type ClientUin: str
        :param _ClientName: 客户名称。由于涉及隐私，名称打码显示，故名称仅支持打码后的模糊搜索
        :type ClientName: str
        :param _ClientFlag: 客户类型，a/b，类型定义参考代理商相关政策文档
        :type ClientFlag: str
        :param _OrderDirection: ASC/DESC， 不区分大小写，按申请时间排序
        :type OrderDirection: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _SalesUin: 业务员ID
        :type SalesUin: str
        :param _SalesName: 业务员姓名（模糊查询）
        :type SalesName: str
        """
        self._ClientUin = None
        self._ClientName = None
        self._ClientFlag = None
        self._OrderDirection = None
        self._Offset = None
        self._Limit = None
        self._SalesUin = None
        self._SalesName = None

    @property
    def ClientUin(self):
        """客户账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def ClientName(self):
        """客户名称。由于涉及隐私，名称打码显示，故名称仅支持打码后的模糊搜索
        :rtype: str
        """
        return self._ClientName

    @ClientName.setter
    def ClientName(self, ClientName):
        self._ClientName = ClientName

    @property
    def ClientFlag(self):
        """客户类型，a/b，类型定义参考代理商相关政策文档
        :rtype: str
        """
        return self._ClientFlag

    @ClientFlag.setter
    def ClientFlag(self, ClientFlag):
        self._ClientFlag = ClientFlag

    @property
    def OrderDirection(self):
        """ASC/DESC， 不区分大小写，按申请时间排序
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

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
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SalesUin(self):
        """业务员ID
        :rtype: str
        """
        return self._SalesUin

    @SalesUin.setter
    def SalesUin(self, SalesUin):
        self._SalesUin = SalesUin

    @property
    def SalesName(self):
        """业务员姓名（模糊查询）
        :rtype: str
        """
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._ClientName = params.get("ClientName")
        self._ClientFlag = params.get("ClientFlag")
        self._OrderDirection = params.get("OrderDirection")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SalesUin = params.get("SalesUin")
        self._SalesName = params.get("SalesName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentClientsResponse(AbstractModel):
    """DescribeAgentClients返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentClientSet: 待审核代客列表
        :type AgentClientSet: list of AgentClientElem
        :param _TotalCount: 符合条件的代客总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentClientSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AgentClientSet(self):
        """待审核代客列表
        :rtype: list of AgentClientElem
        """
        return self._AgentClientSet

    @AgentClientSet.setter
    def AgentClientSet(self, AgentClientSet):
        self._AgentClientSet = AgentClientSet

    @property
    def TotalCount(self):
        """符合条件的代客总数
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
        if params.get("AgentClientSet") is not None:
            self._AgentClientSet = []
            for item in params.get("AgentClientSet"):
                obj = AgentClientElem()
                obj._deserialize(item)
                self._AgentClientSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAgentDealsByCacheRequest(AbstractModel):
    """DescribeAgentDealsByCache请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目 最大200
        :type Limit: int
        :param _CreatTimeRangeStart: 下单时间范围起始点【请保持时间范围最大90天】
        :type CreatTimeRangeStart: str
        :param _CreatTimeRangeEnd: 下单时间范围终止点【请保持时间范围最大90天】
        :type CreatTimeRangeEnd: str
        :param _Order: 0:下单时间降序；其他：下单时间升序
        :type Order: int
        :param _Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)
        :type Status: int
        :param _OwnerUins: 下单人账号ID列表
        :type OwnerUins: list of str
        :param _DealNames: 子订单号列表
        :type DealNames: list of str
        :param _BigDealIds: 大订单号列表
        :type BigDealIds: list of str
        :param _PayerMode: 支付方式，0：自付；1：代付
        :type PayerMode: int
        """
        self._Offset = None
        self._Limit = None
        self._CreatTimeRangeStart = None
        self._CreatTimeRangeEnd = None
        self._Order = None
        self._Status = None
        self._OwnerUins = None
        self._DealNames = None
        self._BigDealIds = None
        self._PayerMode = None

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
    def Limit(self):
        """限制数目 最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CreatTimeRangeStart(self):
        """下单时间范围起始点【请保持时间范围最大90天】
        :rtype: str
        """
        return self._CreatTimeRangeStart

    @CreatTimeRangeStart.setter
    def CreatTimeRangeStart(self, CreatTimeRangeStart):
        self._CreatTimeRangeStart = CreatTimeRangeStart

    @property
    def CreatTimeRangeEnd(self):
        """下单时间范围终止点【请保持时间范围最大90天】
        :rtype: str
        """
        return self._CreatTimeRangeEnd

    @CreatTimeRangeEnd.setter
    def CreatTimeRangeEnd(self, CreatTimeRangeEnd):
        self._CreatTimeRangeEnd = CreatTimeRangeEnd

    @property
    def Order(self):
        """0:下单时间降序；其他：下单时间升序
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Status(self):
        """订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OwnerUins(self):
        """下单人账号ID列表
        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def DealNames(self):
        """子订单号列表
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def BigDealIds(self):
        """大订单号列表
        :rtype: list of str
        """
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def PayerMode(self):
        """支付方式，0：自付；1：代付
        :rtype: int
        """
        return self._PayerMode

    @PayerMode.setter
    def PayerMode(self, PayerMode):
        self._PayerMode = PayerMode


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CreatTimeRangeStart = params.get("CreatTimeRangeStart")
        self._CreatTimeRangeEnd = params.get("CreatTimeRangeEnd")
        self._Order = params.get("Order")
        self._Status = params.get("Status")
        self._OwnerUins = params.get("OwnerUins")
        self._DealNames = params.get("DealNames")
        self._BigDealIds = params.get("BigDealIds")
        self._PayerMode = params.get("PayerMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentDealsByCacheResponse(AbstractModel):
    """DescribeAgentDealsByCache返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentDealSet: 订单数组
        :type AgentDealSet: list of AgentDealNewElem
        :param _TotalCount: 符合条件的订单总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentDealSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AgentDealSet(self):
        """订单数组
        :rtype: list of AgentDealNewElem
        """
        return self._AgentDealSet

    @AgentDealSet.setter
    def AgentDealSet(self, AgentDealSet):
        self._AgentDealSet = AgentDealSet

    @property
    def TotalCount(self):
        """符合条件的订单总数量
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
        if params.get("AgentDealSet") is not None:
            self._AgentDealSet = []
            for item in params.get("AgentDealSet"):
                obj = AgentDealNewElem()
                obj._deserialize(item)
                self._AgentDealSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAgentPayDealsV2Request(AbstractModel):
    """DescribeAgentPayDealsV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目 最大100
        :type Limit: int
        :param _CreatTimeRangeStart: 下单时间范围起始点(不传时会默认查15天内订单，传值时需要传15天内的起始时间)
        :type CreatTimeRangeStart: str
        :param _CreatTimeRangeEnd: 下单时间范围终止点
        :type CreatTimeRangeEnd: str
        :param _Order: 0:下单时间降序；其他：下单时间升序
        :type Order: int
        :param _Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)
        :type Status: int
        :param _OwnerUins: 下单人账号ID列表
        :type OwnerUins: list of str
        :param _DealNames: 子订单号列表
        :type DealNames: list of str
        :param _BigDealIds: 大订单号列表
        :type BigDealIds: list of str
        """
        self._Offset = None
        self._Limit = None
        self._CreatTimeRangeStart = None
        self._CreatTimeRangeEnd = None
        self._Order = None
        self._Status = None
        self._OwnerUins = None
        self._DealNames = None
        self._BigDealIds = None

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
    def Limit(self):
        """限制数目 最大100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CreatTimeRangeStart(self):
        """下单时间范围起始点(不传时会默认查15天内订单，传值时需要传15天内的起始时间)
        :rtype: str
        """
        return self._CreatTimeRangeStart

    @CreatTimeRangeStart.setter
    def CreatTimeRangeStart(self, CreatTimeRangeStart):
        self._CreatTimeRangeStart = CreatTimeRangeStart

    @property
    def CreatTimeRangeEnd(self):
        """下单时间范围终止点
        :rtype: str
        """
        return self._CreatTimeRangeEnd

    @CreatTimeRangeEnd.setter
    def CreatTimeRangeEnd(self, CreatTimeRangeEnd):
        self._CreatTimeRangeEnd = CreatTimeRangeEnd

    @property
    def Order(self):
        """0:下单时间降序；其他：下单时间升序
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Status(self):
        """订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OwnerUins(self):
        """下单人账号ID列表
        :rtype: list of str
        """
        return self._OwnerUins

    @OwnerUins.setter
    def OwnerUins(self, OwnerUins):
        self._OwnerUins = OwnerUins

    @property
    def DealNames(self):
        """子订单号列表
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def BigDealIds(self):
        """大订单号列表
        :rtype: list of str
        """
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CreatTimeRangeStart = params.get("CreatTimeRangeStart")
        self._CreatTimeRangeEnd = params.get("CreatTimeRangeEnd")
        self._Order = params.get("Order")
        self._Status = params.get("Status")
        self._OwnerUins = params.get("OwnerUins")
        self._DealNames = params.get("DealNames")
        self._BigDealIds = params.get("BigDealIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentPayDealsV2Response(AbstractModel):
    """DescribeAgentPayDealsV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentPayDealSet: 订单数组
        :type AgentPayDealSet: list of AgentDealNewElem
        :param _TotalCount: 符合条件的订单总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentPayDealSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AgentPayDealSet(self):
        """订单数组
        :rtype: list of AgentDealNewElem
        """
        return self._AgentPayDealSet

    @AgentPayDealSet.setter
    def AgentPayDealSet(self, AgentPayDealSet):
        self._AgentPayDealSet = AgentPayDealSet

    @property
    def TotalCount(self):
        """符合条件的订单总数量
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
        if params.get("AgentPayDealSet") is not None:
            self._AgentPayDealSet = []
            for item in params.get("AgentPayDealSet"):
                obj = AgentDealNewElem()
                obj._deserialize(item)
                self._AgentPayDealSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAgentRelateBigDealIdsRequest(AbstractModel):
    """DescribeAgentRelateBigDealIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BigDealId: 大订单号
        :type BigDealId: str
        """
        self._BigDealId = None

    @property
    def BigDealId(self):
        """大订单号
        :rtype: str
        """
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId


    def _deserialize(self, params):
        self._BigDealId = params.get("BigDealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentRelateBigDealIdsResponse(AbstractModel):
    """DescribeAgentRelateBigDealIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BigDealIdList: 申请合并支付的关联大订单号列表（不包含请求的订单号）
        :type BigDealIdList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BigDealIdList = None
        self._RequestId = None

    @property
    def BigDealIdList(self):
        """申请合并支付的关联大订单号列表（不包含请求的订单号）
        :rtype: list of str
        """
        return self._BigDealIdList

    @BigDealIdList.setter
    def BigDealIdList(self, BigDealIdList):
        self._BigDealIdList = BigDealIdList

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
        self._BigDealIdList = params.get("BigDealIdList")
        self._RequestId = params.get("RequestId")


class DescribeAgentSelfPayDealsV2Request(AbstractModel):
    """DescribeAgentSelfPayDealsV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 下单人账号ID
        :type OwnerUin: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目 最大100
        :type Limit: int
        :param _CreatTimeRangeStart: 下单时间范围起始点(不传时会默认查15天内订单，传值时需要传15天内的起始时间)
        :type CreatTimeRangeStart: str
        :param _CreatTimeRangeEnd: 下单时间范围终止点
        :type CreatTimeRangeEnd: str
        :param _Order: 0:下单时间降序；其他：下单时间升序
        :type Order: int
        :param _Status: 订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)
        :type Status: int
        :param _DealNames: 子订单号列表
        :type DealNames: list of str
        :param _BigDealIds: 大订单号列表
        :type BigDealIds: list of str
        """
        self._OwnerUin = None
        self._Offset = None
        self._Limit = None
        self._CreatTimeRangeStart = None
        self._CreatTimeRangeEnd = None
        self._Order = None
        self._Status = None
        self._DealNames = None
        self._BigDealIds = None

    @property
    def OwnerUin(self):
        """下单人账号ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

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
    def Limit(self):
        """限制数目 最大100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CreatTimeRangeStart(self):
        """下单时间范围起始点(不传时会默认查15天内订单，传值时需要传15天内的起始时间)
        :rtype: str
        """
        return self._CreatTimeRangeStart

    @CreatTimeRangeStart.setter
    def CreatTimeRangeStart(self, CreatTimeRangeStart):
        self._CreatTimeRangeStart = CreatTimeRangeStart

    @property
    def CreatTimeRangeEnd(self):
        """下单时间范围终止点
        :rtype: str
        """
        return self._CreatTimeRangeEnd

    @CreatTimeRangeEnd.setter
    def CreatTimeRangeEnd(self, CreatTimeRangeEnd):
        self._CreatTimeRangeEnd = CreatTimeRangeEnd

    @property
    def Order(self):
        """0:下单时间降序；其他：下单时间升序
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Status(self):
        """订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DealNames(self):
        """子订单号列表
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def BigDealIds(self):
        """大订单号列表
        :rtype: list of str
        """
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CreatTimeRangeStart = params.get("CreatTimeRangeStart")
        self._CreatTimeRangeEnd = params.get("CreatTimeRangeEnd")
        self._Order = params.get("Order")
        self._Status = params.get("Status")
        self._DealNames = params.get("DealNames")
        self._BigDealIds = params.get("BigDealIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentSelfPayDealsV2Response(AbstractModel):
    """DescribeAgentSelfPayDealsV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentPayDealSet: 订单数组
        :type AgentPayDealSet: list of AgentDealNewElem
        :param _TotalCount: 符合条件的订单总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentPayDealSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AgentPayDealSet(self):
        """订单数组
        :rtype: list of AgentDealNewElem
        """
        return self._AgentPayDealSet

    @AgentPayDealSet.setter
    def AgentPayDealSet(self, AgentPayDealSet):
        self._AgentPayDealSet = AgentPayDealSet

    @property
    def TotalCount(self):
        """符合条件的订单总数量
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
        if params.get("AgentPayDealSet") is not None:
            self._AgentPayDealSet = []
            for item in params.get("AgentPayDealSet"):
                obj = AgentDealNewElem()
                obj._deserialize(item)
                self._AgentPayDealSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClientBalanceNewRequest(AbstractModel):
    """DescribeClientBalanceNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUin: 客户(代客)账号ID
        :type ClientUin: str
        """
        self._ClientUin = None

    @property
    def ClientUin(self):
        """客户(代客)账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientBalanceNewResponse(AbstractModel):
    """DescribeClientBalanceNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Balance: 账户可用余额，单位分 （可用余额 = 现金余额 + 赠送金余额 - 欠费金额 - 冻结金额）
        :type Balance: int
        :param _Cash: 账户现金余额，单位分
        :type Cash: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Balance = None
        self._Cash = None
        self._RequestId = None

    @property
    def Balance(self):
        """账户可用余额，单位分 （可用余额 = 现金余额 + 赠送金余额 - 欠费金额 - 冻结金额）
        :rtype: int
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def Cash(self):
        """账户现金余额，单位分
        :rtype: int
        """
        return self._Cash

    @Cash.setter
    def Cash(self, Cash):
        self._Cash = Cash

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
        self._Cash = params.get("Cash")
        self._RequestId = params.get("RequestId")


class DescribeClientJoinIncreaseListRequest(AbstractModel):
    """DescribeClientJoinIncreaseList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUins: 客户UIN列表
        :type ClientUins: list of str
        """
        self._ClientUins = None

    @property
    def ClientUins(self):
        """客户UIN列表
        :rtype: list of str
        """
        return self._ClientUins

    @ClientUins.setter
    def ClientUins(self, ClientUins):
        self._ClientUins = ClientUins


    def _deserialize(self, params):
        self._ClientUins = params.get("ClientUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientJoinIncreaseListResponse(AbstractModel):
    """DescribeClientJoinIncreaseList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 已审核代客列表
        :type List: list of ClientIncreaseInfoList
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """已审核代客列表
        :rtype: list of ClientIncreaseInfoList
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ClientIncreaseInfoList()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClientSwitchTraTaskInfoRequest(AbstractModel):
    """DescribeClientSwitchTraTaskInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUin: 代客UIN
        :type ClientUin: str
        :param _SwitchType: 1：代理，2：代采
        :type SwitchType: int
        """
        self._ClientUin = None
        self._SwitchType = None

    @property
    def ClientUin(self):
        """代客UIN
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def SwitchType(self):
        """1：代理，2：代采
        :rtype: int
        """
        return self._SwitchType

    @SwitchType.setter
    def SwitchType(self, SwitchType):
        self._SwitchType = SwitchType


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._SwitchType = params.get("SwitchType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientSwitchTraTaskInfoResponse(AbstractModel):
    """DescribeClientSwitchTraTaskInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUin: 客户UIN
        :type ClientUin: str
        :param _SwitchType: 切换类型：代理,代采
        :type SwitchType: str
        :param _Result: ok，符合，fail，不符合
        :type Result: str
        :param _SwitchUrl: 切换链接
        :type SwitchUrl: str
        :param _ResultMsg: 不符合的原因
        :type ResultMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClientUin = None
        self._SwitchType = None
        self._Result = None
        self._SwitchUrl = None
        self._ResultMsg = None
        self._RequestId = None

    @property
    def ClientUin(self):
        """客户UIN
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def SwitchType(self):
        """切换类型：代理,代采
        :rtype: str
        """
        return self._SwitchType

    @SwitchType.setter
    def SwitchType(self, SwitchType):
        self._SwitchType = SwitchType

    @property
    def Result(self):
        """ok，符合，fail，不符合
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def SwitchUrl(self):
        """切换链接
        :rtype: str
        """
        return self._SwitchUrl

    @SwitchUrl.setter
    def SwitchUrl(self, SwitchUrl):
        self._SwitchUrl = SwitchUrl

    @property
    def ResultMsg(self):
        """不符合的原因
        :rtype: str
        """
        return self._ResultMsg

    @ResultMsg.setter
    def ResultMsg(self, ResultMsg):
        self._ResultMsg = ResultMsg

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
        self._ClientUin = params.get("ClientUin")
        self._SwitchType = params.get("SwitchType")
        self._Result = params.get("Result")
        self._SwitchUrl = params.get("SwitchUrl")
        self._ResultMsg = params.get("ResultMsg")
        self._RequestId = params.get("RequestId")


class DescribeRebateInfosNewRequest(AbstractModel):
    """DescribeRebateInfosNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RebateMonth: 返佣月份，如2018-02
        :type RebateMonth: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        """
        self._RebateMonth = None
        self._Offset = None
        self._Limit = None

    @property
    def RebateMonth(self):
        """返佣月份，如2018-02
        :rtype: str
        """
        return self._RebateMonth

    @RebateMonth.setter
    def RebateMonth(self, RebateMonth):
        self._RebateMonth = RebateMonth

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
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RebateMonth = params.get("RebateMonth")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRebateInfosNewResponse(AbstractModel):
    """DescribeRebateInfosNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RebateInfoSet: 返佣信息列表
        :type RebateInfoSet: list of RebateInfoElemNew
        :param _TotalCount: 符合查询条件返佣信息数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RebateInfoSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RebateInfoSet(self):
        """返佣信息列表
        :rtype: list of RebateInfoElemNew
        """
        return self._RebateInfoSet

    @RebateInfoSet.setter
    def RebateInfoSet(self, RebateInfoSet):
        self._RebateInfoSet = RebateInfoSet

    @property
    def TotalCount(self):
        """符合查询条件返佣信息数目
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
        if params.get("RebateInfoSet") is not None:
            self._RebateInfoSet = []
            for item in params.get("RebateInfoSet"):
                obj = RebateInfoElemNew()
                obj._deserialize(item)
                self._RebateInfoSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRebateInfosRequest(AbstractModel):
    """DescribeRebateInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RebateMonth: 返佣月份，如2018-02
        :type RebateMonth: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        """
        self._RebateMonth = None
        self._Offset = None
        self._Limit = None

    @property
    def RebateMonth(self):
        """返佣月份，如2018-02
        :rtype: str
        """
        return self._RebateMonth

    @RebateMonth.setter
    def RebateMonth(self, RebateMonth):
        self._RebateMonth = RebateMonth

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
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RebateMonth = params.get("RebateMonth")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRebateInfosResponse(AbstractModel):
    """DescribeRebateInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RebateInfoSet: 返佣信息列表
        :type RebateInfoSet: list of RebateInfoElem
        :param _TotalCount: 符合查询条件返佣信息数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RebateInfoSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RebateInfoSet(self):
        """返佣信息列表
        :rtype: list of RebateInfoElem
        """
        return self._RebateInfoSet

    @RebateInfoSet.setter
    def RebateInfoSet(self, RebateInfoSet):
        self._RebateInfoSet = RebateInfoSet

    @property
    def TotalCount(self):
        """符合查询条件返佣信息数目
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
        if params.get("RebateInfoSet") is not None:
            self._RebateInfoSet = []
            for item in params.get("RebateInfoSet"):
                obj = RebateInfoElem()
                obj._deserialize(item)
                self._RebateInfoSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSalesmansRequest(AbstractModel):
    """DescribeSalesmans请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _SalesName: 业务员姓名(模糊查询)
        :type SalesName: str
        :param _SalesUin: 业务员ID
        :type SalesUin: str
        :param _OrderDirection: ASC/DESC， 不区分大小写，按创建通过时间排序
        :type OrderDirection: str
        """
        self._Offset = None
        self._Limit = None
        self._SalesName = None
        self._SalesUin = None
        self._OrderDirection = None

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
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SalesName(self):
        """业务员姓名(模糊查询)
        :rtype: str
        """
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName

    @property
    def SalesUin(self):
        """业务员ID
        :rtype: str
        """
        return self._SalesUin

    @SalesUin.setter
    def SalesUin(self, SalesUin):
        self._SalesUin = SalesUin

    @property
    def OrderDirection(self):
        """ASC/DESC， 不区分大小写，按创建通过时间排序
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SalesName = params.get("SalesName")
        self._SalesUin = params.get("SalesUin")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSalesmansResponse(AbstractModel):
    """DescribeSalesmans返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentSalesmanSet: 业务员列表
        :type AgentSalesmanSet: list of AgentSalesmanElem
        :param _TotalCount: 符合条件的代客总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentSalesmanSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AgentSalesmanSet(self):
        """业务员列表
        :rtype: list of AgentSalesmanElem
        """
        return self._AgentSalesmanSet

    @AgentSalesmanSet.setter
    def AgentSalesmanSet(self, AgentSalesmanSet):
        self._AgentSalesmanSet = AgentSalesmanSet

    @property
    def TotalCount(self):
        """符合条件的代客总数
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
        if params.get("AgentSalesmanSet") is not None:
            self._AgentSalesmanSet = []
            for item in params.get("AgentSalesmanSet"):
                obj = AgentSalesmanElem()
                obj._deserialize(item)
                self._AgentSalesmanSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUnbindClientListRequest(AbstractModel):
    """DescribeUnbindClientList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 解绑状态：0:所有,1:审核中,2已解绑
        :type Status: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _UnbindUin: 解绑账号ID
        :type UnbindUin: str
        :param _ApplyTimeStart: 解绑申请时间范围起始点
        :type ApplyTimeStart: str
        :param _ApplyTimeEnd: 解绑申请时间范围终止点
        :type ApplyTimeEnd: str
        :param _OrderDirection: 对申请时间的升序降序，值：asc，desc
        :type OrderDirection: str
        """
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._UnbindUin = None
        self._ApplyTimeStart = None
        self._ApplyTimeEnd = None
        self._OrderDirection = None

    @property
    def Status(self):
        """解绑状态：0:所有,1:审核中,2已解绑
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def UnbindUin(self):
        """解绑账号ID
        :rtype: str
        """
        return self._UnbindUin

    @UnbindUin.setter
    def UnbindUin(self, UnbindUin):
        self._UnbindUin = UnbindUin

    @property
    def ApplyTimeStart(self):
        """解绑申请时间范围起始点
        :rtype: str
        """
        return self._ApplyTimeStart

    @ApplyTimeStart.setter
    def ApplyTimeStart(self, ApplyTimeStart):
        self._ApplyTimeStart = ApplyTimeStart

    @property
    def ApplyTimeEnd(self):
        """解绑申请时间范围终止点
        :rtype: str
        """
        return self._ApplyTimeEnd

    @ApplyTimeEnd.setter
    def ApplyTimeEnd(self, ApplyTimeEnd):
        self._ApplyTimeEnd = ApplyTimeEnd

    @property
    def OrderDirection(self):
        """对申请时间的升序降序，值：asc，desc
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._UnbindUin = params.get("UnbindUin")
        self._ApplyTimeStart = params.get("ApplyTimeStart")
        self._ApplyTimeEnd = params.get("ApplyTimeEnd")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnbindClientListResponse(AbstractModel):
    """DescribeUnbindClientList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的解绑客户数量
        :type TotalCount: int
        :param _UnbindClientList: 符合条件的解绑客户列表
        :type UnbindClientList: list of UnbindClientElem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UnbindClientList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的解绑客户数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UnbindClientList(self):
        """符合条件的解绑客户列表
        :rtype: list of UnbindClientElem
        """
        return self._UnbindClientList

    @UnbindClientList.setter
    def UnbindClientList(self, UnbindClientList):
        self._UnbindClientList = UnbindClientList

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
        if params.get("UnbindClientList") is not None:
            self._UnbindClientList = []
            for item in params.get("UnbindClientList"):
                obj = UnbindClientElem()
                obj._deserialize(item)
                self._UnbindClientList.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyClientRemarkRequest(AbstractModel):
    """ModifyClientRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientRemark: 客户备注名称
        :type ClientRemark: str
        :param _ClientUin: 客户账号ID
        :type ClientUin: str
        """
        self._ClientRemark = None
        self._ClientUin = None

    @property
    def ClientRemark(self):
        """客户备注名称
        :rtype: str
        """
        return self._ClientRemark

    @ClientRemark.setter
    def ClientRemark(self, ClientRemark):
        self._ClientRemark = ClientRemark

    @property
    def ClientUin(self):
        """客户账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin


    def _deserialize(self, params):
        self._ClientRemark = params.get("ClientRemark")
        self._ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClientRemarkResponse(AbstractModel):
    """ModifyClientRemark返回参数结构体

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


class ProductInfoElem(AbstractModel):
    """产品详情

    """

    def __init__(self):
        r"""
        :param _Name: 产品属性
        :type Name: str
        :param _Value: 产品属性值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """产品属性
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """产品属性值
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
        


class RebateInfoElem(AbstractModel):
    """返佣信息定义

    """

    def __init__(self):
        r"""
        :param _Uin: 代理商账号ID
        :type Uin: str
        :param _RebateMonth: 返佣月份，如2018-02
        :type RebateMonth: str
        :param _Amt: 返佣金额，单位分
        :type Amt: int
        :param _MonthSales: 月度业绩，单位分
        :type MonthSales: int
        :param _QuarterSales: 季度业绩，单位分
        :type QuarterSales: int
        :param _ExceptionFlag: NORMAL(正常)/HAS_OVERDUE_BILL(欠费)/NO_CONTRACT(缺合同)
        :type ExceptionFlag: str
        """
        self._Uin = None
        self._RebateMonth = None
        self._Amt = None
        self._MonthSales = None
        self._QuarterSales = None
        self._ExceptionFlag = None

    @property
    def Uin(self):
        """代理商账号ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RebateMonth(self):
        """返佣月份，如2018-02
        :rtype: str
        """
        return self._RebateMonth

    @RebateMonth.setter
    def RebateMonth(self, RebateMonth):
        self._RebateMonth = RebateMonth

    @property
    def Amt(self):
        """返佣金额，单位分
        :rtype: int
        """
        return self._Amt

    @Amt.setter
    def Amt(self, Amt):
        self._Amt = Amt

    @property
    def MonthSales(self):
        """月度业绩，单位分
        :rtype: int
        """
        return self._MonthSales

    @MonthSales.setter
    def MonthSales(self, MonthSales):
        self._MonthSales = MonthSales

    @property
    def QuarterSales(self):
        """季度业绩，单位分
        :rtype: int
        """
        return self._QuarterSales

    @QuarterSales.setter
    def QuarterSales(self, QuarterSales):
        self._QuarterSales = QuarterSales

    @property
    def ExceptionFlag(self):
        """NORMAL(正常)/HAS_OVERDUE_BILL(欠费)/NO_CONTRACT(缺合同)
        :rtype: str
        """
        return self._ExceptionFlag

    @ExceptionFlag.setter
    def ExceptionFlag(self, ExceptionFlag):
        self._ExceptionFlag = ExceptionFlag


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._RebateMonth = params.get("RebateMonth")
        self._Amt = params.get("Amt")
        self._MonthSales = params.get("MonthSales")
        self._QuarterSales = params.get("QuarterSales")
        self._ExceptionFlag = params.get("ExceptionFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebateInfoElemNew(AbstractModel):
    """返佣信息定义

    """

    def __init__(self):
        r"""
        :param _Uin: 代理商账号ID
        :type Uin: str
        :param _RebateMonth: 返佣月份，如2018-02
        :type RebateMonth: str
        :param _Amt: 返佣金额，单位分
        :type Amt: int
        :param _MonthSales: 月度业绩，单位分
        :type MonthSales: int
        :param _QuarterSales: 季度业绩，单位分
        :type QuarterSales: int
        :param _ExceptionFlag: NORMAL(正常)/HAS_OVERDUE_BILL(欠费)/NO_CONTRACT(缺合同)
        :type ExceptionFlag: str
        """
        self._Uin = None
        self._RebateMonth = None
        self._Amt = None
        self._MonthSales = None
        self._QuarterSales = None
        self._ExceptionFlag = None

    @property
    def Uin(self):
        """代理商账号ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RebateMonth(self):
        """返佣月份，如2018-02
        :rtype: str
        """
        return self._RebateMonth

    @RebateMonth.setter
    def RebateMonth(self, RebateMonth):
        self._RebateMonth = RebateMonth

    @property
    def Amt(self):
        """返佣金额，单位分
        :rtype: int
        """
        return self._Amt

    @Amt.setter
    def Amt(self, Amt):
        self._Amt = Amt

    @property
    def MonthSales(self):
        """月度业绩，单位分
        :rtype: int
        """
        return self._MonthSales

    @MonthSales.setter
    def MonthSales(self, MonthSales):
        self._MonthSales = MonthSales

    @property
    def QuarterSales(self):
        """季度业绩，单位分
        :rtype: int
        """
        return self._QuarterSales

    @QuarterSales.setter
    def QuarterSales(self, QuarterSales):
        self._QuarterSales = QuarterSales

    @property
    def ExceptionFlag(self):
        """NORMAL(正常)/HAS_OVERDUE_BILL(欠费)/NO_CONTRACT(缺合同)
        :rtype: str
        """
        return self._ExceptionFlag

    @ExceptionFlag.setter
    def ExceptionFlag(self, ExceptionFlag):
        self._ExceptionFlag = ExceptionFlag


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._RebateMonth = params.get("RebateMonth")
        self._Amt = params.get("Amt")
        self._MonthSales = params.get("MonthSales")
        self._QuarterSales = params.get("QuarterSales")
        self._ExceptionFlag = params.get("ExceptionFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundMap(AbstractModel):
    """退款单关联的原始订单信息

    """

    def __init__(self):
        r"""
        :param _DealName: 退款单关联的原始子订单号
        :type DealName: str
        :param _RefundAmount: 退款金额，单位分
        :type RefundAmount: int
        """
        self._DealName = None
        self._RefundAmount = None

    @property
    def DealName(self):
        """退款单关联的原始子订单号
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RefundAmount(self):
        """退款金额，单位分
        :rtype: int
        """
        return self._RefundAmount

    @RefundAmount.setter
    def RefundAmount(self, RefundAmount):
        self._RefundAmount = RefundAmount


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RefundAmount = params.get("RefundAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemovePayRelationForClientRequest(AbstractModel):
    """RemovePayRelationForClient请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientUin: 客户账号ID
        :type ClientUin: str
        """
        self._ClientUin = None

    @property
    def ClientUin(self):
        """客户账号ID
        :rtype: str
        """
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemovePayRelationForClientResponse(AbstractModel):
    """RemovePayRelationForClient返回参数结构体

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


class UnbindClientElem(AbstractModel):
    """解绑客户信息

    """

    def __init__(self):
        r"""
        :param _Uin: 解绑账号ID
        :type Uin: str
        :param _Name: 名称
        :type Name: str
        :param _Status: 状态：0:审核中；1：已解绑；2：已撤销 3：关联撤销 4: 已驳回
        :type Status: int
        :param _ApplyTime: 申请时间
        :type ApplyTime: str
        :param _ActionTime: 解绑/撤销时间
        :type ActionTime: str
        """
        self._Uin = None
        self._Name = None
        self._Status = None
        self._ApplyTime = None
        self._ActionTime = None

    @property
    def Uin(self):
        """解绑账号ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """状态：0:审核中；1：已解绑；2：已撤销 3：关联撤销 4: 已驳回
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ApplyTime(self):
        """申请时间
        :rtype: str
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def ActionTime(self):
        """解绑/撤销时间
        :rtype: str
        """
        return self._ActionTime

    @ActionTime.setter
    def ActionTime(self, ActionTime):
        self._ActionTime = ActionTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._ApplyTime = params.get("ApplyTime")
        self._ActionTime = params.get("ActionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        