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


class CreateSavingPlanOrderRequest(AbstractModel):
    """CreateSavingPlanOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域编码
        :type RegionId: int
        :param _ZoneId: 区域编码
        :type ZoneId: int
        :param _PrePayType: 预付费类型
        :type PrePayType: str
        :param _TimeSpan: 时长
        :type TimeSpan: int
        :param _TimeUnit: 时长单位
        :type TimeUnit: str
        :param _CommodityCode: 商品唯一标识
        :type CommodityCode: str
        :param _PromiseUseAmount: 承诺时长内的小额金额（单位：元）
        :type PromiseUseAmount: int
        :param _SpecifyEffectTime: 节省计划的指定生效时间，若不传则为当前下单时间。传参数格式:"2023-10-01 00:00:00"，仅支持指定日期的0点时刻
        :type SpecifyEffectTime: str
        :param _ClientToken: 可重入ID
        :type ClientToken: str
        """
        self._RegionId = None
        self._ZoneId = None
        self._PrePayType = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._CommodityCode = None
        self._PromiseUseAmount = None
        self._SpecifyEffectTime = None
        self._ClientToken = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PrePayType(self):
        return self._PrePayType

    @PrePayType.setter
    def PrePayType(self, PrePayType):
        self._PrePayType = PrePayType

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
    def CommodityCode(self):
        return self._CommodityCode

    @CommodityCode.setter
    def CommodityCode(self, CommodityCode):
        self._CommodityCode = CommodityCode

    @property
    def PromiseUseAmount(self):
        return self._PromiseUseAmount

    @PromiseUseAmount.setter
    def PromiseUseAmount(self, PromiseUseAmount):
        self._PromiseUseAmount = PromiseUseAmount

    @property
    def SpecifyEffectTime(self):
        return self._SpecifyEffectTime

    @SpecifyEffectTime.setter
    def SpecifyEffectTime(self, SpecifyEffectTime):
        self._SpecifyEffectTime = SpecifyEffectTime

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._PrePayType = params.get("PrePayType")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._CommodityCode = params.get("CommodityCode")
        self._PromiseUseAmount = params.get("PromiseUseAmount")
        self._SpecifyEffectTime = params.get("SpecifyEffectTime")
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSavingPlanOrderResponse(AbstractModel):
    """CreateSavingPlanOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BigDealId: 订单号
        :type BigDealId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BigDealId = None
        self._RequestId = None

    @property
    def BigDealId(self):
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BigDealId = params.get("BigDealId")
        self._RequestId = params.get("RequestId")


class DescribeSavingPlanDeductRequest(AbstractModel):
    """DescribeSavingPlanDeduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 每页数量，最大值为200
        :type Limit: int
        :param _StartEndDate: 节省计划使用开始的查询结束时间
        :type StartEndDate: str
        :param _StartStartDate: 节省计划使用开始的查询开始时间
        :type StartStartDate: str
        :param _RegionId: 地域编码
        :type RegionId: int
        :param _ZoneId: 区域编码
        :type ZoneId: int
        :param _SpId: 节省计划资源id
        :type SpId: str
        :param _DeductEndDate: 抵扣查询结束时间，格式：yyyy-MM-dd HH:mm:ss
        :type DeductEndDate: str
        :param _DeductStartDate: 抵扣查询开始时间，格式：yyyy-MM-dd HH:mm:ss
        :type DeductStartDate: str
        :param _EndEndDate: 节省计划使用结束的查询结束时间
        :type EndEndDate: str
        :param _EndStartDate: 节省计划使用结束的查询开始时间
        :type EndStartDate: str
        """
        self._Offset = None
        self._Limit = None
        self._StartEndDate = None
        self._StartStartDate = None
        self._RegionId = None
        self._ZoneId = None
        self._SpId = None
        self._DeductEndDate = None
        self._DeductStartDate = None
        self._EndEndDate = None
        self._EndStartDate = None

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
    def StartEndDate(self):
        return self._StartEndDate

    @StartEndDate.setter
    def StartEndDate(self, StartEndDate):
        self._StartEndDate = StartEndDate

    @property
    def StartStartDate(self):
        return self._StartStartDate

    @StartStartDate.setter
    def StartStartDate(self, StartStartDate):
        self._StartStartDate = StartStartDate

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SpId(self):
        return self._SpId

    @SpId.setter
    def SpId(self, SpId):
        self._SpId = SpId

    @property
    def DeductEndDate(self):
        return self._DeductEndDate

    @DeductEndDate.setter
    def DeductEndDate(self, DeductEndDate):
        self._DeductEndDate = DeductEndDate

    @property
    def DeductStartDate(self):
        return self._DeductStartDate

    @DeductStartDate.setter
    def DeductStartDate(self, DeductStartDate):
        self._DeductStartDate = DeductStartDate

    @property
    def EndEndDate(self):
        return self._EndEndDate

    @EndEndDate.setter
    def EndEndDate(self, EndEndDate):
        self._EndEndDate = EndEndDate

    @property
    def EndStartDate(self):
        return self._EndStartDate

    @EndStartDate.setter
    def EndStartDate(self, EndStartDate):
        self._EndStartDate = EndStartDate


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartEndDate = params.get("StartEndDate")
        self._StartStartDate = params.get("StartStartDate")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._SpId = params.get("SpId")
        self._DeductEndDate = params.get("DeductEndDate")
        self._DeductStartDate = params.get("DeductStartDate")
        self._EndEndDate = params.get("EndEndDate")
        self._EndStartDate = params.get("EndStartDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSavingPlanDeductResponse(AbstractModel):
    """DescribeSavingPlanDeduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 查询命中的节省计划抵扣明细数据总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Deducts: 查询命中的节省计划抵扣明细数据明细
        :type Deducts: list of SavingPlanDeductDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Deducts = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Deducts(self):
        return self._Deducts

    @Deducts.setter
    def Deducts(self, Deducts):
        self._Deducts = Deducts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Deducts") is not None:
            self._Deducts = []
            for item in params.get("Deducts"):
                obj = SavingPlanDeductDetail()
                obj._deserialize(item)
                self._Deducts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSavingPlanOverviewRequest(AbstractModel):
    """DescribeSavingPlanOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDate: 开始时间，格式yyyy-MM-dd 注：查询范围请勿超过6个月
        :type StartDate: str
        :param _EndDate: 结束时间，格式yyyy-MM-dd
        :type EndDate: str
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 每页数量，最大值为200
        :type Limit: int
        """
        self._StartDate = None
        self._EndDate = None
        self._Offset = None
        self._Limit = None

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


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSavingPlanOverviewResponse(AbstractModel):
    """DescribeSavingPlanOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Overviews: 节省计划总览明细数据	
注意：此字段可能返回 null，表示取不到有效值。
        :type Overviews: list of SavingPlanOverviewDetail
        :param _Total: 查询命中的节省计划总览明细数据总条数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Overviews = None
        self._Total = None
        self._RequestId = None

    @property
    def Overviews(self):
        return self._Overviews

    @Overviews.setter
    def Overviews(self, Overviews):
        self._Overviews = Overviews

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
        if params.get("Overviews") is not None:
            self._Overviews = []
            for item in params.get("Overviews"):
                obj = SavingPlanOverviewDetail()
                obj._deserialize(item)
                self._Overviews.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeSavingPlanUsageRequest(AbstractModel):
    """DescribeSavingPlanUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDate: 开始时间，格式yyyy-MM-dd 注：查询范围请勿超过6个月
        :type StartDate: str
        :param _EndDate: 结束时间，格式yyyy-MM-dd
        :type EndDate: str
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 每页数量，最大值为200
        :type Limit: int
        :param _TimeInterval: 查询结果数据的时间间隔
        :type TimeInterval: str
        """
        self._StartDate = None
        self._EndDate = None
        self._Offset = None
        self._Limit = None
        self._TimeInterval = None

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
    def TimeInterval(self):
        return self._TimeInterval

    @TimeInterval.setter
    def TimeInterval(self, TimeInterval):
        self._TimeInterval = TimeInterval


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TimeInterval = params.get("TimeInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSavingPlanUsageResponse(AbstractModel):
    """DescribeSavingPlanUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 查询命中的节省计划总览明细数据总条数
        :type Total: int
        :param _Usages: 节省计划使用率数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Usages: list of SavingPlanUsageDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Usages = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Usages(self):
        return self._Usages

    @Usages.setter
    def Usages(self, Usages):
        self._Usages = Usages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Usages") is not None:
            self._Usages = []
            for item in params.get("Usages"):
                obj = SavingPlanUsageDetail()
                obj._deserialize(item)
                self._Usages.append(obj)
        self._RequestId = params.get("RequestId")


class SavingPlanDeductDetail(AbstractModel):
    """节省计划抵扣明细

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 账号id
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _OwnerUinName: 账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUinName: str
        :param _PayerUin: 抵扣账号id
注意：此字段可能返回 null，表示取不到有效值。
        :type PayerUin: str
        :param _PayerUinName: 抵扣账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayerUinName: str
        :param _SpId: 节省计划资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type SpId: str
        :param _ProductCode: 产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param _ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _SubProductCode: 子产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProductCode: str
        :param _SubProductName: 子产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProductName: str
        :param _OutTradeNo: 交易ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OutTradeNo: str
        :param _RegionId: 地域id
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _RegionName: 地域名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param _ZoneId: 地区id
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _ZoneName: 地区名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneName: str
        :param _SpStartTime: 开始使用时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SpStartTime: str
        :param _SpEndTime: 结束使用时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SpEndTime: str
        :param _DeductTime: 折扣时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductTime: str
        :param _DeductAmount: 抵扣金额，单位分
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductAmount: str
        :param _DeductDiscount: 抵扣折扣率
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductDiscount: str
        :param _DeductRate: 抵扣比率
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductRate: str
        """
        self._OwnerUin = None
        self._OwnerUinName = None
        self._PayerUin = None
        self._PayerUinName = None
        self._SpId = None
        self._ProductCode = None
        self._ProductName = None
        self._SubProductCode = None
        self._SubProductName = None
        self._OutTradeNo = None
        self._RegionId = None
        self._RegionName = None
        self._ZoneId = None
        self._ZoneName = None
        self._SpStartTime = None
        self._SpEndTime = None
        self._DeductTime = None
        self._DeductAmount = None
        self._DeductDiscount = None
        self._DeductRate = None

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OwnerUinName(self):
        return self._OwnerUinName

    @OwnerUinName.setter
    def OwnerUinName(self, OwnerUinName):
        self._OwnerUinName = OwnerUinName

    @property
    def PayerUin(self):
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def PayerUinName(self):
        return self._PayerUinName

    @PayerUinName.setter
    def PayerUinName(self, PayerUinName):
        self._PayerUinName = PayerUinName

    @property
    def SpId(self):
        return self._SpId

    @SpId.setter
    def SpId(self, SpId):
        self._SpId = SpId

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductCode(self):
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def SubProductName(self):
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def OutTradeNo(self):
        return self._OutTradeNo

    @OutTradeNo.setter
    def OutTradeNo(self, OutTradeNo):
        self._OutTradeNo = OutTradeNo

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
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def SpStartTime(self):
        return self._SpStartTime

    @SpStartTime.setter
    def SpStartTime(self, SpStartTime):
        self._SpStartTime = SpStartTime

    @property
    def SpEndTime(self):
        return self._SpEndTime

    @SpEndTime.setter
    def SpEndTime(self, SpEndTime):
        self._SpEndTime = SpEndTime

    @property
    def DeductTime(self):
        return self._DeductTime

    @DeductTime.setter
    def DeductTime(self, DeductTime):
        self._DeductTime = DeductTime

    @property
    def DeductAmount(self):
        return self._DeductAmount

    @DeductAmount.setter
    def DeductAmount(self, DeductAmount):
        self._DeductAmount = DeductAmount

    @property
    def DeductDiscount(self):
        return self._DeductDiscount

    @DeductDiscount.setter
    def DeductDiscount(self, DeductDiscount):
        self._DeductDiscount = DeductDiscount

    @property
    def DeductRate(self):
        return self._DeductRate

    @DeductRate.setter
    def DeductRate(self, DeductRate):
        self._DeductRate = DeductRate


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._OwnerUinName = params.get("OwnerUinName")
        self._PayerUin = params.get("PayerUin")
        self._PayerUinName = params.get("PayerUinName")
        self._SpId = params.get("SpId")
        self._ProductCode = params.get("ProductCode")
        self._ProductName = params.get("ProductName")
        self._SubProductCode = params.get("SubProductCode")
        self._SubProductName = params.get("SubProductName")
        self._OutTradeNo = params.get("OutTradeNo")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._SpStartTime = params.get("SpStartTime")
        self._SpEndTime = params.get("SpEndTime")
        self._DeductTime = params.get("DeductTime")
        self._DeductAmount = params.get("DeductAmount")
        self._DeductDiscount = params.get("DeductDiscount")
        self._DeductRate = params.get("DeductRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SavingPlanOverviewDetail(AbstractModel):
    """节省计划总览明细数据

    """

    def __init__(self):
        r"""
        :param _SpType: 节省计划类型
        :type SpType: str
        :param _PayAmount: 支付金额（单位：元）
        :type PayAmount: str
        :param _StartTime: 开始时间 yyyy-mm-dd HH:mm:ss格式
        :type StartTime: str
        :param _EndTime: 结束时间 yyyy-mm-dd HH:mm:ss格式
        :type EndTime: str
        :param _Status: 状态
        :type Status: int
        :param _SavingAmount: 累计节省金额（单位：元）
        :type SavingAmount: str
        :param _Region: 地域
        :type Region: list of str
        :param _PayType: 支付类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PayType: int
        :param _BuyTime: 购买时间 yyyy-mm-dd HH:mm:ss格式
注意：此字段可能返回 null，表示取不到有效值。
        :type BuyTime: str
        """
        self._SpType = None
        self._PayAmount = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._SavingAmount = None
        self._Region = None
        self._PayType = None
        self._BuyTime = None

    @property
    def SpType(self):
        return self._SpType

    @SpType.setter
    def SpType(self, SpType):
        self._SpType = SpType

    @property
    def PayAmount(self):
        return self._PayAmount

    @PayAmount.setter
    def PayAmount(self, PayAmount):
        self._PayAmount = PayAmount

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SavingAmount(self):
        return self._SavingAmount

    @SavingAmount.setter
    def SavingAmount(self, SavingAmount):
        self._SavingAmount = SavingAmount

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def BuyTime(self):
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime


    def _deserialize(self, params):
        self._SpType = params.get("SpType")
        self._PayAmount = params.get("PayAmount")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._SavingAmount = params.get("SavingAmount")
        self._Region = params.get("Region")
        self._PayType = params.get("PayType")
        self._BuyTime = params.get("BuyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SavingPlanUsageDetail(AbstractModel):
    """节省计划使用率数据

    """

    def __init__(self):
        r"""
        :param _SpType: 节省计划类型
        :type SpType: str
        :param _Status: 节省计划状态
        :type Status: int
        :param _DeductAmount: 累计抵扣的金额（单位：元）
        :type DeductAmount: str
        :param _PromiseAmount: 累计承诺消费金额（单位：元）
        :type PromiseAmount: str
        :param _NetSavings: 累计净节省金额（单位：元）
        :type NetSavings: str
        :param _UtilizationRate: 使用率
        :type UtilizationRate: float
        :param _LossAmount: 累计流失金额（单位：元）
        :type LossAmount: str
        :param _DosageAmount: 累计按量计费预期金额（单位：元）
        :type DosageAmount: str
        :param _CostAmount: 累计成本金额（单位：元）
        :type CostAmount: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: list of str
        """
        self._SpType = None
        self._Status = None
        self._DeductAmount = None
        self._PromiseAmount = None
        self._NetSavings = None
        self._UtilizationRate = None
        self._LossAmount = None
        self._DosageAmount = None
        self._CostAmount = None
        self._Region = None

    @property
    def SpType(self):
        return self._SpType

    @SpType.setter
    def SpType(self, SpType):
        self._SpType = SpType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DeductAmount(self):
        return self._DeductAmount

    @DeductAmount.setter
    def DeductAmount(self, DeductAmount):
        self._DeductAmount = DeductAmount

    @property
    def PromiseAmount(self):
        return self._PromiseAmount

    @PromiseAmount.setter
    def PromiseAmount(self, PromiseAmount):
        self._PromiseAmount = PromiseAmount

    @property
    def NetSavings(self):
        return self._NetSavings

    @NetSavings.setter
    def NetSavings(self, NetSavings):
        self._NetSavings = NetSavings

    @property
    def UtilizationRate(self):
        return self._UtilizationRate

    @UtilizationRate.setter
    def UtilizationRate(self, UtilizationRate):
        self._UtilizationRate = UtilizationRate

    @property
    def LossAmount(self):
        return self._LossAmount

    @LossAmount.setter
    def LossAmount(self, LossAmount):
        self._LossAmount = LossAmount

    @property
    def DosageAmount(self):
        return self._DosageAmount

    @DosageAmount.setter
    def DosageAmount(self, DosageAmount):
        self._DosageAmount = DosageAmount

    @property
    def CostAmount(self):
        return self._CostAmount

    @CostAmount.setter
    def CostAmount(self, CostAmount):
        self._CostAmount = CostAmount

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._SpType = params.get("SpType")
        self._Status = params.get("Status")
        self._DeductAmount = params.get("DeductAmount")
        self._PromiseAmount = params.get("PromiseAmount")
        self._NetSavings = params.get("NetSavings")
        self._UtilizationRate = params.get("UtilizationRate")
        self._LossAmount = params.get("LossAmount")
        self._DosageAmount = params.get("DosageAmount")
        self._CostAmount = params.get("CostAmount")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        