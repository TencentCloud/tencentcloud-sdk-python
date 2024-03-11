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