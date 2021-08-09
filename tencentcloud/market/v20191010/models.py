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
        :param Code: 一级错误描述\n        :type Code: str\n        :param Message: 二级错误描述\n        :type Message: str\n        """
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
        :param ProviderUin: 服务商uin\n        :type ProviderUin: str\n        :param SignId: 服务商实例ID\n        :type SignId: str\n        :param ResourceId: 云市场实例ID\n        :type ResourceId: str\n        :param TotalFlow: 实例总流量\n        :type TotalFlow: str\n        :param LeftFlow: 剩余流量\n        :type LeftFlow: str\n        :param FlowUnit: 流量单位\n        :type FlowUnit: str\n        """
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
        :param Success: 是否成功\n        :type Success: str\n        :param FlowId: 流水号\n        :type FlowId: str\n        :param Info: 消息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Info: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 用于查询实例的Id\n        :type InstanceId: str\n        """
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
        :param MaxRequestNum: 最大调用量\n        :type MaxRequestNum: int\n        :param InUseRequestNum: 已经调用量\n        :type InUseRequestNum: int\n        :param RemainingRequestNum: 剩余调用量\n        :type RemainingRequestNum: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductCode: 产品标签\n        :type ProductCode: str\n        :param SubProductCode: 子产品标签\n        :type SubProductCode: str\n        :param BillingItemCode: 计费项\n        :type BillingItemCode: str\n        :param SubBillingItemCode: 计费细项\n        :type SubBillingItemCode: str\n        :param UnitPrice: 单价（单位：分）\n        :type UnitPrice: float\n        :param Dosage: 用量\n        :type Dosage: float\n        :param DosageUnit: 用量单位\n        :type DosageUnit: str\n        :param TimeSpan: 商品的时间大小，当TimeUnit 是package时，timeSpan 只能传1。当TimeUnit是year；month；day；hour；minute；second，传具体时长。\n        :type TimeSpan: float\n        :param TimeUnit: 商品的时间单位：year:年；month:月；day:日；hour:小时；minute:分钟；second:秒; package:与价格无关,一次性购买的产品传package\n        :type TimeUnit: str\n        :param OriginPrice: 原价 （单位：分）OriginPrice=round(UnitPrice * Dosage * TimeSpan)\n        :type OriginPrice: int\n        :param Discount: 折扣百分比，传入0-100的值\n        :type Discount: float\n        :param Fee: 最终扣费金额（单位：分）Fee=round(OriginPrice*Discount/100)\n        :type Fee: int\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param MarketOrders: 腾讯云订单列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type MarketOrders: list of str\n        :param OwnerUin: 腾讯云用户Uin
注意：此字段可能返回 null，表示取不到有效值。\n        :type OwnerUin: str\n        """
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
        :param UserInfo: 企业微信用户信息\n        :type UserInfo: :class:`tencentcloud.market.v20191010.models.WeChatUserInfo`\n        :param OrderInfo: 企业微信订单信息\n        :type OrderInfo: :class:`tencentcloud.market.v20191010.models.WeChatOrderInfo`\n        """
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
        :param Details: 同步用户信息订单信息详情\n        :type Details: :class:`tencentcloud.market.v20191010.models.SyncUserAndOrderInfoDetail`\n        :param Info: 返回信息 成功返回 0 success\n        :type Info: :class:`tencentcloud.market.v20191010.models.Error`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param OrderId: 企业微信订单号\n        :type OrderId: str\n        :param OrderStatus: 订单状态。0-未⽀支付，1-已⽀支付，2-已关闭， 3-未⽀支付且已过期， 4-申请退款中， 5-申请退款成功， 6-退款被拒绝\n        :type OrderStatus: int\n        :param OrderType: 订单类型。0-普通订单，1-扩容订单，2-续期，3-版本变更更\n        :type OrderType: int\n        :param SuiteId: 应⽤id\n        :type SuiteId: str\n        :param EditionId: 购买版本ID\n        :type EditionId: str\n        :param EditionName: 购买版本名称\n        :type EditionName: str\n        :param Price: 实付款金额，单位分\n        :type Price: int\n        :param OrderTime: 下单时间\n        :type OrderTime: int\n        :param PaidTime: 付款时间\n        :type PaidTime: int\n        :param Remark: 备注\n        :type Remark: str\n        :param UseBeginTime: 资源使用开始时间\n        :type UseBeginTime: int\n        :param UseEndTime: 资源使用结束时间\n        :type UseEndTime: int\n        :param Deals: 磐石详细的四层订单\n        :type Deals: :class:`tencentcloud.market.v20191010.models.OfflineProductDeal`\n        """
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
        :param PaidCorpId: 客户企业的corpid\n        :type PaidCorpId: str\n        :param PaidCorpName: 客户企业的Corp全称\n        :type PaidCorpName: str\n        """
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
        