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


class Error(AbstractModel):
    """Error结构

    """

    def __init__(self):
        """
        :param Code: 一级错误描述
        :type Code: str
        :param Message: 二级错误描述
        :type Message: str
        """
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowProductRemindRequest(AbstractModel):
    """FlowProductRemind请求参数结构体

    """

    def __init__(self):
        """
        :param ProviderUin: 服务商uin
        :type ProviderUin: str
        :param SignId: 服务商实例ID
        :type SignId: str
        :param ResourceId: 云市场实例ID
        :type ResourceId: str
        :param TotalFlow: 实例总流量
        :type TotalFlow: str
        :param LeftFlow: 剩余流量
        :type LeftFlow: str
        :param FlowUnit: 流量单位
        :type FlowUnit: str
        """
        self.ProviderUin = None
        self.SignId = None
        self.ResourceId = None
        self.TotalFlow = None
        self.LeftFlow = None
        self.FlowUnit = None


    def _deserialize(self, params):
        self.ProviderUin = params.get("ProviderUin")
        self.SignId = params.get("SignId")
        self.ResourceId = params.get("ResourceId")
        self.TotalFlow = params.get("TotalFlow")
        self.LeftFlow = params.get("LeftFlow")
        self.FlowUnit = params.get("FlowUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowProductRemindResponse(AbstractModel):
    """FlowProductRemind返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 是否成功
        :type Success: str
        :param FlowId: 流水号
        :type FlowId: str
        :param Info: 消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.FlowId = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Success = params.get("Success")
        self.FlowId = params.get("FlowId")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class GetUsagePlanUsageAmountRequest(AbstractModel):
    """GetUsagePlanUsageAmount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 用于查询实例的Id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUsagePlanUsageAmountResponse(AbstractModel):
    """GetUsagePlanUsageAmount返回参数结构体

    """

    def __init__(self):
        """
        :param MaxRequestNum: 最大调用量
        :type MaxRequestNum: int
        :param InUseRequestNum: 已经调用量
        :type InUseRequestNum: int
        :param RemainingRequestNum: 剩余调用量
        :type RemainingRequestNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaxRequestNum = None
        self.InUseRequestNum = None
        self.RemainingRequestNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.InUseRequestNum = params.get("InUseRequestNum")
        self.RemainingRequestNum = params.get("RemainingRequestNum")
        self.RequestId = params.get("RequestId")


class OfflineProductDeal(AbstractModel):
    """线下产品订单

    """

    def __init__(self):
        """
        :param ProductCode: 产品标签
        :type ProductCode: str
        :param SubProductCode: 子产品标签
        :type SubProductCode: str
        :param BillingItemCode: 计费项
        :type BillingItemCode: str
        :param SubBillingItemCode: 计费细项
        :type SubBillingItemCode: str
        :param UnitPrice: 单价（单位：分）
        :type UnitPrice: float
        :param Dosage: 用量
        :type Dosage: float
        :param DosageUnit: 用量单位
        :type DosageUnit: str
        :param TimeSpan: 商品的时间大小，当TimeUnit 是package时，timeSpan 只能传1。当TimeUnit是year；month；day；hour；minute；second，传具体时长。
        :type TimeSpan: float
        :param TimeUnit: 商品的时间单位：year:年；month:月；day:日；hour:小时；minute:分钟；second:秒; package:与价格无关,一次性购买的产品传package
        :type TimeUnit: str
        :param OriginPrice: 原价 （单位：分）OriginPrice=round(UnitPrice * Dosage * TimeSpan)
        :type OriginPrice: int
        :param Discount: 折扣百分比，传入0-100的值
        :type Discount: float
        :param Fee: 最终扣费金额（单位：分）Fee=round(OriginPrice*Discount/100)
        :type Fee: int
        """
        self.ProductCode = None
        self.SubProductCode = None
        self.BillingItemCode = None
        self.SubBillingItemCode = None
        self.UnitPrice = None
        self.Dosage = None
        self.DosageUnit = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.OriginPrice = None
        self.Discount = None
        self.Fee = None


    def _deserialize(self, params):
        self.ProductCode = params.get("ProductCode")
        self.SubProductCode = params.get("SubProductCode")
        self.BillingItemCode = params.get("BillingItemCode")
        self.SubBillingItemCode = params.get("SubBillingItemCode")
        self.UnitPrice = params.get("UnitPrice")
        self.Dosage = params.get("Dosage")
        self.DosageUnit = params.get("DosageUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.OriginPrice = params.get("OriginPrice")
        self.Discount = params.get("Discount")
        self.Fee = params.get("Fee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncUserAndOrderInfoDetail(AbstractModel):
    """同步用户信息订单信息详情

    """

    def __init__(self):
        """
        :param TotalCount: 腾讯云订单总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param MarketOrders: 腾讯云订单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MarketOrders: list of str
        :param OwnerUin: 腾讯云用户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        """
        self.TotalCount = None
        self.MarketOrders = None
        self.OwnerUin = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.MarketOrders = params.get("MarketOrders")
        self.OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncUserAndOrderInfoRequest(AbstractModel):
    """SyncUserAndOrderInfo请求参数结构体

    """

    def __init__(self):
        """
        :param UserInfo: 企业微信用户信息
        :type UserInfo: :class:`tencentcloud.market.v20191010.models.WeChatUserInfo`
        :param OrderInfo: 企业微信订单信息
        :type OrderInfo: :class:`tencentcloud.market.v20191010.models.WeChatOrderInfo`
        """
        self.UserInfo = None
        self.OrderInfo = None


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self.UserInfo = WeChatUserInfo()
            self.UserInfo._deserialize(params.get("UserInfo"))
        if params.get("OrderInfo") is not None:
            self.OrderInfo = WeChatOrderInfo()
            self.OrderInfo._deserialize(params.get("OrderInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncUserAndOrderInfoResponse(AbstractModel):
    """SyncUserAndOrderInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Details: 同步用户信息订单信息详情
        :type Details: :class:`tencentcloud.market.v20191010.models.SyncUserAndOrderInfoDetail`
        :param Info: 返回信息 成功返回 0 success
        :type Info: :class:`tencentcloud.market.v20191010.models.Error`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Details = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self.Details = SyncUserAndOrderInfoDetail()
            self.Details._deserialize(params.get("Details"))
        if params.get("Info") is not None:
            self.Info = Error()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class WeChatOrderInfo(AbstractModel):
    """企业微信订单信息

    """

    def __init__(self):
        """
        :param OrderId: 企业微信订单号
        :type OrderId: str
        :param OrderStatus: 订单状态。0-未⽀支付，1-已⽀支付，2-已关闭， 3-未⽀支付且已过期， 4-申请退款中， 5-申请退款成功， 6-退款被拒绝
        :type OrderStatus: int
        :param OrderType: 订单类型。0-普通订单，1-扩容订单，2-续期，3-版本变更更
        :type OrderType: int
        :param SuiteId: 应⽤id
        :type SuiteId: str
        :param EditionId: 购买版本ID
        :type EditionId: str
        :param EditionName: 购买版本名称
        :type EditionName: str
        :param Price: 实付款金额，单位分
        :type Price: int
        :param OrderTime: 下单时间
        :type OrderTime: int
        :param PaidTime: 付款时间
        :type PaidTime: int
        :param Remark: 备注
        :type Remark: str
        :param UseBeginTime: 资源使用开始时间
        :type UseBeginTime: int
        :param UseEndTime: 资源使用结束时间
        :type UseEndTime: int
        :param Deals: 磐石详细的四层订单
        :type Deals: :class:`tencentcloud.market.v20191010.models.OfflineProductDeal`
        """
        self.OrderId = None
        self.OrderStatus = None
        self.OrderType = None
        self.SuiteId = None
        self.EditionId = None
        self.EditionName = None
        self.Price = None
        self.OrderTime = None
        self.PaidTime = None
        self.Remark = None
        self.UseBeginTime = None
        self.UseEndTime = None
        self.Deals = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.OrderStatus = params.get("OrderStatus")
        self.OrderType = params.get("OrderType")
        self.SuiteId = params.get("SuiteId")
        self.EditionId = params.get("EditionId")
        self.EditionName = params.get("EditionName")
        self.Price = params.get("Price")
        self.OrderTime = params.get("OrderTime")
        self.PaidTime = params.get("PaidTime")
        self.Remark = params.get("Remark")
        self.UseBeginTime = params.get("UseBeginTime")
        self.UseEndTime = params.get("UseEndTime")
        if params.get("Deals") is not None:
            self.Deals = OfflineProductDeal()
            self.Deals._deserialize(params.get("Deals"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeChatUserInfo(AbstractModel):
    """企业微信用户信息

    """

    def __init__(self):
        """
        :param PaidCorpId: 客户企业的corpid
        :type PaidCorpId: str
        :param PaidCorpName: 客户企业的Corp全称
        :type PaidCorpName: str
        """
        self.PaidCorpId = None
        self.PaidCorpName = None


    def _deserialize(self, params):
        self.PaidCorpId = params.get("PaidCorpId")
        self.PaidCorpName = params.get("PaidCorpName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        