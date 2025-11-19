# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
    r"""CreateSavingPlanOrder请求参数结构体

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
        r"""地域编码
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""区域编码
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PrePayType(self):
        r"""预付费类型
        :rtype: str
        """
        return self._PrePayType

    @PrePayType.setter
    def PrePayType(self, PrePayType):
        self._PrePayType = PrePayType

    @property
    def TimeSpan(self):
        r"""时长
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        r"""时长单位
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def CommodityCode(self):
        r"""商品唯一标识
        :rtype: str
        """
        return self._CommodityCode

    @CommodityCode.setter
    def CommodityCode(self, CommodityCode):
        self._CommodityCode = CommodityCode

    @property
    def PromiseUseAmount(self):
        r"""承诺时长内的小额金额（单位：元）
        :rtype: int
        """
        return self._PromiseUseAmount

    @PromiseUseAmount.setter
    def PromiseUseAmount(self, PromiseUseAmount):
        self._PromiseUseAmount = PromiseUseAmount

    @property
    def SpecifyEffectTime(self):
        r"""节省计划的指定生效时间，若不传则为当前下单时间。传参数格式:"2023-10-01 00:00:00"，仅支持指定日期的0点时刻
        :rtype: str
        """
        return self._SpecifyEffectTime

    @SpecifyEffectTime.setter
    def SpecifyEffectTime(self, SpecifyEffectTime):
        self._SpecifyEffectTime = SpecifyEffectTime

    @property
    def ClientToken(self):
        r"""可重入ID
        :rtype: str
        """
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
    r"""CreateSavingPlanOrder返回参数结构体

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
        r"""订单号
        :rtype: str
        """
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BigDealId = params.get("BigDealId")
        self._RequestId = params.get("RequestId")


class DescribeSavingPlanCoverageRequest(AbstractModel):
    r"""DescribeSavingPlanCoverage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDate: 费用起始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 费用结束日期，格式yyyy-MM-dd
        :type EndDate: str
        :param _Offset: 分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :type Offset: int
        :param _Limit: 数量，最大值为200
        :type Limit: int
        :param _PeriodType: 取值包括1（缺省值）和2，1表示按天统计覆盖率，2表示按月统计覆盖率，此参数仅影响返回的RateSet聚合粒度，不影响返回的DetailSet
        :type PeriodType: int
        """
        self._StartDate = None
        self._EndDate = None
        self._Offset = None
        self._Limit = None
        self._PeriodType = None

    @property
    def StartDate(self):
        r"""费用起始日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""费用结束日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Offset(self):
        r"""分页偏移量，Offset=0表示第一页，如果Limit=100，则Offset=100表示第二页，Offset=200表示第三页，以此类推
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""数量，最大值为200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PeriodType(self):
        r"""取值包括1（缺省值）和2，1表示按天统计覆盖率，2表示按月统计覆盖率，此参数仅影响返回的RateSet聚合粒度，不影响返回的DetailSet
        :rtype: int
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PeriodType = params.get("PeriodType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSavingPlanCoverageResponse(AbstractModel):
    r"""DescribeSavingPlanCoverage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetailSet: 节省计划覆盖率明细数据
        :type DetailSet: list of SavingPlanCoverageDetail
        :param _RateSet: 节省计划覆盖率聚合数据
        :type RateSet: list of SavingPlanCoverageRate
        :param _TotalCount: 查询命中的节省计划覆盖率明细数据总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailSet = None
        self._RateSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DetailSet(self):
        r"""节省计划覆盖率明细数据
        :rtype: list of SavingPlanCoverageDetail
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet

    @property
    def RateSet(self):
        r"""节省计划覆盖率聚合数据
        :rtype: list of SavingPlanCoverageRate
        """
        return self._RateSet

    @RateSet.setter
    def RateSet(self, RateSet):
        self._RateSet = RateSet

    @property
    def TotalCount(self):
        r"""查询命中的节省计划覆盖率明细数据总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
                obj = SavingPlanCoverageDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        if params.get("RateSet") is not None:
            self._RateSet = []
            for item in params.get("RateSet"):
                obj = SavingPlanCoverageRate()
                obj._deserialize(item)
                self._RateSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSavingPlanDeductRequest(AbstractModel):
    r"""DescribeSavingPlanDeduct请求参数结构体

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
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页数量，最大值为200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartEndDate(self):
        r"""节省计划使用开始的查询结束时间
        :rtype: str
        """
        return self._StartEndDate

    @StartEndDate.setter
    def StartEndDate(self, StartEndDate):
        self._StartEndDate = StartEndDate

    @property
    def StartStartDate(self):
        r"""节省计划使用开始的查询开始时间
        :rtype: str
        """
        return self._StartStartDate

    @StartStartDate.setter
    def StartStartDate(self, StartStartDate):
        self._StartStartDate = StartStartDate

    @property
    def RegionId(self):
        r"""地域编码
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""区域编码
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SpId(self):
        r"""节省计划资源id
        :rtype: str
        """
        return self._SpId

    @SpId.setter
    def SpId(self, SpId):
        self._SpId = SpId

    @property
    def DeductEndDate(self):
        r"""抵扣查询结束时间，格式：yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._DeductEndDate

    @DeductEndDate.setter
    def DeductEndDate(self, DeductEndDate):
        self._DeductEndDate = DeductEndDate

    @property
    def DeductStartDate(self):
        r"""抵扣查询开始时间，格式：yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._DeductStartDate

    @DeductStartDate.setter
    def DeductStartDate(self, DeductStartDate):
        self._DeductStartDate = DeductStartDate

    @property
    def EndEndDate(self):
        r"""节省计划使用结束的查询结束时间
        :rtype: str
        """
        return self._EndEndDate

    @EndEndDate.setter
    def EndEndDate(self, EndEndDate):
        self._EndEndDate = EndEndDate

    @property
    def EndStartDate(self):
        r"""节省计划使用结束的查询开始时间
        :rtype: str
        """
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
    r"""DescribeSavingPlanDeduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 查询命中的节省计划抵扣明细数据总条数
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
        r"""查询命中的节省计划抵扣明细数据总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Deducts(self):
        r"""查询命中的节省计划抵扣明细数据明细
        :rtype: list of SavingPlanDeductDetail
        """
        return self._Deducts

    @Deducts.setter
    def Deducts(self, Deducts):
        self._Deducts = Deducts

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""DescribeSavingPlanOverview请求参数结构体

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
        r"""开始时间，格式yyyy-MM-dd 注：查询范围请勿超过6个月
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""结束时间，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页数量，最大值为200
        :rtype: int
        """
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
    r"""DescribeSavingPlanOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Overviews: 节省计划总览明细数据	
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
        r"""节省计划总览明细数据	
        :rtype: list of SavingPlanOverviewDetail
        """
        return self._Overviews

    @Overviews.setter
    def Overviews(self, Overviews):
        self._Overviews = Overviews

    @property
    def Total(self):
        r"""查询命中的节省计划总览明细数据总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""DescribeSavingPlanUsage请求参数结构体

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
        r"""开始时间，格式yyyy-MM-dd 注：查询范围请勿超过6个月
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""结束时间，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页数量，最大值为200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TimeInterval(self):
        r"""查询结果数据的时间间隔
        :rtype: str
        """
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
    r"""DescribeSavingPlanUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 查询命中的节省计划总览明细数据总条数
        :type Total: int
        :param _Usages: 节省计划使用率数据
        :type Usages: list of SavingPlanUsageDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Usages = None
        self._RequestId = None

    @property
    def Total(self):
        r"""查询命中的节省计划总览明细数据总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Usages(self):
        r"""节省计划使用率数据
        :rtype: list of SavingPlanUsageDetail
        """
        return self._Usages

    @Usages.setter
    def Usages(self, Usages):
        self._Usages = Usages

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class SavingPlanCoverageDetail(AbstractModel):
    r"""节省计划覆盖率数据

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源 ID：账单中出账对象 ID，不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID
        :type ResourceId: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _ProductCode: 产品编码
        :type ProductCode: str
        :param _SubProductCode: 子产品编码
        :type SubProductCode: str
        :param _StartDate: 费用起始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 费用结束日期，格式yyyy-MM-dd，目前与StartDate相等
        :type EndDate: str
        :param _SpCoveredAmount: 节省计划覆盖金额（即节省计划支付金额）
        :type SpCoveredAmount: float
        :param _SpUncoveredAmount: 节省计划未覆盖金额（即优惠后总价）
        :type SpUncoveredAmount: float
        :param _TotalRealAmount: 总支出（即节省计划未覆盖金额 + 节省计划覆盖金额）
        :type TotalRealAmount: float
        :param _ExpectedAmount: 按量计费预期金额（即折前价 * 折扣）
        :type ExpectedAmount: float
        :param _SpCoverage: 覆盖率结果，取值[0, 100]
        :type SpCoverage: float
        :param _PayerUinName: 支付者昵称
        :type PayerUinName: str
        :param _OwnerUinName: 使用者昵称
        :type OwnerUinName: str
        :param _PayerUin: 支付者uin
        :type PayerUin: str
        :param _SubBillingItemName: 计费项名称
        :type SubBillingItemName: str
        :param _BillingItemName: 计费细项名称
        :type BillingItemName: str
        :param _SubProductName: 子产品名称
        :type SubProductName: str
        """
        self._ResourceId = None
        self._RegionId = None
        self._ProductCode = None
        self._SubProductCode = None
        self._StartDate = None
        self._EndDate = None
        self._SpCoveredAmount = None
        self._SpUncoveredAmount = None
        self._TotalRealAmount = None
        self._ExpectedAmount = None
        self._SpCoverage = None
        self._PayerUinName = None
        self._OwnerUinName = None
        self._PayerUin = None
        self._SubBillingItemName = None
        self._BillingItemName = None
        self._SubProductName = None

    @property
    def ResourceId(self):
        r"""资源 ID：账单中出账对象 ID，不同产品因资源形态不同，资源内容不完全相同，如云服务器 CVM 为对应的实例 ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def RegionId(self):
        r"""地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ProductCode(self):
        r"""产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        r"""子产品编码
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def StartDate(self):
        r"""费用起始日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""费用结束日期，格式yyyy-MM-dd，目前与StartDate相等
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def SpCoveredAmount(self):
        r"""节省计划覆盖金额（即节省计划支付金额）
        :rtype: float
        """
        return self._SpCoveredAmount

    @SpCoveredAmount.setter
    def SpCoveredAmount(self, SpCoveredAmount):
        self._SpCoveredAmount = SpCoveredAmount

    @property
    def SpUncoveredAmount(self):
        r"""节省计划未覆盖金额（即优惠后总价）
        :rtype: float
        """
        return self._SpUncoveredAmount

    @SpUncoveredAmount.setter
    def SpUncoveredAmount(self, SpUncoveredAmount):
        self._SpUncoveredAmount = SpUncoveredAmount

    @property
    def TotalRealAmount(self):
        r"""总支出（即节省计划未覆盖金额 + 节省计划覆盖金额）
        :rtype: float
        """
        return self._TotalRealAmount

    @TotalRealAmount.setter
    def TotalRealAmount(self, TotalRealAmount):
        self._TotalRealAmount = TotalRealAmount

    @property
    def ExpectedAmount(self):
        r"""按量计费预期金额（即折前价 * 折扣）
        :rtype: float
        """
        return self._ExpectedAmount

    @ExpectedAmount.setter
    def ExpectedAmount(self, ExpectedAmount):
        self._ExpectedAmount = ExpectedAmount

    @property
    def SpCoverage(self):
        r"""覆盖率结果，取值[0, 100]
        :rtype: float
        """
        return self._SpCoverage

    @SpCoverage.setter
    def SpCoverage(self, SpCoverage):
        self._SpCoverage = SpCoverage

    @property
    def PayerUinName(self):
        r"""支付者昵称
        :rtype: str
        """
        return self._PayerUinName

    @PayerUinName.setter
    def PayerUinName(self, PayerUinName):
        self._PayerUinName = PayerUinName

    @property
    def OwnerUinName(self):
        r"""使用者昵称
        :rtype: str
        """
        return self._OwnerUinName

    @OwnerUinName.setter
    def OwnerUinName(self, OwnerUinName):
        self._OwnerUinName = OwnerUinName

    @property
    def PayerUin(self):
        r"""支付者uin
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def SubBillingItemName(self):
        r"""计费项名称
        :rtype: str
        """
        return self._SubBillingItemName

    @SubBillingItemName.setter
    def SubBillingItemName(self, SubBillingItemName):
        self._SubBillingItemName = SubBillingItemName

    @property
    def BillingItemName(self):
        r"""计费细项名称
        :rtype: str
        """
        return self._BillingItemName

    @BillingItemName.setter
    def BillingItemName(self, BillingItemName):
        self._BillingItemName = BillingItemName

    @property
    def SubProductName(self):
        r"""子产品名称
        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._RegionId = params.get("RegionId")
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._SpCoveredAmount = params.get("SpCoveredAmount")
        self._SpUncoveredAmount = params.get("SpUncoveredAmount")
        self._TotalRealAmount = params.get("TotalRealAmount")
        self._ExpectedAmount = params.get("ExpectedAmount")
        self._SpCoverage = params.get("SpCoverage")
        self._PayerUinName = params.get("PayerUinName")
        self._OwnerUinName = params.get("OwnerUinName")
        self._PayerUin = params.get("PayerUin")
        self._SubBillingItemName = params.get("SubBillingItemName")
        self._BillingItemName = params.get("BillingItemName")
        self._SubProductName = params.get("SubProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SavingPlanCoverageRate(AbstractModel):
    r"""节省计划覆盖率聚合数据

    """

    def __init__(self):
        r"""
        :param _DatePoint: 聚合时间维度，按天聚合格式为yyyy-MM-dd，按月聚合格式为yyyy-MM
        :type DatePoint: str
        :param _Rate: 覆盖率结果，取值[0, 100]
        :type Rate: float
        """
        self._DatePoint = None
        self._Rate = None

    @property
    def DatePoint(self):
        r"""聚合时间维度，按天聚合格式为yyyy-MM-dd，按月聚合格式为yyyy-MM
        :rtype: str
        """
        return self._DatePoint

    @DatePoint.setter
    def DatePoint(self, DatePoint):
        self._DatePoint = DatePoint

    @property
    def Rate(self):
        r"""覆盖率结果，取值[0, 100]
        :rtype: float
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate


    def _deserialize(self, params):
        self._DatePoint = params.get("DatePoint")
        self._Rate = params.get("Rate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SavingPlanDeductDetail(AbstractModel):
    r"""节省计划抵扣明细

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 账号id
        :type OwnerUin: str
        :param _OwnerUinName: 账号名称
        :type OwnerUinName: str
        :param _PayerUin: 抵扣账号id
        :type PayerUin: str
        :param _PayerUinName: 抵扣账号名称
        :type PayerUinName: str
        :param _SpId: 节省计划资源id
        :type SpId: str
        :param _ProductCode: 产品编码
        :type ProductCode: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _SubProductCode: 子产品编码
        :type SubProductCode: str
        :param _SubProductName: 子产品名称
        :type SubProductName: str
        :param _OutTradeNo: 交易ID
        :type OutTradeNo: str
        :param _RegionId: 地域id
        :type RegionId: int
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _ZoneId: 地区id
        :type ZoneId: int
        :param _ZoneName: 地区名称
        :type ZoneName: str
        :param _SpStartTime: 开始使用时间
        :type SpStartTime: str
        :param _SpEndTime: 结束使用时间
        :type SpEndTime: str
        :param _DeductTime: 折扣时间
        :type DeductTime: str
        :param _DeductAmount: 抵扣金额，单位分
        :type DeductAmount: str
        :param _DeductDiscount: 抵扣折扣率
        :type DeductDiscount: str
        :param _DeductRate: 抵扣比率
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
        r"""账号id
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OwnerUinName(self):
        r"""账号名称
        :rtype: str
        """
        return self._OwnerUinName

    @OwnerUinName.setter
    def OwnerUinName(self, OwnerUinName):
        self._OwnerUinName = OwnerUinName

    @property
    def PayerUin(self):
        r"""抵扣账号id
        :rtype: str
        """
        return self._PayerUin

    @PayerUin.setter
    def PayerUin(self, PayerUin):
        self._PayerUin = PayerUin

    @property
    def PayerUinName(self):
        r"""抵扣账号名称
        :rtype: str
        """
        return self._PayerUinName

    @PayerUinName.setter
    def PayerUinName(self, PayerUinName):
        self._PayerUinName = PayerUinName

    @property
    def SpId(self):
        r"""节省计划资源id
        :rtype: str
        """
        return self._SpId

    @SpId.setter
    def SpId(self, SpId):
        self._SpId = SpId

    @property
    def ProductCode(self):
        r"""产品编码
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductCode(self):
        r"""子产品编码
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def SubProductName(self):
        r"""子产品名称
        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def OutTradeNo(self):
        r"""交易ID
        :rtype: str
        """
        return self._OutTradeNo

    @OutTradeNo.setter
    def OutTradeNo(self, OutTradeNo):
        self._OutTradeNo = OutTradeNo

    @property
    def RegionId(self):
        r"""地域id
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        r"""地域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneId(self):
        r"""地区id
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        r"""地区名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def SpStartTime(self):
        r"""开始使用时间
        :rtype: str
        """
        return self._SpStartTime

    @SpStartTime.setter
    def SpStartTime(self, SpStartTime):
        self._SpStartTime = SpStartTime

    @property
    def SpEndTime(self):
        r"""结束使用时间
        :rtype: str
        """
        return self._SpEndTime

    @SpEndTime.setter
    def SpEndTime(self, SpEndTime):
        self._SpEndTime = SpEndTime

    @property
    def DeductTime(self):
        r"""折扣时间
        :rtype: str
        """
        return self._DeductTime

    @DeductTime.setter
    def DeductTime(self, DeductTime):
        self._DeductTime = DeductTime

    @property
    def DeductAmount(self):
        r"""抵扣金额，单位分
        :rtype: str
        """
        return self._DeductAmount

    @DeductAmount.setter
    def DeductAmount(self, DeductAmount):
        self._DeductAmount = DeductAmount

    @property
    def DeductDiscount(self):
        r"""抵扣折扣率
        :rtype: str
        """
        return self._DeductDiscount

    @DeductDiscount.setter
    def DeductDiscount(self, DeductDiscount):
        self._DeductDiscount = DeductDiscount

    @property
    def DeductRate(self):
        r"""抵扣比率
        :rtype: str
        """
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
    r"""节省计划总览明细数据

    """

    def __init__(self):
        r"""
        :param _SpId: 节省计划资源id
        :type SpId: str
        :param _SpType: 节省计划类型
        :type SpType: str
        :param _PayAmount: 支付金额（单位：元）
        :type PayAmount: str
        :param _StartTime: 开始时间 yyyy-mm-dd HH:mm:ss格式
        :type StartTime: str
        :param _EndTime: 结束时间 yyyy-mm-dd HH:mm:ss格式
        :type EndTime: str
        :param _Status: 1 生效 2 失效 3 作废
        :type Status: int
        :param _SavingAmount: 累计节省金额（单位：元）
        :type SavingAmount: str
        :param _Region: 地域
        :type Region: list of str
        :param _PayType: 1 全预付 2 部分预付 3 全不预付
        :type PayType: int
        :param _BuyTime: 购买时间 yyyy-mm-dd HH:mm:ss格式
        :type BuyTime: str
        :param _PromiseAmount: 承诺金额
注意：此字段可能返回 null，表示取不到有效值。
        :type PromiseAmount: str
        """
        self._SpId = None
        self._SpType = None
        self._PayAmount = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._SavingAmount = None
        self._Region = None
        self._PayType = None
        self._BuyTime = None
        self._PromiseAmount = None

    @property
    def SpId(self):
        r"""节省计划资源id
        :rtype: str
        """
        return self._SpId

    @SpId.setter
    def SpId(self, SpId):
        self._SpId = SpId

    @property
    def SpType(self):
        r"""节省计划类型
        :rtype: str
        """
        return self._SpType

    @SpType.setter
    def SpType(self, SpType):
        self._SpType = SpType

    @property
    def PayAmount(self):
        r"""支付金额（单位：元）
        :rtype: str
        """
        return self._PayAmount

    @PayAmount.setter
    def PayAmount(self, PayAmount):
        self._PayAmount = PayAmount

    @property
    def StartTime(self):
        r"""开始时间 yyyy-mm-dd HH:mm:ss格式
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间 yyyy-mm-dd HH:mm:ss格式
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""1 生效 2 失效 3 作废
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SavingAmount(self):
        r"""累计节省金额（单位：元）
        :rtype: str
        """
        return self._SavingAmount

    @SavingAmount.setter
    def SavingAmount(self, SavingAmount):
        self._SavingAmount = SavingAmount

    @property
    def Region(self):
        r"""地域
        :rtype: list of str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayType(self):
        r"""1 全预付 2 部分预付 3 全不预付
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def BuyTime(self):
        r"""购买时间 yyyy-mm-dd HH:mm:ss格式
        :rtype: str
        """
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime

    @property
    def PromiseAmount(self):
        r"""承诺金额
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PromiseAmount

    @PromiseAmount.setter
    def PromiseAmount(self, PromiseAmount):
        self._PromiseAmount = PromiseAmount


    def _deserialize(self, params):
        self._SpId = params.get("SpId")
        self._SpType = params.get("SpType")
        self._PayAmount = params.get("PayAmount")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._SavingAmount = params.get("SavingAmount")
        self._Region = params.get("Region")
        self._PayType = params.get("PayType")
        self._BuyTime = params.get("BuyTime")
        self._PromiseAmount = params.get("PromiseAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SavingPlanUsageDetail(AbstractModel):
    r"""节省计划使用率数据

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
        r"""节省计划类型
        :rtype: str
        """
        return self._SpType

    @SpType.setter
    def SpType(self, SpType):
        self._SpType = SpType

    @property
    def Status(self):
        r"""节省计划状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DeductAmount(self):
        r"""累计抵扣的金额（单位：元）
        :rtype: str
        """
        return self._DeductAmount

    @DeductAmount.setter
    def DeductAmount(self, DeductAmount):
        self._DeductAmount = DeductAmount

    @property
    def PromiseAmount(self):
        r"""累计承诺消费金额（单位：元）
        :rtype: str
        """
        return self._PromiseAmount

    @PromiseAmount.setter
    def PromiseAmount(self, PromiseAmount):
        self._PromiseAmount = PromiseAmount

    @property
    def NetSavings(self):
        r"""累计净节省金额（单位：元）
        :rtype: str
        """
        return self._NetSavings

    @NetSavings.setter
    def NetSavings(self, NetSavings):
        self._NetSavings = NetSavings

    @property
    def UtilizationRate(self):
        r"""使用率
        :rtype: float
        """
        return self._UtilizationRate

    @UtilizationRate.setter
    def UtilizationRate(self, UtilizationRate):
        self._UtilizationRate = UtilizationRate

    @property
    def LossAmount(self):
        r"""累计流失金额（单位：元）
        :rtype: str
        """
        return self._LossAmount

    @LossAmount.setter
    def LossAmount(self, LossAmount):
        self._LossAmount = LossAmount

    @property
    def DosageAmount(self):
        r"""累计按量计费预期金额（单位：元）
        :rtype: str
        """
        return self._DosageAmount

    @DosageAmount.setter
    def DosageAmount(self, DosageAmount):
        self._DosageAmount = DosageAmount

    @property
    def CostAmount(self):
        r"""累计成本金额（单位：元）
        :rtype: str
        """
        return self._CostAmount

    @CostAmount.setter
    def CostAmount(self, CostAmount):
        self._CostAmount = CostAmount

    @property
    def Region(self):
        r"""地域
        :rtype: list of str
        """
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
        